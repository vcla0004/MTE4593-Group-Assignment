---
title: "Small modular reactors: where they cut the most carbon, what holds them back, and a low-clinker concrete initiative for Darlington"
subtitle: "MTE4593 Materials and Sustainability, Assignment 2 (Group 9)"
author:
  - "Victor Clarke [TODO: student ID]"
  - "Leroy Louis Jean (33880212)"
  - "Sam [TODO: surname] [TODO: student ID]"
date: "October 2026"
---

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```
## Abstract

Small modular reactors (SMRs) are proposed to replace closing coal plants. This report asks whether an SMR is feasible across the triple bottom line, and whether a materials choice can cut its footprint without delaying it. We study the GE Vernova Hitachi BWRX-300 (300 MWe) at Darlington, Ontario, and compare Liddell, New South Wales, a closed coal site.

Our initiative, C1, is low-clinker concrete for the steel-composite infill and forebay shaft of Darlington Units 2–4: pilot limestone calcined clay cement (LC³) in eligible non-safety works first, extend it to the infill only if qualified, and adopt it only if schedule-neutral. A screening life-cycle assessment (ISO 14040/44 principles) gives about 4 g CO₂e/kWh for one unit, mostly from the fuel front end. C1 saves about 2,200 t per unit (1,100–3,300), about 0.36% of the life cycle, and a delay of about 12–18 days cancels it.

Law, cost and timing decide the Australian case. An SMR at Liddell could not start before about 2040, and firmed renewables avoid 10.9 times more CO₂e per dollar. In a multi-criteria analysis, renewables rank first under all four weight sets.

We recommend piloting LC³ in eligible non-safety works first, and extending it to the infill only if qualified on Unit 1 mock-ups. In Australia, we recommend firmed renewables.


## 1 Introduction

**When a coal plant closes, small modular reactors (SMRs) are one proposed replacement. We ask whether an SMR is feasible across the triple bottom line (environmental, economic, social), and whether a materials choice can make it cleaner without making it later.**

**Context.** Liddell in New South Wales (NSW) was approved to close by April 2023 (Australian Energy Regulator, 2021) and has since closed. NSW's grid still emits about 640 g CO₂e/kWh (Department of Climate Change, Energy, the Environment and Water [DCCEEW], 2025); Ontario's, with no coal power, emits about 74 (The Atmospheric Fund, 2025). An SMR is a reactor of up to about 300 MWe built largely from factory-made modules (International Atomic Energy Agency, 2024). The BWRX-300 received a Canadian Nuclear Safety Commission (CNSC) licence to construct at Darlington in April 2025 (CNSC, 2025).

**The two sites.** *Darlington, Ontario* is the initiative site: Ontario Power Generation (OPG) plans four units for C$20.9 billion, Unit 1 in service in 2030 (Ontario Power Generation, 2025a); Units 2–4 need further licensing (§8.1). *Liddell* is the Australian comparison, a closed coal site with a grid connection.

**The initiative (C1).** OPG should pilot limestone calcined clay cement (LC³) in eligible non-safety works first, using it in the steel-composite infill only if qualified and schedule-neutral (§4.1–4.3, §5).

**Research questions.**
1. What does one BWRX-300 emit, and where? (§6)
2. How much does C1 save, and what delay cancels it? (§6–7)
3. Does a unit's climate value differ between Ontario and Liddell? (§7)
4. Which barriers decide whether an SMR is built, and does it beat firmed renewables? (§3, §8–9)

---


## 2 Methods and data

**Four methods carry the numbers: a screening life-cycle assessment (LCA), grid displacement with a schedule break-even, a concentration index for fuel supply, and a multi-criteria analysis. Scripts and parameter files regenerate every figure (Appendix A1).** Values are taken from the documents cited, or, where marked "as reported", from the secondary source named. Where readings differ we give the range, and our own assumptions and inferences are labelled as such.

**LCA.** A screening study following ISO 14040/14044 principles (International Organization for Standardization, 2006a; 2006b), not critically reviewed: functional unit 1 MWh of net electricity at the grid connection, cradle to grave (§6.1). The screening model is scripted in Python; a Granta EduPack Eco Audit cross-check was planned but not completed.

**Displacement and schedule.** One unit (300 MWe net assumed; an OPG filing gives 315, within our sensitivity range) supplies 2.365 TWh a year and avoids that output × (grid factor − SMR factor). The *average* factor is the grid's mean intensity; the *marginal* factor is that of the plant displaced (The Atmospheric Fund, 2025). Ontario's are 73.8 and 343 g/kWh; NSW uses 640 (DCCEEW, 2025). Future grids are our trajectories from published anchor points. Start years are 2030 at Darlington (Ontario Power Generation, 2025a) and 2040 at the earliest in Australia (Graham, Hayward and Foster, 2024). The *schedule break-even* is the delay that cancels a saving S: S ÷ (daily output × grid-factor gap) (Appendix B4–B5).

**Supply concentration.** The Herfindahl–Hirschman index (HHI) sums squared percentage market shares (0 to 10,000), by country for mining and by company capacity for conversion and enrichment. Above 1,800 is highly concentrated (US Department of Justice and Federal Trade Commission, 2023; the 2010 scale uses 2,500). Capacity is not contracts, and "without Russia" adds no capacity (Appendix B2).

**Multi-criteria analysis (MCDA).** A weighted sum (Dodgson et al., 2009) scores four options (status quo, one SMR at Liddell, the same SMR built with C1's concrete, firmed renewables) on seven criteria (life-cycle CO₂e, CO₂e avoided per dollar, cost, time to first power, supply concentration, social licence, legal feasibility), each min-max normalised. Four weight sets are our judgement, not elicited. Robustness: each weight ±50%, 20,000 random sets and input changes (Appendix B7).

**Search strategy and patent search:** Appendix E.

---


## 3 Barriers to cutting emissions with small modular reactors

**Eight barriers decide whether a small modular reactor (SMR) is built and cuts emissions. The initiative, C1 (§4.3), reaches one directly and is constrained by a second.** At Darlington, Ontario, cost and schedule bind. At Liddell, the closed New South Wales coal plant we use as the Australian comparison, law comes first and every later barrier is still open (§8.1–8.5).

*Table T1. Eight barriers to SMR deployment, and whether initiative C1 touches them.*
*Source: as cited in each row; working in Appendix B.*

| Barrier | Number and source | Why it matters | Does C1 touch it? |
|---|---|---|---|
| 1. Cost and finance | **C$149–198/MWh** (OPG's figure as reported, Ontario Power Generation, 2026b; this study); NuScale cancelled 2023 (§8.2) | Capital is 65–86% of cost, so financing sets the price | No |
| 2. Time to deploy | **Unit 1 in service 2030**; **2040 at the earliest** in Australia (Ontario Power Generation, 2025a; Graham, Hayward and Foster, 2024) | Late plants displace less CO₂e (§7) | Yes, as a constraint |
| 3. Law | **No more than 36–37 of the 39 Senate votes** needed to repeal the federal bans (Parliament of Australia, 2026) | NSW's own ban would remain | No |
| 4. Fuel-supply concentration | **Enrichment HHI 3,009** (sum of squared market shares) against 1,800 (World Nuclear Association, 2025; US Department of Justice and Federal Trade Commission, 2023) | Russia holds 41–43% of enrichment (§8.3) | No |
| 5. Embodied carbon and qualification | **7.5%** of life-cycle emissions is construction; C1 saves 2,200 t per unit (this study, §6) | Infill concrete needs nuclear qualification before Units 2–4 are fixed (§8.1) | Yes: C1's target |
| 6. Social licence | **59%** wanted the ban kept in 2024 (Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub, 2025) | Support depends on framing; Australia has no consent route (§8.4) | No |
| 7. Workforce | **AUKUS** submarine work competes for the same trades (Joint Standing Committee on Treaties, 2024) | A civil plant would draw on scarce trades (§8.4) | No |
| 8. Waste | **C$26 bn** Canadian repository cost, producer-funded; Australia has no disposal route (Nuclear Waste Management Organization, n.d.) | No spent fuel can be licensed without a route (§8.4) | No |

**Reading the table.** C1 moves only rows 2 and 5; §7 and §8.6 test the schedule risk.

---


## 4 The technology and the initiative

### 4.1 Technology, projects and patents

**No light-water SMR is yet reported operating on land; the BWRX-300 is the Western design closest to doing so, and China's ACP100 (Linglong One) was still in commissioning, with no criticality reported, in May 2026.** Table T2 rates each project on technology readiness levels (TRL): level 8 is a system "completed and qualified through test and demonstration", level 9 one operated across its full range of conditions (US Department of Energy, 2015). The ratings are ours.

*Table T2. Selected SMR-class projects, October 2026.*
*Source: Canadian Nuclear Safety Commission (2025); Ontario Power Generation (2025b); American Nuclear Society (2026); GE Vernova (2026); World Nuclear News (2023); US Nuclear Regulatory Commission (2025); NuScale Power Corporation (2023); TRL ratings: this study.*
*Status entries are as reported by regulators, vendors, utilities and trade press found by web search; we have not opened the primary documents.*

| Project | Design (MWe) | Status | First power | TRL |
|---|---|---|---|---|
| Darlington Unit 1, Ontario | BWRX-300 (300; 315 net in OPG's filing) | Licence to construct April 2025 | October 2030 | 6–7 |
| Darlington Units 2–4 | BWRX-300 (3 × 300) | In the C$20.9 bn budget but unlicensed; approval to proceed expected 2028 | After Unit 1 | 6–7 |
| Clinch River, Tennessee | BWRX-300 (300) | NRC construction permit, 29 September 2026 | Not announced | 6–7 |
| HTR-PM, Shandong | Pebble-bed, gas-cooled (210) | Commercial operation December 2023 | Grid December 2021 | 8–9 |
| Carbon Free Power Project, Idaho | NuScale (462) | Cancelled November 2023; design approved May 2025 | None | 6 |

**Cost, not licensing, stopped NuScale.** Its design was approved in May 2025, yet the first plant was cancelled when the estimate reached US$9.24 bn as reported, about US$20,000/kW (NuScale Power Corporation, 2023). Darlington's C$20.9 bn for 1,200 MW is C$17,400/kW (Ontario Power Generation, 2025a; 2025b); both are first-of-a-kind, in different currencies. Licensing is quickening: Darlington's construction licence took about 29 months and Clinch River's permit 14, probably helped by the joint CNSC–NRC review of the design's composite building (US Nuclear Regulatory Commission and Canadian Nuclear Safety Commission, 2025).

**Patents.** Appendix E, from search summaries only, found isolation-condenser patents assigned to GE-Hitachi and a shaft-construction family that appears to be GE-Hitachi's, but no patent on the diaphragm-plate composite modules. It found no core LC³ composition patent, while Sika and Construction Research & Technology hold applications on LC³ workability and composition. This suggests, but does not establish, that C1's binder risk lies in qualification rather than patents; no freedom-to-operate search was done.

**Australia's earliest date is about 2040.** The Coalition's 2024 plan claimed SMR power by 2035 (ABC News, 2024), whereas CSIRO's GenCost 2023-24 is reported to say 2040 at the earliest (Graham, Hayward and Foster, 2024). Darlington supports CSIRO: with a licensed site and an experienced regulator, it still needs about eight years from licence application (October 2022) to power (October 2030) (Canadian Nuclear Safety Commission, 2026a; Ontario Power Generation, 2025b). Australia must first repeal two federal bans (§8.1), assumed by 2029, and build a licensing regime, assumed to take three years: 2029 + 3 + 8 gives about 2040, matching first power at Liddell (§7).


### 4.2 The BWRX-300 at Darlington

**The BWRX-300's composite building is what C1 targets.** The reactor is rated 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.; 315 MW net in Ontario Power Generation, 2025b), with a 60-year design life (Canadian Nuclear Safety Commission, 2024). The vendor-reported capacity factor is 95% (Fermi Energia, n.d.); we use 0.90 as a first-of-a-kind discount. Fuel is uranium dioxide, reported at 3.8% average and 4.95% maximum enrichment in a preprint review (Sun and Kurosaki, 2025). GE Hitachi states that isolation condensers cool the core passively for seven days without power or operator action (GE Hitachi Nuclear Energy, n.d.). The reactor building sits in a below-grade shaft of diaphragm-plate steel-composite (DP-SC) modules: two steel faceplates tied by diaphragm plates and filled with self-consolidating concrete (SCC) (GE-Hitachi Nuclear Energy, 2024).

**The vendor's concrete claim is hard to reconcile with Ostrołęka.** GE Vernova (n.d.) claims about half the concrete per MW of its larger ESBWR. The Ostrołęka project information sheet gives 50,000 m³ per unit, or 167 m³/MWe (BWRX-300 Ostrołęka sp. z o.o., 2023), against the ESBWR's 69 (Peterson, Zhao and Petroski, 2005). Ostrołęka is only a design proxy for Darlington, and the gap probably reflects the boundary (whole site against nuclear island; our inference). Either way, a small reactor does not mean small concrete (§4.3).


### 4.3 The initiative: low-clinker concrete for the Darlington Units 2–4 infill

**C1 targets a materials problem that modular construction creates, and it is worth doing only if it is schedule-neutral.** The BWRX-300's reactor building is made of diaphragm-plate steel-composite (DPSC) modules: steel shells filled on site with concrete. The infill must flow between closely spaced plates, so we assume a self-consolidating mix, which is cement-rich (our inference; GE-Hitachi Nuclear Energy, 2024, describes the DPSC design). A delay of 11.6–18.5 days to one unit on Ontario's average grid, or 1.7–1.8 days on its marginal grid, cancels that unit's saving (§7.1).

**The proposal.** Ontario Power Generation (OPG) should pilot limestone calcined clay cement (LC³; Scrivener et al., 2018) in eligible non-safety works first, and use it in steel-composite infill only if it is qualified on Unit 1 mock-ups; Units 2–4 need future licensing (§8.1, §8.6). The Ostrołęka BWRX-300 design uses 50,000 m³ of concrete per unit (BWRX-300 Ostrołęka sp. z o.o., 2023). If 20%, 40% or 60% is eligible, replacing ordinary cement with LC³ (380 to 270 kg CO₂e/m³; Pillai et al., 2019) saves 1,100, 2,200 or 3,300 t CO₂e per unit (40% central), and 6,600 t across Units 2–4. A qualified slag blend is the fallback.

*Table T3. Initiative C1: location, scale, application, technology, saving and condition.*
*Source: this study, §6.3; sources as cited in the cells.*

| Element | Specification |
|---|---|
| Location | Darlington New Nuclear Project, Clarington, Ontario; Units 2–4 (Unit 1's basemat is placed) |
| Scale | 50,000 m³ concrete per unit; 20,000 m³ (40%) eligible (BWRX-300 Ostrołęka sp. z o.o., 2023) |
| Application | Non-safety works first; DPSC basemat, shaft-wall and forebay-shaft infill if qualified |
| Technology | LC³ (270 against 380 kg CO₂e/m³; Pillai et al., 2019); slag cement as fallback |
| Saving | 2,200 t per unit (1,100–3,300); 6,600 t for Units 2–4; about 0.36% of a unit's life cycle |
| Condition | Schedule-neutral. Infill qualified under the topical report NEDO-33926, which rests on AISC N690 and ASME rather than mainly CSA N287 (GE-Hitachi Nuclear Energy, 2024; US Nuclear Regulatory Commission and CNSC, 2025); otherwise slag or the current mix |

**Why it is not the obvious choice.** First, the infill problem is specific to modular construction: a mix that flows, stays cool in thick sections and still shields has to be developed (§10). Second, C1's value is set by schedule, not by the concrete: under three weeks of delay to a unit cancels its saving (§7.1), so C1 is a qualification programme timed to Unit 1 mock-ups rather than a binder swap. Third, its lever is financial: the Units 2–4 equity tranche can carry the condition (§8.6).

**What C1 does not address.** It leaves cost, law, fuel supply, social licence and workforce untouched (Table T1); lower-carbon steel in the same structures is the next lever (§6.3, §10).

---


## 5 Materials from extraction to end-of-life

**For C1, the binder's carbon arises in the kiln, but its risks arise in the pour and at decommissioning.** Stages follow §6's boundary; operation, decommissioning and waste use published per-kWh values (§6.1).

*Table T4. C1 binder options from extraction to end-of-life.*
*Source: as cited in the cells.*

| Stage | Portland clinker | LC³ | Slag |
|---|---|---|---|
| Extraction and processing | Limestone and shale burnt in a kiln; M50 concrete 380 kg CO₂e/m³ (Pillai et al., 2019) | Clay calcined near 800 °C, with half the clinker (Zunino, 2021); 270 kg CO₂e/m³ | Iron blast-furnace by-product, ground; 146.6 kg CO₂e/t (Slag Cement Association, n.d.) |
| Construction | Reference mix | Higher superplasticiser demand, lower flow in trials (Universität der Bundeswehr München, n.d.) | Lower heat in thick sections; used in nuclear mixes (Systematic evaluation of concrete placement reliability, 2026) |
| Service | Aggregate swelling, not the binder, dominates radiation damage (Field, Remec and Le Pape, 2015) | Same aggregates, so similar risk (our inference); no LC³ heat data found (§10) | Established |
| Decommissioning | Activated near the core (below) | Europium and cobalt in calcined clay unknown | Not assessed |

**Steel.** Each unit uses 14,000 t (BWRX-300 Ostrołęka sp. z o.o., 2023). Blast-furnace steel emits about 2.33 t CO₂/t and scrap-based electric arc furnace (EAF) steel 0.68 (World Steel Association, 2026). Nuclear plate is not a drop-in, because copper from scrap embrittles vessel steel under irradiation and the CNSC finds the ASME copper limit of 0.2% too loose (Canadian Nuclear Safety Commission, 2023b; US Nuclear Regulatory Commission, 1988).

**End of life.** Activation depends on trace elements, not carbon: cobalt-60 and europium-152 dominate activated shield concrete, and europium-152 exceeded the German clearance level to about 35 cm in the Greifswald shield (Helmholtz-Zentrum Dresden-Rossendorf, n.d.). Most decommissioning concrete is reportedly cleared, leaving only "a few per cent" as waste (Thierfeldt, 2019). On an assumed 2.4 t/m³ and a 2–5% reading, a unit's 50,000 m³ (120,000 t) would leave 2,400–6,000 t of waste. The europium and cobalt content of calcined clay is unknown, so qualification should measure it (§10).


## 6 Life-cycle assessment and eco-audit

One BWRX-300 at Darlington emits an estimated **4.4 g CO₂e per kWh (Monte Carlo median; 90% interval 3.2–6.1; 3.5 if conversion heat takes its central published value)**, below UNECE's 5.1–6.4 g/kWh for nuclear power. The fuel front end contributes 62% and construction 11.5%. The initiative, C1 (§4.3), puts limestone calcined clay cement (LC³) in 20–60% of the concrete. It saves **2,200 t CO₂e per unit (1,100–3,300 t), about 0.36% of the life cycle**: real but small, so worth adopting only if schedule-neutral (§6.3).

### 6.1 Goal, scope and method

**Goal.** Quantify the life-cycle greenhouse-gas emissions of one BWRX-300 at Darlington (Clarington, Ontario), find the hotspots, and size C1's saving. This is a screening LCA following ISO 14040/14044 principles (International Organization for Standardization, 2006a; 2006b), not critically reviewed.

- **Functional unit:** 1 MWh of net electricity at the grid connection (g CO₂e/kWh equals kg CO₂e/MWh); transmission is outside. One unit delivers 300 MWe × 8,760 h × 0.90 × 60 years = **1.419 × 10⁸ MWh** (Appendix A2).
- **Boundary (Figure F1):** cradle to grave. Construction materials and the fuel front end (mining and milling, conversion, enrichment, fabrication) are modelled from published factors; operation and maintenance (O&M), decommissioning and the back end are per-kWh values from EDF's French-fleet study (EDF R&D, 2024).
- **Baseline (S0):** the concrete OPG would pour anyway, at 380 kg CO₂e/m³ (Pillai et al., 2019, as reported; Indian M50 mixes). We have not seen OPG's mix or any cement-type limit in the specification (GE-Hitachi Nuclear Energy, 2024).
- **Cut-offs:** fuel cladding and hardware, conversion chemicals, upstream gas, fuel-plant capital goods and recycling credits; each biases the result low (§6.5). Impact category: climate change, GWP100.

**Method and inventory.** A reproducible Python model multiplies quantities by published emission factors (Appendices A and C). Plant quantities come from the Ostrołęka project information sheet (BWRX-300 Ostrołęka sp. z o.o., 2023, as reported in the project information sheet): **50,000 m³ of concrete and 14,000 t of steel per unit**. This is a design proxy, not confirmed Darlington quantities, and we could not open either the Ostrołęka or the Pillai table. A bottom-up scaling from other reactors (20,700 m³; Peterson, Zhao and Petroski, 2005) is a cross-check (Appendix A3). Key inputs: Table A2b; all 45 ranged inputs: Appendix C2. **A Granta EduPack Eco Audit was planned but not completed; no number here comes from Granta.**

![Figure F1. LCA system boundary for one BWRX-300 at Darlington: fuel front end, construction materials and C1-eligible concrete modelled here; operation, decommissioning and back end from the literature. | Source: this study.](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F1_system_boundary.png){width=95%}

### 6.2 Baseline and hotspots

**One unit emits 4.40 g/kWh (median; 90% interval 3.24–6.05).** With every input at its most likely value (the "mode case") it is 2.86; §6.4 explains the gap. On the expected basis (Figure F2):

1. **Mining and milling: 1.26 g/kWh (28%),** low because Saskatchewan ores are high-grade (Parker, McNaughton and Sparrow, 2016).
2. **Conversion: 1.10 g/kWh (25%),** an *uncertainty* hotspot: published heat demand spans 26–665 kWh per kg of uranium (Gibon and Hahn Menacho, 2023); at the most likely value conversion is only 0.13 g/kWh.
3. **Back end: 0.65 g/kWh (15%),** transferred from France, which reprocesses; Canada plans direct disposal (Nuclear Waste Management Organization, 2024a), so this may be high.

The back end and decommissioning add 18%, O&M 9% and **construction 11.5%** (0.52 g/kWh; 7.2–17.8% across draws). The C1-eligible concrete is only 1.9% of the mode-case total, so **C1 acts on about one-fiftieth of the footprint**.

The vendor claims about 50% less concrete per unit of energy than the ESBWR (GE Vernova, n.d.), while small plants usually lose economies of scale; Ostrołęka's 167 m³ per MWe, 2.4 times the ESBWR's 69 (Peterson, Zhao and Petroski, 2005), sides with scale. The cross-check gives 4.20 g/kWh, so the re-base adds about 0.2 g/kWh, all in construction. Per MWh the plant uses 0.85 kg of concrete, 0.099 kg of steel, 20.7 g of natural uranium and 0.0146 separative work units (Appendix A8).

![Figure F2. Life-cycle emissions of one BWRX-300 by stage: expected value 4.49 g CO₂e/kWh (Monte Carlo mean), with the mode case (every input at its most likely value, total 2.86) marked. | Source: this study, Appendix C3.](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F2_stage_breakdown.png){width=95%}

### 6.3 The initiative against the baseline

**C1 is low-clinker concrete: LC³ on eligible non-safety works first and on the steel-composite infill only if qualified, a slag blend as the fallback, specified only if schedule-neutral (§4.3).** Pillai et al. (2019, as reported) give 380 kg CO₂e/m³ for ordinary concrete and 270 for LC³, a cut of 110 kg/m³ (28.9%). The eligible share is our scenario, not data, and drives the result. At 20, 40 and 60% of 50,000 m³, C1 saves **1,100, 2,200 and 3,300 t per unit, or 0.18, 0.36 and 0.54% of its life cycle** (Table T5). Letting eligibility, the cut and the volumes vary together gives 2,217 t (1,375–3,294) per unit. Only Units 2–4 count, because Unit 1's basemat is placed.

*Table T5. C1 saving against the baseline, per unit and for Units 2–4; share of life cycle is the Monte Carlo median (5th–95th percentile). Source: this study, Appendices A6–A7 and C4.*

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

![Figure F3. One-at-a-time sensitivity of life-cycle intensity (left, centred on the 2.86 g CO₂e/kWh mode case) and of C1's saving per unit (right, centred on 2,200 t), top ten inputs each. | Source: this study, Appendix C2.](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F3_tornado.png){width=95%}

**Monte Carlo (Figure F4): why we report 4.4, not 2.9.** Several inputs can mostly only rise: conversion heat is most likely 26 kWh/kg U but could be 665, which alone adds about 1.0 g/kWh to the mean (Appendix C5). We therefore quote the median. **The headline depends on how conversion heat is distributed:** fixed at Gibon and Hahn Menacho's (2023) central 26 kWh/kg U, the median is 3.51 g/kWh (2.80–4.39); log-uniform over 26–665, 4.11 (3.06–6.12). We quote the **range of medians, 3.51–4.40**. A measured conversion value would settle it. Draws are independent and many ranges are judgement (Appendix C6).

![Figure F4. Monte Carlo distributions (20,000 draws) of life-cycle intensity (median 4.40, 5th–95th percentile 3.24–6.05 g CO₂e/kWh) and of C1's saving per unit at central eligibility. | Source: this study, Appendix C4.](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F4_montecarlo.png){width=95%}

### 6.5 Comparison with published values

**Our median (3.5–4.4 across conversion-heat assumptions) is below UNECE's 5.1–6.4 g/kWh (United Nations Economic Commission for Europe, 2021), though our 90% interval overlaps it, and sits at the low end of the wider literature for reasons we can identify (Figure F5).** It overlaps EDF's French fleet (3.7; EDF R&D, 2024) and is below the global average of 6.1 (Gibon and Hahn Menacho, 2023), an SMR estimate of 9.1 (Carless, Griffin and Fischbeck, 2016), the harmonised light-water-reactor median of 12 (Warner and Heath, 2012) and the IPCC AR5 median of 12, as commonly quoted from a 3.7–110 range (Schlömer et al., 2014). Gas combined cycle (403–513 g/kWh) and coal (751–1,095) are 90–120 and 170–250 times higher (United Nations Economic Commission for Europe, 2021).

**Three reasons explain most of the gap** (sizes in Appendix C7):
1. **Ore grade:** our mining is 1.0–1.3 g/kWh, against about 2.8 at global-average grades (Gibon and Hahn Menacho, 2023).
2. **Enrichment:** centrifuges at 50 kWh per separative work unit, against about 2,500 for the diffusion plants in older study sets.
3. **Cut-offs and long life:** excluded inputs and a 60-year life bias the result low; at 40 years the mode case rises from 2.86 to 3.07 g/kWh.

Construction is now 0.41 g/kWh at the mode case (median 0.50), close to EDF's roughly 0.59 for large reactors (16% of 3.7). The known low bias would raise the total and shrink C1's share, so it does not weaken §6.3.

![Figure F5. Our result against published nuclear life-cycle values (dot = central or median; line = range or interval). UNECE is a range only. Coal (about 750–1,100) and gas (403–513) are off the scale. | Source: this study; EDF R&D (2024); United Nations Economic Commission for Europe (2021); Gibon and Hahn Menacho (2023); Carless, Griffin and Fischbeck (2016); Warner and Heath (2012).](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F5_benchmarks.png){width=95%}

---


## 7 Carbon avoided: Ontario vs Liddell, the value of schedule, and the same money on firmed renewables

**For C1, schedule matters far more than concrete.** A one-month slip of Units 2–4 costs C$33–110 m in carrying cost alone, 29–175 times the carbon value of C1's whole saving, and defers about C$88 m of output. C1's 2,200 t per unit (1,100–3,300; §6.3) is cancelled by 11.6–18.5 days of delay on Ontario's average grid factor, or 1.7–1.8 days on its marginal factor. Timing also decides where an SMR helps the climate: a Darlington unit avoids about as much CO₂e to 2050 as one at Liddell, and firmed renewables beat both on the same money (Appendix B4–B6).

### 7.1 The value of schedule

A unit that starts late gives up each day's displacement (Table T6). Counted to 2050 (the "gross" view) the loss is permanent. Over the plant's whole life (the "net" view) the lost time returns at end of life, but on a cleaner grid.

*Table T6. Days of delay that cancel C1's saving of 2,200 t per unit (1,100–3,300), Darlington Units 2–4, start 2035.*
*Source: this study, Appendix B5; inputs (BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019); grid factors (The Atmospheric Fund, 2025).*

| Ontario grid case | CO₂e lost per day, one unit (t, gross / net) | Days that cancel one unit's saving (gross / net) | Days to one unit that cancel all Units 2–4's saving (gross / net) |
|---|---|---|---|
| Average, falling to 15 g/kWh by 2040 | 189 / 119 | 11.6 (5.8–17.5) / 18.5 (9.2–27.7) | 35 / 55 |
| Marginal (gas), leaving the margin by 2050 | 1,296 / 1,226 | 1.7 (0.8–2.5) / 1.8 (0.9–2.7) | 5.1 / 5.4 |

**In money the gap is wider.** At Canada's industrial carbon price of C$95/t in 2026 and C$115/t in 2030 (Environment and Climate Change Canada, 2026), the 6,600 t saved across Units 2–4 is worth C$0.63–0.76 m. A one-month slip of the three units costs C$33–110 m in carrying cost (3–10% a year on C$13.2 bn, an upper bound) and defers about C$88 m of output at OPG's C$149/MWh (Ontario Power Generation, 2026b). The carbon value is also only a shadow price: construction materials appear to fall outside Ontario's industrial carbon pricing (our inference; §8.2), so no one is paid for it. **Schedule neutrality is therefore the binding condition on C1.** The mix must be qualified on Unit 1 mock-ups before the Units 2–4 decision expected in 2028 (§8.6).

### 7.2 What one BWRX-300 displaces: Darlington vs Liddell

**At today's grid factors, a unit at Liddell would avoid about nine times more CO₂e than one at Darlington. Timing closes most of that gap.** One unit avoids 1.50 Mt a year on the NSW average of 640 g/kWh (DCCEEW, 2025). On Ontario's 2024 average of 73.8 g/kWh it avoids 0.165 Mt (9.1× less), and on Ontario's marginal factor of 343 g/kWh it avoids 0.80 Mt (1.9× less) (The Atmospheric Fund, 2025).

The two plants would not run in the same years. Darlington Unit 1 is planned to enter service in 2030 (Ontario Power Generation, 2025a). Australia's earliest date for nuclear is 2040 (Graham, Hayward and Foster, 2024), against the Coalition's 2035 as reported (ABC News, 2024). If coal leaves the NEM by 2038, as in AEMO's Step Change scenario (Australian Energy Market Operator, 2024), a 2040 unit displaces only a residual mix of 30 g/kWh (assumed).

To 2050 (Figure F6), Darlington Unit 1 avoids **1.0–6.8 Mt** and Liddell **0.67–3.9 Mt**. Liddell wins clearly only if the NEM stays at 640 g/kWh (16.5 Mt).

The grid trajectory, start year and post-coal floor move these results tenfold; capacity factor, net output and our life-cycle interval move them by a few per cent (Appendix B4). An SMR at Liddell would displace the NEM mix, not Liddell's coal (§1).

**An SMR's climate value depends on when it runs and what it displaces, not on today's coal share.** In Ontario the case rests on displacing marginal gas. At Liddell it rests on the NEM decarbonising slowly.

![Figure F6. CO₂e avoided to 2050 by one BWRX-300: Darlington Unit 1 (from 2030) against Liddell (from 2035 or 2040), by grid case; hatched bars are upper bounds. | Source: this study, Appendix B4 (Table B17)](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F6_displacement.png){width=95%}

### 7.3 The same money on firmed renewables

**At GenCost's 2030 costs, the money for one SMR unit would buy about 2.9 times as much energy from firmed renewables, which would avoid about 11 times more CO₂e to 2050 at Liddell.**

GenCost 2023-24 gives A$230–382/MWh for an SMR in 2030, against A$89–125 for solar and wind with integration costs (Graham, Hayward and Foster, 2024, as reported). At the midpoints the same spend buys 2.9× the energy (Figure F7). With renewables from 2028 (assumed) and the SMR from 2040 on the slower trajectory, renewables avoid **10.9×** more CO₂e to 2050. They still avoid 5.7× more in the worst case we tested for them (SMR A$230, renewables A$153), and 4.9× with the SMR at A$198 (Appendix B6, Table B28). If A$387–641 is the 2030 range instead, the ratios become 5.0× and 19.1×.
Renewables come out ahead because they are cheaper per MWh and start about a decade earlier. Two limits apply: that much new output would itself shift the grid trajectory, and integration costs rise beyond the shares GenCost models. **On carbon per dollar, an SMR at Liddell loses.** Its case rests on firm supply, land use, system security and a hedge against renewables or transmission falling behind, which §9 weighs.

![Figure F7. Same money at Liddell: firmed renewables ÷ one SMR unit, as energy bought and CO₂e avoided to 2050, under four cost cases; the dashed line is parity. | Source: this study, Appendix B6 (Table B28)](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F7_same_money.png){width=95%}

---


## 8 Non-technical factors affecting translation to practice

### 8.1 Law, regulation and licensing

Law is where Darlington and Liddell differ most. At Darlington, C1 starts with LC³ in non-safety concrete and extends to the steel-composite infill only if qualified before the Units 2–4 go-ahead expected in 2028 (American Nuclear Society, 2026, as reported). At Liddell, three laws and the site owner block an SMR (Table T7).

**Australia.** Federal repeal fails in the Senate while Labor and the Greens oppose, so the Coalition's pledge to "repeal all legislative prohibitions" (Liberal Party of Australia, 2026) cannot pass unless one of them changes position. Repeal alone would not be enough: ARPANSA licenses only Commonwealth-controlled bodies (ARPANS Act s 13), so a private SMR at Liddell would remain an offence under NSW s 8. Only a Commonwealth-owned operator might fit the s 8(3) exemption that covers ANSTO (our inference).

**Canada.** The construction licence (April 2025) covers one unit. The Canadian Nuclear Safety Commission (CNSC) reports that its first construction hold point was removed in March 2026, and OPG applied that month to operate Unit 1 (CNSC, 2026a; 2026b). Units 2–4 are not covered by the first licence, so they need a further authorisation, with C1 reviewed inside it. The review depends on safety class. Concrete in a non-safety auxiliary structure meets ordinary construction requirements, but infill in a safety-significant structure may alter the licensed design basis and needs a fuller demonstration. REGDOC-2.5.2 (version 2.1) sets risk-informed design requirements and classifies structures (CNSC, 2023a), so no containment standard should be applied to every structure. The cement standard already allows calcined-clay blends with up to 15% limestone (CSA Group, 2023; Hooton, 2023). The BWRX-300 containment is steel-plate composite, so the infill is governed by GE-Hitachi's topical report NEDO-33926 (self-consolidating concrete, strength per draft AISC N690), which the CNSC and US NRC jointly reviewed (GE-Hitachi Nuclear Energy, 2024; US Nuclear Regulatory Commission and CNSC, 2025). CSA N287 applies only to concrete containment, where applicable (CSA Group, 2026). To our reading the public report does not state a cement-type limit, and we found no nuclear precedent for calcined-clay infill: that is C1's real licensing risk. A lower carbon figure cannot override the acceptance criteria for strength, crack control or design life.

**Translation to practice.** The non-safety pilot needs no nuclear qualification. Infill qualification must start in 2027, with slag (S1) as the fallback (§8.6). At Liddell the barrier precedes any materials choice: none of these first-order barriers can be solved by changing Portland cement to LC³.

*Table T7. Legal barriers to an SMR at Liddell and the Darlington equivalent. No row is resolved as at October 2026.*
*Source: legislation as named; Appendix B1; Canadian Nuclear Safety Commission (2021; 2022; 2025).*

| Barrier | Liddell (NSW) | What removes it; veto holder | Darlington (Ontario) |
|---|---|---|---|
| 1. Federal bans | *EPBC Act 1999* (Cth) s 140A bars approval; *ARPANS Act 1998* (Cth) s 10 bars a licence | Amend both. Senate: about 39 votes needed, at most 37 in favour; Labor and the Greens opposed (Appendix B1.2; Parliament of Australia, 2026) | Licence to construct in about 29 months, against 24–32 expected (CNSC, 2022; 2025) |
| 2. Regulator for a private reactor | None: no body licenses private power reactors, and NSW has no nuclear regulator | Commonwealth-owned plant, new federal regulator or NSW regulator (Appendix B3); the naval regulator began in November 2025 (Minister for Defence, 2025) | CNSC is established; Units 2–4 need a further authorisation (CNSC, 2026a) |
| 3. NSW ban | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8 makes building a reactor an offence; s 9 bars state approval | NSW repeal (passed the Council 6 May 2026, stalled in the Assembly, lapses 28 November 2026; Parliament of New South Wales, 2026) or a Commonwealth override under Constitution s 109 | Unit 1 approved 8 May 2025 (Government of Ontario, 2025) |
| 4. Site | AGL owns Liddell and has ruled out nuclear there (Newcastle Herald, 2024a) | AGL's consent, or Commonwealth acquisition | OPG holds the site licence (CNSC, 2021) |

---


### 8.2 Economics, finance and market barriers

An SMR's cost is mostly capital, so whoever finances it sets its price and decides who can build one. C1 is the opposite: it costs almost nothing, but no one is paid for the carbon it saves.

**Cost.** Darlington's C$20.9 bn budget for four 300 MWe units (Ontario Power Generation, 2025a) gives a levelised cost of electricity (LCOE: the constant price that repays every cost over the plant's life) of C$198/MWh at a 7% real discount rate, and C$112–280 from 3% to 10% (Table T8). Capital is 65–86% of it, so finance terms matter as much as engineering. OPG's C$149/MWh implies 4.9%, a regulated Crown utility's cost of capital. Our A$221 at 7% sits just below GenCost's 2030 SMR range (Graham, Hayward and Foster, 2024), plausibly because four units share infrastructure. The agreement is not independent, because GenCost's current edition bases its SMR capital cost on Darlington (Graham and Hayward, 2026). A NuScale-size overrun would give C$317/MWh.

**Risk and finance.** NuScale's Idaho project shows what happens when buyers carry overrun risk: its price rose about 35% in real terms even after tax credits, the Utah utilities did not subscribe, and it was cancelled in 2023 (Table T8). Darlington avoids this with a single Crown owner and a regulated rate base; public and First Nations finance covers about 22% of the budget (§8.5). The second equity tranche is released for Units 2–4 "once project milestones are met" (Canada Growth Fund and Building Ontario Fund, 2025), which is C1's main financial lever.

**Barriers to entry.** About C$17,400/kW is at risk for years before any revenue. Equity markets value US developers on hoped-for orders (NuScale at 168 times its revenue; NuScale Power Corporation, 2026), but first plants are financed by states and rate bases: the US Department of Energy's US$800 m went to two designs, one the BWRX-300 (US Department of Energy, 2025), out of about 70 worldwide (International Atomic Energy Agency, 2024). China's State Council approves batches of reactors for state-owned builders, as reported (Caixin Global, 2026). Australia has neither route. Liddell belongs to AGL, a private company, so an SMR there would need Commonwealth ownership or underwriting, with taxpayers carrying the cost risk (our inference).

**C1.** LC³ saves 6,600 t CO₂e across Units 2–4 (2,200 t a unit; §6.3), worth C$0.63–0.76 m at the federal carbon price of C$95/t in 2026 and C$115/t in 2030 (Environment and Climate Change Canada, 2026; BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019). That justifies an LC³ premium of up to C$10.4–12.7/m³, or 4.6–5.5% of commodity concrete at C$229/m³. The target concrete costs about C$13.7 m, 0.10% of Units 2–4 capital. No one captures the carbon value, because construction materials appear to sit outside Ontario's industrial carbon pricing (our inference). Qualification sets the abatement cost: a C$1 m programme (assumed) adds about C$152/t, above the C$95–115/t price path, and one day of delay costs C$1.8–2.9 m, more than C1's whole carbon value. Responses are compared and sequenced in §8.6 (Table T12).

*Table T8. Cost evidence for an SMR: our Darlington estimate against published values.*
*Source: this study, Appendix B6.3; Ontario Power Generation (2025a; 2026b); Graham, Hayward and Foster (2024); Rao, Kaffine and Hodge (2026); Steigerwald et al. (2023).*

| Measure | Value | What it shows |
|---|---|---|
| Our Darlington LCOE, real, 60-year life | C$112 / 151 / **198** / 280 per MWh at 3 / 5 / 7 / 10% | Finance terms move it 2.5-fold |
| OPG's reported four-unit LCOE | C$149/MWh (2024 dollars); ours matches at 4.9% real | A regulated utility's cost of capital |
| GenCost 2023-24, 2030: SMR / large nuclear / firmed solar and wind | A$230–382 / 141–233 / 89–125 per MWh | Our A$221 sits just below the SMR range |
| Capital cost: vendor BWRX-300 vs Darlington | US$2,250/kW vs about US$12,600/kW | Vendor figures are a fifth of budget |
| NuScale Carbon Free Power Project, Idaho, 2020 to 2023 | Price US$58 to 89/MWh; cost US$5.3 bn to 9.24 bn; cancelled November 2023 (NuScale Power Corporation and Utah Associated Municipal Power Systems, 2023; Schlissel, 2023) | Buyers leave when they carry overruns |

---


### 8.3 Supply concentration and geopolitics

Every front-end fuel stage we measured is concentrated. Each Herfindahl–Hirschman index (HHI; §2) exceeds 1,800, "highly concentrated" on the 2023 US merger guidelines (US Department of Justice and Federal Trade Commission, 2023), though on the 2010 scale only enrichment is (Table T9). For Darlington this is a price risk; for an Australian SMR it is a sovereign risk.

**Sanctions make it worse.** Russia holds 41.0–42.8% of enrichment capacity (calculated from World Nuclear Association, 2025; World Nuclear University, 2025). Removing Russia, as US buyers must once import-ban waivers end in 2028 (United States Congress, 2024), raises every HHI. Without Russia and China, enrichment is a Urenco–Orano duopoly (HHI 5,621). Mining is concentrated by country but not by company (HHI about 850–1,400, top three firms only), so its risk is geopolitical rather than market power (Appendix B2).

**Darlington and Liddell compared.** OPG's announced Unit 1 fuel suppliers (Cameco, Urenco USA, Orano, GNF-A) include no Russian firm (Ontario Power Generation, 2023, as reported by Power Engineering, 2023). Four units need about 196 t of natural uranium and 138 thousand separative work units (SWU) a year, about 3.2% of Urenco USA's output (assumed typical BWR fuel values; Appendix B2.6). Australia holds 28% of identified recoverable uranium resources (OECD Nuclear Energy Agency and International Atomic Energy Agency, 2025; the 2026 edition gives 27–29%) but has no conversion or enrichment (World Nuclear Association, 2026). An Australian SMR would import enrichment and fabrication by law (EPBC s 140A; ARPANS s 10), and conversion because no plant exists (Parliamentary Library, 2024).

**Translation to practice.** C1 does not reduce fuel risk. Fuel independence also needs conversion, enrichment, fabrication, forged components and skilled labour, not uranium deposits alone. Patents identify proprietary designs but do not establish any royalty per unit of electricity, so patent counts alone give no royalty estimate. The HHI measures nominal capacity, not the contracts open to one buyer. Contracts with allied enrichers, as OPG uses, cut a buyer's exposure but not concentration (§8.6). C1 adds a small supply risk of its own. LC³ needs a suitable calcined-clay source and blending capacity (Scrivener et al., 2018), and a single qualified supplier would be a risk even if its product footprint were favourable. One Western option links back to Darlington: laser enrichment from Australia's Silex Systems, commercialised in the US by Global Laser Enrichment (51% Silex, 49% Cameco, OPG's uranium supplier). The NRC docketed its Paducah application in August 2025, as reported by Silex Systems Limited (2025), and Cameco has agreed to buy all its output (Silex Systems Limited, 2026, as reported by World Nuclear News, 2026). EPBC s 140A would bar such a plant in Australia (§10).

*Table T9. Herfindahl–Hirschman index (HHI) of the uranium front end, by stage, with and without Russia and China.*
*Source: this study, Appendix B2, from World Nuclear Association (2024; 2025; 2026).*

| Stage (measure, base year) | HHI | Class (2023 / 2010) | Russia's share | HHI without Russia | HHI without Russia and China | Australia's share | Canada's share |
|---|---:|---|---:|---:|---:|---:|---:|
| Mining (output by country, 2024) | 2,341 | High / Moderate | 4.5% | 2,546 | 2,686 | 7.6% | 23.8% |
| Conversion (capacity by company) | 2,111 | High / Moderate | 20.2% | 2,674 | 3,615 | 0% | 20.2% |
| Enrichment (capacity by company, 2025) | **3,009** | **High / High** | **42.8%** | 3,599 | **5,621** | 0% | 0% |

*Note: High is above 1,800 (2023) and above 2,500 (2010). Sensitivity and limits: Appendix B2.4–B2.5.*

---


### 8.4 Social licence

The same reactor has a social licence at Darlington and none at Liddell. Safety data do not explain the difference; consent, benefit and trust do (Table T10).

**Perceived and actual safety.** In 2024, 61% of Australians supported using nuclear power to generate electricity (Neelam, 2024), yet 59% wanted to keep the legal ban, up from 51% a year earlier (Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub, 2025). One poll asks about a technology and the other about the law, so support depends on framing; older polls found support 16–20 points lower for a plant nearby (Newspoll, 2007). The health benefit, like the carbon benefit (§7), depends on what the reactor displaces.

**Consent: equity in Canada, failed top-down siting in Australia.** At Darlington the CNSC found the duty to consult met (CNSC, 2025). In June 2026 the seven Williams Treaties First Nations agreed to lend C$700 m to the project, converting to equity once all four units are complete, guaranteed half each by federal and Ontario programmes (Williams Treaties First Nations et al., 2026). Two of the seven told the CNSC in 2023–24 that their concerns had not been addressed, so equity is a means of consent, not a substitute for it. Australia's precedent is a waste site chosen top-down and set aside by the Federal Court for apprehended bias (*Barngarla Determination Aboriginal Corporation RNTBC v Minister for Resources* [2023] FCA 809). Canada's waste agency instead used volunteer siting and a priced hosting agreement (Nuclear Waste Management Organization [NWMO], 2024a). Scored on legitimacy, legal risk, speed, public cost and fairness, consent-based routes beat top-down siting by 3–6 points under every weighting, and not building scores highest (Appendix B8.3).

**Translation to practice.** C1 changes no land use, emissions or waste, so it raises no new consent issue; its social value is indirect, as a lower-carbon build that OPG can report to its First Nations and public equity partners (our inference). For Liddell, low-regret steps can precede any repeal: a producer-funded waste body, and a two-key test in which both the host community and the Traditional Owners must agree. A priced hosting agreement, First Nations equity with a loan guarantee and a skills plan coordinated with AUKUS would follow (§8.6).

*Table T10. Social licence at Darlington and at Liddell.*
*Source: as cited in each cell; full source list in Appendix B8.*

| Factor | Darlington, Ontario | Liddell, NSW (hypothetical) | Effect on translation to practice |
|---|---|---|---|
| Deaths per TWh; deaths avoided per unit-year | Nuclear 0.03 vs gas 2.82 (Ritchie, 2020): about 6.6 avoided if gas is displaced | Coal 24.62: about 58, an upper bound; about zero against wind or solar (Markandya and Wilkinson, 2007) | Nuclear is about 820 times safer than coal, yet "dread" risk factors keep acceptance low (Slovic, 1987); Appendix B8.1 |
| Traditional Owners and consent | Williams Treaties First Nations; duty to consult met; C$700 m loan converting to equity (Williams Treaties First Nations et al., 2026) | Wonnarua people: no public position located in our searches, itself a finding; no process | Canada has a funded way to say yes; Australia has none |
| Residual dissent and litigation | Scugog Island and Curve Lake raised unmet concerns in 2023–24 (Mississaugas of Scugog Island First Nation, 2023; Curve Lake First Nation, 2024) | Kimba ballot 61.6% yes, Barngarla excluded; declaration set aside (*Barngarla* [2023] FCA 809) | Excluding Traditional Owners left the declaration open to challenge |
| Waste route | Volunteer siting from 2010: 22 communities to 1; Ignace vote 77%; C$170 m over 81 years to the host; C$26 bn paid by producers (NWMO, 2024c; n.d.) | No disposal route, even for research-reactor waste | Waste is a hard gate for Liddell |
| Workforce | About 1,600 construction and 200 operating jobs per SMR (Conference Board of Canada, 2021); unions support (Power Workers' Union, 2021) | No civil nuclear workforce; AUKUS needs about 20,000 jobs over 30 years (Joint Standing Committee on Treaties, 2024) | A civil SMR would compete with AUKUS for scarce trades |

---


### 8.5 Stakeholders and money flows

At Darlington none of the seven high-power actors opposes the project; at Liddell three of the four do (the Commonwealth, NSW and AGL), and the only strong supporter, the federal Coalition, is in opposition. Our power-weighted stance scores (−2 to +2; our judgement, not survey data; Figure F8; Appendix B8.2) are +1.07 and −1.03.

Money follows the same pattern (Table T11). OPG carries about 78% of Darlington on its balance sheet (by subtraction; our calculation), recovered through rates the Ontario Energy Board approves, while federal, provincial and First Nations finance lowers the cost of capital and spreads ownership. That model needs a publicly owned utility with a regulated rate base. Liddell has a private owner, so it would need Commonwealth ownership or underwriting (§8.2), with taxpayers carrying the cost risk under the Coalition's 2024 model, as reported by ABC News (2024).

For C1, the decisive actors are OPG as buyer, GE Vernova Hitachi as owner of the infill specification, and the two equity funds at the Units 2–4 tranche (§8.2). None is opposed, but none yet has a reason to act; the tranche condition supplies one (§8.6).

![Figure F8. Stakeholder power/interest maps for Darlington Units 2–4 with C1 (left) and a hypothetical Liddell BWRX-300 (right). Colour shows stance; positions are our judgement from §8.1–8.4. Source: this study, Appendix B8.2.](/home/user/MTE4593-Group-Assignment/03_LCA_Calculations/results/F8_stakeholder_map.png){width=95%}

*Table T11. Who pays and who earns: the C$20.9 bn Darlington New Nuclear Project.*
*Source: as cited in each row; shares calculated in Appendix B8.4.*

| Flow | Who pays | Who earns | Amount (share) |
|---|---|---|---|
| OPG's share, recovered through Ontario Energy Board-approved rates | OPG, repaid by Ontario ratepayers (Ontario Power Generation, 2025b) | GE Vernova Hitachi, construction partners, suppliers | C$16.2 bn (78%) |
| Phase 1 loan | Canada Infrastructure Bank (2022) | The project; the bank earns interest | C$0.97 bn (4.6%) |
| Equity in two tranches | Canada Growth Fund and Building Ontario Fund (2025) | Returns on stakes of up to 15% and 7.5% | C$3.0 bn (14.4%) |
| Loan converting to equity | Williams Treaties First Nations; guarantors carry default risk (Williams Treaties First Nations et al., 2026) | First Nations equity returns | C$0.70 bn (3.3%) |

---


### 8.6 Implementation pathway

**C1 can be built with no added delay on the evidence available if OPG applies a carbon specification to eligible non-safety concrete now (the LC³ pilot), qualifies the steel-composite infill on a Unit 1 mock-up, and ties a milestone to the Units 2–4 equity tranche.** The levers in Table T12 are scored on enforceability, speed and low schedule risk (1 to 3 each; our judgement, not sourced scores). L1 and L2 tie at 8. If enforceability counts double, L2 leads with 11; if speed counts double, L1 leads with 11; the recommendation is the same under both. L1 is C1's pilot step, not an add-on: a 10% floor invites LC³, whose full saving is 1,100–3,300 t CO₂e per unit (§4.3; Pillai et al., 2019).

*Table T12. Levers for putting C1 into practice, compared.*
*Source: our evaluation from Treasury Board of Canada Secretariat (2022); Canada Growth Fund and Building Ontario Fund (2025). Scores are our judgement (Appendix B3.1).*

| Lever | Who pays | Binding on OPG? | Time | Schedule risk | Score (enforceability / speed / low risk) |
|---|---|---|---|---|---|
| L1. OPG specification: environmental product declarations (EPDs) and concrete at least 10% below the regional baseline, with a cap on emissions; non-safety concrete first | OPG, so ratepayers (premium break-even, §8.2) | Yes (own contracts) | Next procurement round (2027) | Low | 2 / 3 / 3 = **8** |
| L2. Units 2–4 equity-tranche milestone: EPD disclosure and a reduction target, with a schedule-neutral exemption | The funds; no cash cost | Yes, if the funds agree | With tranche 2 (around 2028) | Low, if the exemption is written in | 3 / 2 / 3 = **8** |
| L3. Ontario shareholder direction to OPG | Ratepayers, after Ontario Energy Board review | Yes | Months | Depends on wording | 3 / 2 / 2 = 7 |
| L4. Public funding for qualification on the Unit 1 mock-up (assumed C$1–3 m) | Federal or Ontario research budget | No | 2027 | Removes the main schedule risk | — (enabling step for L1's infill extension) |

**Qualification and sequencing.** The sequence is L1 now, L4 in 2027, then L2 at the 2028 tranche. A CNSC licence condition is not a lever, because the CNSC does not set climate conditions; it only has to accept that the change is safe (our inference). Step 1, in 2027, develops slag and LC³ self-consolidating mixes (about 6 to 9 months). Step 2 is a full-scale mock-up trial off Unit 1's critical path (about 6 months), funded by L4. Step 3 is the design-change evaluation, submitted with the Units 2–4 licensing package ahead of the approval expected in 2028, as reported (American Nuclear Society, 2026); it takes about 6 to 9 months (assumed). The steps total about 18 to 24 months (assumed), so they fit only if they start in 2027. We have not costed the programme; §9 tests an assumed C$1 m. If the evidence is not ready, Units 2–4 proceed with the current mix, the pilot continues in non-safety concrete, and the infill enters at a later unit. Doing nothing forgoes the saving at near-zero cost and is rejected.

**The federal standard is a template, not an obligation.** The Standard on Embodied Carbon in Construction binds federal departments (Treasury Board of Canada Secretariat, 2022); OPG, an Ontario Crown corporation, is outside its scope (our inference). Its allowance of 130% of baseline for specialised mixes could let self-consolidating infill emit 30% more than the baseline, so any OPG or fund clause must benchmark infill against a cement-rich self-consolidating reference mix.

---


## 9 Triple-bottom-line evaluation and multi-criteria analysis

**Adopt C1 only as a schedule-neutral specification; for Australia, the same money on firmed renewables ranks first, ahead of the status quo and of an SMR at Liddell.** C1 changes the life cycle by about 0.36%, and no predefined weight set, input test or ±50% weight test puts an SMR first.

### 9.1 Triple bottom line

Table T13 applies the triple bottom line to C1 at Darlington and to the comparison at Liddell, each cell traced to its section.

*Table T13. Triple-bottom-line summary: C1 at Darlington Units 2–4 and one BWRX-300 at Liddell.*
*Source: this study, from the sections cited.*

| | Darlington, with C1 | Liddell (one unit) | Traced to |
|---|---|---|---|
| **Environment** | About 4 g CO₂e/kWh (§6). C1 saves 2,200 t per unit, about 0.36% of the life cycle; Unit 1 avoids 1.0–6.8 Mt to 2050. | Avoids 0.67–3.9 Mt to 2050, from about 2040. Firmed renewables avoid 10.9× more per dollar. | §6.3, §7 |
| **Economy** | LCOE C$198/MWh at 7%. C1's carbon value (C$0.63–0.76 m, Units 2–4) is less than one day of delay (C$1.8–2.9 m). | SMR A$230–382/MWh in 2030 against A$89–125 for firmed renewables. A first unit would need Commonwealth ownership or underwriting (our inference, §8.2). | §7.3, §8.2 |
| **Society** | Stance +1.07; no high-power actor opposed. Williams Treaties First Nations lend C$700 m, converting to equity. C1 adds no consent issue. | Stance −1.03; 59% want the ban kept. No legal route is open. Enrichment and conversion would be imported. | §8.1, §8.3–8.5 |
| **Net** | Marginal gain; feasible if schedule-neutral (break-even 11.6–18.5 days). | Not feasible before 2040 on current law, cost and consent. | §6–§8 |

### 9.2 Multi-criteria analysis

Method in §2; working in Appendix B7; social-licence and legal scores from Appendix B8.3 and B3. Technology readiness level (TRL) is not scored.

*Table T14. MCDA total scores (0–100) by weight set, and first-place tests.*
*Source: this study, Appendix B7. SMR + C1 is the 2,200 t case. Social, legal and weight inputs are our judgement.*

| Option | Equal | Climate and cost | Firm and sovereign | Host community |
|---|---:|---:|---:|---:|
| Firmed renewables, same money | **80.1** | **85.9** | **63.7** | **89.3** |
| Status quo | 52.4 | 41.7 | 60.0 | 55.0 |
| One SMR at Liddell | 29.7 | 24.0 | 43.6 | 20.4 |
| SMR + C1 | 29.7 | 24.0 | 43.6 | 20.4 |
| First place changed by a ±50% change in one weight (of 14 tests) | 0 | 0 | 2 | 0 |

**Renewables rank first under every weight set.** The SMR wins only on life-cycle CO₂e (about 4 against 30 g/kWh) and supply concentration. It loses on CO₂e avoided per dollar (10.9×), cost (2.9×), time (about 12 years later), social licence and legal feasibility.

**Rank reversal.** Of 56 weight changes of ±50%, two change first place, both under the firm-and-sovereign weights and both to the status quo, not the SMR. An SMR ranks first only if life-cycle CO₂e carries at least 94% of the weight, or in 0.1% of 20,000 random weight sets. Of 68 input tests, renewables stay first in 66; the other two go to the status quo.

**SMR + C1 and SMR are indistinguishable.** At 2,200 t per unit (50,000 m³ of concrete, 40% eligible; BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019), C1 moves the weighted score by under 0.005 point, and the ranking is unchanged. At Liddell, an 18.5-day slip would forgo CO₂e equal to 15 times the saving (Appendix B7.5), so schedule neutrality decides whether C1 helps.

**The status quo's second place over the SMR is a scaling artefact.** It scores full marks on cost, supply and legal feasibility because it changes nothing; on fixed global scales the SMR moves above it. Renewables stay first on both.

### 9.3 Verdict and limits

**Darlington.** Pilot LC³ in eligible non-safety works first; use steel-composite infill only if qualified on Unit 1 mock-ups, otherwise specify the slag blend. Qualification must start in 2027 for the 2028 Units 2–4 decision (§8.6).

**Australia.** An SMR at Liddell would need its cost gap closed, first power well before 2040, and the legal and consent barriers removed first (Appendix B3, route C). We would keep SMRs under review against Darlington's outturn cost.

**Limits.** The social, legal and renewables-supply scores and all four weight sets are our judgement. The status quo's lead over the SMR depends on the scaling; only "renewables first" is robust to it. Schedule risk enters through first power (2040 at the earliest; the Coalition's 2035 and a 2045 case change nothing). Costs are GenCost's (Graham, Hayward and Foster, 2024); the renewables supply score uses solar PV alone (International Energy Agency, 2022).

---


## 10 Future material properties and processes

**C1 and the levers beyond it each depend on a property or process still to be proven (Table T15).**

*Table T15. What must be proven.*
*Source: as cited in the cells.*

| Need | Evidence now | To prove |
|---|---|---|
| SCC LC³ for DP-SC infill | Calcined clay raises superplasticiser demand (Universität der Bundeswehr München, n.d.); no LC³ heat-of-hydration data found; M50 strength 56.7 against 60.0 MPa (Pillai et al., 2019) | Mock-up panels testing flow through diaphragm holes, temperature rise and shrinkage; qualification under NEDO-33926, which reportedly rests on a modified AISC N690 (GE-Hitachi Nuclear Energy, 2024), before the approval expected in 2028 (American Nuclear Society, 2026) |
| Low-residual EAF nuclear plate | Scrap-EAF steel emits 0.68 against 2.33 t CO₂/t (World Steel Association, 2026), but copper limits scrap use in vessel steel (Canadian Nuclear Safety Commission, 2023b) | Qualify diluted-scrap or direct-reduced-iron plate, first outside the pressure boundary (our inference) |
| Laser enrichment | Enrichment is the most concentrated fuel-cycle step (§8.3); a US laser plant's licence application was accepted in August 2025 (Silex Systems Limited, 2025) and Cameco takes its output (Silex Systems Limited, 2026) | NRC licence decision; Australian law (EPBC s140A, ARPANS s10) bars it |
| Waste forms | Three non-BWRX SMR designs may produce 2–30 times more waste by volume per unit of energy (Krall, Macfarlane and Ewing, 2022; contested); ANSTO's Synroc ceramic, hot-pressed at 1,000 °C and 30 MPa, cuts volume against cement but is pre-commissioning (ANSTO, n.d.) | Synroc commissioning; for Australia, an export of know-how rather than a reason to build |


## 11 Conclusions and recommendations

**Pilot LC³ in eligible non-safety works first; use it in the steel-composite infill only if qualified on Unit 1 mock-ups (slag blend as fallback); and adopt it only if it adds no delay to Darlington Units 2–4. For Australia, law, cost and timing bar an SMR at Liddell before about 2040, and the same money on firmed renewables ranks first.**

**Research questions.**
1. *Life cycle (§6).* One BWRX-300 emits about 4 g CO₂e/kWh, mostly from the fuel front end; conversion heat is the largest uncertainty.
2. *C1 (§6–7).* It saves 2,200 t per unit (1,100–3,300; §4.3), about 0.36% of the life cycle; a delay of 11.6–18.5 days cancels it (1.7–1.8 days on the marginal grid factor).
3. *Displacement (§7).* Darlington Unit 1 avoids 1.0–6.8 Mt CO₂e to 2050 and a Liddell unit 0.67–3.9 Mt; firmed renewables avoid 10.9 times more per dollar.
4. *Barriers and options (§3, §8–9).* Law (three bans), cost (C$149–198/MWh) and time (2040 at the earliest) decide; firmed renewables rank first under all four weight sets (80 against 30 with equal weights).

**Ranked materials levers.**
1. **Schedule:** a month's slip to Units 2–4 costs 29–175 times C1's carbon value (§7).
2. **Fuel front end:** a measured conversion-heat value would narrow the headline most (§6).
3. **Whole-plant steel:** up to 3,714 t per unit, if feasible for nuclear-grade plate (§10).
4. **Concrete (C1):** real and low-risk if schedule-neutral, but it moves the life cycle by about 0.36%.

**Limitations.** A screening LCA, not critically reviewed; MCDA scores and weights are our judgement; inputs are as described in §2; legislation is as compiled, without the 2025 EPBC reforms.

---


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```


