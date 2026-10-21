Rubric coverage: R1.3, R1.4, R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, R3.2, R3.4, R3.5, R3.6, R3.7, R3.8, R4.3, R5.2, R5.4, RB.5, RB.6; presentation rubric (visual 2%, teamwork 1%)

# Fact-check: §8.1, §8.3 and the slide deck (20/10/2026)

Fact-checker run, 20/10/2026. Scope:
- `01_Report/sections/8.1-law-regulation-licensing.md` (v1)
- `01_Report/sections/8.3-supply-concentration.md` (v1)
- `04_Presentation/deck-source/project/slides/*.html` (15 slides: on-slide text and `<aside>` speaker notes), checked against `00_Brief/presentation_rubric_text.txt`

The drafts were not edited.

## Method and access

- **Network.** No source could be opened. WebFetch failed at DNS (`ENOTFOUND`) for legislation.gov.au, classic.austlii.edu.au, justice.gov, world-nuclear.org, wnn.world-nuclear.org, pmc.ncbi.nlm.nih.gov, silex.com.au and archive.ourworldindata.org. Curl through the proxy returned no connection (code 000) for legislation.gov.au, ftc.gov, govinfo.gov, nrc.gov, canada.ca, aph.gov.au, concrete.org, ans.org, lowyinstitute.org, ourworldindata.org, pnas.org, en.wikipedia.org, parliament.nsw.gov.au, abc.net.au, newcastleherald.com.au, web.archive.org, iaea.org and osti.gov. The proxy log also shows earlier 403 denials for unece.org, ipcc.ch, nrel.gov and dcceew.gov.au.
- **Web search.** I ran WebSearch for alternative copies. Search summaries are recorded below as *leads* but never as verification. **No citation is marked "verified".** Every externally sourced claim is "unreachable (needs a human check)" unless the bibliography or our own results show a problem, which is marked separately.
- **Scripts.** I re-ran `hhi.py`, `displacement.py`, `schedule_value.py`, `same_money.py` and `law_timelines.py` with `python3 -I` from `03_LCA_Calculations`. All exit 0. All six result files are **byte-identical** to the versions before the run (diffed against a scratch copy). Every computed number below is checked against these outputs.
- **Status key.**
  - Citations: **verified**, **not supported**, **source not found**, **unreachable** (needs a human check).
  - Numbers and claims: **calc OK** (matches script output), **error** (wrong), **inconsistent** (differs across files), **overclaim**.

---

## A. §8.1 Law, regulation and licensing

| # | Claim (as drafted) | Citation | Status | Evidence | Suggested fix |
|---|---|---|---|---|---|
| A1 | "At Darlington, C1 needs **only** the regulator's acceptance of a concrete change in the Units 2–4 approval expected in 2028" | American Nuclear Society, 2026 | **not supported** (as worded) + unreachable | The sources.md entry (ANS_2026_Darlington) says only that approval to progress Units 2–4 is "expected in 2028". `parameters_run2.yaml` `units2to4_approval_year` note: "Whether this is a provincial approval, a CNSC licence amendment, or both is not stated." The section itself then says the obstacle is qualification (Canada paragraph), so "needs only" contradicts the section. | "At Darlington, C1 needs a qualified mix and acceptance of the design change before Units 2–4 are approved to proceed, a milestone expected in 2028 (ANS, 2026)." Replace ANS with the OEB filing (OPG_OEB_EB-2025-0297_D2-4-1) once opened. |
| A2 | "three laws bar any SMR, and **none can be repealed in this Parliament**" | Table T7 | **overclaim** | The NSW Act is a state law, and its repeal bill has passed the Legislative Council (row 3 of T7). Federal repeal fails only on *current* party positions: the ABC source says the Coalition has "no chance" **without Labor or the Greens changing position** (sources.md, ABC_2026_CoalitionEnergyPlan). | "…and on current party positions none will be repealed in this Parliament." |
| A3 | Federal repeal needs 39 Senate votes; pro-repeal bloc 32; Labor + Greens 40 | Parliament of Australia, 2026; Appendix B | **calc OK**; inputs unreachable | `law_timelines.csv`: majority 39, bloc 32, shortfall 7. Inputs: ALP 30 + Greens 10 = 40; 27 + 4 + 1 = 32; parts sum to 76 (asserted in the script). 39 assumes all 76 senators vote. A tie fails, so the opposing 40 is a blocking majority. | Add "(with all 76 senators voting)". Appendix B does not exist yet; add the csv rows to it. |
| A4 | One Nation and Babet in the "plausible pro-repeal bloc" | none | **source not found** | `parameters_run2.yaml` `senate_pro_repeal_max`: "One Nation's and Babet's voting intent is an assumption, not sourced." The law brief cites ABC, 31 Aug 2026 for One Nation (secondary, not in sources.md). Nothing is given for Babet. | Label it as an assumption in the text ("assuming One Nation and Senator Babet vote with the Coalition") or add sources. |
| A5 | Labor and Greens oppose repeal | Bowen, 2025; Australian Greens, 2025 | unreachable | Both are in sources.md. Bowen's date is TO VERIFY, and there is no 2026 Labor statement. | Add a 2026 Labor statement if one exists; confirm Bowen's date. |
| A6 | Coalition pledge to "repeal all legislative prohibitions" … "therefore **cannot pass**" | ABC News, 2026 | unreachable; **overclaim** | The quote matches the sources.md extract. "Cannot pass" is arithmetic on current positions only (see A2). The entry also says to pair it with Liberal_2026_EnergyPlan (primary). | "…cannot pass unless Labor or the Greens change position". Cite the Liberal Party page alongside the ABC. |
| A7 | ARPANSA licenses only Commonwealth-controlled bodies, so a private plant would fall to NSW | ARPANSA, n.d. | unreachable | Matches the sources.md extract (ARPANSA_WhoWeRegulate). The entry also asks for ARPANS Act s 13 ("controlled person") to be checked. | Add a citation to ARPANS Act s 13 once opened. |
| A8 | Route A (Commonwealth-owned plant, the Coalition's 2024 model) | ABC News, 2024 | unreachable | Matches the extract. The sources.md entry says it is "Secondary-weak … cite [the Coalition's 19 June 2024 release] instead". R1.4 says "No reliance on news and blogs". | Replace with the Coalition release (TODO 4 already lists this). |
| A9 | Federal override "risks a High Court challenge" | Canberra Times, 2025 | unreachable | Twomey_2025_Override: Partlett "warns of a High Court challenge". The date is TO VERIFY, and sources.md has two Canberra Times entries (2025 and n.d.). | Cite Constitution s 109 plus the named experts as quoted (as sources.md recommends). |
| A10 | "Our scoring (Appendix B) shows the ranking depends on whether speed or durability is valued more" | Appendix B | **source not found** (Appendix B not written) | The scoring exists only in law brief §5 (A 10 / B 7 / C 9 with regulator readiness doubled; A 8 / B 6 / C 11 with durability doubled). It is the analyst's judgement, "not a sourced score". | Move it to Appendix B and label it as our qualitative scoring. Needed for R3.6. |
| A11 | Licence to construct took 29.1 months | CNSC, 2025; 2026a | **calc OK**; inputs unreachable | `law_timelines.csv`: 29.1 months (31 Oct 2022 → 4 Apr 2025). Sensitivity 29.1–30.1 because CNSC gives only "October 2022". The application was "submitted in a number of packages over … several months". | Write "about 29–30 months" or "29 months", matching slide 10 ("29 months"). |
| A12 | "17.9 years after the environmental assessment began" | CNSC, 2026a | **calc OK**; unreachable | `ea_start_to_ltc_decision_years` = 17.9 (May 2007 → Apr 2025). The YAML notes this is elapsed time, not active review time. | Add "(elapsed, not continuous review)". |
| A13 | CSA cement standard "already allows calcined-clay blends with up to 15% limestone" | Hooton, 2023 | unreachable | Matches the extract: "CSA A3001/ASTM C595/AASHTO M240 allow Type IT cements with up to 15% limestone together with any SCM including calcined clay." These are secondary webinar slides with a truncated title. | Cite CSA A3001:23 (CSA_A3000_23) as the primary and Hooton as the commentary; complete the title. |
| A14 | "Slag blends have nuclear precedent" | [TODO: authors], 2026 | unreachable; **incomplete reference** | IJCSM_2026_NPPConcrete has no authors, and the journal is TO VERIFY. The extract supports "fly ash and GGBS are widely adopted in NPP concrete mixes". | Complete the reference from the DOI (s40069-026-00964-8). Until then, a Harvard citation with no author fails R5.4. |
| A15 | SC module design "the CNSC and US NRC **jointly accepted**" | GE-Hitachi Nuclear Energy, 2024; US NRC and CNSC, 2025 | unreachable; wording | The extract says the joint report finds the topical report "gives an acceptable way to meet both regulators' requirements". | "…whose design approach the CNSC and US NRC jointly reviewed and found acceptable". Use one author form for the CNSC throughout (see R5.4 below). |
| A16 | CSIRO's 2040 "earliest" date | Graham, Hayward and Foster, 2024 | unreachable; scope unconfirmed | A search lead (WNN/ESD News summaries of GenCost 2023-24) ties the 2040 statement to the report that first added **large-scale** nuclear. The SMR scope is not confirmed (the section's own TO VERIFY). The current edition is GenCost 2025-26 (sources.md csiro2026_gencost2526). | Confirm in the PDF whether the statement covers SMRs, and quote it. Decide which edition the report cites. |
| A17 | "a regulator in place **before sites are chosen**" | IAEA, 2015 | **not supported** (by the recorded extract) + unreachable | The IAEA_Milestones extract records only three phases, three milestones and 19 issues "including a legal framework and an independent regulator". Nothing on sequencing relative to site selection is recorded. The edition is uncertain. | Find the phase where the IAEA places the regulator and siting and quote it, or soften to "an independent regulator early in the programme (IAEA, [year])". |
| A18 | T7: EPBC s 140A (also ss 37J, 146M): the Minister "must not approve" a nuclear power plant | EPBC Act | unreachable | Matches the sources.md extract. The effect of the *Environment Protection Reform Act 2025* is unknown (Norton Rose Fulbright, 2025, also unreachable). | Human check P1 (checklist H1). |
| A19 | T7: ARPANS s 10: the CEO "must not issue a licence" | ARPANS Act | unreachable | Matches the extract: "the CEO must not issue a licence under section 32…". The search returned a 2011 compilation. | Human check P1 (H1). |
| A20 | T7: the 2022 repeal bill "was not passed" | Senate ECLC, 2023 | **not supported** (by the cited source) | The committee report *recommended* that it not be passed. The lapse comes from the Parliamentary Library (not cited), and the sources.md entry says "Confirm the lapse on the bill's ParlInfo page". | "The committee recommended against it (Senate ECLC, 2023) and it lapsed at prorogation (ParlInfo)." |
| A21 | T7: NSW Act s 8 "building or operating a reactor is an offence"; s 9 "no state authority may build or approve one" | NSW Act 1986 | unreachable; **incomplete** | The extract shows s 8(3) exceptions: the former AAEC and its **Commonwealth successors**, research and medical waste facilities, and nuclear vessels. ANSTO's reactor at Lucas Heights, NSW, operates under these. Section 9 says other Acts do not *authorise* a state authority to do so; the paraphrase is slightly stronger. TODO 2 already flags the s 8(3) question. | Add "(except the Commonwealth's ANSTO successor, s 8(3))". This matters for route A. |
| A22 | T7: NSW repeal bill passed the LC on 6 May 2026, stalled, lapses 28 Nov 2026 | Parliament of NSW, 2025–26; 2026 | unreachable | Matches the YAML (`nsw_repeal_bill_*`). The notice paper has a date inconsistency flagged in sources.md. | Check the latest LA notice paper. |
| A23 | T7: Ontario approved construction on 8 May 2025 | Ontario Power Generation, 2025 | unreachable; ambiguous key | "OPG 2025" could be OPG_2025_Q1 or opg_dnnp. The search lead (WNN, BLG) says Ontario approved "the first of four" SMRs. | Cite the Government of Ontario release (ontario2025_fid) and say "approved construction of the first unit". |
| A24 | T7: AGL "is building a battery on the site" | Newcastle Herald, 2024 | unreachable; possibly **out of date** | The sources.md extract says full operation is expected early 2026 (RenewEconomy). By October 2026 it may already be operating. The year is TO VERIFY, and it is a news source. | Check the battery's status; cite an AGL ASX release (TODO 4). |
| A25 | T7: CNSC licence valid to 31 March 2035; EA from May 2007; site licence 2012, renewed to 2031 | CNSC, 2021; 2025; 2026a | unreachable | All match `parameters_run2.yaml`. The "October 2022" date comes from CNSC 2026a, not CNSC 2025. | Cite (CNSC, 2025; 2026a) in that cell. |
| A26 | "Constitution s 109" | none in sources.md | **source not found** | It appears only inside the Twomey entry. | Add the *Commonwealth of Australia Constitution Act* s 109 to the references. |

## B. §8.3 Supply concentration and geopolitics

