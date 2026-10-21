# Rubric coverage: R2.7, R2.4, RB.5, RB.6, R5.2
"""Uncertainty: one-at-a-time tornado, Monte Carlo, and the benchmark comparison (F3, F4, F5; Appendix C).

Run:  python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py
Reads parameters_lca.yaml. Writes:
  results/lca_tornado.csv, results/lca_montecarlo_summary.csv, results/lca_mc_conversion_alt.csv,
  results/lca_uncertainty.md
  results/lca_stages_expected.csv, results/F2_stage_breakdown.png, F3_tornado.png, F4_montecarlo.png, F5_benchmarks.png

Tornado: each ranged parameter set to its low and then its high value, all others central.
Monte Carlo: every ranged parameter drawn independently from its stated distribution (tri = triangular
low/value/high; uniform = low/high), fixed seed, N draws from the YAML. Independence is an assumption: in
reality concrete and steel intensities are positively correlated, which would widen the construction tail
slightly; the construction share is small, so the headline interval is barely affected.
Monte Carlo shares are reported for every scenario (S1, S2, S2b, S3 like-for-like, S3 upper bound, S3 high),
each saving divided by the same draw's S0 life-cycle total, so the T8 shares and the headline share share one basis.
Conversion-heat test (review.md section 6 point 7): the Monte Carlo is re-run with the SAME draws for every other
input and conversion heat (a) held at its sourced central value and (b) log-uniform between its low and high.
"""
import csv
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lca_model import (RESULTS, load_raw, central, varied_names, model, fmt,  # noqa: E402
                       steel_target_saving)
import lca_plot as lp  # noqa: E402

RAW = load_raw()
P0 = central(RAW)
NAMES = varied_names(RAW)
N_UNITS = int(P0["units_initiative"])


def outputs(p):
    b = model(p, "S0", RAW)
    s1 = model(p, "S1", RAW)
    s2 = model(p, "S2", RAW)
    sav2 = (b["concrete_kg"] - s2["concrete_kg"]) / 1000
    sav1 = (b["concrete_kg"] - s1["concrete_kg"]) / 1000
    s2b = model(p, "S2b", RAW)
    sav2b = (b["concrete_kg"] - s2b["concrete_kg"]) / 1000
    steel_b = b["rebar_kg"] + b["plate_kg"]
    s3lo = (steel_b - sum(model(p, "S3lo", RAW)[k] for k in ("rebar_kg", "plate_kg"))) / 1000
    s3hi = (steel_b - sum(model(p, "S3hi", RAW)[k] for k in ("rebar_kg", "plate_kg"))) / 1000
    s3lfl = steel_target_saving(p, RAW)["t_per_unit"]
    life = b["total_t_life"]
    return {"g_per_kwh": b["total_g"], "lc3_saving_t_per_unit": sav2, "lc3_saving_pct": 100 * sav2 / life,
            "slag_saving_t_per_unit": sav1, "slag_saving_pct": 100 * sav1 / life,
            "s2b_saving_t_per_unit": sav2b, "s2b_saving_pct": 100 * sav2b / life,
            "s3_like_for_like_saving_t_per_unit": s3lfl, "s3_like_for_like_saving_pct": 100 * s3lfl / life,
            "s3_upper_bound_saving_t_per_unit": s3lo, "s3_upper_bound_saving_pct": 100 * s3lo / life,
            "s3_high_saving_t_per_unit": s3hi, "s3_high_saving_pct": 100 * s3hi / life,
            "concrete_m3_per_unit": b["vol"]["total"], "target_m3_per_unit": b["vol"]["target"],
            "clipped": b["vol"]["clipped"], "construction_g": b["construction_g"], "fuel_g": b["fuel_g"],
            "mining_g": b["g"]["Fuel: mining and milling"],
            **{"stage::" + k: g for k, g in b["g"].items()}}


BASE = outputs(P0)

