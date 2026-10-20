Rubric coverage: R3.4, R3.5, R3.7, R3.6, R3.8, R3.1, R1.4, R4.3, R4.4, RB.1, RB.7

# Brief: Route to practice for C1, LC3 concrete for Darlington Units 2–4 (analyst run 2, 20/10/2026)

For §8.1 (CNSC path and the qualification route), §8.6 (implementation pathway), §4.3 (the initiative) and §10. Source keys refer to `02_Research/sources_run2.md`, and numbers to `03_LCA_Calculations/parameters_run2.yaml`. Durations are calculated in `scripts/law_timelines.py`, with output in `results/law_timelines.csv`.

> **Verification warning.** No source could be opened from this session; everything is from search-engine extracts and is **[TO VERIFY]** until opened. Statements marked *(inference)* are the analyst's reasoning from those sources, not something a source says. They must be presented that way in the report, or checked with OPG or the CNSC.

## 1. Question

What has to happen, who decides, and how long does it take, for OPG to put LC3 (or a slag blend) into the concrete of Darlington Units 2–4 without delaying them? Which non-technical levers (licensing, procurement, finance) can make that happen?

## 2. Answer in brief

1. **The licensing window is the Units 2–4 approval, expected around 2028.**
   - The CNSC licence to construct (PRCL 32.00/2035, issued 4 April 2025, valid to 31 March 2035) covers **one** BWRX-300.
   - OPG has signalled "a future application for up to 3 additional units" (CNSC_DNNP_Page; CNSC_2025_LTCDecision).
   - Approval to progress Units 2–4 is reported as "expected in 2028" (ANS_2026_Darlington; secondary).
   - A concrete change has to be inside the Units 2–4 design and licensing basis by then. If it arrives later, it means a design change on a live project, and that is where schedule risk comes from.
2. **The governing concrete specification is the BWRX-300 steel-plate composite topical report, not mainly CSA N287.**
   - GEH's NEDO-33926 Rev. 2 specifies "that self-consolidating concrete is used in the integrated RB DP-SC modules". Infill strength is set "per draft ANSI/AISC N690". Containment criteria are adapted from the ASME code.
   - The CNSC and the NRC reviewed it jointly and found it an acceptable approach (GEH_NEDO33926; NRC_CNSC_2025_JointReport).
   - CSA N287 covers *concrete* containment structures. The BWRX-300 containment is steel-plate composite, so N287 probably does not govern it *(inference)*. CSA N291 (safety-related structures, building on CSA A23.3) is the likely Canadian layer for the reactor building and shafts *(inference; ask OPG or the CNSC)* (CSA_N287_N291).
3. **The cement standard is not the barrier; nuclear qualification is.**
   - CSA A3001 already allows ternary (Type IT) cements "with up to 15% limestone together with any SCM including calcined clay". Only LC3 recipes with more than 15% limestone would need a standards change (Hooton_2023_ACI; CSA_A3000_23).
   - Blended binders (slag, fly ash) are "widely adopted in NPP concrete mixes", including at "high replacement levels" (IJCSM_2026_NPPConcrete).
   - So S1 (slag) has precedent. S2 (LC3) needs new qualification data for self-consolidating infill between steel plates.
4. **Canada's federal Standard on Embodied Carbon in Construction probably does not apply to Darlington.**
   - It binds "departments within the meaning of section 2 of the Financial Administration Act" (TBS_SECC).
   - OPG is an Ontario Crown corporation, and the federal money comes through Crown corporations: a CAD 970 m CIB loan for Phase 1 (CIB_2022_Loan), and up to CAD 2 bn of CGF and CAD 1 bn of BOF equity (CGF_BOF_2025) *(inference from the scope clause; TO VERIFY)*.
   - The standard is a ready-made template, not an obligation. **Plan §2.1 point 4 should be reworded:** "Darlington has federal finance… that is the hook" is a proposal, not an existing requirement.
5. **The strongest lever is the CGF/BOF second tranche.** The equity comes in two tranches, the second "for SMRs 2–4 once project milestones are met" (CGF_BOF_2025).
   - The CGF already reports financed emissions, "Scope 1, 2, and 3 where possible" (CGF_InvestmentCriteria).
   - An embodied-carbon milestone (EPD disclosure plus a reduction target) attached to tranche 2 fits that mandate and the timing *(proposal)*.