## References

ABC News, 2024. Peter Dutton reveals seven sites for proposed nuclear power plants. *ABC News*, 19 June. [online] Available at: https://www.abc.net.au/news/2024-06-19/dutton-reveals-seven-sites-for-proposed-nuclear-power-plants/103995310 [Accessed 20 October 2026].

ABC News, 2026. Coalition vows to "take a chainsaw" to climate laws and offshore wind. *ABC News*, 23 September. [online] Available at: https://www.abc.net.au/news/2026-09-23/coalition-energy-plan-scrap-renewables-climate-laws/107184376 [Accessed 20 October 2026].

American Institute of Steel Construction, 2022. *Buy Clean California quick guide*. [pdf] Available at: https://www.aisc.org/contentassets/937a380ddd404a2da0c48669d438bf3b/quickguide_buycleancali2022.pdf.

American Nuclear Society, 2026. North American construction is back—smaller and faster—at OPG's Darlington. *Nuclear Newswire*, 5 June. [online] Available at: https://www.ans.org/news/2026-06-05/article-8047/north-american-construction-is-back-smaller-and-faster-at-opgs-darlington/ [Accessed 20 October 2026].

ANSTO, n.d. *ANSTO Synroc*. [online] Lucas Heights: Australian Nuclear Science and Technology Organisation. Available at: https://ansto.gov.au/products-services/ansto-synroc [Accessed 25 October 2026].

