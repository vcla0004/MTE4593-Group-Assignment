Rubric coverage: R1.4, R2.1, R2.6, R2.7, R3.2, R3.4, R3.5, R3.6, R3.7, R3.8, R4.3, R5.2, R5.4, RB.5, RB.6; presentation rubric (visual 2%, teamwork 1%)

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
