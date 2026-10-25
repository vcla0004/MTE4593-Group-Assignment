Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3 (also supports R3.1, R4.1, R4.2, R4.3, R4.4, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- v5, 25/10/2026 (writer, final day; Victor owns Sam's red sections, Sam may review). Rewritten on the re-based LCA (`lca_rebase_deck.md`, `c1_deck_case.md`): Ostrołęka 50,000 m³ / 14,000 t main case, Pillai 380 vs 270 kg CO₂e/m³, C1 at 20/40/60% = 1,100/2,200/3,300 t; the 20,700 m³ model is a cross-check. Median 4.40 (3.24–6.05), range of medians 3.51–4.40, construction 11.5%, share 0.36%, break-even 11.6–18.5 and 1.7–1.8 days. T6 to App A2 (Table A2b), T9 to App C7, T8 cut to four rows (S2b and steel rows in App A7, Table A7b). Granta stated as not run; markers hedged or cut; no C$ values; IPCC AR5 added. Serves R2.1–R2.7, RB.5, RB.6, R1.3, R5.3, R5.5.
-->

## 6 Life-cycle assessment and eco-audit

One BWRX-300 at Darlington emits an estimated **4.4 g CO₂e per kWh (Monte Carlo median; 90% interval 3.2–6.1; 3.5 if conversion heat takes its central published value)**, below UNECE's 5.1–6.4 g/kWh for nuclear power. The fuel front end contributes 62% and construction 11.5%. The initiative, C1 (§4.3), puts limestone calcined clay cement (LC³) in 20–60% of the concrete. It saves **2,200 t CO₂e per unit (1,100–3,300 t), about 0.36% of the life cycle**: real but small, so worth adopting only if schedule-neutral (§6.3).

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of one BWRX-300 at Darlington (Clarington, Ontario), find the hotspots, and size C1's saving. This is a screening LCA following ISO 14040/14044 principles (International Organization for Standardization, 2006a; 2006b), not critically reviewed.

- **Functional unit:** 1 MWh of net electricity at the grid connection (g CO₂e/kWh equals kg CO₂e/MWh); transmission is outside. One unit delivers 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh** (Appendix A2).
- **Boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are modelled from published factors; operation and maintenance (O&M), decommissioning and the back end are per-kWh values from EDF's French-fleet study (EDF R&D, 2024).
- **Baseline (S0):** the concrete OPG would pour anyway, at 380 kg CO₂e/m³ (Pillai et al., 2019, as reported; Indian M50 mixes). We have not seen OPG's mix or any cement-type limit in the specification (GE-Hitachi Nuclear Energy, 2024).
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, upstream gas, fuel-plant capital goods and recycling credits; each biases the result low (§6.5). Impact category: climate change, GWP100.

**Method and inventory.** A reproducible Python model multiplies quantities by published emission factors (Appendices A and C). Plant quantities come from the Ostrołęka project information sheet (BWRX-300 Ostrołęka sp. z o.o., 2023, as reported in the project information sheet): **50,000 m³ of concrete and 14,000 t of steel per unit**. This is a design proxy, not confirmed Darlington quantities, and we could not open either the Ostrołęka or the Pillai table. A bottom-up scaling from other reactors (20,700 m³; Peterson, Zhao and Petroski, 2005) is a cross-check (Appendix A3). Key inputs: Table A2b; all 45 ranged inputs: Appendix C2. **A Granta EduPack Eco Audit was planned but not completed; no number here comes from Granta.**

[Figure F1. LCA system boundary for one BWRX-300 at Darlington: fuel front end, construction materials and C1-eligible concrete modelled here; operation, decommissioning and back end from the literature. | Source: this study.]

### 6.2 Baseline and hotspots

**One unit emits 4.40 g/kWh (median; 90% interval 3.24–6.05).** With every input at its most likely value (the "mode case") it is 2.86; §6.4 explains the gap. On the expected basis (Figure F2):

1. **Mining and milling: 1.26 g/kWh (28%),** low because Saskatchewan ores are high-grade (Parker, McNaughton and Sparrow, 2016).
2. **Conversion: 1.10 g/kWh (25%),** an *uncertainty* hotspot: published heat demand spans 26–665 kWh per kg of uranium (Gibon and Hahn Menacho, 2023); at the most likely value conversion is only 0.13 g/kWh.
3. **Back end: 0.65 g/kWh (15%),** transferred from France, which reprocesses; Canada plans direct disposal (Nuclear Waste Management Organization, 2024a), so this may be high.

The back end and decommissioning add 18%, O&M 9% and **construction 11.5%** (0.52 g/kWh; 7.2–17.8% across draws). The C1-eligible concrete is only 1.9% of the mode-case total, so **C1 acts on about one-fiftieth of the footprint**.

The vendor claims about 50% less concrete per unit of energy than the ESBWR (GE Vernova, n.d.), while small plants usually lose economies of scale; Ostrołęka's 167 m³ per MWe, 2.4 times the ESBWR's 69 (Peterson, Zhao and Petroski, 2005), sides with scale. The cross-check gives 4.20 g/kWh, so the re-base adds about 0.2 g/kWh, all in construction. Per MWh the plant uses 0.85 kg of concrete, 0.099 kg of steel, 20.7 g of natural uranium and 0.0146 separative work units (Appendix A8).

[Figure F2. Life-cycle emissions of one BWRX-300 by stage: expected value 4.49 g CO₂e/kWh (Monte Carlo mean), with the mode case (every input at its most likely value, total 2.86) marked. | Source: this study, Appendix C3.]

### 6.3 The initiative against the baseline

**C1 is low-clinker concrete: LC³ on eligible non-safety works first and on the steel-composite infill only if qualified, a slag blend as the fallback, specified only if schedule-neutral (§4.3).** Pillai et al. (2019, as reported) give 380 kg CO₂e/m³ for ordinary concrete and 270 for LC³, a cut of 110 kg/m³ (28.9%). The eligible share is our scenario, not data, and drives the result. At 20, 40 and 60% of 50,000 m³, C1 saves **1,100, 2,200 and 3,300 t per unit, or 0.18, 0.36 and 0.54% of its life cycle** (Table T8). Letting eligibility, the cut and the volumes vary together gives 2,217 t (1,375–3,294) per unit. Only Units 2–4 count, because Unit 1's basemat is placed.

*Table T8. C1 saving against the baseline, per unit and for Units 2–4; share of life cycle is the Monte Carlo median (5th–95th percentile). Source: this study, Appendices A6–A7 and C4.*

| Scenario | Per unit, t CO₂e | Units 2–4, t | Clinker avoided per unit, t | Share of life cycle |
|---|---|---|---|---|
| LC³ on 20% of plant concrete | 1,100 | 3,300 | 1,470 | 0.18% (0.11–0.28) |
| **LC³ on 40% (central)** | **2,200** | **6,600** | **2,940** | **0.36% (0.23–0.56)** |
| LC³ on 60% | 3,300 | 9,900 | 4,410 | 0.54% (0.34–0.84) |
| Slag blend on the same 40% (fallback) | 2,288 | 6,865 | 2,576 | 0.34% (0.18–0.60) |

Four findings follow, each with a consequence for the initiative.
1. **The saving is small at plant scale.** It is about 0.016 g/kWh, so C1 does not change the plant's climate case. It still exceeds the swing from the LC³ cut (1,672–2,964 t), the largest input other than eligibility. Its economic value is in §8.2.
2. **Slag is about as good as LC³, so the carbon case is for low-clinker concrete, not LC³ in particular.** LC³ beats slag in only 55% of draws (median difference +54 t; 90% interval −588 to +766). If OPG's baseline already contains slag, LC³'s gain is about −90 t, within noise. The specification should accept whichever binder qualifies first (§8.1).3. **Lower-carbon steel is the larger lever but is not part of C1.** Steel in the structures C1 targets saves only 566 t per unit (Appendix A7). All 14,000 t at best-practice electric-arc-furnace factors would save up to 3,915 t (1.8 times LC³), but this is an upper bound, not shown feasible for forgings and nuclear-grade plate. It is the next lever (§10).
4. **Schedule dominates.** A delay of **11.6–18.5 days** to one unit on Ontario's average grid factor, or **1.7–1.8 days** on the marginal factor, cancels its saving (§7.1; Appendix B5). C1 is therefore specified only if schedule-neutral (§8.6).

For the triple-bottom-line evaluation (§9), C1 is environmentally positive but marginal; feasibility hinges on qualification and schedule.

### 6.4 Uncertainty: tornado and Monte Carlo

The tornado varies 45 inputs one at a time; the Monte Carlo varies them together, 20,000 times (Appendix C).

**The total depends on the fuel inputs, not the concrete (Figure F3).** The largest swings are conversion heat (2.86 → 5.53 g/kWh), the mining factor (2.43 → 3.82) and the back end (2.58 → 3.41). No concrete input moves the total by more than 0.06 g/kWh. **The saving depends on four inputs:** eligible share (1,100 → 3,300 t), LC³ cut (1,672 → 2,964 t), plant concrete volume (1,760 → 2,640 t) and the OPC factor (1,911 → 2,432 t).

[Figure F3. One-at-a-time sensitivity of life-cycle intensity (left, centred on the 2.86 g CO₂e/kWh mode case) and of C1's saving per unit (right, centred on 2,200 t), top ten inputs each. | Source: this study, Appendix C2.]

**Monte Carlo (Figure F4): why we report 4.4, not 2.9.** Several inputs can mostly only rise: conversion heat is most likely 26 kWh/kg U but could be 665, which alone adds about 1.0 g/kWh to the mean (Appendix C5). We therefore quote the median. **The headline depends on how conversion heat is distributed:** fixed at Gibon and Hahn Menacho's (2023) central 26 kWh/kg U, the median is 3.51 g/kWh (2.80–4.39); log-uniform over 26–665, 4.11 (3.06–6.12). We quote the **range of medians, 3.51–4.40**. A measured conversion value would settle it. Draws are independent and many ranges are judgement (Appendix C6).

[Figure F4. Monte Carlo distributions (20,000 draws) of life-cycle intensity (median 4.40, 5th–95th percentile 3.24–6.05 g CO₂e/kWh) and of C1's saving per unit at central eligibility. | Source: this study, Appendix C4.]

### 6.5 Comparison with published values

**Our median (3.5–4.4 across conversion-heat assumptions) is below UNECE's 5.1–6.4 g/kWh (United Nations Economic Commission for Europe, 2021), though our 90% interval overlaps it, and sits at the low end of the wider literature for reasons we can identify (Figure F5).** It overlaps EDF's French fleet (3.7; EDF R&D, 2024) and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016), the harmonised light-water-reactor median of 12 (Warner and Heath, 2012) and the IPCC AR5 median of 12, as commonly quoted from a 3.7–110 range (Schlömer et al., 2014). Gas combined cycle (403–513 g/kWh) and coal (751–1,095) are 90–120 and 170–250 times higher (United Nations Economic Commission for Europe, 2021).

**Three reasons explain most of the gap** (sizes in Appendix C7):
1. **Ore grade:** our mining is 1.0–1.3 g/kWh, against about 2.8 at global-average grades (Gibon and Hahn Menacho, 2023).
2. **Enrichment:** centrifuges at 50 kWh per separative work unit, against about 2,500 for the diffusion plants in older study sets.
3. **Cut-offs and long life:** excluded inputs and a 60-year life bias the result low; at 40 years the mode case rises from 2.86 to 3.07 g/kWh.

Construction is now 0.41 g/kWh at the mode case (median 0.50), close to EDF's roughly 0.59 for large reactors (16% of 3.7). The known low bias would raise the total and shrink C1's share, so it does not weaken §6.3.

[Figure F5. Our result against published nuclear life-cycle values (dot = central or median; line = range or interval). UNECE is a range only. Coal (about 750–1,100) and gas (403–513) are off the scale. | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012).]

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1, R2.3.** Produced: median with 90% interval, stage hotspots, C1 saving per unit and Units 2–4, clinker, resource use per MWh, steel lever. Missing: Ostrołęka and Pillai tables opened by a person.
- **R2.2.** Produced: an equivalent screening model, honestly labelled. Missing: Granta EduPack Eco Audit (not run).
- **R2.4, RB.5, R2.5.** Produced: method, functional unit, boundary, S0, cut-offs, design-proxy caveat; working in Appendices A and C. Missing: nothing structural.
- **R2.6, R2.7, RB.6, R1.3.** Produced: slag-versus-LC³ test, tornado, Monte Carlo, conversion-heat test, benchmark comparison with three sized reasons, vendor-versus-scale synthesis. Missing: verified benchmarks.

### Remaining TODOs

None in the body. For a person: open Ostrołęka Table 14 and Pillai Table 2; run Granta (needs Sam's machine); confirm the IPCC AR5 Annex III values.