ARPANSA, n.d. *Who we regulate*. [online] Australian Radiation Protection and Nuclear Safety Agency. Available at: https://www.arpansa.gov.au/regulation-and-licensing/regulation/about-regulatory-services/who-we-regulate [Accessed 20 October 2026].

The Atmospheric Fund, 2021. *A Clearer View of Ontario's Emissions: Electricity Emissions Factors and Guidelines, 2021 Edition*. [pdf] Toronto: The Atmospheric Fund. Available at: https://taf.ca/custom/uploads/2021/11/20211116_TAF_Emissions-Factors-Guidelines.pdf.

The Atmospheric Fund, 2025. *Ontario Electricity Emissions Factors and Guidelines: 2025 Edition*. [pdf] Toronto: The Atmospheric Fund. Available at: https://taf.ca/custom/uploads/2025/10/2025TAF-EmissionsFactors.pdf.

Australian Electoral Commission, 2019. *District Council of Kimba community ballot on the National Radioactive Waste Management Facility: results*. Canberra: Australian Electoral Commission.

Australian Electoral Commission, 2025. *2025 federal election report*. [pdf] Canberra: Australian Electoral Commission. Available at: https://www.aec.gov.au/Elections/federal_elections/2025/2025-Federal-Election-Report.pdf [Accessed 20 October 2026].

Australian Energy Market Operator, 2024. *2024 Integrated System Plan for the National Electricity Market*. Melbourne: AEMO.

Australian Energy Market Operator, 2025. *Carbon Dioxide Equivalent Intensity Index Procedures*. [pdf] Melbourne: AEMO. Available at: https://aemo.com.au/-/media/files/electricity/nem/settlements_and_payments/settlements/2025/carbon-dioxide-equivalent-intensity-index-procedures.pdf.

Australian Energy Regulator, 2021. *Decision notice: AGL application, 30 April 2021*. [pdf] Available at: https://www.aer.gov.au/system/files/Decision%20notice%20-%20AGL%20application%2030%20April%202021.pdf.

Australian Greens, 2025. *2035: Powering Past Coal & Gas*. [pdf] Available at: https://cdn.greens.org.au/cdn/ff/fk0q_VgBQA5t00ZlhkPcF6i2IEZByQHBjpMq1g6YdVQ/1744244709/public/2025-04/2035%20Powering%20Past%20Coal%20&%20Gas.pdf [Accessed 20 October 2026].

Bowen, C., 2025. *Joint media release: Experts agree: nuclear only getting more expensive, slower for Australia's energy needs*. [online] Canberra: Minister for Climate Change and Energy. Available at: https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-experts-agree-nuclear-only-getting-more-expensive-slower-australias-energy-needs [Accessed 20 October 2026].

BWRX-300 Ostrołęka sp. z o.o., 2023. *Small Modular Nuclear Power Plant: Project Information Sheet*. [pdf] Table 14, p. 83. Available at: https://am.lrv.lt/media/viesa/saugykla/2024/2/oHCKCUp7Lrs.pdf

Caixin Global, 2026. Beijing clears eight new reactors as China accelerates nuclear buildout. *Caixin Global*, 1 August.

Canada Energy Regulator, n.d. *Provincial and Territorial Energy Profiles – Ontario*. [online] Available at: https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/provincial-territorial-energy-profiles/provincial-territorial-energy-profiles-ontario.html.

Canada Growth Fund and Building Ontario Fund, 2025. *Canada Growth Fund and Building Ontario Fund announce innovative equity investment in world-leading Ontario Power Generation SMR project*. [online] Newswire.ca, 23 October. Available at: https://www.newswire.ca/news-releases/canada-growth-fund-and-building-ontario-fund-announce-innovative-equity-investment-in-world-leading-ontario-power-generation-smr-project-862778443.html [Accessed 20 October 2026].

Canada Infrastructure Bank, 2022. *CIB commits $970 million towards Canada's first Small Modular Reactor (SMR)*. [online] Toronto: Canada Infrastructure Bank. Available at: https://cib-bic.ca/en/medias/articles/cib-commits-970-million-towards-canadas-first-small-modular-reactor/ [Accessed 20 October 2026].

Canadian Nuclear Safety Commission, 2021. *CNSC renews Ontario Power Generation's site preparation licence for its Darlington New Nuclear Project*. [online] News release, 12 October. Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2021/10/cnsc-renews-ontario-power-generations-site-preparation-licence-for-its-darlington-new-nuclear-project.html [Accessed 20 October 2026].

Canadian Nuclear Safety Commission, 2022. *REGDOC-3.5.1, Licensing Process for Class I Nuclear Facilities and Uranium Mines and Mills*, Version 2.1. [online] Available at: https://www.cnsc-ccsn.gc.ca/eng/acts-and-regulations/regulatory-documents/published/html/regdoc3-5-1-v2-1/ [Accessed 20 October 2026].

Canadian Nuclear Safety Commission, 2023a. *REGDOC-2.5.2, Design of Reactor Facilities: Nuclear Power Plants*, Version 2.1. [online] Ottawa: Canadian Nuclear Safety Commission. Available at: https://www.cnsc-ccsn.gc.ca/eng/acts-and-regulations/regulatory-documents/published/html/regdoc2-5-2-v2-1/ [Accessed 25 October 2026].

Canadian Nuclear Safety Commission, 2023b. *Regulatory consideration of environmental degradation in licensing light water small reactors in Canada*. [online] Technical paper. Ottawa: Canadian Nuclear Safety Commission. Available at: https://cnsc-ccsn.gc.ca/eng/resources/research/technical-papers-and-articles/2023/regulatory-consideration-of-environmental-degradation-in-licensing-light-water-small-reactor-in-canada [Accessed 25 October 2026].

Canadian Nuclear Safety Commission, 2024. *CMD 24-H3-1B* (staff presentation, Darlington New Nuclear Project). [pdf] Ottawa: Canadian Nuclear Safety Commission. Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD-24-H3-1B.pdf/object.

Canadian Nuclear Safety Commission, 2025. *Commission authorizes Ontario Power Generation Inc. to construct 1 BWRX-300 reactor at the Darlington New Nuclear Project site*. [online] News release, 4 April. Ottawa: Canadian Nuclear Safety Commission. Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html [Accessed 20 October 2026].

Canadian Nuclear Safety Commission, 2026a. *Darlington New Nuclear Project*. [online] Ottawa: Canadian Nuclear Safety Commission. Available at: https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/ [Accessed 20 October 2026].

Canadian Nuclear Safety Commission, 2026b. *Regulatory hold points for new reactor facilities*. [online] Available at: https://www.cnsc-ccsn.gc.ca/eng/reactors/regulatory-hold-points/new-reactors/ [Accessed 20 October 2026].

Canadian Ready-Mixed Concrete Association, 2022. *Industry-wide EPD for ready-mixed concrete, Ontario* (EPD 351, valid to 27 July 2027). [pdf] Available at: https://www.rmcao.org/wp-content/uploads/2023/04/CRMCA-EPD-Ontario-20220803.pdf.

Canberra Times, 2025. Dutton's nuclear power plan faces legal hurdles. *Canberra Times*. [online] Available at: https://www.canberratimes.com.au/story/8851241/duttons-nuclear-power-plan-faces-legal-hurdles/ [Accessed 20 October 2026].

Canberra Times, n.d. 'Nightmare scenario': states slam Dutton's nuclear plan. *Canberra Times*. [online] Available at: https://www.canberratimes.com.au/story/8668232/nightmare-scenario-states-slam-duttons-nuclear-plan/ [Accessed 20 October 2026].

Carless, T.S., Griffin, W.M. and Fischbeck, P.S., 2016. The environmental competitiveness of small modular reactors: a life cycle study. *Energy*, 114, pp.84–99. Available at: https://ideas.repec.org/a/eee/energy/v114y2016icp84-99.html.

Cement Association of Canada, 2022. *Environmental Product Declaration: General Use (GU) and Portland-Limestone (GUL) Cements*. [pdf] Available at: https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blt9992df315e96e31c/697b1f51f6a61062618f5048/919.CAC_General_Use_(GU)_and_Portland-Limestone_(GUL)_Cements.pdf.

Circular Ecology, 2019. *Inventory of Carbon and Energy (ICE) database v3.0*. Bath: Circular Ecology.

Concrete Reinforcing Steel Institute, 2017. *Industry-wide EPD for fabricated steel reinforcing bar*. [pdf] Available at: https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blt4900ac0ff22764a2/697b1fc25e3544dd57d83a3d/362.EPD_for_CRSI_EPD_FINAL_2017-08-28.pdf.

Concrete Reinforcing Steel Institute, 2022. *Environmental Product Declaration: Fabricated Steel Reinforcement*. Schaumburg, IL: Concrete Reinforcing Steel Institute. Available at: https://www.crsi.org/sustainability/environmental-product-declaration/.

Conference Board of Canada, 2021. *A New Power: The Economic Impacts of Small Modular Reactors*. Ottawa: Conference Board of Canada.

CSA Group, 2023. *CSA A3000:23, Cementitious materials compendium* (includes CSA A3001:23, *Cementitious materials for use in concrete*). [online] Toronto: CSA Group. Available at: https://www.csagroup.org/store/product/2430659/ [Accessed 20 October 2026].

CSA Group, 2026. *CSA N287.2, Material requirements for concrete containment structures for nuclear power plants*. [online] Standard catalogue information. Toronto: CSA Group. Available at: https://webstore.ansi.org/standards/csa/csan2872026 [Accessed 25 October 2026].

Curve Lake First Nation, 2024. *Written submission, CMD 24-H3.83, DNNP licence to construct*, 11 November. Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD24-H3-83.pdf/object [Accessed 21 October 2026].

Department of Climate Change, Energy, the Environment and Water, 2025. *Australian National Greenhouse Accounts Factors: 2025*. [pdf/xlsx] Canberra: Department of Climate Change, Energy, the Environment and Water.

Department of Industry, Science, Energy and Resources, 2020. *A new agency to manage radioactive waste*. [online] Available at: https://industry.gov.au/news-media/australian-radioactive-waste-agency-news/a-new-agency-to-manage-radioactive-waste [Accessed 21 October 2026].

Development Alternatives, n.d. *LC3 Sustainability Assessment* (ver 1.14). Available at: https://devalt.org/images/L2_ProjectPdfs/Report%20-%20LC3%20Sustainability%20Assessment_ver1.14.pdf.

Dodgson, J.S., Spackman, M., Pearman, A. and Phillips, L.D., 2009. *Multi-criteria analysis: a manual*. London: Department for Communities and Local Government. Available at: https://www.gov.uk/government/publications/multi-criteria-analysis-manual-for-making-government-policy [Accessed 21 October 2026].

EDF R&D, 2024. Life cycle assessment of nuclear power in France: EDF case study. *EPJ Nuclear Sciences & Technologies*, 10, art. 5. Available at: https://www.epj-n.org/10.1051/epjn/2024005.

EFNARC, 2005. *The European Guidelines for Self-Compacting Concrete: Specification, Production and Use*. Farnham: EFNARC.

ENR, 2018. Clay and limestone cement could cut carbon emissions. *Engineering News-Record*, 7 May. Available at: https://digital.bnpmedia.com/article/Construction+Materials/3078554/494167/article.html.

Environment and Climate Change Canada, 2026. *Industrial carbon pricing in Canada*. Ottawa: Government of Canada. Available at: https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/putting-price-on-carbon-pollution/industry.html [Accessed 21 October 2026].

Fermi Energia, n.d. *New SMR project*. [online] Tallinn: Fermi Energia. Available at: https://fermi.ee/new-smr-project/ [Accessed 25 October 2026].

Field, K.G., Remec, I. and Le Pape, Y., 2015. Radiation effects in concrete for nuclear power plants – Part I: Quantification of radiation exposure and radiation effects. *Nuclear Engineering and Design*, 282, pp.126–143. Available at: https://www.ornl.gov/publication/radiation-effects-concrete-nuclear-power-plants-part-i-quantification-radiation [Accessed 25 October 2026].

GE Hitachi Nuclear Energy, n.d. *GE Hitachi BWRX-300 fact sheet*. [pdf] Wilmington, NC: GE Hitachi Nuclear Energy. Available at: https://gevernova.com/content/dam/gepower-nuclear/global/en_US/documents/product-fact-sheets/BWRX-300_Fact_Sheet-2020.pdf [Accessed 25 October 2026].

GE-Hitachi Nuclear Energy, 2024. *BWRX-300 Steel-Plate Composite Containment Vessel (SCCV) and Reactor Building Structural Design*, NEDO-33926, Revision 2 (non-proprietary), 16 August. [pdf] US NRC ADAMS ML24110A134. Available at: https://www.nrc.gov/docs/ML2411/ML24110A134.pdf [Accessed 20 October 2026].

GE Vernova, n.d. *BWRX-300 Small Modular Reactor*. [online] Available at: https://www.gevernova.com/nuclear/carbon-free-power/bwrx-300-small-modular-reactor.

GE Vernova, 2026. *NRC issues first U.S. construction permit for BWRX-300 small modular reactor at TVA Clinch River*. [online] Press release. Available at: https://www.gevernova.com/news/press-releases/nrc-issues-first-us-construction-permit-bwrx-300-small-modular-reactor-tva-clinch-river [Accessed 25 October 2026].

GE Vernova Hitachi Nuclear Energy, n.d. *BWRX-300 General Description* (005N9751). [pdf] Wilmington, NC: GE Vernova. Available at: https://www.gevernova.com/content/dam/gevernova-nuclear/global/en_us/documents/carbon-free-power/005N9751-BWRX-300-General-Description.pdf.

Geneski, N., McKellar, J.M. and Atkinson, K.D., n.d. Life cycle environmental impacts of small modular reactors: BWRX-300 Darlington project. *Proceedings of the Canadian Nuclear Society*. Available at: https://proceedings.cns-snc.ca/index.php/pcns/article/view/7692.

Gibon, T. and Hahn Menacho, Á., 2023. Parametric life cycle assessment of nuclear power for simplified models. *Environmental Science & Technology*, 57(38), pp.14194–14205. Available at: https://doi.org/10.1021/acs.est.3c03190.

Government of Canada, 2026. *Darlington New Nuclear Project*. [online] Ottawa: Major Projects Office, updated 8 July 2026. Available at: https://www.canada.ca/en/privy-council/major-projects-office/projects/national/darlington.html [Accessed 25 October 2026].

Government of Ontario, 2025. *Ontario Leads the G7 by Building First Small Modular Reactor*. [news release] 8 May. Toronto: Government of Ontario.

Government of Ontario, n.d. *Ontario energy snapshot*. [online] Available at: https://www.ontario.ca/page/ontario-energy-snapshot.

Graham, P. and Hayward, J., 2026. *GenCost 2025-26: Final report*. [pdf] Australia: CSIRO. Available at: https://www.csiro.au/-/media/Energy/GenCost-2025-26-Final/GenCost_2025-26_Final_Report_20260715.pdf.

Graham, P., Hayward, J. and Foster, J., 2024. *GenCost 2023-24: Final report*. [pdf] Australia: CSIRO. Available at: https://www.csiro.au/-/media/Energy/GenCost/GenCost2023-24Final_20240522.pdf.

Graham, P., Hayward, J. and Foster, J., 2025. *GenCost 2024-25: Final report*. [pdf] Australia: CSIRO. Executive summary available at: https://www.csiro.au/-/media/Energy/GenCost/GenCost2024-25Final_ES.pdf.

Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub, 2025. *What Australians really think of nuclear power*. [news release] 2 May. Available at: https://news.griffith.edu.au/2025/05/02/what-australians-really-think-of-nuclear-power/ [Accessed 21 October 2026].

Helmholtz-Zentrum Dresden-Rossendorf, n.d. [Activation of the biological shield of Greifswald NPP Unit 2]. Publication Publ-39008. Dresden: Helmholtz-Zentrum Dresden-Rossendorf. Available at: https://hzdr.de/publications/Publ-39008 [Accessed 25 October 2026].

Hooton, R.D., 2023. [Webinar slides on changes to ASTM cement and concrete standards]. ACI Fall 2023 webinar slides. [pdf] Farmington Hills: American Concrete Institute. Available at: https://www.concrete.org/portals/0/files/pdf/webinars/ws_F23_NEU_DouglasHooton.pdf [Accessed 20 October 2026].

Independent Electricity System Operator, 2024. *Ontario's Energy Future: Spring 2024 Update*. [pdf] Toronto: Independent Electricity System Operator. Available at: https://www.ieso.ca/-/media/Files/IESO/Document-Library/Decarbonization-Hub/IESO-Ontarios-Energy-Future-Spring-2024.pdf.

International Atomic Energy Agency, 2023. *What are small modular reactors (SMRs)?* [online] Vienna: International Atomic Energy Agency. Available at: https://www.iaea.org/newscenter/news/what-are-small-modular-reactors-smrs [Accessed 25 October 2026].

International Atomic Energy Agency, 2024. *Small Modular Reactors: Advances in SMR Developments 2024*. Vienna: International Atomic Energy Agency.

International Energy Agency, 2022. *Solar PV Global Supply Chains*. Paris: International Energy Agency. Available at: https://www.iea.org/reports/solar-pv-global-supply-chains [Accessed 21 October 2026].

International Organization for Standardization, 2006a. *ISO 14040:2006 Environmental management — Life cycle assessment — Principles and framework*. Geneva: International Organization for Standardization.

International Organization for Standardization, 2006b. *ISO 14044:2006 Environmental management — Life cycle assessment — Requirements and guidelines*. Geneva: International Organization for Standardization. Available at: https://www.iso.org/standard/38498.html.

IPCC, 2006. *2006 IPCC Guidelines for National Greenhouse Gas Inventories*, Vol. 2 Energy, Ch. 2, Table 2.2. Hayama: Institute for Global Environmental Strategies.

Joint Standing Committee on Treaties, 2024. *Report 224: Agreement among Australia, the UK and the US for cooperation related to naval nuclear propulsion*, Chapter 6, 'Employment and education impacts'. Canberra: Parliament of Australia. Available at: https://www.aph.gov.au/Parliamentary_Business/Committees/Joint/Treaties/NuclearPropulsion/Report/Chapter_6_-_Employment_and_education_impacts [Accessed 21 October 2026].

Kazatomprom, 2025. *Integrated Annual Report 2024*. [pdf] Astana: NAC Kazatomprom JSC. Available at: https://www.kazatomprom.kz/storage/59/kap_iar_2024_eng_0205__clean.pdf [Accessed 20 October 2026].

Kim and Macfarlane, 2026. *Challenges of small modular reactors: a comprehensive exploration*. [pdf] Available at: https://www.nirs.org/wp-content/uploads/2025/09/SMR-Costs_Challenges-of-SMRs-cost-waste_Kim-Macfarlane_2026.pdf.

Krall, L.M., Macfarlane, A.M. and Ewing, R.C., 2022. Nuclear waste from small modular reactors. *Proceedings of the National Academy of Sciences of the United States of America*, 119(23), e2111833119. Available at: https://doi.org/10.1073/pnas.2111833119 [Accessed 25 October 2026].

LACCEI, 2026. Comparative life cycle assessment and structural performance analysis of eco-friendly LC3 cement for CO₂ reduction compared to Portland cement. In: *Proceedings of the 24th LACCEI International Multi-Conference for Engineering, Education and Technology*, Santiago, Chile, 15–17 July 2026. Contribution 2661. Available at: https://laccei.org/LACCEI2026-Chile/full-papers/Contribution_2661_final_a.pdf.

LC3 Project, 2015. *LCA of LC3: India team progress* (industry meeting, September 2015). Available at: https://lc3.ch/wp-content/uploads/2023/03/LCA-of-LC3-India-team-progress-Industry-meeting-Sep-2015.pdf.

Liberal Party of Australia, 2026. *Our Plan for Cheaper Power*. [online] Available at: https://www.liberal.org.au/our-plan/energy [Accessed 20 October 2026].

Markandya, A. and Wilkinson, P., 2007. Electricity generation and health. *The Lancet*, 370(9591), pp.979–990. Available at: https://doi.org/10.1016/S0140-6736(07)61253-7 [Accessed 20 October 2026].

Minister for Defence, 2025. *An AUKUS milestone – launch of the Australian Naval Nuclear Power Safety Regulator*. [media release] 1 November. Available at: https://www.minister.defence.gov.au/media-releases/2025-11-01/aukus-milestone-launch-australian-naval-nuclear-power-safety-regulator [Accessed 20 October 2026].

Mississaugas of Scugog Island First Nation, 2023. Written submissions to the CNSC: CMD 23-H9.18A (Darlington Waste Management Facility, January 2023); CMD 24-H2.26 (November 2023); CMD 24-H3.81 (November 2024). Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD23-H9-18A.pdf/object [Accessed 21 October 2026].