6. **Staging removes most of the schedule risk.**
   - Apply a TBS-style requirement (at least 10% below the regional baseline) at once to non-safety concrete, where no nuclear qualification is needed.
   - Qualify LC3 self-consolidating infill on a full-scale DP-SC mock-up while Unit 1 is being built.
   - Adopt it in the safety-related DP-SC modules only if it clears qualification before the Units 2–4 design freeze. Otherwise fall back to S1 (slag), or to the current mix for those modules.
   - This is the "schedule-neutral" condition in plan §2.1 point 3, turned into a procedure.

## 3. The Canadian licensing path, and where C1 fits

| Milestone | Date | Key | C1 relevance |
|---|---|---|---|
| CNSC begins the EA (joint review panel) | May 2007 | CNSC_DNNP_Page | — |
| Licence to prepare site issued (10 years) | 17 Aug 2012 | CNSC_DNNP_Page | — |
| Site licence renewed, valid to 11 Oct 2031 | 12 Oct 2021 | CNSC_2021_LPTSRenewal | Covers site works for all four units |
| CIB commits CAD 970 m (Phase 1) | 2022 | CIB_2022_Loan | Phase 1 only; no embodied-carbon terms found |
| Licence-to-construct application (one unit) | Oct 2022 (in packages) | CNSC_DNNP_Page | — |
| Hearing part 1 (virtual); part 2 (Ajax) | 2 Oct 2024; 8–14 Jan 2025 | CNSC_2025_LTCDecision | — |
| Licence to construct issued, one BWRX-300, valid to 31 Mar 2035, 3 hold points, 4 site-specific conditions | 4 Apr 2025 | CNSC_2025_LTCDecision | 29.1 months after application |
| Ontario approves construction of Unit 1; four units about CAD 20.9 bn | 8 May 2025 | OPG_2025_Q1 | — |
| CGF/BOF equity (tranche 1 for SMR 1; tranche 2 for SMRs 2–4 on milestones) | 23 Oct 2025 | CGF_BOF_2025 | **Lever: tranche 2** |
| RHP-1 lifted (reactor building foundation, the DP-SC basemat) | 30 Mar 2026 | CNSC_RHP_Page | Unit 1 basemat concrete is placed, so C1 cannot apply to Unit 1 |
| Licence-to-operate application (Unit 1, 20 years) | Mar 2026 | CNSC_DNNP_Page | — |
| Operating-licence hearing | "likely in 2027" (OPG) | CNSC_DNNP_Page | — |
| Approval to progress Units 2–4 | "expected in 2028" | ANS_2026_Darlington | **Decision point for C1** |
| Unit 1 in service | Oct 2030 (OEB filing) / end-2030 grid connection | OPG_OEB_EB-2025-0297_D2-4-1 | — |
| Licence to construct expires | 31 Mar 2035 | CNSC_2025_LTCDecision | Units 2–4 need an amendment or a new licence either way *(inference)* |

**Comparison with CNSC norms.** REGDOC-3.5.1 gives an expected 32 months for a Class IA licence to construct (CNSC_REGDOC_3_5_1; the table extract was ambiguous, so check it). OPG's 29.1 months is about 3 months faster. The hearing-to-decision interval (2.8 months from part 2) fits the CNSC FAQ's "up to 90 days" (CNSC_FAQ_NewReactors).

**What Units 2–4 need *(inference from the sources; confirm with the CNSC)*:**
- The current licence authorises construction of one reactor, so construction of Units 2–4 needs Commission authorisation: a licence amendment or a new licence, with a public hearing.
- Standardised design and the Unit 1 safety case should make the review shorter than Unit 1's 29 months. No source gives a figure, so use a range of 12–29 months as a sensitivity bound only, labelled an assumption.
- A change to the infill concrete would be reviewed inside that application. It counts as a change to safety-related structures, so it needs evidence that the DP-SC design basis (strength, composite action, shrinkage, durability, shielding) still holds.

## 4. The qualification route for LC3 and slag infill

