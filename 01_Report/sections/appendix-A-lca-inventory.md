Rubric coverage: RB.5, R2.2, R2.4 (also supports R2.1, R2.3, R2.5, R2.6, R2.7, R1.4, R5.2, R5.4)

<!--
CHANGELOG
- v5, 25/10/2026 (writer, final day; Victor owns Sam's red sections, Sam may review): re-based on `lca_rebase_deck.md` (Ostrołęka 50,000 m³ / 14,000 t main case; Pillai 380 vs 270 kg CO₂e/m³; C1 at 20/40/60% = 1,100/2,200/3,300 t). Key assumptions moved here from §6 as Table A2b; S2b and steel rows as Table A7b; the 20,700 m³ model is a cross-check (A3, A6); A9 cut to one sentence; okdiario geometry and every marker hedged or cut. Tables renumbered to follow the section numbers.
-->

## Appendix A. LCA inventory and calculations

This appendix gives the full working behind §6. The analysis is a screening LCA following ISO 14040/44 principles, not critically reviewed, in which a Python model multiplies quantities by published emission factors. The Ostrołęka and Pillai tables behind the main case could not be opened, so their values are taken as reported; other inputs are labelled as reported by a secondary source, an assumption or a placeholder. The intervals therefore describe the uncertainty in our inputs as found, not in verified data.

### A1. Reproducing the results

Every table and figure in §6 and Appendices A and C regenerates in about five seconds from one parameter file. To change a value, edit `parameters_lca.yaml` and re-run the three scripts.

*Table A1. Scripts, inputs and outputs.*
*Source: `03_LCA_Calculations/`.*

| Step | Command (from the repository root) | Output |
|---|---|---|
| Baseline inventory, fuel mass balance, stage totals | `python3 -I 03_LCA_Calculations/scripts/lca_baseline.py` | `results/lca_baseline.md`, `lca_inventory.csv`, `lca_stages.csv`, `lca_fuel.csv`, Figure F1 |
| Initiative scenarios | `python3 -I 03_LCA_Calculations/scripts/lca_scenarios.py` | `results/lca_scenarios.md`, `lca_scenarios.csv` |
| Tornado and Monte Carlo (Appendix C) | `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py` | `results/lca_uncertainty.md`, `lca_tornado.csv`, `lca_montecarlo_summary.csv`, `lca_stages_expected.csv`, Figures F2–F5 |

All three scripts read only `03_LCA_Calculations/parameters_lca.yaml` (68 parameters, each with a value, range, distribution, source key and status).

### A2. Functional unit, lifetime output and key assumptions

**Result.** One unit delivers 1.419 × 10⁸ MWh over its life, the denominator for every per-MWh value in §6 and §7.

- Annual output = P_net × 8,760 h × CF = 300 MWe × 8,760 × 0.90 = 2,365,200 MWh/yr.
- Lifetime output E = 2,365,200 × 60 = **1.419 × 10⁸ MWh**.
- Net efficiency η = P_net / P_th = 300 / 870 = **0.345** (870 MWt from Sun and Kurosaki, 2025, an unrefereed preprint).
- Conversion to the functional unit: 1 t CO₂e spread over E is 7.05 × 10⁻⁶ g/kWh.

Inputs: P_net 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.), with 315 MWe net in OPG's filing to the Ontario Energy Board (Ontario Power Generation, 2025b) as the upper bound; CF 0.90, a placeholder shared with §7; L 60 years (Canadian Nuclear Safety Commission, 2024; 65 years is reported elsewhere).

*Table A2a. Plant quantities and results per unit: main case and cross-check.*
*Source: this study; BWRX-300 Ostrołęka sp. z o.o. (2023), as reported in the project information sheet; Peterson, Zhao and Petroski (2005).*