Municipality of Clarington, 2024. Letter / written submission to the CNSC on the DNNP licence to construct. Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD24-H2-12.pdf/object [Accessed 21 October 2026].

Neelam, R., 2024. *Lowy Institute Poll 2024*. Sydney: Lowy Institute. Available at: https://poll.lowyinstitute.org/report/2024/ [Accessed 20 October 2026].

Newcastle Herald, 2024a. AGL says Liddell site will not be used for nuclear power. *Newcastle Herald*. [online] Available at: https://www.newcastleherald.com.au/story/8557276/agl-says-liddell-site-will-not-be-used-for-nuclear-power [Accessed 20 October 2026].

Newcastle Herald, 2024b. Coalition government could seize Liddell for nuclear power plant; Dutton's nuclear energy plan divides opinion in the Hunter. *Newcastle Herald*. [online] Available at: https://newcastleherald.com.au/story/8670020/ and https://newcastleherald.com.au/story/8668177/ [Accessed 21 October 2026].

Newspoll, 2007. National survey on nuclear power, 2–4 March 2007 (n ≈ 1,200). Published in *The Australian*.

Ng, J.H.C., Vyawahare, P., Benavides, P.T., Gan, Y., Sun, P., Boardman, R., Marcinkoski, J. and Elgowainy, A., 2025. Life-cycle greenhouse gas emissions associated with nuclear power generation in the United States. *Journal of Industrial Ecology*, 29(3), pp.719–732. Available at: https://doi.org/10.1111/jiec.70008.

Norton Rose Fulbright, 2025. *Key amendments to the Environment Protection Reform Act 2025 and their implications for the EPBC Act*. [online] Available at: https://www.nortonrosefulbright.com/en-au/knowledge/publications/df336551/key-amendments-to-the-environment-protection-reform-act-2025-and-their-implications-for-the-epbc-act [Accessed 20 October 2026].

NRMCA, 2021. *Environmental Product Declaration EPD 20046: St Marys Cement, Bowmanville plant*. [pdf] Available at: https://www.nrmca.org/wp-content/uploads/2021/09/NRMCA_EPD20046StMarys_EPD_BOW_Sep2021.pdf.

Nuclear Waste Management Organization, 2024a. *The Nuclear Waste Management Organization selects site for Canada's deep geological repository for used nuclear fuel*. [news release] 28 November. Toronto: Nuclear Waste Management Organization. Available at: https://www.nwmo.ca/News/The-Nuclear-Waste-Management-Organization-selects-site-for-Canadas-deep-geological-repository [Accessed 21 October 2026].

Nuclear Waste Management Organization, 2024b. *Implementing Adaptive Phased Management 2024–28: Selecting a site*. Available at: https://implementationplan.nwmo.ca/2024_28/selecting-a-site/ [Accessed 21 October 2026].

Nuclear Waste Management Organization, 2024c. *Mayor and Council of the Township of Ignace sign historic potential hosting agreement with the NWMO*. [news release] March. Available at: https://www.nwmo.ca/news/mayor-and-council-of-the-township-of-ignace-sign-historic--potential-hosting-agreement-with-the-nwmo [Accessed 21 October 2026].

Nuclear Waste Management Organization, 2026. *Regulatory process: deep geological repository for Canada's used nuclear fuel project*. [online] Toronto: Nuclear Waste Management Organization. Available at: https://www.nwmo.ca/en/Regulatory-process [Accessed 25 October 2026].

Nuclear Waste Management Organization, n.d. *Project costs*. [online] Available at: https://www.nwmo.ca/Who-we-are/Funding/Project-Costs [Accessed 21 October 2026].

NuScale Power Corporation, 2023. *Amendment No. 3 to Development Cost Reimbursement Agreement* [exhibit to Form 10-Q / 424B3]. Washington, DC: US Securities and Exchange Commission. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296623000092/a101dcraamendment3execut.htm [Accessed 20 October 2026].

NuScale Power Corporation, 2026. *Form 10-K for the fiscal year ended 31 December 2025*. Washington, DC: US Securities and Exchange Commission. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm.

NuScale Power Corporation and Utah Associated Municipal Power Systems, 2023. *UAMPS and NuScale Power agree to terminate the Carbon Free Power Project* [joint press release, 8 November 2023]. Exhibit to NuScale Power Corporation Form 8-K. Washington, DC: US Securities and Exchange Commission. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296623000256/uampsnuscalejointpressre.htm [Accessed 20 October 2026].

OECD Nuclear Energy Agency and International Atomic Energy Agency, 2025. *Uranium 2024: Resources, Production and Demand*. [pdf] Paris: OECD Publishing. Available at: https://www.oecd-nea.org/jcms/pl_103179/uranium-2024-resources-production-and-demand [Accessed 20 October 2026].

OECD Nuclear Energy Agency and International Atomic Energy Agency, 2026. *Uranium 2026: Resources, Production and Demand*. [pdf] Paris: OECD Publishing. Available at: https://www.oecd-nea.org/jcms/pl_121658/uranium-2026-resources-production-and-demand [Accessed 20 October 2026].

Ontario Power Generation, 2023. OPG selects first fuel suppliers for its small modular reactor. [press release] Toronto: Ontario Power Generation.

Ontario Power Generation, 2025a. *OPG reports 2025 first quarter financial results*. [online] News release, 13 May. Toronto: Ontario Power Generation. Available at: https://www.opg.com/news-resources/newsroom/release/opg-reports-2025-first-quarter-financial-results/ [Accessed 20 October 2026].

Ontario Power Generation, 2025b. *EB-2025-0297, Exhibit D2, Tab 4, Schedule 1: Darlington New Nuclear Project overview* (updated 21 May 2026). [pdf] Filed with the Ontario Energy Board. Available at: https://files.opg.com/wp-content/uploads/2026/05/D2-04-01-Darlington-New-Nuclear-Project-Overview_Updated_20260521_260522_191835.pdf [Accessed 20 October 2026].

Ontario Power Generation, 2025c. *Darlington New Nuclear Project construction update*. [online] Available at: https://www.opg.com/projects-services/projects/nuclear/smr/darlington-smr/.

Ontario Power Generation, 2026a. *OPG reports 2026 first quarter financial results*. [online] Available at: https://www.opg.com/news-resources/newsroom/release/opg-reports-2026-first-quarter-financial-results/ [Accessed 20 October 2026].

Ontario Power Generation, 2026b. Interrogatory response giving the Darlington New Nuclear Project levelised cost, EB-2025-0297. Filed with the Ontario Energy Board.

Ontario Power Generation, 2026c. *Laying the foundation for the G7's first small modular reactor*. [online] 30 April. Available at: https://www.opg.com/news-and-media/story/laying-the-foundation-for-the-g7s-first-small-modular-reactor [Accessed 25 October 2026].

Parker, D.J., McNaughton, C.S. and Sparrow, G.A., 2016. Life cycle greenhouse gas emissions from uranium mining and milling in Canada. *Environmental Science & Technology*, 50(17), pp.9746–9753. Available at: https://pubs.acs.org/doi/10.1021/acs.est.5b06072.

Parliament of Australia, 2026. *Senate composition*. [online] Available at: https://www.aph.gov.au/Senators_and_Members/Senators/Senate_composition [Accessed 20 October 2026].

Parliament of New South Wales, 2025. *Uranium Mining and Nuclear Facilities (Prohibitions) Repeal Bill 2025*: bill details. [online] Available at: https://www.parliament.nsw.gov.au/bills/Pages/bill-details.aspx?pk=18833 [Accessed 20 October 2026].

Parliament of New South Wales, 2026. *Legislative Assembly Notice Paper*. [pdf] Available at: https://files.parliament.nsw.gov.au/fileapi/ParlFiles/GetArtifact/170%20NOM%20(combined).pdf?serverRelativeUrl=%2Fhp%2Fhousepaper%2F31312%2F170+NOM+%28combined%29.pdf [Accessed 20 October 2026].

Parliamentary Library, 2024. *Current prohibitions on nuclear activities in Australia: a quick guide*. Research Paper Series 2023–24, Quick Guide. [online] Canberra: Parliamentary Library, Parliament of Australia, 30 May. Available at: https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Quick_Guides/2023-24/NuclearActivitiesProhibitions [Accessed 21 October 2026].

Peterson, P.F., Zhao, H. and Petroski, R., 2005. *Metal and concrete inputs for several nuclear power plants* (UCBTH-05-001). [pdf] Berkeley: University of California, Berkeley. Available at: https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf.

Pillai, R.G. et al., 2019. Service life and life cycle assessment of reinforced concrete systems with limestone calcined clay cement (LC³). *Cement and Concrete Research*, 118, pp.111–119. Available at: https://doi.org/10.1016/j.cemconres.2018.11.019.

Power Engineering, 2023. OPG selects first fuel suppliers for its small modular reactors. *Power Engineering*. [online] Available at: https://www.power-eng.com/nuclear/smrs/opg-selects-first-fuel-suppliers-for-its-small-modular-reactors/.

Power Workers' Union, 2021. *Written submission in support of OPG's application to renew the Darlington power reactor operating licence*, CMD 21-H4.38. Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD21-H4-38.pdf/object [Accessed 21 October 2026].

Rao, P., Kaffine, D.T. and Hodge, B.-M., 2026. *The consequences of high SMR operating costs in electricity markets*. arXiv preprint 2609.08929. Available at: https://arxiv.org/pdf/2609.08929.

Reserve Bank of Australia, 2025. *Historical Data: Exchange Rates (F11)*. [online] Sydney: Reserve Bank of Australia.

Ritchie, H., 2020. *What are the safest and cleanest sources of energy?* [online] Our World in Data. Available at: https://ourworldindata.org/safest-sources-of-energy [Accessed 20 October 2026].

Schlissel, D., 2023. *Eye-popping new cost estimates released for NuScale small modular reactor*. Institute for Energy Economics and Financial Analysis. Available at: https://ieefa.org/resources/eye-popping-new-cost-estimates-released-nuscale-small-modular-reactor.

Schlömer, S. et al., 2014. Annex III: Technology-specific cost and performance parameters. In: *Climate Change 2014: Mitigation of Climate Change. Contribution of Working Group III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge: Cambridge University Press.

Scrivener, K., Martirena, F., Bishnoi, S. and Maity, S., 2018. Calcined clay limestone cements (LC3). *Cement and Concrete Research*, 114, pp.49–56. Available at: https://doi.org/10.1016/j.cemconres.2017.08.017.

Senate Environment and Communications Legislation Committee, 2023. *Environment and Other Legislation Amendment (Removing Nuclear Energy Prohibitions) Bill 2022 [Provisions]*. [online] Canberra: Parliament of Australia. Available at: https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Nuclearprohibitions [Accessed 20 October 2026].

Silex Systems Limited, 2025. [ASX announcement on the NRC's acceptance of GLE's Paducah licence application], 6 August. Sydney: ASX. Available at: https://announcements.asx.com.au/asxpdf/20250806/pdf/06mkwks19y2zck.pdf.

Silex Systems Limited, 2026. [ASX announcement on Cameco's offtake agreement for the Paducah Laser Enrichment Facility], 16 September. Sydney: ASX.

Slag Cement Association, n.d. *Industry-average EPD for slag cement* (USA and Canada). [pdf] Available at: https://www.lafarge.ca/sites/canada/files/images/sca_epd_for_slag_cement.pdf.

Slovic, P., 1987. Perception of risk. *Science*, 236(4799), pp.280–285.

Steigerwald, B., Weibezahn, J., Slowik, M. and von Hirschhausen, C., 2023. Uncertainties in estimating production costs of future nuclear technologies: a model-based analysis of small modular reactors. *Energy*, 281, 128204.

Sun, Y. and Kurosaki, K., 2025. *Technical overview of recent developments in small modular reactors in the United States*. arXiv:2504.02599 [physics.soc-ph]. Available at: https://arxiv.org/abs/2504.02599.

Systematic evaluation of concrete placement reliability in heavily reinforced nuclear structures, 2026. *International Journal of Concrete Structures and Materials*. Available at: https://link.springer.com/article/10.1186/s40069-026-00964-8 [Accessed 25 October 2026].

Thierfeldt, S., 2019. [Clearance and recycling of materials from decommissioning]. Presentation slides, SOGIN workshop, Rome. [pdf] Available at: https://www.sogin.it/SiteAssets/uploads/2019/media/09_THIERFELDT_Clearance_Recycling_Materials_Decommissioning.pdf [Accessed 25 October 2026].

Treasury Board of Canada Secretariat, 2022. *Standard on Embodied Carbon in Construction* (amended 20 March 2025). [online] Ottawa: Treasury Board of Canada Secretariat. Available at: https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32814 [Accessed 20 October 2026].

United Nations Economic Commission for Europe, 2021. *Carbon Neutrality in the UNECE Region: Integrated Life-cycle Assessment of Electricity Sources*. ECE/ENERGY/141. Geneva: United Nations. Available at: https://unece.org/sites/default/files/2021-10/LCA-2.pdf [Accessed 20 October 2026].

United States Congress, 2024. *Prohibiting Russian Uranium Imports Act*, Public Law 118-62, 13 May 2024. [pdf] Washington, DC: US Government Publishing Office. Available at: https://www.govinfo.gov/content/pkg/PLAW-118publ62/pdf/PLAW-118publ62.pdf [Accessed 20 October 2026].

Universität der Bundeswehr München, n.d. [Self-consolidating mortar with calcined clay]. [pdf] Munich: Universität der Bundeswehr München. Available at: https://athene-forschung.rz.unibw-muenchen.de/doc/141635/141635.pdf [Accessed 25 October 2026].

US Department of Energy, 2015. *Technology Readiness Assessment Guide*, DOE G 413.3-4A (Admin. Chg 1). [online] Washington, DC: US Department of Energy. Available at: https://www.directives.doe.gov/directives/0413.3-EGuide-04a [Accessed 25 October 2026].

US Department of Energy, 2025. *Energy Department Selects TVA and Holtec to Advance Deployment of U.S. Small Modular Reactors*. Washington, DC: US Department of Energy. Available at: https://www.energy.gov/articles/energy-department-selects-tva-and-holtec-advance-deployment-us-small-modular-reactors.

US Department of Justice and Federal Trade Commission, 2010. *Horizontal Merger Guidelines*. [online] Washington, DC: US Department of Justice and Federal Trade Commission, 19 August. Available at: https://www.justice.gov/atr/horizontal-merger-guidelines-08192010 [Accessed 20 October 2026].

US Department of Justice and Federal Trade Commission, 2023. *Merger Guidelines*. [pdf] Washington, DC: US Department of Justice and Federal Trade Commission, 18 December. Available at: https://www.justice.gov/d9/2023-12/2023%20Merger%20Guidelines.pdf [Accessed 20 October 2026].

US EPA, 2024. *Power Profiler: terms, calculations and data sources*. [pdf] Available at: https://www.epa.gov/system/files/documents/2024-04/power-profiler-terms-calculations-and-data-sources.pdf.

US Nuclear Regulatory Commission, 1988. *Regulatory Guide 1.99, Revision 2: Radiation embrittlement of reactor vessel materials*. [pdf] Washington, DC: US Nuclear Regulatory Commission. Available at: https://www.nrc.gov/docs/ML1214/ML12145A013.pdf [Accessed 25 October 2026].

US Nuclear Regulatory Commission, 2025. *NuScale US460*. [online] Rockville, MD: US Nuclear Regulatory Commission. Available at: https://www.nrc.gov/reactors/new-reactors/advanced/who-were-working-with/applicant-projects/nuscale-us460.html [Accessed 25 October 2026].

US Nuclear Regulatory Commission and Canadian Nuclear Safety Commission, 2025. *CNSC–NRC Joint Report on GEH BWRX-300 Steel-Plate Composite Containment Vessel and Reactor Building Structural Design Topical Report*. ADAMS ML25325A075. [pdf] Available at: https://www.nrc.gov/docs/ML2532/ML25325A075.pdf [Accessed 20 October 2026].

Warner, E.S. and Heath, G.A., 2012. Life cycle greenhouse gas emissions of nuclear electricity generation: systematic review and harmonization. *Journal of Industrial Ecology*, 16(S1), pp.S73–S92. Available at: https://doi.org/10.1111/j.1530-9290.2012.00472.x.

Williams Treaties First Nations, Ontario Power Generation, Government of Ontario and Government of Canada, 2026. *Williams Treaties First Nations announce historic $700 million investment in Darlington New Nuclear Project*. [press release] 23 June. Available at: https://www.bnnbloomberg.ca/press-releases/2026/06/23/williams-treaties-first-nations-announce-historic-700-million-investment-in-darlington-new-nuclear-project/ [Accessed 21 October 2026].

World Nuclear Association, 2024. *Conversion and Deconversion*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/conversion-and-deconversion [Accessed 20 October 2026].

World Nuclear Association, 2025. *Uranium Enrichment*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment [Accessed 20 October 2026].

World Nuclear Association, 2026. *World Uranium Mining Production*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/mining-of-uranium/world-uranium-mining-production [Accessed 20 October 2026].

World Nuclear News, 2023. China's demonstration HTR-PM enters commercial operation. *World Nuclear News*, 6 December. [online] Available at: https://world-nuclear-news.org/articles/chinese-htr-pm-demo-begins-commercial-operation [Accessed 25 October 2026].

World Nuclear News, 2026. Cameco in offtake agreement for US laser enrichment plant. *World Nuclear News*. [online] Available at: https://www.world-nuclear-news.org/articles/cameco-in-offtake-agreement-for-us-laser-enrichment-plant.

World Nuclear University, 2025. [Enrichment: WNU Summer Institute presentation slides], 17 June. Available at: https://world-nuclear-university.org/SummerInsituteFiles/2025-06-17_WNU_Enrichment_Platov_final_62a48c29.pdf.

World Steel Association, 2026. *CO₂ emissions and energy intensity, 2022–2024* (Sustainability indicators). [online] Brussels: World Steel Association. Available at: https://worldsteel.org/steel-topics/sustainability/sustainability-indicators-2024-report [Accessed 25 October 2026].

Zunino, F., 2021. *Limestone calcined clay cements* [presentation slides]. Lausanne: EPFL / LC3 project. [pdf] Available at: https://lc3.ch/wp-content/uploads/2021/12/6-Franco-LimestoneCalcinedClayCements.pdf [Accessed 25 October 2026].

### Legislation

*Environment Protection and Biodiversity Conservation Act 1999* (Cth), s 140A. [online] Federal Register of Legislation, C2004A00485. Available at: https://www.legislation.gov.au/C2004A00485/latest/text [Accessed 20 October 2026].

*Australian Radiation Protection and Nuclear Safety Act 1998* (Cth), s 10. [online] Federal Register of Legislation, C2004A00383. Available at: https://www.legislation.gov.au/C2004A00383/latest/text [Accessed 20 October 2026].

*Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW), No 194, ss 8–9. [online] NSW Legislation. Available at: https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1986-194 [Accessed 20 October 2026].

### Cases

*Barngarla Determination Aboriginal Corporation RNTBC v Minister for Resources* [2023] FCA 809 (Federal Court of Australia, Charlesworth J, 18 July 2023). Available at: https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2023/2023fca0809 [Accessed 21 October 2026].


## Declaration of generative AI use

[TODO: team to write the AI-use declaration required by the unit (CLAUDE.md: the team decides how AI use is declared).]


```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```
# Appendices


## Appendix A. LCA inventory and calculations

This appendix gives the full working behind §6. The analysis is a screening LCA following ISO 14040/44 principles, not critically reviewed, in which a Python model multiplies quantities by published emission factors. The Ostrołęka and Pillai tables behind the main case could not be opened, so their values are taken as reported; other inputs are labelled as reported by a secondary source, an assumption or a placeholder. The intervals therefore describe the uncertainty in our inputs as found, not in verified data.

### A1. Reproducing the results

Every table and figure in §6 and Appendices A and C regenerates in about five seconds from one parameter file. To change a value, edit `parameters_lca.yaml` and re-run the three scripts.

*Table A1. Scripts, inputs and outputs.*
*Source: `03_LCA_Calculations/`.*

| Step | Command (from the repository root) | Output |
|---|---|---|
| Baseline inventory, fuel mass balance, stage totals | `python3 -I 03_LCA_Calculations/scripts/lca_baseline.py` | `results/lca_baseline.md`, `lca_inventory.csv`, `lca_stages.csv`, `lca_fuel.csv`, Figure F1 |
| Initiative scenarios | `python3 -I 03_LCA_Calculations/scripts/lca_scenarios.py` | `results/lca_scenarios.md`, `lca_scenarios.csv` |
| Tornado and Monte Carlo (Appendix C) | `python3 -I 03_LCA_Calculations/scripts/lca_uncertainty.py` | `results/lca_uncertainty.md`, `lca_tornado.csv`, `lca_montecarlo_summary.csv`, `lca_stages_expected.csv`, Figures F2–F5 |

All three scripts read only `03_LCA_Calculations/parameters_lca.yaml` (68 parameters, each with a value, range, distribution, source key and status).

### A2. Functional unit, lifetime output and key assumptions

**Result.** One unit delivers 1.419 × 10⁸ MWh over its life, the denominator for every per-MWh value in §6 and §7.

- Annual output = P_net × 8,760 h × CF = 300 MWe × 8,760 × 0.90 = 2,365,200 MWh/yr.
- Lifetime output E = 2,365,200 × 60 = **1.419 × 10⁸ MWh**.
- Net efficiency η = P_net / P_th = 300 / 870 = **0.345** (870 MWt from Sun and Kurosaki, 2025, an unrefereed preprint).
- Conversion to the functional unit: 1 t CO₂e spread over E is 7.05 × 10⁻⁶ g/kWh.

Inputs: P_net 300 MWe (GE Vernova Hitachi Nuclear Energy, n.d.), with 315 MWe net in OPG's filing to the Ontario Energy Board (Ontario Power Generation, 2025b) as the upper bound; CF 0.90, a placeholder shared with §7; L 60 years (Canadian Nuclear Safety Commission, 2024; 65 years is reported elsewhere).

*Table A2a. Plant quantities and results per unit: main case and cross-check.*
*Source: this study; BWRX-300 Ostrołęka sp. z o.o. (2023), as reported in the project information sheet; Peterson, Zhao and Petroski (2005).*

| Quantity | Main case (Ostrołęka) | Cross-check (bottom-up) |
|---|---|---|
| Concrete per unit | 50,000 m³ (input range 40,000–60,000) | 20,700 m³ (69 m³/MWe × 300 MWe) |
| Concrete per MWe | 167 m³ | 69 m³ |
| Steel per unit | 14,000 t (11,200–16,800) | 9,900 t (33 t/MWe × 300 MWe) |
| Rebar; plate, structural and equipment steel | 7,500 t; 6,500 t | 3,105 t; 6,795 t |
| C1-eligible concrete | 20,000 m³ (40%; 10,000–30,000) | 13,081 m³ (infill and forebay shaft) |
| Construction, mode case | 57,600 t CO₂e (0.41 g/kWh) | 34,381 t (0.24 g/kWh) |
| Life cycle: mode case; Monte Carlo median (90% interval) | 2.86; 4.40 (3.24–6.05) g/kWh | 2.70; 4.20 (3.05–5.86) g/kWh |

*Table A2b. Key assumptions for one BWRX-300 at Darlington (all 45 ranged inputs in Appendix C, Table C2).*
*Source: `parameters_lca.yaml`; references as listed. Ranges are model input bounds, not result intervals.*

| Parameter | Central (input range) | Basis |
|---|---|---|
| Net output; capacity factor; design life | 300 MWe (300–315); 0.90 (0.80–0.95); 60 years (40–80) | GE Vernova Hitachi Nuclear Energy (n.d.); Ontario Power Generation (2025b); placeholder; Canadian Nuclear Safety Commission (2024) |
| Plant concrete; steel | 50,000 m³ (40,000–60,000); 14,000 t (11,200–16,800) | BWRX-300 Ostrołęka sp. z o.o. (2023), as reported; ±20% is our assumption |
| Baseline concrete factor (S0) | 380 kg CO₂e/m³ (330–420) | Pillai et al. (2019), as reported; range from Canadian Ready-Mixed Concrete Association (2022) Ontario values (334 and 417) |
| LC³ concrete factor; cut | 270 kg CO₂e/m³; 28.9% (22–39%) | Pillai et al. (2019), as reported; range is our assumption |
| Eligible share for LC³ | 40% (20–60%) | Assumption: non-safety works first; DPSC infill only if qualified |
| Rebar; plate and equipment steel | 0.97 (0.89–1.99); 1.73 (1.22–2.50) t CO₂e/t | Concrete Reinforcing Steel Institute (2017; a 2022 declaration supersedes it); American Institute of Steel Construction (2022), Buy Clean California limits as proxies |
| Other materials and site energy | +50% of bulk materials (25–150%) | Assumption |
| Mining and milling | 42 kg CO₂e/kg U₃O₈ (24–81) | Parker, McNaughton and Sparrow (2016) |
| Conversion heat; centrifuge enrichment | 26 kWh/kg U (26–665); 50 kWh/SWU (40–100) | Gibon and Hahn Menacho (2023) |
| Enrichment; burnup | 3.8% U-235 (3.4–4.95); 45 GWd/t (35–55) | Sun and Kurosaki (2025), unrefereed preprint; assumption (both placeholders) |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 g/kWh (×0.5 to ×2; decommissioning ×3) | EDF R&D (2024) stage shares as reported by secondary sources; back end by difference |
| Cross-check and slag inputs | GU cement 854 kg CO₂e/t (796–898); slag cement 146.6 (93.4–146.6); binder 350 kg/m³ | Cement Association of Canada (2022); Slag Cement Association (n.d.); assumption |

### A3. Material quantities per unit

**Result.** The main case is 50,000 m³ of concrete and 14,000 t of steel per unit, with 20,000 m³ (40%) eligible for C1. **These come from a Polish design (Ostrołęka) and are a proxy, not measured Darlington quantities.** We do not know whether they cover the whole site or the nuclear island, or whether the steel includes equipment; if equipment is excluded, the construction uplift (A7) covers it. Darlington's 35 m reactor shaft, forebay and tunnels may differ. No BWRX-300 bill of materials could be opened (searched: OPG's environmental impact statement review report, TVA's Clinch River environmental report, GEH's NEDO-33914; only front matter or summaries were visible).