# ---------------- tornado ----------------
trows = []
for k in NAMES:
    lo, hi = dict(P0), dict(P0)
    lo[k], hi[k] = float(RAW[k]["low"]), float(RAW[k]["high"])
    o_lo, o_hi = outputs(lo), outputs(hi)
    trows.append({"parameter": k, "low": RAW[k]["low"], "central": RAW[k]["value"], "high": RAW[k]["high"],
                  "unit": RAW[k]["unit"], "status": RAW[k]["status"],
                  "g_at_low": round(o_lo["g_per_kwh"], 4), "g_at_high": round(o_hi["g_per_kwh"], 4),
                  "g_swing": round(abs(o_hi["g_per_kwh"] - o_lo["g_per_kwh"]), 4),
                  "saving_at_low": round(o_lo["lc3_saving_t_per_unit"]), "saving_at_high": round(o_hi["lc3_saving_t_per_unit"]),
                  "saving_swing": round(abs(o_hi["lc3_saving_t_per_unit"] - o_lo["lc3_saving_t_per_unit"])),
                  "label": lp.label(k)})
trows.sort(key=lambda r: -r["g_swing"])
with open(RESULTS / "lca_tornado.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(trows[0].keys()))
    w.writeheader()
    w.writerows(trows)

# ---------------- Monte Carlo ----------------
N = int(P0["mc_draws"])
rng = np.random.default_rng(int(P0["mc_seed"]))
draws = {}
for k in NAMES:
    lo, c, hi = float(RAW[k]["low"]), float(RAW[k]["value"]), float(RAW[k]["high"])
    if RAW[k].get("dist", "tri") == "uniform":
        draws[k] = rng.uniform(lo, hi, N)
    else:
        draws[k] = rng.triangular(lo, c, hi, N)
res = {key: np.empty(N) for key in BASE if key != "clipped"}
clipped = 0
for i in range(N):
    p = dict(P0)
    for k in NAMES:
        p[k] = float(draws[k][i])
    o = outputs(p)
    clipped += int(o.pop("clipped"))
    for key, val in o.items():
        res[key][i] = val
res["lc3_saving_t_units_2_4"] = res["lc3_saving_t_per_unit"] * N_UNITS
res["lc3_minus_slag_t_per_unit"] = res["lc3_saving_t_per_unit"] - res["slag_saving_t_per_unit"]
p_lc3_beats_slag = float(np.mean(res["lc3_minus_slag_t_per_unit"] > 0))

CENTRAL = {k: v for k, v in BASE.items() if k != "clipped"}
CENTRAL["lc3_saving_t_units_2_4"] = BASE["lc3_saving_t_per_unit"] * N_UNITS
CENTRAL["lc3_minus_slag_t_per_unit"] = BASE["lc3_saving_t_per_unit"] - BASE["slag_saving_t_per_unit"]
srows = []
for key, arr in res.items():
    if key.startswith("stage::"):
        continue
    q = np.percentile(arr, [5, 50, 95])
    srows.append({"output": key, "central_case": round(float(CENTRAL[key]), 4), "mean": round(float(arr.mean()), 4),
                  "p5": round(float(q[0]), 4), "p50": round(float(q[1]), 4), "p95": round(float(q[2]), 4)})
with open(RESULTS / "lca_montecarlo_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(srows[0].keys()))
    w.writeheader()
    w.writerows(srows)
S = {r["output"]: r for r in srows}

# ---------------- conversion-heat distribution test (same draws for every other input) ----------------
CH = "conversion_heat_kwh_per_kgU"
ch_lo, ch_c, ch_hi = float(RAW[CH]["low"]), float(RAW[CH]["value"]), float(RAW[CH]["high"])
rng_alt = np.random.default_rng(int(P0["mc_seed"]) + 1)      # separate stream: other inputs' draws are unchanged
ALT_CASES = [
    ("triangular (baseline)", f"triangular {ch_lo:g} / {ch_c:g} / {ch_hi:g} (mode = low)", draws[CH]),
    ("held at central", f"fixed at {ch_c:g} kWh/kg U (Gibon and Hahn Menacho 2023 central, TO VERIFY)", np.full(N, ch_c)),
    ("log-uniform", f"log-uniform {ch_lo:g}-{ch_hi:g} kWh/kg U", np.exp(rng_alt.uniform(np.log(ch_lo), np.log(ch_hi), N))),
]
arows = []
for case, desc, ch_draws in ALT_CASES:
    if case.startswith("triangular"):
        g_arr, pct_arr = res["g_per_kwh"], res["lc3_saving_pct"]
    else:
        g_arr, pct_arr = np.empty(N), np.empty(N)
        for i in range(N):
            p = dict(P0)
            for k in NAMES:
                p[k] = float(draws[k][i])
            p[CH] = float(ch_draws[i])
            b = model(p, "S0", RAW)
            s2 = model(p, "S2", RAW)
            g_arr[i] = b["total_g"]
            pct_arr[i] = 100 * (b["concrete_kg"] - s2["concrete_kg"]) / 1000 / b["total_t_life"]
    q = np.percentile(g_arr, [5, 50, 95])
    qp = np.percentile(pct_arr, [5, 50, 95])
    arows.append({"conversion_heat_case": case, "distribution": desc, "conv_heat_mean_kwh_per_kgU": round(float(np.mean(ch_draws)), 1),
                  "g_mean": round(float(g_arr.mean()), 3), "g_p5": round(float(q[0]), 3), "g_p50": round(float(q[1]), 3),
                  "g_p95": round(float(q[2]), 3), "lc3_share_pct_p50": round(float(qp[1]), 3),
                  "lc3_share_pct_p5": round(float(qp[0]), 3), "lc3_share_pct_p95": round(float(qp[2]), 3)})
with open(RESULTS / "lca_mc_conversion_alt.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(arows[0].keys()))
    w.writeheader()
    w.writerows(arows)

# ---------------- expected-value stage breakdown (means are additive) ----------------
stage_keys = [k for k in res if k.startswith("stage::")]
mean_total = float(res["g_per_kwh"].mean())
st_rows = []
for k in stage_keys:
    arr = res[k]
    st_rows.append({"stage": k[7:], "mode_case_g_per_kwh": round(BASE[k], 4), "mc_mean_g_per_kwh": round(float(arr.mean()), 4),
                    "mc_p5": round(float(np.percentile(arr, 5)), 4), "mc_p95": round(float(np.percentile(arr, 95)), 4),
                    "share_of_mc_mean_pct": round(100 * float(arr.mean()) / mean_total, 1)})
st_rows.sort(key=lambda r: -r["mc_mean_g_per_kwh"])
with open(RESULTS / "lca_stages_expected.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(st_rows[0].keys()))
    w.writeheader()
    w.writerows(st_rows)

# ---------------- markdown ----------------
L = ["Rubric coverage: R2.7, R2.4, RB.5, RB.6\n", "# Uncertainty, generated by `scripts/lca_uncertainty.py`\n",
     f"Monte Carlo: {N:,} draws, seed {int(P0['mc_seed'])}, {len(NAMES)} parameters varied independently "
     "(triangular low/central/high unless the YAML says uniform). "
     f"Draws where the scaled whole-plant concrete fell below the C1 target volume (whole plant set equal to target): {clipped:,} ({100 * clipped / N:.1f}%).\n",
     "## Monte Carlo results (5th, 50th, 95th percentiles)\n",
     "| Output | Central case | Mean | P5 | P50 | P95 |", "|---|---|---|---|---|---|"]
for r in srows:
    L.append(f"| {r['output']} | {r['central_case']} | {r['mean']} | {r['p5']} | {r['p50']} | {r['p95']} |")
L += ["\n## Stage breakdown: mode case and expected value (Monte Carlo mean)\n",
      "| Stage | Mode case g/kWh | MC mean g/kWh | P5 | P95 | Share of mean |", "|---|---|---|---|---|---|"]
for r in st_rows:
    L.append(f"| {r['stage']} | {r['mode_case_g_per_kwh']} | {r['mc_mean_g_per_kwh']} | {r['mc_p5']} | {r['mc_p95']} | {r['share_of_mc_mean_pct']}% |")
L.append(f"| **Total** | {BASE['g_per_kwh']:.3f} | {mean_total:.3f} | | | 100% |")
L.append(f"\nProbability that LC3 (S2) saves more than the slag blend (S1): {100 * p_lc3_beats_slag:.0f}%.\n")
L += ["## Scenario savings and life-cycle shares on the Monte Carlo basis (one basis for Table T8)\n",
      "Each draw's saving is divided by the same draw's S0 life-cycle total. S3 rows are steel sensitivities, not part of C1; "
      "S3 high is negative (adds emissions).\n",
      "| Scenario | Saving t/unit P50 (P5-P95) | Share of life cycle % P50 (P5-P95) | Mode-case share % |", "|---|---|---|---|"]
for lab, key in [("S1 slag blend (C1 fallback)", "slag"), ("S2 LC3 (C1 target binder)", "lc3"), ("S2b LC3 + slag elsewhere", "s2b"),
                 ("S3 like-for-like (target-structure steel)", "s3_like_for_like"), ("S3 upper bound (all steel, EAF sections factors)", "s3_upper_bound"),
                 ("S3 high (world-average steel)", "s3_high")]:
    t, pc = S[f"{key}_saving_t_per_unit"], S[f"{key}_saving_pct"]
    L.append(f"| {lab} | {t['p50']:,.0f} ({t['p5']:,.0f} to {t['p95']:,.0f}) | {pc['p50']:.3f} ({pc['p5']:.3f} to {pc['p95']:.3f}) | {pc['central_case']:.3f} |")
L += ["\n## Conversion-heat distribution test (Table C2 row; review.md section 6 point 7)\n",
      f"Same {N:,} draws for the other {len(NAMES) - 1} inputs; only the conversion-heat distribution changes.\n",
      "| Conversion heat | Mean heat kWh/kg U | Life cycle mean g/kWh | P5 | P50 | P95 | LC3 share P50 % (P5-P95) |",
      "|---|---|---|---|---|---|---|"]
for r in arows:
    L.append(f"| {r['distribution']} | {r['conv_heat_mean_kwh_per_kgU']} | {r['g_mean']} | {r['g_p5']} | {r['g_p50']} | {r['g_p95']} | "
             f"{r['lc3_share_pct_p50']} ({r['lc3_share_pct_p5']}-{r['lc3_share_pct_p95']}) |")
_med = [r["g_p50"] for r in arows]
L.append(f"\nRange of medians across the three conversion-heat assumptions: {min(_med):.2f}-{max(_med):.2f} g CO2e/kWh.\n")
L += ["## Tornado (one at a time), ranked by swing in life-cycle g CO2e/kWh\n",
      "| Parameter | Low | Central | High | Status | g/kWh at low | g/kWh at high | Swing | LC3 saving at low (t) | at high (t) | Swing (t) |",
      "|---|---|---|---|---|---|---|---|---|---|---|"]
for r in trows:
    L.append(f"| {r['label']} (`{r['parameter']}`) | {r['low']} | {r['central']} | {r['high']} | {r['status']} | {r['g_at_low']} | {r['g_at_high']} | "
             f"{r['g_swing']} | {fmt(r['saving_at_low'])} | {fmt(r['saving_at_high'])} | {fmt(r['saving_swing'])} |")
(RESULTS / "lca_uncertainty.md").write_text("\n".join(L) + "\n")

# ---------------- F2 stage breakdown (expected value, mode case marked) ----------------
lp.style()
items = st_rows[::-1]
fig, ax = lp.plt.subplots(figsize=(8.4, 4.8))
def colour(k):
    if "concrete" in k:
        return lp.ORANGE
    if k.startswith("Fuel"):
        return lp.BLUE
    if k.startswith("Construction"):
        return lp.AQUA
    return lp.VIOLET
ax.barh(range(len(items)), [r["mc_mean_g_per_kwh"] for r in items], color=[colour(r["stage"]) for r in items], height=0.62)
ax.plot([r["mode_case_g_per_kwh"] for r in items], range(len(items)), "|", color=lp.INK, ms=13, mew=1.6)
for i, r in enumerate(items):
    x = max(r["mc_mean_g_per_kwh"], r["mode_case_g_per_kwh"])
    ax.text(x + 0.015, i, f"{r['mc_mean_g_per_kwh']:.2f} ({r['share_of_mc_mean_pct']:.0f}%)", va="center", fontsize=8.5, color=lp.INK)
ax.set_yticks(range(len(items)))
ax.set_yticklabels([r["stage"] for r in items], fontsize=8.6)
ax.set_xlabel("g CO2e per kWh delivered")
ax.set_xlim(0, max(max(r["mc_mean_g_per_kwh"], r["mode_case_g_per_kwh"]) for r in items) * 1.3)
ax.grid(axis="y", visible=False)
# no embedded title: the Word caption carries "Figure F2" (review.md section 6 point 9)
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
ax.legend(handles=[Patch(color=lp.BLUE, label="Fuel front end (bottom-up)"), Patch(color=lp.AQUA, label="Construction (bottom-up)"),
                   Patch(color=lp.ORANGE, label="Concrete (where C1 acts)"), Patch(color=lp.VIOLET, label="Literature transfer (EDF 2024)"),
                   Line2D([], [], color=lp.INK, marker="|", ls="none", ms=11, mew=1.6, label=f"Mode case (all inputs central; total {BASE['g_per_kwh']:.1f})")],
          loc="lower right", fontsize=8.3)
lp.save(fig, RESULTS / "F2_stage_breakdown.png",
        f"Bars: Monte Carlo mean per stage ({N:,} draws; means add up to the expected total). Source: this study; inputs parameters_lca.yaml (TO VERIFY).")

# ---------------- F3 tornado ----------------
lp.style()
fig, axes = lp.plt.subplots(1, 2, figsize=(11.5, 5.4))
for ax, key, ckey, title, unit in [
    (axes[0], "g", "g_per_kwh", "(a) Life-cycle intensity", "g CO₂e per kWh (all other inputs at their mode values)"),
    (axes[1], "saving", "lc3_saving_t_per_unit", "(b) LC3 saving per unit", "t CO₂e saved per unit"),
]:
    rows = [r for r in sorted(trows, key=lambda r: -r[f"{key}_swing"]) if r[f"{key}_swing"] > 0][:10][::-1]
    base = BASE[ckey]
    span = max(max(abs(r[f"{key}_at_low"] - base), abs(r[f"{key}_at_high"] - base)) for r in rows)
    for i, r in enumerate(rows):
        lo_v, hi_v = r[f"{key}_at_low"], r[f"{key}_at_high"]
        ax.barh(i, lo_v - base, left=base, color=lp.BLUE, height=0.6)
        ax.barh(i, hi_v - base, left=base, color=lp.ORANGE, height=0.6)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r["label"] for r in rows], fontsize=8.3)
    ax.axvline(base, color=lp.INK, lw=1)
    ax.set_ylim(-0.7, len(rows) - 0.3 + 0.9)
    ax.text(base, len(rows) - 0.2, f"mode case {base:,.2f}" if key == "g" else f"mode case {base:,.0f}",
            ha="center", va="bottom", fontsize=8.5, color=lp.INK, bbox=dict(facecolor="white", edgecolor="none", pad=1.5))
    ax.set_xlim(base - 1.12 * span, base + 1.12 * span)
    ax.set_xlabel(unit)
    ax.grid(axis="y", visible=False)
    ax.set_title(title, fontsize=10)
from matplotlib.patches import Patch  # noqa: E402
fig.legend(handles=[Patch(color=lp.BLUE, label="Parameter at its low value"), Patch(color=lp.ORANGE, label="Parameter at its high value")],
           loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.06))
fig.tight_layout()
lp.save(fig, RESULTS / "F3_tornado.png", "Top 10 inputs per panel, each moved from its low to its high value with all others at their mode (most likely) "
        "values.\nSource: this study, scripts/lca_uncertainty.py; ranges in parameters_lca.yaml.")

# ---------------- F4 Monte Carlo ----------------
fig, axes = lp.plt.subplots(1, 2, figsize=(11.5, 4.2))
for ax, key, xlabel in [(axes[0], "g_per_kwh", "Life-cycle g CO2e/kWh"),
                        (axes[1], "lc3_saving_t_per_unit", "LC3 saving, t CO2e per unit")]:
    arr = res[key]
    ax.hist(arr, bins=80, color=lp.BLUE, edgecolor="white", linewidth=0.3)
    for q, ls in zip(np.percentile(arr, [5, 50, 95]), ["--", "-", "--"]):
        ax.axvline(q, color=lp.INK, lw=1, ls=ls)
        ax.text(q, ax.get_ylim()[1] * 0.97, f" {q:,.2f}" if key == "g_per_kwh" else f" {q:,.0f}", fontsize=8, color=lp.INK, va="top")
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Draws")
    ax.grid(axis="x", visible=False)
axes[0].set_title("Life-cycle intensity (P5, P50, P95 marked)", fontsize=10)
axes[1].set_title("C1 LC3 saving per unit", fontsize=10)
fig.tight_layout()
lp.save(fig, RESULTS / "F4_montecarlo.png", f"Monte Carlo, {N:,} draws, seed {int(P0['mc_seed'])}. Source: this study, scripts/lca_uncertainty.py.")

# ---------------- F5 benchmarks ----------------
# Each row: label, point (None = range only), low, high, colour flag. UNECE reports a range, so no point is drawn (factcheck L66).
# Warner and Heath: median only (the max 110 is off-scale; no minimum is attributed to them, factcheck L31).
# IPCC AR5 Annex III is drawn only once all three bm_ipcc2014_* entries are verified (review.md section 6 point 8).
bm = [("This study (BWRX-300, Darlington), median and 90% interval", S["g_per_kwh"]["p50"], S["g_per_kwh"]["p5"], S["g_per_kwh"]["p95"], True),
      ("EDF (2024), French fleet, central and sensitivity", RAW["bm_edf2024"]["value"], RAW["bm_edf2024"]["low"], RAW["bm_edf2024"]["high"], False),
      ("UNECE (2021), nuclear range", None, RAW["bm_unece2021_low"]["value"], RAW["bm_unece2021_high"]["value"], False),
      ("Gibon & Hahn Menacho (2023), global 2020", RAW["bm_gibon2023"]["value"], RAW["bm_gibon2023"]["value"], RAW["bm_gibon2023"]["value"], False),
      ("Carless et al. (2016), Westinghouse SMR, mean and 90% CI", RAW["bm_carless2016_wsmr"]["value"], RAW["bm_carless2016_wsmr"]["low"], RAW["bm_carless2016_wsmr"]["high"], False),
      ("Warner & Heath (2012), harmonised LWR median", RAW["bm_warner2012"]["value"], RAW["bm_warner2012"]["value"], RAW["bm_warner2012"]["value"], False)]
IPCC_KEYS = ("bm_ipcc2014_min", "bm_ipcc2014_median", "bm_ipcc2014_max")
ipcc_ok = all(RAW[k]["status"] == "verified" for k in IPCC_KEYS)
if ipcc_ok:
    bm.append(("IPCC AR5 WGIII Annex III, nuclear median (min-max)", RAW["bm_ipcc2014_median"]["value"], RAW["bm_ipcc2014_min"]["value"],
               RAW["bm_ipcc2014_max"]["value"], False))
XMAX = 17
fig, ax = lp.plt.subplots(figsize=(8.6, 3.9))
for i, (lab, c, lo, hi, ours) in enumerate(bm[::-1]):
    col = lp.ORANGE if ours else lp.BLUE
    hi_d = min(hi, XMAX - 0.6)
    ax.plot([lo, hi_d], [i, i], color=col, lw=2.2, solid_capstyle="round")
    if hi > XMAX - 0.6:
        ax.annotate("", xy=(XMAX - 0.3, i), xytext=(hi_d, i), arrowprops=dict(arrowstyle="->", color=col, lw=1.5))
    if c is not None:
        ax.plot([c], [i], "o", color=col, ms=8, mec="white", mew=1.5)
        txt = f"{c:.1f}" + (f" ({lo:.1f}-{hi:.1f})" if hi > lo else "")
    else:
        txt = f"{lo:.1f}-{hi:.1f} (range only)"
    ax.text(min(hi, XMAX - 0.3) + 0.25, i, txt, va="center", fontsize=8.5, color=lp.INK)
ax.set_yticks(range(len(bm)))
ax.set_yticklabels([b[0] for b in bm[::-1]], fontsize=8.6)
ax.set_xlim(0, XMAX + 0.5)
ax.set_xticks(np.arange(0, XMAX + 0.1, 2.5))
ax.set_xlabel("Life-cycle g CO₂e per kWh (dot = central, mean or median; line = range or interval)")
ax.grid(axis="y", visible=False)
# no embedded title: the Word caption carries "Figure F5" (review.md section 6 point 9)
fig.text(0.01, -0.13,
        "Benchmarks are search leads [TO VERIFY]. Off-scale and not drawn: Warner & Heath maximum 110; Gibon scenario range 5.4-122.\n"
        "Coal about 750-1,100 and gas CC 403-513 g/kWh (UNECE 2021). " + ("" if ipcc_ok else "IPCC AR5 Annex III added once verified."),
         fontsize=7.5, color=lp.MUTED, ha="left", va="bottom")
lp.save(fig, RESULTS / "F5_benchmarks.png")

g = S["g_per_kwh"]
s = S["lc3_saving_t_per_unit"]
print(f"MC {N:,}: g/kWh P50 {g['p50']:.2f} (P5 {g['p5']:.2f}, P95 {g['p95']:.2f}); LC3 saving t/unit P50 {s['p50']:,.0f} "
      f"(P5 {s['p5']:,.0f}, P95 {s['p95']:,.0f}); P(LC3 > slag) {100 * p_lc3_beats_slag:.0f}%; clipped {clipped}")
print("Top tornado (g/kWh):", ", ".join(f"{r['parameter']} {r['g_swing']}" for r in trows[:6]))
