# Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R5.2, RB.5
"""Baseline (S0) life-cycle result for one BWRX-300 at Darlington: inventory, stages, hotspots, fuel demand.
MAIN case (re-based 25/10/2026): Ostrołęka PIS 50,000 m3 concrete and 14,000 t steel per unit, Pillai (2019) OPC
380 kg CO2e/m3. The 21/10 bottom-up 20,700 m3 model is reported alongside as the cross-check (basis "bottomup").

Run:  python3 -I 03_LCA_Calculations/scripts/lca_baseline.py
Reads parameters_lca.yaml. Writes:
  results/lca_inventory.csv      construction inventory per unit (volumes, masses, factors, t CO2e)
  results/lca_stages.csv         g CO2e/kWh and t CO2e per unit by stage, with shares (hotspot table)
  results/lca_fuel.csv           fuel mass balance per MWh and per year (1 unit and 4 units)
  results/lca_baseline.md        the same tables, appendix-ready, with the working
  results/F1_system_boundary.png  (F2 is drawn by lca_uncertainty.py)
  ../Accounting_corrected.csv    corrected version of Sam's two-row sheet (Sam's files untouched)
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))   # -I drops the script dir from sys.path
from lca_model import RESULTS, ROOT, CONCRETE_DENSITY_T_PER_M3, load_raw, central, model, fmt, main_mix_factor  # noqa: E402
import lca_plot as lp  # noqa: E402
from matplotlib.patches import FancyBboxPatch  # noqa: E402

RAW = load_raw()
P = central(RAW)
R = model(P, "S0", RAW)                       # main basis (Ostrołęka)
RX = model(P, "S0", RAW, basis="bottomup")    # cross-check
RESULTS.mkdir(exist_ok=True)


def src(k):
    return f"{RAW[k]['source']} [{RAW[k]['status']}]"


# ---------------- inventory ----------------
def binder_ef(p):
    return p["ef_gu_cement"]


def per_m3(binder):
    return binder * P["ef_gu_cement"] / 1000 + P["ef_concrete_other_kg_per_m3"]


inv = []
EF_OPC = main_mix_factor(P, "GU")[0]
for name, blk, basis in [
    (f"C1-eligible concrete ({P['c1_eligible_share']:.0%} of plant: non-safety works first)", R["c_dpsc"],
     "c1_eligible_share x Ostrołęka PIS total (team deck scenario)"),
    ("Other plant concrete (safety-related and not eligible)", R["c_oth"], "Ostrołęka PIS total minus eligible"),
]:
    inv.append({"item": name, "material": "Concrete, OPC (S0)", "quantity": round(blk["vol"]), "unit": "m3",
                "mass_t": round(blk["vol"] * CONCRETE_DENSITY_T_PER_M3),
                "binder_kg_per_m3": "", "ef": round(EF_OPC, 1), "ef_unit": "kg CO2e/m3 (Pillai 2019 M50 OPC)",
                "t_co2e": round(blk["kg"] / 1000), "basis": basis})
inv.append({"item": "Reinforcing steel (whole plant)", "material": "Rebar, EAF North American", "quantity": round(R["rebar_t"]),
            "unit": "t", "mass_t": round(R["rebar_t"]), "binder_kg_per_m3": "", "ef": P["ef_rebar"], "ef_unit": "t CO2e/t",
            "t_co2e": round(R["rebar_kg"] / 1000), "basis": "rebar_ratio x total concrete volume"})
inv.append({"item": "Plate, structural and equipment steel (incl. DPSC faceplates)", "material": "Steel plate / sections / equipment",
            "quantity": round(R["other_steel_t"]), "unit": "t", "mass_t": round(R["other_steel_t"]), "binder_kg_per_m3": "",
            "ef": P["ef_plate_other"], "ef_unit": "t CO2e/t", "t_co2e": round(R["plate_kg"] / 1000),
            "basis": "Ostrołęka PIS steel total minus rebar"})
inv.append({"item": "Transport to site (A4)", "material": "Truck", "quantity": "", "unit": "", "mass_t": "",
            "binder_kg_per_m3": "", "ef": P["ef_truck_kg_per_tkm"], "ef_unit": "kg CO2e/t-km",
            "t_co2e": round(R["transport_kg"] / 1000),
            "basis": f"concrete {P['transport_concrete_km']:.0f} km, steel {P['transport_steel_km']:.0f} km"})
inv.append({"item": "Other construction (uplift)", "material": "Other materials, site energy, equipment processing", "quantity": "",
            "unit": "", "mass_t": "", "binder_kg_per_m3": "", "ef": P["construction_other_uplift"], "ef_unit": "x bulk",
            "t_co2e": round(R["other_constr_kg"] / 1000), "basis": "assumption (construction_other_uplift)"})
with open(RESULTS / "lca_inventory.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(inv[0].keys()))
    w.writeheader()
    w.writerows(inv)

# ---------------- stages ----------------
tot = R["total_g"]
stages = []
for k, g in R["g"].items():
    stages.append({"stage": k, "g_per_kwh": round(g, 4), "t_per_unit_life": round(g * R["mwh_life"] / 1000),
                   "share_pct": round(100 * g / tot, 1)})
stages.append({"stage": "TOTAL", "g_per_kwh": round(tot, 3), "t_per_unit_life": round(R["total_t_life"]), "share_pct": 100.0})
with open(RESULTS / "lca_stages.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(stages[0].keys()))
    w.writeheader()
    w.writerows(stages)

groups = {
    "Construction (all)": R["construction_g"],
    "Fuel front end (mining to fabrication)": R["fuel_g"],
    "Operation and maintenance": R["g"]["Operation and maintenance"],
    "Back end and decommissioning": R["g"]["Decommissioning"] + R["g"]["Back end: spent fuel and disposal"],
}
by_material = {
    "Concrete (all)": R["g"]["Construction: concrete"],
    "Steel (rebar + plate/equipment)": R["g"]["Construction: rebar"] + R["g"]["Construction: plate, structural and equipment steel"],
    "C1-eligible concrete (40% of plant)": R["target_concrete_kg"] / R["mwh_life"],
}

# ---------------- fuel ----------------
mwh_yr = R["mwh_yr"]
fuel = [
    {"quantity": "Net efficiency (net MWe / MWt)", "per_MWh": "", "per_year_1_unit": round(R["eta"], 4), "per_year_4_units": ""},
    {"quantity": "Feed factor (kg natural U per kg enriched U)", "per_MWh": "", "per_year_1_unit": round(R["feed"], 3), "per_year_4_units": ""},
    {"quantity": "SWU per kg enriched U", "per_MWh": "", "per_year_1_unit": round(R["swu_per_kg"], 3), "per_year_4_units": ""},
    {"quantity": "Enriched U (kg)", "per_MWh": round(R["encU_kg_per_mwh"] * 1000, 3),
     "per_year_1_unit": round(R["encU_kg_per_mwh"] * mwh_yr / 1000, 2), "per_year_4_units": round(4 * R["encU_kg_per_mwh"] * mwh_yr / 1000, 2)},
    {"quantity": "Natural U (kg)", "per_MWh": round(R["natU_kg_per_mwh"] * 1000, 3),
     "per_year_1_unit": round(R["natU_kg_per_mwh"] * mwh_yr / 1000, 1), "per_year_4_units": round(4 * R["natU_kg_per_mwh"] * mwh_yr / 1000, 1)},
    {"quantity": "Separative work (SWU)", "per_MWh": round(R["swu_per_mwh"] * 1000, 3),
     "per_year_1_unit": round(R["swu_per_mwh"] * mwh_yr / 1000, 1), "per_year_4_units": round(4 * R["swu_per_mwh"] * mwh_yr / 1000, 1)},
]
fuel_units = "per_MWh column: g U per MWh, or SWU per GWh; per-year columns: t U, or tSWU (thousand SWU)"
with open(RESULTS / "lca_fuel.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(fuel[0].keys()))
    w.writeheader()
    w.writerows(fuel)

# ---------------- corrected inventory sheet (Sam's Accounting.xlsx left untouched) ----------------
fore_ef = per_m3(P["binder_conv_kg_per_m3"])
acc = [
    {"row": 1, "lca_sheet": "SMR Parts LCA (construction)", "structure": "Unit 1 forebay shaft (CCW system)", "material": "Concrete",
     "quantity": 4000, "unit": "m3", "mass_kg": 4000 * CONCRETE_DENSITY_T_PER_M3 * 1000,
     "scope": "PARTIAL: one construction milestone of one structure of Unit 1; not the whole plant",
     "quantity_source": "opg_forebay_update [TO VERIFY]", "ef": round(fore_ef, 1), "ef_unit": "kg CO2e/m3 (S0, A1-A3)",
     "ef_source": "cac2020_epd x binder_conv + ef_concrete_other (parameters_lca.yaml)",
     "t_co2e_A1A3": round(4000 * fore_ef / 1000),
     "correction": "Moved from 'Nuclear Fuel LCA' to construction; labelled partial (review.md items 3-4); 2.4 t/m3 density kept (arithmetic correct)"},
    {"row": 2, "lca_sheet": "SMR Parts LCA (construction)", "structure": "Unit 1 forebay shaft (CCW system)", "material": "Reinforcing steel",
     "quantity": 1000, "unit": "t", "mass_kg": 1_000_000,
     "scope": "PARTIAL: as row 1", "quantity_source": "opg_forebay_update [TO VERIFY]", "ef": P["ef_rebar"],
     "ef_unit": "t CO2e/t (A1-A3)", "ef_source": src("ef_rebar"), "t_co2e_A1A3": round(1000 * P["ef_rebar"]),
     "correction": "Recycled-content basis stated (North American EAF), not virgin steel (plan 2.1 trap); volume 127.4 m3 is not a bored volume"},
    {"row": 3, "lca_sheet": "SMR Parts LCA (construction)", "structure": "Unit 1 DPSC basemat module", "material": "Steel plate (diaphragm-plate steel composite)",
     "quantity": P["dpsc_basemat_steel_t"], "unit": "t", "mass_kg": P["dpsc_basemat_steel_t"] * 1000,
     "scope": "PARTIAL: steel only; infill concrete not reported", "quantity_source": src("dpsc_basemat_steel_t"),
     "ef": P["ef_plate_other"], "ef_unit": "t CO2e/t (A1-A3)", "ef_source": src("ef_plate_other"),
     "t_co2e_A1A3": round(P["dpsc_basemat_steel_t"] * P["ef_plate_other"]), "correction": "New row (plan 2.5 item 4)"},
    {"row": 4, "lca_sheet": "SMR Parts LCA (construction)", "structure": "Tunnel boring (CCW tunnels)", "material": "Excavated rock (not a material input)",
     "quantity": "", "unit": "m3", "mass_kg": "", "scope": "TODO",
     "quantity_source": "[TODO: tunnel length x bored cross-section from OPG/CNSC]", "ef": "", "ef_unit": "", "ef_source": "",
     "t_co2e_A1A3": "", "correction": "Assumptions.docx's 4,127.29 m3 is concrete (4,000) + rebar (127.39), NOT the bored volume (review.md item 2); TBM energy sits in the construction uplift until data exist"},
]
for i, row in enumerate(inv[:4], start=5):
    acc.append({"row": i, "lca_sheet": "SMR Parts LCA (construction)", "structure": f"Whole unit, scaled: {row['item']}",
                "material": row["material"], "quantity": row["quantity"], "unit": row["unit"],
                "mass_kg": row["mass_t"] * 1000 if row["mass_t"] != "" else "",
                "scope": "WHOLE-UNIT ESTIMATE per unit (Ostrołęka PIS quantities; parameters_lca.yaml section B0)", "quantity_source": row["basis"],
                "ef": row["ef"], "ef_unit": row["ef_unit"], "ef_source": "parameters_lca.yaml", "t_co2e_A1A3": row["t_co2e"],
                "correction": "New: replaces the forebay-only rows as the whole-plant inventory"})
with open(ROOT / "Accounting_corrected.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(acc[0].keys()))
    w.writeheader()
    w.writerows(acc)

# ---------------- markdown ----------------
v = R["vol"]
L = []
L.append("Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, RB.5\n")
L.append("# LCA baseline (S0), generated by `scripts/lca_baseline.py`\n")
L.append("Do not edit by hand: change `parameters_lca.yaml` and re-run. Every input is TO VERIFY, assumption or placeholder (see the YAML).\n")
L.append("## Lifetime output (functional-unit denominator)\n")
L.append(f"- {P['net_mwe']:.0f} MWe x 8,760 h x {P['capacity_factor']:.2f} = {fmt(R['mwh_yr'])} MWh/yr; x {P['design_life_yr']:.0f} yr = **{R['mwh_life']:.4g} MWh** per unit")
L.append(f"- Net efficiency {P['net_mwe']:.0f}/{P['thermal_mwt']:.0f} = {R['eta']:.3f}\n")
vx = RX["vol"]
L.append("## Concrete volume per unit\n")
L.append("| Part | Main case m3 | Working | Cross-check (bottom-up) m3 | Working |\n|---|---|---|---|---|")
L.append(f"| Whole plant | **{fmt(v['total'])}** | Ostrołęka PIS Table 14 | {fmt(vx['total'])} | {P['concrete_intensity_m3_per_mwe']} m3/MWe x {P['net_mwe']:.0f} MWe |")
L.append(f"| C1 target | **{fmt(v['target'])}** | {P['c1_eligible_share']:.0%} eligible | {fmt(vx['target'])} | DPSC basemat {fmt(vx['basemat'])} + walls {fmt(vx['wall'])} + forebay {fmt(vx['forebay'])} |")
L.append(f"| Other plant concrete | {fmt(v['other'])} | whole - target | {fmt(vx['other'])} | whole - target |")
L.append(f"| Steel (t) | {fmt(R['steel_t'])} | Ostrołęka PIS Table 14 | {fmt(RX['steel_t'])} | {P['steel_intensity_t_per_mwe']} t/MWe x {P['net_mwe']:.0f} |\n")
L.append("## Construction inventory per unit (S0)\n")
L.append("| Item | Quantity | Unit | Factor | t CO2e |\n|---|---|---|---|---|")
for r in inv:
    L.append(f"| {r['item']} | {fmt(r['quantity']) if r['quantity'] != '' else ''} | {r['unit']} | {r['ef']} {r['ef_unit']} | {fmt(r['t_co2e'])} |")
L.append(f"| **Construction total** | | | | **{fmt(R['construction_kg'] / 1000)}** |\n")
L.append(f"Steel total {fmt(R['steel_t'])} t (Ostrołęka PIS); concrete {fmt(R['concrete_kg'] / 1000)} t CO2e vs steel {fmt((R['rebar_kg'] + R['plate_kg']) / 1000)} t CO2e.\n")
L.append("## Results by stage (hotspot table)\n")
L.append("| Stage | g CO2e/kWh | t CO2e per unit (life) | Share |\n|---|---|---|---|")
for s in stages:
    b = "**" if s["stage"] == "TOTAL" else ""
    L.append(f"| {b}{s['stage']}{b} | {b}{s['g_per_kwh']:.3f}{b} | {b}{fmt(s['t_per_unit_life'])}{b} | {s['share_pct']:.1f}% |")
L.append("\n| Group | g CO2e/kWh | Share |\n|---|---|---|")
for k, g in groups.items():
    L.append(f"| {k} | {g:.3f} | {100 * g / tot:.1f}% |")
for k, g in by_material.items():
    L.append(f"| {k} | {g:.3f} | {100 * g / tot:.1f}% |")
L.append("\n## Fuel mass balance\n")
L.append(f"Units: {fuel_units}.\n")
L.append("| Quantity | per MWh | 1 unit / yr | 4 units / yr |\n|---|---|---|---|")
for r in fuel:
    L.append(f"| {r['quantity']} | {r['per_MWh']} | {r['per_year_1_unit']} | {r['per_year_4_units']} |")
L.append(f"\nWorking: kWh_e per kg enriched U = burnup {P['burnup_gwd_per_t']:.0f} GWd/t x 24,000 kWh_th per kg U per (GWd/t) x {R['eta']:.3f} = "
         f"{P['burnup_gwd_per_t'] * 24000 * R['eta']:,.0f}. Feed = (xp - xt)/(xf - xt) with xp {P['enrichment_pct']}%, xf {P['feed_assay_pct']}%, xt {P['tails_assay_pct']}%. "
         "SWU = V(xp) + (F - 1)V(xt) - F V(xf), V(x) = (2x - 1) ln(x/(1 - x)).")
L.append("\n## Cross-check: bottom-up 21/10 model (S0, mode case)\n")
L.append("| Quantity | Main (Ostrołęka) | Cross-check (bottom-up) |\n|---|---|---|")
for lab, a, b in [("Concrete m3/unit", v["total"], vx["total"]), ("Steel t/unit", R["steel_t"], RX["steel_t"]),
                  ("Concrete t CO2e", R["concrete_kg"] / 1000, RX["concrete_kg"] / 1000),
                  ("Steel t CO2e", (R["rebar_kg"] + R["plate_kg"]) / 1000, (RX["rebar_kg"] + RX["plate_kg"]) / 1000),
                  ("Construction t CO2e", R["construction_kg"] / 1000, RX["construction_kg"] / 1000),
                  ("Life cycle t CO2e/unit", R["total_t_life"], RX["total_t_life"])]:
    L.append(f"| {lab} | {fmt(a)} | {fmt(b)} |")
L.append(f"| Construction g/kWh | {R['construction_g']:.3f} | {RX['construction_g']:.3f} |")
L.append(f"| Life cycle g/kWh | {R['total_g']:.3f} | {RX['total_g']:.3f} |")
(RESULTS / "lca_baseline.md").write_text("\n".join(L) + "\n")

# F2 (stage breakdown) is drawn by lca_uncertainty.py on an expected-value basis, with this mode case marked.
lp.style()

# ---------------- F1: system boundary ----------------
fig, ax = lp.plt.subplots(figsize=(9.5, 5.4))
ax.set_xlim(0, 100)
ax.set_ylim(0, 60)
ax.axis("off")


def box(x, y, w, h, text, fc, ec=lp.INK2, bold=False, fs=8.5):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.4,rounding_size=1.2", fc=fc, ec=ec, lw=1.0))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=lp.INK, weight="bold" if bold else "normal", wrap=True)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=lp.INK2, lw=1.0))


FUEL, CONS, LIT, CORE = "#dceafa", "#d6f2e7", "#e9e6fa", "#fbe1d6"
ax.add_patch(FancyBboxPatch((1, 6), 98, 50, boxstyle="round,pad=0.3,rounding_size=2", fc="none", ec=lp.INK2, lw=1.2, ls="--"))
ax.text(2.5, 54, "System boundary: cradle to grave, GWP100", fontsize=9, color=lp.INK2, weight="bold")
fy = 42
for i, t in enumerate(["Mining and\nmilling\n(Saskatchewan)", "Conversion\n(UF6, Ontario)", "Enrichment\n(centrifuge)", "Fuel\nfabrication\n(GNF2)"]):
    box(3 + i * 15, fy, 12, 9, t, FUEL)
    if i:
        arrow(3 + i * 15 - 3, fy + 4.5, 3 + i * 15, fy + 4.5)
box(63, 30, 21, 14, "BWRX-300 operation\nDarlington, Clarington ON\n300 MWe net, 60 yr", CORE, bold=True, fs=7.4)
arrow(60, fy + 4.5, 63, 40)
box(87.5, 31, 11, 12, "1 MWh net\nelectricity\n(functional\nunit)", "#ffffff", ec=lp.INK, bold=True, fs=7.5)
arrow(84.5, 37, 87.5, 37)
box(3, 24, 27, 11, "Construction materials:\n50,000 m³ concrete, 14,000 t steel\n(rebar, DPSC plate, equipment)", CONS, fs=7.6)
box(33, 24, 22, 11, "C1: eligible concrete\n(20/40/60% of plant)\nOPC → LC³ (slag fallback)", CORE, ec=lp.ORANGE, bold=True, fs=8)
box(3, 10, 22, 9, "Transport to site;\nother materials,\nsite energy (uplift)", CONS)
arrow(55, 29.5, 63, 33)
box(28, 10, 16, 9, "Operation and\nmaintenance", LIT)
box(47, 10, 16, 9, "Decommissioning", LIT)
box(66, 10, 22, 9, "Back end: spent fuel\nstorage and deep\ngeological repository", LIT)
arrow(74, 30, 74, 19)
ax.text(2.5, 2.2, "Blue: fuel, per kg U (this study). Green: materials (Ostrołęka quantities, this study). Purple: literature per kWh (EDF 2024 shares).\n"
        "Cut off: grid transmission beyond the plant, cladding and fuel hardware manufacture, conversion chemicals, fuel-plant capital goods, recycling credits.",
        fontsize=7.6, color=lp.INK2)
# no embedded title: the Word caption carries "Figure F1" (review.md section 6 point 9)
lp.save(fig, RESULTS / "F1_system_boundary.png")

print(f"Cross-check bottom-up S0: {RX['total_g']:.3f} g/kWh; construction {RX['construction_g']:.3f}")
print(f"Baseline S0 (main): {tot:.3f} g CO2e/kWh; {R['total_t_life']:,.0f} t CO2e per unit-life; concrete {v['total']:,.0f} m3/unit "
      f"(target {v['target']:,.0f}); construction {R['construction_g']:.3f} g/kWh; fuel front end {R['fuel_g']:.3f} g/kWh")
