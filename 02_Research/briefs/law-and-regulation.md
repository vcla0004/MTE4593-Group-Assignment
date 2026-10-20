Rubric coverage: R3.2, R3.4, R3.5, R3.7, R3.8, R1.4, R1.2, RB.2

# Brief: Australian law, regulation and party positions (analyst run 2, 20/10/2026)

For §8.1 (Law, regulation and licensing), §3 (Barriers) and slide 10. Canada's licensing and the C1 route are in `route-to-practice-c1.md`. Source keys refer to `02_Research/sources_run2.md`, and numbers to `03_LCA_Calculations/parameters_run2.yaml`. Calculations are in `scripts/law_timelines.py`, with output in `results/law_timelines.csv`.

> **Verification warning (read first).** No source could be opened from this session (proxy 403 and DNS failure on every host, including legislation.gov.au, austlii.edu.au, aph.gov.au and cnsc-ccsn.gc.ca). Every claim below comes from search-engine extracts, mostly restricted to the primary domain, and is **[TO VERIFY]** until Victor or the fact-checker opens the source. Statutory wording in quotation marks is as extracted; check it word for word on the Federal Register of Legislation or the state register before it goes in the report. The P1 checks are listed in §7.

## 1. Question

What legal and political barriers stop an SMR being built at an Australian coal site such as Liddell (NSW)? What would have to change, who decides, and how long would it take? How does that compare with the path Darlington actually took in Canada?

## 2. Answer in brief

1. **Three layers of law stand in the way at Liddell, not two.**
   - Federal environmental approval is barred: EPBC Act s 140A, plus the parallel bars in ss 37J and 146M (EPBC_Act_s140A).
   - Federal radiation licensing is barred: ARPANS Act s 10 (ARPANS_Act_s10).
   - NSW makes it an offence to build or operate any nuclear reactor: *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* s 8. Section 9 also bars any NSW electricity authority from building one or approving one (NSW_UMNFP_Act_1986).
   - Victoria (Loy Yang) and Queensland (Tarong, Callide) have their own bans. Queensland's Act also obliges the state to hold a plebiscite if the Commonwealth moves towards a facility there (QLD_NFP_Act_2007, s 21). [TO VERIFY all]
2. **ARPANSA could not license a private plant even if s 10 went.** The ARPANS Act covers only "controlled persons": Commonwealth entities and companies the Commonwealth controls. Non-Commonwealth operators fall to state regulators (ARPANSA_WhoWeRegulate).
   - The Coalition's 2024 plan was for Commonwealth-owned plants, which would sit inside ARPANSA's remit (ABC_2024_SevenSites).
   - A privately owned SMR at AGL's Liddell site would need a NSW nuclear regulator, or a new Commonwealth law extending federal licensing to private operators. Constitutional experts say such a law would rest on the corporations power and s 109 override, with a likely High Court test (Twomey_2025_Override). [TO VERIFY]
3. **The Senate decides, and the numbers say no in this Parliament.** As at 14 May 2026 the Senate was ALP 30, Coalition 27, Greens 10, One Nation 4 and five others (APH_SenateComposition_2026).
   - A bill needs 39 votes. The largest plausible pro-repeal bloc (Coalition, One Nation and Babet) is 32, seven short. Even with every other crossbencher it reaches only 36 (`law_timelines.csv`).
   - Repeal therefore needs Labor or the Greens. Both oppose it:
     - Labor: the Government says nuclear is the costliest, slowest option, and that voters "thoroughly rejected" it in 2025 (Bowen_Statements).
     - Greens: "The Greens will vote to keep the prohibition on nuclear in our environment laws" (Greens_2025_Plan).
   - In the House, Labor holds 94 of 150 seats (AEC_2025_Report). [TO VERIFY]
