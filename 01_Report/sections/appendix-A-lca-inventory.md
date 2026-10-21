Rubric coverage: RB.5, R2.2, R2.4 (also supports R2.1, R2.3, R2.5, R2.7, R5.2)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/lca.md` §2, §3 and §12, `lca_baseline.md`, `lca_scenarios.md`, `lca_inventory.csv`, `Accounting_corrected.csv`, `parameters_lca.yaml`, `granta_inputs.md` and `02_Research/sources_lca.md`. Cited from §6 as Appendices A3, A5, A6 and A9.
  - review.md "For Sam" items 1–4: the corrections the lca-analyst made in `Accounting_corrected.csv` are listed in A4. Sam's `Assumptions.docx` and `Accounting.xlsx` are untouched.
  - factcheck.md S17: A3 states that plant quantities are scaled from per-MWe intensities, with the forebay and basemat as the only measured structures.
  - plan §2.1 "virgin rebar trap": rebar uses an electric-arc-furnace (recycled-content) factor (A5).
  - Granta: A9 gives the set-up and the model values Granta should be compared with. **No Granta result exists; the result cells say [TODO: results pending].**
- Presentation items: R5.1 (each subsection opens with its result); R5.2 (Tables A1–A10, caption and source above each); R5.3 (prose limited to the steps; appendices do not count towards the page limit); R5.4 (Harvard, same author forms as §6); R5.5 (Australian English).
- Every input is unverified. All [TO VERIFY] markers are kept.
-->

## Appendix A. LCA inventory and calculations

This appendix gives the full working behind §6. The analysis is an **equivalent analysis built from published factors**: a Python model multiplies quantities by emission factors. It is not a Granta EduPack run; the Granta cross-check is set up in A9 [TODO: results pending]. **No input has yet been checked against its primary source** (`status: TO VERIFY`, `assumption` or `placeholder` in `parameters_lca.yaml`), so every number here is provisional.

### A1. Reproducing the results

Every table and figure in §6 and Appendices A and C regenerates in about five seconds from one parameter file. If a value changes, edit `parameters_lca.yaml` and re-run the three scripts.

*Table A1. Scripts, inputs and outputs.*
*Source: `03_LCA_Calculations/`.*

| Step | Command (from the repository root) | Output |
|---|---|---|
| Baseline inventory, fuel mass balance, stage totals | `python3 -I 03_LCA_Calculations/scripts/lca_baseline.py` | `results/lca_baseline.md`, `lca_inventory.csv`, `lca_stages.csv`, `lca_fuel.csv`, Figure F1 |
| Initiative scenarios S1, S2, S2b, S3 | `python3 -I 03_LCA_Calculations/scripts/lca_scenarios.py` | `results/lca_scenarios.md`, `lca_scenarios.csv`, `lca_scenarios_structures.csv` |
| Tornado and Monte Carlo (Appendix C) | `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py` | `results/lca_uncertainty.md`, `lca_tornado.csv`, `lca_montecarlo_summary.csv`, `lca_stages_expected.csv`, Figures F2–F5 |

All three scripts read only `03_LCA_Calculations/parameters_lca.yaml` (59 parameters, each with a value, range, distribution, source key and status).

### A2. Functional unit and lifetime output

**Result.** One unit delivers 1.419 × 10⁸ MWh over its life, the denominator for every per-MWh value in §6 and §7.

- Annual output = P_net × 8,760 h × CF = 300 MWe × 8,760 × 0.90 = 2,365,200 MWh/yr.
- Lifetime output E = annual output × L = 2,365,200 × 60 = **1.419 × 10⁸ MWh**.
- Net efficiency η = P_net / P_th = 300 / 870 = **0.345** (870 MWt: [TODO: authors], 2025) [TO VERIFY].
- Conversion to the functional unit: 1 t CO₂e spread over E is 7.05 × 10⁻⁶ kg CO₂e/MWh (= g/kWh).

Inputs: P_net 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.) [placeholder; 315 MW net in an OPG filing, TO VERIFY]; CF 0.90 [placeholder, assumption shared with §7]; L 60 years (Canadian Nuclear Safety Commission, 2024) [TO VERIFY; 65 years reported elsewhere].

### A3. Material quantities per unit

**Result.** About 20,700 m³ of concrete and 9,900 t of steel per unit, of which 13,081 m³ of concrete is in the C1 target structures. **These are scaled estimates, not measured quantities**: no BWRX-300 bill of materials could be opened (searched: OPG's EIS review report NK054-REP-07730-00055-R001, TVA's Clinch River environmental report ML25118A209 and SEIS ML26035A285, GEH NEDO-33914; only front matter or summaries were visible) [TODO: Leroy].

**Whole plant.** Concrete = I_c × P_net; steel = I_s × P_net.
- Central: ESBWR intensities, I_c = 69 m³/MWe and I_s = 33 t/MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY], because the BWRX-300 is derived from the ESBWR.
- Low: GE Vernova's claim of about 50% less concrete (and, in one release, steel) per MW than the ESBWR, giving 34.5 m³/MWe and 16.5 t/MWe (GE Vernova, n.d.) [TO VERIFY; manufacturer projection].
- High: ABWR, 138 m³/MWe and 46 t/MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY], standing in for small-plant scale penalties.
- **Assumption:** in the central case the claimed halving is offset by SMR diseconomies of scale.

**C1 target structures (geometry).** With D = 37 m (module diameter) and h = 35 m (shaft depth) (Ontario Power Generation, 2026) [TO VERIFY]:
- V_basemat = π/4 × D² × t_b = 0.7854 × 37² × 3.0 = **3,226 m³** (t_b = 3.0 m, assumption, range 2–4 m).
- V_wall = π × (D − t_w) × t_w × h = π × 35.5 × 1.5 × 35 = **5,855 m³** (t_w = 1.5 m, assumption, range 1–2 m).
- Forebay shaft = **4,000 m³** placed to date (Ontario Power Generation, 2025) [TO VERIFY]; a floor, with 6,000 m³ as the high value. Whether the forebay serves one unit or all four is [TODO: Leroy/OPG].

**Rebar.** Rebar = ρ × plant concrete = 0.15 t/m³ × 20,700 = 3,105 t (assumption; the forebay's observed 1,000 t / 4,000 m³ = 0.25 t/m³ is the high value, and DPSC modules use steel faceplates instead of most rebar). Plate, structural and equipment steel = 9,900 − 3,105 = 6,795 t, which includes the 953 t Unit 1 DPSC basemat module (Ontario Power Generation, 2026) [TO VERIFY]. The rebar ratio only splits total steel between two factors.

*Table A2. Concrete volume per unit.*
*Source: `results/lca_baseline.md`.*

| Part | m³ | Working |
|---|---:|---|
| DPSC basemat infill | 3,226 | π/4 × 37² × 3.0 m |
| DPSC shaft-wall infill | 5,855 | π × (37 − 1.5) × 1.5 × 35 m |
| Forebay shaft | 4,000 | OPG update (floor) |
| **C1 target structures** | **13,081** | Sum of the three (63% of the plant) |
| Other plant concrete | 7,619 | Whole plant − target |
| **Whole plant** | **20,700** | max(69 m³/MWe × 300 MWe, target) |

In 3.5% of Monte Carlo draws (706 of 20,000) the scaled plant fell below the target volume, and the plant volume was then set equal to the target (Appendix C1).

### A4. Corrected inventory and corrections to the team's spreadsheet

**Result.** The spreadsheet's forebay rows describe one milestone of one Unit 1 structure. They are kept, labelled PARTIAL, and whole-unit rows are added.

*Table A3. Corrected construction inventory (A1–A3, central case).*
*Source: `03_LCA_Calculations/Accounting_corrected.csv`; quantities as in A3; factors as in A5. All [TO VERIFY].*

| Row | Structure and material | Quantity | Scope | Factor | t CO₂e |
|---|---|---|---|---|---:|
| 1 | Unit 1 forebay shaft, concrete | 4,000 m³ (9.6 million kg) | PARTIAL (one milestone) | 328.9 kg CO₂e/m³ | 1,316 |
| 2 | Unit 1 forebay shaft, rebar | 1,000 t | PARTIAL | 0.97 t/t (EAF) | 970 |
| 3 | Unit 1 DPSC basemat module, steel plate | 953 t | PARTIAL (steel only) | 1.73 t/t | 1,649 |
| 4 | Tunnel boring (cooling-water tunnels) | [TODO: tunnel length × bored cross-section] | — | — | — |
| 5 | Whole unit: DPSC reactor-building infill | 9,081 m³ | Scaled estimate | 414.3 kg CO₂e/m³ | 3,762 |
| 6 | Whole unit: forebay shaft | 4,000 m³ | Scaled estimate | 328.9 kg CO₂e/m³ | 1,316 |
| 7 | Whole unit: other plant concrete | 7,619 m³ | Scaled estimate | 328.9 kg CO₂e/m³ | 2,506 |
| 8 | Whole unit: rebar | 3,105 t | Scaled estimate | 0.97 t/t | 3,012 |
| 9 | Whole unit: plate, structural and equipment steel | 6,795 t | Scaled estimate | 1.73 t/t | 11,755 |

Corrections made (review.md items 1–4):
1. **Site.** The Darlington New Nuclear Project is in Clarington, Ontario, not Ottawa (to be corrected in `Assumptions.docx` by its owner).
2. **Tunnel boring.** The 4,127.29 m³ in `Assumptions.docx` is the forebay concrete (4,000 m³) plus its rebar (127.39 m³), not a bored volume. Row 4 is a TODO; tunnel-boring energy sits in the construction uplift (A7) until data exist.
3. **Sheet.** Concrete and steel rows move from "Nuclear Fuel LCA" to "SMR Parts LCA (construction)".
4. **Scope.** Rows 1–3 are labelled PARTIAL; rows 5–9 are the whole-unit inventory used in §6.

Also corrected: the "[From X patent]" header is replaced by a source column; rebar uses a recycled-content (electric-arc furnace) factor, not virgin steel; construction electricity is not assumed renewable (the uplift covers site energy on the Ontario grid). Still unresolved: what preprint 202505.1533 in the team notes is [TODO].

### A5. Emission factors

**Result.** Every factor is a published North American or Canadian value where one was found, and an assumption otherwise. All are cradle-to-gate (A1–A3) GWP100.

*Table A4. Emission and energy factors used.*
*Source: `parameters_lca.yaml`; references as listed. All [TO VERIFY] unless marked as an assumption.*

| Factor | Central | Range | Unit | Reference |
|---|---|---|---|---|
| General-use (GU) cement | 854 | 796–898 | kg CO₂e/t | Cement Association of Canada (2022), Central region (which region covers Ontario is [TO VERIFY]); to be replaced by the St Marys Bowmanville EPD (NRMCA, 2021) |
| Slag cement | 146.6 | 93.4–146.6 | kg CO₂e/t | Slag Cement Association (n.d.); low = Lafarge NewCem plant EPD |
| LC3 binder cut vs GU | 37% | 30–43% | — | Median of five estimates (below) |
| Non-binder share of concrete (aggregates, water, admixtures, batching) | 30 | 15–60 | kg CO₂e/m³ | Assumption |
| Binder content: DPSC self-consolidating infill | 450 | 400–550 | kg/m³ | EFNARC (2005) gives 360–500 kg/m³ powder for SCC [TO VERIFY]; 450 and 550 are assumptions for a cement-rich nuclear mix |
| Binder content: other structural concrete | 350 | 300–420 | kg/m³ | Assumption |
| Clinker factor: GU; LC3 | 0.92; 0.50 | 0.90–0.95; 0.50–0.55 | t/t binder | Assumption; Scrivener et al. (2018) |
| Rebar (electric-arc furnace, fabricated) | 0.97 | 0.89–1.99 | t CO₂e/t | Concrete Reinforcing Steel Institute (2017); low = American Institute of Steel Construction (2022) limit; high = world average (Circular Ecology, 2019) |
| Plate, structural and equipment steel | 1.73 | 1.22–2.50 | t CO₂e/t | American Institute of Steel Construction (2022) fabricated-plate limit as a proxy; high is an assumption for forged and machined equipment |
| Heavy truck | 0.10 | 0.06–0.15 | kg CO₂e/t-km | Assumption |
| Mining and milling | 42 | 24–81 | kg CO₂e/kg U₃O₈ | Parker, McNaughton and Sparrow (2016), Saskatchewan, production-weighted |
| Conversion: electricity; heat | 11.8; 26 | 10.3–16.9; 26–665 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Centrifuge enrichment | 50 | 40–100 | kWh/SWU | Gibon and Hahn Menacho (2023) |
| Fuel fabrication | 36 | 36–50 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Grid: conversion (Ontario) | 0.0738 | 0.035–0.343 | kg CO₂e/kWh | The Atmospheric Fund (2025); low = Canada Energy Regulator (n.d.) |
| Grid: enrichment and fabrication (USA) | 0.373 | 0.05–0.637 (enrichment); 0.20–0.637 (fabrication) | kg CO₂e/kWh | US EPA (2024); lows are assumptions |
| Natural-gas heat | 0.202 | — | kg CO₂/kWh | IPCC (2006) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 | 0.17–0.67; 0.06–0.33; 0.28–1.11 | g CO₂e/kWh | EDF R&D (2024): 9%, 3% and 15% of 3.7 g/kWh; ranges are assumptions for transfer to one BWRX-300 |

**The LC3 cut (37%)** is the median of five published estimates of LC3's binder emissions against Portland cement: 30% (ENR, 2018); 34%, 700 → 465 kg CO₂/t (Development Alternatives, n.d.); 37%, 856 → 543 kg CO₂/t (LC3 Project, 2015); about 40% (Scrivener et al., 2018, as summarised in the EPFL abstract); 43%, 903.5 → 513.5 kg CO₂e/t (LACCEI, 2026) [TODO: authors]. All five are [TO VERIFY]; ENR is trade press and should be replaced if a primary is found (R1.4). The estimates come from Indian, Cuban and Latin American settings; an Ontario LC3 calcined with natural gas is untested.

**Check on the per-m³ model.** At 350 kg/m³ the model gives 328.9 kg CO₂e/m³ for S0 concrete, close to the Ontario industry baseline of 334 kg CO₂e/m³ for 35 MPa concrete and below the 417 kg CO₂e/m³ industry benchmark mix (Canadian Ready-Mixed Concrete Association, 2022) [TO VERIFY].

### A6. Concrete and the C1 scenarios

**Result.** LC3 cuts emissions from the target concrete by 1,734 t per unit (34%) and avoids 2,304 t of clinker; slag cuts them by 1,552 t (31%).

For each structure: **kg CO₂e = V × (b × EF_binder / 1,000 + c)**, where V is volume (m³), b binder content (kg/m³), EF_binder the binder factor (kg CO₂e/t) and c the non-binder share (30 kg/m³).
- S0 (general-use cement): EF_binder = 854 kg/t; clinker factor 0.92.
- S1 (slag, s = 40% of binder): EF_binder = (1 − s) × 854 + s × 146.6 = 0.6 × 854 + 0.4 × 146.6 = **571.0 kg/t**; clinker factor (1 − s) × 0.92 = 0.552.
- S2 (LC3-50): EF_binder = 854 × (1 − r) = 854 × 0.63 = **538.0 kg/t** (r = 37%); clinker factor 0.50; binder content × (1 + u), with u = 0 central (0–10% if LC3 needs extra binder to flow; assumption).
- Clinker (t) = V × b × clinker factor / 10⁶.

Worked example (DPSC infill, 9,081 m³ at 450 kg/m³):
- S0: 450 × 854 / 1,000 + 30 = 414.3 kg/m³; 9,081 × 414.3 / 1,000 = **3,762 t**.
- S2: 450 × 538.0 / 1,000 + 30 = 272.1 kg/m³; 9,081 × 272.1 / 1,000 = **2,471 t**; saving **1,291 t** (142.2 kg/m³).
- Clinker avoided: 9,081 × 450 × (0.92 − 0.50) / 10⁶ = **1,716 t**.

*Table A5. Savings per structure, one unit.*
*Source: `results/lca_scenarios.md`.*

| Structure | Scenario | m³ | Binder kg/m³ | S0 t CO₂e | Scenario t CO₂e | Saving t (kg/m³) | Clinker avoided t |
|---|---|---:|---:|---:|---:|---:|---:|
| DPSC reactor-building infill | S1 slag | 9,081 | 450 | 3,762 | 2,606 | 1,156 (127.3) | 1,504 |
| DPSC reactor-building infill | S2 LC3 | 9,081 | 450 | 3,762 | 2,471 | 1,291 (142.2) | 1,716 |
| Forebay shaft | S1 slag | 4,000 | 350 | 1,316 | 919 | 396 (99.0) | 515 |
| Forebay shaft | S2 LC3 | 4,000 | 350 | 1,316 | 873 | 442 (110.6) | 588 |

*Table A6. Scenario totals (central case).*
*Source: `results/lca_scenarios.md`. Units 2–4 = 3 × per unit (Unit 1's basemat and forebay are already placed).*

| Scenario | Saving t CO₂e/unit | Units 2–4 t CO₂e | Clinker avoided t/unit (Units 2–4) | % of target concrete | % of unit life cycle (mode case) | g/kWh saved |
|---|---:|---:|---:|---:|---:|---:|
| S1 slag in C1 target structures | 1,552 | 4,657 | 2,019 (6,057) | 30.6 | 0.405 | 0.0109 |
| **S2 LC3 in C1 target structures (the initiative)** | **1,734** | **5,201** | **2,304 (6,913)** | **34.1** | **0.452** | **0.0122** |
| S2b LC3 in targets + slag in all other concrete | 2,488 | 7,464 | 3,286 (9,857) | 49.0 | 0.649 | 0.0175 |
| S3 low: all steel at EAF / high-recycled-content factors | 3,714 | 11,142 | 0 | — | 0.969 | 0.0262 |
| S3 high: all steel at world-average factors | −8,399 | −25,198 | 0 | — | −2.192 | −0.0592 |

S3 rows are a sensitivity on the baseline steel, not part of C1 (positive = lower than S0). The life-cycle share uses the mode-case total (383,243 t per unit); at the Monte Carlo median the LC3 share is 0.29% (Appendix C4). Savings exclude the construction uplift (A7).

**Resource use per unit of output.** Clinker avoided by LC3 = 2,304 t / 1.419 × 10⁸ MWh = 0.016 kg/MWh (7.7 t/MWe). Concrete: 20,700 m³ × 2.4 t/m³ / 1.419 × 10⁸ MWh = 0.35 kg/MWh. Steel: 9,900 t / 1.419 × 10⁸ MWh = 0.070 kg/MWh.

### A7. Steel, transport and construction total

**Result.** Construction emits 34,381 t CO₂e per unit (0.24 g/kWh, mode case); steel emits about twice what concrete does.

- Steel: kg CO₂e = rebar × EF_rebar + other × EF_other = 3,105 × 0.97 + 6,795 × 1.73 = 3,012 + 11,755 = **14,767 t**.
- Transport to site (A4): concrete 20,700 m³ × 2.4 t/m³ × 15 km × 0.10 kg/t-km = 74.5 t; steel 9,900 t × 500 km × 0.10 kg/t-km = 495 t; total **570 t** (distances are assumptions; the cement plant is also in Clarington [TO VERIFY]).
- Other materials and site energy (copper, cabling, insulation, site diesel, Ontario-grid electricity, processing of equipment beyond steel production, tunnel boring): uplift of 50% (assumption, range 25–150%) on concrete + steel + transport: 0.5 × (7,584 + 14,767 + 570) = **11,460 t**.
- **Construction total** = 7,584 + 14,767 + 570 + 11,460 = **34,381 t**, or 34,381 / 1.419 × 10⁸ MWh = **0.242 g/kWh**.

*Table A7. Construction inventory per unit (S0, central case).*
*Source: `results/lca_baseline.md`.*

| Item | Quantity | Factor | t CO₂e |
|---|---|---|---:|
| DPSC reactor-building infill (basemat + shaft walls) | 9,081 m³ | 414.3 kg CO₂e/m³ | 3,762 |
| Forebay shaft (condenser cooling water) | 4,000 m³ | 328.9 kg CO₂e/m³ | 1,316 |
| Other plant concrete | 7,619 m³ | 328.9 kg CO₂e/m³ | 2,506 |
| Reinforcing steel (whole plant) | 3,105 t | 0.97 t CO₂e/t | 3,012 |
| Plate, structural and equipment steel (incl. DPSC faceplates) | 6,795 t | 1.73 t CO₂e/t | 11,755 |
| Transport to site | — | 0.10 kg CO₂e/t-km | 570 |
| Other materials and site energy | — | +50% of the above | 11,460 |
| **Construction total** | | | **34,381** |

### A8. Fuel cycle and life-cycle total

**Result.** The fuel front end emits 1.46 g/kWh in the mode case (54%) and 2.75 g/kWh on the expected basis (64%, Appendix C4). Four units need about 196 t of natural uranium and 138 tSWU a year.

Mass balance (inputs: burnup B = 45 GWd/t [placeholder, assumption]; product assay x_p = 3.8% U-235 [placeholder; [TODO: authors], 2025]; feed x_f = 0.711%; tails x_t = 0.25% [assumption]):
- Electricity per kg of enriched uranium = B × 24,000 kWh_th per kg per (GWd/t) × η = 45 × 24,000 × 0.345 = 372,414 kWh, so **2.685 g enriched U per MWh**.
- Feed factor F = (x_p − x_t) / (x_f − x_t) = (3.8 − 0.25) / (0.711 − 0.25) = **7.70**, so **20.68 g natural U per MWh**.
- Separative work per kg of product = V(x_p) + (F − 1) V(x_t) − F V(x_f), with V(x) = (2x − 1) ln[x / (1 − x)]: 2.986 + 6.70 × 5.959 − 7.70 × 4.869 = **5.42 SWU/kg**, so **0.0146 SWU per MWh**.
- U₃O₈ to uranium: 3 × 238.03 / (3 × 238.03 + 8 × 16.00) = 0.848 kg U per kg U₃O₈.

Stage emissions, kg CO₂e per MWh (= g/kWh), mode case:
- Mining and milling = 0.02068 kg U/MWh × 42 / 0.848 = 0.02068 × 49.5 = **1.024**.
- Conversion = 0.02068 × (11.8 kWh × 0.0738 + 26 kWh × 0.202) = 0.02068 × 6.12 = **0.127**.
- Enrichment = 0.002685 × 5.42 × 50 kWh/SWU × 0.373 = **0.272**.
- Fabrication = 0.002685 × 36 kWh × 0.373 = **0.036**.

*Table A8. Fuel demand.*
*Source: `results/lca_baseline.md`. Inputs are placeholders until Leroy supplies BWRX-300 fuel data.*

| Quantity | Per MWh | One unit per year | Four units per year |
|---|---:|---:|---:|
| Enriched uranium | 2.685 g | 6.35 t U | 25.4 t U |
| Natural uranium | 20.68 g | 48.9 t U | 195.6 t U |
| Separative work | 0.0146 SWU | 34.4 tSWU | 137.7 tSWU |

*Table A9. Life-cycle emissions by stage, mode case (every input at its central value).*
*Source: `results/lca_baseline.md`. The expected-value breakdown quoted in §6 is in Appendix C4.*

| Stage | g CO₂e/kWh | t CO₂e per unit (life) | Share |
|---|---:|---:|---:|
| Fuel: mining and milling | 1.024 | 145,336 | 37.9% |
| Back end: spent fuel and disposal | 0.560 | 79,471 | 20.7% |
| Operation and maintenance | 0.330 | 46,831 | 12.2% |
| Fuel: enrichment | 0.272 | 38,530 | 10.1% |
| Fuel: conversion | 0.127 | 17,967 | 4.7% |
| Decommissioning | 0.110 | 15,610 | 4.1% |
| Construction: plate, structural and equipment steel | 0.083 | 11,755 | 3.1% |
| Construction: other materials and site energy | 0.081 | 11,460 | 3.0% |
| Construction: concrete | 0.053 | 7,584 | 2.0% |
| Fuel: fabrication | 0.036 | 5,117 | 1.3% |
| Construction: rebar | 0.021 | 3,012 | 0.8% |
| Construction: transport to site | 0.004 | 570 | 0.1% |
| **Total** | **2.701** | **383,243** | **100%** |
| *Of which C1 target concrete (DPSC infill + forebay)* | *0.036* | *5,078* | *1.3%* |

Grouped (mode case): fuel front end 1.458 g/kWh (54.0%); back end and decommissioning 0.670 (24.8%); O&M 0.330 (12.2%); construction 0.242 (9.0%).

### A9. Granta EduPack Eco Audit cross-check [TODO: results pending]

**Status.** A Granta EduPack Eco Audit cross-check of the C1 target structures is set up but **has not been run**. Granta runs only on the team's machines; until the export is saved in `03_LCA_Calculations/results/granta/`, no number in the report comes from Granta. Purpose: an independent check of the construction-material factors where C1 acts, and the screenshot for this appendix (R2.2).

**Set-up** (full instructions in `results/granta_inputs.md`; under one hour):
- Product: "BWRX-300 Darlington unit, C1 target structures, S0"; life 60 years; static (no use-phase energy).
- Bill of materials: DPSC infill concrete 21,794 t (9,081 m³ × 2.4 t/m³); forebay concrete 9,600 t; forebay rebar 1,000 t (recycled content from the CRSI EPD [TODO]); DPSC basemat steel 953 t. Shaft-wall module steel is unknown and left out.
- Transport: concrete 15 km and steel 500 km by heavy truck.
- End of life: concrete downcycled, steel recycled; the end-of-life potential is reported separately and not netted (cut-off approach, §6.1).
- Scenarios, if custom materials are allowed: scale the concrete record's CO₂ footprint by 0.693 (S1) and 0.657 (S2) for the infill, and 0.699 (S1) and 0.664 (S2) for the forebay.
- Record: EduPack version, database, date and operator [TODO].

*Table A10. Granta Eco Audit against the model (A1–A3 materials, central case).*
*Source: model values from `results/granta_inputs.md` §7; Granta values [TODO: results pending].*

| Row | Model t CO₂e | Model kg CO₂e/kg | Granta t CO₂e | Difference |
|---|---:|---:|---|---|
| DPSC infill concrete (S0) | 3,762 | 0.173 | [TODO: results pending] | [TODO] |
| Forebay concrete (S0) | 1,316 | 0.137 | [TODO: results pending] | [TODO] |
| Forebay rebar | 970 | 0.97 | [TODO: results pending] | [TODO] |
| DPSC basemat steel | 1,649 | 1.73 | [TODO: results pending] | [TODO] |
| **Total, materials** | **7,697** | | [TODO: results pending] | [TODO] |
| Transport | about 145 | | [TODO: results pending] | [TODO] |
| S2 LC3 saving, concrete rows | 1,734 | | [TODO: results pending] | [TODO] |

How the comparison will be read: within about ±30% per row, Granta confirms the model. If Granta's concrete is much lower, its generic concrete probably has less cement than a nuclear self-consolidating mix; if its steel is much higher, its default is probably virgin steel. Either way both values are reported and the model is not adjusted to match. If the run is not done by the freeze, this subsection is cut and §6 relies on the equivalent analysis alone.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **RB.5 (full calculations in an appendix).** Produced: every formula with a worked example, every input with its source, the corrected inventory, and the reproduce commands. Missing: verified inputs.
- **R2.4 (methods clear, full working).** Produced: A2–A8 step by step, with the same symbols as the scripts. Missing: nothing structural.
- **R2.2 (eco-audit or equivalent).** Produced: the equivalent analysis in full, and the Granta set-up and comparison rule. Missing: the Granta run itself [TODO: results pending].

### Remaining TODOs

1. **[TO VERIFY, blocking]** Every factor in Table A4 and every quantity in A3 (priority order in `02_Research/sources_lca.md`). Re-run the three scripts and re-copy any value that moves.
2. **[TODO: results pending]** Run Granta (A9) and fill Table A10; add the screenshot.
3. **[TODO: Leroy]** Sourced whole-plant concrete and steel quantities, DPSC thicknesses, forebay per unit or shared, net MWe, CF, design life, burnup, enrichment.
4. **[TODO]** Tunnel length and bored cross-section (row 4 of Table A3); recycled content from the CRSI 2022 EPD; what preprint 202505.1533 is.
5. **[TODO: references]** Authors for the arXiv overview (2025) and LACCEI (2026); replace ENR (2018) with a primary; add NRMCA (2021) and Canada Energy Regulator (n.d.) forms consistently with `sources.md`.