- Rebar = ρ × plant concrete = 0.15 t/m³ × 50,000 = **7,500 t** (assumption; range 0.10–0.25, the high value being the forebay's observed 0.25). Plate, structural and equipment steel = 14,000 − 7,500 = **6,500 t**. Rebar is capped at total steel, so plate never goes negative.
- C1-eligible concrete = eligible share × plant concrete = 0.40 × 50,000 = **20,000 m³**; 10,000 and 30,000 m³ at 20% and 60%. The eligible share is a scenario, not data.
- The Monte Carlo 90% interval for plant concrete is 43,224–56,772 m³ (the input is triangular, 40,000–50,000–60,000 m³).

**Cross-check (bottom-up).** Concrete = I_c × P_net and steel = I_s × P_net, with the ESBWR's I_c = 69 m³/MWe and I_s = 33 t/MWe (Peterson, Zhao and Petroski, 2005), because the BWRX-300 descends from the ESBWR: 20,700 m³ and 9,900 t. The vendor claims about 50% less concrete per MW (GE Vernova, n.d.; 34.5 m³/MWe) and the ABWR has 138 m³/MWe; the central case assumes the claimed halving offsets small-plant scale penalties. The cross-check's C1 concrete, 13,081 m³, is the diaphragm-plate steel-composite (DPSC) infill (9,081 m³, from assumed module geometry and wall thicknesses) plus the forebay shaft (4,000 m³ placed to date; Ontario Power Generation, 2025c). Ostrołęka's 167 m³/MWe is 2.4 times the ESBWR's, which is why the main case has more construction emissions (Table A2a).

### A4. Construction inventory and corrections to the team spreadsheet

**Result.** Construction emits 57,600 t CO₂e per unit at the mode case (0.41 g/kWh); concrete and steel are about equal.

*Table A4. Construction inventory per unit (S0, mode case; production-stage factors).*
*Source: `results/lca_baseline.md`; factors as in A5.*

| Item | Quantity | Factor | t CO₂e |
|---|---|---|---:|
| C1-eligible concrete (40%) | 20,000 m³ | 380 kg CO₂e/m³ | 7,600 |
| Other plant concrete | 30,000 m³ | 380 kg CO₂e/m³ | 11,400 |
| Rebar | 7,500 t | 0.97 t CO₂e/t | 7,275 |
| Plate, structural and equipment steel | 6,500 t | 1.73 t CO₂e/t | 11,245 |
| Transport to site | concrete 15 km, steel 500 km | 0.10 kg CO₂e/t-km | 880 |
| Other materials and site energy | +50% of the above | | 19,200 |
| **Construction total** | | | **57,600** |

Corrections made to the team spreadsheet (kept as `Accounting_corrected.csv`; the originals are untouched):
1. **Site.** The Darlington New Nuclear Project is in Clarington, Ontario, not Ottawa.
2. **Tunnel boring.** The 4,127.29 m³ in the assumptions file is the forebay concrete (4,000 m³) plus its rebar (127.39 m³), not a bored volume. Tunnel-boring energy sits in the construction uplift until data exist.
3. **Scope.** The forebay and basemat-module rows describe one milestone of one Unit 1 structure and are labelled partial; the whole-unit rows replace them.
4. **Rebar** uses a recycled-content (electric-arc furnace) factor, not virgin steel, and construction electricity is not assumed renewable.

### A5. Emission factors

**Result.** Every factor is a published North American or Canadian value where one was found, and an assumption otherwise. Construction-material factors are cradle-to-gate (production stage). The impact category is climate change, GWP100; the US grid factors are CO₂ only, used as CO₂e, which understates slightly.

*Table A5. Emission and energy factors used.*
*Source: `parameters_lca.yaml`; references as listed.*

| Factor | Central | Range | Unit | Reference |
|---|---|---|---|---|
| Baseline concrete (OPC, M50) | 380 | 330–420 | kg CO₂e/m³ | Pillai et al. (2019), as reported; range from Canadian Ready-Mixed Concrete Association (2022) |
| LC³ concrete | 270 | cut 28.9% (22–39%) | kg CO₂e/m³ | Pillai et al. (2019), as reported; range assumed |
| Rebar (electric-arc furnace, fabricated) | 0.97 | 0.89–1.99 | t CO₂e/t | Concrete Reinforcing Steel Institute (2017); low = American Institute of Steel Construction (2022) limit; high = world average (Circular Ecology, 2019, read via a secondary) |
| Plate, structural and equipment steel | 1.73 | 1.22–2.50 | t CO₂e/t | American Institute of Steel Construction (2022): a Buy Clean California limit (a policy ceiling, not an industry average), used as a proxy; high assumed for forged equipment |
| Heavy truck | 0.10 | 0.06–0.15 | kg CO₂e/t-km | Assumption |
| Mining and milling | 42 | 24–81 | kg CO₂e/kg U₃O₈ | Parker, McNaughton and Sparrow (2016), Saskatchewan, production-weighted |
| Conversion: electricity; heat | 11.8; 26 | 10.3–16.9; 26–665 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Centrifuge enrichment | 50 | 40–100 | kWh/SWU | Gibon and Hahn Menacho (2023) |
| Fuel fabrication | 36 | 36–50 | kWh/kg U | Gibon and Hahn Menacho (2023) |
| Grid: conversion (Ontario) | 0.0738 | 0.035–0.343 | kg CO₂e/kWh | The Atmospheric Fund (2025); low = Canada Energy Regulator (n.d.) |
| Grid: enrichment and fabrication (USA) | 0.373 | 0.05–0.637 (enrichment); 0.20–0.637 (fabrication) | kg CO₂/kWh | US EPA (2024); lows assumed |
| Natural-gas heat | 0.202 | — | kg CO₂/kWh | IPCC (2006): 56,100 kg/TJ × 3.6 × 10⁻⁶ TJ/kWh; combustion only, upstream gas cut off |
| O&M; decommissioning; back end | 0.33; 0.11; 0.56 | 0.17–0.67; 0.06–0.33; 0.28–1.11 | g CO₂e/kWh | EDF R&D (2024): 9%, 3% and 15% of 3.7 g/kWh, shares as reported by secondary sources, back end by difference; ranges assumed for transfer to one BWRX-300 |
| *Cross-check and slag only:* GU cement | 854 | 796–898 (regional spread) | kg CO₂e/t | Cement Association of Canada (2022), Central region; St Marys Bowmanville declaration (NRMCA, 2021) to replace it |
| *Cross-check and slag only:* slag cement | 146.6 | 93.4–146.6 | kg CO₂e/t | Slag Cement Association (n.d.) |
| *Cross-check only:* binder content (infill; other) | 450; 350 | 400–550; 300–420 | kg/m³ | EFNARC (2005) for the SCC range; central and high assumed |
| *Cross-check only:* clinker factor GU; LC³ | 0.92; 0.50 | 0.90–0.95; 0.50–0.55 | t/t binder | Assumption; Scrivener et al. (2018) |

**The LC³ cut.** The main case takes the concrete-level cut from Pillai et al. (2019): 1 − 270/380 = 28.9%. This is below the binder-level cuts in five published estimates (30% to 43%, median 37%: ENR, 2018; Development Alternatives, n.d.; LC3 Project, 2015; Scrivener et al., 2018; LACCEI, 2026), as it should be, because aggregates, water and batching are unchanged. The range 22–39% is our assumption. The estimates come from Indian, Cuban and Latin American settings; an Ontario LC³ calcined with natural gas is untested.

**Check on the baseline factor.** 380 kg CO₂e/m³ lies between the cross-check's binder-level mixes (329 and 414) and between the Ontario industry baseline of 334 and the 417 benchmark mix (Canadian Ready-Mixed Concrete Association, 2022).

### A6. Concrete and the C1 scenarios

**Result.** LC³ on 40% of plant concrete saves 2,200 t CO₂e per unit (28.9% of that concrete's emissions) and avoids about 2,940 t of clinker; a slag blend saves 2,288 t.

**Baseline S0** is the concrete OPG would pour anyway, at 380 kg CO₂e/m³. We have seen neither OPG's mix nor any cement-type limit in the specification (GE-Hitachi Nuclear Energy, 2024). If OPG's mix already contains slag (40% of binder, in all plant concrete), LC³'s increment on the eligible concrete is −88 t per unit (−0.02% of the life cycle), so every saving below is then overstated.

- **LC³ (C1):** saving = V_eligible × (380 − 270) / 1,000 = 20,000 × 0.110 = **2,200 t**; 10,000 m³ gives 1,100 t and 30,000 m³ gives 3,300 t. Share of the mode-case life cycle: 2,200 / 406,462 = 0.54%; the Monte Carlo median is lower (0.36%) because the total grows with the skewed inputs while the saving barely moves (§6.4).
- **Slag (S1, fallback):** the model's binder-level cut for 40% slag is 0.4 × (1 − 146.6/854) = 33.1% of binder emissions, which is 30.1% of the concrete's (binder is 91% of a 350 kg/m³ mix's emissions), applied to 380 kg/m³: 20,000 × 0.114 = **2,288 t**.
- **Clinker (indicative):** clinker avoided = V × b × (0.92 − 0.50) / 1,000 with b = 350 kg/m³: 20,000 × 0.147 = **2,940 t**. Pillai's binder content is not known to us, so this is indicative.
- **Units 2–4** = 3 × per unit, because Unit 1's basemat is placed. Whether Unit 1's shaft-wall infill could still use LC³ is unknown.

*Table A6. C1 scenario totals, mode case. Shares divide by the mode-case life-cycle total of the row's own basis (main 406,462 t; cross-check 383,243 t).*
*Source: `results/lca_scenarios.md`.*

| Scenario | Saving t CO₂e/unit | Units 2–4 t | Clinker avoided t/unit (Units 2–4) | % of target concrete | % of unit life cycle | g/kWh saved |
|---|---:|---:|---:|---:|---:|---:|
| LC³ on 20% of plant concrete | 1,100 | 3,300 | 1,470 (4,410) | 28.9 | 0.271 | 0.0078 |
| **LC³ on 40% (central)** | **2,200** | **6,600** | **2,940 (8,820)** | **28.9** | **0.541** | **0.0155** |
| LC³ on 60% of plant concrete | 3,300 | 9,900 | 4,410 (13,230) | 28.9 | 0.812 | 0.0233 |
| Slag blend on the same 40% (fallback) | 2,288 | 6,865 | 2,576 (7,728) | 30.1 | 0.563 | 0.0161 |
| *Cross-check:* slag in infill and forebay | 1,552 | 4,657 | 2,019 (6,057) | 30.6 | 0.405 | 0.0109 |
| *Cross-check:* LC³ in infill and forebay | 1,734 | 5,201 | 2,304 (6,913) | 34.1 | 0.452 | 0.0122 |

Monte Carlo basis (median, with 5th–95th percentile; Table C4b): LC³ on 40% with eligibility, cut and volumes all varying, 2,217 t per unit (1,375–3,294) and 6,651 t for Units 2–4 (4,124–9,881), 0.35% of the life cycle (0.19–0.61%); at fixed eligibility 0.18% (20%), 0.36% (40%) and 0.54% (60%). Slag 2,140 t (1,310–3,238), 0.34% (0.18–0.60%). LC³ beats slag in 55% of draws.

**Resource use per unit of output.** Clinker avoided = 2,940 t / 1.419 × 10⁸ MWh = 0.021 kg/MWh (9.8 t per MWe). Concrete: 50,000 m³ × 2.4 t/m³ / 1.419 × 10⁸ MWh = 0.85 kg/MWh. Steel: 14,000 t / 1.419 × 10⁸ MWh = 0.099 kg/MWh.

### A7. Steel, transport and construction total

**Result.** Construction emits 57,600 t CO₂e per unit (0.406 g/kWh, mode case); concrete (19,000 t) and steel (18,520 t) are about equal.

- Concrete: 50,000 m³ × 380 = **19,000 t**. Steel: 7,500 × 0.97 + 6,500 × 1.73 = 7,275 + 11,245 = **18,520 t**.
- Transport to site (production-stage module A4): concrete 50,000 m³ × 2.4 t/m³ × 15 km × 0.10 kg/t-km = 180 t; steel 14,000 t × 500 km × 0.10 kg/t-km = 700 t; total **880 t** (distances assumed).
- Other materials and site energy (copper, cabling, insulation, site diesel and electricity, equipment beyond steel production, tunnel boring): 50% (assumption; range 25–150%) of concrete + steel + transport: 0.5 × 38,400 = **19,200 t**.
- **Construction total** = 19,000 + 18,520 + 880 + 19,200 = **57,600 t**, or 57,600 / 1.419 × 10⁸ MWh = **0.406 g/kWh**.

**Steel scenarios.** S3 is a sensitivity on the baseline steel, not part of C1; only the like-for-like row compares with C1's saving.
- **Like-for-like (target-structure steel only):** the known steel in the structures C1 targets at the low-end factors (plate 1.22, the Buy Clean California hot-rolled-sections limit; rebar 0.89): 953 t of Unit 1 basemat-module plate (as reported in press coverage of the module lift) × (1.73 − 1.22) + 1,000 t of forebay rebar (Ontario Power Generation, 2025c) × (0.97 − 0.89) = 486 + 80 = **566 t per unit**. Shaft-wall module steel is unknown and excluded, so this is a floor.
- **Whole-plant upper bound:** all 14,000 t at the same low factors: 7,500 × 0.08 + 6,500 × 0.51 = 600 + 3,315 = **3,915 t**. It is an upper bound because it applies a hot-rolled-sections factor to forgings and nuclear-grade plate, for which that factor is not shown to be feasible.
- **World average:** all steel at the high-range factors (rebar 1.99, plate 2.50): **−12,655 t**; world-average steel would add emissions.

*Table A7b. Further scenarios: slag elsewhere and steel (S2b, S3), mode case and Monte Carlo (median, 5th–95th percentile).*
*Source: `results/lca_scenarios.md` and `lca_uncertainty.md`. S3 rows are steel sensitivities, not part of C1; negative means more emissions than the baseline.*

| Scenario | Saving t CO₂e/unit: mode case; Monte Carlo | Units 2–4 t | Share of life cycle: mode case; Monte Carlo |
|---|---|---|---|
| S2b: LC³ on 40% plus slag in all other concrete (upper bound) | 5,633; 5,517 (4,346–6,841) | 16,898 | 1.39%; 0.89% (0.57–1.36) |
| S3 like-for-like: target-structure steel only | 566; 940 (415–1,580) | 1,698 | 0.14%; 0.15% (0.06–0.28) |
| S3 upper bound: all steel, best-practice sections factors | 3,915; 6,428 (2,521–11,486) | 11,745 | 0.96%; 1.03% (0.38–2.04) |
| S3 world-average steel | −12,655; −9,914 (−14,037 to −4,904) | −37,965 | −3.11%; −1.56% (−2.70 to −0.72) |

At the mode case LC³'s 2,200 t is 3.9 times the like-for-like steel saving (2.4 times at the Monte Carlo median) and 0.6 times the whole-plant upper bound (0.3 at the median). Within the structures C1 targets, concrete is the bigger lever; across the plant, steel is.

### A8. Fuel cycle and life-cycle total

**Result.** The fuel front end emits 1.46 g/kWh in the mode case (51%) and 2.76 g/kWh on the expected basis (62%, Appendix C3). Four units need about 196 t of natural uranium and 138 tSWU a year.

Mass balance (inputs: burnup B = 45 GWd/t, a placeholder; product assay x_p = 3.8% U-235, a placeholder from Sun and Kurosaki, 2025; feed x_f = 0.711%; tails x_t = 0.25%, an assumption):
- Electricity per kg of enriched uranium = B × 24,000 kWh_th per kg per (GWd/t) × η = 45 × 24,000 × 0.345 = 372,414 kWh, so **2.685 g enriched U per MWh**.
- Feed factor F = (x_p − x_t) / (x_f − x_t) = (3.8 − 0.25) / (0.711 − 0.25) = **7.70**, so **20.68 g natural U per MWh**.
- Separative work per kg of product = V(x_p) + (F − 1) V(x_t) − F V(x_f), with V(x) = (2x − 1) ln[x / (1 − x)]: 2.986 + 6.70 × 5.959 − 7.70 × 4.869 = **5.42 SWU/kg**, so **0.0146 SWU per MWh**.
- U₃O₈ to uranium: 3 × 238.03 / (3 × 238.03 + 8 × 16.00) = 0.848 kg U per kg U₃O₈.

Stage emissions, kg CO₂e per MWh (= g/kWh), mode case:
- Mining and milling = 0.02068 kg U/MWh × 42 / 0.848 = 0.02068 × 49.5 = **1.024**.
- Conversion = 0.02068 × (11.8 kWh × 0.0738 + 26 kWh × 0.202) = 0.02068 × 6.12 = **0.127**.
- Enrichment = 0.002685 × 5.42 × 50 kWh/SWU × 0.373 = **0.272**.
- Fabrication = 0.002685 × 36 kWh × 0.373 = **0.036**.

*Table A8a. Fuel demand.*
*Source: `results/lca_baseline.md`. Inputs are placeholders until BWRX-300 fuel data are available.*

| Quantity | Per MWh | One unit per year | Four units per year |
|---|---:|---:|---:|
| Enriched uranium | 2.685 g | 6.35 t U | 25.4 t U |
| Natural uranium | 20.68 g | 48.9 t U | 195.6 t U |
| Separative work | 0.0146 SWU | 34.4 tSWU | 137.7 tSWU |

*Table A8b. Life-cycle emissions by stage, mode case (every input at its central value).*
*Source: `results/lca_baseline.md`. The expected-value breakdown quoted in §6 is in Appendix C3.*

| Stage | g CO₂e/kWh | t CO₂e per unit (life) | Share |
|---|---:|---:|---:|
| Fuel: mining and milling | 1.024 | 145,336 | 35.8% |
| Back end: spent fuel and disposal | 0.560 | 79,471 | 19.6% |
| Operation and maintenance | 0.330 | 46,831 | 11.5% |
| Fuel: enrichment | 0.272 | 38,530 | 9.5% |
| Construction: other materials and site energy | 0.135 | 19,200 | 4.7% |
| Construction: concrete | 0.134 | 19,000 | 4.7% |
| Fuel: conversion | 0.127 | 17,967 | 4.4% |
| Decommissioning | 0.110 | 15,610 | 3.8% |
| Construction: plate, structural and equipment steel | 0.079 | 11,245 | 2.8% |
| Construction: rebar | 0.051 | 7,275 | 1.8% |
| Fuel: fabrication | 0.036 | 5,117 | 1.3% |
| Construction: transport to site | 0.006 | 880 | 0.2% |
| **Total** | **2.864** | **406,462** | **100%** |
| *Of which C1-eligible concrete (40% of plant)* | *0.054* | *7,600* | *1.9%* |

Grouped (mode case): fuel front end 1.458 g/kWh (50.9%); back end and decommissioning 0.670 (23.4%); O&M 0.330 (11.5%); construction 0.406 (14.2%).

### A9. Granta EduPack Eco Audit

A Granta EduPack Eco Audit cross-check was planned but not completed; the screening model in Appendix A is the basis of all results.

---


## Appendix B. Working for the policy and supply-chain analysis

This appendix gives the full working behind §8.1 (law and licensing), §8.3 (fuel-supply concentration), §8.4–8.5 (social licence and stakeholders, B8), §7 (displacement, the value of schedule and the same money) and §9 (the multi-criteria analysis). Every number is produced by a script in `03_LCA_Calculations/scripts/` from a parameter file, so it can be re-run. Inputs are taken from the documents cited or, where marked "as reported", from the secondary source named; assumptions and our own inferences are labelled as such.

| Subsection | Script (run from the repository root) | Inputs | Output |
|---|---|---|---|
| B1 Legal and political pathway | `python3 -I 03_LCA_Calculations/scripts/law_timelines.py` | `03_LCA_Calculations/parameters_run2.yaml` | `03_LCA_Calculations/results/law_timelines.csv` |
| B2 Supply concentration (HHI) | `python3 -I 03_LCA_Calculations/scripts/hhi.py` | `03_LCA_Calculations/parameters_run3.yaml` | `03_LCA_Calculations/results/hhi.md`, `hhi_summary.csv` |
| B3 Routes to a licensable SMR in Australia | none: hand calculation (qualitative scoring) | Table B13 | This appendix |
| B4 Displacement | `python3 -I 03_LCA_Calculations/scripts/displacement.py` | `03_LCA_Calculations/parameters_run1.yaml` | `03_LCA_Calculations/results/displacement.md` |
| B5 Value of schedule | `python3 -I 03_LCA_Calculations/scripts/schedule_value.py` | `parameters_run1.yaml` (`c1_deck_*` keys; cost inputs read from `parameters_run5.yaml`) | `results/schedule_value.md` |
| B6 Same money | `python3 -I 03_LCA_Calculations/scripts/same_money.py` | `parameters_run1.yaml` | `results/same_money.md` (cross-check: `results/lcoe.md`) |
| B7 Multi-criteria analysis | `python3 -I 03_LCA_Calculations/scripts/mcda.py --c1-case new_2200` | `parameters_run9.yaml` (with run 6 consent routes) | `results/mcda.md`, `results/mcda_scores.csv` |
| B8 Social licence and stakeholder working | `python3 -I 03_LCA_Calculations/scripts/social_licence.py` | `03_LCA_Calculations/parameters_run6.yaml` | `results/social_licence.md`, `F8_stakeholder_map.png` |

---

### B1. Legal and political pathway

**Result.** Three laws bar an SMR at Liddell, and each has a different veto holder. On current party positions, the federal repeal is about 7 Senate votes short (2–3 short even with every other crossbencher: about 39 votes are needed and at most 37 are available), and the NSW repeal bill is stalled. For comparison, Darlington's licence to construct took about 29 months, 17.9 years after its environmental assessment began.

#### B1.1 The three legal barriers and what removes each

*Table B1. The legal barriers to an SMR at Liddell, what removes each, and who holds the veto.*
*Source: legislation as named; ARPANSA (n.d.); Parliament of New South Wales (2025; 2026); Canberra Times (2025); Newcastle Herald (2024a).*

| # | Barrier | Instrument and effect (as extracted) | What removes it | Who decides (veto holder) | Status, October 2026 |
|---|---|---|---|---|---|
| 1 | Federal environmental approval | *Environment Protection and Biodiversity Conservation Act 1999* (Cth) s 140A (parallel bars in ss 37J and 146M): the Minister "must not approve" an action involving the construction or operation of a nuclear power plant | Amendment of ss 37J, 140A and 146M | Commonwealth Parliament; in practice the Senate (B1.2) | In force. Whether the 2025 EPBC reforms changed s 140A has not been checked (Norton Rose Fulbright, 2025) |
| 2 | Federal radiation licensing | *Australian Radiation Protection and Nuclear Safety Act 1998* (Cth) s 10(2): the CEO "must not issue a licence" for a nuclear power plant. ARPANSA licenses only Commonwealth-controlled bodies (s 13, "controlled person") (ARPANSA, n.d.) | Repeal of s 10, **and** a regulator with power over private operators (route choice, B3) | Commonwealth Parliament (Senate) | In force. A Senate committee recommended against the 2022 repeal bill (Senate Environment and Communications Legislation Committee, 2023); the bill lapsed at prorogation |
| 3 | State ban | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8: offence to build or operate a nuclear reactor, except for the s 8(3) exceptions (the Commonwealth's AAEC successors, such as ANSTO); s 9: other Acts do not authorise a state authority to build or approve one | NSW repeal, or a Commonwealth override under Constitution s 109, which Partlett warns may face a High Court challenge (Canberra Times, 2025) | NSW Parliament (Legislative Assembly), or the Commonwealth | Repeal bill passed the Legislative Council; stalled in the Assembly (B1.3) |
| (4) | Site (not a law) | AGL owns Liddell and has ruled out nuclear there (Newcastle Herald, 2024a) | AGL's consent, or compulsory acquisition by the Commonwealth | AGL, or the Commonwealth | AGL opposed |

Order of removal: federal repeal (1 and 2) → choice of regulator → state repeal or override (3) → site (4) → environmental assessment → licensing. Each step has a different veto holder, so all must agree.

#### B1.2 Senate arithmetic for federal repeal

*Table B2. Senate composition used for the repeal arithmetic.*
*Source: Parliament of Australia (2026), composition as at 14 May 2026; `parameters_run2.yaml`.*

| Party or group | Seats | Position on repeal | Source of position |
|---|---:|---|---|
| Australian Labor Party | 30 | Opposed | Bowen (2025); no 2026 statement found |
| Coalition | 27 | For | Liberal Party of Australia (2026); ABC News (2026), as reported |
| Australian Greens | 10 | Opposed | Australian Greens (2025) |
| One Nation | 4 | Assumed for | **Assumption** (upper bound for the pro-repeal bloc) |
| Senator Babet | 1 | Assumed for | **Assumption** (no source) |
| Lambie, Payman, Pocock, Thorpe | 4 (1 each) | Not assumed | — |
| **Total** | **76** | | Script asserts the parts sum to 76 |

Steps (`law_timelines.py`):

| Step | Working | Result |
|---|---|---|
| 1. Majority needed, all 76 voting | ⌊76 / 2⌋ + 1 (a tied vote fails, Constitution s 23) | **39** |
| 2. Largest pro-repeal bloc (upper bound) | Coalition 27 + One Nation 4 + Babet 1 | **32** |
| 3. Shortfall | 39 − 32 | **7** |
| 4. Bloc plus every other crossbencher | 32 + 4 | **36** (3 short); **37** (2 short) on the alternative count in step 7 |
| 5. Can repeal pass without Labor or the Greens? | 36 or 37 ≥ 39? | **No** on either count |
| 6. Would the Greens alone be enough (arithmetic only)? | 32 + 10 = 42 ≥ 39? | Yes, but the Greens oppose (policy, not arithmetic) |
| 7. Opposed bloc | Labor 30 + Greens 10 = 40 ≥ 39 (39 on the alternative count) | A blocking majority on its own |

Result 4 makes the conclusion independent of the One Nation and Babet assumption (it holds on either count of seats). In the House, Labor holds 94 of 150 seats (Australian Electoral Commission, 2025), so a repeal bill would also need the Government's support there.

#### B1.3 NSW repeal bill status

*Table B3. Progress of the NSW repeal bill (private member's bill).*
*Source: Parliament of New South Wales (2025; 2026); `parameters_run2.yaml`.*

| Event | Date | Note |
|---|---|---|
| Introduced in the Legislative Council | 19 November 2025 | — |
| Passed the Legislative Council | 6 May 2026 | About 5.5 months after introduction. All Liberal and National MLCs voted for it |
| Legislative Assembly | Awaiting the second reading speech (notice paper reported 27 May 2026) | The Minns Labor Government opposes repeal and holds an Assembly majority (Canberra Times, n.d., as reported) |
| Lapses | 28 November 2026 | Unless the Assembly acts first |

#### B1.4 Licensing timelines: Darlington (Canada)

*Table B4. CNSC licensing milestones for the Darlington New Nuclear Project.*
*Source: Canadian Nuclear Safety Commission [CNSC] (2021; 2025; 2026a; 2026b); `parameters_run2.yaml`.*

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
| Against the CNSC's expected review time (REGDOC-3.5.1; CNSC, 2022; the extract is ambiguous: one row reads 32 months, another 24) | 29.1 − 32; 29.1 − 24 | −2.9 months (faster); +5.1 months (slower) |
| Hearing part 2 to decision | 8 Jan 2025 → 4 Apr 2025 | 2.8 months |
| Environmental assessment start to licence to construct | May 2007 → 4 Apr 2025 | **17.9 years** (elapsed, not continuous review) |
| Licence validity from issue | 4 Apr 2025 → 31 Mar 2035 | 10.0 years |
| Licence validity remaining at the report date | 20 Oct 2026 → 31 Mar 2035 | 8.4 years |
| Licence to construct to RHP-1 lifted | 4 Apr 2025 → 30 Mar 2026 | 11.8 months |

The licence covers one unit. Units 2–4 need a further Commission authorisation (our inference), with approval to proceed reported as expected in 2028 (American Nuclear Society, 2026, as reported; the type of approval is not stated). No source gives the Units 2–4 review time.

Australian comparator: the naval nuclear regulator (ANNPSR) began operating on 1 November 2025 under a 2024 Act (Minister for Defence, 2025). It covers submarines only, so it is a precedent for building a regulator, not a regulator for a power reactor.

---

### B2. Supply concentration: Herfindahl–Hirschman index (HHI) working

**Result.** On the 2023 US merger guidelines, mining by country (2,341), conversion (2,111) and enrichment (3,009) are all "highly concentrated". On the superseded 2010 guidelines only enrichment is; mining and conversion are "moderately concentrated". Removing Russia raises the HHI at every stage. Removing Russia and China leaves enrichment as a Urenco–Orano duopoly (5,621). The one case below 1,800 is mining by company (about 850–1,400, from the top three firms only; midpoint 1,118), so mining concentration is a country (geopolitical) risk rather than a market-power risk.

#### B2.1 Method

1. Share of supplier *i*: s*ᵢ* = 100 × q*ᵢ* / Σq (per cent), where q is output or capacity.
2. HHI = Σ s*ᵢ*² (range 0 to 10,000; one supplier = 10,000).
3. Equivalent number of equal-sized suppliers: N_eq = 10,000 / HHI.
4. Measures: mining by country (2024 mine output, tU); conversion by company (licensed capacity, tU as UF₆ per year; production as a check); enrichment by company (capacity, thousand SWU per year; 2025 base, 2022 and 2030 as sensitivity).
5. "Without Russia": Russian supply removed and the remaining shares renormalised, with no new capacity (the market open to a buyer barred from Russian material). "Without Russia and China" also removes CNNC, whose capacity WNA estimates on the assumption that it serves China's own fleet; this approximates the market open to a Canadian or Australian utility.
6. "Others" or residual rows are bounded: one supplier (upper bound) or many small suppliers (lower bound, about 0). The difference is below 3 HHI points in every 2024/2025 case.
7. Shares are squared before rounding, so squaring a rounded share in the tables can differ by less than 1 point.

*Table B6. HHI thresholds used as a scale.*
*Source: US Department of Justice and Federal Trade Commission (2023; 2010).*

| Guideline | Unconcentrated | Moderately concentrated | Highly concentrated | Status |
|---|---|---|---|---|
| *Merger Guidelines* (2023), §2.1 | — | — | HHI > 1,800 | Current |
| *Horizontal Merger Guidelines* (2010), §5.3 | < 1,500 | 1,500–2,500 | > 2,500 | Superseded; reported because mining and conversion fall between the two thresholds |

These are antitrust screens for merger review. Here they are used as a recognised scale for supply concentration, not as a legal test.

**Worked example (enrichment, 2025).**
1. Rosatom's share = 100 × 29,133 / 68,077 = 42.79%; squared = 1,831.3.
2. Repeat for Urenco, CNNC, Orano and Other; sum = 1,831.3 + 645.8 + 410.3 + 121.4 + 0.3 = **3,009**. N_eq = 10,000 / 3,009 = 3.3.
3. Without Russia: total = 68,077 − 29,133 = 38,944 kSWU. Urenco's share = 100 × 17,300 / 38,944 = 44.42%; and so on. HHI = **3,599**.
4. Without Russia and China: total = 38,944 − 13,789 = 25,155 kSWU. Urenco 68.77%, Orano 29.82%, Other 1.41%. HHI = **5,621** (N_eq = 1.8).

#### B2.2 Inputs and shares

*Table B7. Uranium mine output by country, 2024.*
*Source: World Nuclear Association (2026); several rows are WNA estimates; calculated in `hhi.py` (`results/hhi.md` §3.1–3.2). Internal check: the rows sum exactly to 60,213 tU.*

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
*Source: World Nuclear Association (2026); `results/hhi.md` §3.3.*

| Year | Residual (tU) | HHI lower bound | HHI upper bound | Russia's share (%) |
|---|---:|---:|---:|---:|
| 2022 | 1,083 | 2,368 | 2,372 | 5.1 |
| 2023 | 1,204 | 2,243 | 2,248 | 5.0 |

*Table B9. Conversion by company, licensed capacity (tU as UF₆ per year).*
*Source: World Nuclear Association (2024); CNNC and Rosatom are WNA estimates; `results/hhi.md` §3.5.*

| Company (country) | tU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| CNNC (China) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | — | — |
| Orano (France) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | 43.48 | 1,890.4 |
| Cameco (Canada) | 12,500 | 20.16 | 406.5 | 25.25 | 637.7 | 36.23 | 1,312.7 |
| Rosatom (Russia) | 12,500 | 20.16 | 406.5 | — | — | — | — |
| ConverDyn (USA) | 7,000 | 11.29 | 127.5 | 14.14 | 200.0 | 20.29 | 411.7 |
| **Market total (tU/yr) / HHI** | **62,000** | 100.00 | **2,111** | 49,500 | **2,674** | 34,500 | **3,615** |

*Table B10. Enrichment by company, 2025 capacity (thousand SWU per year).*
*Source: World Nuclear Association (2025); CNNC is a WNA estimate; 2030 figures are plans; `results/hhi.md` §3.6.*

| Company | kSWU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rosatom | 29,133 | 42.79 | 1,831.3 | — | — | — | — |
| Urenco | 17,300 | 25.41 | 645.8 | 44.42 | 1,973.4 | 68.77 | 4,729.8 |
| CNNC | 13,789 | 20.26 | 410.3 | 35.41 | 1,253.7 | — | — |
| Orano | 7,500 | 11.02 | 121.4 | 19.26 | 370.9 | 29.82 | 888.9 |
| Other (INB, JNFL) | 355 | 0.52 | 0.3 | 0.91 | 0.8 | 1.41 | 2.0 |
| **Market total (kSWU/yr) / HHI** | **68,077** | 100.00 | **3,009** | 38,944 | **3,599** | 25,155 | **5,621** |

Russia's enrichment share is 43.3% in 2022 and 38.3% in the 2030 plans (World Nuclear Association, 2025). It is 42.8% on WNA's 2025 capacity and 41.0% on World Nuclear University's (2025) figures, which gives the range quoted in §8.3.

#### B2.3 Headline results

*Table B11. HHI of the uranium front end by stage, with and without Russia and China.*
*Source: `03_LCA_Calculations/results/hhi.md` §2 and `hhi_summary.csv`, from the inputs in Tables B7–B10.*

| Stage (measure, base year) | HHI | N_eq | 2023 class | 2010 class | Without Russia | Without Russia and China | Russia's share |
|---|---:|---:|---|---|---:|---:|---:|
| Mining (output by country, 2024) | 2,341 | 4.3 | Highly | Moderately | 2,546 (highly under both) | 2,686 | 4.5% |
| Conversion (capacity by company) | 2,111 | 4.7 | Highly | Moderately | 2,674 (highly under both) | 3,615 | 20.2% |
| Enrichment (capacity by company, 2025) | **3,009** | 3.3 | Highly | Highly | 3,599 | **5,621** | **42.8%** |

Shares for the two producer countries in the comparison: Canada mined 23.8% of world uranium in 2024 and holds 20.2% of world conversion capacity (36.2% of the capacity open to a Western buyer), with no enrichment. Australia mined 7.6% (4,598 tU) and has no conversion or enrichment capacity. Australia holds 28% of identified recoverable resources at < USD 130/kgU in the 2024 Red Book edition we use (OECD Nuclear Energy Agency and International Atomic Energy Agency, 2025); two tabulations of the 2026 edition give 29% and 27%.

#### B2.4 Sensitivity

*Table B12. HHI under every tested scenario.*
*Source: `03_LCA_Calculations/results/hhi_summary.csv`.*

| Stage | Scenario | HHI | N_eq | 2023 class | 2010 class | Note |
|---|---|---:|---:|---|---|---|
| Mining (country) | 2024 base | 2,341 | 4.3 | Highly | Moderately | |
| Mining (country) | 2024 base, "Others" atomistic | 2,341 | 4.3 | Highly | Moderately | Lower bound |
| Mining (country) | 2024 without Russia | 2,546 | 3.9 | Highly | Highly | |
| Mining (country) | 2024 without Russia and China | 2,686 | 3.7 | Highly | Highly | |
| Mining (country) | 2024 without Russia, China and Niger | 2,778 | 3.6 | Highly | Highly | Niger: exports disrupted since the 2023 coup (secondary) |
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

**Mining by company (the one case below 1,800).** Only the top three 2024 shares were retrieved: Kazatomprom 21%, Cameco 17%, Orano 11% (World Nuclear Association, 2026); Kazatomprom's 21% is cross-checked by Kazatomprom (2025). Together they hold 49%.
1. Lower bound (the other 51% held by many small firms): 21² + 17² + 11² = 441 + 289 + 121 = **851**.
2. Upper bound (the other 51% split into firms no larger than the third-ranked, 11%, i.e. four at 11% and one at 7%): 851 + 4 × 11² + 7² = 851 + 484 + 49 = **1,384**.
3. Central value reported by `hhi.py`: the midpoint, (851 + 1,384) / 2 = **1,118** (N_eq = 8.9).

Both bounds are below 1,500, so firms are not concentrated even though countries are. Kazakhstan's 38.6% country share includes joint ventures with foreign partners, whose ownership was not assessed.

#### B2.5 Limitations

"High" is above 1,800 on the 2023 guidelines and above 2,500 on the 2010 guidelines; "Moderate" is 1,500–2,500 (2010). Without Russia, all three stages are high on both scales. Sensitivity: enrichment 2,724–3,065 (2030 plans to 2022); mining by country 2,246–2,370 (2022–2024); conversion 2,015 with the higher ConverDyn capacity; all country-level and capacity-based cases stay above 1,800. Mining by company is about 850–1,400 (midpoint 1,118; top three firms only), mostly below the threshold. Russia's enrichment share is 42.8% on WNA capacity and 41.0% on World Nuclear University's. Australia's resource share is 28% in the 2024 Red Book edition we use; two tabulations of the 2026 edition give 29% and 27%.

Limits:
- Capacity is not supply. Nameplate SWU includes capacity Rosatom uses for underfeeding and tails re-enrichment, and CNNC's figures are WNA estimates.
- Secondary supply (inventories, down-blending, re-enriched tails) is excluded. Mine output in 2024 (60,213 tU) met about 93% of reactor requirements (64,500 tU at 1 January 2025; OECD Nuclear Energy Agency and International Atomic Energy Agency, 2026).
- Company-level enrichment shares hide plant location: Urenco operates in the UK, Germany, the Netherlands and the USA; Orano only in France.
- Mining by country ignores ownership and the transport routes for Kazakh exports, which were not assessed, so Russia's 4.5% of mining may understate its reach. The company-level bound only partly addresses ownership.
- Fuel fabrication, where BWR fuel is thought to have few suppliers, was not assessed (§11).
- The HHI is a world-market measure. Darlington's own demand is sized against it in B2.6.

#### B2.6 Darlington's fuel demand against supplier capacity

**Result.** Four BWRX-300s need about 196 t of natural uranium and 138 thousand separative work units (tSWU) a year: **3.2% of Urenco USA's current capacity** and 0.56% of the Western (Urenco and Orano) enrichment market. The project is too small to move the HHI. Its exposure is to price and contract terms in a duopoly, not to physical shortage. The inputs are assumed typical BWR reload values (3.8% enrichment, 45 GWd/t burnup).

Working (one unit; `hhi.md` §6):
1. Net generation: 300 MWe × 8,760 h × 0.9 = 2,365,200 MWh. Thermal power 870 MWt gives efficiency η = 300 / 870 = 0.3448.
2. Energy per kg of enriched uranium (3.8% U-235, burnup 45 GWd/t) = 45 × 24,000 kWh × η = 372,414 kWh. Enriched uranium needed = 2,365,200,000 kWh / 372,414 = 6.35 t a year.
3. Natural uranium feed factor 7.701 (tails 0.25%): 6.35 × 7.701 = 48.9 t U. Separative work: 5.422 SWU per kg, so 34.4 tSWU.
4. Four units: 25.4 t enriched, **195.6 t U** and **137.7 tSWU** a year.

*Table B12a. Four-unit demand set against supplier capacity.*
*Source: `results/hhi.md` §6.2, using World Nuclear Association (2025) capacities; demand inputs are assumed.*

| Capacity | tSWU a year | Four-unit demand as a share |
|---|---:|---:|
| Urenco USA (Eunice), current | 4,300 | **3.20%** |
| Urenco USA after the 2027 project | 5,000 | 2.75% |
| Urenco USA after the 2032–2036 expansion | 7,000 | 1.97% |
| Urenco and Orano together | 24,800 | 0.56% |
| World enrichment capacity | 68,077 | 0.20% |

Sensitivity: across burnup (35–55 GWd/t), enrichment (3.4–4.95%), tails (0.2–0.3%) and capacity factor (0.80–0.95), demand is 113–199 tSWU for one input varied at a time, and 77–301 tSWU at the envelope (1.79–7.00% of Urenco USA; not a physically consistent fuel design, because burnup and enrichment move together). **Reserve:** two reloads held in stock embody 275–551 tSWU (6–13% of one year of Urenco USA output), depending on a cycle length of 12 to 24 months (assumed). This is a working-capital question (fuel price, not sourced) rather than a supply question.

---

### B3. Routes to a licensable SMR in Australia: scored comparison

**Result.** The ranking depends on the weights: route C (cooperative state repeal) ranks first on equal weights and when durability is valued more; route A (Commonwealth-owned plant) ties with C when regulator readiness is valued more. Route A has the same three veto points as B and C once the NSW ban is counted, so all three score 1 on that objective. Under the 2026 Senate (B1.2), none of the three routes is open. **These scores are our own qualitative judgement from the evidence in B1, not sourced scores, and the totals and the weight test (Table B14) are hand calculations.** They feed the "feasibility" criterion of the §9 MCDA.

*Table B13. Three routes scored against four non-technical objectives (1 = poor, 3 = good).*
*Source: our qualitative judgement, from the evidence cited in the table.*

| Objective | A. Commonwealth-owned plant under ARPANSA (the Coalition's 2024 model) | B. Federal licensing law for private operators, overriding the states | C. Cooperative: state repeal plus a state or joint regulator |
|---|---|---|---|
| Legal changes needed (not scored) | EPBC and ARPANS repeal, plus a s 109 override of NSW (or NSW repeal) | EPBC and ARPANS repeal, a new federal Act and a s 109 override | EPBC and ARPANS repeal, NSW repeal and a NSW regulator Act |
| Fewest veto points | **1**: Senate; NSW (or the High Court, if the Commonwealth overrides); site owner. A would score 2 only if s 8(3) exempted a Commonwealth operator (our inference) | **1**: Senate; High Court; site owner | **1**: Senate; NSW Parliament; site owner |
| Regulator readiness | **3**: builds on ARPANSA, which already regulates Commonwealth entities such as ANSTO (ARPANSA, n.d.) | **2**: a new body, as with the ANNPSR (Minister for Defence, 2025) | **1**: NSW has no nuclear regulator |
| Durability (low exposure to political reversal) | **1**: one government's decision; the next can sell or cancel | **1**: as A, plus litigation risk (Canberra Times, 2025) | **3**: both levels of government committed |
| Social licence | **1**: the states rejected it in 2024 (Canberra Times, n.d., as reported) | **1**: overrides the states | **3**: the states consent, if they do |
| **Total (of 12)** | **6** | **5** | **8** |

Route A's description rests on ABC News (2024), as reported.

*Table B14. Weight test: totals when one objective counts double (maximum 15).*
*Source: calculated from Table B13.*

| Weighting | A | B | C | Ranking |
|---|---:|---:|---:|---|
| Equal weights (base, of 12) | 6 | 5 | 8 | C, A, B |
| Regulator readiness × 2 | 6 + 3 = **9** | 5 + 2 = 7 | 8 + 1 = **9** | A and C tie, B |
| Durability × 2 | 6 + 1 = 7 | 5 + 1 = 6 | 8 + 3 = **11** | C, A, B |

Reading: route B ranks last under all three weightings tested, and C is never behind A. Valuing regulator readiness more only closes the gap, to a tie with A. The choice between A and C is a choice between speed (an existing regulator) and durability (both levels of government committed). That is a political judgement, not a technical one. Whichever route is assumed, an Australian SMR scores lowest on time to first power in the §9 MCDA.

#### B3.1 Implementation levers for C1 (the §8.6 lever table): scores and weight test

Each lever is scored 1 (poor) to 3 (good) on enforceability, speed and low schedule risk. The scores are our judgement, not sourced; the totals are hand calculations.

*Table B14a. Lever scores and weight test for the §8.6 lever table.*
*Source: our judgement and hand calculation.*

| Lever | Enforceability | Speed | Low risk | Equal (of 9) | Enforceability × 2 | Speed × 2 |
|---|---:|---:|---:|---:|---:|---:|
| L1. OPG specification | 2 | 3 | 3 | **8** | 2×2 + 3 + 3 = 10 | 2 + 3×2 + 3 = **11** |
| L2. Equity-tranche milestone | 3 | 2 | 3 | **8** | 3×2 + 2 + 3 = **11** | 3 + 2×2 + 3 = 10 |
| L3. Ontario shareholder direction | 3 | 2 | 2 | 7 | 3×2 + 2 + 2 = 10 | 3 + 2×2 + 2 = 9 |

Reading: L1 and L2 tie at 8 on equal weights. L2 leads (11) if enforceability counts double and L1 leads (11) if speed does. L3 is never first, so the recommendation (L1 now, L2 at tranche 2) holds under all three weightings.

---

### B4. Displacement: CO₂e avoided by one BWRX-300, Darlington vs Liddell

**Result.** At static grid factors, one unit avoids 1.50 Mt CO₂e a year on the NSW grid average. That is 9.1× what it avoids on Ontario's 2024 average (0.165 Mt), but only 1.9× its avoidance on Ontario's marginal factor (0.80 Mt). Valued over the years each plant could actually run, the gap mostly closes:
- Darlington Unit 1 from 2030 avoids **1.01–6.80 Mt to 2050**.
- Liddell from 2040 avoids **0.67–3.85 Mt to 2050**: less than Darlington on the Step Change proxy, and comparable on the slow transition.
- Liddell wins clearly only if the NEM stops decarbonising (frozen grid, 16.54 Mt).

The grid trajectory, the start year and the post-coal floor dominate the result. The SMR's own life-cycle value moves it by a few per cent. Script: `python3 -I 03_LCA_Calculations/scripts/displacement.py`, with inputs in `parameters_run1.yaml` and output in `results/displacement.md`.

#### B4.1 Method

1. Annual output of one unit: E = P × 8,760 h × CF = 300 MW × 1,000 kW/MW × 8,760 h × 0.90 = **2,365,200,000 kWh (2.365 TWh) a year**.
2. CO₂e avoided in year *y*: A(*y*) = E × (EF_grid(*y*) − EF_SMR) / 10⁶ t. EF is in g CO₂e/kWh, and EF_SMR = 4.2 g/kWh (our Monte Carlo median, §6; 90% interval 3.0–5.8).
3. The cumulative total is the sum of A(*y*) from the first full year of operation to 2035, to 2050 (inclusive), or to the end of a 60-year life.
4. Each grid trajectory is linear between its anchor points and flat afterwards. These are our constructions, not AEMO or IESO series:

| Case | Path | Role |
|---|---|---|
| ON-avg-traj | 73.8 g/kWh (2024) → 15 (2040) | Ontario average |
| ON-marginal-declining | 343 (2024) → 15 (2050) | Ontario marginal; assumes gas leaves the margin by 2050 |
| ON-avg-flat, ON-marginal-flat | 2024 values held | Upper bounds |
| NEM-T1 (Step Change proxy) | 640 (2025) → 30 floor (2038) | Central NEM case |
| NEM-T2 (slow) | 640 (2025) → 30 (2050) | Slow transition |
| NEM-T0 (frozen) | 640 held | Upper bound |
| UB-Bayswater; UB-coal-LCA | 990; 1,000 held | Coal upper bounds |

**Worked example 1 (static, NSW 2025).** 2,365,200,000 × (640 − 4.2) / 10⁶ = **1,503,794 t a year**.

**Worked example 2 (cumulative, Liddell from 2040 on NEM-T1).** The NEM is at its 30 g/kWh floor from 2038, so each year avoids 2,365,200,000 × (30 − 4.2) / 10⁶ = 61,022 t.
- To 2050 (11 years, 2040–2050): 11 × 61,022 = **671 kt**.
- Whole life (60 years): 60 × 61,022 = **3.66 Mt**.

*Table B15. Inputs to B4–B6.*
*Source: `03_LCA_Calculations/parameters_run1.yaml` and the references named.*

| Input | Central (range) | Source | Status |
|---|---|---|---|
| Net output | 300 MWe (290–300) | Assumption (an OPG filing gives 315) | Assumed; 315 tested in Table B19 |
| Capacity factor; design life | 0.90 (0.80–0.95); 60 years (40–80) | Assumption | Assumed |
| SMR life cycle | 4.2 g/kWh (3.0–5.8) | This study (§6, Appendix C) | Our result |
| Ontario average, 2024 | 73.8 g/kWh (73–73.8) | The Atmospheric Fund (2025) | As cited |
| Ontario average, 2022; 2023 | 35; 53 g/kWh | Canada Energy Regulator (n.d.); Government of Ontario (n.d.) | As cited |
| Ontario average, 2040 | 15 g/kWh | Independent Electricity System Operator (2024) | As cited |
| Ontario marginal, 2024 | 343 g/kWh (343–472) | The Atmospheric Fund (2025); high = gas generation, The Atmospheric Fund (2021) | As cited (definition ambiguous) |
| Year gas leaves Ontario's margin | 2050 (2040–2060) | Assumption | Assumed |
| NSW/ACT grid, 2025 (scope 2) | 640 g/kWh | Department of Climate Change, Energy, the Environment and Water (2025) | As cited |
| NEM coal exit (T1); slow exit (T2) | 2038; 2050 | Australian Energy Market Operator (2024), as reported; assumption | As reported; assumed |
| NEM floor after coal | 30 g/kWh (0–80) | Assumption | Assumed |
| Bayswater, sent out | 990 g/kWh | Australian Energy Market Operator (2025) | As cited (older value) |
| Coal, life cycle | 1,000 g/kWh (751–1,095) | United Nations Economic Commission for Europe (2021) | As cited |
| Start years | Darlington Unit 1 2030; Units 2–4 2035 (2034–2036); Liddell 2035 (Coalition claim), 2040 (CSIRO earliest), 2045 (late case) | Government of Ontario (2025); Ontario Power Generation (2025a); ABC News (2024), as reported; Graham, Hayward and Foster (2024); assumption | As cited; assumed |

#### B4.2 Results

*Table B16. Annual CO₂e avoided by one unit at static grid factors.*
*Source: `results/displacement.md` §2.*

| Displaced electricity | EF (g/kWh) | Avoided (t a year) | Ratio to Ontario average 2024 |
|---|---:|---:|---:|
| Ontario average 2022 (CER) | 35 | 72,848 | 0.4× |
| Ontario average 2023 (energy snapshot) | 53 | 115,422 | 0.7× |
| Ontario average 2024 (TAF) | 74 | 164,618 | 1.0× |
| Ontario marginal (TAF 2024) | 343 | 801,330 | 4.9× |
| Ontario gas-fired generation (TAF 2021) | 472 | 1,106,441 | 6.7× |
| NSW/NEM average 2025 (NGA Factors, scope 2) | 640 | 1,503,794 | 9.1× |
| Bayswater coal, sent out | 990 | 2,331,614 | 14.2× |
| Coal, life cycle (UNECE) | 1,000 | 2,355,266 | 14.3× |
| Gas combined cycle, life cycle (UNECE) | 458 | 1,073,328 | 6.5× |

On Canada Energy Regulator (n.d.) data for 2022 (35 g/kWh), the NSW figure is 20.6× the Ontario one (1,503,794 / 72,848), against 9.1× on the 2024 average.

*Table B17. Cumulative CO₂e avoided by one unit, by site, start year and grid trajectory (Figure F6 data).*
*Source: `results/displacement.md` §3.*

| Site | Start | Grid case | Year-1 EF (g/kWh) | To 2035 | To 2050 | Whole life |
|---|---|---|---:|---:|---:|---:|
| Darlington Unit 1 | 2030 | ON-avg-traj | 52 | 544 kt | 1.01 Mt | 2.01 Mt |
| Darlington Unit 1 | 2030 | ON-avg-flat | 74 | 988 kt | 3.46 Mt | 9.88 Mt |
| Darlington Unit 1 | 2030 | ON-marginal-declining | 267 | 3.29 Mt | 6.80 Mt | 7.80 Mt |
| Darlington Unit 1 | 2030 | ON-marginal-flat (upper bound) | 343 | 4.81 Mt | 16.83 Mt | 48.08 Mt |
| Liddell | 2035 | NEM-T0 frozen (upper bound) | 640 | 1.50 Mt | 24.06 Mt | 90.23 Mt |
| Liddell | 2035 | NEM-T1 Step Change proxy | 171 | 394 kt | 1.64 Mt | 4.33 Mt |
| Liddell | 2035 | NEM-T2 slow | 396 | 927 kt | 7.90 Mt | 10.59 Mt |
| Liddell | 2040 | NEM-T0 frozen (upper bound) | 640 | 0 | 16.54 Mt | 90.23 Mt |
| Liddell | 2040 | NEM-T1 Step Change proxy | 30 | 0 | 671 kt | 3.66 Mt |
| Liddell | 2040 | NEM-T2 slow | 274 | 0 | 3.85 Mt | 6.84 Mt |
| Liddell | 2045 | NEM-T0 frozen (upper bound) | 640 | 0 | 9.02 Mt | 90.23 Mt |
| Liddell | 2045 | NEM-T1 Step Change proxy | 30 | 0 | 366 kt | 3.66 Mt |
| Liddell | 2045 | NEM-T2 slow | 152 | 0 | 1.23 Mt | 4.53 Mt |
| Liddell | 2040 | UB-Bayswater flat (upper bound) | 990 | 0 | 25.65 Mt | 139.90 Mt |
| Liddell | 2040 | UB-coal-LCA flat (upper bound) | 1,000 | 0 | 25.91 Mt | 141.32 Mt |

*Table B18. All four Darlington units (Unit 1 from 2030; Units 2–4 from 2035).*
*Source: `results/displacement.md` §4.*

| Grid case | To 2035 | To 2050 | Whole life |
|---|---:|---:|---:|
| ON-avg-traj | 751 kt | 2.63 Mt | 7.00 Mt |
| ON-avg-flat | 1.48 Mt | 11.36 Mt | 39.51 Mt |
| ON-marginal-declining | 4.71 Mt | 18.77 Mt | 23.14 Mt |
| ON-marginal-flat (upper bound) | 7.21 Mt | 55.29 Mt | 192.32 Mt |

*Table B19. One-at-a-time sensitivity, Liddell central case (start 2040, NEM-T1). Central: 671 kt to 2050; 3.66 Mt over the whole life.*
*Source: `results/displacement.md` §5.*

| Parameter | Range | To 2050 (low → high input) | Whole life (low → high input) |
|---|---|---|---|
| Capacity factor | 0.80–0.95 | 597 → 709 kt | 3.25 → 3.86 Mt |
| Net output | 290–300 MWe (315 MWe, as in an OPG filing, adds about 5%, proportionally) | 649 → 671 kt | 3.54 → 3.66 Mt |
| SMR life cycle (our 95th → 5th percentile) | 5.8–3.0 g/kWh | 630 → 702 kt | 3.43 → 3.83 Mt |
| SMR life cycle, UNECE midpoint instead of ours | 5.75 vs 4.2 g/kWh | 631 → 671 kt | 3.44 → 3.66 Mt |
| SMR life cycle, stress (IPCC AR5 upper value) | 110–12 g/kWh | −2.08 Mt → 468 kt | −11.35 → 2.55 Mt |
| NEM floor after coal exit | 0–80 g/kWh | −109 kt → 1.97 Mt | −596 kt → 10.76 Mt |
| Coal exit year (T1) | 2035–2045 | 671 kt → 1.75 Mt | 3.66 → 4.74 Mt |
| Design life | 40–80 years | 671 → 671 kt | 2.44 → 4.88 Mt |
| Start year | 2035–2045 | 1.64 Mt → 366 kt | 4.33 → 3.66 Mt |
| Grid trajectory | T1 → T0 (frozen) | 671 kt → 16.54 Mt | 3.66 → 90.23 Mt |

Reading:
- **Order-of-magnitude drivers.** The grid trajectory, the start year and the post-coal floor each move the result by an order of magnitude. Under T1 the SMR spends its whole life displacing the residual mix, so the floor is in effect the displaced intensity.
- **Minor drivers.** Capacity factor, net output and our life-cycle interval move it by a few per cent.
- **When the SMR's own value matters.** Only in the 110 g/kWh stress case, or on a near-zero floor, where the result turns negative.

#### B4.3 Limitations
1. **Boundary mismatch.** The grid factors (NGA scope 2, TAF, CER) count combustion at the power station only, while the SMR value is life cycle, so displacement is slightly understated. The UNECE coal row gives the boundary-consistent upper bound.
2. **Average vs marginal.** A new baseload unit displaces what is on the margin when it runs. In Ontario that is mostly gas, so the marginal factor is the better short-run estimate. Over a 60-year life the margin decarbonises, which makes the flat-marginal case an upper bound.
3. **Counterfactual.** In both grids the real alternative is other new supply, not today's grid forever (B6).
4. **Liddell** was approved to close by April 2023 (Australian Energy Regulator, 2021) and has since closed. An SMR on the site displaces the NEM mix, so Bayswater is an upper bound only.
5. **Assumptions.** Net output, capacity factor, design life and start years are assumed; Table B19 and Table B17 test them.

---

### B5. Value of schedule: the CO₂e and dollar cost of delay, and C1's break-even

**Result.** On Ontario's average factor, C1's per-unit saving (2,200 t; 1,100–3,300 at 20–60% eligible) is cancelled by **11.6–18.5 days** of delay to that unit (gross–net). On the marginal factor it is cancelled by **1.7–1.8 days**. Even all of Units 2–4's saving (6,600 t) is cancelled by 35–55 days (average) or 5.1–5.4 days (marginal) of delay to a single unit. In money, a one-month slip of Units 2–4 costs **29–175 times** C1's carbon value. The saving is 50,000 m³ of concrete per unit (BWRX-300 Ostrołęka sp. z o.o., 2023) × the eligible share × 0.110 t CO₂e/m³ (OPC 380 less LC³ 270 kg CO₂e/m³; Pillai et al., 2019). Script: `python3 -I 03_LCA_Calculations/scripts/schedule_value.py`, with output in `results/schedule_value.md`; `--c1-case old_1734` reproduces the cross-check. The carrying-cost and deferred-output inputs are read from `parameters_run5.yaml`.

#### B5.1 Method

1. Output of one unit: monthly M = E / 12 = 197,100,000 kWh; daily D = E / 365 = 6,480,000 kWh.
2. **Gross loss** per month of delay = M × (EF_grid(start) − EF_SMR) / 10⁶ t. This is the displacement that does not happen while the plant is late, and it matches carbon budgets to 2035 or 2050.
3. **Net loss** per month = M × (EF_grid(start) − EF_grid(start + life)) / 10⁶ t. A late plant still runs its full life, so the lost month returns at the end of life, on a cleaner grid. On a flat grid this gives zero by construction, which is an artefact of assuming the grid never changes.
4. **Break-even delay** for a saving S (t CO₂e) = S / (loss per day), on both bases.

**Worked example (one of Units 2–4, start 2035, ON-avg-traj).**
1. Grid factor in 2035: EF(2035) = 73.8 − (73.8 − 15) × 11/16 = 33.4 g/kWh.
2. Gross loss: 6,480,000 × (33.4 − 4.2) / 10⁶ = **189 t a day**, so the break-even is 2,200 / 189 = **11.6 days**.
3. Net loss: 6,480,000 × (33.4 − 15) / 10⁶ = **119 t a day**, so the break-even is 2,200 / 119 = **18.5 days**.

**Marginal case.** EF(2035) = 343 − (343 − 15) × 11/26 = 204.2 g/kWh. The gross loss is 6,480,000 × 200.0 / 10⁶ = 1,296 t a day, so the break-even is 2,200 / 1,296 = **1.7 days**.

#### B5.2 CO₂e lost per month of delay

*Table B20. CO₂e lost per month of delay, one unit.*
*Source: `results/schedule_value.md` §2. "None" = flat grid, so the month is recovered at the end of life.*

| Site, start year | Grid case | EF at start (g/kWh) | EF at end of life | Gross t/month | Net t/month | Days to cancel 1 kt (gross / net) |
|---|---|---:|---:|---:|---:|---|
| Darlington Unit 1, 2030 | ON-avg-traj | 52 | 15 | 9,372 | 7,243 | 3.2 / 4.2 |
| Darlington Unit 1, 2030 | ON-avg-flat | 74 | 74 | 13,718 | 0 | 2.2 / none |
| Darlington Unit 1, 2030 | ON-marginal-declining | 267 | 15 | 51,859 | 49,730 | 0.6 / 0.6 |
| Darlington Unit 1, 2030 | ON-marginal-flat | 343 | 343 | 66,777 | 0 | 0.5 / none |
| Darlington Units 2–4 (each), 2035 | ON-avg-traj | 33 | 15 | 5,750 | 3,622 | 5.3 / 8.4 |
| Darlington Units 2–4 (each), 2035 | ON-marginal-declining | 204 | 15 | 39,426 | 37,297 | 0.8 / 0.8 |
| Darlington Units 2–4 (each), 2035 | ON-marginal-flat | 343 | 343 | 66,777 | 0 | 0.5 / none |
| Liddell, 2035 | NEM-T0 frozen | 640 | 640 | 125,316 | 0 | 0.2 / none |
| Liddell, 2035 | NEM-T1 Step Change proxy | 171 | 30 | 32,831 | 27,746 | 0.9 / 1.1 |
| Liddell, 2035 | NEM-T2 slow | 396 | 30 | 77,224 | 72,139 | 0.4 / 0.4 |
| Liddell, 2040 | NEM-T0 frozen | 640 | 640 | 125,316 | 0 | 0.2 / none |
| Liddell, 2040 | NEM-T1 Step Change proxy | 30 | 30 | 5,085 | 0 | 6.0 / none |
| Liddell, 2040 | NEM-T2 slow | 274 | 30 | 53,178 | 48,092 | 0.6 / 0.6 |

A one-month slip of all three of Units 2–4 loses:
- 17,251 t gross / 10,865 t net (ON-avg-traj);
- 118,278 / 111,892 t (ON-marginal-declining);
- 200,332 / 0 t (ON-marginal-flat).

**Break-even sensitivity** (Units 2–4, ON-marginal-declining; central 1,226 t a day net, 0.8 days per kt):
- capacity factor 0.80 or 0.95: 0.9 or 0.8 days per kt;
- marginal factor 472 g/kWh (gas generation): 0.6 days per kt;
- gas off the margin by 2040: 1.5 days per kt; by 2060: 0.7 days per kt (`results/schedule_value.md` §5).

#### B5.3 Break-even delay for C1

*Table B21. Days of delay that cancel C1's LC³ saving (Units 2–4, start 2035).*
*Source: `results/schedule_value.md` §6; `results/c1_deck_case.md`. Saving 2,200 t per unit and 6,600 t for Units 2–4 at 40% eligible (BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019). Brackets give the 20% and 60% eligibility cases (1,100 and 3,300 t per unit), not a Monte Carlo interval.*

| Grid case (factor type) | Gross t/day per unit | Net t/day per unit | (a) Per unit, gross days | (a) Per unit, net days | (b) Programme saving, one unit late: gross days | (b) Net days |
|---|---:|---:|---|---|---|---|
| ON-avg-traj (average, declining to 2040) | 189 | 119 | 11.6 (5.8–17.5) | 18.5 (9.2–27.7) | 34.9 (17.5–52.4) | 55.4 (27.7–83.1) |
| ON-avg-flat (average, held at 2024) | 451 | 0 | 4.9 (2.4–7.3) | none (flat grid) | 14.6 (7.3–22.0) | none (flat grid) |
| ON-marginal-declining (gas leaves the margin by 2050) | 1,296 | 1,226 | 1.7 (0.8–2.5) | 1.8 (0.9–2.7) | 5.1 (2.5–7.6) | 5.4 (2.7–8.1) |
| ON-marginal-flat (held at 2024) | 2,195 | 0 | 1.0 (0.5–1.5) | none (flat grid) | 3.0 (1.5–4.5) | none (flat grid) |

The two cases:
- **(a)** compares one unit's saving with a delay to that unit. All three units' saving against a three-unit slip gives the same answer, because both scale by 3.
- **(b)** compares all of Units 2–4's saving with a delay to only one unit, for example when the first LC³ pour holds one unit's critical path.

**Cross-check (earlier geometric model, 20,700 m³ per unit).** Its saving of 1,734 t per unit (5,201 t for Units 2–4; Monte Carlo 90% interval 1,387–2,153 t) gives break-evens of 9.2–14.6 days on the average factor and 1.3–1.4 days on the marginal factor. The deck case lengthens them by about 27% (2,200 / 1,734).

#### B5.4 C1's carbon value against one month's delay

*Table B22. C1's carbon value (Units 2–4, 6,600 t) against the value of the CO₂e lost in a one-month slip of all three units.*
*Source: `results/schedule_value.md` §7. Carbon prices: federal headline industrial trajectory (Environment and Climate Change Canada, 2026); the superseded 2021 path is shown for comparison only. Brackets: 20–60% eligibility.*

| Carbon price (C$/t) | Basis | C1 carbon value, Units 2–4 (C$ m) | CO₂e lost in a one-month slip, average factor (C$ m, gross / net) | Same, marginal factor (C$ m, gross / net) |
|---:|---|---|---|---|
| **95** | **2026, current path (used)** | **0.63 (0.31–0.94)** | 1.64 / 1.03 | 11.24 / 10.63 |
| 110 | 2026, superseded path | 0.73 (0.36–1.09) | 1.90 / 1.20 | 13.01 / 12.31 |
| **115** | **2030, current path (used)** | **0.76 (0.38–1.14)** | 1.98 / 1.25 | 13.60 / 12.87 |
| 170 | 2030, superseded path | 1.12 (0.56–1.68) | 2.93 / 1.85 | 20.11 / 19.02 |

Working: carbon value = saving × price. For example, 6,600 t × C$95/t = C$0.63 m, and 6,600 × 115 = C$0.76 m. C1's concrete would be placed in about 2029–2033, so the 2030 price is the relevant one; 2026 is today's price.

**Direct cost of a one-month slip of Units 2–4** (inputs from `parameters_run5.yaml`; assumptions where stated):
- **Deferred output:** 3 × 300 MW × 8,760 h × 0.90 / 12 = 591,300 MWh × C$149/MWh (OPG's reported LCOE; Ontario Power Generation, 2026b) = **C$88 m**. The output is deferred, not lost, so this is a cash-flow cost to OPG and ratepayers, not a social loss of that size.
- **Carrying cost:** C$13.2 bn (Units 2–4: C$20.9 bn less C$7.7 bn for Unit 1 and common infrastructure) × r / 12. At r = 3, 5, 7 and 10%, that is **C$33, 55, 77 and 110 m**. It is an upper bound, because it assumes all the capital is already spent.

**How the 29–175× in §7 is derived (current carbon-price path):**
- **Low end:** the lowest monthly cost (C$33.0 m) over the largest carbon value on the current path (9,900 t × C$115/t = C$1.139 m) = 29.0×.
- **High end:** the highest cost (C$110.0 m) over the central value at C$95/t (C$0.627 m) = 175.4×.
- **Including the superseded C$170/t path,** the low end is C$33 m / 1.68 = 20×. The earlier 1,734 t model gave 30–223× (44–223× on the current path).
- **In carbon alone,** the slip loses 10,865–118,278 t against C1's 6,600 t, which is 1.6–17.9 times the saving (earlier model: 2.1–22.7×).

One day of delay costs C$1.8–2.9 m (`results/initiative_cost.md` §5), against C1's total carbon value of C$0.63–0.76 m (C$1.14 m at 60% eligibility and C$115/t).

#### B5.5 Year-scale delays

*Table B23. CO₂e avoided to 2050 lost per year of delay, one unit.*
*Source: `results/schedule_value.md` §4.*

| Site | Grid case | Start A | Start B | Avoided to 2050 (A) | Avoided to 2050 (B) | Lost | Lost per year of delay |
|---|---|---:|---:|---:|---:|---:|---:|
| Liddell | NEM-T0 frozen | 2035 | 2040 | 24.06 Mt | 16.54 Mt | 7.52 Mt | 1.50 Mt |
| Liddell | NEM-T1 Step Change proxy | 2035 | 2040 | 1.64 Mt | 0.67 Mt | 0.97 Mt | 0.19 Mt |
| Liddell | NEM-T2 slow | 2035 | 2040 | 7.90 Mt | 3.85 Mt | 4.06 Mt | 0.81 Mt |
| Liddell | NEM-T2 slow | 2040 | 2045 | 3.85 Mt | 1.23 Mt | 2.61 Mt | 0.52 Mt |
| Darlington Unit 1 | ON-avg-traj | 2030 | 2032 | 1.01 Mt | 0.80 Mt | 0.22 Mt | 0.11 Mt |
| Darlington Unit 1 | ON-marginal-declining | 2030 | 2032 | 6.80 Mt | 5.59 Mt | 1.21 Mt | 0.61 Mt |

#### B5.6 Limitations
1. Average factors understate what a late baseload unit would have displaced in Ontario, where gas is on the margin.
2. The net basis assumes the plant's life is fixed in years, not extended.
3. The carbon value is realised only if someone prices it. Construction-material emissions appear to fall outside Ontario's Emissions Performance Standards (our inference).
4. The carrying cost is an upper bound for an early slip.
5. The eligible share (20–60%) is an assumption; the saving per m³ (0.110 t) is fixed, so volume and saving move together.

---

### B6. Same money: Darlington's budget spent on firmed renewables

**Result.** On GenCost 2023-24's 2030 costs, the same annual spend as one SMR unit (A$0.72 bn a year) buys **2.9×** the energy from firmed renewables (6.8 TWh a year against 2.37). For a Liddell SMR from 2040 on the slow trajectory, those renewables avoid **10.9×** more CO₂e to 2050 (5.7× on the GenCost 2030 reading alone, with renewables at A$153). Across all Liddell cases tested the ratio is 4.9–26.0× (4.9× is the lowest, with the A$198 SMR lead and A$153 renewables), so renewables avoid more CO₂e by 2050 in every Liddell case tested. **On Ontario's average grid the SMR wins, on two assumptions** (the 30 g/kWh renewables life-cycle value and the IESO 2040 grid; −0.4×, Table B27, row 5): once that grid is cleaner than the renewables' assumed 30 g/kWh life-cycle value, extra renewables add emissions against it. On Ontario's marginal grid renewables again lead (2.8×). On the alternative reading (SMR A$514/MWh), the ratios are 5.0× and 19.1× (9.3–45.8× across cases). Script: `python3 -I 03_LCA_Calculations/scripts/same_money.py`, with output in `results/same_money.md`.

**Basis of the tables.** The script runs on the 2030 reading: SMR A$306/MWh (range 230–382) and firmed renewables A$107/MWh (89–125), from a report of GenCost 2023-24 (Graham, Hayward and Foster, 2024, as reported) that gives A$387–641 as the SMR's **2023** value and A$230–382 as its **2030** value. The A$514 (387–641) / A$102 reading is kept as the alternative, in the sensitivity rows of Table B28 only. If the GenCost table reads otherwise, change `smr_lcoe_aud` and `vre_firmed_lcoe_aud` in `parameters_run1.yaml` and re-run; every table here regenerates.

#### B6.1 Inputs and method

*Table B24. Cost inputs and the two GenCost readings.*
*Source: `parameters_run1.yaml`; `results/lcoe.md` §5; references as named.*

| Input | Central (used in §7) | Alternative reading (sensitivity only) | Source |
|---|---|---|---|
| SMR LCOE | A$306/MWh (230–382), 2030 | A$514 (387–641), the 2023 value | Graham, Hayward and Foster (2024), as reported |
| Firmed renewables LCOE | A$107/MWh (89–125), solar and wind with integration costs, 2030; 153 = high case, assumption | A$102 | Graham, Hayward and Foster (2024) |
| Low SMR lead (sensitivity) | A$198/MWh | — | Kim and Macfarlane (2026) |
| Darlington budget | C$20.9 bn for four units; Unit 1 plus common infrastructure C$7.7 bn | — | Government of Ontario (2025) |
| Exchange rate | A$1.119 per C$1 (1.10–1.13) | — | Reserve Bank of Australia (2025) |
| Discount rate; annuity | 7% real (3–10%); 30 years (30–60) | — | Assumption |
| First year of renewables output | 2028 (2027–2030) | — | Assumption |
| Renewables life cycle | 30 g/kWh (8–83) | — | Assumption (range: UNECE PV, United Nations Economic Commission for Europe, 2021) |

**Method A: what the Darlington capital would buy.**
1. Capital recovery factor: CRF(r, n) = r(1 + r)ⁿ / ((1 + r)ⁿ − 1). CRF(7%, 30) = 0.07 × 7.612 / 6.612 = 0.0806.
2. Annual capital charge = budget (A$) × CRF.
3. Capital-only LCOE = charge / annual output.
4. Firmed renewables bought with that charge = charge / renewables LCOE.

Worked example (one unit, simple share):
1. Budget: C$5.225 bn × 1.119 = A$5.85 bn.
2. Annual charge: 5.85 bn × 0.0806 = A$471 m a year.
3. Capital-only LCOE: 471 m / 2,365,200 MWh = **A$199/MWh**.
4. Renewables bought: 471 m / A$107 = 4.40 TWh, which is **1.9×** the SMR's 2.37 TWh.

The result is a lower bound on the renewables' advantage, because it ignores the SMR's operating and fuel costs.

**Method B: LCOE ratio and CO₂e per dollar.**
1. Energy ratio = SMR LCOE / renewables LCOE: 306 / 107 = **2.9×**.
2. CO₂e per A$1 m = (10⁶ / LCOE) MWh × (EF_grid − EF_technology) kg/MWh / 1,000. Example (SMR, NSW 640 g/kWh, A$306): 3,268 MWh × 635.8 / 1,000 = 2,078 t.
3. Cumulative comparison: the annual spend = SMR output × SMR LCOE, and the renewables bought with it = spend / renewables LCOE, from 2028. Each technology's avoided CO₂e is summed on the same trajectory (B4.1), net of its own life-cycle intensity (4.2 or 30 g/kWh).

#### B6.2 Results

*Table B25. Method A: what Darlington's capital would buy (7%, 30-year annuity).*
*Source: `results/same_money.md` §2.*

| Budget case | Annual capital charge (A$ m) | SMR capital-only LCOE (A$/MWh) | SMR output (TWh a year) | Firmed renewables bought (TWh a year) | Renewables / SMR energy |
|---|---:|---:|---:|---:|---:|
| Four units, C$20.9 bn | 1,885 | 199 | 9.46 | 17.61 | 1.9× |
| One unit, simple share | 471 | 199 | 2.37 | 4.40 | 1.9× |
| Unit 1 plus common infrastructure, C$7.7 bn | 694 | 294 | 2.37 | 6.49 | 2.7× |

Capital-only LCOE for one unit across discount rates (30-year / 60-year annuity): 3%, A$126 / 89; 7%, A$199 / 176; 10%, A$262 / 248 per MWh (`results/same_money.md` §2).

*Table B26. Method B (SMR A$306, renewables A$107 per MWh): CO₂e avoided per dollar, Liddell/NEM.*
*Source: `results/same_money.md` §3.*

| Displaced grid intensity (g/kWh) | Case | SMR t CO₂e per A$1 m | Renewables t CO₂e per A$1 m | SMR A$/t (gross) | Renewables A$/t (gross) |
|---:|---|---:|---:|---:|---:|
| 640 | NSW 2025 average | 2,078 | 5,701 | 481 | 175 |
| 274 | NEM-T2 in 2040 | 882 | 2,280 | 1,134 | 439 |
| 80 | Post-coal mix + 50 (illustrative) | 248 | 467 | 4,037 | 2,140 |

*Table B27. Cumulative CO₂e avoided for the same annual spend as one SMR unit (A$0.72 bn a year buys 6.8 TWh a year of firmed renewables from 2028, against the SMR's 2.37 TWh).*
*Source: `results/same_money.md` §4. The alternative reading (A$514 / A$102; A$1.22 bn buys 11.9 TWh) gives Liddell ratios of 10.1×, 45.8×, 19.1× and 9.3× for the first four rows (`same_money.md` §4; the NEM-T2 slow rows are in Table B28).*

| Site | Grid case | SMR start | SMR to 2035 | SMR to 2050 | Renewables to 2035 | Renewables to 2050 | Renewables / SMR to 2050 |
|---|---|---:|---:|---:|---:|---:|---:|
| Liddell | NEM-T0 frozen | 2040 | 0 | 16.54 Mt | 33.01 Mt | 94.90 Mt | 5.7× |
| Liddell | NEM-T1 Step Change proxy | 2040 | 0 | 0.67 Mt | 16.50 Mt | 17.46 Mt | 26.0× |
| Liddell | NEM-T2 slow | 2040 | 0 | 3.85 Mt | 24.43 Mt | 41.76 Mt | 10.9× |
| Liddell | NEM-T2 slow | 2035 | 0.93 Mt | 7.90 Mt | 24.43 Mt | 41.76 Mt | 5.3× |
| Darlington (indicative, GenCost costs) | ON-avg-traj | 2030 | 0.54 Mt | 1.01 Mt | 0.88 Mt | −0.39 Mt | −0.4× |
| Darlington (indicative, GenCost costs) | ON-marginal-declining | 2030 | 3.29 Mt | 6.80 Mt | 11.82 Mt | 19.26 Mt | 2.8× |

The negative Ontario-average row arises because, once Ontario's average falls below the renewables' assumed 30 g/kWh life-cycle value, extra renewables add emissions against that average and the SMR's lower life-cycle value wins. This is a real property of a near-clean grid. But it rests on two assumptions (the renewables' life-cycle value and IESO's 2040 figure) and on the average rather than the marginal factor.

*Table B28. Sensitivity of the same-money result (Liddell, NEM-T2 slow, SMR from 2040). Figure F7 data.*
*Source: `results/same_money.md` §5. Bold row is the central case §7 uses; the last six rows are the alternative reading (SMR A$514).*

| Case (SMR / renewables LCOE, A$/MWh) | Energy ratio | Renewables / SMR CO₂e to 2050 |
|---|---:|---:|
| **Central: GenCost 2023-24, 2030 midpoints (306 / 107)** | **2.9×** | **10.9×** |
| SMR LCOE 2030 low (230 / 107) | 2.1× | 8.2× |
| SMR LCOE 2030 high (382 / 107) | 3.6× | 13.6× |
| Renewables LCOE 2030 low (306 / 89) | 3.4× | 13.1× |
| Renewables LCOE 2030 high (306 / 125) | 2.4× | 9.3× |
| Renewables high, assumption (306 / 153) | 2.0× | 7.6× |
| Worst case for renewables on the 2030 reading (230 / 153) | 1.5× | 5.7× |
| Low SMR lead (198 / 107) | 1.9× | 7.0× |
| Lowest SMR lead, worst case tested (198 / 153) | 1.3× | 4.9× |
| SMR starts 2035 (306 / 107) | 2.9× | 5.3× |
| Renewables start 2030 (306 / 107) | 2.9× | 9.0× |
| Renewables life cycle 83 g/kWh (306 / 107) | 2.9× | 8.7× |
| SMR life cycle 5.8 g/kWh, our 95th percentile (306 / 107) | 2.9× | 11.0× |
| Alternative reading, central (514 / 102) | 5.0× | 19.1× |
| Alternative reading, SMR low (387 / 102) | 3.8× | 14.4× |
| Alternative reading, SMR high (641 / 102) | 6.3× | 23.9× |
| Alternative reading, renewables low (514 / 91) | 5.6× | 21.4× |
| Alternative reading, renewables high, assumption (514 / 153) | 3.4× | 12.8× |
| Alternative reading, SMR starts 2035 | 5.0× | 9.3× |

#### B6.3 Capital cost alone, and the check against our own LCOE and OPG's figure

**Capital cost alone (moved from §7.3).** Darlington's C$20.9 bn (Ontario Power Generation, 2025a) is about A$23.4 bn (Reserve Bank of Australia, 2025). At 7% over 30 years that capital alone costs A$199/MWh. That is already enough to buy 1.9–2.7× the energy from renewables at about A$107/MWh (Graham, Hayward and Foster, 2024; Table B25).

Our Darlington LCOE (`results/lcoe.md`; case B, 60 years, vendor operating costs, CF 0.90) is C$112/151/198/280 per MWh at 3/5/7/10% real (A$125/169/221/313).
- **Against GenCost:** A$221 at 7% sits just below GenCost 2023-24's 2030 SMR range (A$230–382). Two reasons it should sit low: Darlington is a four-unit site with shared infrastructure, whereas GenCost prices a generic single Australian SMR; and GenCost 2025-26 reports revising Darlington's capital downwards for interest during construction (Graham and Hayward, 2026, as reported). At 10% (A$313) our figure falls in the upper half of GenCost's range. GenCost 2024-25 gives an SMR value of up to A$487 (Graham, Hayward and Foster, 2025; `results/lcoe.md` §5), so A$221 is below the GenCost ranges we found. GenCost 2025-26 still ranks SMRs as the highest-cost option (Graham and Hayward, 2026), and its SMR range was not retrieved.
- **Against OPG:** OPG's reported four-unit average of C$149/MWh (Ontario Power Generation, 2026b) is reproduced at a real discount rate of 4.9%. That rate is consistent with a ratepayer-backed Crown utility, not with merchant finance.
- **Cost ratio:** on our 7% value against GenCost 2024-25's firmed-renewables lead, the SMR/renewables cost ratio is 221 / 101 = 2.2× (`results/lcoe.md` §5). On GenCost 2023-24's 2030 values it is about 2.9× (1.8–4.3×), or 5.0× on the alternative reading.
- **Overrun:** a NuScale-sized capital overrun (×1.75) at 7% gives C$317/MWh (§8.2), the largest single input, ahead of the discount rate.
- **Market value against revenue (NuScale, 2025):** US$5.3 bn public float against US$31.5 m revenue, 168× (NuScale Power Corporation, 2026). Equity prices future orders; it does not finance first plants.
- **Full working:** in `results/lcoe.md`.

#### B6.4 Limitations
1. Adding several TWh a year of firmed renewables would itself change the NEM trajectory, so the comparison holds only at the margin of the stated trajectory.
2. The LCOE of firmed renewables rises with their share, and GenCost's integration costs cover this only up to the shares it models.
3. Darlington's budget is in nominal Canadian dollars (2025 announcement), while GenCost is in real Australian dollars. Method A is therefore an order-of-magnitude cross-check, not a precise conversion.
4. Renewable assets last about 25–30 years (GenCost). No replacement falls before 2050, but a whole-life comparison would need one.
5. The Ontario rows use Australian costs and are indicative only. Ontario-specific costs were a stretch item in the plan and were not done.

---

### B7. Multi-criteria analysis (MCDA): status quo, SMR, SMR + C1 and firmed renewables

**Result.** Firmed renewables for the same money score highest under all four weight sets (80.1, 85.9, 63.7 and 89.3 of 100). The status quo is second, and SMR and SMR + C1 tie for third (29.7, 24.0, 43.6 and 20.4). C1 moves the SMR's score by under 0.005 point. **The ranking is a structured comparison, not a measurement:** the social, legal and renewables-supply scores and the weights are our judgement. The main-text summary is §9 (the §9 tables). Source: `scripts/mcda.py` (C1 case `new_2200`), `results/mcda.md` and `results/mcda_scores.csv`, which holds every raw score, normalised score, weight set and perturbation (593 rows).

#### B7.1 Options, criteria and inputs

The four options are the status quo (Liddell closed, NSW grid unchanged), one BWRX-300 at Liddell, the same plant with C1, and the same annual spend on firmed renewables. Lower is better for life-cycle CO₂e, cost, first-power year and HHI; higher is better for CO₂e avoided per dollar, social licence and legal feasibility.

*Table B29. Performance matrix (raw values) and the source of each score.*
*Source: `results/mcda.md` §2. SMR + C1 shown for the 2,200 t case.*

| Criterion | Status quo | SMR | SMR + C1 | Firmed renewables | Source (status) |
|---|---:|---:|---:|---:|---|
| Life-cycle CO₂e (g/kWh) | 640 | 4.2 | 4.1845 | 30 | SMR: team LCA median (§6). Renewables: 30 g/kWh assumption inside UNECE's PV range of 8–83. Status quo: NSW grid factor 2025 (NGA Factors) |
| CO₂e avoided to 2050 (Mt per A$1 bn/yr) | 0 | 5.31 | 5.31 | 57.69 | B6 frame (`same_money.py`); GenCost 2030 LCOEs; NEM trajectory T2, slow (assumption) |
| Cost, LCOE (A$/MWh) | 0 | 306.00 | 306.04 | 107 | GenCost 2023-24, 2030 midpoints: SMR 230–382, firmed renewables 89–125. C1 adds A$0.038/MWh (assumptions) |
| First full year of new supply | 2050 | 2040 | 2040 | 2028 | SMR: CSIRO's 2040 for nuclear (Graham, Hayward and Foster, 2024). Renewables: 2028 (assumption). Status quo: no new supply by 2050 (convention) |
| Supply concentration (HHI) | 0 | 3,009 | 3,009 | 6,400 | SMR: enrichment, B2. Renewables: lower bound from China's share, above 80% of every PV stage (International Energy Agency, 2022). Status quo: convention |
| Social licence (Table B39 total, 5–15) | 13 | 11 | 11 | 14 | §8.4 and Table B39 (our judgement) |
| Legal feasibility (Table B13 total, 4–12) | 12 | 8 | 8 | 12 | B3, best SMR route under equal weights (route C, 8); route A scores 6, which leaves this input unchanged (our judgement) |

**Conventions for the status quo (a do-nothing reference).** It takes the NSW grid factor as its "life cycle" (a boundary mismatch: scope 2 only, but it is last on this criterion whatever the boundary), avoids nothing, adds no cost or supply chain, has first supply in 2050, and scores 13 on social licence (nothing to consent to, but no benefit reaches the Upper Hunter) and 12 on legal feasibility. B7.4 tests the cost, supply and social conventions.

**Not scored.** Technology readiness level (TRL) is not scored. Schedule risk enters through the first-power year (tested at 2035 and 2045) and the C1 delay case.

#### B7.2 Method

1. **Model.** Linear additive (weighted-sum) MCDA, the standard compensatory model in the UK government manual (Dodgson et al., 2009).
2. **Normalisation.** Each criterion is min–max normalised across the four options: s = (x − worst) / (best − worst), so the best option scores 1 and the worst 0.
3. **Total.** T = 100 × Σ w_c s_c, with weights renormalised to sum to 1.
4. **CO₂e avoided per dollar.** The same annual spend buys 2,365,200 MWh/yr × A$306/MWh = A$0.724 bn/yr of SMR output, or A$0.724 bn / A$107 = 6.76 TWh/yr of firmed renewables from 2028. Avoided CO₂e to 2050 = Σ over years of MWh × (grid factor − option's life-cycle factor), with the grid falling linearly from 640 g/kWh in 2025 to 30 in 2050 (B6 frame). The SMR avoids 3.85 Mt and renewables 41.76 Mt, divided by A$0.724 bn/yr.
5. **C1 in the model.** Life-cycle reduction = saving / lifetime output. For 2,200 t: 2,200 × 10⁶ g / (2,365,200 MWh × 1,000 × 60 years = 1.419 × 10¹¹ kWh) = **0.0155 g/kWh** (0.37% of 4.2). For the earlier 1,734 t it is 0.0122 g/kWh (0.29%). C1's cost is a premium (base 0%) × C$229/m³ × 20,000 m³ plus qualification (base C$1.0 m), × 1.119 AUD/CAD, annualised at a capital recovery factor of 0.0806 (7%, 30 years) over 2,365,200 MWh: **+A$0.038/MWh**. The base case is schedule-neutral (the §8.6 condition).

**Worked example (equal weights, SMR).** Life cycle: (640 − 4.2) / (640 − 4.1845) = 0.99998. Avoided per dollar: 5.31 / 57.69 = 0.0921. Cost: (306.04 − 306.00) / 306.04 = 0.0001. Time: (2050 − 2040) / (2050 − 2028) = 0.4545. Supply: (6,400 − 3,009) / 6,400 = 0.5298. Social: (11 − 11) / (14 − 11) = 0. Legal: (8 − 8) / (12 − 8) = 0. The sum is 2.0766, and T = 100 × 2.0766 / 7 = **29.7**.

*Table B30. Normalised scores (1 = best of the four options).*
*Source: `results/mcda.md` §3.*

| Criterion | Status quo | SMR | SMR + C1 | Firmed renewables |
|---|---:|---:|---:|---:|
| Life cycle | 0.0000 | 1.0000 | 1.0000 | 0.9594 |
| Avoided per dollar | 0.0000 | 0.0921 | 0.0921 | 1.0000 |
| Cost | 1.0000 | 0.0001 | 0.0000 | 0.6504 |
| Time | 0.0000 | 0.4545 | 0.4545 | 1.0000 |
| Supply | 1.0000 | 0.5298 | 0.5298 | 0.0000 |
| Social licence | 0.6667 | 0.0000 | 0.0000 | 1.0000 |
| Legal feasibility | 1.0000 | 0.0000 | 0.0000 | 1.0000 |

#### B7.3 Weights and results

The weights are our reading of each group's stated priorities (`parameters_run9.yaml`), not elicited from them.

*Table B31. Weight sets and total scores (0–100).*
*Source: `results/mcda.md` §4. Rationale sources: Bowen's statements; the Liberal Party 2026 energy plan; §8.4.*

| Weight set | Life cycle | Avoided per $ | Cost | Time | Supply | Social | Legal | Rationale |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| W0 equal | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | 0.143 | No view privileged |
| W1 climate and cost | 0.10 | 0.25 | 0.25 | 0.20 | 0.05 | 0.10 | 0.05 | Federal Government and AEMO lens: cost and speed of decarbonisation |
| W2 firm and sovereign | 0.25 | 0.05 | 0.15 | 0.05 | 0.30 | 0.15 | 0.05 | Coalition and advocate lens: zero-emission firm supply and security. The most SMR-favourable set we could justify, as a stress test |
| W3 host community | 0.10 | 0.10 | 0.15 | 0.15 | 0.05 | 0.30 | 0.15 | Upper Hunter community, Traditional Owners and unions: consent, legal certainty, early jobs |

| Weight set | Status quo | SMR | SMR + C1 | Firmed renewables | Ranking |
|---|---:|---:|---:|---:|---|
| W0 equal | 52.4 | 29.7 | 29.7 | 80.1 | Renewables > status quo > SMR ≈ SMR + C1 |
| W1 climate and cost | 41.7 | 24.0 | 24.0 | 85.9 | Same |
| W2 firm and sovereign | 60.0 | 43.6 | 43.6 | 63.7 | Same |
| W3 host community | 55.0 | 20.4 | 20.4 | 89.3 | Same |

#### B7.4 Rank reversal and input sensitivity

*Table B32. Each weight varied by ±50% (then renormalised): 14 tests per weight set.*
*Source: `results/mcda.md` §5.*

| Weight set | Tests | First place changes | Cases that change the order |
|---|---:|---:|---|
| W0 equal | 14 | 0 | None |
| W1 climate and cost | 14 | 0 | None |
| W2 firm and sovereign | 14 | 2 | Life cycle × 0.5 and supply × 1.5: both give status quo > renewables > SMR |
| W3 host community | 14 | 0 | None |

- **Random weights.** In 20,000 Dirichlet(1,…,1) draws (seed 20261021), first place goes to renewables in 85.4%, the status quo in 14.5%, SMR + C1 in 0.1% and SMR in 0.0%. An SMR option is above renewables in 1.1% of draws.
- **Threshold.** Putting one criterion's weight at w and sharing the rest equally, an SMR option first ranks first only when life cycle carries at least 0.936. For the other six criteria it never does.
- **SMR versus SMR + C1.** They never swap places in any of the 56 tests.

*Table B33. Input changes that alter first place or the order (base weights). All other changes leave "renewables > status quo > SMR" in all four sets.*
*Source: `results/mcda.md` §6 (17 input cases × 4 weight sets = 68 tests).*

| Change | Result |
|---|---|
| Worst case for renewables (SMR A$198, renewables A$153) | W2: status quo first; others unchanged |
| Status quo social licence at 14 (instead of 13) | W2: status quo first; others unchanged |
| Status quo supply = renewables' HHI (6,400) | W2: renewables > SMR > status quo; others unchanged |
| Fixed global scales (best and worst fixed in advance) | All four sets: renewables > SMR > status quo |

The unchanged cases include the alternative GenCost reading (SMR A$514, renewables A$102), first power in 2035 and 2045, renewables from 2030, grid paths NEM-T1 and T0 (frozen at 640 g/kWh), renewables at 83 g/kWh, enrichment HHI of 5,621, PV China share of 95% (HHI 9,025), status quo cost equal to renewables' LCOE, status quo social licence of 11, a C1 delay of 18.5 days, and a C1 premium of 20% with C$3 m qualification. Reading: renewables first is robust to every input tested. **The status quo above the SMR is not:** it comes from the four-option scale, where doing nothing scores full marks on cost, supply and legal feasibility.

#### B7.5 SMR versus SMR + C1 under each C1 case

*Table B34. Effect of C1 on the SMR's life cycle and score, by C1 case.*
*Source: `results/mcda.md` §7. The 1,100, 2,200 and 3,300 t cases (eligibility of 20/40/60%) are the deck case (BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019). The 1,734 t row is the earlier-model cross-check.*

| C1 case | Saving (t/unit) | Life cycle, SMR → SMR + C1 (g/kWh) | Change | Score gap, equal weights (points) | Score gap if qualification is free |
|---|---:|---|---|---:|---:|
| 1,100 t | 1,100 | 4.200 → 4.1922 | 0.0078 g/kWh (0.18%) | −0.0017 | +0.00024 |
| **2,200 t (central)** | 2,200 | 4.200 → 4.1845 | 0.0155 g/kWh (0.37%) | −0.0015 | +0.00049 |
| 3,300 t | 3,300 | 4.200 → 4.1767 | 0.0233 g/kWh (0.55%) | −0.0012 | +0.00073 |
| 1,734 t (earlier model, cross-check) | 1,734 | 4.200 → 4.1878 | 0.0122 g/kWh (0.29%) | −0.0016 | +0.00038 |

In every case the CO₂e avoided to 2050 rises only from 3.845 to 3.846 Mt, and the extra cost is A$0.038/MWh. The gap is slightly negative in the base case because the assumed C$1 m qualification cost outweighs a 0.016 g/kWh gain on a criterion whose range is 636 g/kWh; with free qualification it turns positive but stays below 0.001 point. **Delay case.** If C1 slips the unit by 18.5 days (the whole-life break-even of Table B21, used as an illustration), the CO₂e not avoided at Liddell during the delay is 32.3 kt, which is 15 times the 2,200 t saving. SMR + C1 then avoids less than the plain SMR, so the schedule-neutral condition decides the sign. The percentages are of the 4.2 g/kWh median.

#### B7.6 Limitations

1. Social licence, legal feasibility and the renewables supply score are our scored judgement (Table B39; Table B13; B7.1). The weights are our reading, not elicited. A stakeholder survey would replace them.
2. Local min–max scaling makes each score depend on which options are compared. The status quo's second place changes on fixed global scales (B7.4).
3. Renewables' supply HHI uses solar PV only; batteries, wind turbines and transmission are not assessed, and the IEA (2022) report was not opened in full.
4. TRL is not scored, and first-power years depend on CSIRO's 2040 and the Coalition's 2035 (as reported).
5. Renewables' 30 g/kWh and 2028 start are assumptions, and the GenCost reading is the one stated in B6. Adding several TWh of renewables would itself change the grid trajectory (B6.4).
6. The UK government manual (Dodgson et al., 2009) was not opened in full.

**Reproduce.** From the repository root: `python3 -I 03_LCA_Calculations/scripts/mcda.py --c1-case new_2200` (cases: `old_1734`, `new_1100`, `new_2200`, `new_3300`). Inputs are in `03_LCA_Calculations/parameters_run9.yaml`; outputs are `results/mcda.md` and `results/mcda_scores.csv`.

---

### B8. Social licence and stakeholder working (for §8.4 and §8.5)

**Result.** Safety data favour nuclear (0.03 deaths per TWh against 24.62 for coal), but the health benefit of one unit is large only against coal (58 deaths avoided a year, an upper bound) and small against gas (6.6). Weighted by power, the average stance is +1.07 at Darlington and −1.03 at Liddell. Consent-based siting routes beat top-down siting by 3–6 points under all five weightings, and not building an SMR at Liddell scores highest. **The stance scores and route scores are our judgement, not measurements.** Script: `python3 -I 03_LCA_Calculations/scripts/social_licence.py` (`parameters_run6.yaml`; output `results/social_licence.md`).

Sources for the §8.4 social-licence table (Darlington and Liddell): Neelam (2024); Griffith University Climate Action Beacon and Monash Climate Change Communication Research Hub (2025); Newspoll (2007); Ritchie (2020); Markandya and Wilkinson (2007); Canadian Nuclear Safety Commission (2025); Williams Treaties First Nations et al. (2026); Mississaugas of Scugog Island First Nation (2023); Curve Lake First Nation (2024); Municipality of Clarington (2024); Australian Electoral Commission (2019); *Barngarla* [2023] FCA 809; Nuclear Waste Management Organization (2024a; 2024b; 2024c; n.d.); Department of Industry, Science, Energy and Resources (2020); Power Workers' Union (2021); Conference Board of Canada (2021); Joint Standing Committee on Treaties (2024); Slovic (1987).

#### B8.1 Perceived and actual safety, and deaths avoided

1. Death rates per TWh (Ritchie, 2020; Markandya and Wilkinson, 2007): coal 24.62, brown coal 32.72, gas 2.82, wind 0.04, nuclear 0.03, solar 0.02. Coal is 24.62 / 0.03 = about 820 times nuclear (gas about 94 times).
2. Output of one unit: 300 MWe × 8,760 h × 0.9 = 2.365 TWh a year (2.102–2.497 at capacity factors of 0.80–0.95).
3. Deaths avoided a year = output × (death rate of the displaced source − nuclear's rate). Example (black coal): 2.365 × (24.62 − 0.03) = **58.2**.

*Table B36. Statistical deaths avoided a year by one unit, by displaced source.*
*Source: `results/social_licence.md` §2.*

| Displaced source | CF 0.80 | CF 0.90 (central) | CF 0.95 |
|---|---:|---:|---:|
| Black coal (Liddell; upper bound, because coal leaves the grid by 2038 in AEMO's central scenario) | 51.7 | **58.2** | 61.4 |
| Brown coal (stretch case) | 68.7 | 77.3 | 81.6 |
| Gas (Darlington, per unit; Ontario has no coal) | 5.9 | **6.6** | 7.0 |
| Gas, four units | 23.5 | 26.4 | 27.9 |
| Wind | 0.02 | 0.02 | 0.02 |
| Solar | −0.02 | −0.02 | −0.02 |

The unit's own output carries 0.07 statistical deaths a year at the nuclear rate (one per 14 years), a rate that includes Chernobyl and Fukushima. The fossil rates are for European plants with pollution controls, so they are conservative. Against wind or solar the difference lies within the uncertainty of the rates.

#### B8.2 Stakeholder power, interest and stance (Figure F8)

Each actor is scored for power (1–5), interest (1–5) and stance (−2 strongly against to +2 strongly for) from the evidence in §8.1–8.4 (evidence keys in `parameters_run6.yaml`). "High power" is a score of 4 or more. Quadrant: power ≥ 4 and interest ≥ 4, manage closely; power ≥ 4 only, keep satisfied; interest ≥ 4 only, keep informed; neither, monitor. **Power-weighted stance** = Σ(power × stance) / Σ(power).

*Table B37. Stakeholder scores, Darlington Units 2–4 with C1.*
*Source: our judgement from §8.1–8.4 evidence; `results/social_licence.md` §6.*

| Stakeholder | Power | Interest | Stance | Quadrant |
|---|---:|---:|---:|---|
| Ontario Government (shareholder) | 5 | 5 | +2 | Manage closely |
| OPG (licensee, owner) | 5 | 5 | +2 | Manage closely |
| CNSC (safety regulator) | 5 | 3 | 0 | Keep satisfied |
| Williams Treaties First Nations | 4 | 5 | +1 | Manage closely |
| Government of Canada (CIB, CGF, CILGC) | 4 | 4 | +2 | Manage closely |
| GE Vernova Hitachi (vendor) | 4 | 4 | +1 | Manage closely |
| Ontario Energy Board (rate regulator) | 4 | 3 | 0 | Keep satisfied |
| Clarington and Durham (host) | 3 | 5 | +2 | Keep informed |
| Unions | 3 | 4 | +2 | Keep informed |
| NGOs | 2 | 5 | −2 | Keep informed |
| Cement suppliers (no source found) | 2 | 3 | +1 | Monitor |
| Ratepayers | 2 | 3 | 0 | Monitor |

Working: Σ(power × stance) = 10 + 10 + 0 + 4 + 8 + 4 + 0 + 6 + 6 − 4 + 2 + 0 = 46; Σ(power) = 43; 46 / 43 = **+1.07**. Seven actors have high power and none is opposed.

*Table B38. Stakeholder scores, a hypothetical BWRX-300 at Liddell.*
*Source: as Table B37.*

| Stakeholder | Power | Interest | Stance | Quadrant |
|---|---:|---:|---:|---|
| Commonwealth Government (Labor) | 5 | 3 | −2 | Keep satisfied |
| NSW Government | 5 | 3 | −2 | Keep satisfied |
| AGL (site owner) | 4 | 4 | −2 | Manage closely |
| ARPANSA (regulator) | 4 | 2 | 0 | Keep satisfied |
| NGOs | 3 | 5 | −2 | Keep informed |
| Wonnarua people (no public position found; scored neutral by default) | 3 | 4 | 0 | Keep informed |
| Unions (ACTU, ETU) | 3 | 4 | −2 | Keep informed |
| Investors in NEM renewables | 3 | 3 | −1 | Monitor |
| Federal Coalition | 2 | 5 | +2 | Keep informed |
| Upper Hunter community | 2 | 5 | 0 | Keep informed |
| SMR vendors | 2 | 3 | +1 | Monitor |

Working: Σ(power × stance) = −10 − 10 − 8 + 0 − 6 + 0 − 6 − 3 + 4 + 0 + 2 = −37; Σ(power) = 36; −37 / 36 = **−1.03**. Four actors have high power and three are opposed. Scoring the Wonnarua people at −2 or +2 would move the Liddell result by −0.17 or +0.17 (3 × 2 / 36), which does not change its sign.

#### B8.3 Social-licence routes for an SMR at Liddell

Four routes are scored 1–3 (3 best) on legitimacy (chance of durable consent), legal risk (low risk scores high), speed, public cost (low cost scores high) and fairness. Each weighted column doubles one criterion.

*Table B39. Route scores by criterion and totals.*
*Source: our judgement (`parameters_run6.yaml`); totals by `social_licence.py`; route models from Newcastle Herald (2024b), NWMO (2024a; 2024c) and Williams Treaties First Nations et al. (2026).*

| Route | Legitimacy | Legal | Speed | Public cost | Fairness | Equal | Legitimacy ×2 | Speed ×2 | Fairness ×2 | Public cost ×2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1. Commonwealth-led siting | 1 | 1 | 2 | 2 | 1 | 7 | 8 | 9 | 8 | 9 |
| R2. Volunteer host plus willingness test (NWMO model) | 3 | 3 | 1 | 2 | 2 | 11 | 14 | 12 | 13 | 13 |
| R3. R2 plus First Nations equity and loan guarantee | 3 | 3 | 1 | 1 | 3 | 11 | 14 | 12 | 14 | 12 |
| R4. No SMR: firmed renewables | 3 | 3 | 3 | 3 | 2 | 14 | 17 | 17 | 16 | 17 |

Reading: R1 beats R3 only on speed (2 against 1) and public cost (2 against 1), and R2 only on speed (2 against 1). Even so, R2 and R3 lead R1 by 3 to 6 points under every weighting. R3 wins outright only when fairness is doubled. R4 (no SMR) scores highest under every weighting, so on social licence alone the Australian SMR case is weaker than the alternative (§9).

#### B8.4 Who finances the Darlington New Nuclear Project

*Table B40. Shares of the C$20.9 bn budget.*
*Source: `results/social_licence.md` §4, from Government of Ontario (2025), Canada Growth Fund and Building Ontario Fund (2025), Canada Infrastructure Bank (2022), Williams Treaties First Nations et al. (2026).*

| Financier | C$ bn | Share of C$20.9 bn |
|---|---:|---:|
| Canada Growth Fund equity (federal) | 2.00 | 9.6% |
| Building Ontario Fund equity (Ontario) | 1.00 | 4.8% |
| Canada Infrastructure Bank loan, phase 1 (federal) | 0.97 | 4.6% |
| Williams Treaties First Nations loan converting to equity | 0.70 | 3.3% |
| **Remainder: OPG's balance sheet, recovered through Ontario Energy Board rates** | **16.23** | **77.7%** |

The 78% is a subtraction (20.9 − 2.00 − 1.00 − 0.97 − 0.70 = 16.23), not a reported figure. Debt (CIB, WTFN) and equity (CGF, BOF) are added only to show scale; the CGF and BOF stakes of up to 15% and 7.5% are shares of the project partnership's equity, not of the budget. Budget per MW: C$20.9 bn / 1,200 MWe = C$17.4 m.

**Limits.** All scores are judgements from secondary summaries. Local min–max scaling and the MCDA use of these scores are in B7. Job and waste figures in the §8.4 social-licence table (Conference Board of Canada, 2021; NWMO, n.d.) are taken from those sources and are not recomputed here, except the Ignace hosting payment (C$170 m over 81 years, about C$2.1 m a year; the C$170 m in total is 0.65% of the C$26 bn lifecycle cost, nominal against 2020 dollars).

---





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

*Table C4b. Scenario savings and life-cycle shares on the Monte Carlo basis (the basis of Table T5 in §6.3 and Table A7b).*
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


## Appendix E. Search log

### E1. Method and access
The patent search covered three areas that bear on the initiative: (i) the BWRX-300's passive safety and civil design (isolation condenser, vertical shaft); (ii) steel-plate composite (DP-SC) modules; and (iii) limestone calcined clay cement (LC³). All searches were run on 25 October 2026.

Google Patents (patents.google.com) **could not be reached** from the research environment (DNS failure). Justia, Espacenet, Lens, PatentsView, USPTO Patent Public Search and Google Scholar also failed to connect. Google Patents result counts are therefore **not available**. Instead, each string was run through a general web search, which returns about 9–10 links per query. Patent records were identified from those links and their summaries. The "hits" column below counts the patent records found, not database hits. Assignees, dates and claims are as given in search summaries; the patent pages were not opened, so they are indicative only.

### E2. Search strings and results
| # | Area | Search string (web search) | Links | Patent records found |
|---|---|---|---|---|
| 1 | (i) | GE-Hitachi patent isolation condenser small modular boiling water reactor US patent | 10 | 2 (US 10,867,712 B2; US 12,308,130) |
| 2 | (i) | US10867712B2 isolation condenser systems … assignee GE-Hitachi inventors | 9 | 5 (one family: US, WO, CA, JP, PL) |
| 3 | (i) | US12308130 simplified nuclear reactor isolation condenser integrally isolatable connections assignee | 9 | 3 (US 12,308,130 B2; US 11,139,087; US 11,955,248) |
| 4 | (i) | GE-Hitachi Nuclear Energy patent "reactor building" below grade vertical shaft small modular reactor | 10 | 2 (US 2020/0208517 A1; US 11,842,821) |
| 5 | (i) | US20200208517 "Underground vertical shafts and nuclear reactors using the same" assignee | 9 | 1 family (EP 3906566), plus 2 older underground-reactor patents |
| 6 | (ii) | patent steel-plate composite modular wall nuclear "steel plate composite" diaphragm plate | 9 | **0** |
| 7 | (ii) | patent "steel-concrete composite" module nuclear plant construction Westinghouse OR GE-Hitachi | 9 | **0** |
| 8 | (ii) | patent steel plate concrete composite wall modules "diaphragm plates" flow holes nuclear GE Hitachi Purdue | 9 | **0** |
| 9 | (iii) | patent limestone calcined clay cement LC3 Scrivener EPFL patent WO | 10 | **0** |
| 10 | (iii) | patents.google.com "calcined clay" limestone cement composition patent kaolinite clinker replacement | 9 | 5 (US 8,906,155 B2; US 2014/0000491; KR 10-2843101 B1; US 2023/0312412 A1; WO 2022/043349 A1) |
| 11 | (iii) | US20230312412A1 limestone calcined clay cement construction composition assignee | 9 | 3 (US 11,939,273 B2; US 2023/0202926 A1; US 2023/0036470 A1) |
| 12 | (iii) | US 2023/0202926 A1 "increase of workability" binder … calcined clay limestone assignee | 9 | 3 (EP 3925941 A1; EP 4168371; US 2025/0187980 A1) |

**Result for (ii).** No DP-SC patent was found under GE-Hitachi or any other applicant. The design is documented in a licensing topical report (GEH, 2024, NEDO-33926), a joint CNSC–NRC review (2025), DOE test reports (Purdue Bowen Laboratory) and an SMiRT-28 paper. Whether GEH protects it by patent or as know-how is unknown. **Gap: search Google Patents for "diaphragm plate" with assignee GE-Hitachi Nuclear Energy Americas when the host is reachable.**

### E3. Patents kept
| # | Number | Title | Assignee | Year | Relevance to this report |
|---|---|---|---|---|---|
| P1 | US 10,867,712 B2 (family WO 2019/005465 A1, CA 3067552 A1, JP 7234150 B2) | Isolation condenser systems for nuclear reactor commercial electricity generation | GE-Hitachi Nuclear Energy Americas LLC | Filed 2017 | The passive decay-heat system behind the BWRX-300's 7-day no-power claim (§4.2) |
| P2 | US 12,308,130 B2 | Reactor condition controlled check valve permits coolant to flow from a reservoir to an isolation condenser chamber | Not confirmed (search summary only); inventors named as Hunt, Dahlgren and Marquino | n.d. | Passive make-up of the condenser pool: how cooling extends beyond 7 days |
| P3 | US 2020/0208517 A1 (EP 3906566) | Underground vertical shafts and nuclear reactors using the same | Not confirmed; inventors include Kirby and McDonald (GE-Hitachi staff) | 2020 | The below-grade shaft reactor building and the basemat poured at the bottom of the shaft (§4.2; C1's infill location) |
| P4 | US 8,906,155 B2 | Clinker substitute based on calcined clay | Outotec (as listed) | 2014 | Reported to cover calcined clays of lower kaolinite content (below 40%), which would widen the clay supply for LC³ (§5) |
| P5 | KR 10-2843101 B1 | Limestone calcined clay cement using low-temperature calcined clay (title as listed by ZKG) | Not confirmed | n.d. | Listed by ZKG as LC³ using low-temperature calcined clay; details not seen |
| P6 | US 11,939,273 B2 (US 2023/0312412 A1; WO 2022/043349 A1) | Limestone calcined clay cement (LC3) construction composition | Construction Research & Technology GmbH | Filed 2021 | Admixture-modified LC³ binder: an admixture supplier is patenting LC³ compositions (§10) |
| P7 | US 2023/0202926 A1 (EP 3925941 A1) | Method for the increase of workability of a binder composition comprising Portland cement, calcined clay, and limestone | Sika Technology AG | 2023 | Directly addresses the main RB.7 barrier: LC³ workability for self-consolidating DP-SC infill (§10) |

Seven patents are kept. Excluded: US 11,139,087 and US 11,955,248 (isolation condenser and feedwater control; assignee not seen), US 11,842,821 (title and date inconsistent between summaries), and US 2023/0036470 A1 and US 2025/0187980 A1 (not LC³-specific).

**What the patents show (R1.3).** The BWRX-300's distinctive systems (isolation condensers, shaft construction) sit in GEH's own patent families. LC³ itself, developed through EPFL's public research programme, appears in no core composition patent in these results. The patenting is around it: clay processing (Outotec) and **admixtures for workability** (Sika, BASF/CR&T). So for C1 the patent risk for the binder looks low on these searches (no freedom-to-operate search was done), and the commercial interest lies exactly where our RB.7 gap is (SCC flow). That supports C1's route: buy a commercial admixture system and qualify it, rather than develop a new binder (inference).

### E4. Literature searches (web-search substitute for Google Scholar)
| # | Topic | String | Kept |
|---|---|---|---|
| L1 | Radiation in concrete | Field Remec Le Pape 2015 radiation effects in concrete … Nuclear Engineering and Design | Field, Remec and Le Pape (2015) |
| L2 | Activated concrete | activated concrete decommissioning Eu-152 Co-60 biological shield … | Greifswald shield study (HZDR); a Belgian BR3 decommissioning study |
| L3 | Clearance and recycling | nuclear decommissioning concrete clearance recycling percentage … | Thierfeldt (2019) |
| L4 | LC³ chloride and SCC | limestone calcined clay cement self-compacting concrete heat of hydration chloride … | LC³ chloride study (2025); UniBw calcined-clay SCC |
| L5 | LC³ heat of hydration | LC3 concrete heat of hydration lower than OPC semi-adiabatic … | **None LC³-specific (gap)** |
| L6 | LC³ SCC rheology | self-compacting concrete limestone calcined clay cement superplasticizer demand rheology … | UniBw; IIT Madras (2020) |
| L7 | Steel residuals | copper tramp element accumulation steel scrap recycling EAF … | a 2025 review of copper in steel scrap |
| L8 | RPV embrittlement | reactor pressure vessel steel SA-508 copper phosphorus irradiation embrittlement … | CNSC (2023b); NRC RG 1.99 Rev. 2 |
| L9 | Steel route intensity | worldsteel CO2 intensity BF-BOF … EAF … | worldsteel (2025; 2026) |
| L10 | Waste forms | ANSTO Synroc … hot isostatic pressing | ANSTO Synroc |
| L11 | Projects | TVA Clinch River …; Linglong One …; HTR-PM …; NuScale US460 SDA … | See `02_Research/briefs/technology-projects-trl.md` |

Literature sources are listed in the reference list.