4. **The Coalition still promises repeal, but not the 2024 build plan.**
   - June 2024: seven Commonwealth-owned plants at coal sites, the first by 2035 (SMR) or 2037 (large) (ABC_2024_SevenSites).
   - After the May 2025 defeat: in-principle support only for removing the moratorium (ABC_2025_DeputyLeaderNuclear).
   - September 2026: under Angus Taylor, the Coalition would "repeal all legislative prohibitions on nuclear energy". The ABC notes this has "no chance" in the Senate without Labor or the Greens (ABC_2026_CoalitionEnergyPlan; Liberal_2026_EnergyPlan).
   - Whether the seven sites are still policy is unconfirmed. [TO VERIFY]
5. **NSW is the one live repeal, and it is stalled.**
   - A private member's bill to repeal the 1986 Act passed the Legislative Council on 6 May 2026, with all Liberal and National MLCs voting for it (NSWParl_RepealBill2025; NSW_Labor_UraniumPosition_2026).
   - It sits in the Legislative Assembly awaiting its second reading speech, and lapses on 28 November 2026 (NSWParl_LANoticePaper_2026).
   - The Minns Labor Government opposes it and has an Assembly majority. Minns has said the ban will not go "under his watch" (Minns_StateBan). [TO VERIFY]
6. **The site owner is a further veto.** AGL, which owns Liddell, says "nuclear energy is not a part of these plans" and is building a 500 MW / 1,000 MWh battery on the site (AGL_Liddell_NoNuclear). Without AGL's agreement, the Commonwealth would have to acquire the land compulsorily. [Secondary; TO VERIFY]
7. **Repeal is the start of the path, not the end.**
   - Darlington's CNSC path ran from the start of the environmental assessment in May 2007 to a licence to construct in April 2025: 17.9 years elapsed. That was with an experienced regulator and an existing nuclear site.
   - The construct-licence step alone took 29.1 months, about 2.4 years: application October 2022, decision 4 April 2025 (CNSC_DNNP_Page; CNSC_2025_LTCDecision; `law_timelines.csv`).
   - Australia stood up its naval nuclear regulator (ANNPSR) under a 2024 Act, operating from 1 November 2025 (DefenceMin_2025_ANNPSR). That shows a new regulator can be built in about two years once Parliament agrees [bill introduction date TO VERIFY]. But that regulator covers submarines, not power reactors.

## 3. The legal stack for an SMR at Liddell

| Layer | Instrument | Operative effect (as extracted, TO VERIFY) | Who can change it | Current position (Oct 2026) |
|---|---|---|---|---|
| Federal environment | EPBC Act 1999 s 140A (also ss 37J, 146M) | "The Minister must not approve an action consisting of or involving the construction or operation of" a fuel fabrication plant, **a nuclear power plant**, an enrichment plant or a reprocessing facility. Naval propulsion plants excepted | Commonwealth Parliament (both Houses) | In force. The EPBC reform package (assented 1 December 2025) renamed "nuclear action" as "radiological exposure action". Whether s 140A changed: **unknown, check** |
| Federal radiation safety | ARPANS Act 1998 s 10 | s 10(1): nothing in the Act "is to be taken to authorise the construction or operation" of those four facilities. s 10(2): "the CEO must not issue a licence under section 32" for them | Commonwealth Parliament | In force. Repeal bills in 2017 and 2022 failed; the 2022 bill was recommended against by a Senate committee on 11 August 2023 |
| Federal regulator's reach | ARPANS Act "controlled person" (s 13) | ARPANSA licenses only Commonwealth entities and Commonwealth-controlled companies | Commonwealth Parliament | A private SMR operator is outside ARPANSA's reach |
| NSW | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* ss 8–9 | s 8(2): offence to construct or operate a "nuclear facility", which includes "a nuclear reactor, whether or not designed for the purpose of generating electricity" (max. 1,000 penalty units). s 9: no state authority may build or approve a power reactor | NSW Parliament, or a valid inconsistent Commonwealth law (Constitution s 109) | Repeal Bill 2025 passed the LC on 6 May 2026; stalled in the LA; lapses 28 November 2026 |
| Victoria | *Nuclear Activities (Prohibitions) Act 1983* s 8 | Prohibits constructing or operating nuclear reactors, including power reactors, and other fuel-cycle facilities | Victorian Parliament | In force. One Nation promises repeal at the November 2026 state election; no Victorian Liberal position found |
| Queensland | *Nuclear Facilities Prohibition Act 2007* | Offence to construct or operate a nuclear facility (max. 1,665 penalty units). s 21: a plebiscite is triggered if the Commonwealth moves to allow one | Queensland Parliament | Premier Crisafulli (LNP) has ruled out changing it (secondary) |
| SA, WA, Tas, ACT | SA and WA waste-storage bans only | No state ban on power reactors (SA, Tas, ACT). WA bans nuclear waste storage and transport | — | SA's Northern and WA's Muja were the 2024 SMR-only sites |
| Site | AGL ownership of Liddell | Owner refuses nuclear use; the site is being reused for a battery | AGL, or compulsory acquisition | AGL opposed (secondary) |

