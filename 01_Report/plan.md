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
| Analyst run 1 → Victor (human) | **Blocker:** the proxy refused every primary host on 20/10, so every value in `03_LCA_Calculations/parameters_run1.yaml` is a search or secondary lead. Open each primary listed in `02_Research/sources_run1.md`, confirm or correct the YAML, then re-run the three scripts. Priority: GenCost 2025-26 final (SMR and firmed-VRE LCOE), 2026 ISP Step Change emissions by year, TAF 2025 average and marginal, NGA Factors 2025 NSW, the Ontario 8 May 2025 release | Wed 12:00 | R1.4, R2.1, R2.7, R3.1 |
| Analyst run 1 → Leroy | Darlington U1 and U2–U4 in-service years (current); whether CSIRO's "2040 at the earliest" covers SMRs; the Coalition's 2035/2037 claims; net MWe, CF, design life with sources. These dominate the §7 results more than the LCA value does (`results/displacement.md` §5) | Tue 21:00 | R2.3, R2.7, R3.4 |
| Analyst run 1 → Sam | Life-cycle g CO₂e/kWh (central, low, high) and the C1 saving per unit in kt, to drop into `parameters_run1.yaml` (`smr_lca_g_per_kwh`); benchmark brief at `02_Research/briefs/benchmarks-for-sam.md` | Wed 12:00 | R2.3, RB.6 |
| Conflict: deck vs latest Ontario factor (Victor) | The deck's 53 g/kWh (ontario.ca, 2023) conflicts with TAF's 73.8 (2024) and CER's 35 (2022). NSW/Ontario becomes 13× → 9.3× (TAF average) → 1.9× (Ontario marginal). The deck also applies the 2025 NSW factor to an SMR that could not run before about 2040. See `02_Research/briefs/displacement-and-cost.md`, "Corrections to the deck" | Wed 21:00 | R2.7, R4.3, R1.3 |
| Overlaps | Victor owns costs, grants, jobs and financing (the "Socio-economic" items in `Assumptions.docx` move to him). Sam owns electricity output. Leroy owns dates | — | R2.6, R5.5 |
| Analyst (run 3) → Leroy | BWRX-300 fuel data with sources: core loading (tU), reload fraction and cycle length, average enrichment (% U-235). Needed to size SWU per year and a strategic fuel reserve in §8.3/§8.6 | Wed 12:00 | R2.3, R3.7 |
| Analyst (run 3) → Victor / fact-checker | HHI inputs could not be opened from the analyst's session (network block). Open the 7 pages in the checklist at the end of `02_Research/briefs/supply-concentration.md`, set `verified: true` in `parameters_run3.yaml`, and rerun `scripts/hhi.py` before §8.3 or slide 13 use the numbers | Wed 09:00 | R1.4, R3.8 |
| Analyst (run 3) → run 2 (law) | Confirm from the Acts whether conversion plants are outside EPBC s140A and ARPANS s10 (Parliamentary Library quick guide says the four listed installations are fuel fabrication, power plant, enrichment, reprocessing), and whether NSW law bans conversion | Wed 09:00 | R3.2, R3.7 |
| Conflict (run 3) → Victor | Australia's resource share: 28% at < USD 130/kgU (Red Book 2024, on slide 13) vs 29% and 27% in two WNA tabulations of Red Book 2026 (now the latest edition). Pick the edition and cost category; the Meeting 2 "30% of reserves" wording is wrong either way | Wed 09:00 | R1.3, R5.4 |
| lca-analyst (21/10) → Leroy | **BWRX-300 plant and fuel data, sourced:** net MWe (300 per GEH vs 315 per OEB D2-4-1; factcheck S3), lifetime capacity factor, design life (60 per CNSC CMD 24-H3-1B vs 65 per Ontario/NucNet), discharge burnup (GWd/t), reload-average enrichment (3.8% lead), cycle length and reload fraction (NEDO-33977), fabrication site (GNF Wilmington?), enrichment supplier(s), uranium origin (Cameco/Saskatchewan?). Placeholders in `parameters_lca.yaml` §A and §E until then. Burnup and enrichment are tornado ranks 4–5 | Thu 09:00 | R2.5, R2.3, R2.7 |
| lca-analyst (21/10) → Leroy | **Quantities:** concrete (m³) and steel (t) per unit from OPG's EIS review report NK054-REP-07730-00055-R001, TVA's Clinch River ER (ML25118A209) or SEIS (ML26035A285), or NEDO-33914/33926 (DPSC basemat and wall thickness). Is the forebay/CCW system per unit or shared by four units? Currently scaled: 20,700 m³/unit (10,350–41,400), C1 target 13,100 m³ with assumed thicknesses | Thu 09:00 | R2.3, R2.7, RB.1 |
| lca-analyst (21/10) → Victor (human) | **Open the LCA primaries** (proxy blocked all of them): Gibon & Hahn Menacho 2023 (PMC copy; conversion heat 26–665 kWh/kgU is the largest uncertainty), Parker 2016, EDF 2024 EPJ-N shares, CAC 2020 GU EPD (which region is Ontario), St Marys Bowmanville EPD 20046, CRSI 2022 rebar EPD, Peterson 2005 tables, the five LC3 leads, Carless 2016, UNECE 2021. Set `status: verified` and re-run `lca_*.py`. Also: Canada GHGRP facility emissions for Cameco Port Hope ÷ UF₆ output would replace the conversion range with a measured value | Thu 12:00 | R1.4, R2.7, RB.6 |
| lca-analyst (21/10) → policy analyst / Victor | **LCA result for §7:** life-cycle 4.2 g CO₂e/kWh (P5–P95 3.0–5.8; mean 4.3; mode case 2.7) replaces the UNECE placeholder `smr_lca_g_per_kwh` 5.75 in `parameters_run1.yaml`; re-run displacement/schedule/same-money. C1 LC3 saving 1.73 kt per unit (1.39–2.15), 5.2 kt for Units 2–4: with `schedule_value.md` that is 10–15 days of delay (Ontario average trajectory) or about 1.4 days (marginal-declining) to cancel it. Fuel demand for §8.3: 4 units ≈ 196 t natural U and 138 tSWU per year (`lca_baseline.md`, placeholders) | Wed 21:00 | R2.3, R4.3, R3.6, R2.1 |
| lca-analyst (21/10) → team | **Granta Eco Audit run** on a team machine following `03_LCA_Calculations/results/granta_inputs.md` (under 1 hour); expected values listed there. Until it exists, slides 6–7 must not say the numbers come from Granta | Thu 12:00 | R2.2, PRES |
| Conflict (lca-analyst) → Victor / deck | Slides 6–7 claim "Granta EduPack Eco Audit" as the source; no Granta run exists. Slide 6 says forebay quantities were scaled to the plant; the LCA scales per-MWe reactor intensities instead. Our 4.2 g/kWh sits at the low edge of UNECE 5.1–6.4 (explained in `lca.md` §9). Full list: `lca.md` §11 | Thu 15:00 | R2.4, R5.5, PRES |
| Finding (lca-analyst) → team, for §2.4 thesis and §10 | Slag (S1) saves nearly as much as LC3 (1,550 vs 1,730 t/unit; LC3 wins in 64% of draws), and moving all steel to EAF-level factors saves about 2× LC3 (3,710 t/unit). C1 still passes plan §2.1's test (concrete ≈ 66% of the target structures' known embodied CO₂e) | Thu 09:00 | R4.1, R4.2, R4.4, R2.6 |
| Analyst (run 7a, Q2) → writer (Q4, Q8) and coordinator (Q15) | **§7 re-based on 4.2 g/kWh (3.0–5.8).** Displacement moves by under 1% (NSW 1.50 Mt/yr; Ontario 0.073–0.165 Mt/yr; ratio 9.1–20.6×; Liddell to 2050 0.67–3.85 Mt). New: `schedule_value.md` §6 (C1 break-even: 9.2–14.6 days per unit on the average factor, 1.3–1.4 days on the marginal factor; whole Units 2–4 saving vs one unit late 28–44 / 4.0–4.2 days) and §7 (C1 carbon value C$0.49–0.88 m vs a one-month Units 2–4 slip: 10.9–118 kt CO₂e, C$33–110 m carrying cost, C$88 m deferred output). Deck slides 9 and 14: see `schedule_value.md` and the Q2 report | Thu 02:00 | R2.3, R2.7, R3.1, R4.3, PRES |
| Conflict (run 7a) → run 5 / Victor | **Canadian carbon price.** `parameters_run5.yaml` `carbon_prices_cad` [95, 110, 170] follows the 2021 path (C$110 in 2026, C$170 in 2030). Two search summaries (canada.ca "Industrial carbon pricing in Canada"; ICAP news) say a new headline industrial trajectory took effect 15 May 2026: **C$95 (2026), C$100 (2027–29), C$115 (2030), C$130 (2035)**. Both hosts refused by the proxy. Victor to open the canada.ca page; if confirmed, run 5 sets 2026 = 95 and 2030 = 115 and re-runs `initiative_cost.py` (break-even premium at 2030 falls from C$22.5 to about C$15/m³). `schedule_value.md` §7 already shows both paths | Thu 09:00 | R3.1, R2.3, R1.4 |
| Conflict (analyst run 5) → Victor | **Run 1's SMR LCOE is probably the 2023 value, not 2030.** `parameters_run1.yaml` `smr_lcoe_aud` 514 (387–641) vs NucNet (23 May 2024): GenCost 2023-24 gives A$387–641 for **2023** and A$230–382 for **2030**. If confirmed, set 2030 values and re-run `same_money.py`: the ratio of SMR to firmed renewables falls from 5.0× to about 2.9×, and the conclusion is unchanged. See `results/lcoe.md` §5 | Thu 09:00 | R1.3, RB.6, R3.1, R3.6 |
| Analyst run 5 → Victor (human) | Open, in this order: (1) GenCost 2025-26 final accessible text (SMR, large nuclear and firmed-VRE LCOE, 2030 and 2050; WACC); (2) OPG's C$149/MWh DNNP LCOE on the OEB record (EB-2025-0297); (3) the NuScale, Oklo and NANO 10-K cover pages; (4) the ECCC carbon benchmark page. Set `status` in `parameters_run5.yaml`, then re-run `lcoe.py` and `initiative_cost.py`. List in `02_Research/sources_run5.md` | Thu 12:00 | R1.4, R3.1, RB.6 |
| Analyst run 5 → Victor / Leroy | **C1 cost inputs have no source:** the LC3 concrete price premium in Ontario (RMI 2024 *Business Case for LC3*, North America scenario, is the best lead) and the cost of a CSA N287.2 qualification and mock-up programme (ask OPG or a nuclear concrete lab). Until then §8.2 reports the **break-even** (C$12.6–22.5/m³ at C$95–170/t), not a point abatement cost | Thu 12:00 | R2.3, R3.1, R3.7 |

