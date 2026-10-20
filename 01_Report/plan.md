Rubric coverage: all

# Report plan: MTE4593 Assignment 2, Small Modular Nuclear Reactors

Examiner, plan mode. Written Tuesday 20/10/2026. **Slide deck due Thursday 22/10/2026** (presentation in the week 11 workshop). **Report due Friday 23/10/2026.** Team: Victor, Sam, Leroy.

The standard is the official *Assignment 2 Report Marking Rubric 2026* (`00_Brief/rubric.md`, check IDs R1.1–R5.5 and RB.1–RB.8). It overrides everything else, including this plan.

**Legend.**
- `[R2.2, RB.6]` = the rubric checks an item serves.
- `PRES` = the slide deck and presentation (5% of the unit, outside the 25% report rubric).
- **MUST** = needed for HD and doable by Friday. **STRETCH** = only after every MUST has a draft (checked Thu 12:00).
- `[TO VERIFY]` = not checked.
- `[checked 20/10]` = seen in today's web search. The analyst or fact-checker still has to confirm it in the primary source before it goes in the report. Search snippets are never citations.

**Where we stand.** Nothing quantitative exists yet:
- The report is headings only.
- The LCA spreadsheet has two partial rows (forebay concrete and rebar) with no emission factors.
- `sources.md` and `parameters.yaml` are empty.
- The deck is a title slide (which still lists Aaron), three slides copied from the brief and an empty references slide.

Every R2 and R3 mark is still to be earned, and there are three days.

---

## 0. Decisions the team must make today (Tue 20 Oct, one 45-minute meeting) [all IDs]

| # | Decision | Examiner's recommendation | Who | Serves |
|---|---|---|---|---|
| D1 | The initiative | **C1**: LC3 low-clinker concrete for the steel-plate composite modules and below-grade shafts of Darlington Units 2–4 (§2). C2 becomes Sam's steel sensitivity run; C3 becomes discussion and future work | Team | RB.1, R4.1–R4.4, R2.3 |
| D2 | Thesis and working title | Thesis in §2.4. Working title, e.g. "Low-clinker concrete for Darlington's small modular reactors: what it saves, and what matters more" | Team | R1.2, R2.6, R4.3, R5.1 |
| D3 | LCA goal and scope | Functional unit (FU) = 1 MWh of net electricity delivered at the plant's grid connection by one BWRX-300 at Darlington. Boundary is cradle-to-grave, including the fuel cycle. Data are hybrid: Granta EduPack Eco Audit for the initiative structures, named literature for everything else. Impacts as GWP100 (IPCC AR5), to match the benchmarks [TO VERIFY each benchmark's basis]. Lifetime output = net MWe × 8,760 h × capacity factor × design life, each input sourced | Sam proposes, team accepts | R2.5, R2.4, R2.2 |
| D4 | Australian comparison site | **Liddell, NSW**, one of the seven coal sites in the Coalition's June 2024 plan [checked 20/10, secondary]. The plan proposed a large reactor there and SMRs only at Northern (SA) and Muja (WA) [checked 20/10, secondary], so say that we model a BWRX-300 at Liddell for comparability. It is in the NEM, so AEMO's ISP, the National Greenhouse Accounts Factors and GenCost all apply consistently. Loy Yang (brown coal) only as STRETCH | Victor | R4.3, R2.3, R3.5 |
| D5 | Scope freeze | Only the MUST list in §4. STRETCH work starts only if every MUST has a draft at the Thu 12:00 check | Team | R5.3, R1.5 |
| D6 | Owners and page budgets | As in §3. **RB.4 (materials from extraction to end-of-life) moves from Sam to Leroy (lead)**, with Sam checking that its stages match the LCA, so Sam can spend his time on the eco-audit | Team | all IDs |
| D7 | Integrator and single sources of truth | **Leroy** assembles the .docx (styles, captions, table of contents, reference list). Numbers come only from `03_LCA_Calculations/parameters.yaml`, references only from `02_Research/sources.md` (Harvard) | Team | R5.1, R5.4, R5.5, R2.4 |
| D8 | Slide deck | Outline and owners in §8. Submit **Thu by 15:00** so it doesn't collide with the report freeze | Team | PRES, R5.2 |
| D9 | Freeze and submission | Content freeze **Thu 21:00**. Report submitted **Fri by 15:00** (confirm the deadline time, T1) | Team | R5.1–R5.5 |
| D10 | AI-use declaration | Agree the wording under Monash's AI-use rules for this unit; insert it by Fri 11:00 | Team | Monash rule (no rubric ID) |
| D11 | Minutes | Write "Meeting 3 20_10_26" from the template: attendees, D1–D10 and actions. Neither earlier set of minutes lists Victor as attending. These minutes are teamwork evidence for the week 12 ITPmetrics moderation | Victor | teamwork evidence (no rubric ID) |

---

## 1. Where the marks are, and where the effort goes [all IDs]

