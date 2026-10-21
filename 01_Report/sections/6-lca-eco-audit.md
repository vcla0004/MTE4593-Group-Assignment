Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3 (also supports R4.2, R4.4, RB.8, R5.2)

<!--
CHANGELOG
- v1, 21/10/2026 (writer, for Victor, who took over Sam's red sections on 21/10; CLAUDE.md). First draft from `03_LCA_Calculations/results/lca.md`, `lca_baseline.md`, `lca_scenarios.md`, `lca_uncertainty.md`, `parameters_lca.yaml`, `granta_inputs.md`, `schedule_value.md`, `02_Research/sources_lca.md`, `sources.md` and `briefs/benchmarks-for-sam.md`. Sam's files are untouched.
  - review.md "For Sam" items 1–4 (Clarington; TBM volume; sheet; forebay rows partial): applied in `Accounting_corrected.csv` by the lca-analyst and shown in Appendix A4. §6.1 and §6.2 say the quantities are scaled, not measured.
  - review.md "Feedback to Sam" (front-end share): §6.2 now gives our own result (fuel front end 64% of the expected total), which §8.3 TODO 3 can cite instead of the unsourced UNECE sentence.
  - factcheck.md S16 (LC3, not "ash-concrete"), S17 (quantities scaled from per-MWe data, not from the forebay), S18 (placeholders now filled from the model), section E (our value now benchmarked, RB.6), S15/S20 (the infill is specified through GEH NEDO-33926, not CSA N287).
  - Honesty points from the coordinator's brief (R2.7, R4.4): equivalent analysis, not a Granta run; Granta cross-check marked [TODO: results pending]; quantities scaled; LC3 about 0.3%; slag nearly matches (LC3 wins 64% of draws); steel saves about 2x; median 4.2 above mode case 2.7 explained.
  - One correction to `lca.md` §7: it says every construction-quantity input moves the total by under 0.07 g/kWh. That holds for the concrete inputs only; steel intensity moves it by 0.17 g/kWh (`lca_uncertainty.md`). §6.4 says so.
- Presentation items: R5.1 (section and each subsection lead with the result); R5.2 (Figures F1–F5 and Tables T6, T8, T9, each captioned and sourced; caption above tables per review.md); R5.3 (about 1,800 words of body text excluding tables, captions and markers, about 3.6 pages at 500 words a page, against a 3.5-page budget; if the integrated report runs long, cut the "Limitations" paragraph of §6.4 to one sentence and fold "Resource use" into Table T8); R5.4 (Harvard, author forms as in sources_lca.md); R5.5 (Australian English).
- Table IDs T8 and T9 are new (T1–T7 are taken in plan §3 and §8.1). Leroy renumbers at integration.
-->

## 6 Life-cycle assessment and eco-audit

One BWRX-300 at Darlington is estimated to emit **about 4.2 kg CO₂e per MWh delivered (90% interval 3.0–5.8)**, at or just below the published range for nuclear power. Nearly two-thirds of that comes from the fuel front end; construction is about 7%. Using LC3 concrete in the targeted structures (initiative C1, §4.3) would save **about 1,730 t CO₂e per unit and 5,200 t across Units 2–4**, or **about 0.3% of each unit's life-cycle footprint**. That saving is real but small. A slag blend saves nearly as much, and lower-carbon steel saves about twice as much. Every input is a published value not yet checked in its primary source [TO VERIFY], so every number in this section is provisional.

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of electricity from one BWRX-300 at the Darlington New Nuclear Project (Clarington, Ontario), find the hotspots, and size what C1 would save. We follow the goal-and-scope structure of ISO 14040/14044 [TODO: source needed: ISO 14040:2006 and ISO 14044:2006 entries in sources.md], without the critical review that a public comparative claim would need.

- **Functional unit:** 1 MWh of net electricity delivered at the plant's grid connection. Results in kg CO₂e/MWh equal the g CO₂e/kWh used in the literature.
- **Reference flow:** one unit over its design life: 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh**, the same denominator as §7. The 60-year life is from the regulator (Canadian Nuclear Safety Commission, 2024) [TO VERIFY]; net output and capacity factor are placeholders for Leroy's plant data [TODO], and the 315 MW net in an OPG filing [TO VERIFY] is carried in the uncertainty analysis.
- **System boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are built bottom-up; operation and maintenance, decommissioning and the back end are per-kWh values transferred from EDF's French-fleet LCA (EDF R&D, 2024) [TO VERIFY]. This makes it a **hybrid LCA**.
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, fuel-plant capital goods, grid transmission and recycling credits, each biasing the result low (§6.5). End of life follows the cut-off (recycled-content) approach: steel carries the burden of its scrap input, with no credit for future recycling.
- **Impact method:** GWP100. The cement declaration uses IPCC AR5 factors (Cement Association of Canada, 2022) [TO VERIFY]; the other factors' basis is [TO VERIFY], but for mostly fossil CO₂ the choice matters far less than the input ranges.

**Method.** The rubric accepts an eco-audit "or equivalent analysis". Ours is an **equivalent analysis built from published factors, not a Granta EduPack run**: a reproducible Python model multiplies material and fuel quantities by published emission factors (working in Appendices A and C). A Granta EduPack Eco Audit cross-check of the C1 target structures [TODO: results pending] is set up (Appendix A9); no number here comes from Granta. With no BWRX-300 bill of materials available, **plant quantities are scaled from per-MWe data for related reactors, not measured** (§6.2). Table T6 lists the key assumptions.

*Table T6. Key assumptions for one BWRX-300 at Darlington (all 40 ranged inputs in Appendix C2).*
*Source: `03_LCA_Calculations/parameters_lca.yaml`; references as listed. All values [TO VERIFY] unless marked as an assumption or placeholder.*

| Parameter | Central (range) | Basis |
|---|---|---|
| Net output; capacity factor; design life | 300 MWe (300–315); 0.90 (0.80–0.95); 60 years (40–80) | GE Vernova Hitachi Nuclear Energy (n.d.); placeholder; Canadian Nuclear Safety Commission (2024) |
| Whole-plant concrete; steel | 69 m³/MWe (34.5–138); 33 t/MWe (16.5–46) | ESBWR and ABWR (Peterson, Zhao and Petroski, 2005); vendor claim as low bound (GE Vernova, n.d.) |
| DPSC infill thickness: basemat; shaft wall | 3.0 m (2–4); 1.5 m (1–2) | Assumption (no source found) |
| Binder: DPSC self-consolidating infill; other concrete | 450 kg/m³ (400–550); 350 kg/m³ (300–420) | EFNARC (2005); assumption |
| General-use cement | 854 kg CO₂e/t (796–898) | Cement Association of Canada (2022) |
| LC3 binder cut vs general-use cement | 37% (30–43%) | Median of five published estimates (Appendix A5) |
| Slag cement | 146.6 kg CO₂e/t (93.4–146.6) | Slag Cement Association (n.d.) |
| Rebar (electric-arc furnace); plate and equipment steel | 0.97 t/t (0.89–1.99); 1.73 t/t (1.22–2.50) | Concrete Reinforcing Steel Institute (2017); American Institute of Steel Construction (2022) |
| Other construction materials and site energy | +50% of bulk materials (25–150%) | Assumption |
| Mining and milling | 42 kg CO₂e/kg U₃O₈ (24–81) | Parker, McNaughton and Sparrow (2016) |
| Conversion heat; centrifuge enrichment | 26 kWh/kg U (26–665); 50 kWh/SWU (40–100) | Gibon and Hahn Menacho (2023) |
| Enrichment; burnup | 3.8% U-235 (3.4–4.95); 45 GWd/t (35–55) | [TODO: authors] (2025); assumption (both placeholders) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh (×0.5 to ×2; decommissioning ×3) | EDF R&D (2024) stage shares |

[Figure F1. LCA system boundary for one BWRX-300 at Darlington: bottom-up fuel front end and construction materials, literature values for operation, decommissioning and the back end, and the C1 target structures. | Source: this study. | File: 03_LCA_Calculations/results/F1_system_boundary.png]

### 6.2 Baseline inventory and hotspots

**Quantities.** Whole-plant concrete and steel are per-MWe intensities × 300 MWe. The central case uses the ESBWR, the larger design the BWRX-300 is derived from: 69 m³ of concrete and 33 t of steel per MWe (Peterson, Zhao and Petroski, 2005) [TO VERIFY]. Sources point in opposite directions for an SMR. GE Vernova (n.d.) [TO VERIFY] claims about 50% less concrete per unit of energy than the ESBWR, while small plants usually lose economies of scale. We take the vendor claim as the low bound and the ABWR (138 m³/MWe) as the high bound, and assume the two effects cancel in the central case. That gives **20,700 m³ of concrete and 9,900 t of steel per unit**. Of this, **13,100 m³ is in the C1 target structures**: the forebay shaft (4,000 m³ placed so far, a floor; Ontario Power Generation, 2025) [TO VERIFY] and the diaphragm-plate steel-composite (DPSC) infill of the reactor-building basemat and shaft walls (9,081 m³). The DPSC volume is a geometric estimate from the 37 m module diameter and 35 m shaft depth (Ontario Power Generation, 2026) [TO VERIFY], with assumed thicknesses.

**Resource use (per unit).** Concrete is 69 m³/MWe (0.35 kg/MWh) and steel 33 t/MWe (0.070 kg/MWh). The fuel needs 20.7 g of natural uranium, 2.69 g of enriched uranium and 0.0146 separative work units (SWU) per MWh, at a net efficiency of 34.5% (300 MWe from 870 MWt; [TODO: authors], 2025) [TO VERIFY]. Four units need about 196 t of natural uranium and 138 tSWU a year, the demand against which §8.3 judges supply risk.

**Hotspots (Figure F2).** On the expected (Monte Carlo mean) basis:
1. **Mining and milling: 1.26 g/kWh (29%).** This is already low because Saskatchewan ores are high-grade (Parker, McNaughton and Sparrow, 2016) [TO VERIFY]; that Darlington's uranium is Canadian is [TO VERIFY].
2. **Conversion: 1.09 g/kWh (26%).** This is an *uncertainty* hotspot, not a measured one. Published heat demand spans 26–665 kWh per kg of uranium (Gibon and Hahn Menacho, 2023) [TO VERIFY]; at the most likely value conversion is only 0.13 g/kWh.
3. **Back end: 0.65 g/kWh (15%),** transferred from France, which reprocesses. Canada plans direct disposal [TODO: source needed: NWMO], so this may be an overestimate.

The fuel front end is 64% of the total and construction about 7%. Within construction, steel emits about twice what concrete does (14,800 vs 7,600 t CO₂e per unit), as Geneski, McKellar and Atkinson (n.d.) [TO VERIFY] also found. Concrete is 1.5% of the expected total, and the C1 target concrete 1.3% of the mode-case total. **C1 therefore acts on roughly one-hundredth of the footprint**, which caps what any concrete change can achieve.

[Figure F2. Life-cycle emissions of one BWRX-300 by stage: expected 4.3 g CO₂e/kWh (Monte Carlo mean), with the mode case (every input at its most likely value; total 2.7) marked. | Source: this study, scripts/lca_uncertainty.py; inputs in parameters_lca.yaml [TO VERIFY]. | File: 03_LCA_Calculations/results/F2_stage_breakdown.png]

### 6.3 The initiative against the baseline

**LC3 saves about 1,730 t CO₂e per unit (90% interval 1,390–2,150 t) and 5,200 t across Units 2–4 (4,160–6,460 t), avoiding 6,900 t of clinker** (Table T8). It cuts the target structures' concrete emissions by 34%. Most of the saving (1,291 t) is in the DPSC infill, because the design calls for self-consolidating concrete (GE-Hitachi Nuclear Energy, 2024) [TO VERIFY], a cement-rich mix (450 kg binder/m³ assumed). Units 2–4 only are counted, because Unit 1's basemat and forebay are already placed.

*Table T8. Savings against the baseline (S0, general-use cement), per unit and for Units 2–4.*
*Source: this study, scripts/lca_scenarios.py and lca_uncertainty.py (Appendices A6 and C4). Inputs [TO VERIFY].*

| Scenario | t CO₂e saved per unit (MC 5th–95th percentile) | Units 2–4, t CO₂e | Clinker avoided, t per unit / Units 2–4 | Share of one unit's life cycle |
|---|---|---|---|---|
| S1 Slag cement, 40% of binder, in target structures | 1,552 (1,205–2,113) | 4,657 | 2,019 / 6,057 | 0.41% (mode case) |
| **S2 LC3-50 in target structures (C1)** | **1,734 (1,387–2,153)** | **5,201** | **2,304 / 6,913** | **0.29% (MC median; 0.18–0.46%)** |
| S2b LC3 in targets plus slag in all other concrete | 2,488 | 7,464 | 3,286 / 9,857 | 0.65% (mode case) |
| S3 sensitivity: all steel at electric-arc-furnace factors | 3,714 | 11,142 | — | 0.97% (mode case) |
| S3 sensitivity: all steel at world-average factors | −8,399 (adds emissions) | −25,198 | — | −2.2% (mode case) |

Five findings follow, each with a consequence for the initiative.
1. **C1 targets the right structures.** Concrete is about 66% of their known embodied emissions (5,078 t, against 2,619 t for the forebay rebar and DPSC basemat steel), and the saving exceeds the largest geometric uncertainty in it (530 t, wall thickness).
2. **The saving is small at plant scale:** about 0.3% of a unit's life cycle, or 0.01 g/kWh. C1 does not change the plant's climate case; its value is as a low-cost cut and a first nuclear use of LC3.
3. **Slag nearly matches LC3.** The central difference is only 180 t per unit, and **LC3 saves more in only 64% of Monte Carlo draws**. Slag blends already have precedent in nuclear concrete ([TODO: authors], 2026) [TO VERIFY]. LC3's case therefore rests on the risk that Ontario's slag supply shrinks as steelmaking moves to electric-arc furnaces (§4.3) [TO VERIFY], not on a bigger saving. Slag (S1) is the fallback if LC3 cannot be qualified in time (§8.1).
4. **Steel is the bigger construction lever.** Steel at electric-arc-furnace factors saves 3,710 t per unit, about twice LC3; world-average steel would add 8,400 t. Specifying lower-carbon steel (C2, §10) deserves at least equal priority.
5. **Schedule dominates.** On the schedule-value results used in §7, a delay of 10–15 days to one of Units 2–4 (Ontario average grid trajectory), or about 1.4 days (marginal grid, declining), would cancel that unit's LC3 saving [TODO: Appendix B working for schedule value]. C1 is worth adopting only if it is schedule-neutral, for example by qualifying the mix on mock-ups during Unit 1 construction (§8.6).

For the triple-bottom-line evaluation (§9), C1 is environmentally positive but marginal, and its feasibility hinges on qualification and schedule rather than on carbon.

### 6.4 Uncertainty: tornado and Monte Carlo

The tornado moves each of 40 ranged inputs to its low and high value in turn; the Monte Carlo draws all 40 together, 20,000 times (set-up in Appendix C).

**The life-cycle total depends on the fuel inputs, not the concrete (Figure F3).** The largest swings are conversion heat (2.70 → 5.37 g/kWh), the mining factor (2.26 → 3.65), the back end (2.42 → 3.25), burnup (3.12 at 35 GWd/t → 2.44 at 55) and enrichment level (2.53 → 3.19). No concrete input moves the total by more than 0.07 g/kWh; steel intensity moves it by 0.17. **The LC3 saving depends on the geometry and the mix**: the LC3 emission cut (1,406 → 2,015 t), DPSC wall thickness (1,464 → 1,995 t), infill binder content (1,590 → 2,021 t), and any extra binder LC3 needs to flow (10% more cuts the saving to 1,438 t). OPG's drawings and mock-up trials would narrow all four.

[Figure F3. One-at-a-time sensitivity of the life-cycle intensity (left, central 2.70 g CO₂e/kWh) and of the LC3 saving per unit (right, central 1,734 t), top ten inputs each. | Source: this study, scripts/lca_uncertainty.py; ranges in parameters_lca.yaml. | File: 03_LCA_Calculations/results/F3_tornado.png]

**Monte Carlo (Figure F4).** The life-cycle intensity has a median of 4.2 g CO₂e/kWh (mean 4.3; 5th–95th percentile 3.0–5.8), and the LC3 saving a median of 1,740 t per unit (1,390–2,150 t).

**Why the median (4.2) sits above the mode case (2.7).** The mode case sets every input to its most likely value. Several inputs are right-skewed: conversion heat is most likely 26 kWh/kg U but could be as high as 665, so almost every draw lies above its mode. Conversion alone raises the expected total by about 1.0 g/kWh (1.09 against 0.13); mining (0.23) and the other skewed stages add the remaining 0.6. We report the median because the inputs we know least about can mostly push the result up. The same skew explains why LC3's share is 0.45% in the mode case but 0.29% at the median: the total grows while the saving barely moves.

**Limitations.** Inputs are drawn independently, although concrete and steel intensities are probably correlated (this would slightly widen the construction tail). Some ranges are our judgement (labelled in Appendix C2), and the triangular shape is a convention, not data. A measured conversion value [TODO: source needed: Cameco Port Hope facility emissions and output] would remove the largest uncertainty.

[Figure F4. Monte Carlo distributions (20,000 draws, seed 20261021) of the life-cycle intensity (median 4.18, 5th–95th percentile 3.05–5.85 g CO₂e/kWh) and of the LC3 saving per unit (median 1,742, 1,387–2,153 t). | Source: this study, scripts/lca_uncertainty.py. | File: 03_LCA_Calculations/results/F4_montecarlo.png]

### 6.5 Comparison with published values

**Our result sits inside the published range for nuclear power, at its low end, for reasons we can identify (Figure F5, Table T9).** It overlaps EDF's French fleet (3.7 g/kWh; EDF R&D, 2024), sits just below UNECE's 5.1–6.4 (United Nations Economic Commission for Europe, 2021) with overlapping intervals, and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016) and the harmonised light-water-reactor median of 12 (Warner and Heath, 2012). Our expected front end (2.7 g/kWh) is close to the 3.0 found for the US fuel cycle (Ng et al., 2025). All benchmark values are [TO VERIFY]. Our median is about 100–120 times lower than gas combined cycle (403–513) and 180–260 times lower than coal (751–1,095) (United Nations Economic Commission for Europe, 2021).