---

## 6. Day-by-day schedule [all IDs, PRES]

> **Superseded from Wed 21/10 18:00 by §7 (revised 21/10), the work queue.** The Wednesday rows for Sam and Leroy are overdue. Sam's work has passed to Victor (CLAUDE.md, 21/10), and Leroy's is subject to gate G1. The Friday rows still stand.

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

## 7 (revised 21/10): work queue to the freeze [all IDs, PRES]

Rubric coverage: all (R1.1–R5.5, RB.1–RB.8); presentation rubric

Written by the examiner at the whole-project audit (`review.md`, "Whole-project audit (21/10)"). **It replaces the old §7 loop order and, from Wed 18:00, the Wednesday–Thursday rows of §6.** Runs 1–4 and the writer drafts of §8.1, §8.3, §6 and Appendices A–C are done (see the audit for their status).

**Decisions it assumes.**
- D1 stays C1. The default framing is "low-clinker SCC infill for the DPSC modules and forebay shafts of Units 2–4: LC3 as the target binder, a slag blend as the fallback, specified only if schedule-neutral". Victor can overrule it.
- Sam's red sections belong to Victor (CLAUDE.md, 21/10).
- Leroy's sections fall back to Victor's agents only if gate **G1** (Wed 18:00) triggers and Victor agrees.

