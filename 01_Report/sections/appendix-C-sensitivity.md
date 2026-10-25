Rubric coverage: R2.7, RB.5, RB.6 (also supports R2.4, R2.1, R5.2)

<!--
CHANGELOG
- v5, 25/10/2026 (writer, final day; Victor owns Sam's red sections, Sam may review): re-based on `lca_uncertainty.md`, `lca_tornado.csv` and `lca_rebase_deck.md` (45 ranged inputs, 29 affecting the main case; median 4.40; conversion-heat medians 3.51–4.40; C1 at 20/40/60% eligibility). New C7 holds the benchmark tables moved from §6.5 (Tables C7a, C7b). Tables renumbered to follow section numbers (C2, C3, C4a, C4b, C5, C7a, C7b). All markers hedged or cut.
-->

## Appendix C. Sensitivity: tornado and Monte Carlo set-up and results

This appendix shows how uncertain the §6 results are and which inputs drive them. **The life-cycle intensity is uncertain mainly through the fuel inputs (conversion heat, mining, back end, burnup, enrichment); C1's saving is uncertain mainly through the eligible share, the LC³ cut and the plant concrete volume.** All ranges come from `parameters_lca.yaml`. The Ostrołęka and Pillai tables could not be opened and other inputs are as reported by secondary sources, assumptions or placeholders, so the intervals describe the uncertainty in our inputs as found, not in verified data.

### C1. Set-up

- **Tornado (one at a time).** Each of the 45 ranged inputs is set to its low and then its high value, with every other input at its central value. Outputs: life-cycle g CO₂e/kWh and C1's saving (t CO₂e per unit, at 40% eligibility).
- **Monte Carlo.** N = 20,000 draws; seed 20261021; generator `numpy.random.default_rng`. All 45 inputs are drawn **independently**: triangular (low, central, high) except net output, uniform 300–315 MWe. Twenty-nine inputs affect the main case; the other 16 are bottom-up only and drive the cross-check on the same draws. Fixed (not drawn): thermal power, feed assay, U₃O₈ stoichiometry, the gas heat factor, forebay rebar, basemat steel and module diameter.
- **C1 in the draws.** Eligibility is drawn (triangular 0.2/0.4/0.6) in the headline saving; the 20/40/60% scenarios hold it fixed while everything else varies. Each draw's saving is divided by the same draw's life-cycle total.
- **Cross-check rule.** If a bottom-up draw's whole-plant concrete falls below the cross-check C1 volume, the plant volume is set equal to it: 696 of 20,000 draws (3.5%). The main case never clips.
- **Outputs.** 5th, 50th and 95th percentiles and the mean. Stage means are additive, so they sum to the expected total.
- **Reproduce:** `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py`.

### C2. Ranged inputs and tornado results

**Result.** Five fuel-cycle inputs each move the life-cycle total by more than 0.6 g/kWh. No concrete input moves it by more than 0.06 g/kWh; plant steel moves it by 0.11 and the construction uplift by 0.34.

*Table C2. The 29 ranged inputs that affect the main case, their basis and tornado results (ranked by swing in life-cycle intensity; the other 16 are listed below).*
*Source: `parameters_lca.yaml`; `results/lca_tornado.csv`. P = placeholder, A = assumption; other rows are as reported by the source named. Distribution triangular unless stated. "—" = no effect on C1's saving (2,200 t at 40% eligibility). Low, central and high are model input bounds, not result intervals.*

| # | Input (unit) | Low / central / high | Basis | Life-cycle g/kWh at low → high (swing) | C1 saving t at low → high |
|---:|---|---|---|---|---|
| 1 | Conversion heat (kWh/kg U) | 26 / 26 / 665 | Gibon and Hahn Menacho (2023) | 2.864 → 5.533 (2.669) | — |
| 2 | Mining and milling (kg CO₂e/kg U₃O₈) | 24 / 42 / 81 | Parker, McNaughton and Sparrow (2016) | 2.425 → 3.815 (1.390) | — |
| 3 | Back end (g/kWh) | 0.28 / 0.56 / 1.11 | EDF R&D (2024); range A | 2.584 → 3.414 (0.830) | — |
| 4 | Burnup (GWd/t) | 35 / 45 / 55 | P | 3.281 → 2.599 (0.682) | — |
| 5 | Enrichment (% U-235) | 3.4 / 3.8 / 4.95 | Sun and Kurosaki (2025); low A; P | 2.694 → 3.357 (0.663) | — |
| 6 | O&M (g/kWh) | 0.17 / 0.33 / 0.67 | EDF R&D (2024); range A | 2.704 → 3.204 (0.500) | — |
| 7 | Enrichment-plant grid (kg CO₂e/kWh) | 0.05 / 0.373 / 0.637 | US EPA (2024), CO₂ only; low A | 2.629 → 3.056 (0.427) | — |
| 8 | Other construction uplift (fraction) | 0.25 / 0.5 / 1.5 | A | 2.797 → 3.135 (0.338) | — |
| 9 | Centrifuge energy (kWh/SWU) | 40 / 50 / 100 | Gibon and Hahn Menacho (2023) | 2.810 → 3.136 (0.326) | — |
| 10 | Design life (years) | 40 / 60 / 80 | Canadian Nuclear Safety Commission (2024); bounds A | 3.067 → 2.763 (0.304) | — |
| 11 | Decommissioning (g/kWh) | 0.06 / 0.11 / 0.33 | EDF R&D (2024); range A | 2.814 → 3.084 (0.270) | — |
| 12 | Tails assay (% U-235) | 0.20 / 0.25 / 0.30 | A | 2.800 → 2.960 (0.160) | — |
| 13 | Plant steel per unit (t) | 11,200 / 14,000 / 16,800 | BWRX-300 Ostrołęka sp. z o.o. (2023), as reported; ±20% A | 2.812 → 2.917 (0.105) | — |
| 14 | Net output (MWe), uniform | 300 / 300 / 315 | GE Vernova Hitachi Nuclear Energy (n.d.); Ontario Power Generation (2025b); P | 2.864 → 2.775 (0.089) | — |
| 15 | Plate and equipment steel (t CO₂e/t) | 1.22 / 1.73 / 2.50 | American Institute of Steel Construction (2022); high A | 2.829 → 2.917 (0.088) | — |
| 16 | Rebar factor (t CO₂e/t) | 0.89 / 0.97 / 1.99 | Concrete Reinforcing Steel Institute (2017); American Institute of Steel Construction (2022); Circular Ecology (2019) | 2.858 → 2.945 (0.087) | — |
| 17 | Conversion-plant grid, Ontario (kg CO₂e/kWh) | 0.035 / 0.0738 / 0.343 | The Atmospheric Fund (2025); Canada Energy Regulator (n.d.) | 2.855 → 2.930 (0.075) | — |
| 18 | Capacity factor | 0.80 / 0.90 / 0.95 | P | 2.915 → 2.843 (0.072) | — |
| 19 | Rebar ratio (t/m³) | 0.10 / 0.15 / 0.25 | A (high = forebay) | 2.884 → 2.824 (0.060) | — |
| 20 | Plant concrete per unit (m³) | 40,000 / 50,000 / 60,000 | BWRX-300 Ostrołęka sp. z o.o. (2023), as reported; ±20% A | 2.836 → 2.893 (0.057) | 1,760 → 2,640 |
| 21 | OPC concrete factor (kg CO₂e/m³) | 330 / 380 / 420 | Pillai et al. (2019), as reported; range from Canadian Ready-Mixed Concrete Association (2022) | 2.838 → 2.885 (0.048) | 1,911 → 2,432 |
| 22 | Fabrication-plant grid (kg CO₂e/kWh) | 0.20 / 0.373 / 0.637 | US EPA (2024), CO₂ only; low A | 2.848 → 2.890 (0.042) | — |
| 23 | Steel haul distance (km) | 100 / 500 / 1,500 | A | 2.858 → 2.879 (0.021) | — |
| 24 | Fabrication energy (kWh/kg U) | 36 / 36 / 50 | Gibon and Hahn Menacho (2023) | 2.864 → 2.878 (0.014) | — |
| 25 | Conversion electricity (kWh/kg U) | 10.3 / 11.8 / 16.9 | Gibon and Hahn Menacho (2023) | 2.862 → 2.872 (0.010) | — |
| 26 | Truck factor (kg CO₂e/t-km) | 0.06 / 0.10 / 0.15 | A | 2.861 → 2.869 (0.008) | — |
| 27 | Concrete haul distance (km) | 5 / 15 / 50 | A | 2.863 → 2.869 (0.006) | — |
| 28 | LC³ cut in concrete emissions | 0.22 / 0.289 / 0.39 | Pillai et al. (2019), as reported; range A | no change | 1,672 → 2,964 |
| 29 | Eligible share of plant concrete | 0.2 / 0.4 / 0.6 | A: non-safety works first | no change | 1,100 → 3,300 |

The other 16 inputs affect only the bottom-up cross-check: concrete intensity (34.5 / 69 / 138 m³/MWe) and steel intensity (16.5 / 33 / 46 t/MWe; Peterson, Zhao and Petroski, 2005; GE Vernova, n.d.); forebay concrete (4,000 / 4,000 / 6,000 m³; Ontario Power Generation, 2025c); shaft depth, basemat and wall thicknesses; binder contents (infill 400 / 450 / 550 kg/m³, EFNARC, 2005; other 300 / 350 / 420); GU cement (796 / 854 / 898 kg CO₂e/t; Cement Association of Canada, 2022); slag cement (93.4 / 146.6 / 146.6; Slag Cement Association, n.d.); non-binder share (15 / 30 / 60 kg CO₂e/m³); GU and LC³ clinker factors; slag share of binder (0.25 / 0.40 / 0.50); the binder-level LC³ cut (0.30 / 0.37 / 0.43; five estimates, Appendix A5); and extra binder LC³ needs to flow (0 / 0 / 0.10). All are assumptions or as-reported values.

### C3. What the tornado shows, and where the emissions arise

**Life-cycle intensity (Figure F3, left).** The ranking is dominated by the fuel chain. Conversion heat alone could double the result, because the published heat demand spans a factor of 25 (26–665 kWh/kg U). The mining factor ranks second because ore grade varies widely between Saskatchewan mines. Higher burnup *lowers* the result (less uranium per MWh) and higher enrichment raises it (more separative work). Of the construction inputs, only the uplift (0.34) and plant steel (0.11) exceed 0.1 g/kWh.

**C1's saving (Figure F3, right).** Four inputs move it: the eligible share (swing 2,200 t), the LC³ cut (1,292 t), plant concrete volume (880 t) and the OPC factor (521 t). No other input moves it. The first is our scenario; the second and fourth come from Pillai et al. (2019), and the third from the Ostrołęka sheet. Even at its lowest single-input value (1,100 t at 20% eligibility), C1 saves more than any other input's swing excluding eligibility.

*Table C3. Expected life-cycle emissions by stage (Monte Carlo mean) against the mode case.*
*Source: `results/lca_uncertainty.md`; last column is our subtraction (mean − mode).*

| Stage | Mode case g/kWh | Mean g/kWh | P5 | P95 | Share of mean | Mean − mode |
|---|---:|---:|---:|---:|---:|---:|
| Fuel: mining and milling | 1.024 | 1.261 | 0.760 | 1.915 | 28.1% | +0.237 |
| Fuel: conversion | 0.127 | 1.105 | 0.228 | 2.392 | 24.6% | +0.978 |
| Back end: spent fuel and disposal | 0.560 | 0.651 | 0.387 | 0.961 | 14.5% | +0.091 |
| Operation and maintenance | 0.330 | 0.390 | 0.233 | 0.577 | 8.7% | +0.060 |
| Fuel: enrichment | 0.272 | 0.355 | 0.133 | 0.634 | 7.9% | +0.083 |
| Construction: other materials and site energy | 0.135 | 0.221 | 0.103 | 0.386 | 4.9% | +0.086 |
| Decommissioning | 0.110 | 0.167 | 0.087 | 0.277 | 3.7% | +0.057 |
| Construction: concrete | 0.134 | 0.135 | 0.101 | 0.178 | 3.0% | +0.001 |
| Construction: rebar | 0.051 | 0.077 | 0.043 | 0.123 | 1.7% | +0.025 |
| Construction: plate, structural and equipment steel | 0.079 | 0.074 | 0.027 | 0.127 | 1.6% | −0.006 |
| Fuel: fabrication | 0.036 | 0.043 | 0.027 | 0.064 | 1.0% | +0.007 |
| Construction: transport to site | 0.006 | 0.009 | 0.004 | 0.017 | 0.2% | +0.003 |
| **Total** | **2.864** | **4.487** | | | **100%** | **+1.623** |

Grouped (expected basis): fuel front end 61.6%, back end and decommissioning 18.2%, O&M 8.7%, construction 11.5% (0.515 / 4.487). Mode-case shares are 50.9, 23.4, 11.5 and 14.2%. Construction's share has a Monte Carlo median of 11.5% (P5–P95 7.2–17.8%). All concrete is 3.0–4.7% of the total.

### C4. Monte Carlo results

**Result.** Life-cycle intensity: **median 4.40, 90% interval 3.24–6.05 g CO₂e/kWh**. C1's saving at central eligibility: **median 2,217 t per unit (1,375–3,294)** and **6,651 t for Units 2–4 (4,124–9,881)**. LC³ saves more than slag in **55%** of draws.

*Table C4a. Monte Carlo outputs (20,000 draws, seed 20261021).*
*Source: `results/lca_uncertainty.md`, `lca_montecarlo_summary.csv`.*

| Output | Mode case | Mean | P5 | P50 | P95 |
|---|---:|---:|---:|---:|---:|
| Life-cycle intensity (g CO₂e/kWh) | 2.864 | 4.487 | 3.236 | 4.396 | 6.053 |
| Fuel front end (g/kWh) | 1.458 | 2.764 | 1.586 | 2.661 | 4.280 |
| of which mining and milling (g/kWh) | 1.024 | 1.261 | 0.760 | 1.217 | 1.915 |
| Construction (g/kWh) | 0.406 | 0.515 | 0.347 | 0.500 | 0.736 |
| Construction share of life cycle (%) | 14.17 | 11.83 | 7.19 | 11.45 | 17.78 |
| Plant concrete (m³ per unit) | 50,000 | 50,008 | 43,224 | 50,009 | 56,772 |
| C1-eligible concrete (m³ per unit) | 20,000 | 20,007 | 12,886 | 19,879 | 27,540 |
| C1 saving, LC³ (t CO₂e per unit) | 2,200 | 2,259 | 1,375 | 2,217 | 3,294 |
| C1 saving, Units 2–4 (t CO₂e) | 6,600 | 6,776 | 4,124 | 6,651 | 9,881 |
| C1 saving as share of the unit's life cycle (%) | 0.541 | 0.373 | 0.195 | 0.355 | 0.614 |
| Slag blend saving (t CO₂e per unit) | 2,288 | 2,193 | 1,310 | 2,140 | 3,238 |
| LC³ minus slag (t CO₂e per unit) | −88 | 66 | −588 | 54 | 766 |
| Cross-check life-cycle intensity (g/kWh) | 2.701 | 4.293 | 3.050 | 4.199 | 5.863 |

At fixed eligibility the share of the life cycle is 0.18% (P5–P95 0.11–0.28%) at 20%, 0.36% (0.23–0.56%) at 40% and 0.54% (0.34–0.84%) at 60%. The LC³-minus-slag interval spans zero: the two binders cannot be separated on carbon with present data, and if OPG's baseline already contains slag the same row is LC³'s increment over business as usual. Plant concrete is a ±20% triangular input, so its 90% interval (43,224–56,772 m³) is narrower than its bounds.

*Table C4b. Scenario savings and life-cycle shares on the Monte Carlo basis (the basis of Table T8 in §6.3 and Table A7b).*
*Source: `results/lca_uncertainty.md`. Each draw's saving is divided by the same draw's S0 life-cycle total. S3 rows are steel sensitivities, not part of C1; S3 world-average is negative (adds emissions).*

| Scenario | Saving, t per unit: median (5th–95th) | Share of life cycle, %: median (5th–95th) | Mode-case share, % |
|---|---|---|---:|
| C1: LC³ on 40% (eligibility drawn) | 2,217 (1,375–3,294) | 0.355 (0.195–0.614) | 0.541 |
| S1 slag blend on the same 40% (fallback) | 2,140 (1,310–3,238) | 0.343 (0.185–0.602) | 0.563 |
| Cross-check: LC³ in infill and forebay | 1,750 (1,389–2,152) | 0.293 (0.187–0.458) | 0.452 |
| S2b LC³ on 40% plus slag elsewhere | 5,517 (4,346–6,841) | 0.886 (0.566–1.357) | 1.386 |
| S3 like-for-like (target-structure steel) | 940 (415–1,580) | 0.149 (0.062–0.283) | 0.139 |
| S3 upper bound (all steel, sections factors) | 6,428 (2,521–11,486) | 1.025 (0.382–2.041) | 0.963 |
| S3 world-average steel | −9,914 (−14,037 to −4,904) | −1.559 (−2.700 to −0.717) | −3.114 |

### C5. Why the median (4.40) sits above the mode case (2.86)

**Result.** The gap is real information, not an error: the inputs we know least about have long upper tails, so they can mostly push the result up.

- A triangular distribution's mean is (low + mode + high) / 3. For conversion heat that is (26 + 26 + 665) / 3 ≈ 239 kWh/kg U, nine times the mode of 26.
- Conversion therefore contributes +0.98 of the +1.62 g/kWh gap (Table C3). Mining (+0.24), the back end (+0.09), enrichment (+0.08), the construction uplift (+0.09), O&M (+0.06) and decommissioning (+0.06) add most of the rest.
- C1's saving is almost symmetric (mode 2,200 t, median 2,217 t), so its share of the total falls from 0.54% at the mode case to 0.36%.
- We quote the median as the result and the mode case only as "every input at its most likely value". A measured conversion value would collapse most of the gap.
- Because one distribution choice carries most of the gap, Table C5 re-runs the Monte Carlo with conversion heat fixed at 26 kWh/kg U and with a log-uniform 26–665 distribution; the other 44 inputs use the same draws. The median does not stay near 4.4: it is 3.51 and 4.11, so §6 reports the **range of medians, 3.51–4.40 g CO₂e/kWh**. Conversion heat accounts for about 0.9 g/kWh of the median (4.40 − 3.51) and decides how skewed the result is.

*Table C5. Conversion-heat distribution test (life-cycle g CO₂e/kWh).*
*Source: `results/lca_uncertainty.md`. C1's share is the headline saving with eligibility drawn.*

| Conversion-heat distribution | Mean heat (kWh/kg U) | Mean | P5 | P50 | P95 | C1 share, % median (P5–P95) |
|---|---:|---:|---:|---:|---:|---|
| Triangular 26 / 26 / 665 (headline) | 241 | 4.487 | 3.236 | 4.396 | 6.053 | 0.355 (0.195–0.614) |
| Fixed at 26 (Gibon and Hahn Menacho, 2023) | 26 | 3.540 | 2.797 | 3.506 | 4.391 | 0.446 (0.258–0.734) |
| Log-uniform 26–665 | 197 | 4.294 | 3.063 | 4.113 | 6.116 | 0.373 (0.200–0.650) |

### C6. Limitations of the uncertainty analysis

1. **Independence.** Inputs are drawn independently. Concrete and steel quantities are probably positively correlated, and enrichment and burnup are linked in practice; the effect on the total is small because construction is about 11.5%.
2. **Ranges partly judgement.** The ±20% on the Ostrołęka quantities, the eligible share, the LC³ cut range and the ×0.5 to ×2 transfer ranges on the EDF stages are assumptions, not data.
3. **Triangular shape.** A convention, not a fitted distribution; Table C5 tests it for conversion heat only.
4. **Inputs as found.** The Ostrołęka and Pillai tables were not opened. The intervals will move when they are.
5. **Model structure not varied.** The boundary (process-based stages plus three stages transferred as per-kWh values) and the cut-offs (§6.1) are not sampled; they bias the result low (C7).

### C7. Why our result differs from the benchmarks

**Result.** Our median is below UNECE's range but our 90% interval overlaps it; the main reasons are ore grade, enrichment technology and cut-offs.

*Table C7a. Published life-cycle values against ours (g CO₂e/kWh).*
*Source: this study; references as listed. Benchmark values are as reported in the sources named and were not independently checked.*

| Source | Value | Ours against it |
|---|---|---|
| **This study** | 4.40 median (3.24–6.05); range of medians 3.51–4.40 | |
| United Nations Economic Commission for Europe (2021), nuclear | 5.1–6.4 | Median below the range; our 90% interval overlaps it |
| IPCC AR5 Annex III (Schlömer et al., 2014) | 3.7 / 12 / 110 (minimum / median / maximum, as commonly quoted) | Near the minimum, well below the median |
| Warner and Heath (2012), harmonised light-water reactors | median 12 | About a third of it |
| EDF R&D (2024), French fleet | 3.7 (2.9–4.6) | Overlaps |
| Gibon and Hahn Menacho (2023), global 2020 | 6.1 | Below |
| Carless, Griffin and Fischbeck (2016), Westinghouse SMR | 9.1 (5.9–13.2) | Below |
| Coal; gas combined cycle (United Nations Economic Commission for Europe, 2021) | 751–1,095; 403–513 | 170–250 and 90–120 times higher than ours |

*Table C7b. Why our result differs from the benchmarks: direction and size of each reason.*
*Source: this study (Appendices A and C), with the references as listed.*

| Reason | Effect on our value | Size |
|---|---|---|
| High-grade Canadian ore | Lower | Our mining is 1.0–1.3 g/kWh; at global-average grades Gibon and Hahn Menacho (2023) attribute 46% of 6.1, about 2.8 g/kWh, to it. This explains most of the gap to UNECE and Gibon |
| Centrifuge enrichment only | Lower than older studies | 50 kWh/SWU against about 2,500 for the diffusion plants in older study sets (Gibon and Hahn Menacho, 2023; Warner and Heath, 2012) |
| Energy-only fuel inventory (cut-offs) | Lower | Not quantified (chemicals, cladding, upstream gas, fuel-plant capital goods excluded) |
| Construction | Now close to large reactors | 0.41 g/kWh at the mode case, 0.50 median (0.35–0.74), against about 0.59 for large reactors (16% of 3.7; EDF R&D, 2024). The SMR scale penalty shows: 167 m³ of concrete per MWe against 69 for the ESBWR and 138 for the ABWR (Peterson, Zhao and Petroski, 2005) |
| Long life and high capacity factor | Lower | At 40 years instead of 60, the mode case rises from 2.86 to 3.07 g/kWh |
| O&M and back end transferred from France (reprocessing) | Possibly higher | Canada plans direct disposal; back-end range 0.28–1.11 g/kWh tested |
| SMR rather than large reactor | Small | Carless, Griffin and Fischbeck (2016) give 9.1 for an SMR against 8.4 for the AP1000, mainly through the fuel cycle; our construction share is too small for scale effects to move the total much |

The sources disagree mainly about the fuel front end (ore grade, enrichment technology and grid), not construction, and that is where our result departs from them. The known low bias would raise the total and make C1's share smaller still, so it does not weaken §6.3.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.7 (uncertainty realistically estimated and discussed).** Produced: 45-input tornado with basis; 20,000-draw Monte Carlo with percentiles; stage-level skew analysis; conversion-heat distribution test (range of medians 3.51–4.40); LC³-versus-slag overlap (55%); Monte Carlo shares for every scenario; stated limitations. Missing: opened primaries for the ranges; a correlated-draw case (stated as a limitation).
- **RB.6.** Produced: benchmark table and seven sized reasons (C7). Missing: independently checked benchmark values.
- **RB.5.** Produced: set-up, every range, every result, reproduce command. Missing: nothing structural.

### Remaining TODOs

None in the body. For a person: open Ostrołęka Table 14 and Pillai Table 2, then re-run `lca_uncertainty.py` and re-copy any value that moves.