## 4. What repeal would actually require: the steps for Liddell

| Step | Decision-maker | Evidence for time needed | Veto points |
|---|---|---|---|
| 1. Federal Parliament amends EPBC ss 37J, 140A and 146M (Clayton Utz also lists s 305(2)(d)) and repeals ARPANS s 10 | House and Senate | Past attempts in 2017 and 2022 failed. Under 2026 numbers the repeal bloc is 32 against 39 needed | Senate (Labor 30 + Greens 10 = 40 opposed) |
| 2. Choose who regulates a power reactor: (a) Commonwealth ownership under ARPANSA; (b) a new federal regulator with power over private operators; (c) a NSW regulator | Commonwealth (a, b); NSW (c) | ANNPSR took about two years from Act to operation for a narrower scope. IAEA guidance makes the legal framework and an independent regulator two of 19 infrastructure issues across three phases, with durations that depend on "commitment and resources" (IAEA_Milestones) | (b) faces a possible High Court challenge (Twomey) |
| 3. Remove the NSW ban (repeal), or override it under s 109 | NSW Parliament, or the Commonwealth | NSW repeal bill: LC passed after about 5.5 months (19 Nov 2025 to 6 May 2026); LA stalled | NSW Labor Assembly majority; Premier's stated position |
| 4. Secure the site | AGL, or Commonwealth acquisition | — | AGL refuses (secondary) |
| 5. Environmental assessment and approval under the amended EPBC Act | Federal Environment Minister | Darlington's EA began in May 2007; the site licence followed in August 2012 | Community, First Nations and legal challenge [run 6] |
| 6. Licensing stages (site, construct, operate) | The new regulator | Darlington: construct licence 29.1 months; operating licence applied for in March 2026, hearing likely in 2027. A new regulator would be slower than the CNSC [inference] | Hold points; public hearings |

**Translation to practice.**
- In practice, no SMR can be licensed in Australia before a change of federal government **and** a change in the Senate, then NSW repeal or a federal override, then the site.
- Each step has a different veto holder, so the probabilities multiply, not add.
- This is why the report models Liddell as a comparison of climate value, not a build proposal. It also supports the deck's "earliest 2040" framing (CSIRO via run 1).

## 5. Evaluation: three routes to a licensable SMR in Australia, scored against non-technical objectives

Qualitative, for §8.1 and as an input to the MCDA. Scores: 1 = poor, 3 = good. Analyst's judgement from the evidence above; for discussion, not a sourced score.

| Objective | A. Commonwealth-owned plant under ARPANSA (2024 Coalition model) | B. Federal licensing law for private operators, overriding states | C. Cooperative: state repeal plus a state or joint regulator |
|---|---|---|---|
| Legal changes needed | EPBC and ARPANS repeal, plus s 109 override of NSW (or NSW repeal) | EPBC and ARPANS repeal plus a new federal Act; s 109 override | EPBC and ARPANS repeal plus NSW repeal and a NSW regulator Act |
| Veto points | Senate; site owner | Senate; High Court; site owner | Senate; NSW Parliament; site owner |
| Regulator readiness | Best: builds on ARPANSA, which already licenses ANSTO | Medium: new body, as with ANNPSR | Worst: NSW has no nuclear regulator |
| Exposure to political reversal | High: a future government could sell or cancel | High | Lower once both levels agree |
| Social licence | Low: the states rejected it in 2024 | Lowest: overrides states | Highest, if it happens |
| Score (sum of 4 rows from "Veto points", higher is better) | 2+3+1+1 = 7 | 1+2+1+1 = 5 | 2+1+2+3 = 8 |

