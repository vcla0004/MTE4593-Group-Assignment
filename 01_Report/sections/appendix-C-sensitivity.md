Rubric coverage: R2.7, RB.5 (also supports R2.4, R2.1, RB.6, R5.2)

<!--
CHANGELOG
- v2, 21/10/2026 (writer, for Victor). Revised against factcheck.md §H: L63 (C3: basemat thickness is geometry, not mix design); L65 (C4: why expected plate steel is below its mode value); L57 (construction 7.5% on the expected basis, C4 and C6); L61 (C6: "hybrid boundary" replaced); L67 (C4: the Monte Carlo 90% interval, 15,050–36,521 m³, is the concrete range to quote; Table C1 rows are input bounds); L5, L22, L25 (Table C1 source notes: cement regional spread; CRSI 2017 superseded; US grid CO₂ only); L55 (C4 note that the share row is LC3 only). Values unchanged; all [TO VERIFY] markers kept.
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/lca_uncertainty.md`, `lca_tornado.csv`, `lca_montecarlo_summary.csv`, `lca_stages_expected.csv`, `lca.md` §7–§8 and `parameters_lca.yaml`. Cited from §6.4 as Appendices C1, C2 and C4.
  - plan §4.1 acceptance tests: tornado with at least six sourced or justified ranges (40 here, each with its source and status); Monte Carlo with at least 10,000 draws (20,000), stated distributions, fixed seed, median and 5th–95th percentiles, reproducible from `scripts/`.
  - Correction to `lca.md` §7 carried here too: steel intensity moves the life-cycle total by 0.17 g/kWh, so "every construction-quantity input moves it by under 0.07" holds for concrete inputs only.
  - The mean-minus-mode column in Table C4 is our subtraction of two columns of `lca_uncertainty.md`; it sums to the 1.58 g/kWh gap.
- Presentation items: R5.1 (each subsection opens with its result); R5.2 (Tables C1–C4 with caption and source above; Figures F3 and F4 referenced); R5.3; R5.4; R5.5 (Australian English).
- Every input is unverified. All [TO VERIFY] markers are kept.
-->

## Appendix C. Sensitivity: tornado and Monte Carlo set-up and results

This appendix shows how uncertain the §6 results are and which inputs drive them. **The life-cycle intensity is uncertain mainly through the fuel inputs (conversion heat, mining, back end, burnup, enrichment); the LC3 saving is uncertain mainly through the LC3 emission cut, the DPSC geometry and the infill mix.** All ranges come from `parameters_lca.yaml`; every input is [TO VERIFY], an assumption or a placeholder, so the intervals describe the uncertainty in our *inputs as found*, not in verified data.

### C1. Set-up

- **Tornado (one at a time).** Each of the 40 ranged inputs is set to its low and then its high value, with every other input at its central value. Outputs: life-cycle g CO₂e/kWh and the LC3 saving (t CO₂e per unit). Inputs are ranked by the swing in life-cycle intensity.
- **Monte Carlo.** N = 20,000 draws; seed 20261021; generator `numpy.random.default_rng`. All 40 inputs are drawn **independently**: triangular (low, central, high) for 39 of them, and uniform 300–315 MWe for net output (the two values in the sources). Fixed parameters (thermal power, feed assay, U₃O₈ stoichiometry, the gas heat factor, the forebay rebar, the basemat steel and the module diameter) are not drawn.
- **Outputs.** 5th, 50th and 95th percentiles and the mean. Stage means are additive, so they sum to the expected total.
- **Rule for small plants.** If a draw's scaled whole-plant concrete is below the C1 target volume, the plant volume is set equal to the target. This happened in 706 of 20,000 draws (3.5%).
- **Mode case vs expected value.** The "mode case" (2.70 g/kWh) has every input at its central, most likely value. The expected value (Monte Carlo mean, 4.28) and median (4.18) include the skew of the ranges (C5).
- **Reproduce:** `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py` (writes `results/lca_uncertainty.md`, `lca_tornado.csv`, `lca_montecarlo_summary.csv`, `lca_stages_expected.csv` and Figures F2–F5).

### C2. Ranged inputs and tornado results

**Result.** Five fuel-cycle inputs each move the life-cycle total by more than 0.6 g/kWh. No concrete input moves it by more than 0.07 g/kWh; steel intensity moves it by 0.17.

*Table C1. The 40 ranged inputs, their sources, and the tornado results (ranked by swing in life-cycle intensity).*
*Source: `parameters_lca.yaml`; `results/lca_uncertainty.md`. Status: V = TO VERIFY (search lead), A = assumption, P = placeholder for Leroy's plant data. Distribution triangular unless stated. "—" = no effect on the LC3 saving (1,734 t). Low / central / high are model input bounds, not result intervals (results are in Table C2).*

| # | Input (unit) | Low / central / high | Source | Status | Life-cycle g/kWh at low → high (swing) | LC3 saving t at low → high |
|---:|---|---|---|---|---|---|
| 1 | Conversion heat (kWh/kg U) | 26 / 26 / 665 | Gibon and Hahn Menacho (2023) | V | 2.701 → 5.370 (2.669) | — |
| 2 | Mining and milling (kg CO₂e/kg U₃O₈) | 24 / 42 / 81 | Parker, McNaughton and Sparrow (2016) | V | 2.262 → 3.652 (1.390) | — |
| 3 | Back end (g/kWh) | 0.28 / 0.56 / 1.11 | EDF R&D (2024); range assumed | V | 2.421 → 3.251 (0.830) | — |
| 4 | Burnup (GWd/t) | 35 / 45 / 55 | Assumption | P | 3.117 → 2.435 (0.682) | — |
| 5 | Enrichment (% U-235) | 3.4 / 3.8 / 4.95 | [TODO: authors] (2025); low assumed | P | 2.530 → 3.193 (0.663) | — |
| 6 | O&M (g/kWh) | 0.17 / 0.33 / 0.67 | EDF R&D (2024); range assumed | V | 2.541 → 3.041 (0.500) | — |
| 7 | Enrichment-plant grid (kg CO₂e/kWh) | 0.05 / 0.373 / 0.637 | US EPA (2024), CO₂ only; low assumed | V | 2.466 → 2.893 (0.427) | — |
| 8 | Centrifuge energy (kWh/SWU) | 40 / 50 / 100 | Gibon and Hahn Menacho (2023) | V | 2.646 → 2.972 (0.326) | — |
| 9 | Decommissioning (g/kWh) | 0.06 / 0.11 / 0.33 | EDF R&D (2024); range assumed | V | 2.651 → 2.921 (0.270) | — |
| 10 | Other construction uplift (fraction) | 0.25 / 0.5 / 1.5 | Assumption | A | 2.660 → 2.862 (0.202) | — |
| 11 | Design life (years) | 40 / 60 / 80 | Canadian Nuclear Safety Commission (2024); bounds assumed | V | 2.822 → 2.640 (0.182) | — |
| 12 | Steel intensity (t/MWe) | 16.5 / 33 / 46 | Peterson, Zhao and Petroski (2005); GE Vernova (n.d.) | V | 2.607 → 2.774 (0.167) | — |
| 13 | Tails assay (% U-235) | 0.20 / 0.25 / 0.30 | Assumption | A | 2.636 → 2.796 (0.160) | — |
| 14 | Plate, structural and equipment steel (t CO₂e/t) | 1.22 / 1.73 / 2.50 | American Institute of Steel Construction (2022); high assumed | V | 2.664 → 2.756 (0.092) | — |
| 15 | Conversion grid, Ontario (kg CO₂e/kWh) | 0.035 / 0.0738 / 0.343 | The Atmospheric Fund (2025); Canada Energy Regulator (n.d.) | V | 2.691 → 2.766 (0.075) | — |
| 16 | Net output (MWe), uniform | 300 / 300 / 315 | GE Vernova Hitachi Nuclear Energy (n.d.); OPG filing | P | 2.701 → 2.631 (0.070) | — |
| 17 | Concrete intensity (m³/MWe) | 34.5 / 69 / 138 | Peterson, Zhao and Petroski (2005); GE Vernova (n.d.) | V | 2.683 → 2.748 (0.065) | — |
| 18 | Capacity factor | 0.80 / 0.90 / 0.95 | Assumption | P | 2.731 → 2.688 (0.043) | — |
| 19 | Fabrication grid (kg CO₂e/kWh) | 0.20 / 0.373 / 0.637 | US EPA (2024), CO₂ only; low assumed | V | 2.684 → 2.726 (0.042) | — |
| 20 | Rebar (t CO₂e/t) | 0.89 / 0.97 / 1.99 | Concrete Reinforcing Steel Institute (2017, superseded by 2022 EPD); American Institute of Steel Construction (2022); Circular Ecology (2019) | V | 2.698 → 2.734 (0.036) | — |
| 21 | Rebar ratio (t/m³) | 0.10 / 0.15 / 0.25 | Assumption (high = forebay) | A | 2.709 → 2.684 (0.025) | — |
| 22 | Steel transport (km) | 100 / 500 / 1,500 | Assumption | A | 2.696 → 2.711 (0.015) | — |
| 23 | Fabrication energy (kWh/kg U) | 36 / 36 / 50 | Gibon and Hahn Menacho (2023) | V | 2.701 → 2.715 (0.014) | — |
| 24 | Binder, other concrete (kg/m³) | 300 / 350 / 420 | Assumption | A | 2.695 → 2.708 (0.013) | 1,670 → 1,822 |
| 25 | Binder, DPSC infill (kg/m³) | 400 / 450 / 550 | EFNARC (2005); central and high assumed | V | 2.697 → 2.709 (0.012) | 1,590 → 2,021 |
| 26 | Conversion electricity (kWh/kg U) | 10.3 / 11.8 / 16.9 | Gibon and Hahn Menacho (2023) | V | 2.698 → 2.708 (0.010) | — |
| 27 | Non-binder concrete share (kg CO₂e/m³) | 15 / 30 / 60 | Assumption | A | 2.697 → 2.707 (0.010) | — |
| 28 | GU cement (kg CO₂e/t) | 796 / 854 / 898 | Cement Association of Canada (2022); range is the West–East regional spread | V | 2.696 → 2.704 (0.009) | 1,616 → 1,823 |
| 29 | Truck factor (kg CO₂e/t-km) | 0.06 / 0.10 / 0.15 | Assumption | A | 2.698 → 2.704 (0.005) | — |
| 30 | DPSC wall thickness (m) | 1.0 / 1.5 / 2.0 | Assumption | A | 2.699 → 2.702 (0.003) | 1,464 → 1,995 |
| 31 | Concrete transport (km) | 5 / 15 / 50 | Assumption | A | 2.700 → 2.702 (0.002) | — |
| 32 | DPSC basemat thickness (m) | 2.0 / 3.0 / 4.0 | Assumption | A | 2.700 → 2.702 (0.002) | 1,581 → 1,886 |
| 33 | Shaft depth (m) | 35 / 35 / 38 | Ontario Power Generation (2026); high = containment height, GE Vernova Hitachi Nuclear Energy (n.d.) | V | 2.701 → 2.701 (<0.001) | 1,734 → 1,805 |
| 34 | Forebay concrete (m³) | 4,000 / 4,000 / 6,000 | Ontario Power Generation (2025); high assumed | V | 2.701 → 2.701 (0) | 1,734 → 1,955 |
| 35 | Slag cement (kg CO₂e/t) | 93.4 / 146.6 / 146.6 | Slag Cement Association (n.d.) | V | no change (S1 only) | — |
| 36 | GU clinker factor | 0.90 / 0.92 / 0.95 | Assumption | A | no change (clinker tonnage only) | — |
| 37 | Slag share of binder, S1 | 0.25 / 0.40 / 0.50 | Assumption | A | no change (S1 only) | — |
| 38 | LC3 clinker factor | 0.50 / 0.50 / 0.55 | Scrivener et al. (2018) | V | no change (clinker tonnage only) | — |
| 39 | LC3 binder emission cut | 0.30 / 0.37 / 0.43 | Five estimates (Appendix A5) | V | no change | 1,406 → 2,015 |
| 40 | Extra binder LC3 needs for flow | 0 / 0 / 0.10 | Assumption | A | no change | 1,734 → 1,438 |

### C3. What the tornado shows

**Life-cycle intensity (Figure F3, left).** The ranking is dominated by the fuel chain. Conversion heat alone could double the result, because the published heat demand spans a factor of 25 (26–665 kWh/kg U). The mining factor ranks second because ore grade varies widely between Saskatchewan mines. Higher burnup *lowers* the result (less uranium per MWh), and higher enrichment raises it (more separative work). Of the construction inputs, only the uplift (0.20) and steel intensity (0.17) exceed 0.1 g/kWh.

**LC3 saving (Figure F3, right).** The saving depends on the LC3 emission cut (swing 609 t), DPSC wall thickness (532 t), infill binder content (430 t), basemat thickness (306 t), extra binder for flow (295 t), forebay volume (221 t) and the cement factor (207 t). The first two are the LC3 literature and OPG's drawings. Of the next three, binder content and extra binder are mix design and basemat thickness is geometry. Even at the lowest single-input value (1,406 t), LC3 saves more than the largest geometric swing, so the saving is robust in sign but uncertain by about ±20–25%.

### C4. Monte Carlo results

**Result.** Life-cycle intensity: **median 4.18, 90% interval 3.05–5.85 g CO₂e/kWh**. LC3 saving: **median 1,742 t per unit (1,387–2,153)**, **5,225 t for Units 2–4 (4,161–6,458)**. LC3 saves more than slag in **64%** of draws.

*Table C2. Monte Carlo outputs (20,000 draws, seed 20261021).*
*Source: `results/lca_uncertainty.md`, `lca_montecarlo_summary.csv`.*

| Output | Mode case | Mean | P5 | P50 | P95 |
|---|---:|---:|---:|---:|---:|
| Life-cycle intensity (g CO₂e/kWh) | 2.701 | 4.279 | 3.048 | 4.178 | 5.849 |
| Fuel front end (g/kWh) | 1.458 | 2.746 | 1.590 | 2.634 | 4.272 |
| of which mining and milling (g/kWh) | 1.024 | 1.258 | 0.753 | 1.214 | 1.891 |
| Construction (g/kWh) | 0.242 | 0.321 | 0.198 | 0.309 | 0.484 |
| Whole-plant concrete (m³ per unit) | 20,700 | 24,809 | 15,050 | 24,066 | 36,521 |
| C1 target concrete (m³ per unit) | 13,081 | 13,903 | 12,216 | 13,894 | 15,606 |
| LC3 saving (t CO₂e per unit) | 1,734 | 1,752 | 1,387 | 1,742 | 2,153 |
| LC3 saving, Units 2–4 (t CO₂e) | 5,201 | 5,256 | 4,161 | 5,225 | 6,458 |
| LC3 saving as share of the unit's life cycle (%) | 0.452 | 0.304 | 0.185 | 0.295 | 0.455 |
| Slag (S1) saving (t CO₂e per unit) | 1,552 | 1,649 | 1,205 | 1,642 | 2,113 |
| LC3 minus slag (t CO₂e per unit) | 181 | 103 | −343 | 97 | 574 |

The whole-plant concrete median (24,066 m³) sits above the central value (20,700 m³) because its input range is right-skewed (34.5–69–138 m³/MWe). **The 90% interval, about 15,050–36,521 m³, is the concrete range to quote**; the input bounds (10,350–41,400 m³) are not results, and the clip rule (C1) also lifts the low tail. The LC3-minus-slag interval spans zero: the two options cannot be separated on carbon with present data. The share row is for LC3 only; Monte Carlo shares for the other scenarios are not in the outputs [TODO: lca-analyst].

*Table C3. Expected life-cycle emissions by stage (Monte Carlo mean) against the mode case.*
*Source: `results/lca_uncertainty.md`; last column is our subtraction (mean − mode).*

| Stage | Mode case g/kWh | Mean g/kWh | P5 | P95 | Share of mean | Mean − mode |
|---|---:|---:|---:|---:|---:|---:|
| Fuel: mining and milling | 1.024 | 1.258 | 0.753 | 1.891 | 29.4% | +0.234 |
| Fuel: conversion | 0.127 | 1.094 | 0.227 | 2.390 | 25.6% | +0.967 |
| Back end: spent fuel and disposal | 0.560 | 0.654 | 0.389 | 0.963 | 15.3% | +0.094 |
| Operation and maintenance | 0.330 | 0.391 | 0.235 | 0.579 | 9.1% | +0.061 |
| Fuel: enrichment | 0.272 | 0.351 | 0.130 | 0.632 | 8.2% | +0.079 |
| Decommissioning | 0.110 | 0.167 | 0.086 | 0.276 | 3.9% | +0.057 |
| Construction: other materials and site energy | 0.081 | 0.138 | 0.060 | 0.252 | 3.2% | +0.057 |
| Construction: plate, structural and equipment steel | 0.083 | 0.073 | 0.021 | 0.133 | 1.7% | −0.010 |
| Construction: concrete | 0.053 | 0.066 | 0.040 | 0.102 | 1.5% | +0.013 |
| Fuel: fabrication | 0.036 | 0.044 | 0.027 | 0.063 | 1.0% | +0.007 |
| Construction: rebar | 0.021 | 0.038 | 0.018 | 0.068 | 0.9% | +0.017 |
| Construction: transport to site | 0.004 | 0.006 | 0.002 | 0.012 | 0.1% | +0.002 |
| **Total** | **2.701** | **4.279** | | | **100%** | **+1.578** |

Grouped (expected basis): fuel front end 64.2%, back end and decommissioning 19.2%, O&M 9.1%, construction 7.5% (0.321 / 4.279).

**Why plate steel falls (−0.010).** Plate steel is total steel minus rebar, and rebar scales with plant concrete (capped at total steel; Appendix A3). Concrete intensity is right-skewed (34.5–69–138 m³/MWe), so expected rebar rises above its mode value, while steel intensity is slightly left-skewed (16.5–33–46 t/MWe). Expected plate steel is therefore below its mode value, even though expected total steel emissions (rebar plus plate) rise.

### C5. Why the median (4.2) sits above the mode case (2.7)

**Result.** The gap is real information, not an error: the inputs we know least about have long upper tails, so they can mostly push the result up.

- A triangular distribution's mean is (low + mode + high) / 3. For conversion heat that is (26 + 26 + 665) / 3 = 239 kWh/kg U, nine times the mode of 26.
- Conversion therefore contributes +0.97 of the +1.58 g/kWh gap (Table C3). Mining (+0.23), the back end (+0.09), enrichment (+0.08), O&M (+0.06), decommissioning (+0.06) and the construction uplift (+0.06) add most of the rest.
- The LC3 saving is almost symmetric (mode 1,734 t, median 1,742 t), so its share of the total falls from 0.45% (mode case) to 0.29% (median).
- We therefore quote the median as the result and the mode case only as "every input at its most likely value". A measured conversion value would collapse most of the gap [TODO: source needed: Cameco Port Hope facility emissions divided by UF₆ output].

### C6. Limitations of the uncertainty analysis

1. **Independence.** Inputs are drawn independently. Concrete and steel intensities are probably positively correlated (bigger plants need more of both), which would widen the construction tail slightly; enrichment and burnup are also linked in practice. The effect on the total is small because construction is about 7.5%.
2. **Ranges partly judgement.** Ranges marked A or P in Table C1 are our assumptions; ×0.5 to ×2 transfer ranges on the EDF stages are not data.
3. **Triangular shape.** A convention, not a fitted distribution.
4. **Unverified inputs.** Every V in Table C1 is a search lead. The intervals will move when the primaries are opened.
5. **Model structure not varied.** The boundary (process-based stages plus three stages transferred as per-kWh values) and the cut-offs (§6.1) are not sampled; they bias the result low (§6.5, Table T9).

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.7 (uncertainty realistically estimated and discussed).** Produced: 40-input tornado with sources and status; 20,000-draw Monte Carlo with percentiles; stage-level skew analysis explaining median vs mode; LC3 vs slag overlap (64%; interval spans zero); stated limitations. Missing: verified ranges; a correlation case (stated as a limitation instead).
- **RB.5 (full calculations in an appendix).** Produced: set-up, every range, every result, reproduce command. Missing: nothing structural.

### Remaining TODOs

1. **[TO VERIFY, blocking]** Open the primaries for every V input in Table C1 (priority: Gibon and Hahn Menacho 2023 for conversion heat; Parker et al. 2016; EDF R&D 2024), then re-run `lca_uncertainty.py` and update Tables C1–C3.
2. **[TODO: Leroy]** Burnup, enrichment, net MWe, capacity factor and design life (the P rows) with sources.
3. **[TODO: source needed]** A measured conversion value (Cameco Port Hope facility emissions and UF₆ output).
4. **[TODO: optional, STRETCH]** A correlated-draw case (concrete with steel intensity; burnup with enrichment) to replace limitation 1.