**Rules for every job.**
- Every output starts with its `Rubric coverage:` line.
- Every number comes from a parameter file or a script.
- Every unverified claim keeps its [TO VERIFY] marker until assembly (Q19), where it is either verified, hedged or cut. **No marker ships.**
- Teammates' files are never edited. Fallback drafts are new files labelled "drafted for Leroy; Leroy may reclaim".

**Parallelism.**
- Jobs marked **‖** can run at the same time as the other ‖ jobs in their wave: they write different files and none needs another's output.
- "after Qn" means wait for Qn.
- If only one writer instance can run at a time, run the writer jobs in this order: Q4, Q7, Q6, Q8, Q10, Q9, Q14, Q16.

### Already running (do not re-queue)
- **R5. Analyst run 5: economics and finance.** GenCost 2025-26 LCOE; NuScale/UAMPS (primary filings); Darlington financing (OPG, CIB, CGF/BOF); barriers to entry; **the initiative's carbon value or abatement cost**. Writes to `02_Research/briefs/` and `03_LCA_Calculations/`. [R3.1, R2.3, RB.6, R3.8]
- **R6. Analyst run 6: social licence, stakeholders and money flows, workforce, waste governance.** [R3.3, R3.4, R3.5, R3.8, R5.2]
- **W0. Writer: §6 v3** with the text fixes from `review.md` §6 (points 1–3, 5–6, 8). Any fix that needs a script result stays a TODO for Q8. [R2.3, R2.5, R2.6, R5.1, R5.2]

