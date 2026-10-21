# Rubric coverage: R3.3, R3.4, R3.5, R3.6, R3.7, R3.8, R5.2, RB.5
"""Social licence, stakeholders, money flows, workforce and waste governance (analyst run 6).

Calculations
  1. Poll arithmetic: Lowy 2024 support/oppose sums and net support; Griffith-Monash keep-ban margin.
  2. Perceived vs actual safety: death-rate ratios (OWID) and statistical deaths avoided per year by one
     BWRX-300 (and four at Darlington), depending on what it displaces. Sensitivity on capacity factor.
       E_TWh   = net_MWe * 8760 * CF / 1e6
       avoided = (rate_displaced - rate_nuclear) * E_TWh
  3. Consent-process arithmetic: Kimba ballot share vs the 65% benchmark; Ignace willingness vote;
     NWMO hosting payment per year; NWMO siting duration.
  4. Money flows at Darlington: each financier's nominal share of the C$20.9 bn budget (debt and equity
     mixed; indicative only).
  5. Workforce: trades-shortfall sum check; CBoC jobs per MWe.
  6. Stakeholder quadrants (Mendelow power/interest grid) and figure F8.
  7. Social-licence routes for Liddell: weighted scores under five weight sets (sensitivity).

Inputs : 03_LCA_Calculations/parameters_run6.yaml
Outputs: results/social_licence.md, results/social_licence.csv, results/F8_stakeholder_map.png
Run    : python3 -I 03_LCA_Calculations/scripts/social_licence.py
"""
from __future__ import annotations

import csv
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import lca_plot  # noqa: E402  (shared chart style)

PARAMS = ROOT / "parameters_run6.yaml"
RES = ROOT / "results"
P = yaml.safe_load(PARAMS.read_text())

rows: list[tuple[str, str, float | str, str]] = []  # (block, item, value, unit)
md: list[str] = []


def add(block, item, value, unit):
    rows.append((block, item, value, unit))
    return value


# ---------------------------------------------------------------- 1. polls
lowy = P["polls"]["lowy_2024"]
sup = lowy["strongly_support"] + lowy["somewhat_support"]
opp = lowy["strongly_oppose"] + lowy["somewhat_oppose"]
tot = sup + opp + lowy["dont_know"]
assert tot == 100, f"Lowy rows sum to {tot}"
add("polls", "Lowy 2024 support", sup, "%")
add("polls", "Lowy 2024 oppose", opp, "%")
add("polls", "Lowy 2024 net support", sup - opp, "pct points")
gm = P["polls"]["griffith_monash_2024wave"]
keep_margin = gm["keep_ban"][2024] - gm["against_ban"][2024]
add("polls", "Griffith-Monash 2024 keep-ban margin", keep_margin, "pct points")
add("polls", "Griffith-Monash keep-ban change 2023-24", gm["keep_ban"][2024] - gm["keep_ban"][2023], "pct points")
np07 = P["polls"]["newspoll_2007_local"]
add("polls", "Newspoll 2007 national minus local support", np07["national_support"] - np07["local_plant_support"], "pct points")
es19 = P["polls"]["essential_2019_local"]
add("polls", "Essential 2019 support minus comfortable living close", es19["support_plants"] - es19["comfortable_living_close"], "pct points")

# ---------------------------------------------------------------- 2. safety
d = P["deaths_per_twh"]["values"]
for k in ("brown_coal", "coal", "gas"):
    add("safety", f"ratio {k}/nuclear", round(d[k] / d["nuclear"]), "x")

pl = P["plant"]
def e_twh(cf):
    return pl["net_mwe"]["value"] * 8760 * cf / 1e6

