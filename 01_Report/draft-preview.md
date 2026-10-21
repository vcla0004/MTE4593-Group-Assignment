---
title: "MTE4593 SMR report: DRAFT PREVIEW (21/10)"
---

**Draft preview, not the submission.** It contains only the sections drafted so far. Missing: §1–§5, §8.6, §9–§11 and the abstract. Every [TO VERIFY] marker is still unverified, and §7 may still be in progress.

Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3 (also supports R3.1, R4.1, R4.2, R4.3, R4.4, RB.1, RB.8, R5.1, R5.2, R5.3)

<!--
CHANGELOG
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

One BWRX-300 at Darlington is estimated to emit **about 4.2 g CO₂e per kWh delivered (Monte Carlo median; 90% interval 3.0–5.8)**: just below UNECE's 5.1–6.4 g/kWh for nuclear power (our interval overlaps it) and at the low end of the wider literature range. Nearly two-thirds comes from the fuel front end; construction is about 7.5%. The initiative, C1 (§4.3), specifies low-clinker concrete for targeted structures of Units 2–4, with LC3 as the target binder and slag as the fallback. LC3 would save **about 1,740 t CO₂e per unit (1,390–2,150 t) and 5,200 t across Units 2–4**, about 0.3% of each unit's life-cycle emissions. The saving is real but small, and **a delay of about 1.4–15 days to one unit would cancel it**, so C1 is worth adopting only if it is schedule-neutral. No input has yet been checked in its primary source [TO VERIFY], so every number is provisional.

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of electricity from one BWRX-300 at the Darlington New Nuclear Project (Clarington, Ontario), find the hotspots, and size what C1 would save. This is a screening LCA following the goal-and-scope principles of ISO 14040/14044 [TODO: source needed: ISO 14040:2006 and ISO 14044:2006 entries in sources.md]. It has not been critically reviewed, so it cannot support a public comparative claim.

- **Functional unit:** 1 MWh of net electricity at the plant's grid connection. Results are in g CO₂e/kWh, which equals kg CO₂e/MWh. Grid transmission lies beyond the connection, so it is outside the boundary.
- **Reference flow:** one unit over its design life, 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh**, the same denominator as §7 (inputs and their status in Table T6; Appendix A2).
- **Baseline (S0):** the concrete OPG would pour anyway, without C1, modelled as general-use (GU) Portland cement with no supplementary cementitious materials. We have seen neither OPG's mix nor whether the governing specification (GE-Hitachi Nuclear Energy, 2024) limits cement type [TO VERIFY]. If OPG's mix already contains slag, S0 must include it: the §6.3 savings are then overstated, and LC3's gain over business as usual falls to about 100–180 t per unit (finding 3).
- **System boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are modelled bottom-up from process data; operation and maintenance (O&M), decommissioning and the back end are per-kWh values transferred from EDF's French-fleet LCA (EDF R&D, 2024) [TO VERIFY]. It is a **process-based LCA with three stages taken from secondary per-kWh data**.
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, upstream supply of the gas burnt for conversion heat, fuel-plant capital goods and recycling credits; each biases the result low (§6.5). End of life follows the cut-off (recycled-content) approach: steel carries the burden of its scrap input, with no credit for future recycling.
- **Impact category:** climate change, GWP100 (IPCC AR5 where stated). Construction-material factors are cradle-to-gate, EN 15804 modules A1–A3 [TODO: source needed: EN 15804 entry in sources.md]. The US grid factors are CO₂ only (US EPA, 2024) [TO VERIFY] and the basis of several others is [TO VERIFY]; for mostly fossil CO₂ this matters far less than the input ranges.

**Method.** In place of an eco-audit we use an **equivalent analysis**: a reproducible Python model multiplies material and fuel quantities by published emission factors (working in Appendices A and C). **No number here comes from Granta EduPack**; a cross-check of the C1 target structures is set up for the team's machines (Appendix A9) [TODO: results pending]. With no BWRX-300 bill of materials available, plant quantities are **scaled from per-MWe data for related reactors, not measured** (§6.2).

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

*Table T8. Savings against the baseline (S0: what OPG would pour anyway, modelled as general-use cement), per unit and for Units 2–4. Every column except the bracketed interval is on the mode-case basis (every input at its most likely value).*
*Source: this study, `results/lca_scenarios.csv` and `lca_montecarlo_summary.csv` (Appendices A6, A7 and C4). The like-for-like steel row is the examiner's estimate (review.md, 21/10), not yet scripted. Inputs [TO VERIFY].*

| Scenario | t CO₂e saved per unit, mode case (MC 5th–95th percentile) | Units 2–4, t CO₂e | Clinker avoided, t per unit / Units 2–4 | Share of one unit's life cycle |
|---|---|---|---|---|
| S1 Slag cement, 40% of binder, in target structures (C1 fallback) | 1,552 (1,205–2,113) | 4,657 | 2,019 / 6,057 | 0.41% |
| **S2 LC3-50 in target structures (C1 target binder)** | **1,734 (1,387–2,153)** | **5,201** | **2,304 / 6,913** | **0.45%** |
| S2b LC3 in targets plus slag in all other concrete | 2,488 | 7,464 | 3,286 / 9,857 | 0.65% |
| S3 like-for-like: low-end steel factors, target-structure steel only | about 570 [examiner estimate, TODO: script] | [TODO: script] | — | [TODO: script] |
| S3 upper bound: all plant steel at best-practice electric-arc-furnace sections factors | 3,714 | 11,142 | — | 0.97% |
| S3 sensitivity: all plant steel at world-average factors | −8,399 (adds emissions) | −25,198 | — | −2.19% |

*Note: shares are each saving divided by the mode-case life-cycle total (383,243 t CO₂e per unit). On the Monte Carlo basis the savings have medians of 1,742 t (LC3) and 1,642 t (slag), and LC3's share has a median of 0.29% (0.18–0.46%), lower because the total grows while the saving barely moves (§6.4). Monte Carlo shares for S1, S2b and S3 are not in the model outputs [TODO: lca-analyst to add them to `lca_montecarlo_summary.csv`]. S3 rows are sensitivities on the baseline steel, not part of C1.*

Five findings follow, each with a consequence for the initiative.
1. **C1 targets the right structures.** Concrete is about 66% of their known embodied emissions (5,078 t, against 2,619 t for the forebay rebar and DPSC basemat steel), and the saving exceeds the largest geometric uncertainty in it (530 t, wall thickness).
2. **The saving is small at plant scale, and so is its economic value.** It is about 0.3% of a unit's life cycle (0.45% in the mode case), or about 0.01 g/kWh, so C1 does not change the plant's climate case. At [TODO: carbon price and basis, from results/initiative_cost.md] it is worth [TODO: from results/initiative_cost.md] per unit and [TODO: from results/initiative_cost.md] for Units 2–4, against a four-unit budget of CAD 20.9 bn (Ontario Power Generation, 2025) [TO VERIFY] and the value of one month's delay to one unit [TODO: from results/initiative_cost.md]. The cost per tonne abated follows in §8.2.
3. **Slag nearly matches LC3, so the carbon case is for low-clinker infill, not for LC3 in particular.** LC3 saves only 97–180 t more per unit (Monte Carlo median and mode case; 90% interval −343 to +574 t), and more in only 64% of draws. If OPG's baseline already contains slag (§6.1), LC3's gain over business as usual is within this noise. Slag blends have precedent in nuclear concrete ([TODO: authors], 2026) [TO VERIFY], which makes a qualified slag blend the fallback if LC3 cannot be qualified in time (§8.1). Preferring LC3 rests on Ontario's slag supply shrinking, which is unsourced [TODO: source needed: Ontario blast-furnace-to-electric-arc conversions]; until it is sourced, the specification should accept whichever binder qualifies first.
4. **Within the structures C1 targets, concrete is the bigger lever; across the whole plant, steel is.** The low-end steel factors (Table T6) applied only to the steel in the target structures (953 t of DPSC basemat plate and 1,000 t of forebay rebar) save about 570 t per unit [examiner estimate, TODO: script], against LC3's 1,734 t. Moving all 9,900 t of plant steel to those factors saves 3,714 t, about twice LC3, but that is an upper bound: it applies a hot-rolled-sections factor to forgings and nuclear-grade plate, for which it is not shown to be feasible. World-average steel would instead add 8,399 t. Lower-carbon steel is therefore the next lever (§10), not part of C1.
5. **Schedule dominates.** On the schedule-value results used in §7, a delay of 10–15 days to one of Units 2–4 (Ontario average grid trajectory), or about 1.4 days (marginal grid, declining), would cancel that unit's LC3 saving [TODO: Appendix B working for schedule value]. C1 is therefore specified only if schedule-neutral, for example by qualifying the mix on mock-ups during Unit 1 construction (§8.6).

For the triple-bottom-line evaluation (§9), C1 is environmentally positive but marginal, its economic value is [TODO: from results/initiative_cost.md], and its feasibility hinges on qualification and schedule rather than on carbon.

### 6.4 Uncertainty: tornado and Monte Carlo

The tornado varies each of 40 inputs alone; the Monte Carlo varies all 40 together, 20,000 times (Appendix C).

**The life-cycle total depends on the fuel inputs, not the concrete (Figure F3).** The largest swings are conversion heat (2.70 → 5.37 g/kWh), the mining factor (2.26 → 3.65) and the back end (2.42 → 3.25), followed by burnup and enrichment level. No concrete input moves the total by more than 0.07 g/kWh; steel intensity moves it by 0.17. **The LC3 saving depends on the geometry and the mix**: the LC3 emission cut (1,406 → 2,015 t), DPSC wall thickness (1,464 → 1,995 t), infill binder content (1,590 → 2,021 t), and any extra binder LC3 needs to flow (10% more cuts the saving to 1,438 t). OPG's drawings and mock-up trials would narrow all four.

[Figure F3. One-at-a-time sensitivity of the life-cycle intensity (left, centred on the mode case, 2.70 g CO₂e/kWh) and of the LC3 saving per unit (right, central 1,734 t), top ten inputs each. | Source: this study, scripts/lca_uncertainty.py; ranges in parameters_lca.yaml. | File: 03_LCA_Calculations/results/F3_tornado.png] [TODO: lca-analyst to replace the Python variable names with plain labels (e.g. "Conversion heat (kWh/kg U)"), mark the left axis centre "mode case 2.70", and remove the embedded "Figure F3." title]

**Monte Carlo (Figure F4): why we report 4.2, not 2.7.** The mode case (2.7 g/kWh) puts every input at its single most likely value. Several inputs, however, can mostly only rise: conversion heat is most likely 26 kWh/kg U but could be 665, which alone adds about 1.0 g/kWh to the average (Appendix C5). We therefore report the median of all draws (4.2 g/kWh) rather than the mode case; the same skew lowers LC3's share from 0.45% to 0.29%, while the saving itself barely moves. Whether 4.2 is an artefact of the triangular shape chosen for conversion heat is to be tested with conversion heat held at a sourced central value and drawn log-uniform [TODO: lca-analyst: script flag; result row in Table C2]. Other limitations (independent draws, judgement ranges) are in Appendix C6.

[Figure F4. Monte Carlo distributions (20,000 draws, seed 20261021) of the life-cycle intensity (median 4.18, 5th–95th percentile 3.05–5.85 g CO₂e/kWh) and of the LC3 saving per unit (median 1,742, 1,387–2,153 t). | Source: this study, scripts/lca_uncertainty.py. | File: 03_LCA_Calculations/results/F4_montecarlo.png]

### 6.5 Comparison with published values

**Our median is just below UNECE's 5.1–6.4 g/kWh (United Nations Economic Commission for Europe, 2021; our 90% interval overlaps it) and at the low end of the wider literature range, for reasons we can identify (Figure F5, Table T9).** It overlaps EDF's French fleet (3.7 g/kWh; EDF R&D, 2024) and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016) and the harmonised light-water-reactor median of 12 (Warner and Heath, 2012) [TODO: add the IPCC AR5 WGIII Annex III minimum, median and maximum (Schlömer et al., 2014) once a value is confirmed]. All benchmark values are [TO VERIFY]. Our median is about 100–120 times lower than gas combined cycle (403–513 g/kWh) and 180–260 times lower than coal (751–1,095) (United Nations Economic Commission for Europe, 2021).

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

The sources disagree mainly about the fuel front end (ore grade, enrichment technology and grid), not about construction, and that is where our result departs from them. The known low bias (cut-offs, possibly construction) would raise the total and make C1's share smaller still, so it does not weaken §6.3. If the Granta cross-check is run [TODO: results pending], its construction values will be compared here with the model's (Appendix A9).

[Figure F5. Our BWRX-300 result against published nuclear life-cycle values (point = central or median; line = range or interval); coal about 750–1,100 and gas combined cycle 403–513 g CO₂e/kWh for scale. UNECE reports a range only: its point at 5.8 is our midpoint, not a UNECE value. | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012). Benchmarks [TO VERIFY]. | File: 03_LCA_Calculations/results/F5_benchmarks.png] [TODO: lca-analyst to redraw UNECE as a range only, drop any 3.7 minimum attributed to Warner and Heath (factcheck L31, L66), and remove the embedded "Figure F5." title]

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: life-cycle intensity with a 90% interval, stage hotspots, savings per structure, per unit and for Units 2–4, clinker avoided, fuel demand, and a like-for-like steel comparison (examiner estimate). Missing: verified inputs; the scripted like-for-like steel row.
- **R2.2 (eco-audit or equivalent).** Produced: an equivalent analysis covering the whole life cycle, honestly labelled. Missing: the Granta EduPack cross-check [TODO: results pending].
- **R2.3 (resources and benefits sized to the proposal).** Produced: kg/MWh, g U and SWU per MWh, net efficiency, t CO₂e and t clinker for Darlington Units 2–4; the economic-benefit sentence is in place (finding 2). Missing: its numbers from `results/initiative_cost.md`; §8.3 use of the fuel demand; Leroy's plant data.
- **R2.4 (methods clear, working in appendix).** Produced: §6.1 method; full working in Appendices A and C. Missing: §2 methods paragraph.
- **R2.5 (assumptions, scope, functional unit).** Produced: FU (transmission outside the boundary), reference flow, the S0 counterfactual and its consequence, boundary, cut-offs, end-of-life approach, impact category, T6. Missing: ISO 14040/44 and EN 15804 entries in `sources.md`; OPG's actual baseline mix; GWP basis of several factors.
- **R2.6 (logical, justified).** Produced: like-for-like steel comparison and the whole-plant row relabelled as an upper bound; slag-vs-LC3 tied to the baseline; the LC3 preference reduced to what the evidence supports. Missing: the slag-supply source (or "whichever qualifies first" stands).
- **R2.7 and RB.6.** Produced: tornado, Monte Carlo, the conversion-heat distribution test specified, limitations, seven discrepancy reasons with sign and size. Missing: the test's result; verified benchmarks; IPCC AR5 values; the F5 redraw.
- **R1.3, R1.4.** Produced: syntheses as in v2; the geometry now cited as read. Missing: verification; a sources.md entry for the news report; OPG story or NEDO-33926 dimensions.
- **R4.1–R4.4, RB.1, RB.8 (supporting).** Produced: the sharpened C1 statement, the schedule condition in the lead, the honest 0.3% finding, the TBL inputs for §9. Missing: §4.3 and §9 drafts; the economic value.
- **R5.1–R5.5.** Produced: lead ends on the finding; one unit; T8 labels; figure fixes listed; about 3.5 pages (hand estimate, to confirm in Word). Missing: the F3/F5 redraws; markers stripped before submission.

### Remaining TODOs

1. **[TO VERIFY, blocking HD]** Open the LCA primaries in the priority order of `02_Research/sources_lca.md` (Gibon and Hahn Menacho 2023; Parker et al. 2016; EDF R&D 2024; the OPG basemat story or NEDO-33926 dimensions; the CAC 2022 EPD region; the five LC3 estimates; Peterson et al. 2005; the CRSI 2022 EPD; UNECE 2021 and one title for it; Warner and Heath's minimum; Ng et al.'s scope). Set `status: verified`, re-run the three `lca_*.py` scripts and update every number here.
2. **[TO VERIFY]** OPG's actual infill and forebay mix, and whether NEDO-33926 limits cement type. If the baseline already has slag, re-define S0 and re-run (§6.1, finding 3).
3. **[TODO: from results/initiative_cost.md]** Carbon price and basis; carbon value per unit and for Units 2–4; value of one month's delay to one unit (finding 2 and the §9 line). Analyst run 5.
4. **[TODO: script]** lca-analyst: add the like-for-like S3 row (low-end steel factors on target-structure steel only) to `lca_scenarios.py`, with Units 2–4 and the life-cycle share, and replace the examiner's estimate (about 570 t) in T8 and finding 4.
5. **[TODO: lca-analyst]** Conversion-heat distribution test (sourced central value; log-uniform) as a row in Table C2; Monte Carlo shares for S1, S2b and S3; F3 plain labels, mode-case marker and no embedded title; F5 redraw (L66, L31) and no embedded title; correct `results/lca.md` (L64).
6. **[TODO: results pending]** Granta EduPack cross-check (`results/granta_inputs.md`, under one hour); fill Table A10. If not run by the freeze, cut A9 and every Granta sentence (§6.1, §6.5).
7. **[TODO: Leroy]** Net MWe, capacity factor, design life, burnup, enrichment, uranium origin; whole-plant concrete and steel (OPG EIS, TVA Clinch River ER, NEDO-33926 thicknesses; forebay per unit or shared); whether Unit 1's shaft-wall infill is still to be poured.
8. **[TODO: source needed]** ISO 14040:2006, ISO 14044:2006 and EN 15804 entries in `sources.md`; a `sources.md` entry for the okdiario (2026) news report; NWMO (direct disposal); Cameco Port Hope (conversion); Ontario blast-furnace-to-electric-arc conversions (finding 3); authors of the arXiv overview (2025) and the 2026 nuclear-concrete paper; IPCC AR5 Annex III values.
9. **[TODO: references]** Disambiguate Ontario Power Generation (2025) (forebay update vs Q1 2025 results with the CAD 20.9 bn budget) with letter suffixes.
10. **[TODO: Appendix B]** Schedule-value working (`results/schedule_value.md`), cited in finding 5.
11. **[TODO: §8.3]** Use the four-unit fuel demand (196 t U and 138 tSWU a year).
12. **[Deck, Victor]** Slides 5–8 to match: the sharpened C1 title; "slag nearly matches; within the target structures LC3 is the bigger lever, whole-plant low-carbon steel up to about 2× (upper bound)"; no Granta claim; concrete range 15,000–36,500 m³.


