# Rubric coverage: R2.1, R2.3, R2.6, R4.2, R4.4, RB.1, RB.5
"""Re-based 25/10/2026: MAIN case = Ostrołęka PIS inventory, C1 = LC3 (Pillai 2019, 380 -> 270 kg/m3) on
20/40/60% of the plant concrete (40% central). The bottom-up 21/10 scenarios are kept as the cross-check rows
(basis "bottomup"), together with the per-structure table and the S0 counterfactual.

Initiative C1 scenarios: S0 baseline GU, S1 slag, S2 LC3, S2b LC3 + slag elsewhere, S3 steel sensitivity
(S3lfl like-for-like in the target structures; S3lo whole-plant upper bound; S3hi world-average), and the
S0 counterfactual (what if OPG's baseline mixes already contain slag).

Run:  python3 -I 03_LCA_Calculations/scripts/lca_scenarios.py
Writes results/lca_scenarios.csv, results/lca_scenarios_structures.csv, results/lca_s0_counterfactual.csv
and results/lca_scenarios.md. Monte Carlo medians and intervals of every scenario's saving and life-cycle
share are in results/lca_montecarlo_summary.csv (scripts/lca_uncertainty.py).

Savings are changes in concrete (or steel) A1-A3 only. The construction uplift is NOT applied to savings:
changing the binder does not change cabling, copper or site energy. Life-cycle shares use the S0 total.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lca_model import (RESULTS, load_raw, central, model, lc3_saving, concrete_block, fmt,  # noqa: E402
                       steel_target_saving, steel_whole_saving, slag_baseline_counterfactual)

RAW = load_raw()
P = central(RAW)
N = int(P["units_initiative"])
B = model(P, "S0", RAW)
BX = model(P, "S0", RAW, basis="bottomup")

rows = []
CASES = []
for share in (float(RAW["c1_eligible_share"]["low"]), P["c1_eligible_share"], float(RAW["c1_eligible_share"]["high"])):
    q = dict(P)
    q["c1_eligible_share"] = share
    CASES.append((q, "ostroleka", f"C1_{share * 100:.0f}", "S2",
                  f"C1 LC3 on {share:.0%} of plant concrete ({share * P['ostroleka_concrete_m3']:,.0f} m3)"
                  + (" (central)" if share == P["c1_eligible_share"] else "")))
CASES += [(P, "ostroleka", "S1_40", "S1", "S1 slag blend (fallback) on the same 40% eligible concrete"),
          (P, "ostroleka", "S2b_40", "S2b", "S2b LC3 on 40% eligible + slag blend in all other concrete (upper bound)"),
          (P, "bottomup", "X_S1", "S1", "Cross-check (bottom-up 20,700 m3): S1 slag in DPSC infill + forebay"),
          (P, "bottomup", "X_S2", "S2", "Cross-check (bottom-up 20,700 m3): S2 LC3 in DPSC infill + forebay (old C1)"),
          (P, "bottomup", "X_S2b", "S2b", "Cross-check (bottom-up 20,700 m3): S2b LC3 in targets + slag elsewhere")]
for q, basis, sc_id, sc, label in CASES:
    x = lc3_saving(q, RAW, sc, basis)
    Bb = model(q, "S0", RAW, basis)
    rows.append({"scenario": sc_id, "basis": basis, "description": label,
                 "saving_t_per_unit": round(x["t_per_unit"]), "saving_t_units_2_4": round(N * x["t_per_unit"]),
                 "clinker_avoided_t_per_unit": round(x["clinker_t_per_unit"]),
                 "clinker_avoided_t_units_2_4": round(N * x["clinker_t_per_unit"]),
                 "pct_of_target_concrete": round(x["pct_target_concrete"], 1),
                 "pct_of_unit_life_cycle": round(x["pct_life_cycle"], 3),
                 "g_per_kwh_saved": round(x["g_per_kwh"], 4),
                 "life_cycle_g_per_kwh_after": round(Bb["total_g"] - x["g_per_kwh"], 4)})

# S3 steel recycled-content sensitivity (vs S0 central steel factors)
# S3lfl: like-for-like with C1 (same structures); S3lo: whole-plant upper bound; S3hi: world-average steel
LFL = steel_target_saving(P, RAW)
S3_ROWS = [("S3lfl", "S3 like-for-like: low-end steel factors on the C1 target-structure steel only "
                     f"({fmt(LFL['steel_t'])} t: DPSC basemat module plate + forebay rebar)", LFL["t_per_unit"]),
           ("S3lo", "S3 upper bound: all steel at best-practice EAF sections factors", steel_whole_saving(P, RAW, "S3lo")),
           ("S3hi", "S3 high: all steel at world-average (BOF-heavy) factors", steel_whole_saving(P, RAW, "S3hi"))]
for sc, label, d in S3_ROWS:
    rows.append({"scenario": sc, "basis": "ostroleka", "description": label, "saving_t_per_unit": round(d), "saving_t_units_2_4": round(N * d),
                 "clinker_avoided_t_per_unit": 0, "clinker_avoided_t_units_2_4": 0, "pct_of_target_concrete": "",
                 "pct_of_unit_life_cycle": round(100 * d / B["total_t_life"], 3), "g_per_kwh_saved": round(1000 * d / B["mwh_life"], 4),
                 "life_cycle_g_per_kwh_after": round(B["total_g"] - 1000 * d / B["mwh_life"], 4)})


with open(RESULTS / "lca_scenarios.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# Per structure (one unit)
srows = []
v = BX["vol"]
for name, vol, binder in [("DPSC reactor-building infill", v["dpsc"], P["binder_scc_kg_per_m3"]),
                          ("Forebay shaft", v["forebay"], P["binder_conv_kg_per_m3"])]:
    base = concrete_block(P, vol, binder, "GU")
    for mix, sc in [("SLAG", "S1"), ("LC3", "S2")]:
        alt = concrete_block(P, vol, binder, mix)
        srows.append({"structure": name, "scenario": sc, "volume_m3": round(vol), "binder_kg_per_m3": binder,
                      "s0_t_co2e": round(base["kg"] / 1000), "scenario_t_co2e": round(alt["kg"] / 1000),
                      "saving_t_co2e": round((base["kg"] - alt["kg"]) / 1000),
                      "saving_kg_per_m3": round((base["kg"] - alt["kg"]) / vol, 1),
                      "clinker_avoided_t": round(base["clinker_t"] - alt["clinker_t"])})
with open(RESULTS / "lca_scenarios_structures.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(srows[0].keys()))
    w.writeheader()
    w.writerows(srows)

L = ["Rubric coverage: R2.1, R2.3, R2.6, R4.2, R4.4, RB.1, RB.5\n",
     "# C1 scenarios, generated by `scripts/lca_scenarios.py` (re-based 25/10/2026)\n",
     f"Main case S0 (Ostrołęka PIS {fmt(P['ostroleka_concrete_m3'])} m3, {fmt(P['ostroleka_steel_t'])} t steel): {B['total_g']:.3f} g CO2e/kWh (mode case); "
     f"{fmt(B['total_t_life'])} t CO2e per unit over {P['design_life_yr']:.0f} years. C1 = LC3 on the eligible share of plant concrete at "
     f"{P['ef_concrete_opc_kg_per_m3']:.0f} x {P['c1_lc3_concrete_cut']:.4f} = {P['ef_concrete_opc_kg_per_m3'] * P['c1_lc3_concrete_cut']:.0f} kg CO2e/m3 saved "
     f"(Pillai 2019: 380 - 270). Cross-check S0 (bottom-up): {BX['total_g']:.3f} g/kWh, {fmt(BX['total_t_life'])} t. Shares here are of the "
     f"mode-case life cycle of the row's own basis; Monte Carlo shares are in lca_uncertainty.md. Units 2-4 = {N} units.\n",
     "## Per unit and for Units 2-4\n",
     "| Scenario | Saving t CO2e/unit | Units 2-4 t CO2e | Clinker avoided t/unit | Units 2-4 clinker t | % of target concrete | % of unit life cycle | g/kWh saved |",
     "|---|---|---|---|---|---|---|---|"]
for r in rows:
    L.append(f"| {r['description']} | {fmt(r['saving_t_per_unit'])} | {fmt(r['saving_t_units_2_4'])} | {fmt(r['clinker_avoided_t_per_unit'])} | "
             f"{fmt(r['clinker_avoided_t_units_2_4'])} | {r['pct_of_target_concrete']} | {r['pct_of_unit_life_cycle']} | {r['g_per_kwh_saved']} |")
L += ["\nS3 rows: positive = lower than the S0 steel factors; negative = higher. They are a sensitivity on the baseline, not part of C1.",
      f"- **S3 like-for-like** (same structures as C1): {fmt(P['dpsc_basemat_steel_t'])} t DPSC basemat plate x ({P['ef_plate_other']:.2f} - "
      f"{float(RAW['ef_plate_other']['low']):.2f}) + {fmt(P['forebay_rebar_t'])} t forebay rebar x ({P['ef_rebar']:.2f} - {float(RAW['ef_rebar']['low']):.2f}) = "
      f"{LFL['plate_t']:.0f} + {LFL['rebar_t']:.0f} = **{LFL['t_per_unit']:.0f} t per unit**, against C1's {lc3_saving(P, RAW, 'S2')['t_per_unit']:,.0f} t (main) "
      f"or {lc3_saving(P, RAW, 'S2', 'bottomup')['t_per_unit']:,.0f} t (cross-check, same structures). "
      "The DPSC shaft-wall plate is not known and is excluded, so this is a floor "
      "for the target-structure steel [TODO: NEDO-33926 / OPG plate tonnage].",
      f"- **S3 upper bound**: all {fmt(B['steel_t'])} t of plant steel, including forgings and nuclear-grade plate, moved to the best-practice EAF *sections* factor "
      f"({float(RAW['ef_plate_other']['low']):.2f} t/t, BCCA hot-rolled sections limit) and the low rebar factor. Not shown to be feasible for forgings or nuclear plate.\n",
      "## Cross-check only: per structure (one unit, bottom-up model)\n",
      "| Structure | Scenario | m3 | Binder kg/m3 | S0 t | Scenario t | Saving t | Saving kg/m3 | Clinker avoided t |",
      "|---|---|---|---|---|---|---|---|---|"]
for r in srows:
    L.append(f"| {r['structure']} | {r['scenario']} | {fmt(r['volume_m3'])} | {r['binder_kg_per_m3']:.0f} | {fmt(r['s0_t_co2e'])} | {fmt(r['scenario_t_co2e'])} | "
             f"{fmt(r['saving_t_co2e'])} | {r['saving_kg_per_m3']} | {fmt(r['clinker_avoided_t'])} |")
gu = P["ef_gu_cement"]
L += ["\n## Working (per tonne of binder)\n",
      f"- S0 GU: {gu:.0f} kg CO2e/t; clinker {P['clinker_factor_gu']:.2f} t/t.",
      f"- S1 slag {P['slag_replacement_s1']:.0%}: (1 - s) x {gu:.0f} + s x {P['ef_slag']:.1f} = {(1 - P['slag_replacement_s1']) * gu + P['slag_replacement_s1'] * P['ef_slag']:.0f} kg/t; "
      f"clinker {(1 - P['slag_replacement_s1']) * P['clinker_factor_gu']:.3f} t/t.",
      f"- S2 LC3: {gu:.0f} x (1 - {P['lc3_gwp_reduction']:.2f}) = {gu * (1 - P['lc3_gwp_reduction']):.0f} kg/t; clinker {P['lc3_clinker_factor']:.2f} t/t; "
      f"binder content x (1 + {P['lc3_binder_uplift']:.2f}).",
      f"- Concrete per m3 = binder (kg/m3) x factor / 1000 + {P['ef_concrete_other_kg_per_m3']:.0f} kg/m3 (aggregates, water, admixtures, batching).",
      "- Saving per structure = volume x (S0 per m3 - scenario per m3). Units 2-4 = 3 x per unit (Unit 1's basemat is placed and its forebay well advanced)."]
(RESULTS / "lca_scenarios.md").write_text("\n".join(L) + "\n")

# ---- S0 counterfactual: what if OPG's baseline mixes already contain slag? (review.md section 6 point 2) ----
crow = []
for lab, frac in [("low (slag 25% of binder)", float(RAW["slag_replacement_s1"]["low"])),
                  ("central (slag 40% of binder)", P["slag_replacement_s1"])]:
    c = slag_baseline_counterfactual(P, RAW, frac, "bottomup")
    crow.append({"counterfactual_s0": lab, "slag_fraction": round(c["slag_fraction"], 2),
                 "s0_change_vs_gu_t_per_unit": round(-c["s0slag_vs_gu_t"]),
                 "s0_life_cycle_g_per_kwh": round(c["s0slag_total_g"], 4),
                 "lc3_increment_t_per_unit": round(c["lc3_increment_t"]),
                 "lc3_increment_t_units_2_4": round(N * c["lc3_increment_t"]),
                 "lc3_increment_clinker_t_per_unit": round(c["lc3_increment_clinker_t"]),
                 "lc3_increment_pct_of_life_cycle": round(c["lc3_increment_pct_life"], 3)})
with open(RESULTS / "lca_s0_counterfactual.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(crow[0].keys()))
    w.writeheader()
    w.writerows(crow)
L += ["\n## S0 counterfactual (cross-check, bottom-up model): if OPG's baseline already contains slag\n",
      "Whether GEH's NEDO-33926 SCC infill specification or OPG's Darlington mixes already permit or use supplementary cementitious "
      "materials (slag, fly ash) has **not** been found [TO VERIFY: NEDO-33926 Rev. 2 (NRC ML24110A134) concrete section; OPG/St Marys "
      "mix submittals]. If they do, S0 is a slag blend in all plant concrete (scenario S0slag), S1 becomes business as usual, and C1's "
      "increment is LC3 in the targets with slag elsewhere (S2b) against S0slag. Slag fractions are the S1 range (`slag_replacement_s1`, assumption).\n",
      "| Counterfactual S0 | Slag share | S0 change vs GU t/unit | S0 life cycle g/kWh | LC3 increment t/unit | Units 2-4 t | Clinker t/unit | % of life cycle |",
      "|---|---|---|---|---|---|---|---|"]
for r in crow:
    L.append(f"| {r['counterfactual_s0']} | {r['slag_fraction']:.2f} | {fmt(r['s0_change_vs_gu_t_per_unit'])} | {r['s0_life_cycle_g_per_kwh']} | "
             f"{fmt(r['lc3_increment_t_per_unit'])} | {fmt(r['lc3_increment_t_units_2_4'])} | {fmt(r['lc3_increment_clinker_t_per_unit'])} | "
             f"{r['lc3_increment_pct_of_life_cycle']} |")
_cm = slag_baseline_counterfactual(P, RAW, None, "ostroleka")
L += [f"\nMain case equivalent (slag {P['slag_replacement_s1']:.0%} in all plant concrete as S0): LC3's increment on the 40% eligible concrete = "
      f"{_cm['lc3_increment_t']:,.0f} t/unit ({_cm['lc3_increment_pct_life']:.3f}% of the life cycle), clinker {_cm['lc3_increment_clinker_t']:,.0f} t/unit.",
      f"\nReading: on a slag baseline the life cycle barely moves, and C1's carbon increment shrinks from {lc3_saving(P, RAW, 'S2', 'bottomup')['t_per_unit']:,.0f} t (cross-check) to the LC3-minus-slag "
      "difference in the target structures (Monte Carlo interval spans zero: `lca_montecarlo_summary.csv`, row lc3_minus_slag_t_per_unit). "
      "The clinker increment stays positive because LC3 carries less clinker per tonne than a 25-40% slag blend."]
(RESULTS / "lca_scenarios.md").write_text("\n".join(L) + "\n")

s2 = next(r for r in rows if r["scenario"] == "C1_40")
print(f"S2 LC3: {s2['saving_t_per_unit']:,} t CO2e/unit, {s2['saving_t_units_2_4']:,} t for Units 2-4, "
      f"{s2['pct_of_unit_life_cycle']}% of the unit life cycle; clinker avoided {s2['clinker_avoided_t_per_unit']:,} t/unit")
