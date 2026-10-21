Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3 (also supports R4.2, R4.4, RB.8, R5.2)

<!--
CHANGELOG
- v2, 21/10/2026 (writer, for Victor). Revised against factcheck.md §H. Items addressed:
  - Blocking: **L55** (Table T8 now has one basis per column: every life-cycle share is the mode-case saving ÷ the mode-case total, copied from `results/lca_scenarios.csv` (0.405/0.452/0.649/0.969/−2.192%); column 2 relabelled "mode case (MC 5th–95th percentile)"; the LC3 Monte Carlo median share (0.29%, 0.18–0.46%) moved to a note. Monte Carlo shares for slag and steel are not in the outputs, so there is a TODO). **L59** ("low-cost … first nuclear use" cut; cost marked TODO). **L67** (whole-plant concrete range now the Monte Carlo 90% interval, 15,050–36,521 m³; the 34.5–138 m³/MWe bounds are labelled as input bounds). **L56/L35** (one wording: just below UNECE's 5.1–6.4, with our interval overlapping it, and at the low end of the wider literature range). **L1/L52/L71** ("screening LCA following ISO 14040/44 principles, not critically reviewed"; nothing implies a Granta run). **L9** (§6.2 says the module geometry rests on a news report; [TO VERIFY] kept). **L18** (Ontario slag supply cut to a one-sentence risk with a TODO).
  - Also: L4 (EDF shares secondary, back end by difference, T6); L5 (cement range is a regional spread); L14 (Geneski: direction only); L22 (rebar EPD superseded); L23 (AISC value is a Buy Clean California limit); L25 and L26 (US grid factors CO₂ only; upstream gas cut-off added); L32 (Ng et al. scope hedged); L48 (T9 "0.3–0.8"); L57 (construction 7.5%); L58 (§8.3 "should use" the fuel demand); L60 (Unit 1 forebay partly placed, not placed); L61 ("hybrid LCA" replaced); L62 (impact category wording); L66 and L31 (F5 caption flags the UNECE midpoint; figure fix is the lca-analyst's).
  - Headline saving now on the Monte Carlo basis (median 1,740 t, as the 4.2 g/kWh is), so the lead no longer pairs a mode-case centre with a Monte Carlo interval. Units 2–4: about 5,200 t on both bases.
  - Not in this file: L64 (`results/lca.md`, lca-analyst); the F5 redraw (script); slide items L67–L79 (deck).
  - Length: §6.4 "Limitations" cut to one sentence (the cut planned in v1) to absorb the additions.
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/lca.md`, `lca_baseline.md`, `lca_scenarios.md`, `lca_uncertainty.md`, `parameters_lca.yaml`, `granta_inputs.md`, `02_Research/sources_lca.md`, `sources.md` and `briefs/benchmarks-for-sam.md`. Sam's files are untouched. Addressed review.md "For Sam" items 1–4 and "Feedback to Sam"; factcheck S15/S16/S17/S18/S20 and section E.
- Presentation items: R5.1 (section and each subsection lead with the result); R5.2 (Figures F1–F5 and Tables T6, T8, T9, captioned and sourced, caption above tables); R5.3 (v2 estimated by hand, not tool-counted, at about 1,800–1,850 words of body text excluding tables, notes, captions and markers, about 3.6 pages at 500 words a page against the ~3.5-page budget; if the integrated report runs long, fold "Resource use" into Table T6 and cut hotspot item 3 to one line); R5.4 (Harvard, author forms as in sources_lca.md); R5.5 (Australian English).
- Table IDs T8 and T9 are new (T1–T7 are taken in plan §3 and §8.1). Leroy renumbers at integration.
-->

## 6 Life-cycle assessment and eco-audit

One BWRX-300 at Darlington is estimated to emit **about 4.2 kg CO₂e per MWh delivered (Monte Carlo median; 90% interval 3.0–5.8)**. That is just below UNECE's 5.1–6.4 g/kWh for nuclear power (our interval overlaps it) and at the low end of the wider literature range. Nearly two-thirds comes from the fuel front end; construction is about 7.5%. Using LC3 concrete in the targeted structures (initiative C1, §4.3) would save **about 1,740 t CO₂e per unit (90% interval 1,390–2,150 t) and about 5,200 t across Units 2–4**, or **about 0.3% of each unit's life-cycle footprint**. That saving is real but small. A slag blend saves nearly as much, and lower-carbon steel saves about twice as much. This is a screening LCA following ISO 14040/44 principles, not critically reviewed, and every input is a published value not yet checked in its primary source [TO VERIFY], so every number here is provisional.

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of electricity from one BWRX-300 at the Darlington New Nuclear Project (Clarington, Ontario), find the hotspots, and size what C1 would save. The study follows the goal-and-scope principles of ISO 14040/14044 [TODO: source needed: ISO 14040:2006 and ISO 14044:2006 entries in sources.md]. It is a screening study and has not been critically reviewed, so it cannot support a public comparative claim.

- **Functional unit:** 1 MWh of net electricity delivered at the plant's grid connection. Results in kg CO₂e/MWh equal the g CO₂e/kWh used in the literature.
- **Reference flow:** one unit over its design life: 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh**, the same denominator as §7. The 60-year life is from the regulator (Canadian Nuclear Safety Commission, 2024) [TO VERIFY]; net output and capacity factor are placeholders for Leroy's plant data [TODO], and the 315 MW net in an OPG filing [TO VERIFY] is carried in the uncertainty analysis.
- **System boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are built bottom-up from process data. Operation and maintenance (O&M), decommissioning and the back end are per-kWh values transferred from EDF's French-fleet LCA (EDF R&D, 2024) [TO VERIFY]. It is therefore a **process-based LCA with three stages taken from secondary per-kWh data**.
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, upstream supply of the natural gas used for conversion heat (combustion CO₂ only), fuel-plant capital goods, grid transmission and recycling credits. Each biases the result low (§6.5). End of life follows the cut-off (recycled-content) approach: steel carries the burden of its scrap input, with no credit for future recycling.
- **Impact category:** climate change, characterised as GWP100 (IPCC AR5 where stated). The cement declaration uses AR5 factors (Cement Association of Canada, 2022) [TO VERIFY]; the US grid factors are CO₂ only (US EPA, 2024) [TO VERIFY]; the basis of the other factors is [TO VERIFY]. For mostly fossil CO₂ the choice matters far less than the input ranges.

**Method.** The rubric accepts an eco-audit "or equivalent analysis". Ours is an **equivalent analysis built from published factors**: a reproducible Python model multiplies material and fuel quantities by published emission factors (working in Appendices A and C). **No Granta EduPack run has been done, and no number here comes from Granta**; a cross-check of the C1 target structures is set up for the team's machines (Appendix A9) [TODO: results pending]. With no BWRX-300 bill of materials available, **plant quantities are scaled from per-MWe data for related reactors, not measured** (§6.2). Table T6 lists the key assumptions.

*Table T6. Key assumptions for one BWRX-300 at Darlington (all 40 ranged inputs in Appendix C2).*
*Source: `03_LCA_Calculations/parameters_lca.yaml`; references as listed. All values [TO VERIFY] unless marked as an assumption or placeholder. Ranges are model input bounds, not result intervals.*

| Parameter | Central (input range) | Basis |
|---|---|---|
| Net output; capacity factor; design life | 300 MWe (300–315); 0.90 (0.80–0.95); 60 years (40–80) | GE Vernova Hitachi Nuclear Energy (n.d.); placeholder; Canadian Nuclear Safety Commission (2024) |
| Whole-plant concrete; steel | 69 m³/MWe (34.5–138); 33 t/MWe (16.5–46) | ESBWR and ABWR (Peterson, Zhao and Petroski, 2005); vendor claim as low bound (GE Vernova, n.d.) |
| DPSC infill thickness: basemat; shaft wall | 3.0 m (2–4); 1.5 m (1–2) | Assumption (no source found) |
| Binder: DPSC self-consolidating infill; other concrete | 450 kg/m³ (400–550); 350 kg/m³ (300–420) | EFNARC (2005), read via a 2024 secondary, with central and high assumed; assumption |
| General-use cement | 854 kg CO₂e/t (796–898, regional spread West–East) | Cement Association of Canada (2022); which region covers Ontario [TO VERIFY] |
| LC3 binder cut vs general-use cement | 37% (30–43%) | Median of five published estimates (Appendix A5) |
| Slag cement | 146.6 kg CO₂e/t (93.4–146.6) | Slag Cement Association (n.d.) |
| Rebar (electric-arc furnace); plate and equipment steel | 0.97 t/t (0.89–1.99); 1.73 t/t (1.22–2.50) | Concrete Reinforcing Steel Institute (2017) [superseded by a 2022 EPD, TO VERIFY]; American Institute of Steel Construction (2022) (Buy Clean California limit, used as a proxy) |
| Other construction materials and site energy | +50% of bulk materials (25–150%) | Assumption |
| Mining and milling | 42 kg CO₂e/kg U₃O₈ (24–81) | Parker, McNaughton and Sparrow (2016) |
| Conversion heat; centrifuge enrichment | 26 kWh/kg U (26–665); 50 kWh/SWU (40–100) | Gibon and Hahn Menacho (2023) |
| Enrichment; burnup | 3.8% U-235 (3.4–4.95); 45 GWd/t (35–55) | [TODO: authors] (2025), unrefereed preprint; assumption (both placeholders) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh (×0.5 to ×2; decommissioning ×3) | EDF R&D (2024) stage shares as reported by secondary sources; back end by difference |

[Figure F1. LCA system boundary for one BWRX-300 at Darlington: bottom-up fuel front end and construction materials, literature values for operation, decommissioning and the back end, and the C1 target structures. | Source: this study. | File: 03_LCA_Calculations/results/F1_system_boundary.png]

### 6.2 Baseline inventory and hotspots

**Quantities.** Whole-plant concrete and steel are per-MWe intensities × 300 MWe. The central case uses the ESBWR, the larger design the BWRX-300 is derived from: 69 m³ of concrete and 33 t of steel per MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY]. Sources point in opposite directions for an SMR. GE Vernova (n.d.) [TO VERIFY] claims about 50% less concrete per unit of energy than the ESBWR, while small plants usually lose economies of scale. We take the vendor claim as the low input bound and the ABWR (138 m³/MWe) as the high input bound, and assume the two effects cancel in the central case. That gives **20,700 m³ of concrete and 9,900 t of steel per unit**; across the Monte Carlo the whole-plant concrete has a **90% interval of about 15,050–36,521 m³** (Appendix C4). Of the central volume, **13,100 m³ is in the C1 target structures**: the forebay shaft (4,000 m³ placed so far, a floor; Ontario Power Generation, 2025) [TO VERIFY] and the diaphragm-plate steel-composite (DPSC) infill of the reactor-building basemat and shaft walls (9,081 m³). The DPSC volume is a geometric estimate from a 37 m module diameter and 35 m shaft depth, with assumed thicknesses. **Those two dimensions rest on a news report of the Unit 1 basemat-module lift, attributed to an OPG story we have not found (Ontario Power Generation, 2026) [TO VERIFY]**, yet they set 69% of the C1 target concrete.

**Resource use (per unit).** Concrete is 69 m³/MWe (0.35 kg/MWh) and steel 33 t/MWe (0.070 kg/MWh). The fuel needs 20.7 g of natural uranium, 2.69 g of enriched uranium and 0.0146 separative work units (SWU) per MWh, at a net efficiency of 34.5% (300 MWe from 870 MWt; [TODO: authors], 2025) [TO VERIFY]. Four units need about 196 t of natural uranium and 138 tSWU a year, the demand against which §8.3 should size supply risk [TODO: §8.3 to use these figures].

**Hotspots (Figure F2).** On the expected (Monte Carlo mean) basis:
1. **Mining and milling: 1.26 g/kWh (29%).** This is already low because Saskatchewan ores are high-grade (Parker, McNaughton and Sparrow, 2016) [TO VERIFY]; that Darlington's uranium is Canadian is [TO VERIFY].
2. **Conversion: 1.09 g/kWh (26%).** This is an *uncertainty* hotspot, not a measured one. Published heat demand spans 26–665 kWh per kg of uranium (Gibon and Hahn Menacho, 2023) [TO VERIFY]; at the most likely value conversion is only 0.13 g/kWh.
3. **Back end: 0.65 g/kWh (15%),** transferred from France, which reprocesses. Canada plans direct disposal [TODO: source needed: NWMO], so this may be an overestimate.

The fuel front end is 64% of the total and construction about 7.5%. Within construction, steel emits about twice what concrete does (14,800 vs 7,600 t CO₂e per unit, mode case); Geneski, McKellar and Atkinson (n.d.) [TO VERIFY] also found that steel exceeds concrete. Concrete is 1.5% of the expected total, and the C1 target concrete 1.3% of the mode-case total. **C1 therefore acts on roughly one-hundredth of the footprint**, which caps what any concrete change can achieve.

[Figure F2. Life-cycle emissions of one BWRX-300 by stage: expected 4.3 g CO₂e/kWh (Monte Carlo mean), with the mode case (every input at its most likely value; total 2.7) marked. | Source: this study, scripts/lca_uncertainty.py; inputs in parameters_lca.yaml [TO VERIFY]. | File: 03_LCA_Calculations/results/F2_stage_breakdown.png]

### 6.3 The initiative against the baseline

**LC3 saves about 1,740 t CO₂e per unit (Monte Carlo median; 90% interval 1,390–2,150 t) and about 5,200 t across Units 2–4 (4,160–6,460 t), avoiding about 6,900 t of clinker** (Table T8). It cuts the target structures' concrete emissions by 34%. Most of the saving (1,291 t) is in the DPSC infill, because the design calls for self-consolidating concrete (GE-Hitachi Nuclear Energy, 2024) [TO VERIFY], a cement-rich mix (450 kg binder/m³ assumed). Only Units 2–4 are counted, because Unit 1's basemat is placed and its forebay is partly placed (4,000 m³ so far). Whether Unit 1's shaft-wall infill is still to be poured, and so could use LC3, is [TO VERIFY].

*Table T8. Savings against the baseline (S0, general-use cement), per unit and for Units 2–4. Every column except the bracketed interval is on the mode-case basis (every input at its most likely value).*
*Source: this study, `results/lca_scenarios.csv` and `lca_montecarlo_summary.csv` (Appendices A6 and C4). Inputs [TO VERIFY].*

| Scenario | t CO₂e saved per unit, mode case (MC 5th–95th percentile) | Units 2–4, t CO₂e | Clinker avoided, t per unit / Units 2–4 | Share of one unit's life cycle |
|---|---|---|---|---|
| S1 Slag cement, 40% of binder, in target structures | 1,552 (1,205–2,113) | 4,657 | 2,019 / 6,057 | 0.41% |
| **S2 LC3-50 in target structures (C1)** | **1,734 (1,387–2,153)** | **5,201** | **2,304 / 6,913** | **0.45%** |
| S2b LC3 in targets plus slag in all other concrete | 2,488 | 7,464 | 3,286 / 9,857 | 0.65% |
| S3 sensitivity: all steel at electric-arc-furnace factors | 3,714 | 11,142 | — | 0.97% |
| S3 sensitivity: all steel at world-average factors | −8,399 (adds emissions) | −25,198 | — | −2.19% |

*Note: shares are each saving divided by the mode-case life-cycle total (383,243 t CO₂e per unit). On the Monte Carlo basis the savings have medians of 1,742 t (LC3) and 1,642 t (slag), and LC3's share has a median of 0.29% (0.18–0.46%), lower because the total grows while the saving barely moves (§6.4). Monte Carlo shares for S1, S2b and S3 are not in the model outputs [TODO: lca-analyst to add them to `lca_montecarlo_summary.csv`].*

Five findings follow, each with a consequence for the initiative.
1. **C1 targets the right structures.** Concrete is about 66% of their known embodied emissions (5,078 t, against 2,619 t for the forebay rebar and DPSC basemat steel), and the saving exceeds the largest geometric uncertainty in it (530 t, wall thickness).
2. **The saving is small at plant scale:** about 0.3% of a unit's life cycle (0.45% in the mode case), or about 0.01 g/kWh. C1 does not change the plant's climate case. Its cost has not been estimated [TODO: abatement cost, §8.2], so it is worth pursuing only as a cut that can be qualified without delay (finding 5).
3. **Slag nearly matches LC3.** The difference is 180 t per unit in the mode case and 97 t at the Monte Carlo median (90% interval −343 to +574 t), and **LC3 saves more in only 64% of draws**, so on carbon the two cannot be separated. Slag blends already have precedent in nuclear concrete ([TODO: authors], 2026) [TO VERIFY], which makes slag (S1) the fallback if LC3 cannot be qualified in time (§8.1). A shrinking Ontario slag supply would favour LC3, but that risk is unsourced [TODO: source needed: Ontario blast-furnace-to-electric-arc conversions].
4. **Steel is the bigger construction lever.** Steel at electric-arc-furnace factors saves 3,710 t per unit (mode case), about twice LC3; world-average steel would add 8,400 t. Specifying lower-carbon steel (C2, §10) deserves at least equal priority.
5. **Schedule dominates.** On the schedule-value results used in §7, a delay of 10–15 days to one of Units 2–4 (Ontario average grid trajectory), or about 1.4 days (marginal grid, declining), would cancel that unit's LC3 saving [TODO: Appendix B working for schedule value]. C1 is worth adopting only if it is schedule-neutral, for example by qualifying the mix on mock-ups during Unit 1 construction (§8.6).

For the triple-bottom-line evaluation (§9), C1 is environmentally positive but marginal, and its feasibility hinges on qualification and schedule rather than on carbon.

### 6.4 Uncertainty: tornado and Monte Carlo

The tornado moves each of 40 ranged inputs to its low and high value in turn; the Monte Carlo draws all 40 together, 20,000 times (set-up in Appendix C).

**The life-cycle total depends on the fuel inputs, not the concrete (Figure F3).** The largest swings are conversion heat (2.70 → 5.37 g/kWh), the mining factor (2.26 → 3.65), the back end (2.42 → 3.25), burnup (3.12 at 35 GWd/t → 2.44 at 55) and enrichment level (2.53 → 3.19). No concrete input moves the total by more than 0.07 g/kWh; steel intensity moves it by 0.17. **The LC3 saving depends on the geometry and the mix**: the LC3 emission cut (1,406 → 2,015 t), DPSC wall thickness (1,464 → 1,995 t), infill binder content (1,590 → 2,021 t), and any extra binder LC3 needs to flow (10% more cuts the saving to 1,438 t). OPG's drawings and mock-up trials would narrow all four.

[Figure F3. One-at-a-time sensitivity of the life-cycle intensity (left, central 2.70 g CO₂e/kWh) and of the LC3 saving per unit (right, central 1,734 t), top ten inputs each. | Source: this study, scripts/lca_uncertainty.py; ranges in parameters_lca.yaml. | File: 03_LCA_Calculations/results/F3_tornado.png]

**Monte Carlo (Figure F4): why the median (4.2) sits above the mode case (2.7).** The life-cycle median is 4.2 g CO₂e/kWh (mean 4.3; 5th–95th percentile 3.0–5.8) and the LC3 saving median 1,740 t per unit (1,390–2,150 t). The mode case sets every input to its most likely value, but several inputs are right-skewed: conversion heat is most likely 26 kWh/kg U but could be 665, which alone raises the expected total by about 1.0 g/kWh (Appendix C5). We report the median because the inputs we know least about can mostly push the result up; the same skew lowers LC3's share from 0.45% (mode case) to 0.29% (median).

**Limitations.** Inputs are drawn independently, some ranges are our judgement and the triangular shape is a convention (Appendix C6); a measured conversion value [TODO: source needed: Cameco Port Hope facility emissions and output] would remove the largest uncertainty.

[Figure F4. Monte Carlo distributions (20,000 draws, seed 20261021) of the life-cycle intensity (median 4.18, 5th–95th percentile 3.05–5.85 g CO₂e/kWh) and of the LC3 saving per unit (median 1,742, 1,387–2,153 t). | Source: this study, scripts/lca_uncertainty.py. | File: 03_LCA_Calculations/results/F4_montecarlo.png]

### 6.5 Comparison with published values

**Our median is just below UNECE's 5.1–6.4 g/kWh (United Nations Economic Commission for Europe, 2021; our 90% interval overlaps it) and at the low end of the wider literature range, for reasons we can identify (Figure F5, Table T9).** It overlaps EDF's French fleet (3.7 g/kWh; EDF R&D, 2024) and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016) and the harmonised light-water-reactor median of 12 (Warner and Heath, 2012). Our expected front end (2.7 g/kWh) is close to the 3.0 found for the US nuclear fuel cycle (Ng et al., 2025), if that figure covers the front end only [TO VERIFY: scope]. All benchmark values are [TO VERIFY]. Our median is about 100–120 times lower than gas combined cycle (403–513) and 180–260 times lower than coal (751–1,095) (United Nations Economic Commission for Europe, 2021).

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

The sources disagree mainly about the fuel front end (ore grade, enrichment technology and grid), not about construction, and that is where our result departs from them. The known low bias (cut-offs, possibly construction) would raise the total, which would make C1's share smaller still, so it does not weaken the conclusion of §6.3. If the Granta cross-check is run [TODO: results pending], its construction values will be compared here with the model's (Appendix A9).

[Figure F5. Our BWRX-300 result against published nuclear life-cycle values (point = central or median; line = range or interval); coal about 750–1,100 and gas combined cycle 403–513 g CO₂e/kWh for scale. UNECE reports a range only: its point at 5.8 is our midpoint, not a UNECE value. | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012). Benchmarks [TO VERIFY]. | File: 03_LCA_Calculations/results/F5_benchmarks.png] [TODO: lca-analyst to redraw UNECE as a range only, and to drop any 3.7 minimum attributed to Warner and Heath (factcheck L31, L66)]

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: life-cycle intensity with a 90% interval, stage hotspots, savings per structure, per unit and for Units 2–4, clinker avoided, fuel demand; headline values now on one basis. Missing: verified inputs (every factor is a search lead).
- **R2.2 (eco-audit or equivalent).** Produced: an equivalent analysis, labelled as a screening LCA following ISO 14040/44 principles, not critically reviewed, covering the whole life cycle. Missing: the Granta EduPack cross-check [TODO: results pending]; until it exists R2.2 rests on "equivalent analysis" only.
- **R2.3 (resources and benefits sized to the proposal).** Produced: m³/MWe, t/MWe, kg/MWh, g U and SWU per MWh, net efficiency, t CO₂e and t clinker for Darlington Units 2–4. Missing: the economic benefit (abatement cost, §8.2); §8.3 does not yet use the fuel demand; sourced plant data from Leroy.
- **R2.4 (methods clear, working in appendix).** Produced: method stated in §6.1, full working in Appendices A and C, scripts reproducible. Missing: §2 methods paragraph.
- **R2.5 (assumptions, scope, functional unit).** Produced: FU, reference flow, boundary (F1), cut-offs including upstream gas, end-of-life approach, impact category, Table T6 with input bounds labelled. Missing: ISO 14040/14044 reference; GWP basis of most factors.
- **R2.6 (logical, justified).** Produced: five findings, each tied to a consequence for C1; T8 on one basis, so the LC3-vs-slag comparison is no longer contradicted by the share column; the unsourced cost and slag-supply premises are removed or flagged. Missing: nothing structural.
- **R2.7 and RB.6 (uncertainty; literature comparison).** Produced: tornado, Monte Carlo, limitations, seven reasons for discrepancies with sign and size, one consistent UNECE wording. Missing: verified benchmark values; the F5 redraw (UNECE as a range); IPCC AR5 not used because no value has been confirmed.
- **R1.3 (synthesis).** Produced: vendor claim vs scale penalty on quantities; Parker vs Gibon on ore grade; EDF vs our construction; Carless on SMR vs large reactor; Geneski on steel vs concrete (direction only). Missing: verification.
- **RB.5.** Produced: results summarised here, full calculations in Appendices A and C.

### Remaining TODOs

1. **[TO VERIFY, blocking HD]** Open the LCA primaries in the priority order of `02_Research/sources_lca.md`: Gibon and Hahn Menacho 2023 (conversion heat 26–665); Parker et al. 2016; EDF R&D 2024 (stage shares; whether "downstream" includes reprocessing); **the OPG basemat story or NEDO-33926 dimensions (37 m, 35 m; currently a news report)**; the CAC 2022 EPD and which region is Ontario (or the St Marys Bowmanville EPD); the five LC3 estimates; Peterson et al. 2005; the CRSI 2022 EPD; UNECE 2021 and one title for it; then the other benchmarks (Warner and Heath's minimum; Ng et al.'s scope). Set `status: verified`, re-run the three `lca_*.py` scripts and update every number here.
2. **[TODO: results pending]** Granta EduPack Eco Audit cross-check on a team machine (`results/granta_inputs.md`, under one hour). If run, add the EduPack version, database and date to §6.1 and the comparison to §6.5 and Appendix A9; if not, cut those sentences.
3. **[TODO: Leroy]** Net MWe (300 or 315), capacity factor, design life (60 or 65 years), burnup, enrichment, uranium origin and enricher; whole-plant concrete and steel quantities (OPG EIS review report; TVA Clinch River ER; NEDO-33926 for DPSC thicknesses; is the forebay per unit or shared?); whether Unit 1's shaft-wall infill is still to be poured.
4. **[TODO: source needed]** ISO 14040:2006 and ISO 14044:2006 entries in `sources.md`; Cameco Port Hope facility emissions (conversion); NWMO for Canada's direct-disposal plan; Ontario blast-furnace-to-electric-arc conversions (finding 3); the authors of the arXiv overview (2025) and of the 2026 nuclear-concrete paper (R5.4: no Harvard citation without an author).
5. **[TODO: abatement cost]** C1's cost per tonne of CO₂e (§8.2), needed for the economic half of R2.3.
6. **[TODO: lca-analyst]** Add Monte Carlo life-cycle shares for S1, S2b and S3 to `lca_montecarlo_summary.csv` (T8 note); redraw F5 with UNECE as a range only (L66) and check the Warner and Heath minimum on the figure (L31); correct `results/lca.md` §7 (L64).
7. **[TODO: references]** Disambiguate Ontario Power Generation (2025) (forebay update vs Q1 results vs OEB filing) and (2026) (basemat story vs Q1 2026) with letter suffixes; the basemat story's exact URL.
8. **[TODO: Appendix B]** Schedule-value working (`results/schedule_value.md`) is cited in finding 5 but not yet in Appendix B.
9. **[TODO: §8.3]** Use the four-unit fuel demand (196 t U and 138 tSWU a year) in §8.3 (L58; closes an R2.3 gap).
10. **[Deck, Victor]** Slides 5–8 must match this version: concrete range 15,000–36,500 m³ (L67), no Granta claim (L70), "screening LCA following ISO 14040/44 principles, not critically reviewed" (L71), "just below UNECE's range" (L56).