| Layer | What governs it | Is LC3 in scope today? | What has to be shown | Who decides |
|---|---|---|---|---|
| Cement product | CSA A3001:23 (in A3000:23) | Yes, as Type IT with ≤15% limestone plus calcined clay. A recipe with more limestone needs a CSA change | Standard cement tests | CSA; the cement supplier |
| Concrete materials and testing (general) | CSA A23.1/A23.2 (via N291) *(inference)* | Yes, as for any blended cement | Mix design, strength, durability class | OPG; the concrete supplier |
| DP-SC infill (Seismic Category I) | GEH NEDO-33926 Rev. 2: self-consolidating concrete; strength per draft AISC N690; jointly reviewed by the CNSC and NRC | **Unknown**: check §6.2.1 "Concrete Infill" for cement-type limits | Flow through stud and tie congestion; heat of hydration in thick sections; shrinkage (it governs faceplate-to-concrete composite action); strength gain; long-term durability; shielding density | GEH (design authority for the topical report), OPG (licensee), CNSC |
| Concrete containment | CSA N287.1/N287.2 | Probably not applicable: the containment is steel-plate composite *(inference)* | — | — |
| Shafts (forebay, condenser cooling water) | N291 if safety-related, otherwise A23.3 *(inference)* | Depends on the safety classification [TODO: OPG] | Normal durability for water-retaining structures | OPG |
| Precedent | NPP practice with slag and fly ash at high replacement (IJCSM_2026_NPPConcrete); the Canadian roadmap says SCMs can replace "30% or more" of cement (ISED_2022_ConcreteRoadmap) | Slag: yes. Calcined clay: no nuclear precedent found | — | — |

**Translation to practice.** The binding constraint is not a rule against LC3. It is that nobody has the qualification data for LC3 self-consolidating infill in DP-SC modules, and the data have to exist before the Units 2–4 design freeze. That is the RB.7 "future material properties" item:
- a self-consolidating LC3 mix with low shrinkage and controlled heat;
- data showing composite action with the faceplates;
- long-term durability and radiation data.

## 5. The procurement and finance levers, compared

| Lever | Decides | Binding on OPG? | Time to take effect | Schedule risk to Units 2–4 | Cost exposure | Evidence | Score (1–3: enforceability / speed / low schedule risk) |
|---|---|---|---|---|---|---|---|
| L1. OPG voluntary specification (EPDs plus at least 10% below the regional baseline, for non-safety concrete first) | OPG | Yes (own contracts) | Next procurement round | Low (non-safety only) | Small: TBS's one reported project cut 21%; cost not reported | TBS_GreeningProgress | 2 / 3 / 3 = **8** |
| L2. CGF/BOF tranche-2 milestone: embodied-carbon disclosure plus a reduction target, with a schedule-neutral exemption | CGF and BOF boards, with OPG | Yes, contractually, if agreed | With the tranche 2 terms (around the 2028 approval) | Low, if the exemption clause is written in | Capped, e.g. TBS's 2% premium rule as a model | CGF_BOF_2025; CGF_InvestmentCriteria; TBS_GreeningProgress | 3 / 2 / 3 = **8** |
| L3. Ontario shareholder direction to OPG | Ontario Minister of Energy | Yes | Months | Depends on wording | Must be recovered through OEB-approved payment amounts; the OEB reviews prudence [TO VERIFY] | OPG_OEB_EB-2025-0297_D2-4-1 | 3 / 2 / 2 = **7** |
| L4. Extend the federal standard to projects financed by federal Crown corporations (CIB, CGF) | Treasury Board or the Finance Minister (mandate letters) | Only after a policy change | Years | Low | — | TBS_SECC | 2 / 1 / 3 = **6** |
| L5. CNSC licence condition | CNSC | — | — | — | — | — | Not a lever: the CNSC regulates safety, not climate. It only has to accept that the change is safe *(inference)* |

**Reading.** L1 and L2 together score best. L1 is quick and safe; L2 is binding and timed to the Units 2–4 decision.
- Weight test: if enforceability counts double, L2 leads with 11, L1 and L3 tie on 10, and L4 has 8.
- If speed counts double, L1 leads with 11, then L2 10, L3 9 and L4 7.
- Under both weightings the recommendation is the same: **L1 now, L2 at tranche 2.**
- The scores are the analyst's judgement from the evidence in the table. They are for the MCDA discussion, not sourced scores.

**A design trap in L1 and L2.** The federal standard benchmarks "high performance" and other specialised mixes at 130% of the baseline (TBS_SECC). Self-consolidating DP-SC infill could be classed as specialised, which would let it pass while still emitting 30% more than the baseline. Any OPG or CGF clause should benchmark the DP-SC infill against a cement-rich self-consolidating reference mix, not the general baseline. Otherwise the clause does nothing for the very concrete C1 targets.

## 6. Implementation roadmap for C1 (for §8.6 and a figure)