*Table T9. Why our result differs from the benchmarks: direction and size of each reason.*
*Source: this study (Appendices A and C), with the references as listed. All [TO VERIFY].*

| Reason | Effect on our value | Size |
|---|---|---|
| High-grade Canadian ore | Lower | Our mining is 1.0–1.3 g/kWh; at global-average grades Gibon and Hahn Menacho (2023) attribute 46% of 6.1, about 2.8 g/kWh, to it. This explains most of the gap to UNECE and Gibon |
| Centrifuge enrichment only | Lower than older studies | 50 kWh/SWU against about 2,500 for the diffusion plants in older study sets (Gibon and Hahn Menacho, 2023; Warner and Heath, 2012) |
| Energy-only fuel inventory (cut-offs) | Lower | Not quantified (chemicals, cladding, fuel-plant capital goods excluded) |
| Construction possibly underestimated | Lower | Ours 0.24–0.32 g/kWh against about 0.59 for large reactors (16% of 3.7; EDF R&D, 2024). At 0.6–1.0, the total would rise 0.3–0.7 g/kWh and LC3's share would fall further |
| Long life and high capacity factor | Lower | At 40 years instead of 60, the mode case rises from 2.70 to 2.82 g/kWh |
| O&M and back end transferred from France (reprocessing) | Possibly higher | Canada plans direct disposal; back-end range 0.28–1.11 g/kWh tested |
| SMR rather than large reactor | Small | Carless, Griffin and Fischbeck (2016) give 9.1 for an SMR against 8.4 for the AP1000, mainly through the fuel cycle; our construction share is too small for scale effects to move the total much |