| Quantity | Main case (Ostrołęka) | Cross-check (bottom-up) |
|---|---|---|
| Concrete per unit | 50,000 m³ (input range 40,000–60,000) | 20,700 m³ (69 m³/MWe × 300 MWe) |
| Concrete per MWe | 167 m³ | 69 m³ |
| Steel per unit | 14,000 t (11,200–16,800) | 9,900 t (33 t/MWe × 300 MWe) |
| Rebar; plate, structural and equipment steel | 7,500 t; 6,500 t | 3,105 t; 6,795 t |
| C1-eligible concrete | 20,000 m³ (40%; 10,000–30,000) | 13,081 m³ (infill and forebay shaft) |
| Construction, mode case | 57,600 t CO₂e (0.41 g/kWh) | 34,381 t (0.24 g/kWh) |
| Life cycle: mode case; Monte Carlo median (90% interval) | 2.86; 4.40 (3.24–6.05) g/kWh | 2.70; 4.20 (3.05–5.86) g/kWh |

*Table A2b. Key assumptions for one BWRX-300 at Darlington (all 45 ranged inputs in Appendix C, Table C2).*
*Source: `parameters_lca.yaml`; references as listed. Ranges are model input bounds, not result intervals.*

| Parameter | Central (input range) | Basis |
|---|---|---|
| Net output; capacity factor; design life | 300 MWe (300–315); 0.90 (0.80–0.95); 60 years (40–80) | GE Vernova Hitachi Nuclear Energy (n.d.); Ontario Power Generation (2025b); placeholder; Canadian Nuclear Safety Commission (2024) |
| Plant concrete; steel | 50,000 m³ (40,000–60,000); 14,000 t (11,200–16,800) | BWRX-300 Ostrołęka sp. z o.o. (2023), as reported; ±20% is our assumption |
| Baseline concrete factor (S0) | 380 kg CO₂e/m³ (330–420) | Pillai et al. (2019), as reported; range from Canadian Ready-Mixed Concrete Association (2022) Ontario values (334 and 417) |
| LC³ concrete factor; cut | 270 kg CO₂e/m³; 28.9% (22–39%) | Pillai et al. (2019), as reported; range is our assumption |
| Eligible share for LC³ | 40% (20–60%) | Assumption: non-safety works first; DPSC infill only if qualified |
| Rebar; plate and equipment steel | 0.97 (0.89–1.99); 1.73 (1.22–2.50) t CO₂e/t | Concrete Reinforcing Steel Institute (2017; a 2022 declaration supersedes it); American Institute of Steel Construction (2022), Buy Clean California limits as proxies |
| Other materials and site energy | +50% of bulk materials (25–150%) | Assumption |
| Mining and milling | 42 kg CO₂e/kg U₃O₈ (24–81) | Parker, McNaughton and Sparrow (2016) |
| Conversion heat; centrifuge enrichment | 26 kWh/kg U (26–665); 50 kWh/SWU (40–100) | Gibon and Hahn Menacho (2023) |
| Enrichment; burnup | 3.8% U-235 (3.4–4.95); 45 GWd/t (35–55) | Sun and Kurosaki (2025), unrefereed preprint; assumption (both placeholders) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh (×0.5 to ×2; decommissioning ×3) | EDF R&D (2024) stage shares as reported by secondary sources; back end by difference |
| Cross-check and slag inputs | GU cement 854 kg CO₂e/t (796–898); slag cement 146.6 (93.4–146.6); binder 350 kg/m³ | Cement Association of Canada (2022); Slag Cement Association (n.d.); assumption |

### A3. Material quantities per unit

**Result.** The main case is 50,000 m³ of concrete and 14,000 t of steel per unit, with 20,000 m³ (40%) eligible for C1. **These come from a Polish design (Ostrołęka) and are a proxy, not measured Darlington quantities.** We do not know whether they cover the whole site or the nuclear island, or whether the steel includes equipment; if equipment is excluded, the construction uplift (A7) covers it. Darlington's 35 m reactor shaft, forebay and tunnels may differ. No BWRX-300 bill of materials could be opened (searched: OPG's environmental impact statement review report, TVA's Clinch River environmental report, GEH's NEDO-33914; only front matter or summaries were visible).