All durations are the analyst's planning estimates (assumptions), anchored to the dated milestones above.

| Step | When | Who decides or does | Gate or output | Fallback |
|---|---|---|---|---|
| 0. Disclosure and non-safety concrete: EPDs for every Units 2–4 concrete package; at least 10% below the regional baseline for non-safety structures (L1) | From the next procurement round (2027) | OPG procurement; concrete suppliers | EPD register; tonnes CO₂e avoided [Sam: per-m³ saving × non-safety volume] | — |
| 1. Mix development: S1 slag and S2 LC3 (≤15% limestone, so CSA A3001 Type IT) self-consolidating infill mixes; flow, heat, shrinkage and strength tests | 2027 (about 6–9 months) | OPG engineering, GEH, cement supplier [St Marys Bowmanville: LC3 or calcined-clay capability TO VERIFY] | Mix data against NEDO-33926 / AISC N690 infill requirements | Drop S2, keep S1 |
| 2. Full-scale DP-SC mock-up infill trial, off the Unit 1 critical path | 2027–28 (about 6 months) | OPG, GEH; CNSC staff invited to witness | Trial report: filling, voids, temperature, composite action | Keep the current mix for DP-SC; LC3 only in non-safety concrete |
| 3. Design-change evaluation, submitted with the Units 2–4 licensing package | By the 2028 approval | GEH (topical report owner), OPG (licensee); CNSC reviews | Accepted change, or a request for more data | If more data are needed, Units 2–4 go ahead with the current mix; LC3 enters at a later unit or project |
| 4. Tranche-2 milestone (L2): disclosure plus a reduction target, with a schedule-neutral clause and a cost cap | Tranche 2 terms (around 2028) | CGF, BOF, OPG | Signed condition | L1 only |
| 5. Placement in Units 2–4 basemats and shafts; the hold point at the reactor building foundation (as RHP-1 was for Unit 1) | From the Units 2–4 construction start [Leroy: dates] | OPG; CNSC inspection | As-built EPDs | — |
| 6. Reporting | Annually | OPG (ESG report); CGF (financed emissions) | Verified t CO₂e saved | — |

**Time needed.** About 18–24 months from mix development (step 1) to licensing acceptance (step 3). That fits only if step 1 starts in 2027 and the approval comes in 2028 as reported *(assumption; the critical path is steps 1–3)*. This is the evidence for the thesis condition that C1 is worth adopting only if it is schedule-neutral (plan §2.4). Run 1's `schedule_value` gives the CO₂e cost of each month of delay, which caps how much delay C1 could ever justify.

## 7. Stakeholders who decide (feeds §8.5)

| Actor | Role in C1 | Power | Interest in C1 | Evidence |
|---|---|---|---|---|
| OPG | Licensee, owner (majority), buyer | High | Medium: net-zero company by 2040; supplier ESG scorecard asks for supply-chain targets | OPG_2020_ClimatePlan |
| GE Vernova Hitachi | Design authority; owns the DP-SC topical report | High (technical veto) | Low–medium: a change costs review effort, but a qualified LC3 infill helps sales | GEH_NEDO33926 |
| CNSC | Safety regulator | High (safety only) | Neutral: only needs a safe design | CNSC_* |
| CGF / BOF | Minority equity (15% / 7.5%) with a milestone-conditional tranche 2 | Medium–high at tranche 2 | High: emissions mandate | CGF_BOF_2025; CGF_InvestmentCriteria |
| CIB | Phase 1 lender | Low for Units 2–4 (Phase 1 only) | Medium | CIB_2022_Loan |
| Ontario (Minister of Energy; OEB) | Shareholder; rate regulator | High | Cost-focused (ratepayers) | OPG_OEB_EB-2025-0297_D2-4-1 |
| Cement and concrete suppliers | Supply LC3 or slag | Medium | High if the volume is credible | [TODO: St Marys] |
| CSA Group | Standards (A3001, N291) | Medium (slow) | Medium | CSA_* |

## 8. Numbers table