cf_c, cf_l, cf_h = (pl["capacity_factor"][k] for k in ("value", "low", "high"))
cases = [
    ("Liddell: displaces black coal (upper bound)", "coal", 1),
    ("Liddell: displaces brown coal (Loy Yang stretch case)", "brown_coal", 1),
    ("Darlington: displaces gas (Ontario has no coal), per unit", "gas", 1),
    ("Darlington: displaces gas, four units", "gas", pl["units_darlington"]["value"]),
    ("Either site: displaces wind", "wind", 1),
    ("Either site: displaces solar", "solar", 1),
]
safety_tbl = []
for label, src, n in cases:
    vals = [(d[src] - d["nuclear"]) * e_twh(cf) * n for cf in (cf_l, cf_c, cf_h)]
    safety_tbl.append((label, src, n, *vals))
    add("safety", f"deaths avoided/yr: {label}", round(vals[1], 2), "statistical deaths per year")
nuc_own = d["nuclear"] * e_twh(cf_c)
add("safety", "statistical deaths/yr attributed to one unit's own output", round(nuc_own, 3), "deaths per year")
add("safety", "years per statistical death, one unit", round(1 / nuc_own, 1), "years")
add("safety", "annual output per unit (central)", round(e_twh(cf_c), 4), "TWh")

# ---------------------------------------------------------------- 3. consent
kb = P["kimba_ballot_2019"]
k_pct = 100 * kb["yes"] / (kb["yes"] + kb["no"])
assert abs(k_pct - kb["reported_yes_pct"]) < 0.01, k_pct
add("consent", "Kimba 2019 yes share (recomputed)", round(k_pct, 2), "%")
add("consent", "Kimba shortfall vs 65% benchmark", round(kb["minister_benchmark_pct"] - k_pct, 2), "pct points")
add("consent", "Kimba ballot turnout (votes cast)", kb["yes"] + kb["no"], "votes")
ig = P["ignace_willingness_vote_2024"]
ig_pct = 100 * ig["yes"] / ig["participants"]
assert abs(ig_pct - ig["reported_pct"]) < 0.5, ig_pct
add("consent", "Ignace 2024 yes share (recomputed)", round(ig_pct, 1), "%")
ha = P["ignace_hosting_agreement"]
add("consent", "Ignace hosting payment, average per year", round(ha["total_cad_m"] / ha["years"], 2), "C$ m/yr (nominal, undiscounted)")
ns = P["nwmo_siting"]
add("consent", "NWMO siting duration (start to selection)", int(str(ns["selected"])[:4]) - ns["process_start"], "years")
add("consent", "NWMO funnel 22 -> 11 -> 2 -> 1", f"{ns['communities_expressed_interest']}->{ns['communities_phase2']}->{ns['shortlist_by_2019']}->1", "communities")
mk = P["muckaty"]
add("consent", "Muckaty nomination to withdrawal", mk["withdrawn"] - mk["nominated"], "years")
nc = P["nwmo_cost"]
add("waste", "NWMO lifecycle cost, average per year", round(nc["lifecycle_cost_cad_bn_2020"] / nc["lifecycle_years"], 3), "C$ bn/yr (2020$)")
add("waste", "NFWA trust funds as share of lifecycle cost", round(100 * nc["nfwa_trust_funds_cad_bn_dec2023"] / nc["lifecycle_cost_cad_bn_2020"], 1), "% (mixed dollar bases; indicative)")
add("waste", "Hosting payment as share of NWMO lifecycle cost", round(100 * ha["total_cad_m"] / 1000 / nc["lifecycle_cost_cad_bn_2020"], 2), "% (indicative)")

# ---------------------------------------------------------------- 4. money
m = P["darlington_money"]
budget = m["budget_four_units"]["value"]
fin = {
    "CGF equity (federal Crown)": m["cgf_equity"]["value"],
    "BOF equity (Ontario)": m["bof_equity"]["value"],
    "CIB loan, Phase 1 (federal Crown)": m["cib_loan_phase1"]["value"],
    "WTFN loan-to-equity (guaranteed by CILGC + Ontario)": m["wtfn_loan_to_equity"]["value"],
}
money_tbl = []
for k, v in fin.items():
    money_tbl.append((k, v, 100 * v / budget))
    add("money", f"share of C$20.9 bn: {k}", round(100 * v / budget, 1), "%")