| # | Claim (as drafted) | Citation | Status | Evidence | Suggested fix |
|---|---|---|---|---|---|
| B1 | "**Every processing stage** at the front end of the BWRX-300 fuel chain is 'highly concentrated'" | Table T3 | **overclaim** | T3 covers mining, conversion and enrichment only. Fuel fabrication is not computed (supply brief, Gaps 7). Mining is highly concentrated by **country** (2,341) but **not by company** (1,118, range 851–1,384; `hhi_summary.csv`). | "Every front-end stage we measured (mining by country, conversion, enrichment) is…; fabrication was not assessed." |
| B2 | Threshold HHI > 1,800 "highly concentrated" | US DOJ and FTC, 2023 | unreachable | Matches USDOJ_FTC_2023. Search lead: law-firm summaries (Paul Weiss, Mondaq) describe a post-merger HHI "above 1,800" as highly concentrated. Not the primary. | Human check H-justice (quote §2.1 wording). |
| B3 | "**No sensitivity case falls below 1,800** (Appendix B)" (also in the T3 note) | results/hhi.md | **error** | `hhi_summary.csv` row "Mining (company), 2024 bounds": **1,118** (851–1,384), classed "not highly concentrated". | "No country-level or company-level case for conversion or enrichment falls below 1,800; mining by company (1,118) does, so mining risk is geopolitical, not market power." This is also a better R1.3/R2.7 point. |
| B4 | "Russia holds 42.8% of world enrichment capacity" | World Nuclear Association, 2025 | **calc OK**; unreachable | `hhi.py`: "Russia enrichment share 2025: 42.79%" = 29,133 / 68,077 kSWU. This is **our calculation** from the WNA table, not a WNA statement, and "2025" is the table's capacity column (it comes from a projection report). | "42.8% of 2025 enrichment capacity (calculated from WNA, 2025)". |
| B5 | Excluding Russia raises the HHI at every stage | Appendix B | **calc OK** | Mining 2,341 → 2,546; conversion 2,111 → 2,674; enrichment 3,009 → 3,599. | none |
| B6 | US ban's waivers end in 2028 | United States Congress, 2024 | unreachable | US_PL118_62: waivers end 1 January 2028; the ban sunsets 31 Dec 2040. The ban binds US imports, not Canada or Australia; the link to OPG is that GNF-A fabricates the fuel in the US. | Add that link in one clause, or say "as the US market will". |
| B7 | Without Russia and China: Urenco–Orano duopoly, HHI 5,621 | Appendix B | **calc OK** | Urenco 68.77%, Orano 29.82%, Other 1.41%; HHI 5,621. | none |
| B8 | OPG fuel chain: Saskatchewan uranium, Ontario conversion, Urenco USA and Orano enrichment, US fabrication; "no Russian stage" | Ontario Power Generation, 2023 | unreachable; **primary not identified** | The OPG_2023_fuel title, date and URL are all TO VERIFY. The only pointer is Power Engineering (trade press). | Find the OPG release (H-opg), or cite Power Engineering explicitly as secondary. |
| B9 | Australia 28% of identified recoverable resources (< USD 130/kgU) | OECD NEA and IAEA, 2025 | unreachable; **edition conflict** | The 28% (Red Book 2024) came via news reports. Red Book 2026 is now out: 29% or 27% in two WNA tabulations that do not reconcile (NEA_IAEA_2026). Slide 13 also says 28%. | Team decision (TODO 4). Name the edition and cost category, and keep the slide identical. |
| B10 | Australia mines 7.6% of world output | World Nuclear Association, 2026 | **calc OK**; unreachable | 4,598 / 60,213 = 7.64%; the 2024 rows sum exactly to 60,213 (internal check). | none |
| B11 | Enrichment and fabrication are barred by EPBC s 140A and ARPANS s 10 | Parliamentary Library, 2024 | unreachable; **duplicate reference** | Matches APH_2024. sources.md has two entries for the same URL with different titles: "Current prohibitions on nuclear activities in Australia: a quick guide" (StateBans_Summary) and "Nuclear activities prohibitions: a quick guide" (APH_2024). | Merge them into one entry with the title from the page. |
| B12 | "only the Coalition proposes lifting the bans (§8.1)" | §8.1 | **error** (inconsistent with §8.1 and the brief) | §8.1 counts One Nation (and Babet) in the pro-repeal bloc; the law brief records One Nation supporting repeal (ABC, 31 Aug 2026); the NSW repeal bill is a Libertarian private member's bill (John Ruddick MLC). | "Of the major parties, only the Coalition proposes…" |
| B13 | "The front end is reported to be nuclear power's largest source of life-cycle emissions" | UNECE, 2021 | **not supported** (by the sources.md entry) + unreachable | The unece2021 entry does not record this finding (TODO 3). Search lead: a Nucleation Capital summary says the fuel chain ("front-end") "contributes most"; the primary is unopened (unece.org 403). | Add the finding to sources.md once opened (page or figure). Until then the sentence and the R4.3 claim rest on a secondary. |
| B14 | "So fuel, not concrete, dominates both supply risk and footprint" | (inference) | **overclaim** (premature) | It depends on B13 and on Sam's Granta result, which does not exist yet (slide 7 placeholders). | "…is likely to dominate… (to be confirmed by §6)". |
| B15 | Silex laser re-enrichment of tails; commercialised in the US "**because** s 140A bars enrichment plants here" | [TODO: source needed] | **source not found** | There is no Silex or GLE entry in sources.md. Search lead (silex.com.au, WNN; unopened): GLE is 51% Silex, 49% Cameco; the NRC accepted the Paducah licence application for review in August 2025; GLE has a 2016 agreement for DOE tails. **No lead supports the causal "because s 140A".** | Add primaries (Silex ASX releases, NRC docket). Reword to "…is being commercialised in the US; s 140A would bar such a plant here." |
| B16 | Dual-source contracts reduce exposure but not HHI | (reasoning) | OK | Logical. It is consistent with HHI being a market measure. | none (but see slide 13, S20) |
| B17 | T3: all 18 values (HHI, shares, AU 7.6%, Canada 23.8%/20.2%) | hhi.py | **calc OK** | Every cell matches `hhi.md` §2–3 (Russia mining 4.547% → 4.5%; Canada 23.76% → 23.8%). | Add the year to "Conversion (capacity by company)": WNA table date TO VERIFY. |
| B18 | T3 note sensitivity ranges: enrichment 2,724–3,065; mining 2,246–2,370; conversion 2,015 | hhi.py | **calc OK** | Matches `hhi_summary.csv`. | Delete or fix "no case falls below 1,800" (B3). |
| B19 | T3 source years "WNA (2024; 2025; 2026)" | sources.md | unreachable | The WNA page years are all TO VERIFY. | Confirm the page dates (TODO 7). |

## C. Slide deck (on-slide text and speaker notes)