Rubric coverage: R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, R3.6, RB.5, RB.6 (also supports R3.5, R3.7, RB.8, R5.1, R5.2, R5.3)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, Q4). First draft from Q2's re-based results (displacement, schedule_value, same_money), run 5 (lcoe, initiative_cost), both briefs and §6 v3; working in App B4–B6. Addresses review audit §2 (R2 "economic benefits ... appropriate to the scale of the proposal"; R4 "new feasible ideas or connections") and factcheck L47 (break-even working).
- Conflicts per plan §5: GenCost = run 5's 2030 reading (A$230–382, 2.9×), 5.0× stated as the alternative [TO VERIFY: GenCost table/year]; carbon price = federal path C$95 (2026) / C$115 (2030) [TO VERIFY]; C$170 used only for the conservative end of 30–223× (explained in B5.3).
- factcheck S2 (boundary mismatch) stated; deck's "13×" replaced by the timing-aware comparison; S3 (300 vs 315 MWe) and S9 (start year) left as TODOs.
- Presentation: R5.1 leads with the schedule finding; R5.2 T10, F6, F7 specified from results; R5.3 about 880 body words excluding table, captions and markers (about 1.75 p, hand estimate; confirm in Word); R5.4 Harvard; R5.5 Australian English.
- T10 is a new table ID; renumber at assembly (Q19).
-->

## 7 Carbon avoided: Ontario vs Liddell, the value of schedule, and the same money on firmed renewables

**For C1, schedule matters far more than concrete.** A one-month slip of Units 2–4 costs C$33–110 m in carrying cost and defers about C$88 m of output: **30–223 times the carbon value of C1's entire saving**. Per unit, the LC3 saving (about 1,740 t CO₂e, §6.3) is cancelled by **9–15 days of delay on Ontario's average grid factor, or 1.3–1.4 days on its marginal factor**. Timing also decides where an SMR helps the climate at all. Counted from when each plant could actually run, a Darlington unit avoids as much CO₂e to 2050 as a unit at Liddell, or more. And at Liddell, the same money spent on firmed renewables avoids more CO₂e in every case we tested. Every input is provisional [TO VERIFY]; the working is in Appendices B4–B6.

**Method.** CO₂e avoided = output × (intensity of the displaced electricity − 4.2 g CO₂e/kWh, our life-cycle value from §6). The output is that of one 300 MWe unit at a 0.90 capacity factor, 2.365 TWh a year [TODO: Leroy: 300 vs 315 MWe net].
- An *average* factor is the grid's mean intensity.
- A *marginal* factor is the intensity of the generation that actually runs less (mostly gas in Ontario). It is the factor recommended for evaluating new supply (The Atmospheric Fund, 2025) [TO VERIFY].
- The grid trajectories are our own constructions from published anchor points [TODO: replace with the 2026 ISP Step Change and IESO series].

### 7.1 The value of schedule

**A saving of kilotonnes is undone by a few days of delay.** A unit that starts late gives up each day's displacement (Table T10). Counted to 2050 (the "gross" view), that loss is permanent. Over the plant's whole life (the "net" view), the lost time comes back at the end of life, but on a cleaner grid.

*Table T10. Days of delay that cancel C1's LC3 saving, Darlington Units 2–4 (start 2035).*
*Source: this study, `scripts/schedule_value.py` (`results/schedule_value.md` §6; Appendix B5). Saving 1,734 t per unit and 5,201 t for Units 2–4 (§6.3). Brackets give the range over the saving's 90% interval. Grid factors: The Atmospheric Fund (2025); Independent Electricity System Operator (2024) [TO VERIFY].*

| Ontario grid case | CO₂e lost per day of delay, one unit (t, gross / net) | Days that cancel one unit's saving (gross / net) | Days of delay to one unit that cancel all of Units 2–4's saving (gross / net) |
|---|---|---|---|
| Average, falling to 15 g/kWh by 2040 | 189 / 119 | 9.2 (7.3–11.4) / 14.6 (11.6–18.1) | 28 / 44 |
| Marginal (gas), leaving the margin by 2050 | 1,296 / 1,226 | 1.3 (1.1–1.7) / 1.4 (1.1–1.8) | 4.0 / 4.2 |

**In money the gap is wider.** Canada's industrial carbon price is C$95/t in 2026, rising to C$115/t in 2030 (Environment and Climate Change Canada, 2026) [TO VERIFY]. At those prices, C1's 5,200 t across Units 2–4 is worth **C$0.49–0.60 m**. Even at the superseded C$170/t and the 95th-percentile saving, it is worth only C$1.10 m. A one-month slip of the three units does far more damage:
- It costs C$33–110 m in carrying cost (3–10% a year on their C$13.2 bn). This is an upper bound, because it assumes all the capital has already been spent.
- It defers about C$88 m of output at OPG's reported C$149/MWh [TO VERIFY; TODO: merge `opg_oeb_lcoe_lead` into sources.md].
- It loses 10.9–118 kt CO₂e, 2.1–22.7 times C1's saving.

The carbon value is also only a shadow price. Construction-material emissions appear to fall outside Ontario's industrial carbon pricing [TO VERIFY: analyst inference] (§8.2), so nobody is paid for the saving. **Schedule neutrality is therefore the binding condition on C1.** The mix must be qualified on mock-ups during Unit 1, before the Units 2–4 decision expected in 2028 [TO VERIFY] (§8.6).

### 7.2 What one BWRX-300 displaces: Darlington vs Liddell

**At today's grid factors, a unit at Liddell would avoid about nine times more CO₂e than one at Darlington. Timing closes most of that gap.**
- **NSW:** on the NSW grid average of 640 g/kWh (Department of Climate Change, Energy, the Environment and Water, 2025) [TO VERIFY], one unit avoids **1.50 Mt a year**.
- **Ontario, average:** on the 2024 average of 73.8 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY], it avoids 0.165 Mt. NSW's figure is **9.1×** larger, or 20.6× on Canada Energy Regulator (n.d.) data for 2022.
- **Ontario, marginal:** on the marginal factor of 343 g/kWh (The Atmospheric Fund, 2025) [TO VERIFY definition], Darlington avoids 0.80 Mt and the ratio falls to **1.9×**.

**The two plants would not run in the same years.**
- Darlington Unit 1 runs from 2030 [TODO: Leroy: in-service date].
- An Australian unit is unlikely before 2040, CSIRO's earliest date for nuclear (Graham, Hayward and Foster, 2024) [TO VERIFY that it covers SMRs]. The Coalition claimed 2035 (ABC News, 2024) [TO VERIFY; secondary].
- If coal leaves the NEM by 2038, as in AEMO's Step Change scenario (Australian Energy Market Operator, 2024) [TO VERIFY; secondary], a 2040 unit displaces only a residual mix (30 g/kWh, assumed).

**CO₂e avoided to 2050 (Figure F6):**
- **Darlington Unit 1:** **1.0–6.8 Mt**, from the average trajectory to the declining marginal factor.
- **Liddell:** **0.67–3.9 Mt**, from the Step Change proxy to a slower transition. It reaches 16.5 Mt only if the NEM stays at 640 g/kWh.
- **Whole life:** the two sites are close, at 2.0–7.8 Mt against 3.7–6.8 Mt.

**What moves the results.** The grid trajectory, the start year and the post-coal floor move them by an order of magnitude. Capacity factor, net output and our life-cycle interval (3.0–5.8 g/kWh, which gives 630–702 kt) move them by only a few per cent (Appendix B4). Each year Australia takes to change the law, license and build costs 0.19–1.50 Mt per unit to 2050 (§8.1).

**Two caveats.**
- The grid factors count combustion only, while ours is a life-cycle value, so displacement is slightly understated.
- Liddell closed in 2023 (Australian Energy Regulator, 2021) [TO VERIFY closure date]. An SMR there would reuse the site and its grid connection, but it would displace the NEM mix, not Liddell.

**So an SMR's climate value depends on when it runs and what it displaces, not on today's coal share.** In Ontario the case rests on displacing marginal gas. At Liddell it rests on the NEM decarbonising slowly.