resid = budget - sum(fin.values())
money_tbl.append(("Remainder: OPG balance sheet, recovered from Ontario ratepayers via OEB", resid, 100 * resid / budget))
add("money", "remainder (OPG / ratepayers)", round(resid, 2), "C$ bn")
add("money", "remainder share", round(100 * resid / budget, 1), "%")
add("money", "budget per MW (four units, ~1,200 MW)", round(budget * 1000 / (pl["net_mwe"]["value"] * 4), 1), "C$ m/MW (at 300 MWe per unit)")

# ---------------------------------------------------------------- 5. workforce
w = P["workforce"]
ts = w["trades_shortfall_2030_31"]
ts_sum = sum(v for k, v in ts.items() if isinstance(v, int))
assert ts_sum > 75000, ts_sum
add("workforce", "four-trade shortfall sum, 2030-31", ts_sum, "workers")
cb = P["cboc_jobs"]["single_smr_2021"]
add("workforce", "CBoC construction jobs per MW", round(cb["manufacturing_construction"] / 300, 2), "jobs/MW/yr")
add("workforce", "CBoC operations jobs per MW", round(cb["operations"] / 300, 2), "jobs/MW/yr")
add("workforce", "Liddell workers redeployed to Bayswater", round(w["liddell_workforce_at_closure"]["value"] * w["liddell_share_moved_to_bayswater_pct"]["value"] / 100), "workers (approx.)")

# ---------------------------------------------------------------- 6. stakeholders
def quadrant(p, i):
    hp, hi = p >= 4, i >= 4
    return {(True, True): "Manage closely", (True, False): "Keep satisfied",
            (False, True): "Keep informed", (False, False): "Monitor"}[(hp, hi)]

stake_tbl = {}
for site, lst in P["stakeholders"].items():
    stake_tbl[site] = [(s["name"], s["power"], s["interest"], s["stance"], quadrant(s["power"], s["interest"]), s["evidence"]) for s in lst]
    hp = [s for s in lst if s["power"] >= 4]
    add("stakeholders", f"{site}: high-power actors", len(hp), "count")
    add("stakeholders", f"{site}: high-power actors opposed (stance<0)", sum(1 for s in hp if s["stance"] < 0), "count")
    add("stakeholders", f"{site}: power-weighted stance", round(sum(s["power"] * s["stance"] for s in lst) / sum(s["power"] for s in lst), 2), "-2 to +2")

# Figure F8
import matplotlib.pyplot as plt  # noqa: E402
lca_plot.style()
fig, axes = plt.subplots(1, 2, figsize=(11, 5.2), sharey=True)
col = {2: lca_plot.GREEN, 1: lca_plot.AQUA, 0: lca_plot.MUTED, -1: lca_plot.ORANGE, -2: lca_plot.RED}
for ax, (site, title) in zip(axes, [("darlington", "Darlington, Ontario (C1 and Units 2-4)"), ("liddell", "Liddell, NSW (hypothetical BWRX-300)")]):
    pts = P["stakeholders"][site]
    seen: dict[tuple[int, int], int] = {}
    for s in pts:
        key = (s["interest"], s["power"])
        k = seen.get(key, 0)
        seen[key] = k + 1
        y = s["power"] - 0.28 * k
        ax.scatter(s["interest"], y, s=70, color=col[s["stance"]], edgecolor="white", zorder=3)
        ax.annotate(s["name"], (s["interest"], y), xytext=(6, -3), textcoords="offset points", fontsize=7.2, color=lca_plot.INK)
    ax.axhline(3.5, color=lca_plot.GRID, lw=1.2, zorder=1)
    ax.axvline(3.5, color=lca_plot.GRID, lw=1.2, zorder=1)
    for (x, y, t) in [(1.1, 5.55, "Keep satisfied"), (3.6, 5.55, "Manage closely"), (1.1, 0.75, "Monitor"), (3.6, 0.75, "Keep informed")]:
        ax.text(x, y, t, fontsize=7.5, color=lca_plot.MUTED, style="italic")
    ax.set_xlim(1, 6.9)
    ax.set_ylim(0.6, 5.8)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xlabel("Interest in the outcome (1 low - 5 high)")
    ax.text(0.0, 1.02, title, transform=ax.transAxes, fontsize=9.5, color=lca_plot.INK, weight="bold")