### Wave 1: start now (Wed afternoon)

| # | Agent | Job | Inputs | Output file(s) | IDs | Due | Parallel |
|---|---|---|---|---|---|---|---|
| Q1 | lca-analyst | **LCA script fixes.** (a) A like-for-like S3 row: low-carbon steel in the C1 target structures only; relabel the whole-plant row "upper bound: all steel at best-practice EAF sections factors". (b) Monte Carlo shares for S1, S2b, S3 (E1). (c) A conversion-heat alternative run: held at 26, and log-uniform 26–665, as one row for Table C2. (d) F3: plain labels, a "mode case 2.70" marker, no embedded title. (e) F5: UNECE as a range only, no 3.7 attributed to Warner and Heath (L31, L66). (f) Correct `lca.md` §0, §1, §7, §10, §11 (L64). (g) An S0 counterfactual note: does NEDO-33926 permit SCMs [TO VERIFY]; if so, what S0 becomes | `review.md` §6 points 2, 4, 7, 9; factcheck L31, L64, L66, E1; `parameters_lca.yaml` | `scripts/lca_scenarios.py`, `lca_uncertainty.py`, `lca_plot.py`; `results/lca_scenarios.*`, `lca_montecarlo_summary.csv`, `lca_uncertainty.md`, `F3_tornado.png`, `F5_benchmarks.png`, `lca.md` | R2.6, R2.3, R2.7, R2.5, R5.2, RB.6 | Wed 20:00 | ‖ |
| Q2 | analyst (run 7a) | **Re-base §7 on our LCA and value C1.** Set `smr_lca_g_per_kwh` to 4.2 (3.0–5.8; source = our model) and re-run `displacement.py`, `schedule_value.py`, `same_money.py`. Add a schedule-value table: break-even days against C1's saving per unit (1.74 kt) and for Units 2–4 (5.2 kt), at average and marginal factors. Add C1's carbon value at a sourced 2026 Canadian carbon price, set against the CO₂e and dollar cost of one month's delay. If run 5 already gives the carbon value, use it | `results/lca.md` §0; `parameters_run1.yaml`; R5 output | `parameters_run1.yaml`; `results/displacement.md`, `schedule_value.md`, `same_money.md` | R2.3, R2.7, R3.1, R4.3 | Wed 21:00 | ‖ |
| Q3 | analyst (run 7b) | **Close the sourcing gaps that block text.** Add `sources.md` entries for: ISO 14040/44; EN 15804; NWMO APM; Constitution ss 23 and 109; IPCC AR5 WGIII Annex III (min/median/max); Silex/GLE (ASX release, NRC Paducah docket; B15); Ontario blast-furnace-to-EAF conversions (L18); Krall 2022; Lowy; OWID (plus Markandya and Wilkinson); NuScale/UAMPS primary; GEH 2021. Supply authors for L10, L17, LACCEI and Ng. Replace ENR; use the CRSI 2022 EPD; merge the APH duplicates. Add a CRAI row to `hhi.py`. **Size §8.3:** four units' 196 t U and 138 tSWU a year against Urenco USA capacity, plus a two-reload reserve. Propose the Red Book edition (B9) | factcheck A, B, H; `results/lca_baseline.md`; `briefs/supply-concentration.md` | `02_Research/sources.md`; `parameters_run3.yaml`; `scripts/hhi.py`; `results/hhi.md` (new §6, sizing) | R1.4, R1.3, R4.3, R2.3, R5.4 | Wed 23:00 (Silex go/cut: **Thu 12:00**) | ‖ |
| Q4 | writer | **§7 Carbon avoided: Ontario vs Liddell, the value of schedule, the same money on firmed renewables** (≤ 1.75 pages; F6 and F7 specified from the results files). Plus **Appendix B4 (displacement), B5 (schedule value, including the C1 break-even), B6 (same money)** | `briefs/displacement-and-cost.md`; Q2 outputs; §6 v3; `review.md` audit §2 | `01_Report/sections/7-carbon-avoided.md`; `appendix-B-policy-and-supply-working.md` (append B4–B6) | R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, R3.6, RB.5, RB.6 | Thu 02:00 | after Q2 |