- Rebar = ρ × plant concrete = 0.15 t/m³ × 50,000 = **7,500 t** (assumption; range 0.10–0.25, the high value being the forebay's observed 0.25). Plate, structural and equipment steel = 14,000 − 7,500 = **6,500 t**. Rebar is capped at total steel, so plate never goes negative.
- C1-eligible concrete = eligible share × plant concrete = 0.40 × 50,000 = **20,000 m³**; 10,000 and 30,000 m³ at 20% and 60%. The eligible share is a scenario, not data.
- The Monte Carlo 90% interval for plant concrete is 43,224–56,772 m³ (the input is triangular, 40,000–50,000–60,000 m³).

**Cross-check (bottom-up).** Concrete = I_c × P_net and steel = I_s × P_net, with the ESBWR's I_c = 69 m³/MWe and I_s = 33 t/MWe (Peterson, Zhao and Petroski, 2005), because the BWRX-300 descends from the ESBWR: 20,700 m³ and 9,900 t. The vendor claims about 50% less concrete per MW (GE Vernova, n.d.; 34.5 m³/MWe) and the ABWR has 138 m³/MWe; the central case assumes the claimed halving offsets small-plant scale penalties. The cross-check's C1 concrete, 13,081 m³, is the diaphragm-plate steel-composite (DPSC) infill (9,081 m³, from assumed module geometry and wall thicknesses) plus the forebay shaft (4,000 m³ placed to date; Ontario Power Generation, 2025c). Ostrołęka's 167 m³/MWe is 2.4 times the ESBWR's, which is why the main case has more construction emissions (Table A2a).

### A4. Construction inventory and corrections to the team spreadsheet

**Result.** Construction emits 57,600 t CO₂e per unit at the mode case (0.41 g/kWh); concrete and steel are about equal.

*Table A4. Construction inventory per unit (S0, mode case; production-stage factors).*
*Source: `results/lca_baseline.md`; factors as in A5.*

| Item | Quantity | Factor | t CO₂e |
|---|---|---|---:|
| C1-eligible concrete (40%) | 20,000 m³ | 380 kg CO₂e/m³ | 7,600 |
| Other plant concrete | 30,000 m³ | 380 kg CO₂e/m³ | 11,400 |
| Rebar | 7,500 t | 0.97 t CO₂e/t | 7,275 |
| Plate, structural and equipment steel | 6,500 t | 1.73 t CO₂e/t | 11,245 |
| Transport to site | concrete 15 km, steel 500 km | 0.10 kg CO₂e/t-km | 880 |
| Other materials and site energy | +50% of the above | | 19,200 |
| **Construction total** | | | **57,600** |

Corrections made to the team spreadsheet (kept as `Accounting_corrected.csv`; the originals are untouched):
1. **Site.** The Darlington New Nuclear Project is in Clarington, Ontario, not Ottawa.
2. **Tunnel boring.** The 4,127.29 m³ in the assumptions file is the forebay concrete (4,000 m³) plus its rebar (127.39 m³), not a bored volume. Tunnel-boring energy sits in the construction uplift until data exist.
3. **Scope.** The forebay and basemat-module rows describe one milestone of one Unit 1 structure and are labelled partial; the whole-unit rows replace them.
4. **Rebar** uses a recycled-content (electric-arc furnace) factor, not virgin steel, and construction electricity is not assumed renewable.

### A5. Emission factors

**Result.** Every factor is a published North American or Canadian value where one was found, and an assumption otherwise. Construction-material factors are cradle-to-gate (production stage). The impact category is climate change, GWP100; the US grid factors are CO₂ only, used as CO₂e, which understates slightly.

*Table A5. Emission and energy factors used.*
*Source: `parameters_lca.yaml`; references as listed.*

| Factor | Central | Range | Unit | Reference |
|---|---|---|---|---|
| Baseline concrete (OPC, M50) | 380 | 330–420 | kg CO₂e/m³ | Pillai et al. (2019), as reported; range from Canadian Ready-Mixed Concrete Association (2022) |
| LC³ concrete | 270 | cut 28.9% (22–39%) | kg CO₂e/m³ | Pillai et al. (2019), as reported; range assumed |
| Rebar (electric-arc furnace, fabricated) | 0.97 | 0.89–1.99 | t CO₂e/t | Concrete Reinforcing Steel Institute (2017); low = American Institute of Steel Construction (2022) limit; high = world average (Circular Ecology, 2019, read via a secondary) |
| Plate, structural and equipment steel | 1.73 | 1.22–2.50 | t CO₂e/t | American Institute of Steel Construction (2022): a Buy Clean California limit (a policy ceiling, not an industry average), used as a proxy; high assumed for forged equipment |
| Heavy truck | 0.10 | 0.06–0.15 | kg CO₂e/t-km | Assumption |
| Mining and milling | 42 | 24–81 | kg CO₂e/kg U₃O₈ | Parker, McNaughton and Sparrow (2016), Saskatchewan, production-weighted |
| Conversion: electricity; heat | 11.8; 26 | 10.3–16.9; 26–665 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Centrifuge enrichment | 50 | 40–100 | kWh/SWU | Gibon and Hahn Menacho (2023) |
| Fuel fabrication | 36 | 36–50 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Grid: conversion (Ontario) | 0.0738 | 0.035–0.343 | kg CO₂e/kWh | The Atmospheric Fund (2025); low = Canada Energy Regulator (n.d.) |
| Grid: enrichment and fabrication (USA) | 0.373 | 0.05–0.637 (enrichment); 0.20–0.637 (fabrication) | kg CO₂/kWh | US EPA (2024); lows assumed |
| Natural-gas heat | 0.202 | — | kg CO₂/kWh | IPCC (2006): 56,100 kg/TJ × 3.6 × 10⁻⁶ TJ/kWh; combustion only, upstream gas cut off |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 | 0.17–0.67; 0.06–0.33; 0.28–1.11 | g CO₂e/kWh | EDF R&D (2024): 9%, 3% and 15% of 3.7 g/kWh, shares as reported by secondary sources, back end by difference; ranges assumed for transfer to one BWRX-300 |
| *Cross-check and slag only:* GU cement | 854 | 796–898 (regional spread) | kg CO₂e/t | Cement Association of Canada (2022), Central region; St Marys Bowmanville declaration (NRMCA, 2021) to replace it |
| *Cross-check and slag only:* slag cement | 146.6 | 93.4–146.6 | kg CO₂e/t | Slag Cement Association (n.d.) |
| *Cross-check only:* binder content (infill; other) | 450; 350 | 400–550; 300–420 | kg/m³ | EFNARC (2005) for the SCC range; central and high assumed |
| *Cross-check only:* clinker factor GU; LC³ | 0.92; 0.50 | 0.90–0.95; 0.50–0.55 | t/t binder | Assumption; Scrivener et al. (2018) |

**The LC³ cut.** The main case takes the concrete-level cut from Pillai et al. (2019): 1 − 270/380 = 28.9%. This is below the binder-level cuts in five published estimates (30% to 43%, median 37%: ENR, 2018; Development Alternatives, n.d.; LC3 Project, 2015; Scrivener et al., 2018; LACCEI, 2026), as it should be, because aggregates, water and batching are unchanged. The range 22–39% is our assumption. The estimates come from Indian, Cuban and Latin American settings; an Ontario LC³ calcined with natural gas is untested.

**Check on the baseline factor.** 380 kg CO₂e/m³ lies between the cross-check's binder-level mixes (329 and 414) and between the Ontario industry baseline of 334 and the 417 benchmark mix (Canadian Ready-Mixed Concrete Association, 2022).

### A6. Concrete and the C1 scenarios

**Result.** LC³ on 40% of plant concrete saves 2,200 t CO₂e per unit (28.9% of that concrete's emissions) and avoids about 2,940 t of clinker; a slag blend saves 2,288 t.

**Baseline S0** is the concrete OPG would pour anyway, at 380 kg CO₂e/m³. We have seen neither OPG's mix nor any cement-type limit in the specification (GE-Hitachi Nuclear Energy, 2024). If OPG's mix already contains slag (40% of binder, in all plant concrete), LC³'s increment on the eligible concrete is −88 t per unit (−0.02% of the life cycle), so every saving below is then overstated.

- **LC³ (C1):** saving = V_eligible × (380 − 270) / 1,000 = 20,000 × 0.110 = **2,200 t**; 10,000 m³ gives 1,100 t and 30,000 m³ gives 3,300 t. Share of the mode-case life cycle: 2,200 / 406,462 = 0.54%; the Monte Carlo median is lower (0.36%) because the total grows with the skewed inputs while the saving barely moves (§6.4).
- **Slag (S1, fallback):** the model's binder-level cut for 40% slag is 0.4 × (1 − 146.6/854) = 33.1% of binder emissions, which is 30.1% of the concrete's (binder is 91% of a 350 kg/m³ mix's emissions), applied to 380 kg/m³: 20,000 × 0.114 = **2,288 t**.
- **Clinker (indicative):** clinker avoided = V × b × (0.92 − 0.50) / 1,000 with b = 350 kg/m³: 20,000 × 0.147 = **2,940 t**. Pillai's binder content is not known to us, so this is indicative.
- **Units 2–4** = 3 × per unit, because Unit 1's basemat is placed. Whether Unit 1's shaft-wall infill could still use LC³ is unknown.

*Table A6. C1 scenario totals, mode case. Shares divide by the mode-case life-cycle total of the row's own basis (main 406,462 t; cross-check 383,243 t).*
*Source: `results/lca_scenarios.md`.*

| Scenario | Saving t CO₂e/unit | Units 2–4 t | Clinker avoided t/unit (Units 2–4) | % of target concrete | % of unit life cycle | g/kWh saved |
|---|---:|---:|---:|---:|---:|---:|
| LC³ on 20% of plant concrete | 1,100 | 3,300 | 1,470 (4,410) | 28.9 | 0.271 | 0.0078 |
| **LC³ on 40% (central)** | **2,200** | **6,600** | **2,940 (8,820)** | **28.9** | **0.541** | **0.0155** |
| LC³ on 60% of plant concrete | 3,300 | 9,900 | 4,410 (13,230) | 28.9 | 0.812 | 0.0233 |
| Slag blend on the same 40% (fallback) | 2,288 | 6,865 | 2,576 (7,728) | 30.1 | 0.563 | 0.0161 |
| *Cross-check:* slag in infill and forebay | 1,552 | 4,657 | 2,019 (6,057) | 30.6 | 0.405 | 0.0109 |
| *Cross-check:* LC³ in infill and forebay | 1,734 | 5,201 | 2,304 (6,913) | 34.1 | 0.452 | 0.0122 |

Monte Carlo basis (median, with 5th–95th percentile; Table C4b): LC³ on 40% with eligibility, cut and volumes all varying, 2,217 t per unit (1,375–3,294) and 6,651 t for Units 2–4 (4,124–9,881), 0.35% of the life cycle (0.19–0.61%); at fixed eligibility 0.18% (20%), 0.36% (40%) and 0.54% (60%). Slag 2,140 t (1,310–3,238), 0.34% (0.18–0.60%). LC³ beats slag in 55% of draws.

**Resource use per unit of output.** Clinker avoided = 2,940 t / 1.419 × 10⁸ MWh = 0.021 kg/MWh (9.8 t per MWe). Concrete: 50,000 m³ × 2.4 t/m³ / 1.419 × 10⁸ MWh = 0.85 kg/MWh. Steel: 14,000 t / 1.419 × 10⁸ MWh = 0.099 kg/MWh.

### A7. Steel, transport and construction total

**Result.** Construction emits 57,600 t CO₂e per unit (0.406 g/kWh, mode case); concrete (19,000 t) and steel (18,520 t) are about equal.

- Concrete: 50,000 m³ × 380 = **19,000 t**. Steel: 7,500 × 0.97 + 6,500 × 1.73 = 7,275 + 11,245 = **18,520 t**.
- Transport to site (production-stage module A4): concrete 50,000 m³ × 2.4 t/m³ × 15 km × 0.10 kg/t-km = 180 t; steel 14,000 t × 500 km × 0.10 kg/t-km = 700 t; total **880 t** (distances assumed).
- Other materials and site energy (copper, cabling, insulation, site diesel and electricity, equipment beyond steel production, tunnel boring): 50% (assumption; range 25–150%) of concrete + steel + transport: 0.5 × 38,400 = **19,200 t**.
- **Construction total** = 19,000 + 18,520 + 880 + 19,200 = **57,600 t**, or 57,600 / 1.419 × 10⁸ MWh = **0.406 g/kWh**.

**Steel scenarios.** S3 is a sensitivity on the baseline steel, not part of C1; only the like-for-like row compares with C1's saving.
- **Like-for-like (target-structure steel only):** the known steel in the structures C1 targets at the low-end factors (plate 1.22, the Buy Clean California hot-rolled-sections limit; rebar 0.89): 953 t of Unit 1 basemat-module plate (as reported in press coverage of the module lift) × (1.73 − 1.22) + 1,000 t of forebay rebar (Ontario Power Generation, 2025c) × (0.97 − 0.89) = 486 + 80 = **566 t per unit**. Shaft-wall module steel is unknown and excluded, so this is a floor.
- **Whole-plant upper bound:** all 14,000 t at the same low factors: 7,500 × 0.08 + 6,500 × 0.51 = 600 + 3,315 = **3,915 t**. It is an upper bound because it applies a hot-rolled-sections factor to forgings and nuclear-grade plate, for which that factor is not shown to be feasible.
- **World average:** all steel at the high-range factors (rebar 1.99, plate 2.50): **−12,655 t**; world-average steel would add emissions.

*Table A7b. Further scenarios: slag elsewhere and steel (S2b, S3), mode case and Monte Carlo (median, 5th–95th percentile).*
*Source: `results/lca_scenarios.md` and `lca_uncertainty.md`. S3 rows are steel sensitivities, not part of C1; negative means more emissions than the baseline.*

| Scenario | Saving t CO₂e/unit: mode case; Monte Carlo | Units 2–4 t | Share of life cycle: mode case; Monte Carlo |
|---|---|---|---|
| S2b: LC³ on 40% plus slag in all other concrete (upper bound) | 5,633; 5,517 (4,346–6,841) | 16,898 | 1.39%; 0.89% (0.57–1.36) |
| S3 like-for-like: target-structure steel only | 566; 940 (415–1,580) | 1,698 | 0.14%; 0.15% (0.06–0.28) |
| S3 upper bound: all steel, best-practice sections factors | 3,915; 6,428 (2,521–11,486) | 11,745 | 0.96%; 1.03% (0.38–2.04) |
| S3 world-average steel | −12,655; −9,914 (−14,037 to −4,904) | −37,965 | −3.11%; −1.56% (−2.70 to −0.72) |

At the mode case LC³'s 2,200 t is 3.9 times the like-for-like steel saving (2.4 times at the Monte Carlo median) and 0.6 times the whole-plant upper bound (0.3 at the median). Within the structures C1 targets, concrete is the bigger lever; across the plant, steel is.

### A8. Fuel cycle and life-cycle total

**Result.** The fuel front end emits 1.46 g/kWh in the mode case (51%) and 2.76 g/kWh on the expected basis (62%, Appendix C3). Four units need about 196 t of natural uranium and 138 tSWU a year.

Mass balance (inputs: burnup B = 45 GWd/t, a placeholder; product assay x_p = 3.8% U-235, a placeholder from Sun and Kurosaki, 2025; feed x_f = 0.711%; tails x_t = 0.25%, an assumption):
- Electricity per kg of enriched uranium = B × 24,000 kWh_th per kg per (GWd/t) × η = 45 × 24,000 × 0.345 = 372,414 kWh, so **2.685 g enriched U per MWh**.
- Feed factor F = (x_p − x_t) / (x_f − x_t) = (3.8 − 0.25) / (0.711 − 0.25) = **7.70**, so **20.68 g natural U per MWh**.
- Separative work per kg of product = V(x_p) + (F − 1) V(x_t) − F V(x_f), with V(x) = (2x − 1) ln[x / (1 − x)]: 2.986 + 6.70 × 5.959 − 7.70 × 4.869 = **5.42 SWU/kg**, so **0.0146 SWU per MWh**.
- U₃O₈ to uranium: 3 × 238.03 / (3 × 238.03 + 8 × 16.00) = 0.848 kg U per kg U₃O₈.

Stage emissions, kg CO₂e per MWh (= g/kWh), mode case:
- Mining and milling = 0.02068 kg U/MWh × 42 / 0.848 = 0.02068 × 49.5 = **1.024**.
- Conversion = 0.02068 × (11.8 kWh × 0.0738 + 26 kWh × 0.202) = 0.02068 × 6.12 = **0.127**.
- Enrichment = 0.002685 × 5.42 × 50 kWh/SWU × 0.373 = **0.272**.
- Fabrication = 0.002685 × 36 kWh × 0.373 = **0.036**.

*Table A8a. Fuel demand.*
*Source: `results/lca_baseline.md`. Inputs are placeholders until BWRX-300 fuel data are available.*

| Quantity | Per MWh | One unit per year | Four units per year |
|---|---:|---:|---:|
| Enriched uranium | 2.685 g | 6.35 t U | 25.4 t U |
| Natural uranium | 20.68 g | 48.9 t U | 195.6 t U |
| Separative work | 0.0146 SWU | 34.4 tSWU | 137.7 tSWU |

*Table A8b. Life-cycle emissions by stage, mode case (every input at its central value).*
*Source: `results/lca_baseline.md`. The expected-value breakdown quoted in §6 is in Appendix C3.*

| Stage | g CO₂e/kWh | t CO₂e per unit (life) | Share |
|---|---:|---:|---:|
| Fuel: mining and milling | 1.024 | 145,336 | 35.8% |
| Back end: spent fuel and disposal | 0.560 | 79,471 | 19.6% |
| Operation and maintenance | 0.330 | 46,831 | 11.5% |
| Fuel: enrichment | 0.272 | 38,530 | 9.5% |
| Construction: other materials and site energy | 0.135 | 19,200 | 4.7% |
| Construction: concrete | 0.134 | 19,000 | 4.7% |
| Fuel: conversion | 0.127 | 17,967 | 4.4% |
| Decommissioning | 0.110 | 15,610 | 3.8% |
| Construction: plate, structural and equipment steel | 0.079 | 11,245 | 2.8% |
| Construction: rebar | 0.051 | 7,275 | 1.8% |
| Fuel: fabrication | 0.036 | 5,117 | 1.3% |
| Construction: transport to site | 0.006 | 880 | 0.2% |
| **Total** | **2.864** | **406,462** | **100%** |
| *Of which C1-eligible concrete (40% of plant)* | *0.054* | *7,600* | *1.9%* |

Grouped (mode case): fuel front end 1.458 g/kWh (50.9%); back end and decommissioning 0.670 (23.4%); O&M 0.330 (11.5%); construction 0.406 (14.2%).

### A9. Granta EduPack Eco Audit

A Granta EduPack Eco Audit cross-check was planned but not completed; the screening model in Appendix A is the basis of all results.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **RB.5, R2.4.** Produced: every formula with a worked example, every input with its basis, the inventory, the cross-check and reproduce commands. Missing: nothing structural.
- **R2.2.** Produced: the equivalent screening model in full. Missing: the Granta run (not completed).
- **R2.5, R2.6, R1.4.** Produced: S0 counterfactual and its consequence, design-proxy caveat, steel upper-bound caveat, sources by input. Missing: Ostrołęka and Pillai tables opened by a person.

### Remaining TODOs

None in the body. For a person: open Ostrołęka Table 14 and Pillai Table 2; Granta (needs Sam's machine).
