Rubric coverage: R2.7, RB.5, RB.6 (also supports R2.4)

## Appendix C. Sensitivity analysis

### C1 Set-up
- **Tornado:** each of 45 ranged inputs set to its low and high value, others at central. Ranges are in `parameters_lca.yaml`.
- **Monte Carlo:** 20,000 draws, seed 20261021, inputs independent and triangular (net output uniform 300–315 MWe). Twenty-nine inputs affect the main case.
- Reproduce: `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py`.

### C2 Ranged inputs and tornado results
Swing in life-cycle intensity (g CO₂e/kWh), ranked (Parker, McNaughton and Sparrow, 2016; Gibon and Hahn Menacho, 2023; EDF R&D, 2024):

| Input (low / central / high) | Swing |
|---|---:|
| Conversion heat (26 / 26 / 665 kWh/kg U) | 2.669 |
| Mining and milling (24 / 42 / 81 kg CO₂e/kg U₃O₈) | 1.390 |
| Back end (0.28 / 0.56 / 1.11 g/kWh) | 0.830 |
| Burnup (35 / 45 / 55 GWd/t) | 0.682 |
| Enrichment (3.4 / 3.8 / 4.95%) | 0.663 |

Plant steel moves the total by 0.105 and plant concrete by 0.057. C1's saving (2,200 t) moves with eligible share (1,100–3,300 t), LC³ cut (1,672–2,964 t), plant concrete (1,760–2,640 t) and OPC factor (1,911–2,432 t).

### C3 What the tornado shows
Fuel-cycle inputs dominate; construction inputs are minor. Expected stage means (Monte Carlo) total 4.487 g/kWh: mining 1.261, conversion 1.105, back end 0.651, O&M 0.390, enrichment 0.355, construction 0.515.

### C4 Monte Carlo results
| Output | Mode case | P5 | P50 | P95 |
|---|---:|---:|---:|---:|
| Life cycle (g/kWh) | 2.864 | 3.236 | 4.396 | 6.053 |
| C1 saving per unit (t) | 2,200 | 1,375 | 2,217 | 3,294 |
| C1 saving, Units 2–4 (t) | 6,600 | 4,124 | 6,651 | 9,881 |

LC³ beats slag in 55% of draws.

### C5 Why the median (4.40) sits above the mode case (2.86)
Skewed upper tails, mainly conversion heat: triangular mean (26 + 26 + 665) / 3 ≈ 239 kWh/kg U, nine times the mode, adds +0.98 of the +1.62 g/kWh gap. With conversion heat fixed at 26 the median is 3.51; log-uniform 26–665 gives 4.11. The reported range of medians is **3.51–4.40 g CO₂e/kWh**.

### C6 Limitations
Inputs are drawn independently; some ranges (±20%, eligible share, LC³ cut, EDF transfer ranges) are assumptions; triangular shapes are conventions; the Ostrołęka and Pillai tables were not opened; model boundary and cut-offs are not sampled.

### C7 Benchmarks
Our median 4.40 (3.24–6.05) g/kWh against UNECE (2021) 5.1–6.4, EDF R&D (2024) 3.7 (2.9–4.6), Gibon and Hahn Menacho (2023) 6.1, Warner and Heath (2012) median 12, and coal 751–1,095 g/kWh. Differences arise mainly from high-grade ore, centrifuge enrichment and fuel-inventory cut-offs.