The sources disagree mainly about the fuel front end (ore grade, enrichment technology and grid), not about construction, and that is where our result departs from them. The known low bias (cut-offs, possibly construction) would raise the total, which would make C1's share smaller still, so it does not weaken the conclusion of §6.3. The Granta cross-check [TODO: results pending] will be compared here with the model's construction values (Appendix A9).

[Figure F5. Our BWRX-300 result against published nuclear life-cycle values (point = central or median; line = range or interval); coal about 750–1,100 and gas combined cycle 403–513 g CO₂e/kWh for scale. | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012). Benchmarks [TO VERIFY]. | File: 03_LCA_Calculations/results/F5_benchmarks.png]

---

### IDs covered (towards the HD descriptor) and what is still missing

- **R2.1 (strong quantitative analysis).** Produced: life-cycle intensity with a 90% interval, stage hotspots, savings per structure, per unit and for Units 2–4, clinker avoided, fuel demand. Missing: verified inputs (every factor is a search lead).
- **R2.2 (eco-audit or equivalent).** Produced: an equivalent analysis, labelled as such, covering the whole life cycle. Missing: the Granta EduPack Eco Audit cross-check [TODO: results pending]; until it exists R2.2 rests on "equivalent analysis" only.
- **R2.3 (resources and benefits sized to the proposal).** Produced: m³/MWe, t/MWe, kg/MWh, g U and SWU per MWh, net efficiency, t CO₂e and t clinker for Darlington Units 2–4. Missing: the economic benefit (abatement cost, §8.2) and sourced plant data from Leroy.
- **R2.4 (methods clear, working in appendix).** Produced: method stated in §6.1, full working in Appendices A and C, scripts reproducible. Missing: §2 methods paragraph.
- **R2.5 (assumptions, scope, functional unit).** Produced: FU, reference flow, boundary (F1), cut-offs, end-of-life approach, GWP basis, Table T6. Missing: ISO 14040/14044 reference; GWP basis of most factors.
- **R2.6 (logical, justified).** Produced: five findings, each tied to a consequence for C1; the median-vs-mode explanation. Missing: nothing structural.
- **R2.7 and RB.6 (uncertainty; literature comparison).** Produced: tornado, Monte Carlo, limitations, seven reasons for discrepancies with sign and size. Missing: verified benchmark values; IPCC AR5 not used because no value has been confirmed.
- **R1.3 (synthesis).** Produced: vendor claim vs scale penalty on quantities; Parker vs Gibon on ore grade; EDF vs our construction; Carless on SMR vs large reactor; Geneski on steel vs concrete. Missing: verification.
- **RB.5.** Produced: results summarised here, full calculations in Appendices A and C.