| # | Slide | Claim | Citation | Status | Evidence | Suggested fix |
|---|---|---|---|---|---|---|
| S1 | 1 cover | Speakers "Leroy Louis Jean · Sam · Victor Clarke" | — | OK, minor | Aaron removed (review item 7 done). Sam has no surname. | Add Sam's full name. |
| S2 | 2 problem | NSW 640 g/kWh vs nuclear 5–6 g life cycle | DCCEEW 2025; UNECE 2021 | unreachable; **boundary mismatch** | 640 is NGA scope 2 (combustion only, `displacement.md` caveat 1); 5.1–6.4 is life cycle. The UNECE title on the slide differs from sources.md (see S27). | Notes: "640 g at the power station". The comparison still holds. |
| S3 | 3 smr | 300 MWe | GEH 2021 | **inconsistent** (open) | sources.md OPG_OEB_EB-2025-0297_D2-4-1: "315 MW net per unit [TO VERIFY; conflicts with the deck's 300 MWe]". A search lead on the OEB filing (rds.oeb.ca) describes "a 300 MW … design". `displacement.py` sensitivity covers only 290–300 MWe. | Confirm 300 vs 315 net in the OEB filing. Add 315 to the sensitivity range. If 315: 2.48 TWh/yr, NSW about 1.58 Mt. |
| S4 | 3 smr notes | "it uses **more than half as much** concrete … per MW as its large ESBWR" | GEH 2021 | **error** (inverts the slide) | The slide says ">50% less concrete". "More than half as much" means more than 50% *of*. | "less than half as much concrete…". |
| S5 | 3 smr | GEH 2021 Alberta Innovates presentation | — | **source not found** | It is not in sources.md. | Add the entry with its URL. |
| S6 | 3 notes | "nobody has measured it yet" | — | overclaim | Unit 1 is under construction; unverifiable. | "not yet independently verified". |
| S7 | 4 darlington | "the **first G7 SMR** under construction" | none | **source not found** | There is no source in sources.md. | Cite OPG or Ontario wording, e.g. "first grid-scale SMR licensed for construction in the G7". |
| S8 | 4 darlington | "May 2025: **Ontario approves 4 units**, 1,200 MW, C$20.9 billion" | WNN 2025 | **error** | sources.md ontario2025_fid: approval "for OPG to start building the **first of four**". The C$20.9 bn is the four-unit budget. §8.1 says Units 2–4 approval is expected in **2028**. | "May 2025: Ontario approves Unit 1; C$20.9 bn budget for all 4 units (1,200 MW)". |
| S9 | 4 darlington | "End 2029: Unit 1 commercial operation" | WNN/NucNet | **inconsistent** | `displacement.py`, `schedule_value.py` and `same_money.py` all start Darlington U1 in **2030**. sources.md opg_dnnp: grid connection end-2030 (Q1 2025 release), others end-2029; OEB extract: in-service **October 2030** [TO VERIFY]. Verdict Q5 also uses end-2029. | Pick one date from OPG's OEB filing and use it on slides 4 and 14 and in the YAML. |
| S10 | 4 darlington | About C$17 million per MW | calc | **calc OK** | 20.9 bn / 1,200 MW = C$17.4 m/MW. | none |
| S11 | 4 darlington | "the **only** real cost and schedule benchmark the West has" | — | overclaim | NuScale/UAMPS (slide 11) is another Western cost data point. | "the first Western SMR with a construction budget and licence". |
| S12 | 4 darlington | Sources: WNN (2022, 2025); NucNet (2025) | — | **source not found** | None is in sources.md. All are news sources (R1.4). §8.1's changelog says CNSC replaces NucNet. | Cite CNSC (2025; 2026a), OPG (2025) and Government of Ontario (2025). |
| S13 | 5 proposal | "about **[__] m³** of concrete per unit" | — | **placeholder** | Not filled. Visible on screen. | Sam to fill before Thursday, or remove the clause. |
| S14 | 5 proposal + notes | "Unit 1's concrete is already in" | — | overclaim | sources.md: the basemat is in place (ANS, June 2026); RHP-1 (foundation) was lifted 30 Mar 2026. Not all Unit 1 concrete (module infill, shafts) is shown to be placed. | "Unit 1's basemat is already poured". |
| S15 | 5 notes | "qualify under Canada's nuclear concrete standards" | — | inconsistent (mild) | §8.1/sources.md: DP-SC infill follows the GEH topical report (AISC N690 and ASME), and N287 is for *concrete* containment. | "qualify under the BWRX-300's licensed design codes". |
| S16 | 6 lca-method notes | "where our **ash-concrete** change acts" | — | **error** | The initiative is LC3 (calcined clay and limestone), not fly ash (README, plan D1). | "our LC3 concrete change". |
| S17 | 6 lca-method | "Material quantities from OPG Darlington construction data" | — | overclaim | review.md items 2–4: the data cover the forebay shaft only (partial). | "partial quantities (forebay shaft) scaled to…", or state the source of the whole-plant quantities. |
| S18 | 7 lca-results | "[Sam: __ g] · LC3 saves [__] t" | — | **placeholder** | Not filled. Notes tell the speaker to say "likely 1% or less" before any result exists (plan §2.3 estimate). | Fill from Granta, or show "result pending" and drop the 1% prediction. |
| S19 | 7 lca-results | Coal 751–1,095; gas 403–513; nuclear 5.1–6.4 g/kWh | UNECE 2021 | unreachable | sources.md unece2021: nuclear 5.1–6.4 and NGCC 403–513 agree across outlets. Coal is "751 (IGCC, USA) or 753 to 1095 depending on the outlet", so the low end is uncertain. | Human check H-unece. |
| S20 | 8 materials-rd + verdict Q2 | LC3 "qualifies under Canada's **CSA N287**" | — | **inconsistent** with §8.1 | sources.md CSA_N287_N291: N287 covers concrete containment; the BWRX-300 containment is steel-plate composite. GEH_NEDO33926: infill follows draft AISC N690. | "qualifies under the codes accepted for the BWRX-300's steel-composite modules (AISC N690, CSA N291)". |
| S21 | 8 materials-rd | SILEX laser re-enrichment; US commercialisation; "where the fuel chain emits the most" | none | **source not found** | Same as B13 and B15. README lists this for Victor to verify. | Add the Silex/GLE primary; hedge "reported to emit the most". |
| S22 | 8 materials-rd | SMRs "2–30× more waste by volume per unit of energy" | Krall, Macfarlane and Ewing (2022) | **source not found** in sources.md; unreachable | Search lead (Stanford release, PNAS abstract via search): "factors of 2 to 30 for the reactors in our case study" (NuScale, IMSR, 4S). It is specific to those designs, not the BWRX-300. PNAS 119(23) e2111833119 matches the slide's references. | Add the entry to sources.md. Say "for the three designs studied". |
| S23 | 9 location | NSW 1.5 Mt/yr; Ontario 0.07–0.16 Mt; 2.37 TWh | calc | **calc OK** | `displacement.md` §2: 1,500,128 t; 69,182 t (35 g); 160,952 t (73.8 g); 2,365,200 MWh. | none |
| S24 | 9 location (title and notes) | "about 10× more"; notes "9 to 20 times less" | calc | minor | Ratios: 9.3× (73.8 g) to 21.7× (35 g). | Title "at least 9× more"; notes "9 to 22 times". |
| S25 | 9 notes | Marginal: "0.8 to 1.1 Mt … the gap shrinks to about 2 times" | calc | minor | 797,664 t (343 g) and 1,102,774 t (472 g) give ratios of 1.9× and 1.4×. The 343 g factor's definition is ambiguous (taf2025). | "to about 1.4–1.9 times". |
| S26 | 9 notes | Liddell to 2050: 0.6 Mt (coal gone by 2038) to 3.8 Mt (slower) | calc | **calc OK** | 631 kt (T1, start 2040) and 3.81 Mt (T2). | none |
| S27 | 9 location (source line) | "Ontario Government (2024), TAF (2025)"; range 35–74 g | — | **source not found / inconsistent** | The 35 g value is the CER (cer_ontario_profile, 2022), which is not cited on the slide or on slide 15. The Ontario snapshot is "n.d." in sources.md and gives 53 g, which is not used. TAF is missing from slide 15. | Cite CER (n.d.) and TAF (2025); drop the Ontario snapshot or give it its year. |
| S28 | 9 location vs verdict Q5 | "couldn't run before about **2040**" vs Q5 "realistically the **late 2030s** at the earliest" | — | **inconsistent** | §8.1 treats CSIRO's 2040 as optimistic. Q5 contradicts slide 9 and §8.1. | Q5: "2040 at the earliest (CSIRO), probably later". |
| S29 | 10 law | "Nuclear power is illegal in Australia today" | Acts | wording | Federal law bars approval and licensing; only state laws create offences. | "Nuclear power is banned in Australia today". |
| S30 | 10 law | "NSW Act 1986, s8: Bans **any** nuclear reactor in NSW" | NSW Act | **error** | The s 8(3) exceptions cover the AAEC's Commonwealth successors (ANSTO's Lucas Heights reactor is in NSW) and research and medical facilities (sources.md NSW_UMNFP_Act_1986). | "Bans nuclear power reactors in NSW, including at Liddell". |
| S31 | 10 law | 29 months; LC passed May 2026, stalled in LA; Labor and Greens oppose | CNSC 2025 etc. | calc OK; unreachable | Consistent with §8.1 and `law_timelines.csv`. | none |
| S32 | 10 law | The analyst's correction "site owner added as barrier" | — | **not applied** | §8.1's changelog says the deck corrections include the site owner; slide 10 and its notes do not mention AGL. | Add one line to the notes: "and the site owner, AGL, has ruled nuclear out at Liddell". |
| S33 | 11 cost | "CSIRO GenCost 2024–25: highest cost … even with Darlington's real costs" | CSIRO 2025 | unreachable; **superseded edition** | sources.md csiro2026_gencost2526: the 2025-26 final (15 July 2026) is "the current edition, which should be the one the report cites"; SMRs remain highest cost. | Cite GenCost 2025-26, or say why 2024-25 is used. |
| S34 | 11 cost | NuScale: $58 → $89/MWh; 462 MW; cancelled 2023; US$232M | Power Engineering 2023; WNN 2025 | **source not found** in sources.md; unreachable | No NuScale entry exists. Search lead (Power Engineering, E&E News; unopened): +53% from $58 to $89, 6 × 77 MW = 462 MW, DOE "$232 million since 2020". E&E gives $55, not $58. The $89 included IRA credits [check]. | Add entries (prefer UAMPS/NuScale filings or DOE). Confirm whether $89 includes IRA subsidies. |
| S35 | 11 cost | "as Ontario and Canada are doing for Darlington" | WNN 2025 | **source not found** | WNN 2025 is not in sources.md. The primary exists there: CGF_BOF_2025 (C$2 bn + C$1 bn equity); CIB_2022_Loan (C$970 m). | Cite CGF and BOF (2025) and CIB (2022). |
| S36 | 12 social | 61% support, 37% oppose (Lowy 2024) | Lowy Institute 2024 | **source not found** in sources.md; unreachable | Search lead: Lowy chart, 2024 = 27% strongly + 34% somewhat support, 17% + 20% oppose. No 2025 or 2026 electricity result surfaced. | Add the entry; check poll.lowyinstitute.org for a newer year. |
| S37 | 12 social | 0.03 deaths/TWh nuclear vs 24.6 coal | OWID 2024 | **source not found** in sources.md; unreachable | Search lead confirms 0.03 for nuclear; 24.6 was **not** found in leads. OWID draws on Markandya and Wilkinson (2007) and Sovacool et al. (2016). | Human check of the coal figure (README already asks). Add the entry and cite the underlying papers too. |
| S38 | 13 supply | 28%; 43% (42.8%); HHI ≈ 3,000 > 1,800; mining 2,341, conversion 2,111 | NEA/IAEA 2025; WNA 2025 | **calc OK**; unreachable | Matches §8.3 and `hhi.md`. The threshold correction to 1,800 is applied. | Keep it identical to §8.3 once B9 is decided. |
| S39 | 13 notes | "3,600 if Russia is excluded, **because the rest is essentially just Urenco and Orano**" | calc | **error** | Without Russia, CNNC still holds 35.4% (3,599). The Urenco–Orano duopoly is the without-Russia-**and-China** case (5,621). | "3,600 without Russia, and 5,600 once China is also excluded, when it is essentially Urenco and Orano". |
| S40 | 13 supply | "Solution: long-term contracts with allied enrichers" | — | inconsistent framing | §8.3: such contracts "reduce a buyer's exposure but not the HHI". | "Mitigation: …". |
| S41 | 13 references | "World Nuclear Association, 2025. Conversion and Enrichment" | — | **source not found** (title) | The WNA pages are "Uranium Enrichment" and "Conversion and Deconversion". | Correct the titles and list both. |
| S42 | 14 verdict notes | "Darlington's **C$20.9 billion** (about A$23 billion) would buy roughly **5 times** the energy … (1.3 times in the worst case)" | same_money.md | **error** | 5.0× and 1.3× are **Method B** (GenCost LCOE ratio A$514 / A$102; worst case 198/153). Darlington's C$20.9 bn is **Method A**, which gives **2.0×** (four units) to 2.9× (Unit 1 + common), on capital charge only. A$23.39 bn is correct. | "At GenCost costs the same spend buys about 5× the energy as firmed renewables (1.3× in the worst case); on Darlington's own capital, about 2×." |
| S43 | 14 verdict | "Environmental: **Strong**"; title "Strong for the climate"; notes "SMRs are a strong climate option for Australia" | same_money.md, displacement.md | not supported by our own results | `same_money.md`: "in **every** tested Liddell case the same money spent on firmed renewables avoids more CO₂e by 2050 than one SMR" (5.0× to 48.8×). Liddell avoids only 0.6–3.8 Mt to 2050. | "Strong per kWh, weak per dollar and too late". The rating should follow the MCDA (R3.6, R2.6). |
| S44 | 14 verdict Q2 | CSA N287 | — | inconsistent | See S20. | As S20. |
| S45 | 14 verdict Q5 | Licensing 2.5 yr; construction "about 4.5 years" (Apr 2025 → end 2029) | calc | calc OK / inconsistent | 29.1 months ≈ 2.4 yr. Apr 2025 → end 2029 is about 4.7 yr, and about 5.5 yr if the in-service date is Oct 2030 (S9). | "about 5 years". Fix the start-date question (S9) and 2040 (S28). |
| S46 | 15 references | Format and completeness | — | R5.4 | Not alphabetical (Power Engineering after Scrivener; the Acts last). No URLs or access dates. Missing: TAF, CER, CNSC, Ontario release, CGF/BOF. Uses the news sources NucNet and WNN. "CSIRO, 2025" vs the Graham, Hayward and Foster author form in §8.1. "Ontario Government, 2024" vs n.d. in sources.md. | Rebuild from sources.md in Harvard form (style guide). |
| S47 | 14 verdict | "same money buys about 5× the energy" (on slide) | same_money.md | calc OK | Method B 5.0×. | Add "at GenCost costs". |

## D. Cross-document consistency

| Quantity | §8.1 / §8.3 | Slides | Results / YAML | Verdict |
|---|---|---|---|---|
| Net output per unit | — | 300 MWe (slides 3, 5, 9) | 300 (`displacement.py`; sensitivity 290–300); OEB extract 315 [TO VERIFY] | **Open.** Confirm, then add 315 to the sensitivity. |
| NSW avoided, one unit | — | 1.5 Mt (slides 9, 14) | 1,500,128 t | Consistent |
| Ontario avoided | — | 0.07–0.16 Mt | 69,182 – 160,952 t | Consistent (CER source missing on slide) |
| Russia's enrichment share | 42.8% | 43% on-slide; 42.8% notes | 42.79% | Consistent |
| Enrichment HHI | 3,009 | ≈ 3,000 | 3,009 | Consistent |
| Without-Russia story | duopoly = without Russia **and China** (5,621) | notes: duopoly = without Russia (3,600) | 3,599 / 5,621 | **Inconsistent** (S39) |
| "No case below 1,800" | §8.3 text and T3 note | — | mining by company 1,118 | **Error** (B3) |
| LTC duration | 29.1 months | 29 months; 2.5 years | 29.1 (29.1–30.1) | Consistent within rounding |
| Budget | — | C$20.9 bn; C$17 m/MW; A$23 bn | C$20.9 bn; A$23.39 bn | Consistent |
| What Ontario approved, May 2025 | "approved construction" | "approves 4 units" | sources: first of four | **Slide wrong** (S8) |
| Unit 1 start | — | end-2029 (slides 4, 14) | 2030 in all three scripts | **Inconsistent** (S9) |
| Earliest Australian SMR | CSIRO 2040, treated as optimistic | slide 9: ~2040; Q5: late 2030s | Liddell start 2040 central | **Inconsistent** (S28) |
| Australia's uranium share | 28% (< USD 130, RB 2024) | 28% | 28 (RB 2024); 29/27 (RB 2026) | Consistent, but edition undecided |
| Who supports repeal | §8.1: Coalition + One Nation + Babet; §8.3: "only the Coalition" | — | YAML: bloc 32 | **Inconsistent** (B12) |
| Qualification code for LC3 | §8.1: GEH topical report / AISC N690 | slides 5, 8, 14: CSA N287 | sources.md CSA_N287_N291 | **Inconsistent** (S15, S20) |
| UNECE title | — | "Life Cycle Assessment of Electricity Generation Options" (2021) | sources.md: "Carbon Neutrality in the UNECE Region…" | **Inconsistent.** A search lead confirms both titles exist (2021 report; 2022 book). Pick one. |

## E. Benchmarks (check 3)

- **Life-cycle values.** The deck's nuclear range (5.1–6.4 g/kWh, UNECE) sits inside the IPCC AR5 range (3.7–110, with sources.md noting this is *not confirmed*). The UNECE coal range (751–1,095) and NGCC range (403–513) are UNECE's own. Sam's BWRX-300 value is missing, so it can't yet be benchmarked (RB.6 open).
- **Cost.** The capital-only LCOE in `same_money.md` is A$199/MWh at 7% over 30 years. GenCost's full SMR LCOE is A$387–641/MWh (2023-24, secondary). The script flags this as a cross-check only, because O&M and fuel are not sourced. It is not used on the slides. No out-of-range result is stated without explanation.
- **HHI.** No published benchmark exists. The secondary range of 40–44% for Russia's enrichment share brackets 42.8% (supply brief R1.3).

## F. Presentation rubric (things that would cost marks on Thursday)

1. **Visual communication (2%): "without unnecessary text or clutter. Effective use of figures, images".** Two slides show raw placeholders ("[__] m³", "[Sam: __ g]", "[__] t"). No slide contains an image or SVG (`grep <img|<svg` finds nothing). Only slide 7 has a to-scale bar chart. Before Thursday, fill or remove the placeholders. Add at least a BWRX-300 or Darlington image (credited) and turn slides 9 and 13 into bar charts (the displacement and HHI numbers are ready).
2. **Teamwork (1%): "All members contribute effectively".** Note timings are Leroy about 4.75 min (slides 1–5), Sam about 3.5 min (6–8) and Victor about 6 min (9–14), for a total of about 14.25 min (within 15). The split is uneven. Consider moving slide 13 (supply) or slide 9 (location) to Sam, or giving Sam the verdict's environmental row.
3. **Engagement and Q&A.** The prepared answers Q2 (CSA N287) and Q5 (late 2030s; 4.5 years) contradict the report (S20, S28, S45). A wrong answer under questioning costs marks in the teamwork and response criterion.
4. **Consistency.** The numbers spoken in the notes must match the slide: S4 (concrete), S39 (HHI), S42 (5×).