### Gate G1: Leroy, Wed 18:00 (Victor decides)
- **G1.** If a Leroy file is in `01_Report/sections/` (or has been sent to Victor) by 18:00, skip Q5 and Q9. His drafts go to Q11 (fact-check) and Q13 (review), and he keeps assembly (Q19) if he confirms by Thu 12:00.
- If nothing has arrived, Victor triggers the fallback and records it in CLAUDE.md and the Meeting 3 minutes, on the same terms as Sam's (21/10).
- [RB.3, RB.4, RB.7, R1.1, R1.4]

| # | Agent | Job | Inputs | Output file(s) | IDs | Due | Parallel |
|---|---|---|---|---|---|---|---|
| Q5 | analyst (run 8, Leroy fallback) | **Technology, projects, timescales, plant and fuel data, materials life cycle, patents.** (a) T2: a projects, timelines and TRL table (Darlington U1–U4, Clinch River, Linglong One, NuScale/UAMPS cancellation), with CNSC hold points and the Australian earliest-date claims (Coalition 2035/2037 vs CSIRO 2040). (b) BWRX-300 data: net MWe (300 vs 315), capacity factor, design life (60 vs 65), burnup, reload enrichment, cycle length, fabrication site, sourced into `parameters_lca.yaml`. Tell the lca-analyst if any value changes (re-run before Thu 12:00). (c) The LC3 and slag life cycle from extraction to end-of-life (for §5 and F9). (d) RB.7 evidence: SCC LC3 qualification data, low-residual EAF plate, laser enrichment, waste forms. (e) **Appendix E**: a Google Patents log (BWRX-300; steel-plate composite / DP-SC modules; LC3 / calcined clay) with strings, dates, hit counts and 5–10 patents kept. If the host is blocked, log the attempt and the gap | plan §3 rows 4.1, 4.2, 5, 10, E; `briefs/route-to-practice-c1.md`; `lca.md` §13 requests | `02_Research/briefs/technology-projects-trl.md`; `briefs/materials-eol-future.md`; `parameters_lca.yaml` (§A, §E); `01_Report/sections/appendix-E-search-log.md` | RB.3, RB.4, RB.7, R1.1, R1.3, R1.4, R2.5, R4.2 | Thu 07:00 | ‖ (with Q4, Wave 2) |

### Wave 2: Wednesday night, as inputs land