Reading: route C is the most durable but needs the most political change. Route A is the quickest legally but the most exposed. Under the 2026 Senate, none is open. **This is a sensitivity point for the MCDA's "feasibility" criterion: whichever route is assumed, Australia scores lowest on time-to-first-power.**

## 6. Party positions (for the §8.1 table and slide 10)

| Actor | Position on lifting the bans | Evidence (key) | Date of evidence |
|---|---|---|---|
| Federal Coalition (Taylor) | Lift all prohibitions; urges states to reconsider; seven sites not confirmed | ABC_2026_CoalitionEnergyPlan; Liberal_2026_EnergyPlan | Sept 2026 |
| Federal Coalition (Dutton, 2024) | Seven Commonwealth-owned plants at coal sites; first 2035 (SMR) or 2037 (large) | ABC_2024_SevenSites (find the party release) | June 2024 |
| Federal Labor Government | Opposed; cites GenCost cost and timing; "investment chill" | Bowen_Statements | 2024–25 (no 2026 statement found) |
| Greens | Will vote to keep the prohibition | Greens_2025_Plan | Apr 2025 |
| One Nation | Supports repeal (Victorian policy August 2026) | ABC, 31 August 2026 (secondary) | Aug 2026 |
| NSW Labor (Minns) | Opposes repeal of the 1986 Act | NSW_Labor_UraniumPosition_2026; Minns_StateBan | 2024–26 |
| NSW Liberal and Nationals MLCs | Voted for the repeal bill | NSW_Labor_UraniumPosition_2026 | May 2026 |
| Queensland LNP (Crisafulli) | Will not change the state ban | QLD_NFP_Act_2007 entry (secondary) | 2024–25 |
| AGL (Liddell owner) | No nuclear on its sites | AGL_Liddell_NoNuclear | 2024 [TO VERIFY] |

## 7. Against the slide deck's law slide (slide 10)

| Slide says | Finding | Fix |
|---|---|---|
| "EPBC Act s140A: The Environment Minister must not approve a nuclear power plant" | Accurate paraphrase. The words are "must not approve an action consisting of or involving the construction or operation of… a nuclear power plant". Sections 37J and 146M are parallel bars. Post-December 2025 status still to check | Keep. Add "(and ss 37J, 146M)" in the report; check the current compilation |
| "ARPANS Act s10: The national radiation regulator must not licence one" | Accurate for s 10(2), but incomplete. ARPANSA licenses only Commonwealth entities, so a private plant would never reach it anyway; the state bans are the binding constraint for private operators | Add in the speaker notes: "and NSW's own 1986 Act bans any reactor at Liddell". Spelling: Australian English uses "license" for the verb, so the line should read "must not license one" (style guide, R5.5) |
| "Parliament repeals both bans, then builds a licensing regime from scratch" | Incomplete: NSW repeal (or a federal override) and the site owner are also needed. "From scratch" overstates it, because ARPANSA exists and licenses ANSTO, and ANNPSR shows a new regulator can be stood up | "Parliament repeals both federal bans, NSW repeals its own, and a power-reactor regulator is set up" |
| "Canada's took 2.5 years for one licence" | The construct licence took 29.1 months (2.4 years), October 2022 to 4 April 2025. But that was one step of a path that began with an EA in May 2007 (17.9 years elapsed). The operating licence is still pending (applied March 2026, hearing likely 2027). Source: CNSC, not NucNet | "Canada's construction licence alone took about 2.5 years, on a site first licensed in 2012" |
| Sources line: "NucNet (2025)" | News source; R1.4 wants primary | Cite CNSC (2025) |

## 8. Numbers table