## G. Rubric evidence (check 5): what each section claims vs what is there

**§8.1** claims R3.2, R3.4, R3.5, R3.7, R1.4 (supports R3.6, R3.8, R1.2, RB.2).
- **R3.2** ("comprehensive and detailed discussion of the major … political … factors"). Present: three bans, Senate arithmetic, Labor, Greens, Coalition and NSW positions, override route. Gaps: One Nation and Babet intent unsourced (A4); no 2026 Labor statement; "cannot pass" overclaims (A2, A6). **Partial.**
- **R3.4** (regulation and licensing timelines). Present: CNSC durations, recomputed correctly. Gaps: no Units 2–4 review time; the 2028 milestone is secondary and its type is unknown (A1). Workforce and waste governance are not in §8.1 (they must be elsewhere for R3.4). **Partial.**
- **R3.5** (framed as translation to practice). The lead and closing paragraphs do this, but the lead's "needs only" contradicts the body (A1). **Met once A1 is fixed.**
- **R3.7** ("implementation issues and non-technical solutions"). Present: mock-up qualification, S1 fallback, the Australian action list. The comparison is deferred to §8.6, which is not yet written. **Partial.**
- **R1.4** ("primary sources … No reliance on news"). Primaries are cited, but **none is verified**. Load-bearing claims still rest on ABC (A6, A8), Canberra Times (A9), Newcastle Herald (A24) and ANS (A1). **Not yet evidenced.**
- **R3.6** ("strong evaluation and comparison of solutions"). The route scoring is claimed in Appendix B, which does not exist (A10). **Missing.**
- **R5.4.** Incomplete citation (A14); ambiguous OPG 2025 key (A23); author forms are mixed ("CNSC" vs "US NRC and CNSC" vs the full names in sources.md); Constitution missing (A26). **Not met.**

**§8.3** claims R3.2, R3.8, R2.1, R4.3, R3.5, R3.7 (supports R1.3, R2.7, R3.6).
- **R2.1 / R3.8** ("strong quantitative analysis"). Present: Table T3 with reproducible values, all calc OK. Gaps: the inputs are unverified (`verified: false` throughout `parameters_run3.yaml`); B3 is a factual error in the summary of the sensitivity. **Partial until the inputs are verified and B3 is fixed.**
- **R2.7** ("uncertainties … realistically estimated"). Present: the sensitivity ranges. The capacity-vs-supply and CNNC-estimate limits (`hhi.md` §5) are not mentioned in the section. **Partial.**
- **R4.3** ("new feasible connections"). Both legs are currently unsupported: the UNECE front-end finding (B13) and Silex/GLE (B15). **At risk.**
- **R3.2.** Present: geopolitics and sanctions. B12 is an error. Kazakh routes and Rosatom stakes are missing. **Partial.**
- **R3.5.** Darlington vs Liddell framing present. **Met.**
- **R3.7.** Dual sourcing and its limit, then a pointer to §8.6. **Partial.**
- **R1.3** ("disagreements between sources explained"). The Red Book 2024 vs 2026 conflict and the Rosatom capacity spread (WNA vs CRAI) are in the brief but not in the section. **Partial.**

**Slides** (support R5.2 and the presentation rubric). Errors S8, S16, S30, S39 and S42 and placeholders S13 and S18 must be fixed before submission.

---

## Summary

**Counts by status.** Tables A–C have 92 rows. Each row is counted once, under its most serious status. Rows with a substantive problem are usually also unreachable.

| Status | Count | Rows |
|---|---:|---|
| Verified (citation opened and confirmed) | **0** | Network blocked every primary host |
| Unreachable (needs a human check), no other problem found | 21 | A5, A7, A8, A9, A13, A16, A18, A19, A21, A22, A23, A24, A25, B2, B6, B9, B11, B19, S2, S19, S33 |
| Not supported (by the cited or recorded source, or by our own results) | 5 | A1, A17, A20, B13, S43 |
| Source not found (not in sources.md, or reference incomplete) | 17 | A4, A10, A14, A26, B8, B15, S5, S7, S12, S21, S22, S27, S34, S35, S36, S37, S41 |
| Calc or logic OK (re-run matches the text) | 17 | A3, A11, A12, B4, B5, B7, B10, B16, B17, B18, S1, S10, S23, S26, S31, S38, S47 |
| Error (factually or arithmetically wrong) | 8 | B3, B12, S4, S8, S16, S30, S39, S42 |
| Inconsistent (across section, slides and results) | 9 | S3, S9, S15, S20, S28, S32, S40, S44, S45 |
| Overclaim or wording | 12 | A2, A6, A15, B1, B14, S6, S11, S14, S17, S24, S25, S29 |
| Placeholder on slide | 2 | S13, S18 |
| Format (R5.4) | 1 | S46 |
| **Total** | **92** | |

**Blocking issues**
1. **No citation in §8.1, §8.3 or the deck is verified.** Every primary host is blocked from this environment. Victor must open the P1 items in the Human checklist before the examiner can mark anything HD (CLAUDE.md rule 3).
2. **B3:** "No sensitivity case falls below 1,800" is false (mining by company, 1,118). It appears in the §8.3 text and the T3 note.
3. **B15 / S21:** Silex/GLE has no source, and the causal "because s 140A" is unsupported. The §8.3 R4.3 claim and slide 8 depend on it.
4. **B13 / B14:** the UNECE front-end finding is not recorded in sources.md, and "fuel dominates footprint" pre-empts Sam's LCA.
5. **A1:** §8.1's lead sentence ("needs only…") is unsupported and contradicts the section body.
6. **A10:** Appendix B (Senate arithmetic, route scoring, HHI working) is cited but does not exist.
7. **Slides (Thursday):** S8, S42, S30, S39, S16, S4, S20/S44, S28, S9, and the placeholders S13 and S18.

---

## Human checklist (open these yourself; P1 = needed before Thursday's slides or blocking for §8.1/§8.3)

Each item gives the URL, the claim, and **the value to confirm**. Hosts in **bold** were blocked from this environment.

### **legislation.gov.au** / **classic.austlii.edu.au** (blocked: DNS)
- **P1** https://www.legislation.gov.au/C2004A00485/latest/text : EPBC Act s 140A(1)(b). Confirm "The Minister must not approve an action consisting of or involving the construction or operation of … (b) a nuclear power plant". Note the compilation date, and whether the *Environment Protection Reform Act 2025* amended or renumbered it. Check that ss 37J and 146M exist as described. Mirror: https://classic.austlii.edu.au/au/legis/cth/consol_act/epabca1999588/s140a.html
- **P1** https://www.legislation.gov.au/C2004A00383/latest/text : ARPANS Act s 10(2). Confirm "the CEO must not issue a licence under section 32 in respect of any of the facilities mentioned in subsection (1)". Check s 13, "controlled person" (A7). Mirror: https://classic.austlii.edu.au/au/legis/cth/consol_act/arpansa1998487/s10.html

### **legislation.nsw.gov.au**
- **P1** https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1986-194 : s 8(1), (2) and (3) exceptions (AAEC and Commonwealth successors), and s 9. Confirm whether "bans any nuclear reactor" (slide 10) is wrong given s 8(3) (S30), and whether conversion is covered (§8.3 TODO 5).

### **parliament.nsw.gov.au** / files.parliament.nsw.gov.au
- **P1** https://www.parliament.nsw.gov.au/bills/Pages/bill-details.aspx?pk=18833 : repeal bill passed the LC on **6 May 2026**; status "In Legislative Assembly".
- https://files.parliament.nsw.gov.au/fileapi/ParlFiles/GetArtifact/170%20NOM%20(combined).pdf?serverRelativeUrl=%2Fhp%2Fhousepaper%2F31312%2F170+NOM+%28combined%29.pdf : "lapses **28 November 2026**". Check that this is the latest notice paper.

### **aph.gov.au**
- **P1** https://www.aph.gov.au/Senators_and_Members/Senators/Senate_composition : ALP **30**, Coalition **27**, Greens **10**, One Nation **4**, plus 5 others = **76**. Note any change after 14/05/2026.
- https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Quick_Guides/2023-24/NuclearActivitiesProhibitions : the exact title (B11); s 140A and s 10 cover fabrication, power, enrichment and reprocessing, and **not conversion**.
- https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Nuclearprohibitions : the committee recommended the 2022 bill **not be passed** (tabled 11 Aug 2023). Then confirm the lapse on the bill's ParlInfo page (A20).

### **cnsc-ccsn.gc.ca** / **canada.ca**
- **P1** https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html : licence issued **4 April 2025**, **1** BWRX-300, valid to **31 March 2035**.
- **P1** https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/ (and /project-timeline/) : EA began **May 2007**; LTC application **October 2022** (which day?); site licence **17 Aug 2012**.
- https://www.canada.ca/en/nuclear-safety-commission/news/2021/10/cnsc-renews-ontario-power-generations-site-preparation-licence-for-its-darlington-new-nuclear-project.html : renewed to **11 October 2031**.
- https://www.cnsc-ccsn.gc.ca/eng/reactors/regulatory-hold-points/new-reactors/ : RHP-1 lifted **30 March 2026**.

