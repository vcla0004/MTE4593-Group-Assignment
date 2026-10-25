Rubric coverage: RB.5, R2.2, R2.4 (also supports R2.1, R2.5, R2.6, R1.4)

## Appendix A. LCA inventory and calculations

All calculations are reproducible from the Python scripts and parameter files in the team repository (03_LCA_Calculations).

This is a screening LCA (ISO 14040/44 principles). Ostrołęka and Pillai values are used as reported; other inputs are assumptions or placeholders.

### A1 Reproducing the results
Edit `parameters_lca.yaml` (68 parameters) and re-run `lca_baseline.py`, `lca_scenarios.py` and `lca_uncertainty.py` (`python3 -I 03_LCA_Calculations/scripts/<name>`). Outputs are in `03_LCA_Calculations/results/`.

### A2 Functional unit
- Annual output = 300 MWe × 8,760 h × 0.90 = 2,365,200 MWh/yr.
- Lifetime output E = 2,365,200 × 60 years = **1.419 × 10⁸ MWh**.
- Net efficiency = 300 / 870 MWt = **0.345** (Sun and Kurosaki, 2025, unrefereed preprint).
- Inputs: 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.; 315 in Ontario Power Generation, 2025b); capacity factor 0.90 (placeholder); life 60 years (Canadian Nuclear Safety Commission, 2024).

### A3 Material quantities per unit
- Main case (BWRX-300 Ostrołęka sp. z o.o., 2023, as reported): **50,000 m³ concrete, 14,000 t steel**, a Polish-design proxy rather than Darlington data.
- Rebar = 0.15 t/m³ × 50,000 = 7,500 t (assumption); plate and equipment steel = 14,000 − 7,500 = 6,500 t.
- C1-eligible concrete = 0.40 × 50,000 = **20,000 m³** (10,000 and 30,000 at 20% and 60%; a scenario, not data).
- Cross-check (Peterson, Zhao and Petroski, 2005; ESBWR 69 m³/MWe, 33 t/MWe): 20,700 m³ and 9,900 t.

### A4 Construction inventory
Construction emits **57,600 t CO₂e per unit** (mode case, 0.41 g/kWh).

| Item | Quantity × factor | t CO₂e |
|---|---|---:|
| Concrete (all) | 50,000 m³ × 380 kg/m³ | 19,000 |
| Rebar | 7,500 t × 0.97 | 7,275 |
| Plate and equipment steel | 6,500 t × 1.73 | 11,245 |
| Transport | 15 km concrete, 500 km steel, 0.10 kg/t-km | 880 |
| Other materials and site energy | +50% of above | 19,200 |

Spreadsheet corrections: site is Clarington, not Ottawa; 4,127.29 m³ is forebay concrete plus rebar, not a bored volume; rebar uses an electric-arc-furnace factor.

### A5 Emission factors
Climate change, GWP100; cradle-to-gate for materials. Source: `parameters_lca.yaml`.

| Factor | Central (range) | Reference |
|---|---|---|
| Baseline concrete | 380 (330–420) kg CO₂e/m³ | Pillai et al. (2019), as reported |
| LC³ concrete | 270 kg CO₂e/m³ (cut 28.9%) | Pillai et al. (2019), as reported |
| Rebar | 0.97 (0.89–1.99) t CO₂e/t | Concrete Reinforcing Steel Institute (2017) |
| Plate steel | 1.73 (1.22–2.50) t CO₂e/t | American Institute of Steel Construction (2022) |
| Mining and milling | 42 (24–81) kg CO₂e/kg U₃O₈ | Parker, McNaughton and Sparrow (2016) |
| Conversion; enrichment | 26 kWh/kg U (heat); 50 kWh/SWU | Gibon and Hahn Menacho (2023) |
| Grid: Ontario; USA | 0.0738; 0.373 kg CO₂e/kWh | The Atmospheric Fund (2025); US EPA (2024) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh | EDF R&D (2024), as reported |

LC³ cut: 1 − 270/380 = 28.9%.

### A6 Concrete and the C1 scenarios
- **LC³ (C1):** saving = 20,000 m³ × (380 − 270) / 1,000 = **2,200 t per unit** (1,100 at 20%; 3,300 at 60%); 2,200 / 406,462 = 0.54% of the mode-case life cycle.
- **Slag fallback:** 20,000 × 0.114 = 2,288 t.
- **Clinker avoided:** 20,000 × 350 kg/m³ × (0.92 − 0.50) / 1,000 = 2,940 t (indicative).
- **Units 2–4:** 3 × per unit = 6,600 t.
- Monte Carlo median for LC³ at 40%: 2,217 t per unit (1,375–3,294).

