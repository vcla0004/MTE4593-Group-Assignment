Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3 (also supports R3.1, R4.1, R4.2, R4.3, R4.4, RB.1, RB.8, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- v4, 21/10/2026 (writer, Q8). Q1/Q2 outputs dropped in: like-for-like steel row (566 t, MC 941) and Monte Carlo shares for every scenario in T8; conversion-heat test in the lead and §6.4 (medians 3.3–4.2); carbon value and cost of delay in finding 2; break-even 9.2–14.6 days (average) and 1.3–1.4 (marginal) in lead and finding 5; F3/F5 captions updated (redrawn).
  - Granta (A9/A10) left as a marked TODO (H2, due Thu 12:00; cut if not run). Remaining TODOs renumbered. Rubric items: R2.2, R2.3, R2.6, R2.7, RB.6, R5.2.
- v3, 21/10/2026 (writer, for Victor). Revised against review.md "Review of §6 and Appendices A, C (21/10)". Victor's decision applied: keep C1, sharpened as low-clinker infill (LC3 target, slag fallback), schedule-neutral; steel is not added to the initiative. Items addressed:
  - Thesis: §6.3 opens with the sharpened C1 statement; T8 labels S1 "C1 fallback" and S2 "C1 target binder"; finding 4 ends "next lever (§10), not part of C1".
  - Review point 1 (lead): one unit throughout (g CO₂e/kWh; equivalence stated once in §6.1); lead now ends on the finding (1.4–15 days of delay cancel the saving) [R5.1, R4.3].
  - Point 2 (§6.1): S0 defined as what OPG would pour anyway, with the OPG-mix/NEDO-33926 cement-type question [TO VERIFY] and the consequence if S0 already has slag [R2.5, R2.6]; grid transmission moved from the cut-offs to the FU bullet; ISO 14040/44 and EN 15804 named with source TODOs (not yet in sources.md, so not cited as Harvard).
  - Point 3 (§6.2): the 63% target share flagged as a limitation (geometric vs scaled estimate) with a TODO for Leroy; the examiner's "plausible for a BWRX-300" reasoning is not used because no source supports it.
  - Point 4 (finding 4, steel): like-for-like comparison added (target-structure steel about 0.57 kt vs LC3 1.73 kt), marked "[examiner estimate, TODO: script]" because `lca_scenarios.py` has no such row; whole-plant row relabelled "upper bound"; feasibility caveat for forgings and nuclear plate [R2.6, R2.3].
  - Point 5 (finding 2, economic benefit): carbon value per unit and for Units 2–4, set against CAD 20.9 bn and one month's delay, as "[TODO: from results/initiative_cost.md]" (analyst run 5) [R2.3, R3.1].
  - Point 6 (finding 3, slag): business-as-usual consequence added; carbon case is for low-clinker infill; LC3 preference rests on the unsourced slag-supply premise, so "whichever binder qualifies first" until sourced.
  - Point 7 (§6.4): conversion-heat distribution test stated as a TODO for the lca-analyst (no output exists); mode/median wording simplified for a general reader.
  - Point 8 (§6.5): IPCC AR5 Annex III (Schlömer et al., 2014, in sources.md, unverified) added as a TODO, not a value.
  - Point 9 (figures): F3 placeholder carries the plain-label, mode-case-marker and embedded-title fixes as a lca-analyst TODO; F5 TODO kept.
  - L9 / R1.4: the 37 m / 35 m geometry is now cited as read (okdiario, 2026), not to OPG.
  - Granta kept as [TODO: results pending] (Victor's decision); A10 left ready to fill.
  - Length: to absorb the additions, the lead, §6.1 (reference-flow detail moved to T6), resource use, the tornado list and the §6.4 limitations were trimmed, and the Ng et al. (2025) comparison was cut from §6.5 (its scope is unconfirmed, L32). Hand estimate, not tool-counted: about 1,750 words of body text excluding tables, notes, captions and markers, about 3.5 pages at 500 words a page. Confirm with a Word count at integration; if over, fold "Resource use" into T6 first.
  - Presentation items: R5.1 (each subsection leads with its result; lead ends on the finding); R5.2 (T8 relabelled; F3 fixes listed); R5.3 (within budget); R5.4 (geometry cited as read); R5.5 (one unit throughout).
- v2, 21/10/2026 (writer, for Victor). Revised against factcheck.md §H: L55, L59, L67, L56/L35, L1/L52/L71, L9, L18; also L4, L5, L14, L22, L23, L25, L26, L32, L48, L57, L58, L60, L61, L62, L66, L31. Headline saving put on the Monte Carlo basis.
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/`. Sam's files are untouched.
- Table IDs T8 and T9 are new (T1–T7 are taken in plan §3 and §8.1). Leroy renumbers at integration.
-->

## 6 Life-cycle assessment and eco-audit

One BWRX-300 at Darlington is estimated to emit **about 4.2 g CO₂e per kWh delivered (Monte Carlo median; 90% interval 3.0–5.8; the median is 3.3 if conversion heat takes its central published value)**: below UNECE's 5.1–6.4 g/kWh for nuclear power on either reading and at the low end of the wider literature range. Nearly two-thirds comes from the fuel front end; construction is about 7.5%. The initiative, C1 (§4.3), specifies low-clinker concrete for targeted structures of Units 2–4, with LC3 as the target binder and slag as the fallback. LC3 would save **about 1,740 t CO₂e per unit (1,390–2,150 t) and 5,200 t across Units 2–4**, about 0.3% of each unit's life-cycle emissions. The saving is real but small, and **a delay of 9–15 days to one unit (Ontario's average grid factor; 1.3–1.4 days on the marginal factor) would cancel it**, so C1 is worth adopting only if it is schedule-neutral. No input has yet been checked in its primary source [TO VERIFY], so every number is provisional.

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of electricity from one BWRX-300 at the Darlington New Nuclear Project (Clarington, Ontario), find the hotspots, and size what C1 would save. This is a screening LCA following the goal-and-scope principles of ISO 14040/14044 [TODO: source needed: ISO 14040:2006 and ISO 14044:2006 entries in sources.md]. It has not been critically reviewed, so it cannot support a public comparative claim.

- **Functional unit:** 1 MWh of net electricity at the plant's grid connection. Results are in g CO₂e/kWh, which equals kg CO₂e/MWh. Grid transmission lies beyond the connection, so it is outside the boundary.
- **Reference flow:** one unit over its design life, 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh**, the same denominator as §7 (inputs and their status in Table T6; Appendix A2).
- **Baseline (S0):** the concrete OPG would pour anyway, without C1, modelled as general-use (GU) Portland cement with no supplementary cementitious materials. We have seen neither OPG's mix nor whether the governing specification (GE-Hitachi Nuclear Energy, 2024) limits cement type [TO VERIFY]. If OPG's mix already contains slag, S0 must include it: the §6.3 savings are then overstated, and LC3's gain over business as usual falls to about 100–180 t per unit (finding 3).
- **System boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are modelled bottom-up from process data; operation and maintenance (O&M), decommissioning and the back end are per-kWh values transferred from EDF's French-fleet LCA (EDF R&D, 2024) [TO VERIFY]. It is a **process-based LCA with three stages taken from secondary per-kWh data**.
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, upstream supply of the gas burnt for conversion heat, fuel-plant capital goods and recycling credits; each biases the result low (§6.5). End of life follows the cut-off (recycled-content) approach: steel carries the burden of its scrap input, with no credit for future recycling.
- **Impact category:** climate change, GWP100 (IPCC AR5 where stated). Construction-material factors are cradle-to-gate, EN 15804 modules A1–A3 [TODO: source needed: EN 15804 entry in sources.md]. The US grid factors are CO₂ only (US EPA, 2024) [TO VERIFY] and the basis of several others is [TO VERIFY]; for mostly fossil CO₂ this matters far less than the input ranges.

**Method.** In place of an eco-audit we use an **equivalent analysis**: a reproducible Python model multiplies material and fuel quantities by published emission factors (working in Appendices A and C). **No number here comes from Granta EduPack**; a cross-check of the C1 target structures is set up for the team's machines (Appendix A9) [TODO: Granta cross-check, H2 due Thu 12:00; cut if not run]. With no BWRX-300 bill of materials available, plant quantities are **scaled from per-MWe data for related reactors, not measured** (§6.2).

*Table T6. Key assumptions for one BWRX-300 at Darlington (all 40 ranged inputs in Appendix C2).*
*Source: `03_LCA_Calculations/parameters_lca.yaml`; references as listed. All values [TO VERIFY] unless marked as an assumption or placeholder. Ranges are model input bounds, not result intervals.*

| Parameter | Central (input range) | Basis |
|---|---|---|
| Net output; capacity factor; design life | 300 MWe (300–315); 0.90 (0.80–0.95); 60 years (40–80) | GE Vernova Hitachi Nuclear Energy (n.d.), with 315 MW net from an OPG filing [TO VERIFY]; placeholder; Canadian Nuclear Safety Commission (2024) |
| Baseline binder (S0) | General-use cement, no supplementary cementitious materials | Assumption: what OPG would pour anyway; OPG's mix and any cement-type limit in GE-Hitachi Nuclear Energy (2024) [TO VERIFY] |
| Whole-plant concrete; steel | 69 m³/MWe (34.5–138); 33 t/MWe (16.5–46) | ESBWR and ABWR (Peterson, Zhao and Petroski, 2005); vendor claim as low bound (GE Vernova, n.d.) |
| DPSC infill thickness: basemat; shaft wall | 3.0 m (2–4); 1.5 m (1–2) | Assumption (no source found) |
| Binder: DPSC self-consolidating infill; other concrete | 450 kg/m³ (400–550); 350 kg/m³ (300–420) | EFNARC (2005), read via a 2024 secondary, with central and high assumed; assumption |
| General-use cement | 854 kg CO₂e/t (796–898, regional spread West–East) | Cement Association of Canada (2022), AR5 factors; which region covers Ontario [TO VERIFY] |
| LC3 binder cut vs general-use cement | 37% (30–43%) | Median of five published estimates (Appendix A5) |
| Slag cement | 146.6 kg CO₂e/t (93.4–146.6) | Slag Cement Association (n.d.) |
| Rebar (electric-arc furnace); plate and equipment steel | 0.97 t/t (0.89–1.99); 1.73 t/t (1.22–2.50) | Concrete Reinforcing Steel Institute (2017) [superseded by a 2022 EPD, TO VERIFY]; American Institute of Steel Construction (2022) (Buy Clean California limits used as proxies; 1.22 is the hot-rolled-sections limit) |
| Other construction materials and site energy | +50% of bulk materials (25–150%) | Assumption |
| Mining and milling | 42 kg CO₂e/kg U₃O₈ (24–81) | Parker, McNaughton and Sparrow (2016) |
| Conversion heat; centrifuge enrichment | 26 kWh/kg U (26–665); 50 kWh/SWU (40–100) | Gibon and Hahn Menacho (2023) |
| Enrichment; burnup | 3.8% U-235 (3.4–4.95); 45 GWd/t (35–55) | [TODO: authors] (2025), unrefereed preprint; assumption (both placeholders) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh (×0.5 to ×2; decommissioning ×3) | EDF R&D (2024) stage shares as reported by secondary sources; back end by difference |

[Figure F1. LCA system boundary for one BWRX-300 at Darlington: bottom-up fuel front end and construction materials, literature values for operation, decommissioning and the back end, and the C1 target structures. | Source: this study. | File: 03_LCA_Calculations/results/F1_system_boundary.png]

### 6.2 Baseline inventory and hotspots

**Quantities.** Whole-plant concrete and steel are per-MWe intensities × 300 MWe. The central case uses the ESBWR, from which the BWRX-300 is derived: 69 m³ of concrete and 33 t of steel per MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY]. The sources pull in opposite directions: the vendor claims about 50% less concrete per unit of energy (GE Vernova, n.d.) [TO VERIFY], while small plants usually lose economies of scale. We take the vendor claim as the low input bound and the ABWR (138 m³/MWe) as the high, and assume the two effects cancel. That gives **20,700 m³ of concrete and 9,900 t of steel per unit** (concrete 90% interval about 15,050–36,521 m³; Appendix C4).

Of this, **13,100 m³ is in the C1 target structures**: the forebay shaft (4,000 m³ placed so far, a floor; Ontario Power Generation, 2025) [TO VERIFY] and the diaphragm-plate steel-composite (DPSC) infill of the reactor-building basemat and shaft walls (9,081 m³, from a 37 m module diameter, a 35 m shaft depth and assumed thicknesses). **Those two dimensions set 69% of the target concrete, and we read them in a news report of the Unit 1 basemat-module lift (okdiario, 2026) [TODO: sources.md entry] that cites an OPG story we have not found [TO VERIFY].** The 63% share of plant concrete this implies combines a geometric and a scaled estimate, so it is unconfirmed [TODO: Leroy: OPG EIS or Clinch River quantities]; a larger plant total would lower the share, not the saving.

**Resource use.** Per unit, the plant uses 0.35 kg of concrete and 0.070 kg of steel per MWh, and the fuel 20.7 g of natural uranium and 0.0146 separative work units (SWU) per MWh at 34.5% net efficiency ([TODO: authors], 2025; Appendix A8) [TO VERIFY]. Four units need about 196 t of natural uranium and 138 tSWU a year, the demand §8.3 should use to size supply risk [TODO: §8.3].

**Hotspots (Figure F2),** on the expected (Monte Carlo mean) basis:
1. **Mining and milling: 1.26 g/kWh (29%),** already low because Saskatchewan ores are high-grade (Parker, McNaughton and Sparrow, 2016) [TO VERIFY]; that Darlington's uranium is Canadian is [TO VERIFY].
2. **Conversion: 1.09 g/kWh (26%),** an *uncertainty* hotspot: published heat demand spans 26–665 kWh per kg of uranium (Gibon and Hahn Menacho, 2023) [TO VERIFY], and at the most likely value conversion is only 0.13 g/kWh.
3. **Back end: 0.65 g/kWh (15%),** transferred from France, which reprocesses; Canada plans direct disposal [TODO: source needed: NWMO], so this may be high.

The fuel front end is 64% of the total and construction about 7.5%. Within construction, steel emits about twice what concrete does (14,800 vs 7,600 t CO₂e per unit with every input at its most likely value, the "mode case"); Geneski, McKellar and Atkinson (n.d.) [TO VERIFY] also found that steel exceeds concrete. The C1 target concrete is 1.3% of the mode-case total, so **C1 acts on roughly one-hundredth of the footprint**, which caps what any concrete change can achieve.

[Figure F2. Life-cycle emissions of one BWRX-300 by stage: expected 4.3 g CO₂e/kWh (Monte Carlo mean), with the mode case (every input at its most likely value; total 2.7) marked. | Source: this study, scripts/lca_uncertainty.py; inputs in parameters_lca.yaml [TO VERIFY]. | File: 03_LCA_Calculations/results/F2_stage_breakdown.png]

### 6.3 The initiative against the baseline

**C1 is low-clinker concrete for the DPSC infill and forebay shafts of Units 2–4: LC3 (limestone calcined clay cement) as the target binder, a qualified slag blend as the fallback, specified only if schedule-neutral.** LC3 saves **about 1,740 t CO₂e per unit (Monte Carlo median; 90% interval 1,390–2,150 t) and about 5,200 t across Units 2–4 (4,160–6,460 t), avoiding about 6,900 t of clinker** (Table T8). Most of it (1,291 t) is in the DPSC infill, because the design calls for self-consolidating concrete (GE-Hitachi Nuclear Energy, 2024) [TO VERIFY], a cement-rich mix (450 kg binder/m³ assumed). Only Units 2–4 are counted, because Unit 1's basemat is placed and its forebay partly placed; whether Unit 1's shaft-wall infill could still use LC3 is [TO VERIFY].

*Table T8. Savings against the baseline (S0: what OPG would pour anyway, modelled as general-use cement), per unit and for Units 2–4. Monte Carlo columns give the median (5th–95th percentile); each draw's saving is divided by the same draw's life-cycle total.*
*Source: this study, `results/lca_scenarios.md` and `lca_uncertainty.md` (Appendices A6, A7 and C4). Inputs [TO VERIFY].*

| Scenario | Saving per unit, t CO₂e: Monte Carlo (mode case) | Units 2–4, t CO₂e (mode case) | Clinker avoided, t per unit / Units 2–4 | Share of one unit's life cycle: Monte Carlo (mode case) |
|---|---|---|---|---|
| S1 Slag cement, 40% of binder, in target structures (C1 fallback) | 1,642 (1,205–2,113) (1,552) | 4,657 | 2,019 / 6,057 | 0.28% (0.17–0.44%) (0.41%) |
| **S2 LC3-50 in target structures (C1 target binder)** | **1,742 (1,387–2,153) (1,734)** | **5,201** | **2,304 / 6,913** | **0.29% (0.18–0.46%) (0.45%)** |
| S2b LC3 in targets plus slag in all other concrete | 2,746 (1,809–4,107) (2,488) | 7,464 | 3,286 / 9,857 | 0.46% (0.26–0.80%) (0.65%) |
| S3 like-for-like: low-end steel factors, target-structure steel only | 941 (404–1,581) (566) | 1,698 | — | 0.16% (0.06–0.30%) (0.15%) |
| S3 upper bound: all plant steel at best-practice electric-arc-furnace sections factors | 4,731 (1,713–9,084) (3,714) | 11,142 | — | 0.79% (0.28–1.68%) (0.97%) |
| S3 sensitivity: all plant steel at world-average factors | −6,695 (−10,805 to −3,178) (−8,399; adds emissions) | −25,198 | — | −1.11% (−2.11 to −0.49%) (−2.19%) |

*Note: the mode-case share divides each saving by the mode-case life-cycle total (383,243 t CO₂e per unit). The Monte Carlo share is lower because the total grows with the skewed inputs while the saving barely moves (§6.4). S3 rows are sensitivities on the baseline steel, not part of C1.*

Five findings follow, each with a consequence for the initiative.
1. **C1 targets the right structures.** Concrete is about 66% of their known embodied emissions (5,078 t, against 2,619 t for the forebay rebar and DPSC basemat steel), and the saving exceeds the largest geometric uncertainty in it (530 t, wall thickness).
2. **The saving is small at plant scale, and so is its economic value.** It is about 0.3% of a unit's life cycle (0.45% in the mode case), or about 0.01 g/kWh, so C1 does not change the plant's climate case. At the federal industrial carbon price (C$95/t in 2026, C$115/t in 2030; Environment and Climate Change Canada, 2026) [TO VERIFY] it is worth about C$0.16–0.20 m per unit and C$0.49–0.60 m for Units 2–4. That is 0.004% of the C$13.2 bn for those units (four-unit budget C$20.9 bn; Ontario Power Generation, 2025) [TO VERIFY]. One day of delay to Units 2–4 costs C$1.8–2.9 m, three to six times C1's entire carbon value (Appendix B5.4). LC3 could carry a premium of up to about C$12.6–15.2/m³ (5.5–6.6% of the central concrete price) before it costs more per tonne than the carbon price; the abatement cost follows in §8.2.
3. **Slag nearly matches LC3, so the carbon case is for low-clinker infill, not for LC3 in particular.** LC3 saves only 97–180 t more per unit (Monte Carlo median and mode case; 90% interval −343 to +574 t), and more in only 64% of draws. If OPG's baseline already contains slag (§6.1), LC3's gain over business as usual is within this noise. Slag blends have precedent in nuclear concrete ([TODO: authors], 2026) [TO VERIFY], which makes a qualified slag blend the fallback if LC3 cannot be qualified in time (§8.1). Preferring LC3 rests on Ontario's slag supply shrinking, which is unsourced [TODO: source needed: Ontario blast-furnace-to-electric-arc conversions]; until it is sourced, the specification should accept whichever binder qualifies first.
4. **Within the structures C1 targets, concrete is the bigger lever; across the whole plant, steel is.** The low-end steel factors (Table T6) applied only to the steel in the target structures (953 t of DPSC basemat plate and 1,000 t of forebay rebar) save 566 t per unit (Monte Carlo median 941 t; 404–1,581), against LC3's 1,734 t (median 1,742): LC3 is about three times larger at the mode case and 1.9 times at the median. The shaft-wall plate is unknown and excluded, so this is a floor for the target-structure steel. Moving all 9,900 t of plant steel to those factors saves 3,714 t (median 4,731), about twice LC3, but that is an upper bound: it applies a hot-rolled-sections factor to forgings and nuclear-grade plate, for which it is not shown to be feasible. World-average steel would instead add 8,399 t. Lower-carbon steel is therefore the next lever (§10), not part of C1.
5. **Schedule dominates.** On the schedule-value results in §7 (Table T10; working in Appendix B5.3), a delay of **9.2 days (to-2050 view) to 14.6 days (whole-life view)** to one of Units 2–4 on Ontario's average grid factor, or **1.3–1.4 days** on the marginal factor (gas), would cancel that unit's LC3 saving (7.3–18.1 and 1.1–1.8 days across its 90% interval). C1 is therefore specified only if schedule-neutral, for example by qualifying the mix on mock-ups during Unit 1 construction (§8.6).

For the triple-bottom-line evaluation (§9), C1 is environmentally positive but marginal, its economic value is C$0.49–0.60 m for Units 2–4, and its feasibility hinges on qualification and schedule rather than on carbon.

### 6.4 Uncertainty: tornado and Monte Carlo

The tornado varies each of 40 inputs alone; the Monte Carlo varies all 40 together, 20,000 times (Appendix C).

**The life-cycle total depends on the fuel inputs, not the concrete (Figure F3).** The largest swings are conversion heat (2.70 → 5.37 g/kWh), the mining factor (2.26 → 3.65) and the back end (2.42 → 3.25), followed by burnup and enrichment level. No concrete input moves the total by more than 0.07 g/kWh; steel intensity moves it by 0.17. **The LC3 saving depends on the geometry and the mix**: the LC3 emission cut (1,406 → 2,015 t), DPSC wall thickness (1,464 → 1,995 t), infill binder content (1,590 → 2,021 t), and any extra binder LC3 needs to flow (10% more cuts the saving to 1,438 t). OPG's drawings and mock-up trials would narrow all four.

[Figure F3. One-at-a-time sensitivity of the life-cycle intensity (left, centred on the mode case, 2.70 g CO₂e/kWh, not the 4.2 median) and of the LC3 saving per unit (right, centred on the mode case, 1,734 t), top ten inputs each. | Source: this study, scripts/lca_uncertainty.py; ranges in parameters_lca.yaml. | File: 03_LCA_Calculations/results/F3_tornado.png]

**Monte Carlo (Figure F4): why we report 4.2, not 2.7, and why it is a range of medians.** The mode case (2.7 g/kWh) puts every input at its single most likely value. Several inputs, however, can mostly only rise: conversion heat is most likely 26 kWh/kg U but could be 665, which alone adds about 1.0 g/kWh to the average (Appendix C5). We therefore report the median of all draws (4.2 g/kWh) rather than the mode case; the same skew lowers LC3's share from 0.45% to 0.29%, while the saving itself barely moves. **The headline does depend on how conversion heat is distributed** (Table C2). With it fixed at Gibon and Hahn Menacho's (2023) central 26 kWh/kg U [TO VERIFY] the median is 3.3 g/kWh (90% interval 2.6–4.2); with a log-uniform 26–665 it is 3.9 (2.9–5.9). We therefore quote the **range of medians, 3.3–4.2 g/kWh**, and LC3's share of the life cycle ranges over 0.29–0.37%. Every value stays below UNECE's range. A measured conversion value would settle it [TODO: source needed: Cameco Port Hope]. Other limitations (independent draws, judgement ranges) are in Appendix C6.

[Figure F4. Monte Carlo distributions (20,000 draws, seed 20261021) of the life-cycle intensity (median 4.18, 5th–95th percentile 3.05–5.85 g CO₂e/kWh) and of the LC3 saving per unit (median 1,742, 1,387–2,153 t). | Source: this study, scripts/lca_uncertainty.py. | File: 03_LCA_Calculations/results/F4_montecarlo.png]

### 6.5 Comparison with published values

**Our median (3.3–4.2 across conversion-heat assumptions, §6.4) is below UNECE's 5.1–6.4 g/kWh (United Nations Economic Commission for Europe, 2021; our 90% interval overlaps it) and at the low end of the wider literature range, for reasons we can identify (Figure F5, Table T9).** It overlaps EDF's French fleet (3.7 g/kWh; EDF R&D, 2024) and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016) and the harmonised light-water-reactor median of 12 (Warner and Heath, 2012) [TODO: add the IPCC AR5 WGIII Annex III minimum, median and maximum (Schlömer et al., 2014) once a value is confirmed]. All benchmark values are [TO VERIFY]. Our median is about 100–120 times lower than gas combined cycle (403–513 g/kWh) and 180–260 times lower than coal (751–1,095) (United Nations Economic Commission for Europe, 2021).

*Table T9. Why our result differs from the benchmarks: direction and size of each reason.*
*Source: this study (Appendices A and C), with the references as listed. All [TO VERIFY].*

| Reason | Effect on our value | Size |
|---|---|---|
| High-grade Canadian ore | Lower | Our mining is 1.0–1.3 g/kWh; at global-average grades Gibon and Hahn Menacho (2023) attribute 46% of 6.1, about 2.8 g/kWh, to it. This explains most of the gap to UNECE and Gibon |
| Centrifuge enrichment only | Lower than older studies | 50 kWh/SWU against about 2,500 for the diffusion plants in older study sets (Gibon and Hahn Menacho, 2023; Warner and Heath, 2012) |
| Energy-only fuel inventory (cut-offs) | Lower | Not quantified (chemicals, cladding, upstream gas, fuel-plant capital goods excluded) |
| Construction possibly underestimated | Lower | Ours 0.24–0.32 g/kWh against about 0.59 for large reactors (16% of 3.7; EDF R&D, 2024). At 0.6–1.0, the total would rise 0.3–0.8 g/kWh and LC3's share would fall further |
| Long life and high capacity factor | Lower | At 40 years instead of 60, the mode case rises from 2.70 to 2.82 g/kWh |
| O&M and back end transferred from France (reprocessing) | Possibly higher | Canada plans direct disposal; back-end range 0.28–1.11 g/kWh tested |
| SMR rather than large reactor | Small | Carless, Griffin and Fischbeck (2016) give 9.1 for an SMR against 8.4 for the AP1000, mainly through the fuel cycle; our construction share is too small for scale effects to move the total much |

The sources disagree mainly about the fuel front end (ore grade, enrichment technology and grid), not about construction, and that is where our result departs from them. The known low bias (cut-offs, possibly construction) would raise the total and make C1's share smaller still, so it does not weaken §6.3. If the Granta cross-check is run, its construction values will be compared here with the model's (Appendix A9) [TODO: Granta cross-check, H2 due Thu 12:00; cut if not run].

[Figure F5. Our BWRX-300 result against published nuclear life-cycle values (point = central or median; line = range or interval); coal about 750–1,100 and gas combined cycle 403–513 g CO₂e/kWh for scale. UNECE reports a range only (5.1–6.4), so it is drawn as a range with no midpoint; Warner and Heath are drawn as a median only (12). | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012). Benchmarks [TO VERIFY]. | File: 03_LCA_Calculations/results/F5_benchmarks.png] [TODO: IPCC AR5 WGIII Annex III row is drawn automatically once its values are set to verified in parameters_lca.yaml]

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: life-cycle intensity with a 90% interval, stage hotspots, savings per structure, per unit and for Units 2–4, clinker avoided, fuel demand, and a scripted like-for-like steel comparison with Monte Carlo shares for every scenario (T8). Missing: verified inputs.
- **R2.2 (eco-audit or equivalent).** Produced: an equivalent analysis covering the whole life cycle, honestly labelled. Missing: the Granta EduPack cross-check [TODO: Granta cross-check, H2 due Thu 12:00; cut if not run].
- **R2.3 (resources and benefits sized to the proposal).** Produced: kg/MWh, g U and SWU per MWh, net efficiency, t CO₂e and t clinker for Darlington Units 2–4; economic benefit (C$0.49–0.60 m, break-even premium C$12.6–15.2/m³, cost of delay, finding 2). Missing: §8.3 use of the fuel demand; Leroy's plant data; a sourced LC3 price and qualification cost.
- **R2.4 (methods clear, working in appendix).** Produced: §6.1 method; full working in Appendices A and C. Missing: §2 methods paragraph.
- **R2.5 (assumptions, scope, functional unit).** Produced: FU (transmission outside the boundary), reference flow, the S0 counterfactual and its consequence, boundary, cut-offs, end-of-life approach, impact category, T6. Missing: ISO 14040/44 and EN 15804 entries in `sources.md`; OPG's actual baseline mix; GWP basis of several factors.
- **R2.6 (logical, justified).** Produced: like-for-like steel comparison and the whole-plant row relabelled as an upper bound; slag-vs-LC3 tied to the baseline; the LC3 preference reduced to what the evidence supports. Missing: the slag-supply source (or "whichever qualifies first" stands).
- **R2.7 and RB.6.** Produced: tornado, Monte Carlo, the conversion-heat distribution test and its result (range of medians 3.3–4.2), limitations, seven discrepancy reasons with sign and size, F3 and F5 redrawn. Missing: verified benchmarks; IPCC AR5 values.
- **R1.3, R1.4.** Produced: syntheses as in v2; the geometry now cited as read. Missing: verification; a sources.md entry for the news report; OPG story or NEDO-33926 dimensions.
- **R4.1–R4.4, RB.1, RB.8 (supporting).** Produced: the sharpened C1 statement, the schedule condition in the lead, the honest 0.3% finding, the TBL inputs for §9 (economic value now in). Missing: §9 draft.
- **R5.1–R5.5.** Produced: lead ends on the finding; one unit; T8 on one basis; F3 and F5 redrawn; about 3.6 pages (hand estimate, to confirm in Word). Missing: markers stripped before submission.

### Remaining TODOs

1. **[TO VERIFY, blocking HD]** Open the LCA primaries in the priority order of `02_Research/sources_lca.md` (Gibon and Hahn Menacho 2023; Parker et al. 2016; EDF R&D 2024; the OPG basemat story or NEDO-33926 dimensions; the CAC 2022 EPD region; the five LC3 estimates; Peterson et al. 2005; the CRSI 2022 EPD; UNECE 2021 and one title for it; Warner and Heath's minimum; Ng et al.'s scope). Set `status: verified`, re-run the three `lca_*.py` scripts and update every number here.
2. **[TO VERIFY]** OPG's actual infill and forebay mix, and whether NEDO-33926 limits cement type. If the baseline already has slag, re-define S0 and re-run (§6.1, finding 3).
3. **[TO VERIFY]** The federal carbon price path (C$95 in 2026, C$115 in 2030) and the OPG C$149/MWh behind finding 2's delay costs.
4. **[TO VERIFY]** A sourced central value for conversion heat (Gibon and Hahn Menacho 2023; Cameco Port Hope), which decides whether the headline is 3.3 or 4.2.
5. **[TODO: Granta cross-check, H2 due Thu 12:00; cut if not run]** `results/granta_inputs.md`, under one hour; fill Table A10. If not run, cut A9 and every Granta sentence (§6.1, §6.5, Appendices A and C).
7. **[TODO: Leroy]** Net MWe, capacity factor, design life, burnup, enrichment, uranium origin; whole-plant concrete and steel (OPG EIS, TVA Clinch River ER, NEDO-33926 thicknesses; forebay per unit or shared); whether Unit 1's shaft-wall infill is still to be poured.
8. **[TODO: source needed]** ISO 14040:2006, ISO 14044:2006 and EN 15804 entries in `sources.md`; a `sources.md` entry for the okdiario (2026) news report; NWMO (direct disposal); Cameco Port Hope (conversion); Ontario blast-furnace-to-electric-arc conversions (finding 3); authors of the arXiv overview (2025) and the 2026 nuclear-concrete paper; IPCC AR5 Annex III values.
9. **[TODO: references]** Disambiguate Ontario Power Generation (2025) (forebay update vs Q1 2025 results with the CAD 20.9 bn budget) with letter suffixes.
10. **[TODO: §8.3]** Use the four-unit fuel demand (196 t U and 138 tSWU a year).
11. **[Deck, Victor]** Slides 5–8 to match: the sharpened C1 title; "slag nearly matches; within the target structures LC3 is the bigger lever, whole-plant low-carbon steel up to about 2× (upper bound)"; the 9–15 and 1.3–1.4 day break-evens; the 3.3–4.2 range; no Granta claim; concrete range 15,000–36,500 m³.