| Quantity | Value | Key | Status |
|---|---|---|---|
| Construct-licence application to decision | 29.1 months (2.4 years); sensitivity 29.1–30.1 | calculated | inputs TO VERIFY |
| CNSC expected time, licence to construct (Class IA) | 32 months | CNSC_REGDOC_3_5_1 | TO VERIFY (ambiguous extract) |
| Hearing part 2 to decision | 2.8 months | calculated | inputs TO VERIFY |
| EA start to construct licence | 17.9 years | calculated | inputs TO VERIFY |
| Licence validity from decision; from 20/10/2026 | 10.0 years; 8.4 years | calculated | inputs TO VERIFY |
| RHP-1 lifted after licence | 11.8 months | calculated | inputs TO VERIFY |
| Four-unit cost; Unit 1; shared facilities | CAD 20.9 bn; 6.1 bn; 1.6 bn | OPG_2025_Q1 | TO VERIFY |
| CIB loan | CAD 970 m | CIB_2022_Loan | TO VERIFY |
| CGF equity, stake; BOF equity, stake | up to CAD 2 bn, up to 15%; up to CAD 1 bn, 7.5% | CGF_BOF_2025 | TO VERIFY |
| Tranche 1 received (April 2026) | about CAD 585 m | OPG_2026_Q1 | TO VERIFY |
| Federal concrete requirement; specialised-mix allowance | ≥10% below the regional baseline; 130% of baseline | TBS_SECC | TO VERIFY |
| Federal thresholds | CAD 5 m (2022 notice: 10 m) and 100 m³; steel 200 t; WBLCA 30% or within a 2% premium (>2,000 m²) | TBS_GreeningProgress | TO VERIFY |
| First reported project result | 21% below baseline (2024–25) | TBS_GreeningProgress | TO VERIFY |
| CSA A3001 limestone cap (PLC / Type IT) | 15% | Hooton_2023_ACI; CSA_A3000_23 | TO VERIFY |
| Average achievable SCM replacement (roadmap) | ≥30% of cement | ISED_2022_ConcreteRoadmap | TO VERIFY |

## 9. Interfaces raised (for the coordinator to add to plan §5; this run did not edit `plan.md`)

| From → to | Item | Sources | Serves |
|---|---|---|---|
| Victor (analyst) → Leroy | Licensing milestones for the timeline table: §3 above (application Oct 2022; licence 4 Apr 2025 to 31 Mar 2035; RHP-1 lifted 30 Mar 2026; operating-licence application Mar 2026, hearing likely 2027; Units 2–4 approval expected 2028) | CNSC_*, ANS_2026_Darlington | RB.3, R3.4 |
| Victor (analyst) → Sam, Leroy | **Possible conflict on net output:** OPG's OEB filing (Exhibit A1-4-3) reportedly gives **315 MW net** per unit; the deck and run 1 use 300 MWe | OPG_OEB_EB-2025-0297_D2-4-1 vs deck | R2.5, R2.3 |
| Victor (analyst) → Sam | Are the forebay and condenser-cooling-water shafts safety-related (N291) or not? That decides whether C1's biggest known concrete volume needs nuclear qualification at all. Also: the per-m³ saving for S1 and S2, to size step 0 | GEH_NEDO33926; CSA_N287_N291 | R2.3, R4.2 |
| Victor (analyst) → examiner | Plan §2.1 point 4 and the §8.6 outline treat the federal embodied-carbon standard as applying via federal finance. The evidence says it binds federal departments only, so reword it as a proposed lever (L2/L4) | TBS_SECC | R3.7, R1.5 |

## 10. Open gaps

1. **P1:** NEDO-33926 Rev. 2 §6.2.1 "Concrete Infill": any cement type, SCM or limestone limits? The joint report's conditions on materials.
2. **P1:** Which standards the Darlington BWRX-300 licence conditions handbook names for DP-SC and shaft concrete (N291? N287? AISC N690?).
3. **P1:** The scope clause of the Policy on Green Procurement (s 3) and the standard (s 4.1). Confirm that Crown corporations are excluded and whether CIB or CGF have adopted anything similar.
4. The CGF/BOF agreement: what the "project milestones" for tranche 2 are. Can conditions still be added?
5. The Units 2–4 regulatory step: amendment or new licence, and the expected review time. The OEB filing D2-4-1 is the best lead.
6. St Marys Cement Bowmanville: LC3 or calcined-clay capability; local clay supply; slag supply after Dofasco's move to an electric arc furnace (plan §2.1 point 2).
7. Cost premium of LC3 or slag self-consolidating concrete versus the current mix, needed for the abatement cost ($/t) in run 5.
8. Whether OPG's 2040 net-zero commitment covers Scope 3 or construction emissions.
9. A primary source for "approval to progress Units 2–4 expected in 2028" (OPG or Ontario rather than the ANS).
