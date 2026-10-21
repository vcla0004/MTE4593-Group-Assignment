Rubric coverage: R2.2, R2.4, R2.5, RB.5

# Granta EduPack Eco Audit: set-up for the C1 target structures (one BWRX-300 unit)

For whoever runs Granta on a team machine (Victor, Leroy, or Sam if he returns). Target time: under one hour. **No Granta output exists yet. Nothing in the report may say "Granta shows ..." until this run is done and the export is saved in `03_LCA_Calculations/results/granta/`.** (The deck's slides 6 and 7 currently say Granta was used: see `lca.md` section 11.)

Why this run matters: R2.2 asks for "an eco-audit or equivalent analysis of impacts". Our Python model is the equivalent analysis for the whole life cycle; the Granta run is the independent check on the construction materials where C1 acts, and gives Appendix A its screenshot.

## 0. Before you start (5 min)
1. Record the EduPack version, the database (Level 3 Sustainability, or whichever has Eco Audit), and the date. They go in §6.1 of the report.
2. Make a folder `03_LCA_Calculations/results/granta/`.
3. Keep `results/lca_inventory.csv` open: every mass below comes from it (central case, 21/10/2026). If `parameters_lca.yaml` changes, re-run `scripts/lca_baseline.py` and use the new masses.

## 1. Product definition
- Eco Audit tool → new product. Name: `BWRX-300 Darlington unit, C1 target structures, S0`.
- Product life: **60 years** (`design_life_yr`).
- Functional unit for the report stays 1 MWh; Granta reports per product, so divide by the lifetime output **1.419 × 10⁸ MWh** (`lca_baseline.md`) to convert t CO₂e → g/kWh (1 t over 1.419 × 10⁸ MWh = 7.05 × 10⁻⁶ g/kWh).

## 2. Bill of materials (one row each)

| Row | Component | Granta material record (pick the closest) | Mass | Recycled content | Primary process | Source of the mass |
|---|---|---|---|---|---|---|
| 1 | DPSC infill, basemat + shaft walls | Concrete (generic, or the highest-strength concrete record available) | **21,794 t** (9,081 m³ × 2.4 t/m³) | 0% (Granta default; no recycled aggregate assumed) | None/default for concrete | Geometric estimate, `lca_baseline.md` (assumed thicknesses) |
| 2 | Forebay shaft concrete | Concrete (generic) | **9,600 t** (4,000 m³ × 2.4) | 0% | None/default | OPG update (partial, floor value) |
| 3 | Forebay rebar | Carbon steel (plain, low-carbon) | **1,000 t** | Set to the realistic EAF scrap share [TODO: read it from the CRSI 2022 EPD]; if no value is found, use Granta's "typical" and record which | Rolling (or Granta's default for bar) | OPG update (partial) |
| 4 | DPSC basemat steel module (Unit 1 value used for each unit) | Carbon steel or low-alloy steel (plate) | **953 t** | Granta "typical" | Rolling | OPG basemat story |

Notes:
- Row 4 covers the basemat module only. The shaft-wall modules' steel is unknown; do not invent it. Leave it out and say so in the caption.
- If your EduPack version allows a **user-defined material** (custom CO₂ footprint), add a second product for each scenario below. If not, run S0 only in Granta and state that S1/S2 come from the Python model.

## 3. Transport
| Stage | Vehicle | Distance | Applies to |
|---|---|---|---|
| Concrete (cement plant / ready-mix to site) | Truck, 32 t (or Granta's heavy-goods truck) | **15 km** (St Marys Cement, Bowmanville, also in Clarington; distance TO VERIFY) | Rows 1–2 |
| Steel (mill/fabricator to site) | Truck, 32 t | **500 km** (assumption) | Rows 3–4 |

## 4. Use phase
Static structure: no energy in use. Leave the use phase empty (or "static", 0 kWh).

## 5. End of life
- Concrete: **Downcycle** (crushed aggregate). Steel: **Recycle**.
- Report the **end-of-life potential** column separately. Our boundary uses the cut-off approach (no recycling credit in the total), so the report quotes Granta's totals **without** the EoL potential and shows the EoL potential as a note.

## 6. Scenarios (if custom records are allowed)
Make a custom concrete record for each mix by scaling the CO₂ footprint of Granta's concrete record by these ratios (from `lca_scenarios.md`, per m³ including the 30 kg/m³ non-binder share):

| Scenario | DPSC infill (450 kg binder/m³) ratio to S0 | Forebay (350 kg/m³) ratio to S0 |
|---|---|---|
| S1 slag 40% | 0.693 (287.0 / 414.3 kg CO₂e/m³) | 0.699 (229.9 / 328.9) |
| S2 LC3-50 | 0.657 (272.1 / 414.3) | 0.664 (218.3 / 328.9) |

For steel S3, rerun rows 3–4 at recycled content 0% (virgin) and at the EAF value; that is the steel recycled-content sensitivity.

## 7. What it should come close to (our model, A1–A3 materials, central case)

| Row | Our t CO₂e | Our per-kg factor | Basis |
|---|---|---|---|
| 1 DPSC infill (S0) | 3,762 | 0.173 kg CO₂e/kg | 450 kg GU/m³ × 854 kg/t + 30 kg/m³ |
| 2 Forebay (S0) | 1,316 | 0.137 kg CO₂e/kg | 350 kg GU/m³ |
| 3 Forebay rebar | 970 | 0.97 | CRSI 2017 EPD lead, EAF |
| 4 DPSC basemat steel | 1,649 | 1.73 | BCCA plate limit as proxy |
| **Total rows 1–4** | **7,697** | | |
| Transport (rows 1–4) | about 145 (concrete 31,394 t × 15 km = 47; steel 1,953 t × 500 km = 98; at 0.10 kg/t-km) | | |
| S2 LC3 saving, rows 1–2 | 1,734 | | `lca_scenarios.md` |

How to read the comparison:
- **Within about ±30% per row:** report Granta as confirming the model; quote both in Appendix A.
- **Concrete well below ours:** Granta's generic concrete probably has a lower cement content than nuclear self-consolidating infill. Check Granta's record (density, cement content if listed). Say this in §6.5; do not adjust our model to match.
- **Steel well above ours:** Granta's default steel is probably virgin (BOF) or world-average. That is the "virgin rebar trap" in plan §2.1: set the recycled content properly and quote both.
- **Never** copy our numbers into the Granta columns. If the run is not done by the freeze, the report says the eco-audit is "equivalent analysis" (Python, Appendix A) and omits Granta.

## 8. Export (5 min)
1. Export the Eco Audit summary table (energy and CO₂ by phase: material, manufacture, transport, use, disposal, EoL potential) to `results/granta/eco_audit_S0.xlsx` (and S1/S2 if run).
2. Screenshot the bar chart → `results/granta/eco_audit_S0.png` (Appendix A).
3. Write the totals into a new `results/granta/granta_results.md` with the version, database, date and who ran it. Tell the fact-checker.