[Figure F6. CO₂e avoided by one BWRX-300 to 2050 and over its 60-year life: Darlington Unit 1 from 2030 (Ontario average trajectory; marginal, declining; marginal flat as upper bound) against Liddell from 2035 and 2040 (Step Change proxy; slow transition; frozen grid as upper bound). Inset: CO₂e lost per month of delay to one of Units 2–4, against C1's per-unit saving (1.73 kt). Data series in Tables B17 and B20. | Source: this study, scripts/displacement.py and scripts/schedule_value.py; grid factors The Atmospheric Fund (2025), Department of Climate Change, Energy, the Environment and Water (2025), Independent Electricity System Operator (2024), Australian Energy Market Operator (2024) [TO VERIFY]. | File: TODO: plot script not yet written; draw from results/displacement.md §3 and schedule_value.md §2]

### 7.3 The same money on firmed renewables

**At GenCost's 2030 costs, the money for one SMR unit would buy about 2.9 times as much energy from firmed renewables, which would avoid about 11 times more CO₂e to 2050 at Liddell.**

**Full cost.** GenCost 2023-24 gives A$230–382/MWh for an SMR in 2030, against A$89–125 for solar and wind with integration costs (Graham, Hayward and Foster, 2024, as reported) [TO VERIFY: GenCost table/year]. At the midpoints, the same spend buys **2.9×** the energy (Figure F7). Suppose the renewables start in 2028 [assumption] and the SMR in 2040, on the slower trajectory. The renewables then avoid **10.9×** more CO₂e to 2050, and still 5.7× more in the worst case we tested for them (SMR A$230 against renewables A$153 [assumption]).

**Alternative reading.** We read A$387–641 as GenCost's 2023 value. If it is the 2030 value instead, the ratios are 5.0× and 19.1× (9.3–45.8× across cases). The conclusion holds either way. GenCost 2025-26 still ranks SMRs as the highest-cost option (Graham and Hayward, 2026) [TODO: its SMR and firmed-renewables values].

**Capital cost alone.** Darlington's C$20.9 bn (Ontario Power Generation, 2025) is about A$23.4 bn (Reserve Bank of Australia, 2025) [TO VERIFY]. At 7% over 30 years that capital alone costs A$199/MWh. That is already enough to buy 2.0–2.9× the energy from renewables at about A$102/MWh (Graham, Hayward and Foster, 2025) [TO VERIFY].

**Check against our own costing.** Our full Darlington cost of A$221/MWh at 7% real sits just below GenCost's 2030 range, plausibly because four units share infrastructure. It matches OPG's reported C$149/MWh at a 4.9% discount rate (§8.2).

**Why renewables come out ahead.** They are cheaper per MWh and start about a decade earlier. Two limits apply: that much new renewable output would itself shift the grid trajectory, and integration costs rise beyond the renewable shares GenCost models. The Ontario rows use Australian costs and are indicative only (Appendix B6). **On carbon per dollar, an SMR at Liddell loses.** Its case has to rest on firm supply, land use, system security and a hedge against renewables or transmission falling behind, and §9 weighs these.

[Figure F7. Same money, Liddell: firmed renewables (from 2028) against one SMR unit (from 2040, slower transition), as the ratio of energy bought and of CO₂e avoided to 2050 under four cost cases: GenCost 2023-24 2030 midpoints (SMR A$306, renewables A$107: 2.9× / 10.9×); worst case for renewables (A$230 / A$153: 1.5× / 5.7×); the alternative reading (A$514 / A$102: 5.0× / 19.1×); the lowest SMR lead tested (A$198 / A$153: 1.3× / 4.9×). Data in Table B28. | Source: this study, scripts/same_money.py; costs Graham, Hayward and Foster (2024; 2025) and Kim and Macfarlane (2026) [TO VERIFY: GenCost table/year]. | File: TODO: plot script not yet written; draw from results/same_money.md §5]

### 7.4 What this means for the initiative

C1 changes neither where an SMR is worth building nor what it displaces, and its value depends entirely on not delaying the plant. It gives §9 three inputs:
- **Environment:** "SMR + C1" differs from "SMR" by about 0.3%.
- **Economy:** C1 is worth C$0.49–0.60 m, against C$33–110 m for each month of delay.
- **Feasibility:** C1 stands or falls on schedule neutrality.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: CO₂e avoided per year, to 2050 and over the plant's life, for both sites; t CO₂e and C$ per day and per month of delay; energy and CO₂e ratios for the same money. Missing: verified inputs; F6 and F7 drawn.
- **R2.3 ("economic benefits ... appropriate to the scale of the proposal").** Produced: C1's carbon value (C$0.49–0.60 m) and break-even days sized to Darlington Units 2–4; displacement per unit and for four units (App B4). Missing: verified carbon price and OPG LCOE; Leroy's net MWe, capacity factor and dates.
- **R2.6 (logical, well justified).** Produced: one chain from C1's saving to the schedule condition; gross and net views explained; the counterfactual (same money) addressed. Missing: §9 to close the chain.
- **R2.7 (uncertainty realistically estimated).** Produced: average vs marginal factors, Ontario and NEM trajectories, start-year and floor sensitivity, the C1 saving's 90% interval carried into the break-even, both GenCost readings. Missing: AEMO/IESO series in place of constructed trajectories; 315 MWe in the sensitivity.
- **R4.3 (new, feasible connections).** Produced: schedule value against embodied carbon; the timing-aware Ontario vs Liddell comparison. Missing: a source for the value of reusing Liddell's grid connection.
- **R3.1, R3.6 (economic factors; comparison of solutions).** Produced: the same-money comparison and GenCost cross-check, handed to §8.2 and §9. Missing: GenCost 2025-26 values; the §9 MCDA.
- **RB.5, RB.6.** Produced: working in App B4–B6; our LCOE against GenCost and OPG. Missing: verification.
- **R5.1–R5.3.** Produced: leads with the schedule finding; one table and two specified figures; about 1.75 pages (hand estimate). Missing: Word page count; markers stripped at assembly.

### Remaining TODOs

1. **[TO VERIFY, P1, Victor]** GenCost 2023-24 final: is A$230–382 the 2030 SMR value and A$387–641 the 2023 value (NucNet lead)? If so, set `smr_lcoe_aud` to 306 (230–382) and `vre_firmed_lcoe_aud` to 107 (89–125) in `parameters_run1.yaml` and re-run `same_money.py`, so that all of B6 is on one basis. Also GenCost 2025-26's SMR and firmed-renewables values.
2. **[TO VERIFY, Victor]** The federal industrial carbon price path (C$95 in 2026, C$115 in 2030) on canada.ca; if confirmed, run 5 adopts it and re-runs `initiative_cost.py`.
3. **[TO VERIFY]** TAF 2025 average (73.8) and marginal (343, and its definition); NGA Factors 2025 NSW (640); CER 35; IESO 15 g/kWh by 2040; AEMO coal exit by 2038; the Liddell closure date; the RBA rate; OPG's C$149/MWh (merge `opg_oeb_lcoe_lead` from sources_run5.md into sources.md); C$20.9 bn; the 2028 Units 2–4 decision.
4. **[TODO: Leroy]** Net MWe (300 vs 315; add 315 to the displacement sensitivity), capacity factor, the Unit 1 and Units 2–4 start years (the context card has Unit 1 in service October 2030), and whether CSIRO's 2040 covers SMRs.
5. **[TODO: analyst]** Replace the constructed trajectories with the 2026 ISP Step Change and IESO outlook series; source the post-coal floor and a renewables lead time (2028 is an assumption).
6. **[TODO: plot]** Draw F6 and F7 from the results files in the deck's chart style, and use the same PNGs on slides 9 and 14.
7. **[TODO: §6, Q8]** §6's lead and finding 5 say "1.4–15" and "10–15 days"; Q2's re-run gives 9.2–14.6 days (average) and 1.3–1.4 days (marginal). Align §6 with Table T10.


Rubric coverage: R3.2, R3.4, R3.5, R3.7, R1.4 (also supports R1.3, R2.6, R2.7, R3.6, R3.8, R1.2, RB.2, R5.2, R5.3, R5.4, R5.5)

<!--
CHANGELOG
- v3, 21/10/2026 (writer, plan §7 job Q7). Applies review.md "Review of §8.1 and §8.3 (20/10)", §8.1 points 1–6 and the "cheap §8.1 fixes" list, in full:
  - Point 1 (Units 2–4 step): the Canada paragraph now says the licence covers one unit, so Units 2–4 need a further Commission authorisation with C1 reviewed inside it, labelled as our inference (route brief §3) [R3.4].
  - Point 2: "36 even with every other crossbencher" added (law_timelines.csv, senate_bloc_plus_all_other_crossbench) in the text and T7; Senate composition dated "as at 14 May 2026" in T7 [R2.7, R3.8]. The s 8 consequence is now stated: a privately owned SMR at Liddell stays an offence under NSW s 8 even after federal repeal, and only a Commonwealth operator might fit s 8(3) [R3.5, R3.2]. ARPANS s 13 cited (factcheck A7).
  - Point 3: REGDOC-3.5.1 benchmark (29 vs 32 months; ltc_vs_cnsc_expected_months = −2.9) added [R3.8, R1.3]. NEDO-33926 / draft AISC N690 named as the governing infill specification, not CSA N287; the unknown cement-type limit (§6.2.1) is stated as C1's real licensing risk [R3.4, R2.6].
  - Point 4: the 18–24-month critical path (route brief §6, labelled our planning assumption) and the start-in-2027 condition added; schedule-neutral is now a tested condition, using §6.3's 1.4–15 days of delay that cancel one unit's LC3 saving (same figures as §6 finding 5). Coalition 2035 vs CSIRO 2040 set side by side (R1.3). ANNPSR precedent added, in the new T7 regulator row [R3.7].
  - Point 5 (T7): placeholder line deleted; caption and source line moved above the table in style-guide form. New row "Regulator for a private power reactor" (ARPANSA's reach, routes A–C, IAEA, ANNPSR) and a closing row "Earliest legal start" giving the table's conclusion. Senate arithmetic moved into T7 to hold the page budget. The 17.9-year EA interval moved into T7's Darlington column.
  - Point 6 / plan Q7: the "Note for §9" is cut to a pointer, since Appendix B3 already holds the scored routes and weight test. §9 (Q14) does not exist yet, so the pointer stays until §9 cites B3; delete at assembly (Q19).
  - Factcheck A9: the High Court risk is now attributed to Partlett as quoted, alongside Constitution s 109.
  - Not addressable from here (human checks or other jobs; [TO VERIFY] markers kept): A1 residual (OEB filing), A5, A8 (Coalition release), A16, A18, A19, A22, A24, A26 (Constitution entry, Q3).
- v2.1, 20/10/2026 (writer). Appendix B pointers now read "Appendix B1" and "Appendix B3". No body text changed.
- v2, 20/10/2026 (writer). Revised against factcheck.md section A (A1–A26) and blocking items 5 and 6.
- v1, 20/10/2026 (writer). First draft from the law brief, the route-to-practice C1 brief and law_timelines.csv.
- Presentation items covered: R5.1 (each paragraph leads with its point and ends on what it means for C1 or Liddell); R5.2 (Table T7, captioned above and sourced, now ending on its conclusion); R5.3 (budget held by moving detail into T7); R5.4 (Harvard; one CNSC author form); R5.5 (Australian English). Departure from the writer brief's `[Table N: … | Source: …]` marker: the review asked for the placeholder to be deleted, because the table itself exists.
- Word count of the body text (excluding Table T7, headings, notes and [TO VERIFY]/[TODO] markers): about 310 words without in-text citations, about 0.6 page at about 500 words a page, against a 0.6-page budget. The Senate detail, the regulator routes, ANNPSR and the 17.9-year interval sit in T7, which does not count. If assembly needs more room, the CSIRO/Coalition clause can go, since T7's last row repeats it.
-->

## 8.1 Law, regulation and licensing

Law is where Darlington and Liddell differ most. At Darlington, C1 needs a qualified infill mix, accepted as a design change before Units 2–4 are approved to proceed, a milestone expected in 2028 (American Nuclear Society, 2026) [TO VERIFY]. At Liddell, three laws and the site owner stand in the way, and on current party positions none of the laws will be repealed in this Parliament (Table T7).

**Australia.** Federal repeal fails in the Senate whatever the crossbench does: 36 votes at most, against 39 needed (Table T7; Appendix B1). The Coalition's pledge to "repeal all legislative prohibitions" therefore cannot pass unless Labor or the Greens change position (ABC News, 2026; Liberal Party of Australia, 2026) [TO VERIFY]. Repeal would not be enough either. ARPANSA, the federal radiation regulator, licenses only Commonwealth-controlled bodies (ARPANS Act s 13; ARPANSA, n.d.) [TO VERIFY], so a privately owned SMR at Liddell would remain a criminal offence under NSW s 8. Only a Commonwealth-owned operator might fit the s 8(3) exemption that covers ANSTO [TO VERIFY: whether it extends to a power reactor].

**Canada.** Even at a licensed site, the licence to construct one BWRX-300 took about 29 months, 3 months under the CNSC's expected 32 (Canadian Nuclear Safety Commission [CNSC], 2022; 2025; 2026a) [TO VERIFY]. It covers one unit, so Units 2–4 need a further Commission authorisation, and C1 would be reviewed inside it (our inference) [TO VERIFY with the CNSC]. The cement standard already allows calcined-clay blends with up to 15% limestone (CSA Group, 2023; Hooton, 2023) [TO VERIFY]. The infill, though, is governed by GE-Hitachi's topical report NEDO-33926 (self-consolidating concrete, strength per draft AISC N690, not CSA N287), which the CNSC and US NRC jointly reviewed and found acceptable (GE-Hitachi Nuclear Energy, 2024; US Nuclear Regulatory Commission and CNSC, 2025) [TO VERIFY]. Whether it limits cement type is not yet known [TO VERIFY: NEDO-33926 §6.2.1], and we found no nuclear precedent for calcined-clay infill: that is C1's real licensing risk.

**Translation to practice.** Mix development, a full-scale mock-up and design-change acceptance take about 18–24 months (our assumption), so qualification must start in 2027, during Unit 1 construction. It must stay off the critical path, because a delay of 1.4–15 days to one of Units 2–4 cancels that unit's LC3 saving (§6.3; §7); slag (S1) is the fallback (§8.6). An Australian SMR has no legal start date, so §7 treats even CSIRO's earliest date, 2040 (Graham, Hayward and Foster, 2024) [TO VERIFY: covers SMRs?], as optimistic, let alone the Coalition's 2024 target of 2035 (ABC News, 2024) [TODO: source needed: replace with the Coalition's 19 June 2024 release].

*Table T7. Legal barriers to an SMR at Liddell, what would remove each, and the Darlington equivalent.*
*Source: legislation as named; ARPANSA (n.d.); CNSC (2021; 2022; 2025; 2026a); Government of Ontario (2025); Ontario Power Generation (2025); Parliament of Australia (2026); Parliament of New South Wales (2025–26; 2026); Minister for Defence (2025); Newcastle Herald (2024); Senate arithmetic and licensing durations in Appendix B1; routes A–C scored in Appendix B3.*

| Barrier | Liddell (NSW) | What removes it; who holds the veto | Status, October 2026 | Darlington (Ontario) |
|---|---|---|---|---|
| Federal environmental approval | *Environment Protection and Biodiversity Conservation Act 1999* (Cth) s 140A (also ss 37J, 146M): the Minister "must not approve" a nuclear power plant [TO VERIFY] | Amendment by the Commonwealth Parliament. Senate (as at 14 May 2026; all 76 voting): 39 votes needed; Coalition, One Nation and Babet 32 (our assumption that they vote together); 36 with every other crossbencher; Labor and the Greens, 40, opposed (Parliament of Australia, 2026; Bowen, 2025; Australian Greens, 2025) [TO VERIFY] | In force. Whether the 2025 EPBC reforms changed s 140A has not been checked (Norton Rose Fulbright, 2025) [TO VERIFY] | Environmental assessment from May 2007; site licence 2012, renewed to 2031; 17.9 years elapsed (not continuous review) to the licence to construct (CNSC, 2021; 2026a) [TO VERIFY] |
| Federal radiation licensing | *Australian Radiation Protection and Nuclear Safety Act 1998* (Cth) s 10: the CEO "must not issue a licence" for one [TO VERIFY] | Repeal of s 10. Senate as above | In force. The committee recommended that the 2022 repeal bill not be passed (Senate Environment and Communications Legislation Committee, 2023) [TO VERIFY]; the bill lapsed at prorogation [TODO: source needed: the bill's ParlInfo page] | CNSC licence to construct one unit: about 29 months (October 2022 to 4 April 2025) against the CNSC's expected 32 months; valid to 31 March 2035 (CNSC, 2022; 2025; 2026a) [TO VERIFY: 32 months is from an ambiguous extract] |
| Regulator for a private power reactor | None. ARPANSA licenses only Commonwealth-controlled bodies (ARPANS Act s 13; ARPANSA, n.d.) [TO VERIFY]; NSW has no nuclear regulator | One of three routes (Appendix B3): a Commonwealth-owned plant under ARPANSA (the Coalition's 2024 model; ABC News, 2024 [TODO: replace with the Coalition's release]); a federal regulator for private operators; or a NSW regulator. An independent regulator is needed early in the programme (International Atomic Energy Agency, 2015) [TO VERIFY edition] | No such regulator. Precedent: the naval nuclear regulator (ANNPSR) began operating on 1 November 2025, about two years after its bill, but covers submarines only (Minister for Defence, 2025; Parliamentary Library, 2023) [TO VERIFY: bill introduction date] | The CNSC is an established regulator. Units 2–4 need a further Commission authorisation (our inference) [TO VERIFY] |
| State ban | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8: building or operating a nuclear reactor is an offence, except for the Commonwealth's AAEC successors (ANSTO) and the other s 8(3) exceptions; s 9: other Acts do not authorise a state authority to build or approve one [TO VERIFY] | NSW repeal, or a Commonwealth override under Constitution s 109 [TODO: from Q3: Constitution entry in sources.md], which Partlett warns could face a High Court challenge (Canberra Times, 2025) [TO VERIFY: date] | The repeal bill passed the Legislative Council on 6 May 2026, has stalled in the Assembly, and lapses on 28 November 2026 (Parliament of New South Wales, 2025–26; 2026) [TO VERIFY] | Ontario approved construction of Unit 1 on 8 May 2025; C$20.9 bn is the budget for all four units (Government of Ontario, 2025; Ontario Power Generation, 2025) [TO VERIFY] |
| Site | AGL owns Liddell, has ruled out nuclear there, and has a battery project on the site (Newcastle Herald, 2024) [TO VERIFY: battery status, October 2026; primary needed] | AGL's consent, or compulsory acquisition by the Commonwealth | AGL opposed | OPG holds the site licence (CNSC, 2021) [TO VERIFY] |
| **Earliest legal start** | **None in this Parliament.** Coalition 2024 target: 2035 (SMR); CSIRO: 2040 at the earliest (ABC News, 2024; Graham, Hayward and Foster, 2024) [TO VERIFY] | Every row above, each with a different veto holder: the Senate, the NSW Assembly, AGL | No row is resolved | Unit 1 licensed April 2025; approval to progress Units 2–4 expected in 2028 (CNSC, 2025; American Nuclear Society, 2026) [TO VERIFY] |

---

### Note for §9 (not report text; delete at assembly, Q19, once §9 cites Appendix B3)

The three Australian licensing routes (A Commonwealth-owned under ARPANSA; B federal law for private operators with a s 109 override; C state repeal plus a state or joint regulator) are scored, labelled as our qualitative judgement, with the weight test, in Appendix B3 (Tables B13–B14). §9's MCDA should cite B3 for its legal-feasibility criterion. B3's route A citation (ABC News, 2024) still needs replacing with the Coalition's 19 June 2024 release (factcheck A8).

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.2 (political).**
  - Produced: the three Australian bans, the regulator gap and the site owner; Senate arithmetic that holds whatever the crossbench does (36 < 39), dated; party positions; the consequence of NSW s 8 for a private plant, which explains why the 2024 model was Commonwealth ownership.
  - Missing: no source is verified; no 2026 Labor statement; One Nation's and Babet's voting intent is still an assumption (no longer load-bearing, because of the 36).
- **R3.4 (regulation and licensing timelines).**
  - Produced: 29 months against the CNSC's 32-month norm; 17.9 years elapsed; the Units 2–4 authorisation step; the governing infill code (NEDO-33926 / AISC N690); the 18–24-month qualification path.
  - Missing: a sourced Units 2–4 review time; the approval type for 2028 (OEB filing D2-4-1 unopened); NEDO-33926 §6.2.1 cement-type limits.
- **R3.5 (translation to practice).**
  - Produced: for C1, qualification must start in 2027 and stay off the critical path (1.4–15 days of delay cancel a unit's saving); for Liddell, no legal start date.
  - Missing: nothing structural.
- **R3.7 (non-technical solutions).**
  - Produced: mock-up qualification during Unit 1 with the S1 fallback; the three regulator routes with the ANNPSR precedent and the IAEA sequencing.
  - Missing: the lever comparison (L1–L5) belongs in §8.6 (Q10).
- **R1.3 (supporting).**
  - Produced: Coalition 2035 vs CSIRO 2040; OPG's 29 months against the CNSC norm.
  - Missing: the Coalition's own release as the source of 2035.
- **R1.4 (primary sources).**
  - Produced: the Acts (now including ARPANS s 13), ARPANSA, CNSC (including REGDOC-3.5.1), APH, the NSW Parliament, the Liberal Party page, the GEH topical report, the joint NRC–CNSC report, the Defence Minister's ANNPSR release.
  - Missing: none opened. ANS (2028 milestone), ABC (2024; 2026), the Canberra Times and the Newcastle Herald still carry claims.
- **R3.6 and R3.8 (supporting).**
  - Produced: route scores live in Appendix B3; the text now carries three quantified tests (36 < 39; 29 vs 32 months; 18–24 months vs a 2028 window).
  - Missing: the §9 MCDA that uses B3.
- **R5.2–R5.5.**
  - Produced: T7 captioned above in style-guide form, placeholder removed, closing "Earliest legal start" row; budget held at about 0.6 page.
  - Missing: the Constitution entry in sources.md; reference disambiguation (TODO 9); final table number.

### Remaining TODOs

1. **[TO VERIFY, P1]** Open the current compilations of EPBC Act s 140A (and ss 37J, 146M) and ARPANS Act ss 10 and 13. Quote the words exactly, and check whether the *Environment Protection Reform Act 2025* changed them.
2. **[TO VERIFY, P1]** NSW Act ss 8–9: the exact s 8(3) exceptions, the s 9 wording, and whether s 8(3) could cover a Commonwealth-owned power reactor (a legal question: flag it, don't answer it).
3. **[TO VERIFY]** Senate composition after 14 May 2026; the NSW repeal bill's status (latest Assembly notice paper).
4. **[TODO: source needed]** Primary replacements for news sources: AGL's statement and battery status (ASX release); the Coalition's 19 June 2024 release (2035 target; route A in T7 and B3); Bowen's statement date; the lapse of the 2022 bill (ParlInfo); Partlett's quote date.
5. **[TODO: from Q3]** The *Commonwealth of Australia Constitution Act* (s 109) entry in sources.md.
6. **[TO VERIFY]** Whether CSIRO's "2040 at the earliest" covers SMRs (GenCost 2023-24); quote it; decide the GenCost edition.
7. **[TO VERIFY]** IAEA NG-G-3.1: edition and year, and where it places the regulator.
8. **[TO VERIFY, P1]** REGDOC-3.5.1: the year of version 2.1 and whether 32 months is the Class IA licence-to-construct figure (the extract also showed 24). If it is 24, the sentence becomes "5 months slower than".
9. **[TO VERIFY, P1 for C1]** NEDO-33926 Rev. 2 §6.2.1 "Concrete Infill": any cement-type, SCM or limestone limits.
10. **[TO VERIFY]** The Units 2–4 step: amendment or new licence, and the 2028 approval type. Replace ANS with OPG's OEB filing (OPG_OEB_EB-2025-0297_D2-4-1) once opened.
11. **[TO VERIFY]** ANNPSR bill introduction date (Parliamentary Library, 2023, Bills Digest No. 32) to confirm "about two years".
12. **[TODO: references, Q16]** Disambiguate CNSC 2026a (Darlington New Nuclear Project page) and 2026b; CNSC 2022 = REGDOC-3.5.1 (year TO VERIFY); Parliament of New South Wales 2025–26 needs a single Harvard year with a suffix; Ontario Power Generation 2025 = OPG_2025_Q1. Set the final table number in place of T7.
13. **[Assembly, Q19]** Delete the "Note for §9" once §9 cites Appendix B3.


Rubric coverage: R3.1, R3.5, R3.6, R3.7, R3.8, R2.3, RB.6, R1.3 (also supports R2.7, R5.1, R5.2, R5.4)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, plan §7 job Q6). First draft from briefs/economics-and-finance.md, results/lcoe.md, initiative_cost.md, same_money.md, schedule_value.md §7. Defaults per context card: GenCost 2030 SMR A$230–382, ratio 2.9× with 5.0× stated as the alternative [TO VERIFY: GenCost table/year]; carbon price C$95 (2026) / C$115 (2030) [TO VERIFY].
- Addresses review.md audit §2 (R3 "comprehensive … economic"; "evaluation and comparison of solutions") and factcheck S33 (current GenCost edition named, and why 2023-24 values are used), S34 (NuScale from SEC/DOE keys, dollar years, net of IRA, Idaho), S35 (CGF/BOF and CIB, not WNN). Ministerial-release GenCost 2024-25 values left out (sources_run5: never cite it for the number).
- Presentation: leads with the point; T10 and T11 captioned above with source lines; Harvard. Body about 560 words without citations (about 1.1 page with them) against 0.85: cut candidates are the China sentence and the vendor clause in T10.
-->

## 8.2 Economics, finance and market barriers

An SMR's cost is mostly capital, so whoever finances it sets its price and decides who can build one at all. C1 is the opposite case: it costs almost nothing, but no one is paid for the carbon it saves.

**Cost.** Darlington's C$20.9 bn budget for four 300 MWe units (Ontario Power Generation, 2025) [TO VERIFY] gives a levelised cost of electricity (LCOE: the constant price that repays every cost over the plant's life) of C$198/MWh at a 7% real discount rate, and C$112–280/MWh between 3% and 10% (Table T10). Capital is 65–86% of it, so finance terms matter as much as engineering. OPG's own C$149/MWh implies a 4.9% rate, the cost of capital of a regulated Crown utility, which no merchant developer could match. Our 7% value, A$221/MWh, sits just below GenCost's 2030 SMR range of A$230–382 (Graham, Hayward and Foster, 2024) [TO VERIFY: GenCost table/year], plausibly because Darlington's four units share infrastructure while GenCost prices one Australian unit [TO VERIFY]. The agreement is not independent, because GenCost's current edition bases its SMR capital cost on Darlington itself (Graham and Hayward, 2026) [TO VERIFY]. On either reading of GenCost, firmed renewables are cheaper: in 2030 an SMR costs about 2.9 times as much per MWh, or 5.0 times if A$387–641, the range we first used, is GenCost's 2030 value rather than its 2023 one (§7).

**Risk and finance.** NuScale's project in Idaho shows what happens when buyers carry the overrun risk: its price rose about 35% in real terms even after federal tax credits, the Utah municipal utilities meant to buy the power did not subscribe, and it was cancelled in 2023 (Table T10). Darlington avoids this with a single Crown owner and a regulated rate base. Public and First Nations finance covers about 22% of the budget, and Ontario ratepayers the rest (§8.5). The federal and provincial equity comes in two tranches, the second released for Units 2–4 "once project milestones are met" (Canada Growth Fund and Building Ontario Fund, 2025) [TO VERIFY]. That condition is C1's main financial lever.

**Barriers to entry.** About C$17,400/kW is at risk for years before any revenue. Equity markets value US developers on hoped-for orders (NuScale at 168 times its revenue), but first plants are financed by states and rate bases: the US Department of Energy's US$800 m went to two designs, one of them the BWRX-300 (US Department of Energy, 2025) [TO VERIFY], out of about 70 in development worldwide (International Atomic Energy Agency, 2024) [TO VERIFY]. China removes the financing step: its State Council approves batches of reactors for state-owned builders (Caixin Global, 2026) [TO VERIFY: State Council or NDRC primary]. Australia has neither route. Even if its bans went (§8.1), Liddell belongs to AGL, a private company (Newcastle Herald, 2024) [TO VERIFY], so an SMR there would need Commonwealth ownership or underwriting, with taxpayers carrying the cost risk (our inference).

**C1.** LC3 saves 5,190 t CO₂e across Units 2–4, or 0.132 t per m³ of target concrete (§6). At the federal industrial carbon price, C$95/t in 2026 rising to C$115/t in 2030 (Environment and Climate Change Canada, 2026) [TO VERIFY], that saving is worth C$0.49–0.60 m. It justifies an LC3 price premium of up to about C$12.6–15/m³, or 5–7% of the price of commodity concrete (Appendix B) [TO VERIFY: C$15 to be regenerated by `initiative_cost.py` at C$115]. The target concrete costs about C$9 m in total, 0.07% of the Units 2–4 capital, so money is not the barrier. Two other things are. No one captures the carbon value, because construction materials appear to sit outside Ontario's industrial carbon pricing [TO VERIFY]. And qualification, not concrete, sets the abatement cost: a C$1 m qualification programme alone adds about C$190/t, above any carbon price on the path, while one day of delay to Units 2–4 costs C$1.8–2.9 m, more than C1's whole carbon value.

**Solutions compared.** Of the four responses in Table T11, public funding for qualification on Unit 1 mock-ups (C) removes both the schedule risk and the cost that dominates the abatement cost. An embodied-carbon condition on the Units 2–4 equity tranche (A) then prices the saving at no cash cost. We recommend C plus A, with an OPG contract clause (B) as the fallback; §8.6 sequences them. For Liddell, cost is the second barrier after law: no private owner could finance a first SMR without a state balance sheet behind it.

*Table T10. Cost evidence for an SMR: our Darlington estimate against published values.*
*Source: our calculation in `03_LCA_Calculations/scripts/lcoe.py` (Appendix B) from Ontario Power Generation (2025) and Rao, Kaffine and Hodge (2026); Ontario Power Generation (2026b); Graham, Hayward and Foster (2024); Graham and Hayward (2026); NuScale Power Corporation (2023; 2026); NuScale Power Corporation and Utah Associated Municipal Power Systems (2023); Schlissel (2023); Steigerwald et al. (2023). All inputs [TO VERIFY].*

| Measure | Value | What it shows |
|---|---|---|
| Our Darlington LCOE, real, 60-year life, capacity factor 0.90 | C$112 / 151 / **198** / 280 per MWh at 3 / 5 / 7 / 10% (A$125 / 169 / **221** / 313) | Capital is 65–86% of the cost, so finance terms move it 2.5-fold |
| Same, with a NuScale-sized capital overrun (×1.75), 7% | C$317/MWh | Overrun is the largest single input, ahead of the discount rate |
| OPG's reported four-unit LCOE | C$149/MWh (2024 dollars); our model matches it at 4.9% real | A regulated Crown utility's cost of capital |
| GenCost 2023-24, 2030: SMR / large nuclear / solar and wind with integration costs | A$230–382 / 141–233 / 89–125 per MWh [TO VERIFY: table and year] | Our A$221 sits just below the SMR range |
| GenCost 2025-26 (current edition) | SMRs still the highest cost; capital based on Darlington; range [TODO: from the 2025-26 final] | Not independent of our estimate |
| SMR ÷ firmed renewables, 2030 | About 2.9× (1.8–4.3×); 5.0× if A$387–641 is the 2030 range | Renewables are cheaper on either reading (§7) |
| Capital cost: vendor-advertised BWRX-300 vs Darlington | US$2,250/kW vs about US$12,600/kW [TO VERIFY: preprint; dollar years differ] | Vendor figures are about a fifth of a real budget; industry estimates run low (Steigerwald et al., 2023) |
| NuScale Carbon Free Power Project, Idaho, 2020 → 2023 | Price US$58/MWh (2020 dollars) → US$89/MWh (July 2022 dollars), +35% real, after about US$30/MWh of tax credits; cost US$5.3 bn → 9.24 bn (×1.74); cancelled November 2023 for lack of subscribers | When buyers carry overrun risk, they leave |
| NuScale market value vs revenue, 2025 | US$5.3 bn public float vs US$31.5 m revenue (168×) | Equity prices future orders; it does not finance first plants |

*Table T11. Non-technical responses to C1's economics, compared.*
*Source: our evaluation from Canada Growth Fund and Building Ontario Fund (2025); Treasury Board of Canada Secretariat (2022); break-even and abatement costs from `initiative_cost.py` and `schedule_value.py` (Appendix B).*

| Option | Who pays | What it fixes | Weakness | Verdict |
|---|---|---|---|---|
| A. Embodied-carbon condition on the Units 2–4 equity tranche | The funds; no cash cost | Prices a saving that no market pays for | Needs the funds' agreement before the tranche terms (about 2028) | Recommended, second step |
| B. OPG contract clause capping concrete emissions, modelled on the federal Standard on Embodied Carbon in Construction | OPG, so ratepayers (up to the break-even C$12.6–15/m³) | Makes low-clinker concrete the default | The standard does not bind OPG (our inference) [TO VERIFY]; self-consolidating infill could count as a "specialised" mix allowed 130% of baseline | Fallback |
| C. Public research funding for qualification on Unit 1 mock-ups | Federal or Ontario research budget (C$1–3 m, our assumption) | Removes the schedule risk, the binding constraint, and the cost that dominates C$/t | No sourced qualification cost [TODO: source needed] | Recommended, first step |
| D. Do nothing | — | — | Forgoes 5,190 t CO₂e at near-zero cost | Rejected |

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.1 (economic: LCOE, capital cost risk, GenCost, NuScale/UAMPS, financing, barriers to entry).** Produced: own LCOE at four discount rates with the overrun case; OPG and GenCost comparison; NuScale/UAMPS with dollar years and subsidies; Darlington's finance structure; barriers to entry (capital at risk, valuations, state-financed first plants, China, Australia). Missing: GenCost 2025-26 SMR range; every primary opened.
- **R2.3 and RB.6 (economic benefit sized to the proposal; comparison with literature).** Produced: C1's carbon value and break-even premium for Units 2–4; LCOE against OPG and GenCost with the reasons for the gap and the circularity caveat. Missing: re-run of `initiative_cost.py` at C$115; LCOE and C1-cost working in Appendix B.
- **R3.6 and R3.7 (comparison of solutions; non-technical solutions).** Produced: T11 compares four options and recommends C + A, B as fallback. Missing: a sourced qualification cost and LC3 price premium.
- **R3.5 (translation to practice).** Produced: for C1, who pays for qualification and when; for Liddell, ownership and underwriting as the second barrier after law. Missing: nothing structural.
- **R1.3 (synthesis).** Produced: our LCOE vs OPG vs GenCost (and why GenCost is not independent); the 2023 vs 2030 GenCost reading; vendor vs Darlington capital cost. Missing: the GenCost table itself.
- **R3.8 and R5.2.** Produced: numbers throughout, two captioned tables. Missing: verification; final table numbers.

### Remaining TODOs

1. **[TO VERIFY, P1]** GenCost: open the 2023-24 final (2030 SMR row, A$230–382 vs A$387–641) and the 2025-26 final (SMR, large nuclear and firmed-renewables LCOE for 2030; WACC). If the 2025-26 values are found, replace the 2023-24 row in T10 and the ratio, and re-run `same_money.py` (plan §5 conflict).
2. **[TO VERIFY]** ECCC industrial carbon price path (C$95 in 2026, C$115 in 2030); then re-run `initiative_cost.py` with 95/115 so the C$15/m³ and 5–7% come from the script, not the plan note.
3. **[TO VERIFY, P1]** OPG's C$149/MWh on the OEB record (EB-2025-0297); C$20.9 bn and its dollar basis; CGF/BOF tranche wording; CIB C$970 m.
4. **[TO VERIFY]** NuScale DCRA amendment (US$89, July 2022 dollars), the IEEFA net-of-IRA reading, the UAMPS/NuScale termination release, NuScale and Oklo 10-K covers, DOE US$800 m release, IAEA catalogue count.
5. **[TODO: source needed]** China: a State Council or NDRC approval notice to replace Caixin Global (news); an LC3 price premium for Ontario (RMI 2024 North America scenario); the cost of a qualification programme (ask OPG or a nuclear concrete laboratory).
6. **[TO VERIFY]** Whether construction-material emissions are outside Ontario's Emissions Performance Standards (O. Reg. 241/19).
7. **[TODO: Appendix B, another writer's file]** Appendix B has no LCOE or C1-cost section yet. Add the working from `results/lcoe.md` and `results/initiative_cost.md` (Q14 or Q16), then replace "Appendix B" here with the section number.
8. **[TODO: references, Q16]** Add `sources_run5.md` entries to the reference list. Disambiguate Ontario Power Generation 2025 (= OPG_2025_Q1, as in §8.1) and 2026b (= opg_oeb_lcoe_lead; 2026a = OPG_2026_Q1, used in §8.5). Confirm GenCost 2025-26 authors and the IEEFA author (Schlissel). Set final table numbers in place of T10 and T11.


Rubric coverage: R3.2, R3.8, R2.1, R2.3, R4.3, R3.5, R3.7 (also supports R1.3, R2.6, R2.7, R3.6, R5.2, R5.3, R5.4, R5.5)

<!--
CHANGELOG
- v3, 21/10/2026 (writer, plan §7 job Q7). Applies review.md "Review of §8.1 and §8.3 (20/10)", §8.3 points 1–7, in full:
  - Point 1: "Its" → "Each stage's HHI". Threshold dependence stated in the text (on the 2010 scale only enrichment is highly concentrated) and in a new T3 "Class (2023 / 2010)" column; "a scale for supply risk, not a legal test" clause added (hhi.md §1) [R2.7, R2.6, R2.4].
  - Point 2: CRAI vs WNA Rosatom capacity put in the text as a range, with the CRAI-based share left as [TODO: from Q3] because the CRAI row is not yet in hhi.py and CRAI is not yet in sources.md [R1.3, R2.7]. Kazakh/Rosatom exposure added as a stated limitation in the T3 note (hhi.md §3.4, §5; supply brief gaps 3–4) [R3.2, R2.7].
  - Point 3: the conversion "therefore" fixed: "enrichment and fabrication by law, and conversion because no plant exists" [R2.6]; domestic conversion flagged as the one legal front-end option, for §8.6. Red Book edition and cost category named, with the 2026 disagreement in one clause (B9: the 2024 edition is used pending the team decision) [R1.3].
  - Point 4: Silex/GLE now sourced to the NRC facility page in sources.md (NRC_GLE_PLEF, added by run 4), with the 51% Silex / 49% Cameco ownership tied to Cameco as OPG's uranium and conversion supplier (OPG_2023_fuel) [R4.3]. The causal "because s 140A" stays out (factcheck B15). The five-option comparison is pointed to §8.6 (Q10 owns it).
  - Point 5 (R2.3): sized to the proposal: four units need about 196 t natural U and 138 thousand SWU a year (§6.2 / Appendix A8, placeholder plant data). The share of Urenco USA capacity and the two-reload reserve are [TODO: from Q3, hhi.md §6], which does not exist yet.
  - Point 6 (T3): placeholder line deleted; caption and source moved above the table in style-guide form; class column added. Conversion year still [TO VERIFY] (B19, human check).
  - Point 7: fabrication's few BWR suppliers stated as a limitation in the T3 note; no fabricator source exists, so it is a TODO for §11.
  - "Of the major parties, only the Coalition…" cut from the text to hold the budget; §8.1 carries party positions.
  - Not addressable from here: B2, B8 (OPG primary), B9 (team decision), B11 (Q3 merging the APH entries), B19, CRAI source and row (Q3).
- v2.1, 20/10/2026 (writer). Appendix B pointers now read "Appendix B2". No body text changed.
- v2, 20/10/2026 (writer). Revised against factcheck.md section B (B1–B19) and blocking items 2, 3, 4 and 6.
- v1, 20/10/2026 (writer). First draft from the supply-concentration brief, hhi.md and hhi_summary.csv.
- Presentation items covered: R5.1 (leads with the point; each paragraph ends on Darlington or Liddell); R5.2 (Table T3 with class column, captioned above and sourced); R5.3 (detail moved into the T3 note); R5.4 (Harvard); R5.5 (Australian English). Departure from the writer brief's `[Table N: … | Source: …]` marker: the review asked for the placeholder to be deleted, because the table itself exists.
- Word count of the body text (excluding Table T3 and its note, headings and markers): about 270 words without in-text citations, about 0.55 page at about 500 words a page, against a 0.5-page budget. When Q3's sizing numbers replace the TODO, keep them to one clause. If assembly needs the room, the Darlington fuel-chain sentence can shrink to "OPG's chain has no Russian stage (…)".
-->

## 8.3 Supply concentration and geopolitics

Every front-end fuel stage we measured (mining by country, conversion and enrichment) is concentrated. Each stage's Herfindahl–Hirschman index (HHI, the sum of squared market shares; §2) exceeds 1,800, "highly concentrated" on the 2023 US merger guidelines, which we use as a scale for supply risk, not as a legal test (US Department of Justice and Federal Trade Commission, 2023) [TO VERIFY]. On the superseded 2010 scale only enrichment is (Table T3). For Darlington this concentration is a price risk; for an Australian SMR it is a sovereign risk.

**Sanctions make it worse.** Russia holds 42.8% of 2025 enrichment capacity on WNA data, and [TODO: from Q3: Russia's share with CRAI's 26,200 thousand SWU for Rosatom, from the CRAI row in `hhi.py`] on an older CRAI table (calculated from World Nuclear Association, 2025; CRAI, 2025 [TODO: from Q3: sources.md entry]) [TO VERIFY]. Removing Russia, as US buyers must once the waivers on their import ban end in 2028 (United States Congress, 2024) [TO VERIFY], raises every HHI. Without Russia and China, enrichment is a Urenco–Orano duopoly (HHI 5,621). Mining is concentrated by country but not by company (HHI 1,118), so its risk is geopolitical rather than market power (Appendix B2).

**Darlington and Liddell compared.** OPG's fuel chain for Unit 1 has no Russian stage: Cameco uranium and conversion, enrichment by Urenco USA and Orano, and fabrication in the US (Ontario Power Generation, 2023) [TO VERIFY: primary not yet identified]. Four units would need about 196 t of natural uranium and 138 thousand separative work units (SWU) a year (§6.2; Appendix A8) [TO VERIFY: placeholder plant data], [TODO: from Q3: that demand as a share of Urenco USA capacity, and the size of a two-reload reserve, `hhi.md` §6]. Australia holds 28% of the world's identified recoverable uranium resources below USD 130/kgU in the 2024 Red Book (two tabulations of the 2026 edition give 29% and 27%), but has no conversion or enrichment (OECD NEA and IAEA, 2025; 2026; World Nuclear Association, 2026) [TO VERIFY]. An Australian SMR would therefore import enrichment and fabrication by law (EPBC s 140A; ARPANS s 10), and conversion because no plant exists (Parliamentary Library, 2024) [TO VERIFY: whether NSW law covers conversion].

**Translation to practice.** C1 does not reduce fuel risk. Contracts with allied enrichers, as OPG uses, mitigate a buyer's exposure but leave the HHI unchanged (§8.6). One further Western option links back to Darlington: laser enrichment developed by Australia's Silex Systems is being commercialised in the US by Global Laser Enrichment, owned 51% by Silex and 49% by Cameco, OPG's uranium supplier. The NRC accepted its application to re-enrich depleted-uranium tails at Paducah, Kentucky, for review in August 2025 (US Nuclear Regulatory Commission, n.d.) [TO VERIFY]. EPBC s 140A would bar such a plant in Australia (§10).

*Table T3. Herfindahl–Hirschman index (HHI) of the uranium front end, by stage, with and without Russia and China.*
*Source: calculated in `03_LCA_Calculations/scripts/hhi.py` from World Nuclear Association (2024; 2025; 2026) [TO VERIFY years]; thresholds from US Department of Justice and Federal Trade Commission (2010; 2023); working in Appendix B2.*

| Stage (measure, base year) | HHI | Class (2023 / 2010) | Russia's share | HHI without Russia | HHI without Russia and China | Australia's share | Canada's share |
|---|---:|---|---:|---:|---:|---:|---:|
| Mining (output by country, 2024) | 2,341 | High / Moderate | 4.5% | 2,546 | 2,686 | 7.6% | 23.8% |
| Conversion (capacity by company, [year TO VERIFY]) | 2,111 | High / Moderate | 20.2% | 2,674 | 3,615 | 0% | 20.2% |
| Enrichment (capacity by company, 2025) | **3,009** | **High / High** | **42.8%** | 3,599 | **5,621** | 0% | 0% |

*Note: "High" is above 1,800 on the 2023 guidelines and above 2,500 on the 2010 guidelines; "Moderate" is 1,500–2,500 (2010). Without Russia, all three stages are high on both scales. Sensitivity: enrichment 2,724–3,065 (2030 plans to 2022); mining by country 2,246–2,370 (2022–2024); conversion 2,015 with the higher ConverDyn capacity; all stay above 1,800. Mining by company is 1,118 (851–1,384; top three firms only), below the threshold. Russia's enrichment share is 42.8% on WNA capacity and [TODO: from Q3] on CRAI's. Limits: capacity is not supply; secondary supply (inventories, down-blending, re-enriched tails) is excluded; country shares ignore ownership, so Russia's 4.5% of mining understates its reach through Rosatom's stakes in Kazakh mines [TODO: source needed] and Kazakh export routes, which were not assessed; fuel fabrication, which for BWR fuel has few suppliers, was not assessed [TODO: source needed]. All inputs [TO VERIFY].*

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.2 (geopolitics, supply concentration).**
  - Produced: HHI by stage with the 2023/2010 class; Russia's share as a range (WNA, with CRAI pending); the sanctions effect; the Kazakh/Rosatom ownership limit; Australia's gap between resources and industry, with the legal and economic reasons separated.
  - Missing: verification of every input; a source for Rosatom's Kazakh stakes.
- **R3.8, R2.1 and R2.3 (quantitative, sized to the proposal).**
  - Produced: T3 with class column; Darlington's four-unit demand (196 t U, 138 thousand SWU a year).
  - Missing: that demand against Urenco USA capacity and a two-reload reserve (Q3, `hhi.md` §6); `verified: true` in `parameters_run3.yaml`; real BWRX-300 fuel data (Leroy) behind the placeholder burnup and enrichment.
- **R2.7 and R2.6 (supporting).**
  - Produced: threshold dependence in text and table; "scale, not legal test"; sensitivity ranges and limits; conversion logic corrected.
  - Missing: the CRAI row in `hhi.py`.
- **R4.3 (new connection).**
  - Produced: the Silex/GLE connection, now sourced (NRC facility page) and tied to Darlington through Cameco, OPG's supplier.
  - Missing: the NRC page is unopened (licence status October 2026, ownership wording); a Silex ASX release would strengthen it. The front-end-hotspot leg now rests on §6 (fuel front end 54–64% of our LCA) and can be linked in §10.
- **R3.5 (translation to practice).**
  - Produced: price risk for Darlington, sovereign risk for Liddell, and C1's limited reach.
  - Missing: nothing structural.
- **R3.7 and R3.6 (non-technical solutions).**
  - Produced: dual sourcing as a mitigation with its limit; domestic conversion identified as the only front-end step the federal bans don't name; GLE as an allied supply option.
  - Missing: the five-option comparison table (supply brief) belongs in §8.6 (Q10).
- **R1.3 (synthesis).**
  - Produced: Red Book 2024 vs 2026; WNA vs CRAI (pending number); country vs company mining.
  - Missing: the team's B9 decision on the edition.

### Remaining TODOs

1. **[TO VERIFY, blocking]** Open the pages in the supply brief's checklist (WNA enrichment, conversion and mining; Red Book 2024/2026; DOJ/FTC 2023 and 2010; PL 118-62; the OPG fuel-supplier release). Set `verified: true` and rerun `python3 -I 03_LCA_Calculations/scripts/hhi.py`. Update T3 if any value moves.
2. **[TODO: from Q3]** CRAI (2025) entry in `sources.md` and the CRAI row in `hhi.py`; drop Russia's CRAI-based share into the text and the T3 note.
3. **[TODO: from Q3]** `hhi.md` §6 sizing: four units' 196 t U and 138 thousand SWU a year as a share of Urenco USA capacity, and a two-reload reserve (tU and SWU). One clause in the "compared" paragraph.
4. **[TODO: team decision, B9]** Red Book edition and cost category (28% in 2024 vs 29%/27% in 2026). Keep §8.3, slide 13 and `hhi.md` identical. This draft uses the 2024 edition.
5. **[TO VERIFY]** Whether NSW law covers conversion (Parliamentary Library, 2024 says some state laws do). This decides whether domestic conversion would be legal at a NSW site (§8.6).
6. **[TO VERIFY]** NRC GLE facility page: application accepted 4 August 2025; ownership 51% Silex / 49% Cameco; licence status in October 2026. Add a Silex ASX release if it can be opened.
7. **[TODO: source needed]** Rosatom's (Uranium One) stakes in Kazakh mines; BWR fuel fabricators (GNF, Framatome, Westinghouse). If no source, keep both as limitations and repeat the fabrication one in §11.
8. **[TODO: Leroy, references]** Confirm the WNA page years and add suffixes if two share a year. Harmonise "U.S." to "US" for the NRC and DOJ/FTC entries in the reference list (Q16). Q3 merges the duplicate Parliamentary Library entries. Set the final table number in place of T3 (it clashes with plan T3/T7 numbering until Q19).
9. **[TODO: Leroy]** BWRX-300 burnup, reload enrichment, cycle length and reload fraction, to replace the placeholders behind 196 t U and 138 thousand SWU.


Rubric coverage: R3.3, R3.4, R3.5, R3.6, R3.7, R3.8, R1.3 (also supports R1.4, R4.3, R5.1, R5.2, R5.4)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, plan §7 job Q6). First draft from briefs/social-licence-stakeholders.md, pestle.md, results/social_licence.md/.csv. Route scores labelled as our (the team's) judgement.
- Addresses review.md audit §2 (R3 "comprehensive … social"; "evaluation and comparison of solutions") and §4 slide 12 / factcheck S36–S37 (Lowy and OWID from sources.md keys; Lowy 2024 stated as the latest electricity result; OWID's European-plant caveat; Markandya and Wilkinson cited). Includes the Williams Treaties C$700 m loan-to-equity and the consent-based vs top-down comparison (Q6 brief).
- Presentation: leads with the point; numbers carried by T12 and T13 (captioned above, sourced). Body about 420 words without citations (about 0.8 page with them) against 0.6: cut candidate is the Slovic sentence (the point survives in T12's last column).
-->

## 8.4 Social licence

The same reactor has a social licence at Darlington and none at Liddell. Safety data do not explain the difference; consent, benefit and trust do (Table T12).

**Perceived and actual safety.** Australian support is real but soft. In 2024, 61% supported "using nuclear power to generate electricity" (Neelam, 2024), yet 59% wanted to keep the legal ban, up from 51% a year earlier (Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub, 2025) [TO VERIFY]. The two polls do not conflict: one asks about a technology, the other about the law, so support depends on framing, and it falls 16–20 points for a plant nearby (Newspoll, 2007; Essential Research, 2019) [TO VERIFY]. The actual risk is about 820 times lower for nuclear than for coal per unit of electricity (Ritchie, 2020; Markandya and Wilkinson, 2007) [TO VERIFY], but this does not settle opinion, because nuclear sits at the extreme of the "dread" and "unknown" risk factors (Slovic, 1987) [TO VERIFY]. Its health benefit, like its carbon benefit (§7), also depends on what it displaces, and coal leaves the National Electricity Market by 2038 in AEMO's central scenario, before a Liddell SMR could run (Australian Energy Market Operator, 2024) [TO VERIFY].

**Consent: equity in Canada, failed top-down siting in Australia.** At Darlington the CNSC found the duty to consult met (Canadian Nuclear Safety Commission [CNSC], 2025) [TO VERIFY], and in June 2026 the seven Williams Treaties First Nations agreed to lend C$700 m to the project, converting to equity once all four units are complete, with the loan guaranteed half each by federal and Ontario programmes (Williams Treaties First Nations et al., 2026) [TO VERIFY]. Two Nations still contest the process (T12), so equity is a means of consent, not a substitute for it. Australia's precedent is a waste site chosen top-down and set aside by the Federal Court for apprehended bias after a ballot that excluded native title holders (*Barngarla Determination Aboriginal Corporation RNTBC v Minister for Resources* [2023] FCA 809) [TO VERIFY]. Canada's waste agency instead used volunteer siting with a separate First Nation decision and a priced hosting agreement (Nuclear Waste Management Organization [NWMO], 2024a; 2024c) [TO VERIFY]. Scored on legitimacy, legal risk, speed, public cost and fairness, consent-based routes beat top-down siting under every weighting we tested (Table T13). Not building an SMR at Liddell scores higher still, because it needs no change in law or consent.

**Translation to practice.** C1 changes no land use, emissions or waste, so it raises no new consent issue; its social value is indirect, as a lower-carbon build that OPG can report to its new First Nations and public equity partners (our inference). For Liddell, the low-regret steps can come before any repeal: a producer-funded waste body, and a two-key willingness test in which both the host community and the Traditional Owners must agree. A priced hosting agreement and First Nations equity backed by a federal loan guarantee, which Australia does not yet have [TO VERIFY], would follow, along with a skills plan coordinated with the AUKUS submarine programme (§8.6).

*Table T12. Social licence at Darlington and at Liddell.*
*Source: Neelam (2024); Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub (2025); Newspoll (2007); Essential Research (2019); Ritchie (2020); Markandya and Wilkinson (2007); Australian Energy Market Operator (2024); CNSC (2025); Williams Treaties First Nations et al. (2026); Mississaugas of Scugog Island First Nation (2023); Curve Lake First Nation (2024); Municipality of Clarington (2024); Australian Electoral Commission (2019); Barngarla [2023] FCA 809; NWMO (2024a; 2024b; 2024c; n.d.); Department of Industry, Science, Energy and Resources (2020); Power Workers' Union (2021); Conference Board of Canada (2021); Defence Connect (n.d.); Joint Standing Committee on Treaties (2024); Australian Council of Trade Unions (2024). Deaths avoided calculated in `social_licence.py` (Appendix B). All [TO VERIFY].*

| Factor | Darlington, Ontario | Liddell, NSW (hypothetical) | Effect on translation to practice |
|---|---|---|---|
| Public view | Host municipality "very supportive" | National: 61% support nuclear electricity (2024, latest), but 59% keep the ban; local support 16–20 points below national | Support is conditional; a local poll is needed before any siting |
| Deaths per TWh; deaths avoided per unit-year | Nuclear 0.03 vs gas 2.82: about 6.6 if it displaces gas (Ontario has no coal) | Coal 24.62: about 58, an upper bound because coal exits by 2038; about zero against wind or solar | Safety data favour nuclear but do not build acceptance ("dread" risk) |
| Traditional Owners and consent mechanism | Williams Treaties First Nations; duty to consult met; C$700 m loan converting to equity, guaranteed 50/50 by federal and Ontario programmes | Wonnarua people; no position found [TODO: source needed]; no process | Canada has a funded way to say yes; Australia has none |
| Residual dissent and litigation | Mississaugas of Scugog Island seek "conditions for consent"; Curve Lake says treaty rights not shown to be considered | Kimba waste ballot: 61.6% yes, below the reported 65% benchmark, Barngarla excluded (their own poll 100% no); site set aside in 2023 | Excluding Traditional Owners invalidates a ballot in court |
| Waste route | Volunteer siting from 2010: 22 communities to 1 in 14 years; Ignace vote 77%; C$170 m over 81 years to the host; C$26 bn lifecycle cost paid by producers | No disposal route even for research-reactor waste | Waste is a hard gate for Liddell |
| Workforce and unions | About 1,900 union members at the site; about 1,600 construction and 200 operating jobs per SMR (gross estimate); unions support | "No current Australian talent pool" for civil nuclear roles; 76,950-worker shortfall in four trades by 2030–31; AUKUS needs about 20,000 jobs; ACTU and ETU oppose | A civil SMR would compete with AUKUS for scarce trades |

*Table T13. Social-licence routes for an SMR at Liddell: total score (criteria scored 1–3 on legitimacy, legal risk, speed, public cost and fairness; one criterion doubled in each weighted column).*
*Source: our judgement from the evidence in T12, calculated in `social_licence.py` (Appendix B); route models from Newcastle Herald (2024b), NWMO (2024a; 2024c) and Williams Treaties First Nations et al. (2026). Scores [TO VERIFY] as their evidence is verified.*

| Route | Equal weights | Legitimacy ×2 | Speed ×2 | Fairness ×2 | Public cost ×2 |
|---|---:|---:|---:|---:|---:|
| R1. Commonwealth-led siting, with compulsory acquisition if needed (2024 Coalition model) | 7 | 8 | 9 | 8 | 9 |
| R2. Volunteer host with a willingness test that includes Traditional Owners, plus a hosting agreement (NWMO model) | 11 | 14 | 12 | 13 | **13** |
| R3. R2 plus First Nations equity with a government loan guarantee (Williams Treaties model) | 11 | 14 | 12 | **14** | 12 |
| R4. No SMR: firmed renewables at Liddell (AGL's plan) | 14 | 17 | 17 | 16 | 17 |

*Reading: consent-based routes (R2, R3) beat top-down siting (R1) by 3–6 points under every weighting, even with speed, R1's only advantage, doubled. R4 scores highest throughout, so on social licence alone the Australian SMR case is weaker than the alternative; §9 weighs this against carbon and cost.*

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.3 (social: perception vs safety, social licence, First Nations and host consent, jobs).** Produced: polls against deaths per TWh with the framing and dread explanations; health benefit by displaced source; First Nations consent at both sites, including the C$700 m loan-to-equity and residual dissent; host community; jobs. Missing: verification; a Wonnarua position; WLON's vote.
- **R3.4 (other: workforce, waste governance).** Produced: workforce and unions in both countries; NWMO vs Australia's waste record. Missing: ANSTO and university pipeline numbers.
- **R3.6 and R3.7 (comparison; non-technical solutions).** Produced: T13 scores four routes under five weightings; sequenced solutions for Liddell; C1's indirect social value. Missing: integration into the §9 MCDA.
- **R3.5 (translation to practice).** Produced: what blocks or enables C1 and a Liddell SMR, and in what order. Missing: nothing structural.
- **R1.3 (synthesis).** Produced: Lowy vs Griffith–Monash reconciled; national vs local gap; Canada vs Australia consent records. Missing: the Griffith–Monash method.
- **R3.8, R5.2.** Produced: two captioned tables; scores labelled as judgement. Missing: final table numbers.

### Remaining TODOs

1. **[TO VERIFY, P1]** Williams Treaties release (23 June 2026): amount, conversion trigger, 50/50 guarantee by CILGC and Ontario's IOFP; Barngarla [2023] FCA 809 paragraphs; NWMO selection, Ignace agreement (C$170 m, 81 years) and project costs (C$26 bn); Griffith–Monash method and wording; Slovic (1987) wording on nuclear.
2. **[TO VERIFY]** Lowy 2024 (no later electricity question); OWID 0.03 and 24.62 on the live chart; AEMO 2024 ISP coal exit by 2038 (secondary: Ark Energy); Kimba AEC sheet and the 65% benchmark in a ministerial source; MSIFN and Curve Lake CMD wording (do not quote "never consented").
3. **[TODO: source needed]** Wonnarua position on nuclear at Liddell; primaries for Defence Connect (FOI disclosure log), Newcastle Herald 2024b (Coalition release) and the ACTU campaign; whether Australia has any Indigenous loan-guarantee facility like CILGC.
4. **[TODO: Leroy or Q5]** The 2040 Liddell start assumed for the health and carbon timing.
5. **[TODO: Appendix B, another writer's file]** Add the deaths-avoided calculation and the route scoring from `results/social_licence.md` §2 and §7 to Appendix B, then give the section number here.
6. **[TODO: references, Q16]** Add `sources_run6.md` entries. Suffixes: NWMO 2024a = NWMO_2024_Selection, 2024b = NWMO_SiteProcess, 2024c = NWMO_Ignace_2024, n.d. = NWMO_ProjectCosts; Newcastle Herald 2024 (§8.1, §8.2: AGL) vs 2024b (Coalition_Liddell_2024); Clarington CMD number. Final table numbers for T12 and T13.


Rubric coverage: R3.1, R3.3, R3.5, R3.8, R5.2 (also supports R3.6, R3.7, R5.1, R5.4)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, plan §7 job Q6). First draft from briefs/social-licence-stakeholders.md §5–6, route-to-practice-c1.md §7, results/social_licence.md §4 and §6, and F8 (results/F8_stakeholder_map.png). Stance scores labelled as our (the team's) judgement.
- Addresses review.md audit §2 (R3 "comprehensive … economic, political, social") and plan §3 row 8.5 (power/interest map; who pays and who earns).
- Presentation: leads with the point; F8 and T14 captioned and sourced. Body about 210 words without citations against 0.35 page. Plan cut order: if over 20 pages, this section shrinks to F8 and T14 with one sentence.
-->

## 8.5 Stakeholders and money flows

At Darlington the actors who could stop the project support it or are neutral; at Liddell they form a stack of independent vetoes (Figure 8). We scored each actor's power, interest and stance from the evidence in §8.1–8.4. The scores are our judgement, not survey data. Weighted by power, the average stance is +1.07 at Darlington and −1.03 at Liddell, on a scale from −2 (strongly against) to +2 (strongly for). None of Darlington's seven high-power actors opposes the project. At Liddell three of the four do (the Commonwealth, NSW and AGL), and the only strong supporter, the federal Coalition, is in opposition.

Money follows the same pattern (Table T14). Ontario ratepayers fund about 78% of Darlington through OPG, while federal, provincial and First Nations finance lowers the cost of capital and spreads ownership. That model needs a publicly owned utility with a regulated rate base. Liddell has a private owner, so an SMR there would need Commonwealth ownership, as in the Coalition's 2024 model, with taxpayers carrying the cost risk (ABC News, 2024) [TODO: source needed: the Coalition's 19 June 2024 release].

For C1, the decisive actors are OPG as buyer, GE Vernova Hitachi as owner of the infill specification, and the two equity funds at the Units 2–4 tranche (§8.2). None is opposed, but none yet has a reason to act; the tranche condition supplies one (§8.6).

[Figure 8: Stakeholder power/interest maps for Darlington Units 2–4 with C1 (left) and a hypothetical BWRX-300 at Liddell (right). Numbered markers identify actors; colour shows stance from strongly for to strongly against. Positions are our judgement from the evidence in §8.1–8.4, each tied to a source key in `parameters_run6.yaml`. File: `03_LCA_Calculations/results/F8_stakeholder_map.png` | Source: our analysis (`social_licence.py`, Appendix B), from the sources cited in §8.1–8.4]

*Table T14. Who pays and who earns: the C$20.9 bn Darlington New Nuclear Project, and the Liddell alternative.*
*Source: Government of Ontario (2025); Canada Infrastructure Bank (2022); Canada Growth Fund and Building Ontario Fund (2025); Ontario Power Generation (2025b; 2026a); Williams Treaties First Nations et al. (2026); NWMO (2024c; n.d.); ABC News (2024); shares calculated in `social_licence.py` (Appendix B). Debt and equity are added only to show scale. All [TO VERIFY].*

| Flow | Who pays | Who earns | Amount (share of C$20.9 bn) |
|---|---|---|---|
| OPG's share, recovered through Ontario Energy Board-approved payment amounts | Ontario ratepayers | GE Vernova Hitachi, construction partners [TODO: names], suppliers (80% of spending claimed to go to Ontario firms) | C$16.2 bn (78%) |
| Phase 1 loan | Canada Infrastructure Bank (federal) | The project; the bank earns interest | C$0.97 bn (4.6%) |
| Equity in two tranches; the second tied to Units 2–4 milestones | Canada Growth Fund (federal) and Building Ontario Fund (Ontario) | Returns on 15% and 7.5% stakes | C$2.0 bn and C$1.0 bn (14.4%); C$0.585 bn received April 2026 |
| Loan converting to equity after all four units | Williams Treaties First Nations; federal and Ontario guarantors carry the default risk | First Nations equity returns | C$0.70 bn (3.3%) |
| Spent-fuel disposal (all Canadian used fuel) | OPG and other producers, so ratepayers, through statutory trust funds | Waste agency; host communities (Ignace: C$170 m over 81 years) | C$26 bn lifecycle (outside the C$20.9 bn) |
| **Liddell (hypothetical)** | Commonwealth taxpayers, under the 2024 Coalition model | Vendor and construction workforce; AGL, if paid for the site | Not costed (§8.2) |

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R3.1 and R3.3 (economic and social actors).** Produced: power/interest map for both sites; power-weighted stance; who pays and who earns, with shares. Missing: verification; construction-partner names; a Wonnarua position (F8 shows "unknown").
- **R3.5 (translation to practice).** Produced: the actors who decide C1, and why Liddell's ownership blocks the Ontario financing model. Missing: nothing structural.
- **R3.8 and R5.2 (analysis; figures and tables).** Produced: F8 specified and captioned; T14 with shares; scores labelled as judgement. Missing: F8's footnote still says "analyst's judgement" (should read "our judgement"); final figure and table numbers.

### Remaining TODOs

1. **[TODO: lca/policy analyst]** Change F8's footnote from "analyst's judgement" to "our judgement" and re-export (`social_licence.py`); the report caption already says "our judgement".
2. **[TO VERIFY, P1]** Williams Treaties release; CGF/BOF tranche terms; OPG Q1 2026 (C$585 m); CIB C$970 m; the 80% Ontario-spend claim; NWMO C$26 bn and the Ignace agreement.
3. **[TODO: source needed]** DNNP construction partners (OPG release "Team forms to build North America's first SMR"); the Coalition's 19 June 2024 release to replace ABC News; whether the 15% Clean Electricity ITC applies to DNNP (left out of T14 until confirmed).
4. **[TODO: Appendix B, another writer's file]** Add the stakeholder scoring and money-flow shares (`results/social_licence.md` §4, §6) to Appendix B, then give the section number here.
5. **[TODO: references, Q16]** Ontario Power Generation 2025b = OPG_OEB_EB-2025-0297_D2-4-1, 2026a = OPG_2026_Q1 (see §8.2 TODO 8); NWMO suffixes as in §8.4; final numbers for Figure 8 and T14.


Rubric coverage: RB.5, R2.2, R2.4 (also supports R2.1, R2.3, R2.5, R2.6, R2.7, R1.4, R5.2, R5.4)

<!--
CHANGELOG
- v3, 21/10/2026 (writer, for Victor). Revised against review.md "Review of §6 and Appendices A, C (21/10)", Appendix A items and §6 points 2, 4 and 6, with Victor's decision (keep C1 sharpened: LC3 target, slag fallback, schedule-neutral; no steel in the initiative):
  - A3: the 37 m / 35 m geometry and the 953 t module are cited as read (okdiario, 2026), not to OPG (L9, R1.4, R5.4).
  - A5: ENR flagged for replacement or removal with a re-run (L20); no new median computed, because the model has not been re-run.
  - A6: S0 defined as what OPG would pour anyway, with the business-as-usual consequence; S1 and S2 labelled as the C1 fallback and target binder.
  - A7: like-for-like steel working added (target-structure steel only, about 566 t), marked "[examiner estimate, TODO: script]"; whole-plant S3 row relabelled an upper bound, with the forgings and nuclear-plate caveat. Table A6 gains the like-for-like row with TODO cells.
  - A9/A10: kept as [TODO: results pending] and ready to fill (Victor's decision); the "cut if not run" rule is unchanged.
  - All [TO VERIFY] markers kept.
- v2, 21/10/2026 (writer, for Victor). Revised against factcheck.md §H: L9 (A3 says the 37 m / 35 m geometry and the 953 t module rest on a news report; [TO VERIFY] kept); L67 (A3 labels 10,350–41,400 m³ as input bounds and gives the Monte Carlo 90% interval, 15,050–36,521 m³); L65 (A3 states the rebar cap); L60 (Table A6 caption: Unit 1 forebay partly placed); L62 (A5 and table titles: construction-material factors are EN 15804 modules A1–A3; other factors are not module-based; transport is EN 15804 module A4, not Appendix A4); L5 (cement range is a regional spread); L22 (CRSI 2017 superseded); L23 (AISC is a Buy Clean California limit); L25 (US grid CO₂ only); L26 (gas heat is combustion CO₂ only); L4 (EDF shares secondary, back end by difference); L10 (arXiv source is an unrefereed preprint); L20 (Scrivener figure to confirm); L55 (A6 note: shares all mode case; the MC median applies to LC3 only); L1/L52 (screening LCA wording; no Granta run). All [TO VERIFY] markers kept.
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/lca.md` §2, §3 and §12, `lca_baseline.md`, `lca_scenarios.md`, `lca_inventory.csv`, `Accounting_corrected.csv`, `parameters_lca.yaml`, `granta_inputs.md` and `02_Research/sources_lca.md`. Cited from §6 as Appendices A3, A5, A6 and A9.
  - review.md "For Sam" items 1–4: the corrections the lca-analyst made in `Accounting_corrected.csv` are listed in A4. Sam's `Assumptions.docx` and `Accounting.xlsx` are untouched.
  - factcheck.md S17: A3 states that plant quantities are scaled from per-MWe intensities, with the forebay and basemat as the only measured structures.
  - plan §2.1 "virgin rebar trap": rebar uses an electric-arc-furnace (recycled-content) factor (A5).
  - Granta: A9 gives the set-up and the model values Granta should be compared with. **No Granta result exists; the result cells say [TODO: results pending].**
- Presentation items: R5.1 (each subsection opens with its result); R5.2 (Tables A1–A10, caption and source above each); R5.3 (prose limited to the steps; appendices do not count towards the page limit); R5.4 (Harvard, same author forms as §6); R5.5 (Australian English).
- Every input is unverified. All [TO VERIFY] markers are kept.
-->

## Appendix A. LCA inventory and calculations

This appendix gives the full working behind §6. The analysis is an **equivalent analysis built from published factors**: a screening LCA following ISO 14040/44 principles, not critically reviewed, in which a Python model multiplies quantities by emission factors. **No Granta EduPack run has been done**; the cross-check is only set up (A9) [TODO: results pending]. **No input has yet been checked against its primary source** (`status: TO VERIFY`, `assumption` or `placeholder` in `parameters_lca.yaml`), so every number here is provisional.

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
- Net efficiency η = P_net / P_th = 300 / 870 = **0.345** (870 MWt: [TODO: authors], 2025, an unrefereed preprint) [TO VERIFY].
- Conversion to the functional unit: 1 t CO₂e spread over E is 7.05 × 10⁻⁶ kg CO₂e/MWh (= g/kWh).

Inputs: P_net 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.) [placeholder; 315 MW net in an OPG filing, TO VERIFY]; CF 0.90 [placeholder, assumption shared with §7]; L 60 years (Canadian Nuclear Safety Commission, 2024) [TO VERIFY; 65 years reported elsewhere].

### A3. Material quantities per unit

**Result.** About 20,700 m³ of concrete and 9,900 t of steel per unit, of which 13,081 m³ of concrete is in the C1 target structures. **These are scaled estimates, not measured quantities**: no BWRX-300 bill of materials could be opened (searched: OPG's EIS review report NK054-REP-07730-00055-R001, TVA's Clinch River environmental report ML25118A209 and SEIS ML26035A285, GEH NEDO-33914; only front matter or summaries were visible) [TODO: Leroy].

**Whole plant.** Concrete = I_c × P_net; steel = I_s × P_net.
- Central: ESBWR intensities, I_c = 69 m³/MWe and I_s = 33 t/MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY], because the BWRX-300 is derived from the ESBWR.
- Low: GE Vernova's claim of about 50% less concrete (and, in one release, steel) per MW than the ESBWR, giving 34.5 m³/MWe and 16.5 t/MWe (GE Vernova, n.d.) [TO VERIFY; manufacturer projection].
- High: ABWR, 138 m³/MWe and 46 t/MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY], standing in for small-plant scale penalties.
- **Assumption:** in the central case the claimed halving is offset by SMR diseconomies of scale.
- **Input bounds, not a result range:** 34.5 × 300 = 10,350 m³ and 138 × 300 = 41,400 m³. The Monte Carlo 90% interval for whole-plant concrete is about **15,050–36,521 m³** (median 24,066 m³; Table C2). Quote the interval, not the bounds, as the concrete range.

**C1 target structures (geometry).** With D = 37 m (module diameter) and h = 35 m (shaft depth), as read in a news report of the Unit 1 basemat-module lift (okdiario, 2026) [TODO: sources.md entry] [TO VERIFY]. **Both dimensions, and the 953 t module mass below, come from that report, which misdescribes the module as a "reactor" and cites an OPG story we have not found** [TODO: OPG URL or NEDO-33926 dimensions]. They set 69% of the C1 target concrete.
- V_basemat = π/4 × D² × t_b = 0.7854 × 37² × 3.0 = **3,226 m³** (t_b = 3.0 m, assumption, range 2–4 m).
- V_wall = π × (D − t_w) × t_w × h = π × 35.5 × 1.5 × 35 = **5,855 m³** (t_w = 1.5 m, assumption, range 1–2 m).
- Forebay shaft = **4,000 m³** placed to date (Ontario Power Generation, 2025) [TO VERIFY]; a floor, with 6,000 m³ as the high value. Whether the forebay serves one unit or all four is [TODO: Leroy/OPG].

**Rebar.** Rebar = ρ × plant concrete = 0.15 t/m³ × 20,700 = 3,105 t (assumption; the forebay's observed 1,000 t / 4,000 m³ = 0.25 t/m³ is the high value, and DPSC modules use steel faceplates instead of most rebar). Plate, structural and equipment steel = 9,900 − 3,105 = 6,795 t, which includes the 953 t Unit 1 DPSC basemat module (okdiario, 2026) [TO VERIFY]. The rebar ratio only splits total steel between two factors, and **rebar is capped at total steel** (rebar = min(ρ × plant concrete, total steel)), so plate steel never goes negative.

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

*Table A3. Corrected construction inventory (cradle to gate, EN 15804 modules A1–A3; central case).*
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

**Result.** Every factor is a published North American or Canadian value where one was found, and an assumption otherwise. Construction-material factors are cradle-to-gate (EN 15804 modules A1–A3) [TODO: source needed: EN 15804 entry in sources.md]. The grid, natural-gas, mining and EDF factors are not module-based. The impact category is climate change, characterised as GWP100 (IPCC AR5 where stated); the US grid factors are CO₂ only.

*Table A4. Emission and energy factors used.*
*Source: `parameters_lca.yaml`; references as listed. All [TO VERIFY] unless marked as an assumption.*

| Factor | Central | Range | Unit | Reference |
|---|---|---|---|---|
| General-use (GU) cement | 854 | 796–898 (regional spread, West–East, not an uncertainty range) | kg CO₂e/t | Cement Association of Canada (2022), Central region (which region covers Ontario is [TO VERIFY]); to be replaced by the St Marys Bowmanville EPD (NRMCA, 2021) |
| Slag cement | 146.6 | 93.4–146.6 | kg CO₂e/t | Slag Cement Association (n.d.); low = Lafarge NewCem plant EPD |
| LC3 binder cut vs GU | 37% | 30–43% | — | Median of five estimates (below) |
| Non-binder share of concrete (aggregates, water, admixtures, batching) | 30 | 15–60 | kg CO₂e/m³ | Assumption |
| Binder content: DPSC self-consolidating infill | 450 | 400–550 | kg/m³ | EFNARC (2005) gives 360–500 kg/m³ powder for SCC [TO VERIFY]; 450 and 550 are assumptions for a cement-rich nuclear mix |
| Binder content: other structural concrete | 350 | 300–420 | kg/m³ | Assumption |
| Clinker factor: GU; LC3 | 0.92; 0.50 | 0.90–0.95; 0.50–0.55 | t/t binder | Assumption; Scrivener et al. (2018) |
| Rebar (electric-arc furnace, fabricated) | 0.97 | 0.89–1.99 | t CO₂e/t | Concrete Reinforcing Steel Institute (2017) [superseded by the CRSI 2022 EPD; replace the value, TO VERIFY]; low = American Institute of Steel Construction (2022) limit; high = world average (Circular Ecology, 2019, read via a secondary) |
| Plate, structural and equipment steel | 1.73 | 1.22–2.50 | t CO₂e/t | American Institute of Steel Construction (2022): a Buy Clean California fabricated-plate GWP limit (a policy ceiling, not an industry average), used as a proxy; high is an assumption for forged and machined equipment |
| Heavy truck | 0.10 | 0.06–0.15 | kg CO₂e/t-km | Assumption |
| Mining and milling | 42 | 24–81 | kg CO₂e/kg U₃O₈ | Parker, McNaughton and Sparrow (2016), Saskatchewan, production-weighted |
| Conversion: electricity; heat | 11.8; 26 | 10.3–16.9; 26–665 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Centrifuge enrichment | 50 | 40–100 | kWh/SWU | Gibon and Hahn Menacho (2023) |
| Fuel fabrication | 36 | 36–50 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Grid: conversion (Ontario) | 0.0738 | 0.035–0.343 | kg CO₂e/kWh | The Atmospheric Fund (2025); low = Canada Energy Regulator (n.d.) |
| Grid: enrichment and fabrication (USA) | 0.373 | 0.05–0.637 (enrichment); 0.20–0.637 (fabrication) | kg CO₂/kWh (CO₂ only, used as CO₂e) | US EPA (2024); lows are assumptions [TODO: eGRID CO₂e values] |
| Natural-gas heat | 0.202 | — | kg CO₂/kWh | IPCC (2006): 56,100 kg/TJ × 3.6 × 10⁻⁶ TJ/kWh; combustion only, upstream gas supply cut off (§6.1) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 | 0.17–0.67; 0.06–0.33; 0.28–1.11 | g CO₂e/kWh | EDF R&D (2024): 9%, 3% and 15% of 3.7 g/kWh, shares as reported by secondary sources and the back end by difference [TO VERIFY in the paper]; ranges are assumptions for transfer to one BWRX-300 |

**The LC3 cut (37%)** is the median of five published estimates of LC3's binder emissions against Portland cement: 30% (ENR, 2018); 34%, 700 → 465 kg CO₂/t (Development Alternatives, n.d.); 37%, 856 → 543 kg CO₂/t (LC3 Project, 2015); about 40% (Scrivener et al., 2018, as summarised in the EPFL abstract; to confirm in the paper text); 43%, 903.5 → 513.5 kg CO₂e/t (LACCEI, 2026) [TODO: authors]. All five are [TO VERIFY]. ENR is trade press: replace it with a peer-reviewed LCA, or drop it and re-take the median of the other four, then re-run the scripts [TODO: analyst; L20] (R1.4). The estimates come from Indian, Cuban and Latin American settings; an Ontario LC3 calcined with natural gas is untested.

**Check on the per-m³ model.** At 350 kg/m³ the model gives 328.9 kg CO₂e/m³ for S0 concrete, close to the Ontario industry baseline of 334 kg CO₂e/m³ for 35 MPa concrete and below the 417 kg CO₂e/m³ industry benchmark mix (Canadian Ready-Mixed Concrete Association, 2022) [TO VERIFY].

### A6. Concrete and the C1 scenarios

**Result.** LC3 (the C1 target binder) cuts emissions from the target concrete by 1,734 t per unit (34%) and avoids 2,304 t of clinker; a slag blend (the C1 fallback) cuts them by 1,552 t (31%).

**Baseline S0.** S0 is the concrete OPG would pour anyway, without C1. It is modelled as general-use (GU) Portland cement with no supplementary cementitious materials, because neither OPG's mix nor any cement-type limit in the governing specification (GE-Hitachi Nuclear Energy, 2024) has been seen [TO VERIFY]. If OPG's mix already contains slag, S1 is business as usual: every saving in Tables A5 and A6 is then overstated, and LC3's increment is the LC3-minus-slag difference, 181 t per unit in the mode case and 97 t at the Monte Carlo median (90% interval −343 to +574 t; Table C2), which is within the noise.

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
| DPSC reactor-building infill | S1 slag (fallback) | 9,081 | 450 | 3,762 | 2,606 | 1,156 (127.3) | 1,504 |
| DPSC reactor-building infill | S2 LC3 (target) | 9,081 | 450 | 3,762 | 2,471 | 1,291 (142.2) | 1,716 |
| Forebay shaft | S1 slag (fallback) | 4,000 | 350 | 1,316 | 919 | 396 (99.0) | 515 |
| Forebay shaft | S2 LC3 (target) | 4,000 | 350 | 1,316 | 873 | 442 (110.6) | 588 |

*Table A6. Scenario totals (central case).*
*Source: `results/lca_scenarios.md`; the like-for-like steel row is the examiner's estimate (review.md, 21/10; working in A7), not yet scripted. Units 2–4 = 3 × per unit (Unit 1's basemat is placed and its forebay partly placed; whether Unit 1's shaft-wall infill could still use LC3 is [TO VERIFY]). Every column is on the mode-case basis.*

| Scenario | Saving t CO₂e/unit | Units 2–4 t CO₂e | Clinker avoided t/unit (Units 2–4) | % of target concrete | % of unit life cycle (mode case) | g/kWh saved |
|---|---:|---:|---:|---:|---:|---:|
| S1 slag in C1 target structures (C1 fallback) | 1,552 | 4,657 | 2,019 (6,057) | 30.6 | 0.405 | 0.0109 |
| **S2 LC3 in C1 target structures (C1 target binder)** | **1,734** | **5,201** | **2,304 (6,913)** | **34.1** | **0.452** | **0.0122** |
| S2b LC3 in targets + slag in all other concrete | 2,488 | 7,464 | 3,286 (9,857) | 49.0 | 0.649 | 0.0175 |
| S3 like-for-like: low-end steel factors, target-structure steel only | about 566 [examiner estimate, TODO: script] | [TODO: script] | 0 | — | [TODO: script] | [TODO: script] |
| S3 upper bound: all plant steel at best-practice EAF sections factors | 3,714 | 11,142 | 0 | — | 0.969 | 0.0262 |
| S3 sensitivity: all plant steel at world-average factors | −8,399 | −25,198 | 0 | — | −2.192 | −0.0592 |

S3 rows are sensitivities on the baseline steel, not part of C1 (positive = lower than S0); A7 explains why only the like-for-like row compares with S2. Every life-cycle share uses the mode-case total (383,243 t per unit), so the rows are comparable. On the Monte Carlo basis the LC3 share has a median of 0.29% (0.18–0.46%; Appendix C4); Monte Carlo shares for the other scenarios are not in the model outputs [TODO: lca-analyst]. Savings exclude the construction uplift (A7).

**Resource use per unit of output.** Clinker avoided by LC3 = 2,304 t / 1.419 × 10⁸ MWh = 0.016 kg/MWh (7.7 t/MWe). Concrete: 20,700 m³ × 2.4 t/m³ / 1.419 × 10⁸ MWh = 0.35 kg/MWh. Steel: 9,900 t / 1.419 × 10⁸ MWh = 0.070 kg/MWh.

### A7. Steel, transport and construction total

**Result.** Construction emits 34,381 t CO₂e per unit (0.24 g/kWh, mode case); steel emits about twice what concrete does.

- Steel: kg CO₂e = rebar × EF_rebar + other × EF_other = 3,105 × 0.97 + 6,795 × 1.73 = 3,012 + 11,755 = **14,767 t**.
- Transport to site (EN 15804 module A4): concrete 20,700 m³ × 2.4 t/m³ × 15 km × 0.10 kg/t-km = 74.5 t; steel 9,900 t × 500 km × 0.10 kg/t-km = 495 t; total **570 t** (distances are assumptions; the cement plant is also in Clarington [TO VERIFY]).
- Other materials and site energy (copper, cabling, insulation, site diesel, Ontario-grid electricity, processing of equipment beyond steel production, tunnel boring): uplift of 50% (assumption, range 25–150%) on concrete + steel + transport: 0.5 × (7,584 + 14,767 + 570) = **11,460 t**.
- **Construction total** = 7,584 + 14,767 + 570 + 11,460 = **34,381 t**, or 34,381 / 1.419 × 10⁸ MWh = **0.242 g/kWh**.

**Steel scenarios: like-for-like and whole plant.** S3 is a sensitivity, not part of C1, and only a like-for-like version compares with S2.
- **Like-for-like (target structures only)** [examiner estimate, TODO: script; lca-analyst to add this row to `lca_scenarios.py`]: the known steel in the C1 target structures at the low-end factors of Table A4 (plate 1.22, the Buy Clean California hot-rolled-sections limit; rebar 0.89, the mill-gate limit): 953 t × (1.73 − 1.22) + 1,000 t × (0.97 − 0.89) = 486 + 80 = **about 566 t per unit**, against 1,734 t for LC3. Shaft-wall module steel is unknown and excluded (as in A9), so this understates the target-structure steel; until it is known, LC3 is the larger lever within the structures C1 targets.
- **Whole-plant upper bound** (`lca_scenarios.md`, S3 low): all 9,900 t of plant steel at the same factors saves 3,714 t, about 2.1 × LC3. It is an upper bound because it applies a hot-rolled-sections factor to turbine and reactor-pressure-vessel forgings and nuclear-grade plate, for which that factor is not shown to be feasible (residual-element limits and qualification are not assessed).
- **World average** (S3 high): −8,399 t, i.e. world-average steel would add emissions.

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

*Table A10. Granta Eco Audit against the model (EN 15804 A1–A3 materials, central case, S0 as defined in A6). No Granta values exist yet; the table is ready to fill from the export.*
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
- **R2.2 (eco-audit or equivalent).** Produced: the equivalent analysis in full, and the Granta set-up and comparison rule; Table A10 ready to fill. Missing: the Granta run itself [TODO: results pending].
- **R2.5, R2.6 (supporting).** Produced (v3): the S0 counterfactual and its business-as-usual consequence (A6); the like-for-like steel working and the whole-plant upper-bound caveat (A7). Missing: OPG's actual mix; the scripted like-for-like row.
- **R1.4, R5.4 (supporting).** Produced (v3): the geometry cited as read. Missing: a `sources.md` entry for the news report; ENR replaced.

### Remaining TODOs

1. **[TO VERIFY, blocking]** Every factor in Table A4 and every quantity in A3 (priority order in `02_Research/sources_lca.md`). Re-run the three scripts and re-copy any value that moves.
2. **[TODO: results pending]** Run Granta (A9) and fill Table A10; add the screenshot.
3. **[TODO: Leroy]** Sourced whole-plant concrete and steel quantities, DPSC thicknesses, forebay per unit or shared, net MWe, CF, design life, burnup, enrichment.
4. **[TODO]** Tunnel length and bored cross-section (row 4 of Table A3); recycled content from the CRSI 2022 EPD; what preprint 202505.1533 is.
5. **[TODO: references]** Authors for the arXiv overview (2025) and LACCEI (2026); replace ENR (2018) with a peer-reviewed LCA; add NRMCA (2021), Canada Energy Regulator (n.d.) and EN 15804 forms consistently with `sources.md`; cite the CRSI 2022 EPD instead of 2017.
6. **[TO VERIFY, P1]** The OPG basemat story (or NEDO-33926) for D = 37 m, h = 35 m and the 953 t module; until then A3's geometry rests on a news report.
7. **[TODO: lca-analyst]** US grid factors as CO₂e (eGRID) rather than CO₂ only; Monte Carlo life-cycle shares for S1, S2b and S3.
8. **[TODO: script]** Add the like-for-like S3 row (A7) to `lca_scenarios.py` with Units 2–4, share and g/kWh, and replace the examiner's estimate in Table A6 and §6.
9. **[TO VERIFY]** OPG's actual infill and forebay mix and any cement-type limit in NEDO-33926; if slag is already in the baseline, re-define S0 and re-run (A6).
10. **[TODO: source needed]** A `sources.md` entry for the okdiario (2026) news report, until the OPG story or NEDO-33926 replaces it.


Rubric coverage: RB.5, R2.4, R3.8 (also supports R2.1, R2.7, R3.2, R3.4, R3.6, R1.3, R5.2)

<!--
CHANGELOG
- v1, 20/10/2026 (writer). First draft of Appendix B1–B3, cited from §8.1 and §8.3.
  - review.md A10 and top priority 2; factcheck.md A3, A10 and blocking item 6: the Senate arithmetic, licensing durations, HHI working and route scores now exist in an appendix. The §8.1 and §8.3 pointers are updated to "Appendix B1/B2/B3".
  - factcheck.md A3: the majority of 39 is stated as "all 76 senators voting". review.md §8.1 point 2: the "36 even with every other crossbencher" robustness check is shown (B1.2).
  - review.md §8.3 point 1 and T3 point 6: each HHI result carries both its 2023 and its 2010 class, and the "scale, not legal test" caveat is stated (B2.1, B2.3).
  - factcheck.md B3/B18: the mining-by-company case (1,118) is shown as the one case below 1,800, with its working (B2.4).
  - factcheck.md A10, review.md §8.1 point 6: the route scores are labelled as our qualitative judgement, with the weight test (B3).
  - Not done here: the CRAI enrichment row (review.md §8.3 point 2; analyst must add it to hhi.py and sources.md first), and the other Appendix B calculations listed in plan §3 (displacement, schedule value, same money, LCOE, MCDA).
- Presentation items: R5.1 (each subsection opens with its result); R5.2 (Tables B1–B14, caption and source above each table, as review.md asks); R5.3 (prose kept to the steps; appendices do not count towards the page limit, plan §1 [confirm, T2]); R5.4 (Harvard, same author forms as §8.1 and §8.3); R5.5 (Australian English).
- Every input is unverified. All [TO VERIFY] markers from the briefs, results and parameter files are kept.
-->

## Appendix B. Working for the policy and supply-chain analysis

This appendix gives the full working behind §8.1 (law and licensing) and §8.3 (fuel-supply concentration). Every number is produced by a script in `03_LCA_Calculations/scripts/` from a parameter file, so it can be re-run. **No input has yet been checked against its primary source** (`status: TO VERIFY` in `parameters_run2.yaml`; `verified: false` in `parameters_run3.yaml`).

| Subsection | Script (run from the repository root) | Inputs | Output |
|---|---|---|---|
| B1 Legal and political pathway | `python3 -I 03_LCA_Calculations/scripts/law_timelines.py` | `03_LCA_Calculations/parameters_run2.yaml` | `03_LCA_Calculations/results/law_timelines.csv` |
| B2 Supply concentration (HHI) | `python3 -I 03_LCA_Calculations/scripts/hhi.py` | `03_LCA_Calculations/parameters_run3.yaml` | `03_LCA_Calculations/results/hhi.md`, `hhi_summary.csv` |
| B3 Routes to a licensable SMR in Australia | none (qualitative scoring) [TODO: move into the MCDA script, analyst run 7] | Law brief §5 | This appendix |

---

### B1. Legal and political pathway

**Result.** Three laws bar an SMR at Liddell, and each has a different veto holder. On current party positions, the federal repeal is 7 Senate votes short (3 short even with every other crossbencher), and the NSW repeal bill is stalled. For comparison, Darlington's licence to construct took about 29 months, 17.9 years after its environmental assessment began.

#### B1.1 The three legal barriers and what removes each

*Table B1. The legal barriers to an SMR at Liddell, what removes each, and who holds the veto.*
*Source: legislation as named [TO VERIFY wording in the current compilations]; ARPANSA (n.d.); Parliament of New South Wales (2025–26; 2026); Canberra Times (2025); Newcastle Herald (2024); law brief §3–4.*

| # | Barrier | Instrument and effect (as extracted) | What removes it | Who decides (veto holder) | Status, October 2026 |
|---|---|---|---|---|---|
| 1 | Federal environmental approval | *Environment Protection and Biodiversity Conservation Act 1999* (Cth) s 140A (parallel bars in ss 37J and 146M): the Minister "must not approve" an action involving the construction or operation of a nuclear power plant [TO VERIFY] | Amendment of ss 37J, 140A and 146M | Commonwealth Parliament; in practice the Senate (B1.2) | In force. Whether the 2025 EPBC reforms changed s 140A is unchecked (Norton Rose Fulbright, 2025) [TO VERIFY] |
| 2 | Federal radiation licensing | *Australian Radiation Protection and Nuclear Safety Act 1998* (Cth) s 10(2): the CEO "must not issue a licence" for a nuclear power plant [TO VERIFY]. ARPANSA licenses only Commonwealth-controlled bodies (s 13, "controlled person") (ARPANSA, n.d.) [TO VERIFY] | Repeal of s 10, **and** a regulator with power over private operators (route choice, B3) | Commonwealth Parliament (Senate) | In force. A Senate committee recommended against the 2022 repeal bill (Senate Environment and Communications Legislation Committee, 2023) [TO VERIFY]; the bill lapsed at prorogation [TODO: source needed: ParlInfo bill page] |
| 3 | State ban | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8: offence to build or operate a nuclear reactor, except for the s 8(3) exceptions (the Commonwealth's AAEC successors, such as ANSTO); s 9: other Acts do not authorise a state authority to build or approve one [TO VERIFY] | NSW repeal, or a Commonwealth override under Constitution s 109 [TODO: add the Constitution to sources.md], which may face a High Court challenge (Canberra Times, 2025) [TO VERIFY] | NSW Parliament (Legislative Assembly), or the Commonwealth | Repeal bill passed the Legislative Council; stalled in the Assembly (B1.3) |
| (4) | Site (not a law) | AGL owns Liddell and has ruled out nuclear there (Newcastle Herald, 2024) [TO VERIFY] | AGL's consent, or compulsory acquisition by the Commonwealth | AGL, or the Commonwealth | AGL opposed |

Order of removal: federal repeal (1 and 2) → choice of regulator → state repeal or override (3) → site (4) → environmental assessment → licensing (law brief §4). Each step has a different veto holder, so all must agree.

#### B1.2 Senate arithmetic for federal repeal

*Table B2. Senate composition used for the repeal arithmetic.*
*Source: Parliament of Australia (2026) [TO VERIFY; composition as at 14 May 2026]; `parameters_run2.yaml`.*

| Party or group | Seats | Position on repeal | Source of position |
|---|---:|---|---|
| Australian Labor Party | 30 | Opposed | Bowen (2025) [TO VERIFY date; no 2026 statement found] |
| Coalition | 27 | For | Liberal Party of Australia (2026); ABC News (2026) [TO VERIFY] |
| Australian Greens | 10 | Opposed | Australian Greens (2025) [TO VERIFY] |
| One Nation | 4 | Assumed for | **Assumption** [TODO: source needed: ABC, 31 August 2026, is in the law brief but not in sources.md] |
| Senator Babet | 1 | Assumed for | **Assumption** (no source) |
| Lambie, Payman, Pocock, Thorpe | 4 (1 each) | Not assumed | — |
| **Total** | **76** | | Script asserts the parts sum to 76 |

Steps (`law_timelines.py`):

| Step | Working | Result |
|---|---|---|
| 1. Majority needed, all 76 voting | ⌊76 / 2⌋ + 1 (a tied vote fails, Constitution s 23 [TO VERIFY wording]) | **39** |
| 2. Largest pro-repeal bloc (upper bound) | Coalition 27 + One Nation 4 + Babet 1 | **32** |
| 3. Shortfall | 39 − 32 | **7** |
| 4. Bloc plus every other crossbencher | 32 + 4 | **36** (still 3 short) |
| 5. Can repeal pass without Labor or the Greens? | 36 ≥ 39? | **No** |
| 6. Would the Greens alone be enough (arithmetic only)? | 32 + 10 = 42 ≥ 39? | Yes, but the Greens oppose (policy, not arithmetic) |
| 7. Opposed bloc | Labor 30 + Greens 10 = 40 ≥ 39 | A blocking majority on its own |

Result 4 makes the conclusion independent of the One Nation and Babet assumption. In the House, Labor holds 94 of 150 seats (Australian Electoral Commission, 2025) [TO VERIFY], so a repeal bill would also need the Government's support there.

#### B1.3 NSW repeal bill status

*Table B3. Progress of the NSW repeal bill (private member's bill).*
*Source: Parliament of New South Wales (2025–26; 2026) [TO VERIFY]; `parameters_run2.yaml`.*

| Event | Date | Note |
|---|---|---|
| Introduced in the Legislative Council | 19 November 2025 | — |
| Passed the Legislative Council | 6 May 2026 | About 5.5 months after introduction (law brief §4). All Liberal and National MLCs voted for it [TO VERIFY] |
| Legislative Assembly | Awaiting the second reading speech (notice paper reported 27 May 2026) | The Minns Labor Government opposes repeal and holds an Assembly majority [TO VERIFY; Minns quote is secondary, Canberra Times (n.d.)] |
| Lapses | 28 November 2026 | Unless the Assembly acts first [TO VERIFY against the latest notice paper] |

#### B1.4 Licensing timelines: Darlington (Canada)

*Table B4. CNSC licensing milestones for the Darlington New Nuclear Project.*
*Source: Canadian Nuclear Safety Commission [CNSC] (2021; 2025; 2026a; 2026b) [TO VERIFY]; `parameters_run2.yaml`.*

| Milestone | Date | Parameter key |
|---|---|---|
| Environmental assessment begins (joint review panel) | May 2007 (taken as 1 May) | `dnnp_ea_start` |
| Licence to prepare site issued | 17 August 2012 | `dnnp_lpts_issued` |
| Site licence renewed, valid to 11 October 2031 | 12 October 2021 | `dnnp_lpts_renewed` |
| Licence-to-construct application (one unit, in packages) | October 2022 (taken as 31 October) | `dnnp_ltc_application` |
| Hearing part 2 begins (Ajax) | 8 January 2025 | `dnnp_ltc_hearing_part2_start` |
| Licence to construct issued (PRCL 32.00/2035, one BWRX-300) | 4 April 2025 | `dnnp_ltc_decision` |
| Regulatory hold point 1 lifted (reactor building foundation) | 30 March 2026 | `dnnp_rhp1_lifted` |
| Licence to construct expires | 31 March 2035 | `dnnp_ltc_expiry` |

Method: months = days between two dates ÷ (365.25 / 12); years = months ÷ 12.

*Table B5. Licensing durations calculated from Table B4.*
*Source: `03_LCA_Calculations/results/law_timelines.csv`.*

| Quantity | Dates used | Result |
|---|---|---|
| Application to licence to construct | 31 Oct 2022 → 4 Apr 2025 (886 days) | **29.1 months** (2.43 years) |
| Sensitivity: application day unknown within October | 1 Oct 2022 → 4 Apr 2025 | 29.1–30.1 months |
| Against CNSC's expected review time (32 months, REGDOC-3.5.1 (CNSC, [year TO VERIFY]); extract ambiguous, another row reads 24 months) | 29.1 − 32 | −2.9 months (faster) [TO VERIFY benchmark] |
| Hearing part 2 to decision | 8 Jan 2025 → 4 Apr 2025 | 2.8 months |
| Environmental assessment start to licence to construct | May 2007 → 4 Apr 2025 | **17.9 years** (elapsed, not continuous review) |
| Licence validity from issue | 4 Apr 2025 → 31 Mar 2035 | 10.0 years |
| Licence validity remaining at the report date | 20 Oct 2026 → 31 Mar 2035 | 8.4 years |
| Licence to construct to RHP-1 lifted | 4 Apr 2025 → 30 Mar 2026 | 11.8 months |

The licence covers one unit. Units 2–4 need a further Commission authorisation, with approval to proceed reported as expected in 2028 (American Nuclear Society, 2026) [TO VERIFY; secondary, and the type of approval is not stated]. No source gives the Units 2–4 review time.

Australian comparator: the naval nuclear regulator (ANNPSR) began operating on 1 November 2025 under a 2024 Act (Minister for Defence, 2025) [TO VERIFY], about two years after its Act for a narrower scope [TODO: bill introduction date from Bills Digest No. 32, 2023–24, to give an exact interval].

---

### B2. Supply concentration: Herfindahl–Hirschman index (HHI) working

**Result.** On the 2023 US merger guidelines, mining by country (2,341), conversion (2,111) and enrichment (3,009) are all "highly concentrated". On the superseded 2010 guidelines only enrichment is; mining and conversion are "moderately concentrated". Removing Russia raises the HHI at every stage. Removing Russia and China leaves enrichment as a Urenco–Orano duopoly (5,621). The one case below 1,800 is mining by company (1,118), so mining concentration is a country (geopolitical) risk rather than a market-power risk.

#### B2.1 Method

1. Share of supplier *i*: s*ᵢ* = 100 × q*ᵢ* / Σq (per cent), where q is output or capacity.
2. HHI = Σ s*ᵢ*² (range 0 to 10,000; one supplier = 10,000).
3. Equivalent number of equal-sized suppliers: N_eq = 10,000 / HHI.
4. Measures: mining by country (2024 mine output, tU); conversion by company (licensed capacity, tU as UF₆ per year; production as a check); enrichment by company (capacity, thousand SWU per year; 2025 base, 2022 and 2030 as sensitivity).
5. "Without Russia": Russian supply removed and the remaining shares renormalised, with no new capacity (the market open to a buyer barred from Russian material). "Without Russia and China" also removes CNNC, whose capacity WNA estimates on the assumption that it serves China's own fleet; this approximates the market open to a Canadian or Australian utility.
6. "Others" or residual rows are bounded: one supplier (upper bound) or many small suppliers (lower bound, about 0). The difference is below 3 HHI points in every 2024/2025 case.
7. Shares are squared before rounding, so squaring a rounded share in the tables can differ by less than 1 point.

*Table B6. HHI thresholds used as a scale.*
*Source: US Department of Justice and Federal Trade Commission (2023; 2010) [TO VERIFY wording].*

| Guideline | Unconcentrated | Moderately concentrated | Highly concentrated | Status |
|---|---|---|---|---|
| *Merger Guidelines* (2023), §2.1 | — | — | HHI > 1,800 [TO VERIFY: "greater than" or "1,800 or greater"] | Current |
| *Horizontal Merger Guidelines* (2010), §5.3 | < 1,500 | 1,500–2,500 | > 2,500 | Superseded; reported because mining and conversion fall between the two thresholds |

These are antitrust screens for merger review. Here they are used as a recognised scale for supply concentration, not as a legal test.

**Worked example (enrichment, 2025).**
1. Rosatom's share = 100 × 29,133 / 68,077 = 42.79%; squared = 1,831.3.
2. Repeat for Urenco, CNNC, Orano and Other; sum = 1,831.3 + 645.8 + 410.3 + 121.4 + 0.3 = **3,009**. N_eq = 10,000 / 3,009 = 3.3.
3. Without Russia: total = 68,077 − 29,133 = 38,944 kSWU. Urenco's share = 100 × 17,300 / 38,944 = 44.42%; and so on. HHI = **3,599**.
4. Without Russia and China: total = 38,944 − 13,789 = 25,155 kSWU. Urenco 68.77%, Orano 29.82%, Other 1.41%. HHI = **5,621** (N_eq = 1.8).

#### B2.2 Inputs and shares

*Table B7. Uranium mine output by country, 2024.*
*Source: World Nuclear Association (2026) [TO VERIFY year and every row; several rows are WNA estimates]; calculated in `hhi.py` (`results/hhi.md` §3.1–3.2). Internal check: the rows sum exactly to 60,213 tU.*

| Country | tU | Share (%) | Share² | Share without Russia (%) | Share² |
|---|---:|---:|---:|---:|---:|
| Kazakhstan | 23,270 | 38.65 | 1,493.5 | 40.49 | 1,639.2 |
| Canada | 14,309 | 23.76 | 564.7 | 24.90 | 619.8 |
| Namibia | 7,333 | 12.18 | 148.3 | 12.76 | 162.8 |
| Australia | 4,598 | 7.64 | 58.3 | 8.00 | 64.0 |
| Uzbekistan | 4,000 | 6.64 | 44.1 | 6.96 | 48.4 |
| Russia | 2,738 | 4.55 | 20.7 | — | — |
| China | 1,600 | 2.66 | 7.1 | 2.78 | 7.7 |
| Niger | 962 | 1.60 | 2.6 | 1.67 | 2.8 |
| India | 500 | 0.83 | 0.7 | 0.87 | 0.8 |
| Ukraine | 288 | 0.48 | 0.2 | 0.50 | 0.3 |
| USA | 260 | 0.43 | 0.2 | 0.45 | 0.2 |
| South Africa | 200 | 0.33 | 0.1 | 0.35 | 0.1 |
| Others | 155 | 0.26 | 0.1 | 0.27 | 0.1 |
| **Total (tU) / HHI** | **60,213** (57,475 without Russia) | 100.00 | **2,341** | 100.00 | **2,546** |

Without Russia and China, the mining HHI is 2,686 (`hhi_summary.csv`; `hhi.py` does not print the share table for this case).

*Table B8. Mining by country, earlier years (only the eight largest rows retrieved; residual bounded).*
*Source: World Nuclear Association (2026) [TO VERIFY]; `results/hhi.md` §3.3.*

| Year | Residual (tU) | HHI lower bound | HHI upper bound | Russia's share (%) |
|---|---:|---:|---:|---:|
| 2022 | 1,083 | 2,368 | 2,372 | 5.1 |
| 2023 | 1,204 | 2,243 | 2,248 | 5.0 |

*Table B9. Conversion by company, licensed capacity (tU as UF₆ per year).*
*Source: World Nuclear Association (2024) [TO VERIFY year and rows; CNNC and Rosatom are WNA estimates]; `results/hhi.md` §3.5.*

| Company (country) | tU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| CNNC (China) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | — | — |
| Orano (France) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | 43.48 | 1,890.4 |
| Cameco (Canada) | 12,500 | 20.16 | 406.5 | 25.25 | 637.7 | 36.23 | 1,312.7 |
| Rosatom (Russia) | 12,500 | 20.16 | 406.5 | — | — | — | — |
| ConverDyn (USA) | 7,000 | 11.29 | 127.5 | 14.14 | 200.0 | 20.29 | 411.7 |
| **Market total (tU/yr) / HHI** | **62,000** | 100.00 | **2,111** | 49,500 | **2,674** | 34,500 | **3,615** |

*Table B10. Enrichment by company, 2025 capacity (thousand SWU per year).*
*Source: World Nuclear Association (2025) [TO VERIFY year and rows; CNNC is a WNA estimate; 2030 figures are plans]; `results/hhi.md` §3.6.*

| Company | kSWU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rosatom | 29,133 | 42.79 | 1,831.3 | — | — | — | — |
| Urenco | 17,300 | 25.41 | 645.8 | 44.42 | 1,973.4 | 68.77 | 4,729.8 |
| CNNC | 13,789 | 20.26 | 410.3 | 35.41 | 1,253.7 | — | — |
| Orano | 7,500 | 11.02 | 121.4 | 19.26 | 370.9 | 29.82 | 888.9 |
| Other (INB, JNFL) | 355 | 0.52 | 0.3 | 0.91 | 0.8 | 1.41 | 2.0 |
| **Market total (kSWU/yr) / HHI** | **68,077** | 100.00 | **3,009** | 38,944 | **3,599** | 25,155 | **5,621** |

Russia's enrichment share is 43.3% in 2022 and 38.3% in the 2030 plans (World Nuclear Association, 2025) [TO VERIFY]. [TODO: analyst. Add the CRAI (2025) Rosatom and CNNC capacities to `hhi.py` and `sources.md`, and report Russia's share as a range (review.md §8.3 point 2; R1.3).]

#### B2.3 Headline results

*Table B11. HHI of the uranium front end by stage, with and without Russia and China.*
*Source: `03_LCA_Calculations/results/hhi.md` §2 and `hhi_summary.csv`, from the inputs in Tables B7–B10 [all TO VERIFY].*

| Stage (measure, base year) | HHI | N_eq | 2023 class | 2010 class | Without Russia | Without Russia and China | Russia's share |
|---|---:|---:|---|---|---:|---:|---:|
| Mining (output by country, 2024) | 2,341 | 4.3 | Highly | Moderately | 2,546 (highly under both) | 2,686 | 4.5% |
| Conversion (capacity by company, [year TO VERIFY]) | 2,111 | 4.7 | Highly | Moderately | 2,674 (highly under both) | 3,615 | 20.2% |
| Enrichment (capacity by company, 2025) | **3,009** | 3.3 | Highly | Highly | 3,599 | **5,621** | **42.8%** |

Shares for the two producer countries in the comparison: Canada mined 23.8% of world uranium in 2024 and holds 20.2% of world conversion capacity (36.2% of the capacity open to a Western buyer), with no enrichment. Australia mined 7.6% (4,598 tU) and has no conversion or enrichment capacity. Australia holds 28% of identified recoverable resources at < USD 130/kgU (OECD NEA and IAEA, 2025) [TO VERIFY; Red Book 2026 gives 29% or 27% in two WNA tabulations; team to choose the edition, §8.3 TODO 4].

#### B2.4 Sensitivity

*Table B12. HHI under every tested scenario.*
*Source: `03_LCA_Calculations/results/hhi_summary.csv` [inputs TO VERIFY].*

| Stage | Scenario | HHI | N_eq | 2023 class | 2010 class | Note |
|---|---|---:|---:|---|---|---|
| Mining (country) | 2024 base | 2,341 | 4.3 | Highly | Moderately | |
| Mining (country) | 2024 base, "Others" atomistic | 2,341 | 4.3 | Highly | Moderately | Lower bound |
| Mining (country) | 2024 without Russia | 2,546 | 3.9 | Highly | Highly | |
| Mining (country) | 2024 without Russia and China | 2,686 | 3.7 | Highly | Highly | |
| Mining (country) | 2024 without Russia, China and Niger | 2,778 | 3.6 | Highly | Highly | Niger: exports disrupted since the 2023 coup (secondary) [TO VERIFY] |
| Mining (country) | 2022 (residual bounds) | 2,370 | 4.2 | Highly | Moderately | Range 2,368–2,372 |
| Mining (country) | 2022 without Russia | 2,601 | 3.8 | Highly | Highly | Range 2,598–2,603 |
| Mining (country) | 2023 (residual bounds) | 2,246 | 4.5 | Highly | Moderately | Range 2,243–2,248 |
| Mining (country) | 2023 without Russia | 2,460 | 4.1 | Highly | Moderately | Range 2,457–2,462 |
| **Mining (company)** | **2024 bounds (top three known)** | **1,118** | **8.9** | **Not highly** | **Unconcentrated** | **Range 851–1,384; partial data** |
| Conversion | Capacity base | 2,111 | 4.7 | Highly | Moderately | |
| Conversion | Capacity without Russia | 2,674 | 3.7 | Highly | Highly | |
| Conversion | Capacity without Russia and China | 3,615 | 2.8 | Highly | Highly | Market open to a Western buyer |
| Conversion | Production base | 2,109 | 4.7 | Highly | Moderately | |
| Conversion | Production without Russia | 2,672 | 3.7 | Highly | Highly | |
| Conversion | ConverDyn 15,000 tU (alternative) | 2,015 | 5.0 | Highly | Moderately | Secondary source; sensitivity only |
| Conversion | ConverDyn alternative, without Russia | 2,514 | 4.0 | Highly | Highly | |
| Conversion | ConverDyn alternative, without Russia and China | 3,356 | 3.0 | Highly | Highly | |
| Enrichment | 2022 capacity | 3,065 | 3.3 | Highly | Highly | |
| Enrichment | 2022 without Russia | 3,707 | 2.7 | Highly | Highly | |
| Enrichment | 2022 without Russia and China | 5,722 | 1.7 | Highly | Highly | Market open to a Western buyer |
| Enrichment | 2025 capacity (base) | 3,009 | 3.3 | Highly | Highly | |
| Enrichment | 2025 without Russia | 3,599 | 2.8 | Highly | Highly | |
| Enrichment | 2025 without Russia and China | 5,621 | 1.8 | Highly | Highly | Market open to a Western buyer |
| Enrichment | 2030 capacity (plans) | 2,724 | 3.7 | Highly | Highly | |
| Enrichment | 2030 without Russia | 3,299 | 3.0 | Highly | Highly | |
| Enrichment | 2030 without Russia and China | 4,827 | 2.1 | Highly | Highly | Market open to a Western buyer |

Reading:
- **Data year** moves the HHI by a few hundred points but never changes the 2023 class. Enrichment and conversion are highly concentrated in every year tested.
- **Capacity versus production** (conversion) changes the HHI by less than 10 points.
- **ConverDyn's capacity** (7,000 or 15,000 tU) is the largest data uncertainty for conversion. The higher value lowers the HHI to 2,015, still above 1,800.
- **Threshold choice** matters for mining and conversion only: both are "highly" concentrated on the 2023 scale and "moderately" on the 2010 scale. Enrichment is highly concentrated on both.
- **Removing Russia** is the dominant effect at every stage, and it always increases concentration.

**Mining by company (the one case below 1,800).** Only the top three 2024 shares were retrieved: Kazatomprom 21%, Cameco 17%, Orano 11% (World Nuclear Association, 2026) [TO VERIFY company-table year]; Kazatomprom's 21% is cross-checked by Kazatomprom (2025) [TO VERIFY]. Together they hold 49%.
1. Lower bound (the other 51% held by many small firms): 21² + 17² + 11² = 441 + 289 + 121 = **851**.
2. Upper bound (the other 51% split into firms no larger than the third-ranked, 11%, i.e. four at 11% and one at 7%): 851 + 4 × 11² + 7² = 851 + 484 + 49 = **1,384**.
3. Central value reported by `hhi.py`: the midpoint, (851 + 1,384) / 2 = **1,118** (N_eq = 8.9).

Both bounds are below 1,500, so firms are not concentrated even though countries are. Kazakhstan's 38.6% country share includes joint ventures with Cameco, Orano, Uranium One (Rosatom) and Chinese partners [TO VERIFY ownership detail].

#### B2.5 Limitations

- Capacity is not supply. Nameplate SWU includes capacity Rosatom uses for underfeeding and tails re-enrichment, and CNNC's figures are WNA estimates.
- Secondary supply (inventories, down-blending, re-enriched tails) is excluded. Mine output in 2024 (60,213 tU) met about 93% of reactor requirements (64,500 tU at 1 January 2025; OECD NEA and IAEA, 2026) [TO VERIFY].
- Company-level enrichment shares hide plant location: Urenco operates in the UK, Germany, the Netherlands and the USA; Orano only in France.
- Mining by country ignores ownership (for example, Rosatom's Uranium One stakes in Kazakh mines) and the transport routes for Kazakh exports [TO VERIFY]. The company-level bound only partly addresses ownership.
- Fuel fabrication was not assessed.
- The HHI is a world-market measure. It is not yet sized to Darlington's own fuel demand [TODO: Leroy/analyst. BWRX-300 core loading, reload fraction, cycle length and enrichment, to give SWU/yr for four units; §8.3 TODO 6].

---

### B3. Routes to a licensable SMR in Australia: scored comparison

**Result.** The ranking depends on the weights: route C (cooperative state repeal) ranks first on equal weights and when durability is valued more; route A (Commonwealth-owned plant) ranks first when regulator readiness is valued more. Under the 2026 Senate (B1.2), none of the three routes is open. **These scores are our own qualitative judgement from the evidence in B1, not sourced scores.** They feed the "feasibility" criterion of the §9 MCDA.

*Table B13. Three routes scored against four non-technical objectives (1 = poor, 3 = good).*
*Source: our qualitative judgement (law brief §5), from the evidence cited in the table.*

| Objective | A. Commonwealth-owned plant under ARPANSA (the Coalition's 2024 model) | B. Federal licensing law for private operators, overriding the states | C. Cooperative: state repeal plus a state or joint regulator |
|---|---|---|---|
| Legal changes needed (not scored) | EPBC and ARPANS repeal, plus a s 109 override of NSW (or NSW repeal) | EPBC and ARPANS repeal, a new federal Act and a s 109 override | EPBC and ARPANS repeal, NSW repeal and a NSW regulator Act |
| Fewest veto points | **2**: Senate; site owner | **1**: Senate; High Court; site owner | **1**: Senate; NSW Parliament; site owner |
| Regulator readiness | **3**: builds on ARPANSA, which already regulates Commonwealth entities such as ANSTO (ARPANSA, n.d.) [TO VERIFY] | **2**: a new body, as with the ANNPSR (Minister for Defence, 2025) [TO VERIFY] | **1**: NSW has no nuclear regulator |
| Durability (low exposure to political reversal) | **1**: one government's decision; the next can sell or cancel | **1**: as A, plus litigation risk (Canberra Times, 2025) [TO VERIFY] | **3**: both levels of government committed |
| Social licence | **1**: states rejected it in 2024 [TODO: source needed; Canberra Times (n.d.) on Minns is a secondary lead] | **1**: overrides the states | **3**: the states consent, if they do |
| **Total (of 12)** | **7** | **5** | **8** |

Route A's description currently rests on ABC News (2024), a weak secondary source [TODO: replace with the Coalition's 19 June 2024 release, factcheck A8].

*Table B14. Weight test: totals when one objective counts double (maximum 15).*
*Source: calculated from Table B13 (law brief §5).*

| Weighting | A | B | C | Ranking |
|---|---:|---:|---:|---|
| Equal weights (base, of 12) | 7 | 5 | 8 | C, A, B |
| Regulator readiness × 2 | 7 + 3 = **10** | 5 + 2 = 7 | 8 + 1 = 9 | A, C, B |
| Durability × 2 | 7 + 1 = 8 | 5 + 1 = 6 | 8 + 3 = **11** | C, A, B |

Reading: route B ranks last under all three weightings tested. The choice between A and C is a choice between speed (an existing regulator) and durability (both levels of government committed). That is a political judgement, not a technical one. Whichever route is assumed, an Australian SMR scores lowest on time to first power in the §9 MCDA.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **RB.5 (full calculations in an appendix, results summarised in the main text).**
  - Produced: the working behind every number in §8.1 and §8.3 (Senate arithmetic, licensing durations, HHI shares and sensitivity, route scores), each traced to a script output, with the commands to re-run.
  - Missing: input verification; the other Appendix B calculations in plan §3 (displacement, schedule value, same money, LCOE, MCDA), which have results files but no appendix text yet.
- **R2.4 ("methods are clearly explained and easy to follow").**
  - Produced: stated formulas (months, Senate majority, HHI, N_eq, renormalisation, residual bounds), a worked enrichment example, and the threshold sources with the "scale, not legal test" caveat.
  - Missing: §2 (methods) is not written, so the main text still has no method summary; the B3 weight test is not scripted.
- **R3.8 ("supported by evidence and quantitative/qualitative analysis").**
  - Produced: quantitative tables for the political and supply arguments, the qualitative route scoring clearly labelled as judgement, and every unverified input marked.
  - Missing: no primary source opened; One Nation, Babet and the 2024 state rejection still lack sources.
- **R2.7 and R1.3 (supporting).** Produced: all sensitivity rows, both threshold classes, the company-versus-country contrast, and the limitations. Missing: the CRAI range for Rosatom; the Red Book edition decision.
- **R3.6 (supporting).** Produced: the scored route comparison with a weight test, ready for §9. Missing: the §9 MCDA itself.

### Remaining TODOs

1. **[TO VERIFY, P1]** Open the primaries behind Tables B1–B4 and B7–B10 (factcheck.md human checklist). Set `verified: true` / the verified status, re-run both scripts, and update any value that moves.
2. **[TODO: source needed]** One Nation's position (ABC, 31 August 2026) into `sources.md`; Babet stays an assumption. The 2022 bill's lapse (ParlInfo). The 2024 state rejection of route A. The Coalition's 19 June 2024 release for route A.
3. **[TODO: sources.md]** Add the *Commonwealth of Australia Constitution Act* (ss 23 and 109).
4. **[TODO: analyst]** Add the CRAI (2025) enrichment row to `hhi.py` and `sources.md`; report Russia's share as a range in B2.2.
5. **[TODO: analyst]** Put the B3 scoring and weight test in a script (with the §9 MCDA, run 7) so it is reproducible.
6. **[TODO: Leroy/analyst]** BWRX-300 fuel data, to size Darlington's SWU/yr against Urenco USA and Orano capacity (B2.5).
7. **[TODO: team decision]** Red Book edition for Australia's resource share (B2.3).
8. **[TODO: Leroy, references]** Disambiguate CNSC 2026a (project page) and 2026b (hold-point page); fix "Parliament of New South Wales, 2025–26" to a single year with a suffix; confirm the WNA page years; give REGDOC-3.5.1 its year.
9. **[TODO: bill date]** ANNPSR bill introduction date (Bills Digest No. 32, 2023–24), to give the "Act to operating regulator" interval exactly.
10. **[TODO: coordinator]** Write the remaining Appendix B subsections (displacement, schedule value, same money, LCOE, MCDA) from `results/`, or re-letter them as a separate appendix.
11. **[Before submission]** Strip the [TO VERIFY]/[TODO] markers and the changelog comment; set the final table numbers.


Rubric coverage: R2.7, RB.5 (also supports R2.4, R2.1, RB.6, R5.2)

<!--
CHANGELOG
- v3, 21/10/2026 (writer, for Victor). Revised against review.md "Review of §6 and Appendices A, C (21/10)": Appendix C item and §6 point 7 (Table C2 gains a row for the conversion-heat alternative run, with TODO cells, because no script output exists; C5 says what it tests); L9 (Table C1 row 33 cites the shaft depth as read, okdiario 2026, not OPG); C4 notes that the LC3-minus-slag row is also LC3's increment if OPG's baseline already contains slag (§6.1, A6). No values changed; all [TO VERIFY] markers kept.
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
| 33 | Shaft depth (m) | 35 / 35 / 38 | okdiario (2026), a news report citing an OPG story not found; high = containment height, GE Vernova Hitachi Nuclear Energy (n.d.) | V | 2.701 → 2.701 (<0.001) | 1,734 → 1,805 |
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
| Life-cycle intensity, conversion heat held at a sourced central value (g CO₂e/kWh) | [TODO: script] | [TODO: script] | [TODO: script] | [TODO: script] | [TODO: script] |
| Life-cycle intensity, conversion heat log-uniform 26–665 (g CO₂e/kWh) | [TODO: script] | [TODO: script] | [TODO: script] | [TODO: script] | [TODO: script] |

The whole-plant concrete median (24,066 m³) sits above the central value (20,700 m³) because its input range is right-skewed (34.5–69–138 m³/MWe). **The 90% interval, about 15,050–36,521 m³, is the concrete range to quote**; the input bounds (10,350–41,400 m³) are not results, and the clip rule (C1) also lifts the low tail. The LC3-minus-slag interval spans zero: the two options cannot be separated on carbon with present data. If OPG's baseline mix already contains slag (§6.1, A6), the same row is LC3's increment over business as usual. The last two rows test whether the headline median depends on the triangular shape chosen for conversion heat (C5) [TODO: lca-analyst: add a script flag for both runs and fill the rows]. The share row is for LC3 only; Monte Carlo shares for the other scenarios are not in the outputs [TODO: lca-analyst].

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
- Because one distribution choice carries most of the gap, Table C2's last two rows re-run the Monte Carlo with conversion heat at a sourced central value and with a log-uniform 26–665 distribution. If the median stays near 4.2 under both, the headline is not an artefact of the triangular shape; if not, §6 should report the range of medians [TODO: script].

### C6. Limitations of the uncertainty analysis

1. **Independence.** Inputs are drawn independently. Concrete and steel intensities are probably positively correlated (bigger plants need more of both), which would widen the construction tail slightly; enrichment and burnup are also linked in practice. The effect on the total is small because construction is about 7.5%.
2. **Ranges partly judgement.** Ranges marked A or P in Table C1 are our assumptions; ×0.5 to ×2 transfer ranges on the EDF stages are not data.
3. **Triangular shape.** A convention, not a fitted distribution.
4. **Unverified inputs.** Every V in Table C1 is a search lead. The intervals will move when the primaries are opened.
5. **Model structure not varied.** The boundary (process-based stages plus three stages transferred as per-kWh values) and the cut-offs (§6.1) are not sampled; they bias the result low (§6.5, Table T9).

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.7 (uncertainty realistically estimated and discussed).** Produced: 40-input tornado with sources and status; 20,000-draw Monte Carlo with percentiles; stage-level skew analysis explaining median vs mode; LC3 vs slag overlap (64%; interval spans zero); stated limitations. Missing: verified ranges; the conversion-heat distribution test (rows set up in Table C2, v3); a correlation case (stated as a limitation instead).
- **RB.5 (full calculations in an appendix).** Produced: set-up, every range, every result, reproduce command. Missing: nothing structural.

### Remaining TODOs

1. **[TO VERIFY, blocking]** Open the primaries for every V input in Table C1 (priority: Gibon and Hahn Menacho 2023 for conversion heat; Parker et al. 2016; EDF R&D 2024), then re-run `lca_uncertainty.py` and update Tables C1–C3.
2. **[TODO: Leroy]** Burnup, enrichment, net MWe, capacity factor and design life (the P rows) with sources.
3. **[TODO: source needed]** A measured conversion value (Cameco Port Hope facility emissions and UF₆ output).
4. **[TODO: lca-analyst]** Conversion-heat alternative runs (sourced central value; log-uniform 26–665) for the last two rows of Table C2.
5. **[TODO: source needed]** A `sources.md` entry for okdiario (2026), until the OPG story or NEDO-33926 replaces it (Table C1 row 33).
6. **[TODO: optional, STRETCH]** A correlated-draw case (concrete with steel intensity; burnup with enrichment) to replace limitation 1.