axes[0].set_ylabel("Power to stop or enable (1 low - 5 high)")
from matplotlib.lines import Line2D  # noqa: E402
handles = [Line2D([0], [0], marker="o", ls="", color=col[k], label=l) for k, l in [(2, "Strongly for"), (1, "Leaning for"), (0, "Neutral / unknown"), (-1, "Leaning against"), (-2, "Strongly against")]]
fig.legend(handles=handles, loc="lower center", ncol=5, bbox_to_anchor=(0.5, -0.06))
fig.tight_layout()
lca_plot.save(fig, RES / "F8_stakeholder_map.png",
              "Scores are the analyst's judgement from the evidence keys in parameters_run6.yaml (unverified sources).")

# ---------------------------------------------------------------- 7. consent routes
cr = P["consent_routes"]
crit = cr["criteria"]
route_tbl = []
for rk, r in cr["routes"].items():
    row = [r["label"]]
    for wn, wset in cr["weight_sets"].items():
        row.append(sum(wset[c] * r["scores"][c] for c in crit))
    route_tbl.append((rk, row))
wnames = list(cr["weight_sets"])
for wi, wn in enumerate(wnames):
    smr_only = [(rk, row[1 + wi]) for rk, row in route_tbl if rk != "R4_no_nuclear"]
    best = max(smr_only, key=lambda t: t[1])
    ties = [rk for rk, v in smr_only if v == best[1]]
    add("routes", f"best SMR route under {wn}", "/".join(ties), "route")

# ---------------------------------------------------------------- outputs
with open(RES / "social_licence.csv", "w", newline="") as f:
    wr = csv.writer(f)
    wr.writerow(["block", "item", "value", "unit"])
    wr.writerows(rows)

def fmt(x, nd=1):
    return f"{x:,.{nd}f}" if isinstance(x, float) else f"{x:,}" if isinstance(x, int) else str(x)

md.append("Rubric coverage: R3.3, R3.4, R3.5, R3.6, R3.7, R3.8, R5.2, RB.5\n")
md.append("# Social licence, stakeholders, money flows, workforce and waste: working (analyst run 6)\n")
md.append("Generated by `scripts/social_licence.py` from `parameters_run6.yaml`. **Every input is unverified** (search summaries only; see the YAML header). Judgement scores are labelled as such. For Appendix B.\n")

md.append("## 1. Polls\n")
md.append(f"- Lowy 2024: support {sup}% (27 + 34), oppose {opp}% (20 + 17), don't know 2%: sums to {tot}. Net support **+{sup-opp} points**.")
md.append(f"- Griffith-Monash (2024 wave, n ≈ 4,000): keep the ban {gm['keep_ban'][2024]}% vs remove {gm['against_ban'][2024]}%: a **+{keep_margin}-point margin for keeping the ban**, up {gm['keep_ban'][2024]-gm['keep_ban'][2023]} points on 2023.")
md.append("- The two are not contradictory as stated: Lowy asks about using nuclear power alongside other sources; Griffith-Monash asks about keeping a legal ban. The gap is a wording and framing effect, which is itself evidence that support is soft.")
md.append(f"- Local siting: Newspoll 2007, national support {np07['national_support']}% vs a plant in the local area {np07['local_plant_support']}% (gap {np07['national_support']-np07['local_plant_support']} points). Essential 2019: {es19['support_plants']}% support vs {es19['comfortable_living_close']}% comfortable living close (gap {es19['support_plants']-es19['comfortable_living_close']} points).\n")

