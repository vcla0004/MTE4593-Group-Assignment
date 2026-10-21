Rubric coverage: R3.3, R3.4, R3.5, R3.7, R3.8, R3.6, R3.1, R1.3, R1.4, R5.2, R4.3

# Brief: social licence, stakeholders, money flows, workforce and waste governance (analyst run 6, 21/10/2026)

For §8.4 (social licence), §8.5 (stakeholders and money flows, F8) and §8.6 (implementation pathway). Source keys refer to `02_Research/sources_run6.md` (new) and `sources_run4.md` / `sources.md` (existing). Numbers are in `03_LCA_Calculations/parameters_run6.yaml`. The working is in `scripts/social_licence.py`, with output in `results/social_licence.md`, `results/social_licence.csv` and `results/F8_stakeholder_map.png`. The PESTLE summary is in `briefs/pestle.md`.

> **Verification warning (read first).** No source could be opened from this session: every host returned proxy 403 or DNS failure (list in `sources_run6.md`). Every claim below comes from search-engine summaries and is **[TO VERIFY]** until Victor or the fact-checker opens the source. The P1 checks are in §10. Stakeholder scores and the route scores in §8 are the **analyst's judgement**, labelled as such, each tied to an evidence key.

## 1. Question

What social, workforce and waste-governance factors decide whether (a) C1 and Darlington Units 2–4 get built in Ontario, and (b) a BWRX-300 could ever be built at Liddell? Who holds power, who pays and who earns, and which non-technical mechanisms would move the Australian case from "blocked" towards "buildable"?

## 2. Answer in brief