### A7 Steel, transport and construction total
- Concrete 19,000 t + steel 18,520 t (7,275 + 11,245) + transport 880 t + uplift 0.5 × 38,400 = 19,200 t = **57,600 t**.
- Per kWh: 57,600 / 1.419 × 10⁸ MWh = **0.406 g/kWh**.
- Steel sensitivity (not part of C1): target-structure steel only 566 t per unit; all steel at best-practice factors 3,915 t; world-average steel −12,655 t (adds emissions).

### A8 Fuel cycle and life-cycle total
Inputs: burnup 45 GWd/t and 3.8% U-235 (placeholders); tails 0.25%; feed 0.711%.
- Electricity per kg enriched U = 45 × 24,000 × 0.345 = 372,414 kWh → **2.685 g enriched U per MWh**.
- Feed factor = (3.8 − 0.25) / (0.711 − 0.25) = **7.70**; natural U = 20.68 g/MWh.
- Separative work = 5.42 SWU/kg → 0.0146 SWU/MWh.
- Four units need about **196 t natural U and 138 tSWU a year**.

| Stage (mode case) | g CO₂e/kWh | Share |
|---|---:|---:|
| Mining and milling | 1.024 | 35.8% |
| Back end | 0.560 | 19.6% |
| Operation and maintenance | 0.330 | 11.5% |
| Enrichment | 0.272 | 9.5% |
| Construction (all) | 0.406 | 14.2% |
| Conversion | 0.127 | 4.4% |
| Decommissioning | 0.110 | 3.8% |
| Fabrication | 0.036 | 1.3% |
| **Total** | **2.864** | **100%** |

Total 406,462 t CO₂e per unit. Fuel front end 1.458 g/kWh (50.9%).

### A9 Granta EduPack Eco Audit
Granta EduPack 2024 R1 Eco Audit, one BWRX-300, product life 30 years, country of use North America (team model; full reports in the repository, `03_LCA_Calculations/granta/`). Components: base concrete 120,000 t (user-defined record, 0.1583 kg CO₂e/kg, 0.90 MJ/kg); structural steel 6,000 t and modular steel 8,000 t (low-carbon steel, virgin, roll formed); transport by truck, 30 km for concrete and 200 km for steel; steel recycled at end of life, concrete not. In the LC³ case 48,000 t (40%) of the concrete uses the team's LC³ record (0.1533 kg CO₂e/kg, 0.603 MJ/kg).

*Table A9. Granta Eco Audit results for one unit (first life).*
*Source: Granta EduPack 2024 R1 Eco Audit reports, Base Reactor and LC3 Reactor (25 October 2026).*

| Phase | Base: CO₂e (t) | LC³: CO₂e (t) | Base: energy (TJ) | LC³: energy (TJ) |
|---|---:|---:|---:|---:|
| Material | 51,600 | 51,400 | 554 | 540 |
| Manufacture | 3,030 | 3,030 | 40.4 | 40.4 |
| Transport | 3,490 | 3,490 | 56.1 | 56.1 |
| Disposal | 686 | 686 | 9.8 | 9.8 |
| Total, first life | 58,900 | 58,600 | 660 | 646 |
| End-of-life potential (steel recycling) | −23,400 | −23,400 | −328 | −328 |

The concrete-only saving is (0.1583 − 0.1533) × 48,000 t = 240 t CO₂e; at Pillai et al.'s (2019) 0.1125 kg/kg it would be (0.1583 − 0.1125) × 48,000 t = 2,198 t, the 2,200 t used in the report. Spread over the 60-year functional unit, Granta's 58,900 t is 0.42 g CO₂e/kWh, against 0.50 g/kWh for construction in our model.

[Figure F9. Granta EduPack Eco Audit summary, climate change (kg CO₂e) by life phase: base reactor against LC³ reactor. Source: Granta EduPack 2024 R1, team model.]

[Figure F10. Granta EduPack Eco Audit summary, energy (MJ) by life phase: base reactor against LC³ reactor. Source: Granta EduPack 2024 R1, team model.]