md.append("## 2. Perceived vs actual safety\n")
md.append(f"Deaths per TWh (OWID): coal {d['coal']}, brown coal {d['brown_coal']}, gas {d['gas']}, wind {d['wind']}, nuclear {d['nuclear']}, solar {d['solar']}.")
md.append(f"Ratios to nuclear: coal {round(d['coal']/d['nuclear'])}×, brown coal {round(d['brown_coal']/d['nuclear'])}×, gas {round(d['gas']/d['nuclear'])}×.\n")
md.append(f"One BWRX-300: E = 300 MWe × 8,760 h × CF / 10⁶ = {e_twh(cf_c):.3f} TWh/yr at CF {cf_c} ({e_twh(cf_l):.3f}–{e_twh(cf_h):.3f} at CF {cf_l}–{cf_h}).\n")
md.append("| Case | Displaced source | Units | Deaths avoided/yr (CF 0.80) | Central (CF 0.90) | CF 0.95 |")
md.append("|---|---|---|---|---|---|")
for label, src, n, lo, c, hi in safety_tbl:
    md.append(f"| {label} | {src} | {n} | {lo:.2f} | **{c:.2f}** | {hi:.2f} |")
md.append(f"\nThe unit's own output carries {nuc_own:.3f} statistical deaths a year at the OWID nuclear rate (one per {1/nuc_own:.0f} years), a rate that includes Chernobyl and Fukushima.")
md.append("**Reading.** The health benefit depends on what the SMR displaces, exactly as the carbon benefit does (§7). It is large only against coal. Ontario has no coal, so Darlington's benefit is against gas, about a ninth of the coal case per unit. By the 2040 start at Liddell (Leroy/run 1), the NEM's coal is largely retired under the ISP, so the coal row is an upper bound. Against wind or solar the difference is within the uncertainty of the rates (negative for solar). The fossil rates are for European plants with pollution controls, so OWID calls them conservative.\n")

md.append("## 3. Consent processes\n")
md.append(f"- Kimba 2019: {kb['yes']} yes / {kb['yes']+kb['no']} votes = **{k_pct:.2f}%**, {kb['minister_benchmark_pct']-k_pct:.2f} points below the reported 65% benchmark. Barngarla native title holders were outside the electorate; their own poll returned 100% no.")
md.append(f"- Napandee declaration set aside 18 July 2023 (apprehended bias); site abandoned 10 August 2023. Muckaty: nominated {mk['nominated']}, withdrawn {mk['withdrawn']} ({mk['withdrawn']-mk['nominated']} years).")
md.append(f"- NWMO: process from {ns['process_start']} to selection on {ns['selected']} = **{int(str(ns['selected'])[:4])-ns['process_start']} years**; funnel {ns['communities_expressed_interest']} → {ns['communities_phase2']} → {ns['shortlist_by_2019']} → 1.")
md.append(f"- Ignace 2024: {ig['yes']}/{ig['participants']} = **{ig_pct:.1f}%** yes. Hosting agreement C${ha['total_cad_m']} m over {ha['years']} years = C${ha['total_cad_m']/ha['years']:.2f} m/yr (nominal, undiscounted) = {100*ha['total_cad_m']/1000/nc['lifecycle_cost_cad_bn_2020']:.2f}% of the C${nc['lifecycle_cost_cad_bn_2020']} bn lifecycle cost.")
md.append(f"- NWMO lifecycle cost C${nc['lifecycle_cost_cad_bn_2020']} bn (2020$) over {nc['lifecycle_years']} years = C${nc['lifecycle_cost_cad_bn_2020']/nc['lifecycle_years']:.3f} bn/yr on average; NFWA trust funds C${nc['nfwa_trust_funds_cad_bn_dec2023']} bn (Dec 2023) ≈ {100*nc['nfwa_trust_funds_cad_bn_dec2023']/nc['lifecycle_cost_cad_bn_2020']:.0f}% (different dollar bases).\n")

md.append("## 4. Money flows: who finances the C$20.9 bn Darlington New Nuclear Project\n")
md.append("| Financier | C$ bn | Share of budget |")
md.append("|---|---|---|")
for k, v, s in money_tbl:
    md.append(f"| {k} | {v:.2f} | {s:.1f}% |")