1. **The same reactor sits in two opposite social settings.** At Darlington, all seven high-power actors support the project or are neutral; the power-weighted stance is **+1.07** on a −2 to +2 scale. At Liddell, three of the four high-power actors are opposed (the Commonwealth, NSW and site owner AGL); the stance is **−1.03** (`social_licence.md` §6; analyst judgement). The technology is identical; the social licence is not. That is the main non-technical finding for translation to practice.
2. **Australian support is real but soft.** Lowy 2024: 61% support "using nuclear power to generate electricity", 37% oppose (n = 2,028, ±2.2%) (Lowy_2024). Griffith–Monash, 2024 wave: 59% want to **keep the ban**, up from 51%, and 30% want it removed (GriffithMonash_2025). Both can be true because the questions differ, so support depends on framing. Support also drops for a local plant: national 45% vs local 25% (Newspoll_2007), and 44% vs 28% "comfortable living close" (Essential_2019). No newer independent national electricity poll was found. The 2025 polls found were commissioned by interested parties; together they suggest support fell during the 2025 campaign. [TO VERIFY all]
3. **The safety gap is large, and it is not closed by data.** Deaths per TWh: coal 24.62, gas 2.82, wind 0.04, nuclear 0.03, solar 0.02 (OWID_deaths), so coal is about **820×** nuclear. Yet in the Griffith–Monash survey 26% said the risks of nuclear "far outweigh" the benefits. The risk-perception literature explains why: nuclear sits at the extreme of Slovic's "dread" and "unknown" factors (Slovic_1987; Siegrist_Arvai_2020). **Implication:** information campaigns alone will not build a social licence. What does is control, benefit and trust: consent, equity and a local say.
4. **The health benefit, like the carbon benefit, depends on what is displaced.** One BWRX-300 (2.37 TWh/yr) avoids about **58 statistical deaths a year if it displaces black coal**, **6.6 if it displaces gas** (Darlington's best case, since Ontario has no coal), and about **zero against wind or solar** (`social_licence.md` §2). In the 2024 ISP Step Change, coal leaves the NEM by 2038 (aemo2024_isp, secondary), before a 2040 start at Liddell, so the coal figure is an upper bound there. This links to §7's finding that schedule decides climate value.
5. **Consent is a hard gate in both countries, but Canada has a working mechanism and Australia has a record of failure.**
   - **Darlington:** the CNSC found it met its duty to consult (CNSC_2025_LTC). On 23 June 2026 the seven Williams Treaties First Nations agreed a **C$700 m** loan to DNNP LP that converts to equity when all four units are complete, guaranteed 50/50 by the federal CILGC and Ontario's IOFP (WTFN_DNNP_2026). Consent is still contested inside that group: MSIFN asked to set "conditions for consent" (MSIFN_CNSC_Submissions), and Curve Lake said treaty rights were not shown to be considered (CurveLake_CMD24H383).
   - **Australia:** the Kimba ballot gave **61.58%** yes (452 of 734), below the reported 65% benchmark, and excluded Barngarla native title holders, whose own poll was 100% no (Kimba_Ballot_2019). The Federal Court set the Napandee declaration aside for apprehended bias on 18 July 2023, and the site was abandoned (Barngarla_2023FCA809; King_2023_Napandee). Muckaty was nominated in 2007 and withdrawn in 2014 (Muckaty_2014). Top-down siting has failed twice in court.
6. **Waste governance is the clearest gap.** Canada has a producer-funded statutory process: the NWMO ran a volunteer-host search from **2010** (22 communities → 11 → 2), selected the WLON–Ignace area on **28 November 2024** after an Ignace vote of **77%** (495/640) and a separate WLON willingness decision, and priced community benefit at **C$170 m over 81 years** (NWMO_SiteProcess; NWMO_Ignace_2024; NWMO_2024_Selection). The lifecycle cost (**C$26 bn, 2020$**) is funded by the waste owners, OPG included, through trust funds (C$5.3 bn at December 2023) (NWMO_ProjectCosts). Australia has no disposal route even for current research-reactor waste: ARWA restarted after Kimba, and Lucas Heights stores were said to start reaching capacity from 2026 (ARWA_2020). Spent fuel from a Liddell SMR would have nowhere to go. [TO VERIFY all]
7. **Workforce: Ontario has one, Australia is building one for submarines.** About 1,900 PWU members work at the Darlington site alone (PWU_CMD21H438). Ontario funds OCNI to map its supply chain (OCNI_LMP_2025), and CBoC estimates **1,600** jobs a year during construction and **200** during operation per 300 MW SMR (CBoC_2021_SMR). In Australia, a Defence document says there is "no current Australian talent pool" for civilian nuclear roles, and projects a shortfall of **76,950** in four trades by 2030–31 before submarine demand (Defence_FOI_Workforce). AUKUS needs about **20,000** jobs over 30 years (JSCOT_224_Ch6). A civil SMR programme would compete with AUKUS for the same scarce people.
8. **Unions are the mirror image.** Ontario's nuclear unions back OPG at the CNSC (PWU_CMD21H438). Australia's ACTU and ETU campaigned against the Coalition plan (ACTU_2024; ETU_2024_Report); only the Victorian MEU has backed nuclear, for the Latrobe Valley (MEU_2022_Latrobe). At Liddell the jobs argument is weaker than it looks: 65% of the 180 workers moved to Bayswater with no forced redundancies, and AGL hopes for up to 1,000 jobs at its Hunter Energy Hub (AGL_Liddell_Workforce).
9. **Who pays: Ontario ratepayers, mostly.** Of the C$20.9 bn DNNP budget, the named public financiers cover about 22%: CGF equity C$2.0 bn (9.6%), BOF equity C$1.0 bn (4.8%), the CIB loan C$0.97 bn (4.6%) and the WTFN loan-to-equity C$0.70 bn (3.3%). The remaining **C$16.2 bn (78%)** is OPG's, recovered through OEB-approved payment amounts (`social_licence.md` §4). (Debt and equity are added only to show scale.)
10. **Best non-technical route for Australia (if the bans went):** volunteer siting with a Traditional Owner willingness test and a priced hosting agreement, plus First Nations equity backed by a government loan guarantee. These routes (R2, R3) beat Commonwealth-led siting (R1) by 3–6 points under all five weight sets. But "no SMR at Liddell" (R4, AGL's plan) scores higher still, because it needs no change in law or consent (§8).

## 3. Perceived vs actual safety (§8.4)

| Measure | Value | Source |
|---|---|---|
| Support "using nuclear power to generate electricity" (2024) | 61% (27 strongly + 34 somewhat) | Lowy_2024 |
| Oppose (2024) | 37% (20 + 17); don't know 2% | Lowy_2024 |
| Same, 2011 (different wording) | 35% support / 62% oppose | Lowy_2024 |
| Keep the ban (2023 → 2024) | 51% → 59% | GriffithMonash_2025 |
| Remove the ban (2023 → 2024) | 34% → 30% | GriffithMonash_2025 |
| "Risks far outweigh benefits" (2023 → 2024) | 21.9% → 26% | GriffithMonash_2025 |
| Keep the ban, women vs men (2024) | 66% vs 51% | GriffithMonash_2025 |
| National vs local plant (2007) | 45% vs 25% | Newspoll_2007 |
| Support vs comfortable living close (2019) | 44% vs 28% | Essential_2019 |
| Deaths per TWh: coal / gas / nuclear / wind / solar | 24.62 / 2.82 / 0.03 / 0.04 / 0.02 | OWID_deaths |
| Coal ÷ nuclear | 821× | calc |

**Synthesis (R1.3).** Lowy and Griffith–Monash appear to disagree (net +24 for nuclear vs +29 for keeping the ban). They measure different things: a general preference for a technology and a legal status quo. Both, together with the 16–20-point national-vs-local gap, describe soft, conditional support. Slovic's dread factor predicts exactly this: acceptance falls where the hazard is close, involuntary and controlled by others.

**Evaluation for translation to practice.** Even at 61% national support, a Liddell SMR would face a host region where local support is historically about 20 points lower, a Labor government that won 94 of 150 House seats after campaigning against nuclear (AEC_2025_Report), and a site owner that has said no. Public opinion is not the binding barrier today (law is: §8.1), but it decides whether the law ever changes. The safety evidence is necessary but not sufficient. The levers that work are control (a local say), benefit (equity, hosting payments) and trust (an independent regulator with a record).

**Implementation (non-technical).** (a) Never use deaths per TWh alone in public messaging. Pair it with what the host community controls and gains. (b) Frame the choice as a comparison (what the SMR displaces) rather than in absolute terms; the coal comparison stops being relevant once coal has left the grid. (c) Commission an independent probability-panel poll of the Upper Hunter before any siting decision. [Recommendation; no source]

## 4. Consent and First Nations (§8.4)

| | Darlington (Canada) | Liddell (Australia) |
|---|---|---|
| Traditional Owners | Williams Treaties First Nations (7 Michi Saagiig and Chippewa Anishinaabeg Nations), including MSIFN | Wonnarua people (AGL_Wonnarua); Plains Clans native title claim NC2013/006 over about 10,000 km² of the Hunter, status unknown (Wonnarua_NativeTitle) |
| Legal basis for a say | Constitutional duty to consult (s 35); UNDA 2021 legislates UNDRIP into the interpretive context (UNDA_2021; Kebaowek_2025FC319) | Native title probably extinguished on AGL freehold [inference, TO VERIFY]; heritage law applies; UNDRIP endorsed but not legislated [TO VERIFY] |
| What happened | CNSC found the duty met (CNSC_2025_LTC); C$700 m WTFN loan-to-equity, guaranteed by CILGC and Ontario (WTFN_DNNP_2026) | No process. Coalition 2024: "extensive community engagement" but possible compulsory acquisition (Coalition_Liddell_2024) |
| Residual dissent | MSIFN "conditions for consent"; Curve Lake: treaty and 2018 Settlement not shown to be considered | Unknown: no Wonnarua position found |
| Litigation risk | Real: Kebaowek (2025) found consultation on a CNL waste facility inadequate; NGOs won at first instance against DNNP's EA in 2014, reversed on appeal in 2015 (OPG_v_Greenpeace_2015FCA186) | Real: Barngarla (2023) set aside Napandee for bias; Muckaty settled (2014) |

**Synthesis.** Canada's model works because consultation is a legal duty with a funded way to say yes (equity with a guarantee). Australia's waste history shows the failure mode: defining the "community" by council electors excluded native title holders, and the decision fell in court. Even in Canada, equity has not ended dissent within the treaty group. Equity is a means of consent, not a substitute for it.

**For C1 specifically.** C1 (LC3 infill) changes no land use, emissions or waste, so it raises no new consent issue. Its social-licence value is indirect: OPG can report a lower-carbon build to the CGF, whose mandate covers emissions (CGF_InvestmentCriteria), and to host and First Nations partners who are now equity holders with an interest in the project's reputation [analyst inference].

## 5. Stakeholders: power/interest (§8.5, F8)

Figure: `03_LCA_Calculations/results/F8_stakeholder_map.png` (two panels; numbered markers; colour = stance). Full tables in `social_licence.md` §6. Scores are analyst judgement (1–5), each with an evidence key in `parameters_run6.yaml`.

| Quadrant | Darlington | Liddell |
|---|---|---|
| Manage closely (high power, high interest) | Ontario (+2), OPG (+2), WTFN (+1), Govt of Canada (+2), GE Vernova Hitachi (+1) | AGL (−2) |
| Keep satisfied (high power, lower interest) | CNSC (0), OEB (0) | Commonwealth (−2), NSW (−2), ARPANSA (0) |
| Keep informed (lower power, high interest) | Clarington (+2), unions (+2), NGOs (−2) | NGOs (−2), ACTU/ETU (−2), Wonnarua (0, unknown), Coalition (+2), Upper Hunter (0) |
| Monitor | Cement suppliers (+1), ratepayers (0) | Renewables investors (−1), SMR vendors (+1) |
| Power-weighted stance | **+1.07** | **−1.03** |

**Reading.** At Darlington the decisive actors for C1 are OPG, GE Vernova Hitachi (owner of the infill specification) and the CGF/BOF at tranche 2 (route-to-practice-c1.md §7). At Liddell the vetoes are layered (Commonwealth law, NSW law, the site owner), and the only strong supporter, the federal Coalition, is in opposition with 27 Senate seats (APH_SenateComposition_2026). **Cement suppliers:** no evidence was found that St Marys Cement (Bowmanville) supplies DNNP or offers LC3. This is a gap, not a finding.

## 6. Money flows: who pays and who earns (§8.5)

| Flow | Who pays | Who earns | Amount | Source |
|---|---|---|---|---|
| Construction budget, four units | OPG, then Ontario ratepayers via OEB-approved payment amounts | GE Vernova Hitachi and the construction partners [names TODO: OPG release "Team forms to build North America's first SMR" not opened], suppliers (80% of spend claimed to go to Ontario companies) | C$20.9 bn | ON_2025_FID |
| Phase 1 loan | Canada Infrastructure Bank (federal Crown) | DNNP; CIB earns interest | C$0.97 bn | CIB_2022_Loan |
| Equity | Canada Growth Fund (federal) / Building Ontario Fund (Ontario) | DNNP; CGF and BOF earn returns on 15% / 7.5% stakes; tranche 2 tied to Units 2–4 milestones | C$2.0 bn / C$1.0 bn (C$0.585 bn received April 2026) | CGF_BOF_2025; OPG_2026_Q1 |
| First Nations loan-to-equity | WTFN, with the debt guaranteed by CILGC and Ontario (taxpayers carry the default risk) | WTFN earn equity returns once all four units are complete | C$0.70 bn | WTFN_DNNP_2026 |
| Federal tax credit | Federal taxpayers | Eligible low-emitting electricity investors (DNNP eligibility TO VERIFY) | 15% of eligible capital cost | MPO_2025_Darlington |
| Waste disposal | OPG (and so ratepayers), through NFWA trust funds | NWMO; host communities (Ignace C$170 m over 81 years) | C$26 bn lifecycle (all Canadian used fuel) | NWMO_ProjectCosts; NWMO_Ignace_2024 |
| Jobs and GDP (claimed) | — | Workers, Ontario economy | 18,000 construction jobs; C$500 m/yr; CBoC: C$13.7 bn Ontario GDP, 2,000 jobs/yr (four units) | ON_2025_FID; CBoC_2023_DNNP |
| **Liddell (hypothetical)** | Under the 2024 Coalition model, Commonwealth taxpayers (Commonwealth-owned plants) | Vendor, construction workforce; AGL if paid for the site | Not costed here (see §8.2 / run 5) | ABC_2024_SevenSites; Coalition_Liddell_2024 |

**Evaluation.** In Ontario the cost risk sits with ratepayers through a regulated utility, and public finance is used to lower the cost of capital and spread ownership (federal, provincial, First Nations). That model needs a state-owned utility with a regulated rate base. NSW privatised its generators, and AGL owns Liddell. An Australian SMR would therefore need either Commonwealth ownership (the 2024 Coalition model, with taxpayers carrying the risk) or a contract-for-difference type underwriting scheme [analyst inference; the scheme design is for §8.2/§8.6 and is unsourced here].

## 7. Workforce and waste governance (§8.4, §8.6)

| Factor | Ontario | Australia | Effect on translation to practice |
|---|---|---|---|
| Operating nuclear workforce | Large and unionised: about 1,900 PWU members at Darlington alone | None for power. ANSTO runs a research reactor [staff numbers TODO] | A first Australian plant must import operators and train for about a decade [assumption] |
| Pipeline | OCNI supply-chain mapping (C$1.9 m); CBoC 1,600 construction / 200 operations jobs per SMR | UNSW masters programme since 2014; AUKUS training (A$68.4 m academy; 4,001 STEM places) | Civil SMRs would compete with AUKUS (20,000 jobs over 30 years) and a 76,950 four-trade shortfall |
| Waste route | NWMO site selected (2024); producer-funded trust funds | No facility; Kimba set aside (2023); ARWA restarting; AUKUS high-level waste to go on Defence land (Marles_2023_AUKUSWaste) | Spent fuel from Liddell would need new law and a siting process of a decade or more (NWMO: 14 years from start to site) |
| Who pays for waste | Waste owners, by statute | Commonwealth (taxpayer) for current waste [TO VERIFY] | Australia would need an NFWA-style levy from day one |

## 8. Non-technical solutions compared (R3.6, R3.7)

Social-licence routes for an SMR at Liddell, scored 1–3 on legitimacy, legal risk, speed, public cost and fairness (analyst judgement; evidence in `parameters_run6.yaml` §7).

| Route | Equal | Legitimacy ×2 | Speed ×2 | Fairness ×2 | Cost ×2 |
|---|---|---|---|---|---|
| R1 Commonwealth-led siting (2024 Coalition model; acquisition if needed) | 7 | 8 | 9 | 8 | 9 |
| R2 Volunteer host + willingness test including Traditional Owners + hosting agreement (NWMO model) | 11 | 14 | 12 | 13 | 13 |
| R3 R2 + First Nations equity with a government loan guarantee (WTFN/CILGC model) | 11 | 14 | 12 | **14** | 12 |
| R4 No SMR: firmed renewables at Liddell (AGL's plan) | 14 | 17 | 17 | 16 | 17 |

- **Robust result:** consent-based routes beat top-down siting under every weight set (by 3–6 points). R3 wins only when fairness is weighted up; R2 wins when public cost is.
- **Honest result:** R4 is highest throughout. On social licence alone, the Australian SMR case is weaker than the alternative. This feeds the §9 MCDA (environment and cost weighed there).

**Implementation pathway (for §8.6).**

*Darlington / C1 (actionable now):*
1. Tie C1 to the CGF/BOF tranche-2 milestone and an OPG procurement specification (route-to-practice-c1.md §5, L1 + L2).
2. Report embodied-carbon savings to the WTFN and Clarington as equity partner and host. This strengthens the licence at no schedule cost [analyst recommendation].
3. Keep C1 off the Unit 1 critical path: the social and climate value of on-time delivery exceeds C1's saving (§6.3 finding 5; schedule_value.md).

*Australia (only if the bans are repealed; §8.1):*
1. **Waste first:** legislate an NFWA-style producer-funded waste levy and an independent waste organisation before any reactor licence. Use the NWMO volunteer process, with Traditional Owners voting separately, as the model.
2. **Consent:** replace council-elector ballots with a two-key willingness test (host community and Traditional Owners), as at Ignace and WLON. Rule out compulsory acquisition for the reactor site.
3. **Benefit-sharing:** a priced, long-term hosting agreement (Ignace benchmark: C$2.1 m a year, nominal) and an option for First Nations equity backed by a federal loan guarantee. Australia has no CILGC equivalent [TO VERIFY]; creating one is a policy step.
4. **Workforce:** a nuclear skills plan coordinated with AUKUS, so a civil programme does not draw from the same trades pool.
5. **Site owner:** without AGL's agreement there is no site. A brownfield SMR route needs a willing owner, which points to a state- or Commonwealth-owned coal site rather than Liddell [analyst inference; feeds R4.3].

## 9. Numbers table

| Quantity | Value | Unit | Source / calc | Status |
|---|---|---|---|---|
| Lowy support / oppose (2024) | 61 / 37 | % | Lowy_2024 | unverified |
| Keep ban 2023 → 2024 | 51 → 59 | % | GriffithMonash_2025 | unverified |
| Coal ÷ nuclear deaths per TWh | 821 | × | calc from OWID_deaths | inputs unverified |
| Deaths avoided/yr, one unit vs coal (CF 0.80–0.95) | 58.2 (51.7–61.4) | /yr | calc | inputs unverified |
| Deaths avoided/yr, one unit vs gas | 6.6 (5.9–7.0) | /yr | calc | inputs unverified |
| Deaths avoided/yr, four Darlington units vs gas | 26.4 | /yr | calc | upper bound |
| Kimba yes share | 61.58 (452/734) | % | Kimba_Ballot_2019; recomputed | unverified |
| Ignace yes share | 77.3 (495/640) | % | NWMO_Ignace_2024; recomputed | unverified |
| Ignace hosting payment | 170 over 81 years (2.10/yr) | C$ m | NWMO_Ignace_2024 | unverified |
| NWMO siting, start to selection | 14 | years | NWMO_SiteProcess | unverified |
| NWMO lifecycle cost | 26 (2020$), 175 years | C$ bn | NWMO_ProjectCosts | unverified |
| NFWA trust funds (Dec 2023) | 5.3 | C$ bn | NWMO_ProjectCosts | unverified |
| WTFN loan-to-equity | 0.70 (3.3% of budget) | C$ bn | WTFN_DNNP_2026 | unverified |
| OPG / ratepayer remainder of C$20.9 bn | 16.2 (78%) | C$ bn | calc | inputs unverified |
| CBoC jobs per 300 MW SMR: construction / operations | 1,600 / 200 | jobs/yr | CBoC_2021_SMR | unverified |
| Four-trade shortfall by 2030–31 | 76,950 | workers | Defence_FOI_Workforce; sum | unverified |
| AUKUS jobs | 20,000 over 30 years | jobs | JSCOT_224_Ch6 | unverified |
| Liddell workers at closure / moved to Bayswater | 180 / about 117 | workers | AGL_Liddell_Workforce | unverified |
| Power-weighted stance, Darlington / Liddell | +1.07 / −1.03 | −2 to +2 | analyst judgement | judgement |

## 10. Open gaps and P1 checks

1. **P1:** WTFN_DNNP_2026: date, structure, guarantee split, stake percentage.
2. **P1:** Barngarla_2023FCA809 paragraphs; the Kimba AEC result sheet; the 65% benchmark in a ministerial source.
3. **P1:** NWMO selection, Ignace hosting agreement (C$170 m / 81 years) and project costs (C$26 bn, C$5.3 bn).
4. **P1:** GriffithMonash_2025 method and wording; confirm Lowy has no 2025/2026 electricity question.
5. **P1:** Slovic 1987: the dread/unknown wording and nuclear's position, from the paper itself.
6. **P1:** the MSIFN "never consented" / 37 km wording (unconfirmed; do not quote until found).
7. Wonnarua position on nuclear at Liddell (none found); native title status of NC2013/006.
8. Any St Marys Cement role in DNNP (none found).
9. A union statement on DNNP itself (only Darlington licence renewal found).
10. OPG 3,700 jobs/yr vs CBoC 2,000 jobs/yr: resolve the scope before quoting either.
11. Current ANSTO staffing and Australian nuclear-engineering graduate numbers.
12. Whether Australia has any Indigenous loan-guarantee facility comparable to CILGC.

## 11. Interfaces (for the coordinator to add to plan §5; this run did not edit `plan.md`)

| From → to | What | Serves |
|---|---|---|
| Analyst run 6 → Victor / fact-checker | Open the P1 sources in §10 and set `verified: true` in `parameters_run6.yaml`; re-run `scripts/social_licence.py` | R1.4, R3.8 |
| Analyst run 6 → writer | §8.4 from §§3–4 and 7; §8.5 from §§5–6 with F8; §8.6 from §8. Lead each with its point; end each with what it means for C1 and Liddell | R3.5, R5.1 |
| Analyst run 6 → run 7 (MCDA) | Use the R1–R4 route scores (§8) as the social-licence criterion input, and the health-risk calc (§2 point 4) as a social/health criterion | R3.6, RB.8 |
| Analyst run 6 → Leroy | The 2040 Liddell start used for the health and carbon timing; confirm or replace | R3.4 |
| Conflict → Victor | OPG "3,700 jobs annually" vs CBoC 2023 "2,000 jobs a year" for DNNP | R1.3 |

## 12. Status by rubric ID

- **R3.3 (social):** polling against deaths per TWh, with the risk-perception explanation and a quantified health benefit by displaced source; First Nations consent compared across both sites; host communities; jobs. **Missing for HD:** verification; a Wonnarua position.
- **R3.4 (other):** workforce (both countries, numbers) and waste governance (NWMO vs Kimba/Muckaty/ARWA). **Missing:** verification; ANSTO and university pipeline numbers.
- **R3.5 (translation to practice):** every section states what helps or blocks building C1 and a Liddell SMR. **Missing:** carrying it into the written §8.4–8.6.
- **R3.6 / R3.7:** a scored, weight-tested comparison of four social-licence routes and a sequenced implementation pathway for both sites. **Missing:** integration with the §9 MCDA (run 7).
- **R3.8:** about 20 quantities with working. **Missing:** none verified; judgement scores must be labelled as such in the text.
- **R1.3 / R1.4:** Lowy vs Griffith–Monash reconciled; OPG vs CBoC flagged; mostly primary sources identified. **Missing:** primaries opened.
- **R5.2:** F8 drawn (numbered markers, no embedded title, source note). **Missing:** caption in the report.