### **opg.com** / newswire.ca / **news.ontario.ca** / rds.oeb.ca
- **P1** https://files.opg.com/wp-content/uploads/2026/05/D2-04-01-Darlington-New-Nuclear-Project-Overview_Updated_20260521_260522_191835.pdf : net MW per unit (**300 or 315**, S3); Unit 1 in-service date (**end-2029 or Oct 2030**, S9); the Units 2–4 approval step and year (**2028**, A1).
- **P1** https://www.opg.com/news-resources/newsroom/release/opg-reports-2025-first-quarter-financial-results/ : **C$20.9 bn** for four units; Unit 1 **C$6.1 bn** + **C$1.6 bn** common; Ontario's approval on 8 May 2025 was for the **first unit** (S8).
- news.ontario.ca: find the 8 May 2025 release (URL unknown) and confirm "first of four".
- OPG fuel-supplier release, 2023 (URL unknown; pointer https://www.power-eng.com/nuclear/smrs/opg-selects-first-fuel-suppliers-for-its-small-modular-reactors/): Cameco, Urenco USA, Orano, GNF-A, and the minister's quote (B8).

### **nrc.gov**
- https://www.nrc.gov/docs/ML2411/ML24110A134.pdf : NEDO-33926 Rev 2 §5.2.1 "self-consolidating concrete"; §6.2.1 concrete infill, any cement-type limits.
- https://www.nrc.gov/docs/ML2532/ML25325A075.pdf : the joint report's wording, "acceptable", not "accepted" (A15).

### **world-nuclear.org** (blocked: DNS)
- **P1** https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment : 2025 capacity Rosatom **29,133**, Urenco **17,300**, CNNC **13,789**, Orano **7,500**, Other **355** kSWU (gives **42.8%** and HHI **3,009**); also the 2022 and 2030 rows; the page date.
- **P1** https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/conversion-and-deconversion : Cameco 12,500; CNNC 15,000; ConverDyn 7,000; Orano 15,000; Rosatom 12,500 tU (HHI **2,111**); table date.
- **P1** https://world-nuclear.org/information-library/nuclear-fuel-cycle/mining-of-uranium/world-uranium-mining-production : 2024 rows (Kazakhstan 23,270; Canada 14,309; Australia **4,598**; world **60,213**); company table year.

### **oecd-nea.org**
- **P1** https://www.oecd-nea.org/jcms/pl_103179/uranium-2024-resources-production-and-demand : Australia **28%** of identified recoverable resources at < USD 130/kgU (table number).
- https://www.oecd-nea.org/jcms/pl_121658/uranium-2026-resources-production-and-demand : Australia's share (29% or 27%?) and cost category (B9).

### **justice.gov** / govinfo.gov
- **P1** https://www.justice.gov/d9/2023-12/2023%20Merger%20Guidelines.pdf : the exact words "greater than 1,800" and "highly concentrated", with section number (§2.1).
- https://www.justice.gov/atr/horizontal-merger-guidelines-08192010 §5.3 : > 2,500 highly concentrated.
- https://www.govinfo.gov/content/pkg/PLAW-118publ62/pdf/PLAW-118publ62.pdf : waivers end **1 January 2028**; sunset **31 Dec 2040**.

### **unece.org**
- **P1** UNECE (2021) *Life Cycle Assessment of Electricity Generation Options* (find the PDF on unece.org): nuclear **5.1–6.4** g/kWh; NGCC **403–513**; coal low end **751 or 753** to **1,095**; whether the **fuel-chain front end** is the largest share of nuclear's emissions (B13). Settle the title against the 2022 book.

### **csiro.au**
- **P1** https://www.csiro.au/-/media/Energy/GenCost/GenCost2023-24Final_20240522.pdf : does "deployment from **2040** at the earliest" cover SMRs? Also the 2030 SMR LCOE **A$387–641/MWh**.
- https://www.csiro.au/-/media/Energy/GenCost-2025-26-Final/GenCost_2025-26_Final_Report_20260715.pdf : is the SMR still the highest cost (slide 11)? Get the SMR and firmed-VRE 2030 values to replace A$514 and A$102.

### Other Australian sources
- **P1** https://www.dcceew.gov.au (NGA Factors 2025; URL TODO): NSW/ACT scope 2 = **0.64** kg CO₂e/kWh (slides 2, 9).
- https://www.arpansa.gov.au/regulation-and-licensing/regulation/about-regulatory-services/who-we-regulate : "controlled persons" only (A7).
- https://www.abc.net.au/news/2026-09-23/coalition-energy-plan-scrap-renewables-climate-laws/107184376 : "repeal all legislative prohibitions"; "no chance" without Labor or the Greens.
- https://www.liberal.org.au/our-plan/energy : the Coalition's own wording (replacement for the ABC).
- https://www.newcastleherald.com.au/story/8557276/agl-says-liddell-site-will-not-be-used-for-nuclear-power : the Nicks quote; year; battery status (A24).
- https://www.canberratimes.com.au/story/8851241/duttons-nuclear-power-plan-faces-legal-hurdles/ : Twomey and Partlett; date.

### Canada and Ontario grid (slide 9)
- https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/provincial-territorial-energy-profiles/provincial-territorial-energy-profiles-ontario.html : **35** g/kWh (2022).
- https://carbon.taf.ca/2024/electricity-grid : **73.8** g/kWh (2024). https://taf.ca/custom/uploads/2025/10/2025TAF-EmissionsFactors.pdf : marginal **343** (and its definition).

### Slide-only sources (P1 for Thursday)
- **P1** https://poll.lowyinstitute.org/charts/australia-using-nuclear-power-to-generate-energy/ : 2024 **61%** support / **37%** oppose; check whether a 2025 or 2026 value exists.
- **P1** https://ourworldindata.org/safest-sources-of-energy : coal **24.6**, nuclear **0.03** deaths/TWh; underlying sources.
- **P1** https://www.power-eng.com/nuclear/smrs/facing-mounting-costs-nuscale-cancels-small-modular-reactor-project-in-utah/ : **$58 → $89/MWh**; **462 MW**; cancelled Nov 2023; DOE **US$232 m**; whether $89 includes IRA credits.
- https://www.pnas.org/doi/10.1073/pnas.2111833119 : "factors of **2 to 30**", per unit of energy, for which designs.
- https://doi.org/10.1016/j.cemconres.2017.08.017 : Scrivener et al. (2018), CCR 114, pp. 49–56 (reference details).
- **P1** https://www.silex.com.au/silex-technology/global-laser-enrichment/ : GLE **51% Silex / 49% Cameco**; Paducah application accepted by the NRC (Aug 2025). This is needed for B15 and slide 8. Add the NRC docket page as well.
- GE Hitachi (2021) Alberta Innovates BWRX-300 presentation (URL unknown): ">50% less concrete per MW vs ESBWR".
- https://www.ans.org/news/2026-06-05/article-8047/north-american-construction-is-back-smaller-and-faster-at-opgs-darlington/ : Units 2–4 milestone "expected in 2028"; basemat status (S14).
- https://www.concrete.org/portals/0/files/pdf/webinars/ws_F23_NEU_DouglasHooton.pdf : "up to 15% limestone together with any SCM including calcined clay"; full title.
- https://link.springer.com/article/10.1186/s40069-026-00964-8 : authors and journal (A14).
- https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1704_web.pdf : edition; whether the regulator precedes site selection (A17).

### LCA primaries (§6, Appendices A and C; added 21/10, section H)
Hosts tried on 21/10 and blocked: PMC, fhr.nuc.berkeley.edu, epj-n.org, unece.org, ipcc.ch, nrel.gov, pubs.acs.org, doi.org, circularecology.com, ideas.repec.org, onlinelibrary.wiley.com, astm.org, aisc.org, arxiv.org, istructe.org, devalt.org. After each check, set `status: verified` in `parameters_lca.yaml` and re-run the three `lca_*.py` scripts.

**Fuel-cycle energy and emission sources**
- **P1** Gibon and Hahn Menacho (2023), *Environ. Sci. Technol.* 57(38): https://doi.org/10.1021/acs.est.3c03190 (open copy https://pmc.ncbi.nlm.nih.gov/articles/PMC10537461/). Confirm:
  - conversion heat **26 kWh/kg U, range 26–665**, and what the 665 represents;
  - conversion electricity **11.8 (10.3–16.9)**;
  - centrifuge **50 (40–100) kWh/SWU**; diffusion **2,500**;
  - fabrication **36 (36–50) kWh/kg**;
  - global 2020 average **6.1 g/kWh** (scenarios **5.4–122**); mining and milling **46%** (L12, L29, L34).
- **P1** Parker, McNaughton and Sparrow (2016), *ES&T* 50(17), pp. 9746–9753: https://pubs.acs.org/doi/10.1021/acs.est.5b06072. Confirm:
  - **81 / 64 / 34** kg CO₂e/kg U₃O₈ by grade;
  - production-weighted **42**; **24** with hydro;
  - the authors' names (L11).
- Ng et al. (2025), *J. Ind. Ecol.* 29(3), pp. 719–732: https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.70008. Confirm **3.0 g/kWh** and whether it covers the front end only, the full fuel cycle or the plant; full author list (L32).
- IPCC (2006) Guidelines, Vol. 2 Ch. 2 Table 2.2: https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol2.html. Confirm natural gas **56,100 kg CO₂/TJ** (L26).
- US EPA (2024) Power Profiler data sources: https://www.epa.gov/system/files/documents/2024-04/power-profiler-terms-calculations-and-data-sources.pdf. Confirm:
  - **823.1 lb CO₂/MWh** (0.373) and the marginal **1,405.3** (0.637);
  - whether they are CO₂ or CO₂e;
  - the eGRID year (L25).
- arXiv:2504.02599 (2025): https://arxiv.org/abs/2504.02599. Confirm **870 MWt / 300 MWe**, **3.8%** average and **4.95%** maximum enrichment; get the authors (L10).

**Benchmarks**
- **P1** UNECE (2021): https://unece.org/sites/default/files/2021-10/LCA-2.pdf. Confirm:
  - nuclear **5.1–6.4**; NGCC **403–513**; coal **751 or 753 to 1,095** g CO₂e/kWh;
  - "the fuel chain (front-end) contributes most";
  - the exact title, to settle against the un-ilibrary *Carbon Neutrality…* book (L28; see also the unece.org item above).
- IPCC AR5 WGIII Annex III, Table A.III.2: https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_annex-iii.pdf. Confirm nuclear lifecycle **min 3.7, median 12, max 110** g CO₂e/kWh; editors' names for the reference (L31, L35).
- NREL (2021) *Life Cycle Greenhouse Gas Emissions from Electricity Generation: Update*: https://www.nrel.gov/docs/fy21osti/80580.pdf. Confirm:
  - the nuclear median and range in Figure 2;
  - the report number (NREL/FS-6A50-80580).
- Warner and Heath (2012), *J. Ind. Ecol.* 16(S1), pp. S73–S92: https://doi.org/10.1111/j.1530-9290.2012.00472.x. Confirm:
  - harmonised median **12**, maximum **110**;
  - whether the minimum is **3.7** (L31).
- EDF R&D (2024), *EPJ Nuclear Sci. Technol.* 10, art. 5: https://www.epj-n.org/10.1051/epjn/2024005. Confirm:
  - **3.7 (2.9–4.6)** g/kWh;
  - stage shares: construction **16%**, operation **9%**, decommissioning **3%**, downstream **15%**;
  - whether downstream includes reprocessing;
  - the authors (L4, L33).
- Carless, Griffin and Fischbeck (2016), *Energy* 114, pp. 84–99: https://doi.org/10.1016/j.energy.2016.07.111 [DOI TO VERIFY] (IDEAS page in `sources_lca.md`). Confirm Westinghouse SMR **9.1 (5.9–13.2)** and AP1000 **8.4** (L30).

**Construction quantities and design**
- **P1** Peterson, Zhao and Petroski (2005), UCBTH-05-001: https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf. Confirm:
  - ESBWR **69 m³ and 33 t per MWe**; ABWR **138 m³ and 46 t**;
  - rated vs average MW;
  - whether steel includes rebar and equipment (L6).
- **P1** OPG basemat-module story (URL unknown; search opg.com for "basemat" 2026). Confirm **37 m** diameter, **35 m** shaft depth and **953 t** (L9). Alternatively, take the dimensions from NEDO-33926 (already listed under nrc.gov).
- CNSC CMD 24-H3-1B: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD-24-H3-1B.pdf/object. Confirm "Designed for a **60-year** operational life" (L2).
- Geneski, McKellar and Atkinson (n.d.): https://proceedings.cns-snc.ca/index.php/pcns/article/view/7692. Confirm the year and any steel vs concrete numbers (L14).

**Cement, concrete and LC3 papers**
- **P1** CAC GU/GUL EPD (2022): URL in `sources_lca.md` `cac2020_epd`. Confirm:
  - GU **796 / 854 / 898** kg CO₂e/t (West / Central / East);
  - **which region includes Ontario**;
  - GWP basis IPCC 2013 (L5).
- NRMCA EPD 20046, St Marys Bowmanville (2021): https://www.nrmca.org/wp-content/uploads/2021/09/NRMCA_EPD20046StMarys_EPD_BOW_Sep2021.pdf. Get the GU GWP; it replaces the CAC value.
- Slag Cement Association EPD: https://www.lafarge.ca/sites/canada/files/images/sca_epd_for_slag_cement.pdf. Confirm **146.6** kg CO₂e/t; Lafarge NewCem **93.4** (L19).
- CRMCA Ontario EPD 351 (2022): https://www.rmcao.org/wp-content/uploads/2023/04/CRMCA-EPD-Ontario-20220803.pdf. Confirm **334.49** and **417.05** kg CO₂e/m³ (L27).
- EFNARC (2005) *European Guidelines for Self-Compacting Concrete*. Confirm a powder content of **360–500 kg/m³** (L16).
- **P1, LC3 papers** (L20, L21):
  - Scrivener et al. (2018), CCR 114, pp. 49–56: https://doi.org/10.1016/j.cemconres.2017.08.017. Confirm about **50%** clinker, and whether the paper (not the EPFL abstract) states about **40%** CO₂ reduction.
  - LC3 Project (2015): https://lc3.ch/wp-content/uploads/2023/03/LCA-of-LC3-India-team-progress-Industry-meeting-Sep-2015.pdf. Confirm **856 vs 543** kg CO₂/t.
  - Development Alternatives (n.d.): https://devalt.org/images/L2_ProjectPdfs/Report%20-%20LC3%20Sustainability%20Assessment_ver1.14.pdf. Confirm **700 / 465**.
  - LACCEI (2026) contribution 2661: https://laccei.org/LACCEI2026-Chile/full-papers/Contribution_2661_final_a.pdf. Confirm **903.5 vs 513.5**; get the authors.
  - ENR (2018), "30% less CO₂": replace with a peer-reviewed LC3 LCA if one is found.

**Steel, including the ICE database**
- **ICE database**: Circular Ecology (2019) ICE v3.0 (https://circularecology.com/embodied-carbon-footprint-database.html; IStructE guide https://www.istructe.org/IStructE/media/Public/TSE-Archive/2020/A-brief-guide-to-calculating-embodied-carbon.pdf). Confirm:
  - world-average rebar **1.99** and sections **1.55** kg CO₂e/kg;
  - the version and date to cite (L24).
- CRSI EPD 362 (2022, supersedes 2017). Get the fabricated-rebar GWP to replace **0.97**, and the recycled content for the Granta set-up (L22).
- AISC (2022) Buy Clean California quick guide: https://www.aisc.org/contentassets/937a380ddd404a2da0c48669d438bf3b/quickguide_buycleancali2022.pdf. Confirm:
  - plate **1.49 / 1.73**; rebar **0.89 / 0.98**;
  - that these are limits (L23).

**Standards and waste**
- ISO 14040:2006 and ISO 14044:2006 (+A1:2020, A2:2020): bibliographic details for the references; check the critical-review requirement for comparative assertions (L1, L71). EN 15804:2012+A2:2019 for the A1–A3 and A4 module terms (L62).
- NWMO, Adaptive Phased Management (https://www.nwmo.ca): Canada's plan for direct disposal of used fuel (L13).

---

## Rubric IDs: what this check produced and what is still missing

- **R1.4.** Produced: every citation traced to sources.md, with hosts recorded. Missing: zero primaries verified (network); news sources still carry claims A1, A6, A8, A9, A24 and S12.
- **R2.1, R3.8, RB.5.** Produced: all five scripts re-run, outputs byte-identical, every number in §8.1, §8.3 and slides 4, 9, 13 and 14 traced. Missing: `verified: true` on the inputs; Appendix B not written; B3 to fix.
- **R2.6, R3.6.** Produced: S43 (the verdict contradicts `same_money.md`) and A10 (route scoring has no appendix). Missing: the MCDA.
- **R2.7, RB.6.** Produced: benchmark checks (section E); the 315 MWe gap in the sensitivity. Missing: Sam's LCA value, which can't be benchmarked yet.
- **R3.2, R3.4, R3.5, R3.7.** Produced: per-ID evidence gaps (section G). Missing: the fixes listed against A1, A2, A4, A6 and B12.
- **R4.3.** Produced: shows both legs of the §8.3 connection are unsupported (B13, B15). Missing: sources.
- **R5.2, R5.4, presentation rubric.** Produced: slide errors, placeholders, missing images, uneven speaker time, reference-list defects. Missing: the team's edits.

*I did not edit `rubric-tracker.md`; the examiner owns it. No item can be marked "Fact-checked" yet, because no primary source has been opened.*

---

## H. §6 LCA and Appendices A, C (21/10)

Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3, R1.4, R5.2, R5.4

Fact-checker run, 21/10/2026. The coordinator asked for this as section "D". It is lettered **H** because D–G already exist in this file. Sections A–G were not changed.

Scope:
- `01_Report/sections/6-lca-eco-audit.md` (v1)
- `appendix-A-lca-inventory.md` (v1)
- `appendix-C-sensitivity.md` (v1)
- Slides 5–8 (`proposal.html`, `lca-method.html`, `lca-results.html`, `materials-rd.html`, including `<aside>` notes)

The drafts were not edited.

**Method.**
- **Scripts.** I copied `results/` to a scratch folder. I then re-ran `lca_baseline.py`, `lca_scenarios.py` and `lca_uncertainty.py` with `python3 -I`, first from `03_LCA_Calculations` and then from the repository root (Appendix A1's command). Both runs exit 0 in about 4 s, and every output file, PNGs included, is **byte-identical** to the copy.
- **Hand checks.** I recomputed every formula in Appendix A by hand, including V(x), the feed factor, the annulus volume, the per-m³ factors and the Granta scale factors.
- **Network.** curl returned 000 for all 16 LCA primaries tried: PMC (Gibon), the Berkeley host (Peterson), EPJ-N (EDF), unece.org, ipcc.ch, nrel.gov, pubs.acs.org, doi.org, circularecology.com, IDEAS/RePEc, Wiley, ASTM (CAC EPD), AISC, arXiv, IStructE and devalt.org. WebFetch failed at DNS (ENOTFOUND) for PMC and the Berkeley host.
- **Verification.** No LCA citation is verified. Leads in `sources_lca.md` are compared with the text but are never treated as verification.

Status key as in §Method above, plus **documentation** (working not shown in the appendix).

| # | Where | Claim (as drafted) | Citation | Status | Evidence | Suggested fix |
|---|---|---|---|---|---|---|
| L1 | §6.1, §6.5 TODO 4; slide 6 | Goal and scope "follow ISO 14040/14044" | [TODO: source needed] | **source not found** | There is no ISO entry in `sources.md` or `sources_lca.md`. | Add ISO 14040:2006 and ISO 14044:2006 (both amended 2020) to the references. |
| L2 | §6.1, T6, A2 | 60-year design life | Canadian Nuclear Safety Commission, 2024 | unreachable | Lead `cnsc_cmd24_h3_1b`: "Designed for a 60-year operational life". NucNet reports 65 years (A2 notes this). | Human check. The tornado's 40–80 range covers 65. |
| L3 | T6, A2 | 300 MWe net (300–315 uniform) | GE Vernova Hitachi Nuclear Energy, n.d.; OPG filing | unreachable; open (S3) | The lead gives 300 MWe net. The 315 MW is from the OEB filing (TO VERIFY). The uniform draw matches the YAML. | Resolve with S3. If 315 is confirmed, the mode case falls to 2.63 g/kWh (tornado row 16). |
| L4 | §6.1, T6, A4 | O&M 0.33, decommissioning 0.11, back end 0.56 g/kWh = 9%, 3%, 15% of 3.7 | EDF R&D, 2024 | unreachable; **secondary shares** | `sources_lca.md`: the shares come "as reported by World Nuclear News and Euronuclear, not the abstract", and downstream 15% is "by difference". The arithmetic is OK (0.333, 0.111, 0.555). | Confirm the shares in the paper, and say in T6 that the back end is derived by difference. Also check whether "downstream" includes reprocessing (T9 relies on this). |
| L5 | T6, A4, C1 #28 | GU cement 854 kg CO₂e/t (796–898); GWP basis IPCC AR5 | Cement Association of Canada, 2022 | unreachable; **range is regional** | Lead: 796, 854 and 898 are the **West, Central and East** regional averages, not an uncertainty range. The year (2022) and key (`cac2020_epd`, 2020 data) are consistent. | Label the range "regional spread (West–East)". Confirm that Ontario is in the Central region, or use the St Marys Bowmanville EPD. |
| L6 | §6.2, T6, A3 | ESBWR 69 m³ and 33 t per MWe (central); ABWR 138 m³ and 46 t (high) | Peterson, Zhao and Petroski, 2005 | unreachable; **calc OK and order of magnitude OK** | The lead (via WNA, secondary) gives Gen II PWR 75 m³ and 36 t; ABWR 138 and 46; EPR 128 and 44.3; ESBWR 69 and 33. The ESBWR uses 50% of the ABWR's concrete (69/138 = 0.50). 69 × 300 = 20,700 m³ sits inside the published large-LWR band (69–138 m³/MWe). | Open the PDF. Confirm rated vs average MW and whether steel includes equipment and rebar. |
| L7 | §6.2, A3 | Vendor claims about 50% less concrete per unit of energy than the ESBWR (low bound 34.5 m³/MWe) | GE Vernova, n.d. | unreachable | The lead wording varies ("per unit of energy", "building volume per MW", "concrete and steel per MW"). It is a manufacturer projection, and the text says so. | Quote the exact wording you cite. |
| L8 | §6.2, A3, A4 | Forebay: 4,000 m³ concrete and 1,000 t rebar placed (a floor) | Ontario Power Generation, 2025 | unreachable | Quote in `Assumptions.docx`: "close to 4000 cubic metres of concrete and nearly 1000 tonnes of reinforcing steel have been placed in the forebay shaft". 1,000 t at 7.85 t/m³ = 127.39 m³ (A4 correction 2 is right). | Human check. Whether the forebay is per unit or shared is still TODO. |
| L9 | §6.2, A3 | Module diameter 37 m, shaft depth 35 m, basemat module 953 t | Ontario Power Generation, 2026 | **source not found** (primary not identified) | `opg_basemat_story`: "[exact URL TODO]". The only lead is a news story (okdiario, July 2026) that misdescribes the module. This geometry gives 9,081 m³, which is **69% of the C1 target concrete** and 1,291 t of the 1,734 t saving. | P1: find the OPG story or NEDO-33926 dimensions. Until then, say in §6.2 that the geometry rests on a press report. |
| L10 | §6.2, A2, A8, T6 | 870 MWt (η = 0.345); enrichment 3.8% (max 4.95%) | [TODO: authors], 2025 | **source not found** (incomplete reference) | `arxiv2025_smr_overview`: "Authors TBC". It is an unrefereed preprint. A Harvard citation with no author fails R5.4. The calculation is OK (300/870 = 0.3448). | Add the authors (arXiv:2504.02599), or replace with NEDO-33977 or GEH documents as the entry suggests. |
| L11 | §6.2, T6, A4 | Mining and milling 42 kg CO₂e/kg U₃O₈ (24–81); high-grade Saskatchewan ore | Parker, McNaughton and Sparrow, 2016 | unreachable | The lead matches: 81, 64 and 34 at three grades; production-weighted 42; 24 with hydro. The model's 1.024 g/kWh agrees with the paper's press summary ("about 1 g CO₂e/kWh"). | P1 human check. Also confirm the "Darlington's uranium is Canadian" TO VERIFY (OPG fuel release, B8). |
| L12 | §6.2, T6, A4, C1 #1/#8/#23/#26 | Conversion heat 26 kWh/kg U (26–665), electricity 11.8 (10.3–16.9); 50 kWh/SWU (40–100); fabrication 36 (36–50) | Gibon and Hahn Menacho, 2023 | unreachable (PMC: ENOTFOUND) | Every value matches the lead. Conversion heat is **the largest single uncertainty**: a 2.67 g/kWh swing, and +0.97 g/kWh of the 1.58 mean–mode gap. | **P1**: confirm the 26–665 range and its distribution in the paper (or SI). If the upper bound is a diffusion-era or outlier value, the headline median moves. |
| L13 | §6.2 hotspot 3, T9 | Canada plans direct disposal | [TODO: source needed: NWMO] | **source not found** | Not in either bibliography. | Add the NWMO Adaptive Phased Management / APM site-selection document. |
| L14 | §6.2 | Steel emits about twice what concrete does, "as Geneski, McKellar and Atkinson (n.d.) also found" | Geneski, McKellar and Atkinson, n.d. | unreachable; **direction only** | The lead (abstract) says steel, "particularly for turbine plant equipment, produces more" GHG than concrete. "No numbers seen." Our 14,767 vs 7,584 t is calc OK. | Keep "also found steel exceeds concrete"; don't imply they found 2×. Add the year. |
| L15 | §6.3 | The DPSC design calls for self-consolidating concrete | GE-Hitachi Nuclear Energy, 2024 | unreachable | `GEH_NEDO33926` extract, §5.2.1: "self-consolidating concrete is used in the integrated RB DP-SC modules". It matches. | Human check (§5.2.1 and §6.2.1 cement-type limits). |
| L16 | T6, A4, C1 #25 | SCC binder 450 kg/m³ (400–550) | EFNARC, 2005 | unreachable; secondary | The lead is a 2024 journal article quoting 360–500 kg/m³ powder. The 550 high is above EFNARC's range; A4 labels it as an assumption. | Open EFNARC (2005) or cite the secondary article as read. |
| L17 | §6.3 finding 3 | Slag blends have nuclear precedent | [TODO: authors], 2026 | **source not found** (incomplete) | Same as A14: there is no author for DOI s40069-026-00964-8. | Complete the reference. |
| L18 | §6.3 finding 3 | LC3's case rests on Ontario's slag supply shrinking as steelmaking moves to EAF (§4.3) | none ([TO VERIFY]; §4.3 not drafted) | **source not found** | Not in either bibliography. This is the stated reason to prefer LC3 over slag, so it carries the argument (R2.6). | Source the Ontario blast-furnace closures (e.g. the steelmakers' EAF conversion announcements), or reduce it to a one-sentence risk (the section's own TODO 7). |
| L19 | T6, A4 | Slag cement 146.6 kg CO₂e/t (low 93.4) | Slag Cement Association, n.d. | unreachable | It matches the lead (146.6 = 4.6 + 57.0 + 85; Lafarge NewCem 93.4). | Human check. |
| L20 | T6, A5 | LC3 binder cut 37% (30–43%), the median of five estimates | ENR 2018; Development Alternatives n.d.; LC3 Project 2015; Scrivener et al. 2018; LACCEI 2026 | unreachable; **calc OK; weak set** | Recomputed: (700−465)/700 = 33.6%; (856−543)/856 = 36.6%; (903.5−513.5)/903.5 = 43.2%. With 30% and about 40%, the median is 36.6% ≈ 37%. ENR is trade press, the 40% is from an EPFL abstract (not the paper text), and LACCEI has no authors. | Replace ENR with a peer-reviewed LCA (R1.4). Confirm Scrivener's figure in the paper. Add the LACCEI authors. |
| L21 | A4, C1 #38 | LC3 clinker factor 0.50 (0.50–0.55) | Scrivener et al., 2018 | unreachable | The lead says LC3-50 is about 50% clinker. The reference details (CCR 114, pp. 49–56) match `sources_lca.md`. | Human check. |
| L22 | T6, A4, C1 #20 | Rebar 0.97 t CO₂e/t (EAF, fabricated) | Concrete Reinforcing Steel Institute, 2017 | unreachable; **superseded** | The lead says the 2017 EPD is superseded by EPD 362 (2022), and the 0.97 came via a 2022 presentation. | Use the 2022 EPD value and cite it. |
| L23 | T6, A4, C1 #14 | Plate, structural and equipment steel 1.73 t/t (1.22–2.50) | American Institute of Steel Construction, 2022 | unreachable; **wording** | The lead says these are Buy Clean California **GWP limits** (policy ceilings), "not industry averages". A4 says "limit as a proxy", but T6 in §6 does not. | Add "(Buy Clean California limit, used as a proxy)" to T6. |
| L24 | A4, C1 #20, S3 high | World-average rebar 1.99 | Circular Ecology, 2019 | unreachable | The lead is ICE v3 via IStructE (2020/2022). It is cited through a secondary. | Human check of the ICE v3 spreadsheet (see checklist). |
| L25 | A4, C1 #7/#15/#19 | Grids: Ontario 0.0738 (0.035–0.343); USA 0.373 (lows 0.05/0.20; high 0.637) | The Atmospheric Fund, 2025; Canada Energy Regulator, n.d.; US EPA, 2024 | unreachable; **gas basis** | The EPA leads are **CO₂ only** (823.1 and 1,405.3 lb CO₂/MWh), yet they are used as CO₂e. The 343 g definition is ambiguous (taf2025). The effect is small, since the enrichment grid swing is 0.43 g/kWh. | State that the US factors are CO₂ only, or use eGRID CO₂e. |
| L26 | A4 | Natural-gas heat 0.202 kg CO₂/kWh | IPCC, 2006 | unreachable; **calc OK** | 56,100 kg/TJ × 3.6 × 10⁻⁶ TJ/kWh = 0.202. It is combustion CO₂ only (no upstream gas), which biases conversion slightly low. | Add the upstream-gas cut-off to §6.1's cut-off list. |
| L27 | A5 | Ontario 35 MPa concrete 334 kg CO₂e/m³; benchmark mix 417 | Canadian Ready-Mixed Concrete Association, 2022 | unreachable | It matches the lead (334.49 and 417.05). The model's 328.9 is calc OK. | Human check. |
| L28 | §6.5, F5; slide 7 | Nuclear 5.1–6.4; gas CC 403–513; coal 751–1,095 g/kWh | United Nations Economic Commission for Europe, 2021 | unreachable (unece.org: 000); **title conflict** | Leads agree on 5.1–6.4 and 403–513. The coal low end is "751 (IGCC, USA) or 753" (S19). `sources.md` gives the title *Carbon Neutrality in the UNECE Region…* (un-ilibrary); `sources_lca.md` gives *Life Cycle Assessment of Electricity Generation Options* (LCA-2.pdf); slide 7 uses the latter (D, row "UNECE title"). | P1. Pick one title and edition for §6.5, F5 and slide 7. |
| L29 | §6.5, T9 | Global average 6.1 g/kWh; mining 46%, about 2.8 g/kWh | Gibon and Hahn Menacho, 2023 | unreachable; **calc OK** | 0.46 × 6.1 = 2.81. Mining gap 2.8 − 1.26 = 1.5 of the 1.9 gap to 6.1, so "most of the gap" holds. | Human check (with L12). |
| L30 | §6.5, T9, F5 | SMR 9.1 (5.9–13.2) vs AP1000 8.4, mainly through the fuel cycle | Carless, Griffin and Fischbeck, 2016 | unreachable | It matches the lead ("without the fuel cycle the SMR and AP1000 are effectively equal"). Cite the paper, not the thesis (7.4). | Human check. |
| L31 | §6.5, F5 footnote | Harmonised LWR median 12; F5 footnote "range 3.7–110" | Warner and Heath, 2012 | unreachable; **range attribution** | The lead gives a median of 12 and a maximum of 110 but **no 3.7 minimum**. 3.7 is the commonly quoted IPCC AR5 minimum, itself unconfirmed (`ipcc2014_annex3`). | Confirm the minimum in Warner and Heath, or drop "3.7" from the F5 footnote. |
| L32 | §6.5 | US fuel cycle 3.0 g/kWh, close to our front end 2.7 | Ng et al., 2025 | unreachable; **scope unclear** | The lead says "3.0 g CO₂e/kWh for the US nuclear fuel cycle". Whether it includes the back end or the plant is unknown. The author list is incomplete. | Confirm the scope before comparing it with our front end only. Complete the authors. |
| L33 | §6.5, F5 | French fleet 3.7 (2.9–4.6) | EDF R&D, 2024 | unreachable | It matches the lead (2019 data). | With L4. |
| L34 | T9 | 50 kWh/SWU (centrifuge) vs about 2,500 (diffusion) | Gibon and Hahn Menacho, 2023; Warner and Heath, 2012 | unreachable | It matches the Gibon lead (2,500; 2,400–3,000). Nothing in the Warner lead supports this, and Warner is cited for older study sets only. | Fine once L12 is checked. |
| L35 | §6.5 (check 3: benchmarks) | 4.2 (3.0–5.8) "inside the published range, at its low end"; just below UNECE | — | **OK, with explanation** | The median is below UNECE (5.1–6.4), but the 90% intervals overlap. It is inside the commonly quoted IPCC AR5/NREL harmonised range (3.7–110, median 12; unconfirmed) and overlaps EDF. T9 gives the sign and size of each discrepancy, so RB.6 has an explanation. | No change to the value. See L52 for consistent wording. |
| L36 | §6.1, A2 | 1.419 × 10⁸ MWh; 1 t = 7.05 × 10⁻⁶ kg/MWh; η 0.345 | lca_baseline | **calc OK** | 300 × 8,760 × 0.9 × 60 = 141,912,000. 1,000 kg / 1.419 × 10⁸ = 7.05 × 10⁻⁶. | none |
| L37 | §6.2, A3, T A2 | 20,700 m³; 9,900 t; target 13,081 (3,226 + 5,855 + 4,000); 63%; 706 clipped draws (3.5%) | lca_baseline, lca_uncertainty | **calc OK** | 0.7854 × 37² × 3 = 3,226; π × 35.5 × 1.5 × 35 = 5,855; 13,081/20,700 = 63.2%. | none |
| L38 | §6.2, A6 (units and magnitude) | Concrete 0.35 kg/MWh; steel 0.070 kg/MWh; clinker avoided 0.016 kg/MWh (7.7 t/MWe) | A6 | **calc OK** | 20,700 × 2.4 / 1.419 × 10⁸ = 3.5 × 10⁻⁴ t/MWh; 9,900/1.419 × 10⁸ = 7.0 × 10⁻⁵ t; 2,304/300 = 7.68. The units are right (mass per MWh, not volume). | none |
| L39 | §6.2, A8, T A8 | 2.685 g enriched U, 20.68 g natural U, 0.0146 SWU per MWh; F = 7.70; 5.42 SWU/kg; 4 units 195.6 t U and 137.7 tSWU per year | lca_baseline | **calc OK; magnitude OK** | Hand-computed V(0.038) = 2.986, V(0.0025) = 5.959, V(0.00711) = 4.869, giving 5.421 SWU/kg. 20.7 t U/TWh and 14.6 SWU/MWh are typical of an LWR (about 20–25 t U and about 15 kSWU per TWh). | none |
| L40 | A8 | Mining 1.024; conversion 0.127; enrichment 0.272; fabrication 0.036 g/kWh | lca_baseline | **calc OK** | 0.02068 × 42/0.848 = 1.024; 0.02068 × (11.8 × 0.0738 + 26 × 0.202) = 0.127; 0.002685 × 5.42 × 50 × 0.373 = 0.271; 0.002685 × 36 × 0.373 = 0.036. | none |
| L41 | A7, A9, T A7/A9 | Construction 34,381 t = 0.242 g/kWh; total 383,243 t = 2.701 g/kWh; shares; C1 target concrete 5,078 t (1.3%) | lca_baseline | **calc OK** | Transport 74.5 + 495 = 570; uplift 0.5 × 22,921 = 11,460; 383,243 t / 1.419 × 10⁸ MWh = 2.701 kg/MWh. Every cell matches `lca_baseline.md`. | none |
| L42 | §6 lead, T8, A6 T A6 | S1 1,552; S2 1,734 (5,201; clinker 2,304/6,913); S2b 2,488; S3 3,714 / −8,399; % of target; g/kWh | lca_scenarios | **calc OK** | Every cell matches `lca_scenarios.md`. | none |
| L43 | A6 worked example, T A5, A9 | 571.0 and 538.0 kg/t; 414.3, 328.9 and 272.1 kg/m³; 1,291 t; 1,716 t clinker; Granta scale factors 0.693/0.657/0.699/0.664; BOM 21,794 t; transport about 145 t | A6, A9 | **calc OK** | Recomputed: 0.6 × 854 + 0.4 × 146.6 = 571.04; 9,081 × 2.4 = 21,794; 2,606/3,762 = 0.693; 218.3/328.9 = 0.664; (31,394 t × 15 + 1,953 t × 500) × 0.1 kg/t-km = 145 t. | none |
| L44 | App C T C1–C3 | All 40 tornado rows; MC table; stage means; mean − mode = +1.578 | lca_uncertainty | **calc OK** | Every value matches `lca_uncertainty.md` and the CSVs. Column sum 1.578 = 4.279 − 2.701. | none |
| L45 | §6.4, F3, F4 | Tornado end-points; MC median 4.18 (3.05–5.85), mean 4.28; LC3 1,742 (1,387–2,153); 64%; 20,000 draws, seed 20261021 | lca_uncertainty | **calc OK** | Matches the output. Burnup "2.44" is 2.4354 rounded (OK). | none |
| L46 | §6.5 | 100–120× lower than gas CC; 180–260× lower than coal | calc | **calc OK** | 403/4.18 = 96; 513/4.18 = 123; 751/4.18 = 180; 1,095/4.18 = 262. | none |
| L47 | §6.3 findings 1, 3, 4, 5 | 66% (5,078 vs 2,619); 180 t; about 2×; 10–15 days (avg) or about 1.4 days (marginal) | lca_scenarios; schedule_value.md | **calc OK** | 5,078/7,697 = 66.0%; 1,734 − 1,552 = 182; 3,714/1,734 = 2.1. `schedule_value.md` U2–U4 ON-avg-traj 5.6–8.4 days per kt × 1.734 = 9.7–14.6 days; marginal-declining 1,734/1,226 t/day = 1.41 days. | Appendix B working still TODO (§6 TODO 6). |
| L48 | T9 | Construction 0.24–0.32 vs about 0.59 (16% of 3.7); "at 0.6–1.0 the total would rise 0.3–0.7" | calc | calc OK (rounding) | 0.16 × 3.7 = 0.592. The rise spans 0.6 − 0.32 = 0.28 to 1.0 − 0.24 = 0.76. | "0.3–0.8 g/kWh". |
| L49 | T9 | 40-year life raises the mode case from 2.70 to 2.82 | lca_uncertainty | **calc OK** | Tornado: design_life low 2.8217. | none |
| L50 | App C C5 | Triangular mean (26 + 26 + 665)/3 = 239, nine times the mode | calc | **calc OK** | 239/26 = 9.2. | none |
| L51 | §6.4, F4, App C C1 (MC set-up) | N = 20,000; seed 20261021; `numpy.random.default_rng`; 39 triangular + 1 uniform; independent; fixed parameters listed; clip rule | lca_uncertainty.py; parameters_lca.yaml | **OK** | Script lines 66–73: `default_rng(mc_seed)`, `rng.uniform` / `rng.triangular`. The YAML has 59 parameters; 40 are varied (low ≠ high, not fixed, not bm_/mc_/units_), and only `net_mwe` is uniform. The set-up is fully stated (R2.7). | none |
| L52 | §6, A9, App C | No text implies a Granta run exists | — | **OK** | §6.1: "no number here comes from Granta"; A9: "has not been run"; every Granta cell says [TODO: results pending]; the scripts contain no Granta reference. | Keep. But see slide 6 (L70). |
| L53 | A1 | "regenerates in about five seconds"; commands run from the repository root | — | **OK** | Run from the root: 4.0 s, byte-identical outputs. | none |
| L54 | slide 7 | 4.2 g (90%: 3.0–5.8); LC3 about 1,700 t, 0.3%; mining about 29%; slag almost as much; steel about 2× | lca_uncertainty, lca_scenarios | **calc OK** | It matches §6 and the outputs. | none |
| L55 | §6.3 T8 | "Share of one unit's life cycle" column: S1 0.41% (mode case), **S2 0.29% (MC median)**, S2b/S3 mode case | lca_scenarios; lca_uncertainty | **inconsistent** (mixed basis) | On the same basis, S2 is 0.452% (mode) vs S1 0.405%. As printed, slag appears to save a *larger* share than LC3, which contradicts column 2. Also, the "MC 5th–95th" column's central figures (1,552; 1,734) are mode-case values, while the MC medians are 1,642 and 1,742. | Use one basis per column: mode case for all (0.41/0.45/0.65/0.97/−2.2%), with the S2 median 0.29% (0.18–0.46%) in a note. Relabel column 2 "mode case (MC P5–P95)". |
| L56 | §6 lead vs §6.5 vs slide 7 notes | "at or just below the published range" / "inside the published range … at its low end" / "at the low edge of UNECE's range" | — | **inconsistent** | 4.2 is **below** UNECE's 5.1–6.4 (intervals overlap) and inside the wider literature range (L35). Slide 7's "at the low edge of UNECE's range" is wrong. | Use one phrase everywhere: "just below UNECE's 5.1–6.4 (our interval overlaps it) and at the low end of the wider literature range". |
| L57 | §6 lead, §6.2, App C C4/C6 | "construction about 7%" (expected basis) | lca_uncertainty | **inconsistent** (rounding) | 0.3212/4.279 = **7.5%**. The grouped shares are 64.2 / 19.2 / 9.1 / 7.5. | "about 7.5%" (or 8%). |
| L58 | §6.2 | 196 t U and 138 tSWU a year is "the demand against which §8.3 judges supply risk" | §8.3 | **inconsistent** | §8.3 does not use these numbers. Its TODO 6 still asks for the SWU sizing, and the tracker notes R2.3 "§8.3 is not sized to Darlington's fuel demand". | Either add the numbers to §8.3 (the writer, for Victor; this also closes the R2.3 gap) or change §6.2 to "…which §8.3 should use". |
| L59 | §6.3 finding 2 | "its value is as a **low-cost** cut and **a first nuclear use** of LC3" | none | **overclaim** | No cost was calculated (R2.3 says the economic benefit is "Missing"). No source says LC3 has never been used in nuclear concrete. | "…its value is as a cut of unknown cost and, if qualified, possibly an early nuclear use of LC3 [TO VERIFY]". |
| L60 | §6.3 | "Units 2–4 only are counted, because Unit 1's basemat and **forebay** are already placed" | OPG 2025 | **overclaim** / inconsistent with §6.2 | §6.2 calls the 4,000 m³ placed "so far, a floor". Unit 1's **shaft-wall infill** is not shown to be placed (S14 logic). | "…because Unit 1's basemat is placed and its forebay is well advanced". Note whether Unit 1's shaft-wall infill could still use LC3. |
| L61 | §6.1 (ISO terms) | "This makes it a **hybrid LCA**" | — | **wording** (term misuse) | In LCA usage, "hybrid" means process-based plus input–output (EEIO). This is a process-based LCA supplemented with secondary per-kWh literature data. Slide 6 calls it a "process LCA" (L73). The other ISO terms (functional unit, reference flow, system boundary, cut-off, critical review for public comparative assertions) are used correctly. | "a process-based LCA, with O&M, decommissioning and back end taken from secondary per-kWh data". |
| L62 | §6.1; A5 opening | "Impact method: GWP100"; "All [factors] are cradle-to-gate (A1–A3) GWP100" | — | **error** (wording) | A1–A3 and A4 are EN 15804 / ISO 21930 module codes, not ISO 14040/44 terms, and need that reference. The grid, natural-gas, mining and EDF factors are not A1–A3, and the EPA grid factors are CO₂ only (L25). | §6.1: "Impact category: climate change; characterisation GWP100 (IPCC AR5 where stated)". A5: "Construction-material factors are cradle-to-gate (EN 15804 modules A1–A3)…". Cite EN 15804. |
| L63 | App C C3 | "the first two are the LC3 literature and OPG's drawings; **the next three are mix design**" | lca_uncertainty | **error** | The next three are infill binder (mix), **basemat thickness (geometry)** and extra binder (mix). | "…two of the next three (binder content, extra binder) are mix design; basemat thickness is geometry". |
| L64 | lca.md §7 (source file for the writer) vs §6.4 and App C | "Every construction-quantity input … moves the total by under 0.07 g/kWh" | lca_uncertainty | **error** in `lca.md`; **§6.4 and App C correct** | Tornado: steel intensity **0.1665**, uplift **0.2019**, plate factor 0.092; concrete intensity 0.0654. §6.4 ("No concrete input … 0.07; steel intensity … 0.17") and C2/C3 (uplift 0.20, steel 0.17) use the right figures. `lca.md` line 202 is uncorrected. No slide cites either figure. | lca-analyst: correct `lca.md` §7 so that no one re-copies 0.07 for steel. |
| L65 | App A A3, C1, C3 | Rebar = ratio × plant concrete; plate = steel − rebar | lca_model.py | **documentation** | The model caps rebar at total steel (`min(ratio × V, steel_t)`), which is not stated. Because of this split, expected plate steel (0.073) is *below* its mode value (0.083) in T C3 (−0.010), with no explanation. | Add one sentence to A3: "rebar is capped at total steel". One sentence in C4 explaining the negative row. |
| L66 | F5 (`lca_uncertainty.py` line 221) | UNECE plotted as a point at 5.8 with "point = central or median" | script | **error** (figure) | 5.8 is the script's own midpoint of 5.1 and 6.4. UNECE reports a range, not a central value. | Draw UNECE as a range only, or label the point "midpoint (ours)". |
| L67 | slide 5 notes | "about 20,700 m³ of concrete per unit (**range 10,000–41,000**)" | lca results | **error** | 10,350–41,400 are the raw input bounds (34.5–138 × 300). The model never goes below the target volume (13,081; clip rule), and the MC 90% interval is **15,050–36,521** m³ (T C2). | "(90% interval about 15,000–36,500)". |
| L68 | slide 5 on-slide vs notes and §6 | "about 13,000 m³ of target concrete" vs "about 13,100" | lca_baseline | **inconsistent** (minor) | 13,081. | Use "about 13,100" on the slide. |
| L69 | slide 5 | "deep water **shafts**"; Unit 1 basemat poured | OPG 2025 | wording | The model has one forebay shaft per unit, and whether it is shared is TODO. The basemat wording matches S14. | "the deep cooling-water (forebay) shaft". |
| L70 | slide 6 on-slide | "Tools: Python process LCA …; **Granta EduPack cross-check**" | — | **overclaim** (implies the run exists) | A9: "has not been run". §6 TODO 8: "Slides 6–7 must not cite Granta until TODO 2 is done". The notes are conditional, but the on-slide text is not. | "Granta EduPack cross-check (in progress)", or delete it until the run exists. **Must change before Thursday.** |
| L71 | slide 6 on-slide and notes | "Method: ISO 14040/14044 life-cycle assessment"; "We followed the standard ISO 14040 life-cycle method" | none | **overclaim** | §6.1 says only that it follows the ISO goal-and-scope structure, "without the critical review". ISO is not in the references (L1). | "Structured on ISO 14040/44 (screening study, not critically reviewed)". |
| L72 | slide 6 on-slide | "Material quantities scaled from published reactor data per MWe; **Darlington forebay data as a check**" | — | **inconsistent** with A3 | The forebay (4,000 m³) and the OPG module geometry are **inputs** to the C1 target structures (A3), not a check. | "…scaled from published per-MWe data; OPG forebay and module data for the target structures". |
| L73 | slide 6 vs §6.1 | "Python process LCA" vs "hybrid LCA" | — | **inconsistent** | See L61. | Use the same term in both (L61 wording). |
| L74 | slide 7 source line | "Python LCA model, 20,000 Monte Carlo draws (**Appendix A**)" | — | **error** | The Monte Carlo is in **Appendix C**. | "(Appendices A and C)". |
| L75 | slide 7 notes | LC3 saving "1,400 to 2,150" | lca_uncertainty | **inconsistent** (minor) | P5 is 1,387, given as 1,390 in §6. | "1,390 to 2,150". |
| L76 | slide 7 | "bars to scale" | — | wording | Coal 985 px and gas 462 px are 0.9 px per g (to scale). Nuclear is 8 px and ours 6 px, against 5.8 and 3.8 px at scale: both are widened to stay visible. | Add "(nuclear bars widened to be visible)" to the notes, or keep as is and don't call them exact. |
| L77 | slide 8 | SILEX re-enrichment of tails; fuel chain "reported to be nuclear's largest emitter" | sources.md S21 (NRC_GLE_PLEF, GLE_DOE_2016); on-slide: none | **source not found** (on slide); unreachable | `sources.md` now has NRC and GLE entries (unopened), but the slide's source line lists only Scrivener and Krall. Our own §6.2 now supports the hotspot claim (front end 64% expected, 54% mode), so "reported to be" can cite us. | Add "NRC (n.d.)" to the slide sources. Change to "the fuel front end, about two-thirds of our LCA total (§6)". Keep the B15 causal-wording fix. |
| L78 | slide 8 | "One study of three SMR designs finds 2–30× more waste by volume per unit of energy" | Krall, Macfarlane and Ewing, 2022 | unreachable | It is now in `sources.md` (Krall_2022, PNAS 119(23) e2111833119). The lead says "factors of 2 to 30" for three designs; the per-energy normalisation is still to confirm. | Human check (existing checklist item). |
| L79 | slide 9 notes (consistency only) | Nuclear "adds about 6 g of its own life-cycle emissions" | UNECE 2021 | **inconsistent** (minor) | Our model median is 4.2. The effect on 634 g is negligible (it would be 636). | "about 4–6 g" (ours and UNECE). |

### H summary

**Counts by status (79 rows; each counted once, under its most serious status).**

| Status | Count | Rows |
|---|---:|---|
| Verified (primary opened and confirmed) | **0** | Every LCA primary host blocked (curl 000, WebFetch ENOTFOUND) |
| Unreachable (needs a human check) | 29 | L2–L8, L11, L12, L14–L16, L19–L34, L78 |
| Source not found (missing or incomplete reference) | 7 | L1, L9, L10, L13, L17, L18, L77 |
| Calc or logic OK (re-run byte-identical; hand-checked) | 20 | L35–L54 |
| Error | 6 | L62, L63, L64, L66, L67, L74 |
| Inconsistent | 9 | L55, L56, L57, L58, L68, L72, L73, L75, L79 |
| Overclaim or wording | 7 | L59, L60, L61, L69, L70, L71, L76 |
| Documentation | 1 | L65 |
| **Total** | **79** | |

**Blocking issues**
1. **No LCA input or benchmark is verified (R1.4, R2.1, R2.7, RB.6).** P1 primaries, in order of effect on the headline or on C1:
   - Gibon and Hahn Menacho 2023 (conversion heat 26–665)
   - Parker 2016
   - EDF R&D 2024 (stage shares)
   - The OPG basemat geometry (L9: it drives 69% of the C1 target concrete and rests on a news report)
   - The CAC EPD (and which region Ontario is in)
   - The five LC3 estimates
   - Peterson 2005
   - UNECE 2021
2. **Slide 6 (Thursday):** the on-slide "Granta EduPack cross-check" implies a run that does not exist (L70), and "ISO 14040/14044" overclaims conformance (L71, L1).
3. **T8 mixed basis (L55):** as printed, slag appears to save a larger life-cycle share than LC3. Fix before the examiner marks R2.6/R5.2.
4. **Slide errors (Thursday):** slide 5 notes concrete range (L67); slide 7 "Appendix A" → C (L74) and "at the low edge of UNECE's range" (L56).
5. **Unsourced load-bearing claims in §6.3:** "low-cost … first nuclear use of LC3" (L59) and Ontario slag supply as LC3's rationale (L18).
6. **Steel sensitivity:** §6.4 and Appendix C correctly use 0.17 g/kWh. Only `results/lca.md` §7 still says "< 0.07" for every construction input (L64), so it must not be re-copied.

**Slides that must change:** 5 (notes; L67, L68), 6 (L70, L71, L72, L73), 7 (L56, L74, L75), 8 (L77). Slide 9 notes optional (L79).

### H rubric evidence (check 5): what §6 and Appendices A and C claim vs what is there

- **R2.1** ("strong quantitative analysis"). Present: full inventory, stage results, savings per structure, per unit and for Units 2–4, all reproducible and calc OK. Gap: zero verified inputs. **Partial until verified.**
- **R2.2** ("where feasible, an eco-audit or equivalent analysis"). Present: an equivalent analysis covering the whole life cycle, labelled honestly as not Granta. The Granta set-up exists (A9) but has not been run. **Evidence meets the "equivalent" wording**; slide 6 must not imply more (L70).
- **R2.3** ("calculations of … resource usage and potential environmental or economic benefits … appropriate to the scale of the proposal"). Present: m³/MWe, kg/MWh, U and SWU per MWh, t CO₂e and clinker for Darlington Units 2–4. Gap: **no economic benefit** (abatement cost), and the "low-cost" claim is unsupported (L59). §8.3 does not yet use the fuel demand (L58). **Partial.**
- **R2.4** ("methods clearly explained and easy to follow"). Present: formulas, worked examples, reproduce commands (verified, L53). Gap: the rebar cap is undocumented (L65). **Near HD.**
- **R2.5** ("assumptions, scope and functional unit clearly defined"). Present: FU, reference flow, boundary (F1), cut-offs, T6. Gaps: no ISO reference (L1); impact-basis and module wording (L62); "hybrid" misused (L61). **Partial.**
- **R2.6** ("arguments logical, well justified"). Present: five findings, each with a consequence. Gaps: the T8 basis mix (L55), the unsourced slag-supply premise (L18), the C3 slip (L63). **Partial.**
- **R2.7** ("uncertainties … realistically estimated and discussed"). Present: a 40-input tornado; MC with stated N, seed, generator, distributions and independence (L51); median vs mode explained; limitations stated. Gap: ranges unverified; the conversion-heat range (L12) carries most of the spread. **Strongest ID; HD-capable once L12 is checked.**
- **RB.5.** Present: Appendices A and C give the full working. **Met** (inputs unverified).
- **RB.6** ("results compared with literature values, discrepancies explained"). Present: F5 and T9 with sign and size. Gaps: benchmarks unverified; inconsistent "range" wording (L56); the F5 UNECE midpoint (L66); the Warner 3.7 attribution (L31). **Partial.**
- **R1.3.** Present: vendor claim vs scale penalty, Parker vs Gibon, EDF vs ours, Carless. **Met in form**, pending verification.
- **R5.2 / R5.4.** Figures F1–F5 exist and are captioned. Gaps:
  - Four references have no author: L10, L17, LACCEI, Ng et al.
  - ENR is trade press.
  - The UNECE title conflicts between the two bibliographies (L28).
  - The rebar EPD is superseded (L22).

*Not done by me:* the Granta run, the opening of primaries, and any edit to the drafts, `lca.md` or `rubric-tracker.md`.