md.append(f"\nBudget per MW: C${budget*1000/(pl['net_mwe']['value']*4):.1f} m/MW at 4 × 300 MWe. Debt (CIB, WTFN) and equity (CGF, BOF) are added only to show scale; the remainder is what OPG funds and recovers through OEB-approved payment amounts. CGF/BOF hold 15% and 7.5% of DNNP LP: a larger share of the equity than their 14.4% share of the budget, because the budget is not all equity.\n")

md.append("## 5. Workforce\n")
md.append(f"- Four-trade shortfall by 2030–31 (Defence FOI document, as reported): {ts['electricians']:,} + {ts['construction_managers']:,} + {ts['metal_machinists']:,} + {ts['welders']:,} = **{ts_sum:,}** (reported as \"more than 75,000\": consistent).")
md.append(f"- CBoC (2021), one 300 MW SMR: {cb['manufacturing_construction']:,} jobs/yr in construction ({cb['manufacturing_construction']/300:.1f}/MW) and {cb['operations']} in operations ({cb['operations']/300:.2f}/MW), direct and related.")
md.append(f"- Liddell at closure: {w['liddell_workforce_at_closure']['value']} workers, about {round(w['liddell_workforce_at_closure']['value']*0.65)} moved to Bayswater, no forced redundancies. The CBoC operations figure (direct + related) is not like-for-like with a direct headcount.\n")

md.append("## 6. Stakeholder power/interest (analyst judgement; F8)\n")
for site, lst in stake_tbl.items():
    md.append(f"### {site.title()}\n")
    md.append("| Stakeholder | Power | Interest | Stance | Quadrant | Evidence key |")
    md.append("|---|---|---|---|---|---|")
    for name, p_, i_, st, q, ev in sorted(lst, key=lambda t: (-t[1], -t[2])):
        md.append(f"| {name} | {p_} | {i_} | {st:+d} | {q} | {ev} |")
    pw = sum(t[1] * t[3] for t in lst) / sum(t[1] for t in lst)
    nh = sum(1 for t in lst if t[1] >= 4)
    nho = sum(1 for t in lst if t[1] >= 4 and t[3] < 0)
    md.append(f"\nHigh-power actors: {nh}, of which opposed: {nho}. Power-weighted stance: **{pw:+.2f}** (−2 to +2).\n")

md.append("## 7. Social-licence routes for an SMR at Liddell (analyst judgement; weight sensitivity)\n")
md.append("Criteria scored 1–3 (3 = best): " + ", ".join(crit) + ". Scores and evidence keys in `parameters_run6.yaml`.\n")
md.append("| Route | " + " | ".join(wnames) + " |")
md.append("|---|" + "---|" * len(wnames))
for rk, row in route_tbl:
    md.append(f"| {row[0]} | " + " | ".join(str(v) for v in row[1:]) + " |")
md.append("")
for wi, wn in enumerate(wnames):
    smr_only = [(rk, row[1 + wi]) for rk, row in route_tbl if rk != "R4_no_nuclear"]
    b = max(v for _, v in smr_only)
    md.append(f"- {wn}: best SMR route = {', '.join(rk for rk, v in smr_only if v == b)} ({b}); R4 (no SMR) = {[row for rk, row in route_tbl if rk == 'R4_no_nuclear'][0][1+wi]}.")
md.append("\n**Reading.** Among SMR routes, the consent-based routes (R2, R3) beat top-down siting (R1) under every weight set except speed-doubled, where R1 ties. Equity (R3) wins only when fairness is weighted up and loses when public cost is. R4 (no SMR at Liddell) scores highest throughout because it needs no change in law or consent. This is a social-licence comparison only; it feeds the §9 MCDA, which weighs carbon and cost.\n")

(RES / "social_licence.md").write_text("\n".join(md) + "\n")
print(f"wrote {RES/'social_licence.md'}, {RES/'social_licence.csv'}, {RES/'F8_stakeholder_map.png'}")