### Remaining TODOs

1. **[TO VERIFY, blocking HD]** Open the LCA primaries in the priority order of `02_Research/sources_lca.md` (Gibon and Hahn Menacho 2023; Parker et al. 2016; EDF R&D 2024; CAC 2022 EPD and which region is Ontario; St Marys Bowmanville EPD; the five LC3 estimates; Peterson et al. 2005; CRSI EPD; then the benchmarks). Set `status: verified`, re-run the three `lca_*.py` scripts and update every number here.
2. **[TODO: results pending]** Granta EduPack Eco Audit cross-check on a team machine (`results/granta_inputs.md`, under one hour). Add the EduPack version, database and date to §6.1 and the comparison to §6.5 and Appendix A9.
3. **[TODO: Leroy]** Net MWe (300 or 315), capacity factor, design life (60 or 65 years), burnup, enrichment, uranium origin and enricher; and whole-plant concrete and steel quantities (OPG EIS review report; TVA Clinch River ER; NEDO-33926 for DPSC thicknesses; is the forebay per unit or shared?).
4. **[TODO: source needed]** ISO 14040:2006 and ISO 14044:2006 entries in `sources.md`; Cameco Port Hope facility emissions (conversion); NWMO for Canada's direct-disposal plan; the authors of the arXiv overview (2025) and of the 2026 nuclear-concrete paper (R5.4: no Harvard citation without an author).
5. **[TODO: references]** Disambiguate Ontario Power Generation (2025) (forebay update vs Q1 results vs OEB filing) and (2026) (basemat story vs Q1 2026) with letter suffixes; the basemat story's exact URL.
6. **[TODO: Appendix B]** Schedule-value working (`results/schedule_value.md`) is cited in finding 5 but not yet in Appendix B.
7. **[TO VERIFY]** Whether Ontario's slag supply depends on blast furnaces that are closing (finding 3); otherwise reduce it to a one-sentence risk.
8. **[Deck, Victor]** Slides 6–7 must not cite Granta until TODO 2 is done (`lca.md` §11).