| Quantity | Value | Key | Status |
|---|---|---|---|
| Senate seats; majority needed | 76; 39 | APH_SenateComposition_2026; calculated | TO VERIFY |
| Largest pro-repeal bloc (Coalition + One Nation + Babet) | 32 (7 short) | calculated; voting intent assumed | TO VERIFY / assumption |
| Bloc plus all other non-Greens crossbench | 36 (3 short) | calculated | TO VERIFY |
| House seats, ALP / Coalition | 94 / 43 of 150 | AEC_2025_Report | TO VERIFY |
| Coalition 2024 plan: sites; first power | 7; 2035 (SMR), 2037 (large) | ABC_2024_SevenSites | TO VERIFY (secondary) |
| NSW repeal bill: introduced; LC passed; lapses | 19 Nov 2025; 6 May 2026; 28 Nov 2026 | NSWParl_* | TO VERIFY |
| NSW s 8 maximum penalty | 1,000 penalty units | NSW_UMNFP_Act_1986 | TO VERIFY |
| Qld maximum penalty | 1,665 penalty units | QLD_NFP_Act_2007 | TO VERIFY |
| ANNPSR operating from | 1 Nov 2025 | DefenceMin_2025_ANNPSR | TO VERIFY |
| Darlington: EA start to construct licence | 17.9 years | calculated | TO VERIFY inputs |
| Darlington: construct-licence application to decision | 29.1 months (sensitivity 29.1–30.1) | calculated | TO VERIFY inputs |

## 9. Translation to practice and non-technical solutions (R3.5, R3.7)

- **For our initiative (C1 at Darlington):** Australian law does not touch it. It matters for the Ontario-vs-Liddell comparison in §7:
  - An SMR at Liddell has no legal start date in this Parliament.
  - Run 1's start-year sensitivity should therefore treat 2040 as the optimistic case, not the central one [recommendation to run 1 and Victor].
- **Non-technical solutions an Australian government could take, if it chose to** (for §8.6, framed as conditions, not advocacy):
  1. Amend EPBC ss 37J, 140A and 146M and ARPANS s 10 together, so that environmental and safety regulation start at the same time.
  2. Give a regulator power-reactor licensing scope and funding before any site is chosen. That is the IAEA Milestones order: legal framework and regulator in Phase 2, before bids.
  3. Seek state agreement rather than s 109 override, to cut litigation risk and social-licence risk.
  4. Choose sites with willing owners and host communities. The Liddell owner is unwilling.
- **A cheaper lever that needs no repeal:** Australia can still contribute to SMR emissions cuts through materials and fuel. Silex's laser enrichment is being commercialised in the US because s 140A bars enrichment plants here (plan C3; secondary, TO VERIFY). This is the R4.3 connection.

## 10. Open gaps

1. **P1:** Open both Acts on the Federal Register of Legislation: the current compilation number and date, the exact words of ss 140A, 37J, 146M and ARPANS s 10, and whether the *Environment Protection Reform Act 2025* changed them.
2. **P1:** ARPANS Act s 13, the definition of "controlled person", word for word.
3. **P1:** NSW Act ss 8–9 wording and the s 8(3) "Commonwealth successor" exception. Could a Commonwealth-owned operator fall inside it? A legal question: flag it, don't answer it.
4. **P1:** NSW repeal bill status after May 2026 (the bill page and the latest Assembly notice paper).
5. The Coalition's own June 2024 release, and whether the 2026 policy still names the seven sites.
6. A Labor statement on nuclear from 2026; none was found.
7. Did the House Select Committee table a final report before the 2025 election? Its recommendations.
8. ANNPSR bill introduction date (Bills Digest No. 32, 2023–24), to give "bill to operating regulator" in months.
9. IAEA NG-G-3.1 Rev. 2: is there a typical newcomer timeline in the document? Do not use "10–15 years" unless it is found there.
10. First Nations and host-community consent at Liddell and in the Hunter: not covered here (analyst run 6).
11. Safety regulation of SMRs vs large reactors (graded approach, emergency planning zones): not covered in this run.
12. AGL's primary statement (an ASX release or results transcript).
