# Rubric coverage: R3.2, R2.1, R2.3, R2.4, R2.7, R1.3, R3.8, RB.5
"""Herfindahl-Hirschman index (HHI) for the BWRX-300 fuel supply chain.

Stages: uranium mining (by country, and a bounded estimate by company), conversion (by company)
and enrichment (by company). Sensitivity: with and without Russia (sanctions/ban scenario),
without Russia and China (market open to a Western buyer), data year, treatment of the
"Other" rows, an alternative ConverDyn capacity, and alternative enrichment-capacity sources (CRAI, WNU).
Run 7b (21/10/2026) added section 6: Darlington's four-unit fuel demand (tU and tSWU per year, from
parameters_lca.yaml, read-only) set against supplier capacity, plus a two-reload strategic reserve.

Method
  share_i = 100 * q_i / sum(q)                      (percent)
  HHI     = sum(share_i ** 2)                       (0 to 10,000)
  N_eq    = 10,000 / HHI                            (equivalent number of equal-sized suppliers)
  "Without X": X's quantity is removed and shares are renormalised over the remaining suppliers,
  i.e. the market a buyer barred from X can still draw on (capacity is assumed not to expand).
  Residual / "Other" rows: upper bound treats the row as one supplier; lower bound treats it as
  infinitely many small suppliers (contributes ~0 to HHI).

Inputs : 03_LCA_Calculations/parameters_run3.yaml; parameters_lca.yaml (fuel-cycle inputs, read-only)
Outputs: 03_LCA_Calculations/results/hhi.md, results/hhi_summary.csv
Run    : python3 -I 03_LCA_Calculations/scripts/hhi.py
"""
from __future__ import annotations

import csv
import math
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PARAMS = ROOT / "parameters_run3.yaml"
PARAMS_LCA = ROOT / "parameters_lca.yaml"
RESULTS = ROOT / "results"


def load() -> dict:
    with PARAMS.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_lca() -> dict:
    with PARAMS_LCA.open(encoding="utf-8") as f:
        return yaml.safe_load(f)["parameters"]


def value_fn(x: float) -> float:
    """Separative potential V(x) = (2x - 1) ln(x / (1 - x)); same as lca_model.py."""
    return (2 * x - 1) * math.log(x / (1 - x))


def fuel_year(v: dict[str, float]) -> dict[str, float]:
    """Annual fuel demand of ONE unit. Same enrichment balance as lca_model.py / lca_baseline.md.

    eta = net MWe / MWt; kWh_e per kg enriched U = burnup x 24,000 x eta;
    feed F = (xp - xt)/(xf - xt); SWU per kg EU = V(xp) + (F - 1) V(xt) - F V(xf).
    """
    eta = v["net_mwe"] / v["thermal_mwt"]
    mwh = v["net_mwe"] * 8760 * v["capacity_factor"]
    kwh_per_kg = v["burnup_gwd_per_t"] * 24000 * eta
    enc_t = mwh * 1000 / kwh_per_kg / 1000            # t enriched U per year
    xp, xf, xt = (v[k] / 100 for k in ("enrichment_pct", "feed_assay_pct", "tails_assay_pct"))
    feed = (xp - xt) / (xf - xt)
    swu_kg = value_fn(xp) + (feed - 1) * value_fn(xt) - feed * value_fn(xf)
    return {"mwh": mwh, "enc_t": enc_t, "natU_t": enc_t * feed, "tSWU": enc_t * swu_kg,
            "feed": feed, "swu_per_kg": swu_kg}


def shares(q: dict[str, float]) -> dict[str, float]:
    total = sum(q.values())
    return {k: 100.0 * v / total for k, v in q.items()}


def hhi(q: dict[str, float], atomistic: tuple[str, ...] = ()) -> float:
    """HHI in points. Keys in `atomistic` count towards the total but add ~0 to the sum of squares."""
    s = shares(q)
    return sum(v ** 2 for k, v in s.items() if k not in atomistic)


def drop(q: dict[str, float], *keys: str) -> dict[str, float]:
    return {k: v for k, v in q.items() if k not in keys}