| # | Agent | Job | Inputs | Output file(s) | IDs | Due | Parallel |
|---|---|---|---|---|---|---|---|
| Q6 | writer | **§8.2 Economics, finance and market barriers** (0.85 p; GenCost comparison for RB.6; NuScale; who finances Darlington; C1's carbon value). Then **§8.4 Social licence** (0.6 p; poll vs deaths per TWh; First Nations and host consent; jobs) and **§8.5 Stakeholders and money flows** (0.35 p; F8 power/interest map specified; who pays and who earns) | R5 and R6 briefs; `same_money.md`; Q2 | `sections/8.2-economics-finance.md`; `8.4-social-licence.md`; `8.5-stakeholders-money.md` | R3.1, R3.3, R3.4, R3.5, R3.8, RB.6, R5.2 | Thu 04:00 | ‖, after R5 and R6 |
| Q7 | writer | **§8.1 v3 and §8.3 v3**: apply the 20/10 review in full. §8.1: Units 2–4 licensing step; "36 even with every other crossbencher"; Senate date; s 8 consequence for a private plant; REGDOC 32-month benchmark; NEDO-33926 / AISC N690 as the governing infill code; the 18–24-month critical path; Coalition 2035 vs CSIRO 2040; ANNPSR; caption above the table, placeholder line deleted. §8.3: "Each stage's HHI"; the 2023/2010 class column; the "scale, not legal test" clause; the conversion "therefore" fixed; the Kazakh/Rosatom clause; the CRAI range; the Red Book clause; the Silex text with the Cameco/OPG link, or cut; **SWU sizing from Q3**. Delete §8.1's "Note for §9" once Q14 cites App B3 | `review.md` §8.1/§8.3; factcheck A, B; Q3 | `sections/8.1-law-regulation-licensing.md`; `8.3-supply-concentration.md` | R3.2, R3.4, R3.5, R3.7, R2.3, R2.6, R2.7, R1.3, R4.3, R5.2, R5.5 | Thu 06:00 | ‖, after Q3 |
| Q8 | writer | **§6 v4 and Apps A/C number drop-in.** Like-for-like steel row and the reworded finding 4; MC shares in T8; the conversion-heat alternative sentence (§6.4) and Table C2 row; C1's carbon value in finding 2; the F3 and F5 captions; A3 rebar cap (L65); A5 ENR replaced; A9/A10 Granta results or cut (per H2) | Q1, Q2, W0; H2 result | `sections/6-lca-eco-audit.md`; `appendix-A-lca-inventory.md`; `appendix-C-sensitivity.md` | R2.2, R2.3, R2.6, R2.7, RB.6, R5.2 | Thu 06:00 (Granta rows by Thu 13:00) | ‖, after Q1 and Q2 |
| Q10 | writer | **§3 Barriers** (1.25 p; one number and one source per barrier: cost and finance, time to deploy, law, fuel-supply concentration, embodied carbon and nuclear qualification, social licence, workforce; each says whether C1 touches it). **§4.3 The initiative** (0.75 p; the D1 default in the brief's "better example" form, with T1: about 13,100 m³ per unit, about 1,740 t per unit, about 5,200 t for Units 2–4, about 6,900 t of clinker, about 0.3%; lead with the DPSC infill problem and the schedule condition; say what C1 does **not** address). **§8.6 Implementation pathway** (0.35 p; the route-to-practice brief §5–6 levers compared in a table; the supply-option table from the supply brief; qualification on Unit 1 mock-ups; federal procurement standard) | all briefs; §6; Q4, Q6, Q7 | `sections/3-barriers.md`; `4.3-initiative.md`; `8.6-implementation.md` | R1.2, RB.2, RB.1, RB.3, R4.1, R4.2, R4.3, R3.5, R3.6, R3.7 | Thu 10:00 (§3 and §4.3 can start now; §8.6 after Q7) | ‖ |
| Q9 | writer (Leroy fallback) | **§4.1 Technology, projects and patents** (1.25 p; T2), **§4.2 BWRX-300 at Darlington** (0.5 p), **§5 Materials from extraction to end-of-life** (1.5 p; F9 specified; stages matched to §6), **§10 Future material properties and processes** (0.75 p; SCC LC3 infill qualification; low-residual EAF plate as the next lever, with both S3 rows; conversion energy and ore grade; laser re-enrichment if sourced) | Q5; §6; Q1 | `sections/4.1-technology-projects.md`; `4.2-bwrx300-darlington.md`; `5-materials-life-cycle.md`; `10-future-materials.md` | RB.3, RB.4, RB.7, R1.1, R1.3, R4.2, R4.4 | Thu 11:00 | ‖, after Q5 (skip if G1 shows Leroy delivered) |

### Wave 3: Thursday morning

| # | Agent | Job | Inputs | Output file(s) | IDs | Due | Parallel |
|---|---|---|---|---|---|---|---|
| Q11 | fact-checker | **Pass 3**, in two batches. Batch 1: Appendix B (never checked), §7, §8.2, §8.4, §8.5, §8.1/§8.3 v3, the §6 v4 and Apps A/C deltas, and the Q2/Q3 results. Batch 2: §3, §4.x, §5, §8.6, §10 and the Q5 briefs | all of Wave 2 | `01_Report/factcheck.md` (new section I) | R1.4, R2.1–R2.7, R3.1–R3.8, RB.5, RB.6 | Batch 1 Thu 09:00; batch 2 Thu 13:00 | ‖ with Q12 |
| Q12 | analyst (run 9) | **MCDA.** Four alternatives for Australia: status quo, one SMR at Liddell, SMR + C1, the same money on firmed renewables. Criteria: life-cycle CO₂e; CO₂e avoided to 2050 per dollar; cost (LCOE); time to first power and deliverability (including schedule risk); supply security (HHI); social licence; legal feasibility (App B3). Scores traced to §6–§8. Equal weights plus two stakeholder sets, each weight varied ±50%, with a rank-reversal check. Show explicitly that SMR vs SMR + C1 differ by about 0.3% on the environmental criterion. Script the App B3 route scoring as well | §6, §7, §8.x drafts; App B3; `same_money.md`; R5, R6; Q5 (TRL, dates) | `scripts/mcda.py`; `results/mcda.md`, `mcda_scores.csv` | R3.6, RB.8, R2.6, R4.4, R2.4 | Thu 11:00 (start Thu 07:00) | ‖ with Q11 |
| Q13 | examiner | **Mark Wave 2** (Q4, Q6, Q7, Q8, Q10; Q9 or Leroy's drafts). Update the tracker. Give the cut list for R1.5 and R5.3 if the page count exceeds 20 | Wave 2; Q11 batch 1 | `review.md`; `rubric-tracker.md` | all IDs | Thu 10:30 | — |
| Q14 | writer | **§9 TBL evaluation and MCDA** (1.25 p; T4 TBL summary; T5 MCDA scores, weights, sensitivity; verdict "adopt C1 only as a schedule-neutral specification qualified on Unit 1 mock-ups; otherwise specify the slag blend"). **Appendix B7** (MCDA working). Then revisions to Victor's sections from Q11/Q13 | Q12; Q11; Q13 | `sections/9-tbl-mcda.md`; `appendix-B-…md` (B7); revised section files | R3.6, RB.8, R2.6, R4.4, RB.5 | Thu 14:00 | ‖ with Q15 |
| Q15 | coordinator (main session), then fact-checker | **Deck sync.** Every fix in `review.md` audit §4. Slides 7–8 get F2/F3/F5; an image on slide 3 or 4; an HHI bar chart on slide 13; slide 5's title in the D1 default wording; slide 14 = the Q12 MCDA result (or "preliminary" kept on-slide); Q2 changed to AISC N690 / CSA N291; numbers re-based on Q2; slide 15 rebuilt in Harvard from `sources.md`; `04_Presentation/README.md` speaker plan updated (H5). Fact-checker spot-checks slides against the report (30 min) | audit §4; Q1, Q2, Q3, Q12 | `04_Presentation/deck-source/project/slides/*.html`; `04_Presentation/README.md`; `factcheck.md` (deck rows) | PRES, R5.2 | Edits Thu 13:30; check Thu 14:30; **submit Thu 15:00** | ‖ with Q14 |
| Q16 | writer (+ lca-analyst for Q16a) | **§2 Methods and data** (1.0 p: ISO 14040/44; the model and Granta status; HHI with thresholds and caveat; displacement and GenCost; MCDA; search strings and dates from App E), **§1 Introduction** (0.75), **§11 Conclusions and recommendations** (0.75; the ranked materials levers: schedule, fuel front end, whole-plant steel, concrete; limitations), **abstract** (about 200 words), **one reference list** (merge `sources.md` and `sources_lca.md`; Harvard per the style guide; alphabetical; every in-text citation present, nothing extra). **Q16a (lca-analyst):** generate Appendix D from all parameter files (value, range, source key, verified status) | all sections; Q12; Q5 | `sections/1-introduction.md`, `2-methods.md`, `11-conclusions.md`, `0-abstract.md`, `references.md`; `appendix-D-assumptions.md` (Q16a, Thu 14:00) | R2.4, R2.5, R1.2, R1.4, R4.4, R3.7, R5.1, R5.4, RB.1, RB.5 | Thu 18:00 | ‖ with Q15 |
| Q17 | fact-checker | Batch 3: §9, §1, §2, §11, the abstract, the reference list, App D; cross-document consistency (report vs slides vs results) | Q14, Q16 | `factcheck.md` | R1.4, R5.4, R2.4, R3.6 | Thu 19:30 | — |
| Q18 | writer | Must-fix revisions from Q17 only | Q17 | section files | as flagged | Thu 20:30 | — |
| Q19 | Leroy if confirmed at G1, else coordinator | **Assembly.** pandoc with `MTE4593 Report.docx` as `--reference-doc`. Title page with all three student IDs and Sam's surname; table of contents; one numbering for figures (F1…) and tables (T1…), captions above tables; strip changelogs, "IDs covered" and "Remaining TODOs" blocks; every [TO VERIFY]/[TODO] resolved as verified, hedged or cut (list each cut); text page count 15–20 (cut order in §10); AI-use declaration placeholder (D10) | all section files | `01_Report/MTE4593 Report.docx`; `01_Report/assembly-log.md` (cuts and renumbering) | R5.1–R5.5, R1.5 | **Thu 21:00 FREEZE** | — |
| Q20 | fact-checker | **Final check:** the whole assembled report, and slide-vs-report consistency | Q19 | `factcheck.md` (final) | all IDs | Fri 01:00 | — |
| Q21 | examiner (**max effort**) | **Final pre-submission review:** a grade per criterion, a must-fix list per owner (Fri 11:00 deadline), the final tracker | Q19, Q20 | `review.md`; `rubric-tracker.md` | all IDs | Fri 08:00 | — |

Friday: owners make must-fix edits only (by 11:00). Then page count and PDF (12:00–14:00), and **submit by 15:00** (§6, Friday table).

### Human jobs (gate HD; no agent can do them)
- **H1. Victor: open the P1 primaries, Wed 19:00 to Thu 12:00.** LCA first: Gibon 2023; Parker 2016; EDF 2024; the OPG basemat story or NEDO-33926; the CAC EPD region; UNECE 2021; IPCC AR5. Then: EPBC s 140A; ARPANS s 10 and s 13; the NSW Act ss 8–9; WNA mining, conversion and enrichment; DOJ/FTC 2023; the OEB filing D2-4-1. Set `verified`, re-run the scripts, and tell the fact-checker. [R1.4, R2.1, R2.7, R3.8, RB.6]
- **H2. Granta Eco Audit cross-check by Thu 12:00** (Victor, Leroy or Sam on any EduPack machine; `granta_inputs.md`, under 1 hour). If it is not done, Q8 cuts A9/A10 and slide 6 drops "pending". [R2.2]
- **H3. Meeting 3 minutes:** D1 (with the default framing or Victor's overrule), the Sam takeover, G1's outcome and the B9 Red Book edition. [teamwork evidence]
- **H4. Message Leroy now** with the G1 deadline and the list in `review.md` audit §6.
- **H5. Speaker plan by Thu 12:00:** who presents slides 1–8 if Sam and/or Leroy are absent. Record it in `04_Presentation/README.md`. [PRES teamwork]
- **H6. Tutor questions T1/T2:** the deadline time, and what counts towards the page limit. Needed before Q19's page count. [R5.3]

### Page budget still to write (text pages, plan §3)
- §1 0.75
- §2 1.0
- §3 1.25
- §4.1–4.3 2.5
- §5 1.5
- §7 1.75
- §8.2 0.85, §8.4–8.6 1.3
- §9 1.25
- §10 0.75
- §11 0.75

That is **about 13.65 pages**, against about 4.7 drafted. If time runs out at the Thu 12:00 STRETCH check, cut in this order: §8.5 into a figure only; §4.1 to 1.0 page; §5 to 1.0 page; §2 to 0.75 page. Never cut §7, §9 or §3.

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