| Criterion | Weight | Share of 25 | Earned mainly in | Main-text pages | Effort |
|---|---|---|---|---|---|
| R2 Quality of technical analysis | 8% | 32% | §5, §6, §7, Appendices A–C | 7.25 | About a third of team hours (mostly Sam, plus Victor's §7) |
| R3 Non-technical aspects | 6% | 24% | §8, §9 | 4.5 | About a quarter (Victor and agents) |
| R1 Research coverage | 5% | 20% | §3, §4.1–4.2, sources everywhere | 3.5 | About a fifth (Leroy, Victor) |
| R4 Originality and creativity | 3% | 12% | §4.3, §7, §10 | 1.5 | Decided today in D1 and D2 (framing), not by writing more |
| R5 Presentation | 3% | 12% | The whole report; §1, §11, figures | 1.5 | Thursday evening and Friday morning |

- R2 and R3 are 14 of the 25 marks. Nothing gets time for R1, R4 or R5 polish until §6, §7, §8 and §9 have drafts.
- The brief excludes figures and graphs from the 15–20 page limit [confirm, T2]. Put numbers in tables and charts: it saves text pages and earns R5.2.
- R5 is earned on Friday morning (cross-read, captions, references). Keep Friday free of new content.

---

## 2. The initiative [RB.1, RB.3, R4.1–R4.4, R2.3]

The brief rejects generic proposals, and R4.1 says outright that "build SMRs" or "use better steel" isn't enough. The rule for this sprint is to pick the initiative Sam can quantify fastest with the data he already has, which is the concrete one. Its originality therefore has to come from how it's framed (see "Why it isn't obvious").

### 2.1 Candidates, ranked

**C1 (recommended; team decision D1). LC3 infill for the steel-plate composite modules and shafts of Darlington Units 2–4.**

> "We propose that Ontario Power Generation specify limestone calcined clay cement (LC3) concrete (Scrivener et al., 2018) for the infill of the diaphragm-plate steel-composite (DPSC) reactor-building modules and for the forebay and condenser-cooling-water shafts of BWRX-300 Units 2–4 at the Darlington New Nuclear Project, Clarington, Ontario. That is about [TODO Sam: m³] of concrete per unit, with cement from St Marys Cement's Bowmanville plant, also in Clarington [TO VERIFY distance and LC3 capability]. It would cut embodied emissions by [TODO Sam: t CO₂e] across the three units."

- **Location:** Darlington New Nuclear Project, Clarington, Ontario. The proposal covers Units 2–4 only: Unit 1's forebay concrete and DPSC basemat are already in place.
  - Ontario approved construction of the first unit on 8 May 2025, with CAD 20.9 bn estimated for all four [checked 20/10, secondary].
  - The CNSC licence to construct covers one unit [checked 20/10].
  - Units 2–4 are reported for 2034–36 [TO VERIFY].
- **Scale:**
  - One forebay shaft took about 4,000 m³ of concrete (9.6 million kg) and about 1,000 t of rebar (OPG construction update quoted in `Assumptions.docx`).
  - Unit 1's DPSC basemat module weighed about 953 t (2.1 million lb), 37 m across, lowered 35 m down the reactor-building shaft [checked 20/10, OPG story; confirm].
  - Whole-structure quantities: [TODO Sam, §2.5 item 5].
- **Application:** infill of the DPSC basemat and shaft-wall modules; the forebay and condenser-cooling-water shafts.
- **Technology:** LC3 replaces about half the Portland clinker with calcined clay and limestone [TO VERIFY, Scrivener et al., 2018]. Two scenarios:
  - **S1, slag blend:** the near-term option. Slag blends are common in mass concrete; their use in nuclear safety-related concrete is [TO VERIFY]. Local emission factors come from the St Marys Bowmanville cement EPD (NRMCA, 2021) [checked 20/10: listing].
  - **S2, LC3:** the bigger saving, but it must qualify under Canada's nuclear concrete standards. The CSA N287 series has N287.1:24 current and N287.2 for materials [checked 20/10]. Whether the DPSC structures fall under N287 or N291 is [TO VERIFY].
- **Why it isn't obvious (R4.1–R4.3):**
  1. **Modular DPSC construction creates its own concrete problem.** The infill must flow between steel plates, which usually means a cement-rich self-consolidating mix [TO VERIFY for DPSC]. Calcined clay also raises water and admixture demand [TO VERIFY]. A mix that flows, stays cool in thick sections and qualifies for nuclear use is a genuine materials-engineering task. It feeds RB.7.
  2. **The usual low-carbon answer, blast-furnace slag, may shrink locally.** Ontario steelmaking is moving to electric arc furnaces, which make no blast-furnace slag; for example, ArcelorMittal Dofasco's CAD 1.8 bn DRI-EAF project in Hamilton is due by end-2028 [checked 20/10, secondary]. Whether Ontario's slag cement depends on those blast furnaces is [TO VERIFY]. If it isn't confirmed by Wed 18:00, it becomes a one-sentence risk.
  3. **The climate value of schedule.** If a low-carbon specification delays Units 2–4 even slightly, the displaced generation could outweigh what it saves. So the initiative must be schedule-neutral, for example by qualifying the mix on mock-ups during Unit 1 construction (R3.7, R4.4). §7 quantifies this.
  4. **A non-technical lever.** Canada's federal Standard on Embodied Carbon in Construction already requires concrete at least 10% below the regional average on major federal projects [checked 20/10: Treasury Board page; thresholds TO VERIFY]. Darlington has federal finance (a CAD 970 m Canada Infrastructure Bank loan is reported [TO VERIFY]). That is the hook for R3.7.
- **How Sam's hotspot results confirm or rule it out:** Granta's baseline for the target structures decides which lever leads.
  - C1 leads if concrete is a material share (roughly 40% or more [team to agree]) of those structures' embodied CO₂e, and the LC3 saving is bigger than the tornado swing from quantity scaling.
  - If steel is above about 80% even with realistic recycled content, steel (C2) becomes the lead lever in the same structures. That is a recycled-content slider change in Eco Audit, and LC3 stays the second lever.
  - A small per-MWh effect does **not** rule C1 out. It's an honest finding (R4.4), and §7 supplies the "so what".
- **Trap to avoid:** Canadian rebar is probably already scrap-based electric-arc-furnace steel [TO VERIFY]. If Granta's default steel is virgin, the baseline overstates rebar and invents a saving. Set rebar's recycled content to the realistic supply.

**C2. Lower-carbon steel for the DPSC modules and turbine-plant equipment.**
- **Location:** the same Units 2–4 structures plus turbine-plant steel, supplied from Ontario EAF or DRI-EAF mills (e.g. the Dofasco DRI-EAF plant [checked 20/10, secondary]).
- **Scale:** about 953 t of DPSC steel in Unit 1's basemat alone [checked 20/10]. Shaft-wall rings and equipment steel [TODO].
- **Application:** DPSC plates, rebar and turbine-plant steel.
- **Technology:** DRI-EAF plate with residual-element control (copper, tin) for nuclear grades [TO VERIFY].
- **Hotspot test:** a preliminary BWRX-300 Darlington LCA (Geneski, McKellar and Atkinson, Canadian Nuclear Society proceedings [checked 20/10: listing; year and numbers TO VERIFY]) reports steel, especially turbine-plant equipment, above concrete in construction emissions, scaled from a large reactor. Promote C2 only if Sam's Granta run agrees **and** he has plate or equipment tonnages by Wed 12:00. Otherwise it stays as sensitivity run S3 and a paragraph in §10.

**C3. Laser re-enrichment of depleted-uranium tails as fuel feed for Darlington.**
- **Location:** Global Laser Enrichment's proposed Paducah Laser Enrichment Facility in McCracken County, Kentucky. It would re-enrich legacy Department of Energy (DOE) tails under a 2016 agreement between GLE and the DOE. The NRC accepted the licence application for review in August 2025 [checked 20/10, secondary; TO VERIFY].
- **Scale:** the tails needed each year for four BWRX-300 cores [TODO: fuel mass balance].
- **Application:** natural-uranium-equivalent UF₆ that displaces mined uranium.
- **Technology:** SILEX laser isotope separation, developed by Australia's Silex Systems. GLE is owned by Silex and Cameco [checked 20/10, secondary].
- **Hotspot test:** UNECE (2021) is reported to find the fuel cycle's front end the largest source of nuclear's emissions [checked 20/10, secondary; TO VERIFY in the primary]. So C3 targets the biggest hotspot. But Sam has no fuel-cycle inventory, and laser enrichment energy data are proprietary, so it can't be quantified by Friday.
- **Use:** §8.3 and §10. An Australian-invented enrichment technology can't be built in Australia under EPBC s140A and ARPANS s10 [TO VERIFY wording], so it's being commercialised in the US. That is the cheapest strong R4.3 connection in the report.

### 2.2 Ranking

| Rank | Candidate | Speed for Sam with data in hand | Originality (R4) | Quantifiable by Friday (R2) | Likely hotspot size | Use |
|---|---|---|---|---|---|---|
| 1 | C1 LC3 infill, Units 2–4 | Fastest: forebay quantities in hand; Granta has concrete; one local EPD and one literature factor | Medium-high, if framed as in §2.1 | High | Small (concrete below steel per Geneski et al. [TO VERIFY]) | **The initiative** (D1) |
| 2 | C2 lower-carbon DPSC and equipment steel | Medium: tonnages missing | Medium | Medium | Larger than C1 [TO VERIFY] | Sensitivity S3, §10 |
| 3 | C3 tails re-enrichment | Slow: no fuel-cycle inventory | High | Low by Friday | Largest (front end) [TO VERIFY] | §8.3, §10 |

### 2.3 Planning arithmetic (examiner's check only; not for the report; Sam's numbers replace it)

The purpose is to see roughly how big C1's effect can be before Sam's numbers exist.
- **Lifetime output of one unit:** 300 MWe × 8,760 h × 0.90 × 60 years ≈ 1.4 × 10⁸ MWh. All four inputs are [TO VERIFY].
- **Whole life cycle:** at UNECE's reported 5.1–6.4 g CO₂e/kWh [secondary; TO VERIFY], about 0.7–0.9 Mt CO₂e per unit.
- **Forebay concrete:** 9.6 million kg at an assumed 0.10–0.15 kg CO₂e/kg (Granta replaces this) is about 1.0–1.4 kt. That is roughly 0.1–0.2% of the life-cycle total, and LC3 saves only part of it.

**Expect C1 to move the plant's life-cycle footprint by about 1% or less, even if the target structures hold several times the forebay's concrete.** Build the narrative on that (D2). It is a valid result under R4.4, and the brief says outright that a proposal need not end up net beneficial.

### 2.4 Draft thesis (D2)

"LC3 infill for the DPSC modules of Darlington Units 2–4 is technically promising but not yet qualified for nuclear use. It would save [X] t CO₂e per unit, about [Y]% of the plant's life-cycle footprint. An SMR's climate value depends far more on what it displaces and how soon it runs: compare Ontario with an Australian coal site. So the initiative is worth adopting only if it is schedule-neutral, and the bigger materials levers are construction speed (modular DPSC) and the fuel chain."

### 2.5 Exactly what the team needs from Sam [R2.1–R2.7, RB.5, RB.6]

| # | Deliverable | Detail | By | Serves |
|---|---|---|---|---|
| 1 | Fixes | The four `review.md` items: Clarington, not Ottawa; tunnel-boring-machine volume; move the rows to "SMR Parts LCA"; label the forebay rows as partial. Also: don't assume renewable electricity for construction (use Ontario's grid factor from Victor's analyst, or a stated cut-off). Replace the "[From X patent]" placeholder with a source column. Drop the "Smh BWR…" note. Tell us what preprint 202505.1533 is (it didn't resolve from here on 20/10) | Tue 21:00 | R2.5, R1.4, R5.5 |
| 2 | Goal and scope (1 page) | FU per D3. Reference flow: one unit over its design life. Boundary diagram covering construction, operation and maintenance, the fuel cycle (mining, milling, conversion, enrichment, fabrication), back end and decommissioning. Which stages are Granta and which are literature (named). Cut-offs; the recycled-content and end-of-life approach; Granta version and database | Tue 21:00 | R2.5, R2.4 |
| 3 | Lifetime-output inputs | Net MWe, capacity factor and design life, each sourced (Leroy supplies the BWRX-300 data). Send the resulting MWh to Victor. Every section uses this one denominator | Tue 21:00 | R2.5, R2.3 |
| 4 | Granta Eco Audit baseline | Forebay concrete (4,000 m³ = 9.6 million kg) and rebar (1,000 t, realistic recycled content), plus the 953 t DPSC basemat steel. CO₂e and energy by Eco Audit phase (material, manufacture, transport, use, disposal, end-of-life potential). Export the table and a screenshot for Appendix A | Tue 21:00 | R2.2, R2.1 |
| 5 | Scale-up basis | Concrete and steel for one unit's below-grade structures, plus an estimate for the rest of the plant. Either one sourced quantity, or a per-MWe intensity scaled from a large reactor as Geneski et al. did, with a low/high range. Candidate sources: TVA's Clinch River environmental report on NRC ADAMS (the NRC issued that BWRX-300 construction permit on 29 Sep 2026 [secondary; TO VERIFY]); OPG's 2023 "DNNP Environmental Impact Statement Review Report for Small Modular Reactor BWRX-300" [checked 20/10: listing; quantities TO VERIFY] | Wed 12:00 | R2.3, R2.7 |
| 6 | Initiative scenarios | S1 slag blend and S2 LC3: cement content (kg/m³), clinker factor, emission-factor source. S3: steel recycled-content sensitivity. Change in t CO₂e per structure, per unit and for Units 2–4; tonnes of clinker avoided | Wed 12:00 | R2.3, R2.1, R4.2 |
| 7 | Hotspot table | t CO₂e and g CO₂e/MWh by stage and by material, and each one's share of the life-cycle total (literature background named) | Wed 12:00 | R2.1, R2.2 |
| 8 | Uncertainty inputs | Low/central/high and a distribution for: structure concrete volume, cement content, clinker reduction, concrete emission factor, steel emission factor or recycled content, transport distance, lifetime output | Wed 12:00 (Monte Carlo drops to STRETCH if these aren't in by Wed 18:00) | R2.7 |
| 9 | §6 draft and Appendix A | Saved in `01_Report/sections/` so the fact-checker can run; headline numbers entered in `parameters.yaml` | Wed 21:00 | R2.1–R2.7, RB.5, RB.6 |
| 10 | Sign-off | Tornado and Monte Carlo outputs (from the analyst's script, if Sam accepts it); slides 5–7 | Thu 12:00 | R2.7, PRES |

---

## 3. Report outline mapped to the rubric (18.25 pages of text; cap 20) [all IDs]

| § | Section (pages) | Rubric IDs | Owner | Evidence it needs |
|---|---|---|---|---|
| — | Title page, abstract (about 200 words), table of contents (whether they count: T2) | R5.1, R5.5 | Shared (writer drafts Thu; all approve) | Full title; Victor's and Sam's student IDs (only Leroy's is there); date 23/10/2026 |
| 1 | Introduction (0.75) | RB.1, R1.1, R1.2, R5.1 | Shared | Drawdown SMR solution; the initiative in one sentence; the question; a roadmap |
| 2 | Methods and data (1.0) | R2.4, R2.5, R1.4, R2.7 | Shared: Sam (LCA and Granta), Leroy (literature and patent search), Victor (displacement, LCOE, HHI, MCDA) | ISO 14040/44; Granta version; HHI definition and thresholds (US DOJ/FTC Merger Guidelines 2023 [TO VERIFY]); GenCost; an MCDA reference [TODO analyst]; search strings and dates |
| 3 | Barriers to cutting emissions with SMRs (1.25) | RB.2, R1.2, R1.1, R1.3 | Victor (lead); Leroy (time, TRL) and Sam (material intensity) feed in | One number and one source per barrier. Cost and finance: NuScale/UAMPS; CAD 20.9 bn for four units at Darlington [checked 20/10]. Time to deploy: Darlington first power 2030 [checked 20/10] vs CSIRO's reported "earliest from 2040" for Australia [TO VERIFY]. Law: EPBC s140A, ARPANS s10, state bans [TO VERIFY]. Also fuel-supply concentration (HHI), embodied carbon and nuclear-grade qualification, social licence, workforce |
| 4.1 | SMR technology, projects and patents (1.25) | RB.3, R1.1, R1.3, R1.4 | Leroy | IAEA; CNSC and NRC licensing documents; a project and TRL table (Darlington, Clinch River, Linglong One, the NuScale/UAMPS cancellation); Google Patents |
| 4.2 | The BWRX-300 at Darlington (0.5) | RB.3, R2.3 | Leroy | GE Vernova Hitachi UK design-assessment documents; the CNSC licence to construct one unit (April 2025, valid to 31 Mar 2035, three regulatory hold points [checked 20/10]); DPSC modular construction [checked 20/10] |
| 4.3 | The initiative: location, scale, application, technology, and which barriers it addresses (0.75) | RB.1, RB.3, R4.1, R4.2, R4.3, R2.3 | Sam (technical) and Victor (route to practice); the team approves the wording | The §2.1 statement with Sam's numbers. Say plainly which barriers it doesn't touch (cost, Australian law) |
| 5 | The materials, extraction to end-of-life (1.5) | RB.4, R2.3, R1.1, R4.2 | **Leroy** (lead); Sam checks the stages match §6 | LC3: quarrying, calcination, grinding, mixing, placing in DPSC modules, curing, qualification, service (shielding, durability), decommissioning, crushing and recycling. Steel: EAF/DRI-EAF route, plate, recycling. Scrivener et al. (2018); CSA N287 |
| 6 | Life-cycle assessment and eco-audit (3.5) | R2.1–R2.7, RB.5, RB.6, R1.3 | **Sam** | 6.1 Goal and scope (ISO 14040/44). 6.2 Granta baseline and hotspots. 6.3 Initiative vs baseline per unit and for Units 2–4, with resource use (tonnes of clinker avoided; t/MWe; kg/MWh). 6.4 Tornado and Monte Carlo. 6.5 Benchmarks (UNECE 2021, IPCC AR5, Carless et al. 2016, Geneski et al.) and the reasons for any differences |
| 7 | Carbon avoided: Ontario vs Liddell, the value of schedule, and the same money on firmed renewables (1.75) | R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, R3.6, RB.6 | **Victor** | Sam's g CO₂e/MWh. Ontario's average and marginal emission factors (IESO, Canada Energy Regulator or the National Inventory Report [TO VERIFY which]). NSW factor and the AEMO ISP trajectory. Leroy's start dates; the Darlington cost; GenCost |
| 8 | Non-technical factors affecting translation to practice (3.25) | R3.1–R3.8 | **Victor** | Every subsection ends with what it means for actually building the initiative and the SMR |
| 8.1 | Law, regulation and licensing (0.6) | R3.2, R3.4, R3.5, R1.4 | Victor | EPBC Act 1999 s140A; ARPANS Act 1998 s10; state bans; ARPANSA's role; the CNSC path and timelines; the qualification route for LC3 under CSA N287/N291 |
| 8.2 | Economics, finance and market barriers (0.85) | R3.1, R3.8, R2.3, RB.6 | Victor | GenCost LCOE; NuScale/UAMPS; who finances Darlington (OPG and ratepayers, the CIB loan, and Canada Growth Fund and Building Ontario Fund equity [secondary; TO VERIFY]); barriers to entry; the initiative's abatement cost ($/t CO₂e) |
| 8.3 | Supply concentration and geopolitics (0.5) | R3.2, R3.8, R2.1, R4.3 | Victor | HHI for uranium mining by country and enrichment by company (Red Book, World Nuclear Association); Australia's resource position; party positions (the Coalition's 2024 plan and its current status [TO VERIFY]; Labor; Greens); the C3 link |
| 8.4 | Social licence (0.6) | R3.3, R3.4, R3.8 | Victor | Raw Australian polling (e.g. Lowy Institute) against deaths per TWh; consent of First Nations and host communities (Darlington and NSW); jobs; waste governance |
| 8.5 | Stakeholders and money flows (0.35, plus a figure) | R3.1, R3.3, R3.5, R5.2 | Victor | Power/interest map; a table of who pays and who earns |
| 8.6 | Implementation pathway and non-technical solutions (0.35) | R3.7, R3.5, R3.4, R4.3 | Victor | A procurement requirement (the federal embodied-carbon standard; conditions on federal finance); qualifying the mix on Unit 1 mock-ups; the licence route for Units 2–4; the financing model; community benefit; workforce and skills; reuse of the coal site's grid connection in the Australian case |
| 9 | Triple-bottom-line evaluation and comparison of solutions (1.25) | RB.8, R3.6, R2.6, R4.4 | Victor (lead); scores from Sam and Leroy | A TBL table for the initiative. MCDA comparing the status quo, SMR, SMR + C1, and the same money on firmed renewables, for Australia; weight sensitivity |
| 10 | Future material properties and processes (0.75) | RB.7, R4.2, R4.4 | Leroy (lead), Sam | Self-consolidating LC3 mixes for DPSC infill; nuclear qualification data (radiation, durability, heat of hydration); low-residual EAF plate (C2); laser re-enrichment (C3) |
| 11 | Conclusions and recommendations (0.75) | R2.6, R3.7, R4.4, R1.2, R5.1 | Shared | Answer the question with the numbers; state the honest finding; recommendations; limitations |
| — | References (whether they count: T2) | R1.4, R5.4 | Shared: Victor's agents keep `sources.md`; Leroy formats | Harvard, alphabetical, every in-text citation present |
| A | LCA inventory, Granta exports, calculations | RB.5, R2.2, R2.4 | Sam | Eco Audit exports; the spreadsheet |
| B | Calculations for displacement, schedule value, same money, LCOE, HHI and MCDA | RB.5, R2.4 | Victor | Scripts in `03_LCA_Calculations/scripts/`, outputs in `results/` |
| C | Sensitivity: tornado and Monte Carlo set-up and results | R2.7, RB.5 | Sam (scripts from the analyst if Sam agrees) | Parameter ranges, random seed, outputs |
| D | Assumptions table | R2.5, RB.5 | Shared (generated from `parameters.yaml`) | Every number with its source key |
| E | Literature and patent search log | R1.4 | Leroy | Databases, search strings, dates, hit counts, patents kept |

**Pages by owner:** Victor 7.5 (§3, §7, §8, §9); Sam 3.5 (§6), plus the eco-audit and Appendices A and C; Leroy 4.0 (§4.1, §4.2, §5, §10), plus Appendix E and integration; shared 3.25 (§1, §2, §4.3, §11).

**Old draft headings to new sections:**
- 1 Introduction → §1
- 2 Data Sources/Methodology → §2
- 3.1.1 Current Projects → §4.1
- 3.1.2 Technical Descriptions → §4.2 and §5
- 3.2 Lifecycle Analysis → §6
- 3.3 National Strategies and Industrial Policies, and 3.3.1 Australia → §8.1 and §8.3
- 4 Conclusion → §11
- 5 References → References

New: §3, §4.3, §7, §8.2, §8.4–§8.6, §9, §10 and the appendices.

**Figures and tables.** Figures and graphs don't count towards the page limit (brief; confirm in T2). Use one chart style and palette throughout. Captions follow `Figure N. Description.` with a `Source: Author (Year).` line (style guide).

| ID | Content | § | Owner | Serves |
|---|---|---|---|---|
| F1 | System boundary diagram | 6.1 | Sam | R2.5, R5.2 |
| F2 | Eco Audit results by phase and material | 6.2 | Sam | R2.2, R5.2 |
| F3 | Tornado chart | 6.4 | Sam | R2.7, R5.2 |
| F4 | Monte Carlo histogram (if run) | 6.4 | Sam | R2.7 |
| F5 | Our result against the benchmark ranges | 6.5 | Sam | RB.6, R5.2 |
| F6 | Carbon avoided per year and cumulatively, Ontario vs Liddell, with the schedule effect | 7 | Victor | R4.3, R2.3, R5.2 |
| F7 | Same money: SMR vs firmed renewables | 7 | Victor | R3.6, R2.3 |
| F8 | Stakeholder power/interest map | 8.5 | Victor | R3.3, R5.2 |
| F9 | Material flow from extraction to end-of-life | 5 | Leroy | RB.4, R5.2 |
| T1 | Initiative specification (location, scale, application, technology) | 4.3 | Sam, Victor | RB.1 |
| T2 | Projects, timelines and TRLs | 4.1 | Leroy | RB.3, R1.1 |
| T3 | HHI results | 8.3 | Victor | R3.2, R3.8 |
| T4 | TBL summary of the initiative | 9 | Victor | RB.8 |
| T5 | MCDA scores, weights and sensitivity | 9 | Victor | R3.6 |
| T6 | Key assumptions (full list in Appendix D) | 6.1 | Sam | R2.5 |

---

## 4. Methods: MUST or STRETCH [R2.1–R2.7, R3.1–R3.8, R1.4, R4.2, R4.3, R4.4, RB.3, RB.6, RB.8]

### 4.1 Professional-standard requirements, with acceptance tests

| Requirement | Status | Owner | Acceptance test | Serves |
|---|---|---|---|---|
| ISO 14040/44 goal and scope (FU 1 MWh, cradle-to-grave, fuel cycle included) | MUST | Sam | §6.1 states the goal, FU, reference flow, boundary (F1), cut-offs, allocation, data sources and quality, impact basis and limitations. The lifetime-MWh denominator can be reproduced from Appendix D. The fuel cycle sits inside the boundary using named literature values, and the report says it's a hybrid | R2.5, R2.4, R2.2 |
| What the SMR displaces: Ontario vs an Australian coal site | MUST | Victor | Same FU and the same value from Sam. Ontario shown at **both** average and marginal emission factors. Australia valued for the year an SMR could actually first run there (Leroy's dates; CSIRO's reported 2040 [TO VERIFY]), on the ISP trajectory, not today's coal intensity. Liddell/Bayswater coal intensity only as the upper bound. Results in t CO₂e per year and cumulatively to 2035 and 2050 | R2.3, R4.3, R2.7, R2.6 |
| Carbon value of schedule | MUST (cheap) | Victor | t CO₂e of displaced generation per month of delay, at average and marginal emission factors, against C1's saving. This decides whether "schedule-neutral" goes into the thesis as a condition | R4.3, R2.3, R2.6, R3.7 |
| Same money spent on firmed renewables | MUST for Australia, using GenCost and the Darlington budget (CAD 20.9 bn [checked 20/10], converted at a stated rate and date). STRETCH for Ontario-specific costs | Victor | Firming or integration costs included; build times from GenCost and Leroy; MWh and t CO₂e by 2035 and 2050 for both options; caveats stated | R3.6, R2.3, R3.1, R4.3 |
| Tornado sensitivity | MUST | Sam (analyst's script if he accepts) | At least six parameters, each low/high value sourced or justified, shown as a ranked chart (F3) | R2.7 |
| Monte Carlo | MUST if Sam's ranges arrive by Wed 18:00; otherwise STRETCH, and the report says the tornado bounds the uncertainty | Analyst's script; Sam signs off | 10,000 draws, stated distributions, fixed seed, median and 5th–95th percentiles, reproducible from `scripts/` | R2.7, R2.4 |
| Benchmarks | MUST | Sam (analyst supplies a benchmark brief Wed 09:00) | Result compared with UNECE (2021) (nuclear 5.1–6.4 g CO₂e/kWh [secondary; TO VERIFY]), IPCC AR5 WGIII Annex III [TO VERIFY values], Carless et al. (2016) [TO VERIFY] and Geneski et al. Any value outside a range is explained (boundary, scaling, data year, grid mix) | RB.6, R2.7, R1.3 |
| MCDA triple-bottom-line verdict | MUST for Australia; STRETCH for Ontario scoring | Victor | Four alternatives: status quo, SMR, SMR + C1, same money on firmed renewables. Criteria across environment, economy, society and feasibility. Scores traced to §6–§8. Weights justified (equal weights plus two stakeholder sets), each weight varied ±50%, with a rank-reversal check | R3.6, RB.8, R2.6, R4.4 |

### 4.2 All methods

| Method | MUST / STRETCH | Owner | Due | Serves |
|---|---|---|---|---|
| Granta Eco Audit of the baseline structures | MUST | Sam | Tue 21:00 | R2.2, R2.1 |
| Initiative scenarios S1 and S2; steel sensitivity S3 | MUST | Sam | Wed 12:00 | R2.3, R2.1, R4.2 |
| Hybrid whole-plant total (Granta plus literature) | MUST | Sam | Wed 12:00 | R2.2, R2.5, R2.6 |
| Resource use and efficiency (tonnes of clinker avoided, t/MWe, kg/MWh, plant thermal efficiency) | MUST | Sam (Leroy supplies plant data) | Wed 21:00 | R2.3 |
| Initiative abatement cost ($/t CO₂e) against a stated carbon price | MUST (simple range) | Victor (using Sam's saving) | Wed 21:00 | R2.3, R3.1 |
| GenCost LCOE comparison (cited) | MUST | Victor | Wed | R3.1, RB.6 |
| Own Darlington LCOE at three discount rates | STRETCH | Victor | — | R3.1, R2.7 |
| HHI for mining (by country) and enrichment (by company) | MUST | Victor | Tue | R3.2, R2.1, R3.8 |
| HHI by mining company; HHI of patents by assignee | STRETCH | Victor, Leroy | — | R3.1, R4.3 |
| Law and regulation review (s140A, s10, state bans, CNSC, the CSA route) | MUST | Victor | Tue | R3.2, R3.4, R3.5 |
| Party positions | MUST (short) | Victor | Tue | R3.2 |
| NuScale/UAMPS cost-risk case | MUST (one paragraph with numbers) | Victor | Wed | R3.1 |
| US startup valuations (SEC filings); China's state-led model | STRETCH (one sourced sentence each) | Victor | — | R3.1, R1.1 |
| Stakeholder map and money flows | MUST | Victor | Wed | R3.1, R3.3, R3.5, R5.2 |
| Perceived vs actual safety (one poll series against deaths per TWh) | MUST | Victor | Wed | R3.3, R3.8 |
| First Nations and host communities, jobs, waste governance, workforce | MUST (short, sourced) | Victor | Wed | R3.3, R3.4 |
| Implementation pathway and non-technical solutions | MUST | Victor | Wed | R3.7, R3.5 |
| Patent search, documented (BWRX-300; DPSC and steel-plate composite modules; LC3) | MUST (5–10 patents, logged); Leroy decides his own focus | Leroy | Wed 18:00 | R1.4, RB.3, R4.2 |
| Patents for US startups' designs; laser isotope separation | STRETCH | Leroy | — | R1.4, R4.3 |
| Project, timeline and TRL table | MUST | Leroy | Tue 21:00 | RB.3, R1.1, R3.4 |
| Carbon payback time | STRETCH | Victor (using Sam's totals) | — | R2.3 |
| Coal LCA in Granta (Sam's red task) | STRETCH (use UNECE coal values instead) | Sam | — | RB.6 |
| Own fuel-cycle inventory (separative work, ore grade) | STRETCH | Sam | — | R2.2, R2.7 |
| Second Australian site (Loy Yang) | STRETCH | Victor | — | R2.7, R4.3 |

---

## 5. Interfaces (who needs what from whom, and when) [R1.3, R1.4, R2.3, R2.5, R2.6, R2.7, R3.4, R3.6, R4.2, R4.3, RB.3, RB.4, RB.6, RB.8, R5.1–R5.5]

Analysts add requests here, addressed by name. Conflicts between numbers also go here, with both sources. Agents never edit Sam's or Leroy's work; feedback goes in `review.md`.

| From → to | What | By | Serves |
|---|---|---|---|
| Leroy → Sam | BWRX-300 data with sources: net and thermal output, design life, capacity-factor claims, fuel type | Tue 21:00 | R2.5, R2.3 |
| Leroy → Victor | Timeline table: Darlington Unit 1 (first power 2030 [checked 20/10]), Units 2–4, Clinch River, Linglong One; TRLs; the competing Australian earliest-date claims (Coalition 2035/2037 vs CSIRO 2040 [secondary; TO VERIFY]) | Tue 21:00 | R3.4, R2.3, R3.6, R1.3 |
| Victor → Leroy | Licensing milestones for the timeline: CNSC licence to construct; the licence-to-operate application; the NRC Clinch River permit | Tue 21:00 | RB.3, R3.4 |
| Sam → Victor | Lifetime-MWh denominator, and the capacity factor and design life behind it | Tue 21:00 | R2.5 |
| Victor → Sam | Benchmark brief (UNECE 2021, IPCC AR5, Carless 2016, Geneski et al.); Ontario's grid emission factor for construction electricity | Wed 09:00 | RB.6, R2.7 |
| Sam → Victor | Life-cycle g CO₂e/MWh (central and range); C1's saving per unit and for Units 2–4; tonnes of clinker avoided | Wed 12:00 | R2.3, R4.3, R3.6 |
| Sam → Leroy | The stages and materials in the LCA, so §5 matches | Wed 12:00 | RB.4 |
| Victor → Sam | Tornado and Monte Carlo script, if he wants it | Wed 15:00 | R2.7 |
| Leroy → Sam, Victor | Patents relevant to DPSC modules and LC3 | Wed 18:00 | R1.4, R4.2 |
| Sam, Leroy → Victor | MCDA scores for their criteria (environment from Sam; TRL and timing from Leroy) | Thu 09:00 | R3.6, RB.8 |
| All → Leroy | Final sections into the master document | Thu 18:00 | R5.1–R5.5 |
| Overlaps | Victor owns costs, grants, jobs and financing (the "Socio-economic" items in `Assumptions.docx` move to him). Sam owns electricity output. Leroy owns dates | — | R2.6, R5.5 |

---

## 6. Day-by-day schedule [all IDs, PRES]

### Tuesday 20 October (today)

| By | Who | Task | Serves |
|---|---|---|---|
| 13:00 | All | Meeting: decisions D1–D11; Meeting 3 minutes | RB.1, R4.1–R4.4, R2.5, R5.3 |
| 14:00 | Victor | Send tutor questions T1–T7 | R2.2, RB.1, R5.3, PRES |
| 21:00 | Sam | §2.5 items 1–4: fixes, goal and scope, lifetime inputs, Granta baseline | R2.2, R2.5, R2.4, R2.1 |
| 21:00 | Leroy | BWRX-300 data to Sam; timeline and TRL table to Victor | RB.3, R1.1, R2.5 |
| 21:00 | Leroy | Master .docx rebuilt with the §3 headings and a proper title page | R5.1, R5.5 |
| 21:00 | Leroy | Deck skeleton: delete the three slides copied from the brief; title slide with Victor, Sam and Leroy only | PRES |
| evening | Victor + agents | Analyst runs 1–3 (§7); writer drafts §8.1 and §8.3; fact-checker overnight | R2.3, R4.3, RB.6, R3.2, R3.4, R3.5 |

### Wednesday 21 October

| By | Who | Task | Serves |
|---|---|---|---|
| 09:00 | Examiner | Marks §8.1 and §8.3. Analyst sends the benchmark brief and grid emission factors to Sam | R3.2, R3.4, RB.6 |
| 12:00 | Sam | §2.5 items 5–8 (scale-up, scenarios, hotspots, ranges) to Victor | R2.1, R2.2, R2.3, R2.7 |
| 12:00 | Leroy | §4.1–4.2 draft | RB.3, R1.1, R1.3, R1.4 |
| 18:00 | Leroy | §5 draft; patents to Sam and Victor | RB.4, R1.4, R4.2 |
| 18:00 | Victor + agents | Analyst runs 4–6; writer drafts §7 with Sam's numbers | R2.3, R2.7, R4.3, R3.6 |
| 21:00 | Victor + agents | Writer drafts §8.2, §8.4–8.6 and §3. Victor reads and edits every draft: the team owns the text | R3.1, R3.3–R3.8, RB.2, R1.2 |
| 21:00 | Sam | §6 draft and Appendix A; numbers in `parameters.yaml` | R2.1–R2.7, RB.5, RB.6 |
| 21:00 | All | Fill your own slides with headline figures and numbers from the drafts | PRES, R5.2 |
| overnight | Fact-checker | §3 and §4–§8, including Sam's and Leroy's drafts | R1.4, R2.1–R2.7, R3.1–R3.8, RB.6 |

### Thursday 22 October (deck due; content freeze 21:00)

| By | Who | Task | Serves |
|---|---|---|---|
| 09:00 | Examiner | Marks Wednesday's drafts in `review.md`, with feedback to each owner by name | all IDs |
| 11:00 | Victor + agents | Analyst run 7 (MCDA); writer drafts §9 | R3.6, RB.8, R4.4 |
| 12:00 | Sam | Tornado and Monte Carlo signed off; final numbers in `parameters.yaml` | R2.7 |
| 12:00 | All | STRETCH check: STRETCH starts only if every MUST has a draft | R5.3 |
| 14:00 | Leroy | §10; Appendix E | RB.7, R4.2, R1.4 |
| 15:00 | All | Slide numbers checked against `parameters.yaml`; references slide done; **submit the deck** | PRES |
| 16:00 | Writer | §2 (with Sam's and Leroy's method paragraphs), §1, §11, abstract | R2.4, R1.2, R5.1, RB.1 |
| 18:00 | Owners | Apply the 09:00 review to your own sections; send final sections to Leroy | all IDs |
| 21:00 | Leroy | Assemble the .docx. Converting the Markdown with pandoc, using the draft .docx as `--reference-doc`, keeps the heading and font styles. Add the table of contents, captions and references | R5.1–R5.5 |
| **21:00** | — | **FREEZE: no new content after this** | R5.3 |
| overnight | Fact-checker, then examiner | Fact-checker checks the full report and slide consistency (`factcheck.md`). Examiner's final review at max effort gives a must-fix list in `review.md` by Fri 08:00 | all IDs |

### Friday 23 October (submit)

| By | Who | Task | Serves |
|---|---|---|---|
| 11:00 | Owners | Must-fix items only, in your own sections | R2.1–R2.7, R3.1–R3.8, R5.5 |
| 12:00 | Leroy | Page count (15–20 pages of text), captions, alphabetical references, table of contents; AI-use declaration inserted | R5.3, R5.4, R5.5 |
| 13:30 | Cross-read | Victor reads Leroy's sections, Leroy reads Sam's, Sam reads Victor's: typos and consistency only | R5.5, R5.1 |
| 14:00 | Leroy | PDF export and a visual check | R5.5 |
| **15:00** | Leroy | **Submit**, or at least 3 hours before the confirmed deadline | all IDs |
| TBC | All | One timed 15-minute rehearsal before the week 11 slot. If the slot is Friday, do it Thu 17:00–17:30; otherwise after the report is submitted (date from T1) | PRES |

---

## 7. Agent loop order (Victor's and the shared sections) [R1.2, R1.4, R2.1, R2.3, R2.4, R2.6, R2.7, R3.1–R3.8, R4.3, R4.4, R5.1, RB.1, RB.6, RB.8]

The coordinator runs these in order. Each output starts with its `Rubric coverage:` line (CLAUDE.md). Each section gets one revision cycle; after the freeze, only must-fix items.

1. **Analyst run 1 (Tue, now): inputs for displacement, schedule value and the same-money comparison** [R2.1, R2.3, R2.7, R3.1, R3.6, R4.3, RB.6].
   - First because it carries the most marks, has the longest dependency chain, and the deck needs its headline by Wednesday night.
   - None of it waits for Sam: build parameterised scripts with a placeholder life-cycle value (the UNECE range), then swap in Sam's number at Wed 12:00.
   - Inputs: the Darlington budget and financing; Ontario's average and marginal emission factors; the NSW factor and ISP trajectory; Liddell/Bayswater intensity as the upper bound; GenCost capital costs and LCOE; CSIRO's earliest-date statement; the value of reusing the coal site's grid connection (qualitative unless a source gives a number).
   - Also produces the benchmark brief for Sam.
2. **Analyst run 2 (Tue): law, regulation, licensing, party positions, and the route to practice for C1** [R3.2, R3.4, R3.5, R3.7, R1.4].
   - Open the legislation itself: EPBC s140A and ARPANS s10; also the state bans and ARPANSA's role.
   - Canada: the CNSC licence and hold points, the licensing step for Units 2–4, and CSA N287/N291 qualification.
   - The federal embodied-carbon standard; the Coalition's 2024 plan and its current position.
3. **Analyst run 3 (Tue evening): HHI** [R3.2, R2.1, R3.8]. Mining by country (Red Book or World Nuclear Association production data, latest year); enrichment capacity by company (World Nuclear Association); Australia's position; concentration thresholds.
   → Writer: §8.1 and §8.3 → fact-checker → examiner (Wed 09:00).
4. **Analyst run 4 (Wed, after Sam's 12:00 ranges): tornado and Monte Carlo script for the LCA** [R2.7]. Offered to Sam; he decides whether to use it and owns the results.
5. **Analyst run 5 (Wed): economics and finance** [R3.1, R2.3, RB.6]. GenCost LCOE; NuScale/UAMPS; Darlington financing; barriers to entry; the initiative's abatement cost.
6. **Analyst run 6 (Wed): social licence, stakeholders and money flows, workforce, waste governance** [R3.3, R3.4, R3.5, R3.8].
   → Writer: §7 (after Sam's numbers), §8.2, §8.4–8.6, then §3 → fact-checker (Wed night, including Sam's and Leroy's drafts) → examiner (Thu 09:00).
7. **Analyst run 7 (Thu morning): MCDA** [R3.6, RB.8, R2.6, R4.4], using Sam's and Leroy's scores.
   → Writer: §9, then the shared §2, §1, §11 and abstract [R2.4, R5.1, R1.2, RB.1].
8. **Thu 21:00:** fact-checker on the whole report and the slides → examiner's final review at max effort → `review.md`, and `rubric-tracker.md` once the coordinator releases it [all IDs]. A section is done only when every ID it serves is marked HD with evidence and the fact-checker has confirmed that evidence (CLAUDE.md). Anything short of that at the freeze gets an exact, cheap fix for Friday or is cut.

---

## 8. Slide deck (due Thu 22 Oct; presented in the week 11 workshop) [PRES]

> **Update, 20/10 evening (main session):** a 15-slide draft deck now exists. Its link, speaker split and gaps are in `04_Presentation/README.md`, so the "effectively empty" note below is out of date. **D1 decided by Victor: C1 (LC3 for Darlington Units 2–4), with Liddell as the Australian comparison site.** The deck has been updated to match.

The deck is effectively empty: a title slide that still lists Aaron (remove him, per CLAUDE.md), three slides copied from the brief, and a blank references slide. The talk is 15 minutes plus 3–5 minutes of questions, and attendance is compulsory (brief).

| # | Slide | Owner | Minutes | Serves |
|---|---|---|---|---|
| 1 | Title: Victor, Sam, Leroy | Leroy | — | PRES |
| 2 | Why SMRs, and why Darlington | Leroy | 1 | PRES, R1.1 |
| 3 | The BWRX-300 and DPSC modular construction | Leroy | 1.5 | PRES, RB.3 |
| 4 | Barriers | Victor | 1.5 | PRES, RB.2 |
| 5 | The initiative: location, scale, application, technology | Sam | 1.5 | PRES, RB.1 |
| 6 | LCA scope: FU, boundary, data | Sam | 1 | PRES, R2.5 |
| 7 | Eco-audit results and tornado | Sam | 2 | PRES, R2.2, R2.7 |
| 8 | What it displaces: Ontario vs Liddell, and the value of schedule | Victor | 1.5 | PRES, R4.3 |
| 9 | Same money on firmed renewables; LCOE | Victor | 1 | PRES, R3.6 |
| 10 | Law, politics and supply concentration (HHI) | Victor | 1 | PRES, R3.2 |
| 11 | Triple-bottom-line verdict (MCDA) | Victor | 1 | PRES, RB.8 |
| 12 | Future materials needs (LC3 infill, qualification, tails re-enrichment) | Leroy | 1 | PRES, RB.7 |
| 13 | Conclusion | All | 1 | PRES |
| 14 | References (Harvard) | Leroy | — | PRES, R5.4 |

Speaking time: Victor 6 minutes, Sam 4.5, Leroy 3.5, shared conclusion 1.

Rules:
- Every number comes from `parameters.yaml`.
- Export each chart once and use the same file in the report and the slides [R5.2].
- If a number changes after Thursday, the report is right, and the talk says the figure was updated after the slides were submitted.

---

## 9. Questions for our tutor (send today; ask again at the next class if it's before Friday) [R2.2, R2.5, R4.1, R5.3, R5.4, RB.1, PRES]

1. **(Top)** What time on Fri 23 Oct is the report due, and in what format (Word or PDF; Turnitin)? What time is the deck due on Thu 22 Oct, and when is our week 11 presentation slot? [R5.3, PRES]
2. **(Top)** What counts towards the 15–20 pages: title page, abstract, table of contents, tables, references, appendices? Are there font, spacing or over-length rules? [R5.3]
3. **(Top)** Is a hybrid eco-audit acceptable: Granta EduPack Eco Audit for the initiative's concrete and steel, with cited literature values for the fuel cycle and the rest of the plant (Granta can't model enrichment)? [R2.2, R2.5]
4. Is LC3 infill for Darlington's steel-plate composite modules (Ontario, Canada) acceptable as our specific initiative, with an Australian coal site as the comparison? [RB.1, R4.1]
5. Is there a separate marking guide for the presentation, and must all three of us speak? [PRES]
6. Is Monash Harvard required, or will any consistent style do? [R5.4]
7. What AI use is permitted in this unit, and how should we declare it? [Monash rule]

---

## 10. Risks and fallbacks [R1.4, R2.2, R2.3, R2.4, R2.7, R3.8, R4.1–R4.3, R5.3, R5.5, PRES]

| Risk | Fallback | Serves |
|---|---|---|
| Sam can't run Granta today | Run his inputs on a teammate's or a campus machine by Wed 09:00. Last resort: literature emission factors, labelled as an "equivalent analysis" (the R2.2 wording allows "eco-audit or equivalent") | R2.2 |
| No whole-structure quantities by Wed 12:00 | Report per forebay and per DPSC basemat (known quantities), plus a stated scaling range (Geneski et al.'s scaled-from-a-large-reactor approach as precedent); widen the tornado | R2.3, R2.7 |
| A number has no primary source | Write `[TODO]` and drop the claim; never cite a search snippet | R1.4, R3.8 |
| Thursday overload (deck and freeze on the same day) | Deck content finished Wed 21:00; Thursday is for checks only; deck submitted by 15:00 | PRES |
| Over 20 pages | Cut §8 to 3.0 pages and §4.1 to 1.0 first. Never cut §6 or §7; move working to the appendices | R5.3, R2.4 |
| Slides and report disagree | The report and `parameters.yaml` win; the fact-checker checks both | R5.5 |
| The marker reads C1 as "greener concrete" | Lead §4.3 with the DPSC infill problem and the schedule test, not with emissions per cubic metre | R4.1–R4.3 |

---

## 11. Fix existing work before reusing it [R1.4, R1.5, R2.5, R3.2, R3.3, R5.5, PRES]

- **Sam:** the list in §2.5, item 1. [R2.5, R1.4, R5.5]
- **Team notes:**
  - "Zero risk of meltdown" and "carbon neutral fuel source" overclaim; use sourced wording.
  - "Australia has 30% of the world's uranium reserves" (Meeting 2) needs the Red Book figure and its precise wording (identified recoverable resources in a stated cost category) [TO VERIFY].
  - Personal political opinions in the notes stay out of the report.
  - [R3.3, R3.2, R1.5]
- **Report .docx:** the title is just "SMR", and Victor's and Sam's student IDs are missing. The scandium caption and references are gone, but the image file is still in the package as an unused part. It's harmless, and it disappears if Leroy rebuilds the document from the Markdown sections. [R5.5]
- **Deck:** Aaron is still on the title slide; three slides copied from the brief to delete. [PRES]
- **Housekeeping:** in this folder, `00_Brief/rubric.md`, `CLAUDE.md`, `.claude/agents/*.md` and `01_Report/review.md` are older than the coordinator's copy (`/home/user/mte4593-group-assignment/`). Sync them before running any other agent, or it will work to the old criteria. [all IDs]

---

## 12. Coverage check and status by rubric ID [all IDs]

Every ID has at least one section and an owner. "Plan provides" is what this plan contributes towards the HD descriptor; "Still missing" is the evidence that doesn't exist yet. The Owner and Section(s) columns are ready to copy into `rubric-tracker.md`, which isn't edited here.

| ID | Section(s) | Owner | Plan provides | Still missing |
|---|---|---|---|---|
| R1.1 | §3, §4, §5, §6, §8, §10 | All (Leroy checks at integration) | Each aspect mapped to a section: technology §4; fuel cycle §6, §8.3, §10; construction §5–6; LCA §6; economics §8.2; politics and law §8.1, §8.3; social licence and safety §8.4; supply chain §8.3; timescales §4.1, §7 | All text |
| R1.2 | §3 (and §1, §11) | Victor | A barrier list with one number and one source each | §3 draft |
| R1.3 | §3, §4.1, §6.5, §8.2, §8.3 | All | Disagreements to synthesise: Coalition 2035 vs CSIRO 2040; UNECE vs IPCC vs Carless ranges; Geneski et al.'s steel-over-concrete finding vs ours | Drafts |
| R1.4 | §2, References, Appendix E | All; Leroy (patents) | Primary sources listed per section; patents as a MUST | `sources.md` is empty; no patent log yet |
| R1.5 | Whole report | All; examiner's cut list at the freeze | Rule: every paragraph serves the initiative or an ID | Review at the freeze |
| R2.1 | §6, §7, §8.2, §8.3 | Sam, Victor | MUST calculations (§4) | Every number |
| R2.2 | §6.2, Appendix A | Sam | Eco Audit specification (§2.5 item 4) | Granta runs |
| R2.3 | §4.3, §6.3, §7, §8.2 | Sam, Victor | Scale fixed at the Units 2–4 structures; resource use; abatement cost; displacement | Quantities and results |
| R2.4 | §2, §6.1, Appendices A–D | Sam, Victor | Methods, script locations and appendix structure | Scripts and appendix |
| R2.5 | §6.1, Appendix D | Sam | FU, boundary, hybrid data and impact basis (D3) | Sam's sign-off; sourced lifetime inputs |
| R2.6 | §6, §7, §9, §11 | Sam, Victor | The thesis and its logic chain (§2.4) | Drafts |
| R2.7 | §6.4, §6.5, §7, Appendix C | Sam, Victor | Tornado (MUST); Monte Carlo (MUST with a fallback); benchmarks; average and marginal emission factors | Ranges and runs |
| R3.1 | §8.2, §7 | Victor | LCOE, NuScale/UAMPS, financing, barriers to entry, abatement cost, same money | Analyst runs 1 and 5 |
| R3.2 | §8.1, §8.3 | Victor | Legislation list, party positions, HHI | Analyst runs 2 and 3 |
| R3.3 | §8.4, §8.5 | Victor | Polling against deaths per TWh; consent; jobs | Analyst run 6; First Nations evidence |
| R3.4 | §8.1, §8.4, §8.6 | Victor (Leroy's dates) | Licensing timelines, workforce, waste governance | Analyst runs 2 and 6 |
| R3.5 | All of §8, especially §8.6 | Victor | Rule: each subsection ends with what it means for building C1 and the SMR | Drafts |
| R3.6 | §9, §7 | Victor | MCDA specification; same-money comparison | Analyst runs 1 and 7 |
| R3.7 | §8.6, §11 | Victor | Implementation list: procurement, qualification on Unit 1 mock-ups, licensing of Units 2–4, finance, community benefit, workforce | Drafts |
| R3.8 | §8, §9 | Victor | Numbers wherever possible (HHI, LCOE, poll percentages, deaths per TWh, dollars) | Analyst evidence |
| R4.1 | §4.3 | Team (Sam, Victor) | C1 framed beyond "greener concrete" (§2.1) | Team adopts D1 and D2 |
| R4.2 | §4.3, §5, §10 | Sam, Leroy | The DPSC infill problem; the slag-supply angle; tails re-enrichment | Infill type and slag link still to verify |
| R4.3 | §7, §8.3, §8.6 | Victor | Ontario vs Liddell; reusing the coal site's grid connection; schedule value; the enrichment technology kept offshore by s140A; the procurement lever | Calculations |
| R4.4 | §9, §10, §11 | Team (Victor leads) | The honest-finding rule (§2.3) | Results |
| R5.1 | Whole report; §1, §11 | Leroy (integrator), writer | Outline; lead-with-the-point rule | Drafts |
| R5.2 | Figures F1–F9, tables T1–T6 | Each owner; Leroy for consistency | Figure and table plan | Figures |
| R5.3 | Page budgets (§3) | Leroy | 18.25-page budget and a cut order (§10) | Friday page count |
| R5.4 | References | Leroy; Victor's agents keep `sources.md` | One bibliography, Harvard per the style guide | Bibliography |
| R5.5 | Whole report | All | Friday cross-read pairs | Friday |
| RB.1 | §4.3, §1 | Team | C1 statement in the brief's "better example" form | Sam's numbers in the statement |
| RB.2 | §3 | Victor | Barrier list | Draft |
| RB.3 | §4.1–4.3 | Leroy (Sam and Victor for §4.3) | Technology status, and what C1 does and doesn't address | Drafts |
| RB.4 | §5 | Leroy (lead), Sam | The stages to cover | Draft |
| RB.5 | Appendices A–D | Sam, Victor | Appendix list | Contents |
| RB.6 | §6.5, §7, §8.2 | Sam, Victor | Benchmark list | The comparison |
| RB.7 | §10 | Leroy, Sam | List of future properties and processes | Draft |
| RB.8 | §9 | Victor, team | TBL table and MCDA | Draft |

**Gaps (IDs with no section or owner):** none.

**At risk (homed, but the evidence doesn't exist yet):**
- R2.2: no Granta output.
- R1.4: `sources.md` is empty and there's no patent log.
- R3.3: no evidence yet on First Nations or host communities.
- R3.4: no workforce and skills evidence.
- R4.2: the DPSC infill type and the slag-supply link are unverified.
- R5.3: no page count yet.

**Change from the tracker's provisional owners:** RB.4 moves to Leroy (lead), with Sam checking. Every other ID matches.