def classify(h: float, t: dict) -> tuple[str, str]:
    t23 = t["doj_ftc_2023_highly_concentrated"]["value"]
    lo10 = t["doj_ftc_2010_unconcentrated_below"]["value"]
    hi10 = t["doj_ftc_2010_highly_concentrated"]["value"]
    c2023 = "highly concentrated" if h > t23 else "not highly concentrated"
    if h < lo10:
        c2010 = "unconcentrated"
    elif h <= hi10:
        c2010 = "moderately concentrated"
    else:
        c2010 = "highly concentrated"
    return c2023, c2010


def share_table(q: dict[str, float], unit: str) -> list[str]:
    s = shares(q)
    rows = [f"| Supplier | {unit} | Share (%) | Share² |", "|---|---:|---:|---:|"]
    for k, v in sorted(q.items(), key=lambda kv: -kv[1]):
        rows.append(f"| {k} | {v:,.0f} | {s[k]:.2f} | {s[k] ** 2:,.1f} |")
    rows.append(f"| **Total / HHI** | {sum(q.values()):,.0f} | 100.00 | **{sum(x ** 2 for x in s.values()):,.0f}** |")
    return rows


def main() -> None:
    p = load()
    t = p["thresholds"]
    out: list[str] = []
    summary: list[dict] = []

    def record(stage: str, scenario: str, h: float, note: str = "") -> None:
        c23, c10 = classify(h, t)
        summary.append({"stage": stage, "scenario": scenario, "hhi": round(h),
                        "n_equivalent": round(10000 / h, 1), "doj_ftc_2023": c23,
                        "doj_ftc_2010": c10, "note": note})

    # ---------------- Mining by country ----------------
    m = p["mining_by_country"]
    m24 = {k: float(v) for k, v in m[2024].items()}
    listed_sum = sum(m24.values())
    assert abs(listed_sum - m["world_total"][2024]) < 1, "2024 rows do not sum to world total"

    record("Mining (country)", "2024 base", hhi(m24))
    record("Mining (country)", "2024 base, 'Others' atomistic", hhi(m24, ("Others",)), "lower bound")
    record("Mining (country)", "2024 without Russia", hhi(drop(m24, "Russia")))
    record("Mining (country)", "2024 without Russia and China", hhi(drop(m24, "Russia", "China")))
    record("Mining (country)", "2024 without Russia, China and Niger", hhi(drop(m24, "Russia", "China", "Niger")),
           "Niger: exports disrupted since the 2023 coup (Orano/Somair; secondary)")

    year_rows = []
    for yr in (2022, 2023):
        q = {k: float(v) for k, v in m[yr].items()}
        resid = m["world_total"][yr] - sum(q.values())
        q["Rest of world (residual)"] = resid
        hi_b = hhi(q)
        lo_b = hhi(q, ("Rest of world (residual)",))
        year_rows.append((yr, resid, lo_b, hi_b, shares(q)["Russia"]))
        record("Mining (country)", f"{yr} (residual bounds)", (lo_b + hi_b) / 2,
               f"range {lo_b:,.0f} to {hi_b:,.0f}")
        q_nr = drop(q, "Russia")
        record("Mining (country)", f"{yr} without Russia (residual bounds)",
               (hhi(q_nr) + hhi(q_nr, ("Rest of world (residual)",))) / 2,
               f"range {hhi(q_nr, ('Rest of world (residual)',)):,.0f} to {hhi(q_nr):,.0f}")

    # Mining by company (bounded; only top three shares known)
    mc = p["mining_by_company_2024_pct"]
    known = {k: float(v) for k, v in mc.items() if k not in ("source", "verified")}
    rest = 100.0 - sum(known.values())
    lo_c = sum(v ** 2 for v in known.values())
    cap = min(known.values())  # remaining firms are each no larger than the third-ranked firm
    n_full, rem = divmod(rest, cap)
    hi_c = lo_c + n_full * cap ** 2 + rem ** 2
    record("Mining (company)", "2024 bounds (top 3 known)", (lo_c + hi_c) / 2,
           f"range {lo_c:,.0f} to {hi_c:,.0f}; STRETCH, partial data")

    # ---------------- Conversion ----------------
    cv = p["conversion_by_company"]
    cap_q = {k: float(v) for k, v in cv["capacity"].items()}
    prod_q = {k: float(v) for k, v in cv["production"].items()}
    alt_q = dict(cap_q, ConverDyn=float(cv["converdyn_capacity_alt"]["value"]))
    record("Conversion", "capacity base", hhi(cap_q))
    record("Conversion", "capacity without Russia", hhi(drop(cap_q, "Rosatom")))
    record("Conversion", "capacity without Russia and China", hhi(drop(cap_q, "Rosatom", "CNNC")),
           "market open to a Western buyer")
    record("Conversion", "production base", hhi(prod_q))
    record("Conversion", "production without Russia", hhi(drop(prod_q, "Rosatom")))
    record("Conversion", "capacity, ConverDyn 15,000 tU (alt.)", hhi(alt_q), "secondary source; sensitivity only")
    record("Conversion", "ConverDyn alt., without Russia", hhi(drop(alt_q, "Rosatom")))
    record("Conversion", "ConverDyn alt., without Russia and China", hhi(drop(alt_q, "Rosatom", "CNNC")))

    # ---------------- Enrichment ----------------
    en = p["enrichment_by_company"]
    oth = ("Other_INB_JNFL",)
    enr = {yr: {k: float(v) for k, v in en[yr].items()} for yr in (2022, 2025, 2030)}
    for yr, q in enr.items():
        assert abs(sum(q.values()) - en["stated_total"][yr]) <= 1.5, f"{yr} enrichment rows != total"
        tag = "base" if yr == 2025 else "year sensitivity"
        record("Enrichment", f"{yr} capacity ({tag})", hhi(q), f"Other atomistic: {hhi(q, oth):,.0f}")
        record("Enrichment", f"{yr} without Russia", hhi(drop(q, "Rosatom")),
               f"Other atomistic: {hhi(drop(q, 'Rosatom'), oth):,.0f}")
        record("Enrichment", f"{yr} without Russia and China", hhi(drop(q, "Rosatom", "CNNC")),
               f"market open to a Western buyer; Other atomistic: {hhi(drop(q, 'Rosatom', 'CNNC'), oth):,.0f}")

    # Alternative enrichment-capacity sources (run 7b; R1.3). Replace only the named companies.
    alt_rows = []
    for key, spec in p["enrichment_alt_sources"].items():
        q = dict(enr[2025], **{k: float(v) for k, v in spec["replaces"].items()})
        h_alt = hhi(q)
        alt_rows.append((key, spec, h_alt, shares(q)["Rosatom"], sum(q.values())))
        record("Enrichment", f"2025 capacity, {key} values for {', '.join(spec['replaces'])}", h_alt,
               f"Russia {shares(q)['Rosatom']:.1f}%; source {spec['source']} (unverified)")
    ru_range = sorted([r[3] for r in alt_rows] + [shares(enr[2025])["Rosatom"]])

    # ---------------- Key shares ----------------
    s_m24 = shares(m24)
    s_cv = shares(cap_q)
    s_cv_w = shares(drop(cap_q, "Rosatom", "CNNC"))
    s_en = {yr: shares(q) for yr, q in enr.items()}
    s_en_w = shares(drop(enr[2025], "Rosatom", "CNNC"))
    au = p["australia"]
    req = p["world_reactor_requirements_2025_tU"]["value"]
    mine_cover = 100 * m["world_total"][2024] / req

    # ---------------- Write markdown ----------------
    out += [
        "Rubric coverage: R3.2, R2.1, R2.4, R2.7, R3.8, R3.5, RB.5",
        "",
        "# HHI for the BWRX-300 fuel supply chain (Appendix B working)",
        "",
        "Generated by `03_LCA_Calculations/scripts/hhi.py` from `parameters_run3.yaml`. Do not edit by hand; "
        "rerun the script after changing a parameter.",
        "",
        "> **Verification status: NOT YET CITABLE.** Every input was taken from search-engine extracts of the "
        "named World Nuclear Association, NEA/IAEA and US government pages, because none of those hosts could be "
        "opened from the analyst's session. Internal checks passed (2024 mining rows sum exactly to the world "
        "total of 60,213 tU; conversion and enrichment rows sum to their stated totals). Victor or the "
        "fact-checker must open each page, confirm the numbers and set `verified: true` before any value goes "
        "into the report or slides.",
        "",
        "## 1. Method",
        "",
        "- Share of supplier *i*: s_i = 100 × q_i / Σq (percent). HHI = Σ s_i² (0 to 10,000). "
        "Equivalent number of equal suppliers N_eq = 10,000 / HHI.",
        "- Mining is measured by country (2024 mine output, tU); conversion by company (licensed capacity, "
        "tU as UF₆ per year; production as a check); enrichment by company (capacity, thousand SWU per year, "
        "2025 base, 2022 and 2030 as sensitivity).",
        "- \"Without Russia\": Russian supply is removed and shares are renormalised over the rest, i.e. the "
        "market left to a buyer barred from Russian material, with no new capacity. \"Without Russia and China\": "
        "also removes CNNC, whose enrichment capacity WNA estimates on the assumption that it serves China's own "
        "fleet; this approximates the market open to a Canadian or Australian utility.",
        "- Rows of \"Others\" or a residual are bounded: one supplier (upper bound) vs many small suppliers "
        "(lower bound, ~0). The difference is below 3 points in every 2024/2025 case.",
        "- Thresholds: US DOJ and FTC (2023) *Merger Guidelines*: HHI > 1,800 is highly concentrated. "
        "The superseded 2010 *Horizontal Merger Guidelines*: < 1,500 unconcentrated, 1,500–2,500 moderately "
        "concentrated, > 2,500 highly concentrated. Both are reported because the mining result falls between "
        "them. These are antitrust screens for merger review; here they are used as a recognised scale for supply "
        "concentration, not as a legal test.",
        "",
        "## 2. Headline results",
        "",
        "| Stage (2024/2025 base) | HHI | 2023 guideline | 2010 guideline | Without Russia | Without Russia and China |",
        "|---|---:|---|---|---:|---:|",
    ]

    def get(stage: str, scen: str) -> dict:
        return next(r for r in summary if r["stage"] == stage and r["scenario"] == scen)

    for stage, base, nr, nrc in [
        ("Mining (country)", "2024 base", "2024 without Russia", "2024 without Russia and China"),
        ("Conversion", "capacity base", "capacity without Russia", "capacity without Russia and China"),
        ("Enrichment", "2025 capacity (base)", "2025 without Russia", "2025 without Russia and China"),
    ]:
        b, r1, r2 = get(stage, base), get(stage, nr), get(stage, nrc)
        out.append(f"| {stage} | **{b['hhi']:,}** | {b['doj_ftc_2023']} | {b['doj_ftc_2010']} | "
                   f"{r1['hhi']:,} ({r1['doj_ftc_2010']} under 2010) | {r2['hhi']:,} |")

    out += [
        "",
        f"- Russia's share: mining {s_m24['Russia']:.1f}% (country output, 2024); conversion "
        f"{s_cv['Rosatom']:.1f}% (capacity); enrichment **{s_en[2025]['Rosatom']:.1f}%** (2025 capacity; "
        f"{s_en[2022]['Rosatom']:.1f}% in 2022; {s_en[2030]['Rosatom']:.1f}% planned for 2030). Across the three "
        f"2025 capacity estimates (WNA, WNU, CRAI; section 4) Russia's share is **{ru_range[0]:.1f}–{ru_range[-1]:.1f}%**.",
        "- Removing Russia **raises** the HHI at every stage: the remaining market is smaller and still "
        "dominated by a few suppliers. Under the 2010 scale, 2024 mining moves from moderately to highly "
        "concentrated (the 2023-data case stays just below 2,500; see section 4).",
        f"- Without Russia and China, enrichment is an Urenco–Orano duopoly: Urenco {s_en_w['Urenco']:.1f}%, "
        f"Orano {s_en_w['Orano']:.1f}% (N_eq = {get('Enrichment', '2025 without Russia and China')['n_equivalent']}).",
        f"- Canada (Cameco, Port Hope) holds {s_cv['Cameco']:.1f}% of world conversion capacity and "
        f"{s_cv_w['Cameco']:.1f}% of the capacity open to a Western buyer; Canada mined {s_m24['Canada']:.1f}% of "
        "world uranium in 2024. Canada has no enrichment plant.",
        f"- Australia: {au['share_identified_recoverable_resources_usd130_rb2024']['value']}% of identified "
        "recoverable resources at < USD 130/kgU (Red Book 2024; "
        f"{au['share_identified_recoverable_resources_usd130_rb2026']['value']}% in Red Book 2026 as tabulated "
        f"by WNA, TO VERIFY), but {s_m24['Australia']:.1f}% of 2024 mine output ({au['production_2024_tU']['value']:,} tU) "
        "and 0% of conversion and enrichment capacity.",
        f"- Mine output in 2024 ({m['world_total'][2024]:,} tU) equalled {mine_cover:.0f}% of reactor requirements "
        f"at 1 January 2025 ({req:,} tU, Red Book 2026, TO VERIFY); the rest comes from secondary supply "
        "(inventories, down-blending, re-enriched tails), which this HHI does not cover.",
        "",
        "## 3. Working: shares and squared shares",
        "",
        "### 3.1 Mining by country, 2024 (tU)",
        "",
        *share_table(m24, "tU"),
        "",
        "### 3.2 Mining by country, 2024, without Russia",
        "",
        *share_table(drop(m24, "Russia"), "tU"),
        "",
        "### 3.3 Mining by country, earlier years (only the eight largest rows retrieved; residual bounded)",
        "",
        "| Year | Residual (tU) | HHI lower bound | HHI upper bound | Russia share (%) |",
        "|---|---:|---:|---:|---:|",
    ]
    for yr, resid, lo_b, hi_b, rs in year_rows:
        out.append(f"| {yr} | {resid:,.0f} | {lo_b:,.0f} | {hi_b:,.0f} | {rs:.1f} |")
    out += [
        "",
        "### 3.4 Mining by company, 2024 (STRETCH, partial)",
        "",
        f"Only the top three shares were retrieved: {', '.join(f'{k} {v:.0f}%' for k, v in known.items())} "
        f"(sum {sum(known.values()):.0f}%). Lower bound (remaining {rest:.0f}% atomistic): {lo_c:,.0f}. "
        f"Upper bound (remaining {rest:.0f}% split into firms no larger than the third-ranked, {cap:.0f}%): "
        f"{hi_c:,.0f}. Either way the company-level HHI is below 1,500 (unconcentrated under 2010; "
        "not highly concentrated under 2023): concentration in mining is a **country** (geopolitical) risk, "
        "not a firm-level market-power risk. Kazatomprom's 21% is attributable production; Kazakhstan's 38.6% "
        "country share includes joint ventures with Cameco, Orano, Uranium One (Rosatom) and Chinese partners "
        "[TO VERIFY ownership detail].",
        "",
        "### 3.5 Conversion by company, licensed capacity (tU as UF₆/yr)",
        "",
        *share_table(cap_q, "tU/yr"),
        "",
        "Without Russia:",
        "",
        *share_table(drop(cap_q, "Rosatom"), "tU/yr"),
        "",
        "Without Russia and China:",
        "",
        *share_table(drop(cap_q, "Rosatom", "CNNC"), "tU/yr"),
        "",
        "### 3.6 Enrichment by company, 2025 capacity (thousand SWU/yr)",
        "",
        *share_table(enr[2025], "kSWU/yr"),
        "",
        "Without Russia:",
        "",
        *share_table(drop(enr[2025], "Rosatom"), "kSWU/yr"),
        "",
        "Without Russia and China:",
        "",
        *share_table(drop(enr[2025], "Rosatom", "CNNC"), "kSWU/yr"),
        "",
        "## 4. Sensitivity (all scenarios)",
        "",
        "| Stage | Scenario | HHI | N_eq | 2023 guideline | 2010 guideline | Note |",
        "|---|---|---:|---:|---|---|---|",
    ]
    for r in summary:
        out.append(f"| {r['stage']} | {r['scenario']} | {r['hhi']:,} | {r['n_equivalent']} | "
                   f"{r['doj_ftc_2023']} | {r['doj_ftc_2010']} | {r['note']} |")
    out += [
        "",
        "Reading the sensitivity:",
        "- **Data year** (enrichment 2022 → 2030; mining 2022 → 2024) moves the HHI by a few hundred points but "
        "never changes the 2023-guideline class: enrichment and conversion are highly concentrated in every year.",
        "- **Capacity vs production** (conversion) changes the HHI by less than 10 points.",
        "- **ConverDyn's capacity** (7,000 vs 15,000 tU) is the largest single data uncertainty for conversion; "
        "the higher value lowers the HHI but all conversion cases stay above 1,800.",
        "- **Removing Russia** is the dominant effect at every stage and always increases concentration.",
        "",
        "## 5. Limitations",
        "",
        "- Capacity is not supply: nameplate SWU includes capacity Rosatom uses for underfeeding and tails "
        "re-enrichment, and CNNC's figures are WNA estimates. Secondary supply is excluded.",
        "- Company-level enrichment concentration hides plant location: Urenco operates in the UK, Germany, the "
        "Netherlands and the USA; Orano only in France.",
        "- Mining by country ignores ownership (e.g. Rosatom's Uranium One stakes in Kazakh mines) and transport "
        "routes for Kazakh exports [TO VERIFY]; the company-level bound partly addresses ownership.",
        "- Merger-guideline thresholds are antitrust screens; their use here is an analogy for supply risk.",
        "",
    ]

    # ---------------- 6. Sizing to the proposal (run 7b) ----------------
    lp = load_lca()
    fl = p["fuel_demand_link"]
    n_units = fl["units_at_darlington"]
    base_v = {k: float(lp[k]["value"]) for k in fl["keys"]}
    one = fuel_year(base_v)
    four = {k: one[k] * n_units for k in ("mwh", "enc_t", "natU_t", "tSWU")}
    assert abs(four["natU_t"] - fl["check_four_units_natU_t"]) < 0.1, "natU differs from lca_baseline.md"
    assert abs(four["tSWU"] - fl["check_four_units_tSWU"]) < 0.1, "SWU differs from lca_baseline.md"

    uu = p["urenco_usa"]
    uu_now = uu["capacity_current_kSWU"]["value"]
    uu_2027 = uu_now + uu["expansion_2027_kSWU"]["value"]
    uu_2036 = uu["capacity_after_expansion_kSWU"]["value"]
    west_2025 = enr[2025]["Urenco"] + enr[2025]["Orano"]
    world_2025 = sum(enr[2025].values())
    cameco_conv = cap_q["Cameco"]
    canada_mine = m24["Canada"]

    # One-at-a-time sensitivity on the four-unit demand
    oat = []
    for k in ("capacity_factor", "net_mwe", "burnup_gwd_per_t", "enrichment_pct", "tails_assay_pct"):
        for end in ("low", "high"):
            v = dict(base_v, **{k: float(lp[k][end])})
            r = fuel_year(v)
            oat.append((k, end, float(lp[k][end]), r["natU_t"] * n_units, r["tSWU"] * n_units))
    env_hi = dict(base_v, capacity_factor=float(lp["capacity_factor"]["high"]), net_mwe=float(lp["net_mwe"]["high"]),
                  burnup_gwd_per_t=float(lp["burnup_gwd_per_t"]["low"]), enrichment_pct=float(lp["enrichment_pct"]["high"]),
                  tails_assay_pct=float(lp["tails_assay_pct"]["low"]))
    env_lo = dict(base_v, capacity_factor=float(lp["capacity_factor"]["low"]), net_mwe=float(lp["net_mwe"]["low"]),
                  burnup_gwd_per_t=float(lp["burnup_gwd_per_t"]["high"]), enrichment_pct=float(lp["enrichment_pct"]["low"]),
                  tails_assay_pct=float(lp["tails_assay_pct"]["high"]))
    r_hi, r_lo = fuel_year(env_hi), fuel_year(env_lo)
    swu_hi, swu_lo = r_hi["tSWU"] * n_units, r_lo["tSWU"] * n_units
    nat_hi = max(r_hi["natU_t"], r_lo["natU_t"], *(o[3] / n_units for o in oat)) * n_units
    nat_lo = min(r_hi["natU_t"], r_lo["natU_t"], *(o[3] / n_units for o in oat)) * n_units

    sr = p["strategic_reserve"]
    n_rel = sr["reloads_held"]["value"]
    reserve = []
    for months in (sr["cycle_length_months"]["low"], sr["cycle_length_months"]["high"]):
        yrs = n_rel * months / 12
        reserve.append((months, yrs, four["enc_t"] * yrs, four["natU_t"] * yrs, four["tSWU"] * yrs))

    def pct(a: float, b: float) -> str:
        return f"{100 * a / b:.2f}%"

    out += [
        "## 6. Sizing to the proposal: four BWRX-300s at Darlington (run 7b)",
        "",
        "Inputs: `parameters_lca.yaml` (read-only; burnup, enrichment, capacity factor and net MWe are **placeholders** "
        "awaiting Leroy's BWRX-300 data) and the enrichment balance used in `lca_model.py`. The script asserts that the "
        f"four-unit totals equal `lca_baseline.md` ({fl['check_four_units_natU_t']} t U, {fl['check_four_units_tSWU']} tSWU). "
        "tSWU = tonne-SWU = thousand SWU; kSWU in sections 1–5 is the same unit.",
        "",
        "### 6.1 Annual demand",
        "",
        "| Quantity | 1 unit / yr | 4 units / yr |",
        "|---|---:|---:|",
        f"| Net generation (MWh) | {one['mwh']:,.0f} | {four['mwh']:,.0f} |",
        f"| Enriched U ({base_v['enrichment_pct']}% U-235), t | {one['enc_t']:.2f} | {four['enc_t']:.1f} |",
        f"| Natural U feed, t U | {one['natU_t']:.1f} | **{four['natU_t']:.1f}** |",
        f"| Separative work, tSWU | {one['tSWU']:.1f} | **{four['tSWU']:.1f}** |",
        "",
        f"Working (one unit): {base_v['net_mwe']:.0f} MWe × 8,760 h × {base_v['capacity_factor']} = {one['mwh']:,.0f} MWh; "
        f"η = {base_v['net_mwe']:.0f}/{base_v['thermal_mwt']:.0f} = {base_v['net_mwe'] / base_v['thermal_mwt']:.4f}; "
        f"kWh per kg EU = {base_v['burnup_gwd_per_t']:.0f} × 24,000 × η = "
        f"{base_v['burnup_gwd_per_t'] * 24000 * base_v['net_mwe'] / base_v['thermal_mwt']:,.0f}; "
        f"feed factor F = {one['feed']:.3f}; SWU per kg EU = {one['swu_per_kg']:.3f}.",
        "",
        "### 6.2 Against supplier capacity",
        "",
        "| Four-unit demand set against | Capacity | Darlington share |",
        "|---|---:|---:|",
        f"| Urenco USA (Eunice), current | {uu_now:,} tSWU | **{pct(four['tSWU'], uu_now)}** |",
        f"| Urenco USA after the 2027 project | {uu_2027:,} tSWU | {pct(four['tSWU'], uu_2027)} |",
        f"| Urenco USA after the 2032–2036 expansion (> 7 million SWU) | {uu_2036:,} tSWU | {pct(four['tSWU'], uu_2036)} |",
        f"| Western enrichers, Urenco + Orano (WNA 2025) | {west_2025:,.0f} tSWU | {pct(four['tSWU'], west_2025)} |",
        f"| World enrichment capacity (WNA 2025) | {world_2025:,.0f} tSWU | {pct(four['tSWU'], world_2025)} |",
        f"| Cameco Port Hope conversion (WNA) | {cameco_conv:,.0f} tU | {pct(four['natU_t'], cameco_conv)} |",
        f"| Canadian mine output, 2024 | {canada_mine:,.0f} tU | {pct(four['natU_t'], canada_mine)} |",
        f"| World mine output, 2024 | {m['world_total'][2024]:,} tU | {pct(four['natU_t'], m['world_total'][2024])} |",
        f"| World reactor requirements, 1 Jan 2025 | {req:,} tU | {pct(four['natU_t'], req)} |",
        "",
        f"Envelope (all inputs at the ends that raise or lower SWU together; not a physically consistent fuel design, "
        f"because burnup and enrichment move together in practice): **{swu_lo:.0f}–{swu_hi:.0f} tSWU** a year for four "
        f"units, i.e. {pct(swu_lo, uu_now)}–{pct(swu_hi, uu_now)} of Urenco USA today. Natural U across the one-at-a-time "
        f"and envelope cases: {nat_lo:.0f}–{nat_hi:.0f} t U a year.",
        "",
        "One-at-a-time sensitivity (four units):",
        "",
        "| Input | End | Value | Natural U (t/yr) | tSWU/yr |",
        "|---|---|---:|---:|---:|",
    ]
    for k, end, val, nat, swu in oat:
        out.append(f"| {k} | {end} | {val:g} | {nat:.1f} | {swu:.1f} |")
    out += [
        "",
        f"### 6.3 Strategic reserve of {n_rel} reloads (four units)",
        "",
        "At equilibrium one reload equals annual enriched-U demand × cycle length, so the reserve depends on the "
        "BWRX-300 cycle length (not found; 12–24 months assumed, Leroy request in plan.md section 5).",
        "",
        "| Cycle length | Years of demand held | Enriched U (t) | Natural-U equivalent (t U) | SWU embodied (tSWU) | SWU as share of Urenco USA year |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for months, yrs, enc, nat, swu in reserve:
        out.append(f"| {months} months | {yrs:g} | {enc:.1f} | {nat:.0f} | {swu:.0f} | {pct(swu, uu_now)} |")
    out += [
        "",
        "### 6.4 What the sizing means (for section 8.3)",
        "",
        f"- Darlington's whole four-unit fleet needs about **{four['tSWU']:.0f} tSWU and {four['natU_t']:.0f} t U a year**: "
        f"{pct(four['tSWU'], uu_now)} of Urenco USA's current output capacity and {pct(four['tSWU'], west_2025)} of the "
        "Russia-free, China-free enrichment market. The HHI in sections 2–4 measures the market the project buys from; "
        "the project itself is far too small to move it. The exposure is to **price and contract terms in a "
        "duopoly**, not to physical shortage.",
        f"- The two-reload reserve ({reserve[0][2]:.0f}–{reserve[1][2]:.0f} t of enriched U, embodying "
        f"{reserve[0][4]:.0f}–{reserve[1][4]:.0f} tSWU) is about {pct(reserve[0][4], uu_now)}–{pct(reserve[1][4], uu_now)} "
        "of one year of Urenco USA output. It is a working-capital question (price per kg of fabricated fuel; not "
        "sourced) rather than a supply question.",
        f"- Urenco USA's announced additions (+{uu['expansion_2027_kSWU']['value']:,} tSWU by 2027; "
        f"+{uu['expansion_2032_2036_kSWU']['value']:,} tSWU over 2032–2036) are each larger than Darlington's four-unit demand "
        f"by a factor of about {uu['expansion_2027_kSWU']['value'] / four['tSWU']:.0f} and "
        f"{uu['expansion_2032_2036_kSWU']['value'] / four['tSWU']:.0f}. The binding competition is US utilities replacing "
        "Russian SWU before the PL 118-62 waivers end on 1 January 2028, not Darlington's own volume.",
        "- An Australian unit at Liddell would need the same ~34 tSWU and ~49 t U a year per unit, all of it enriched "
        "offshore (sections 2 and 5).",
        "- All inputs are unverified or placeholders. The ratios are robust to them: even the high envelope stays "
        f"at {pct(swu_hi, uu_now)} of Urenco USA's current capacity.",
        "",
    ]

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "hhi.md").write_text("\n".join(out), encoding="utf-8")
    with (RESULTS / "hhi_summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader()
        w.writerows(summary)

    for r in summary:
        print(f"{r['stage']:<18} {r['scenario']:<45} {r['hhi']:>6,}  {r['doj_ftc_2023']:<24} {r['doj_ftc_2010']}")
    print(f"Russia enrichment share 2025: {s_en[2025]['Rosatom']:.2f}%  (2022 {s_en[2022]['Rosatom']:.2f}%, "
          f"2030 {s_en[2030]['Rosatom']:.2f}%); range across WNA/WNU/CRAI {ru_range[0]:.2f}-{ru_range[-1]:.2f}%")
    print(f"Four units: {four['natU_t']:.1f} tU/yr, {four['tSWU']:.1f} tSWU/yr = {100 * four['tSWU'] / uu_now:.2f}% of "
          f"Urenco USA; envelope {swu_lo:.0f}-{swu_hi:.0f} tSWU; reserve {reserve[0][4]:.0f}-{reserve[1][4]:.0f} tSWU")


if __name__ == "__main__":
    main()
