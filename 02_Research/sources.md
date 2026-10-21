Rubric coverage: R1.4, R1.3, R5.4, R3.2, R3.3, R4.3, R2.3 (single bibliography)

# Sources

Merged from analyst runs 1–4 (20/10/2026); run 7b (21/10/2026, plan job Q3) added the block at the end and merged the two Parliamentary Library entries into APH_2024. Entries marked TO VERIFY were seen only in search extracts: the environment network blocked the primary sites. Confirm before citing.


---

## From analyst run 1


# Sources: analyst run 1 (displacement, schedule value, same money, benchmarks)

To be merged into `02_Research/sources.md` by the coordinator. Format: Harvard reference, then key findings, numbers, reliability, and the section it supports. Keys match `03_LCA_Calculations/parameters_run1.yaml`.

**Access status, 20/10/2026 (read this first).** No primary document in this file could be opened. The session's egress proxy refused (HTTP 403, policy) every primary host tried: csiro.au, ontario.ca / news.ontario.ca, opg.com, unece.org, ipcc.ch, nrel.gov, dcceew.gov.au, aemo.com.au, ieso.ca, cer-rec.gc.ca, rba.gov.au, taf.ca, cleanenergyregulator.gov.au, world-nuclear-news.org. WebFetch couldn't resolve any of them either. Every number below was seen only in a **web-search summary or a secondary source**. Under CLAUDE.md, none of it is citable until a team member opens the primary and confirms the value. Each entry says exactly what to check. I didn't use mirror copies on other hosts (e.g. a github.io copy of the GenCost draft), because that would route around the access policy and the copies can't be trusted.

Status tags: **[TO VERIFY]** = lead only. **[URL TODO]** = the primary's exact URL is not yet known.

---

## Darlington: cost, approval and dates

### ontario2025_fid
**Reference (incomplete):** Government of Ontario, 2025. [Title TODO: news release announcing approval of the first SMR at Darlington, 8 May 2025]. [online] Toronto: Government of Ontario. Available at: [URL TODO, news.ontario.ca].
- **Findings (secondary):** Approval on 8 May 2025 for OPG to start building the first of four BWRX-300s (Darlington New Nuclear Project). The C$20.9 bn budget covers site preparation, engineering and construction of all four units, about 1,200 MW. The first unit is C$6.1 bn, plus C$1.6 bn for common infrastructure (C$7.7 bn).
- **Seen in:** World Nuclear News, "OPG gets go-ahead to build first SMR in Canada" (https://world-nuclear-news.org/articles/opg-gets-go-ahead-to-build-first-smr-in-canada); NS Energy; BLG (https://www.blg.com/insights/2025/06/ontario-approves-construction-of-first-of-its-kind-small-modular-reactor); MobileSyrup, 8 May 2025 (C$6.1 bn); The Globe and Mail (C$1.6 bn shared infrastructure, C$7.7 bn total). The sources disagree on whether C$6.1 bn includes the C$1.6 bn. **Check that in the primary.**
- **Reliability:** high once the government release or OPG's Q1 2025 results are opened; news only until then.
- **Supports:** §3 (cost barrier), §7 (same money), §8.2.

### opg_dnnp
**Reference (incomplete):** Ontario Power Generation, 2025. *Darlington New Nuclear Project* [online]. Available at: [URL TODO, opg.com]; and OPG, 2025. *OPG reports 2025 first quarter financial results* [press release]. Available at: https://www.newswire.ca/news-releases/opg-reports-2025-first-quarter-financial-results-824344588.html.
- **Findings (secondary):** Unit 1 is targeted for completion by the end of the decade, with grid connection by end-2030 (Q1 2025 release, via search). Other sources say commercial operation by end-2029. Units 2–4 are planned for 2034–2036 (Power Engineering, "OPG provides updates on SMRs, Darlington nuclear refurbishment", from July 2023 planning). A June 2026 ANS Nuclear News piece reports the basemat in place but doesn't restate the dates.
- **Reliability:** OPG's own release is primary (newswire.ca, not yet opened). The Units 2–4 dates are from 2023 and may have moved.
- **Supports:** §4.1 (Leroy), §7 start years. **Leroy owns the dates.**

---

## Ontario grid emission factors

### taf2025
**Reference:** The Atmospheric Fund, 2025. *Ontario Electricity Emissions Factors and Guidelines: 2025 Edition*. [pdf] Toronto: TAF. Available at: https://taf.ca/custom/uploads/2025/10/2025TAF-EmissionsFactors.pdf [TO VERIFY title and authors on the cover].
- **Findings (secondary):** An annual update of Ontario's historical average, forecast and marginal factors, with guidance on which to use: marginal for evaluating short-term changes in demand or supply, average for inventories. TAF's carbon page (https://carbon.taf.ca/2024/electricity-grid) gives **73.8 g CO₂e/kWh for 2024**; the 2025 webinar slides give **73**. The guideline says 84% of Ontario's electricity is carbon-free and links the rising intensity to more gas generation. A webinar slide headed "Historical Annual MEF" shows **343 g/kWh for 2024**; the slide wording is ambiguous (average vs marginal).
- **Check:** the 2024 average; the 2024 marginal factor and its definition (hourly, annual, or the average of marginal); the GWP basis; generation vs consumption basis.
- **Reliability:** an NGO analysis of IESO data, widely used in Ontario; method published. Medium-high.
- **Supports:** §7 (Ontario average and marginal), the benchmark brief (construction electricity for Sam).

### taf2021
**Reference:** The Atmospheric Fund, 2021. *A Clearer View of Ontario's Emissions: Electricity Emissions Factors and Guidelines, 2021 Edition*. [pdf] Toronto: TAF. Available at: https://taf.ca/custom/uploads/2021/11/20211116_TAF_Emissions-Factors-Guidelines.pdf.
- **Findings (secondary):** Gas generation factor **472 g CO₂e/kWh**; 2020 annual average **31 g/kWh**; recommends marginal factors for evaluating projects; says IESO forecasts imply factors trending upwards.
- **Reliability:** superseded by taf2025 for values. Used only for the gas-generation upper bound.

### ontario_energy_snapshot
**Reference:** Government of Ontario, n.d. *Ontario energy snapshot*. [online] Available at: https://www.ontario.ca/page/ontario-energy-snapshot [TO VERIFY year of update].
- **Findings (secondary):** **53 g/kWh for 2023**. This is the value used in the deck.
- **Check:** year, and whether it is a generation or consumption factor.
- **Reliability:** government page, but the method isn't stated. It conflicts with TAF (73.8 for 2024) and CER (35 for 2022); the gap may just be different years, since gas use rose. Synthesise in the report (R1.3).

### cer_ontario_profile
**Reference:** Canada Energy Regulator, n.d. *Provincial and Territorial Energy Profiles – Ontario*. [online] Available at: https://www.cer-rec.gc.ca/en/data-analysis/energy-markets/provincial-territorial-energy-profiles/provincial-territorial-energy-profiles-ontario.html.
- **Findings (secondary):** Grid intensity **35 g CO₂e/kWh generated, 2022**.
- **Reliability:** federal regulator; usually based on Canada's National Inventory Report. High once opened.

### ieso2024_energy_future
**Reference:** Independent Electricity System Operator, 2024. *Ontario's Energy Future: Spring 2024 Update*. [pdf] Toronto: IESO. Available at: https://www.ieso.ca/-/media/Files/IESO/Document-Library/Decarbonization-Hub/IESO-Ontarios-Energy-Future-Spring-2024.pdf.
- **Findings (secondary):** Grid intensity projected to fall to **about 15 g/kWh by 2040**.
- **Check:** the scenario and the exact figure. The Annual Planning Outlook may be the better primary for the trajectory.
- **Reliability:** system operator. High for the scenario, but it's a projection.

---

## NSW / NEM grid

### dcceew2025_ngaf
**Reference (incomplete):** Department of Climate Change, Energy, the Environment and Water, 2025. *Australian National Greenhouse Accounts Factors: 2025*. [pdf/xlsx] Canberra: DCCEEW. Available at: [URL TODO, dcceew.gov.au].
- **Findings (secondary):** NSW and ACT scope 2 (location-based) factor **0.64 kg CO₂e/kWh**. Seen in ASIC, *Sustainability reporting educational modules, Module 6 Unit 3* (https://download.asic.gov.au/media/xyzjc1f0/sustainability-reporting-educational-modules-module-6-unit-3.pdf), where it appears in a worked example.
- **Check:** the NSW and ACT scope 2 and scope 3 values, and the inventory year the 2025 factor is based on.
- **Reliability:** the official Australian factor once opened. Scope 2 excludes upstream (scope 3) emissions, so it is not a life-cycle factor (see the displacement caveats).

### aemo_cdeii
**Reference (incomplete):** Australian Energy Market Operator, 2025. *Carbon Dioxide Equivalent Intensity Index Procedures*. [pdf] Melbourne: AEMO. Available at: https://aemo.com.au/-/media/files/electricity/nem/settlements_and_payments/settlements/2025/carbon-dioxide-equivalent-intensity-index-procedures.pdf; and AEMO, n.d. *CDEII Available Generators File* [URL TODO].
- **Findings (secondary):** CDEII combines metered sent-out generation with generator emission factors. **Bayswater: 0.99 t CO₂e/MWh**, from 0.0989 t/GJ at 35.9% HHV sent-out efficiency. Source: Synergy, *Submission to IMO consultation on Emissions Intensity Index* (https://www.erawa.com.au/cproot/14788/2/Synergy%20submission%20re%20EII.pdf), quoting an older Available Generators File. No Liddell value was found.
- **Reliability:** AEMO's file is primary; the 0.99 figure is old and indirect. Medium.
- **Supports:** §7 upper bound.

### aer2021_liddell
**Reference:** Australian Energy Regulator, 2021. *Decision notice: AGL application, 30 April 2021*. [pdf] Available at: https://www.aer.gov.au/system/files/Decision%20notice%20-%20AGL%20application%2030%20April%202021.pdf.
- **Findings (secondary):** Approved AGL's swap of closure dates so the last Liddell unit would run to April 2023. News (Newcastle Herald; RenewEconomy) reports the final unit closed on **28 April 2023**; the station was 2,000 MW (4 × 500 MW).
- **Reliability:** AER primary for the plan; news for the actual date. AGL's own release would be better.
- **Supports:** §7. An SMR at Liddell displaces the NEM mix, not Liddell.

### aemo2024_isp / aemo2026_isp
**Reference (incomplete):** Australian Energy Market Operator, 2024. *2024 Integrated System Plan for the National Electricity Market*. Melbourne: AEMO. [URL TODO]. AEMO, 2026. *2026 Integrated System Plan* (final, June 2026). [URL TODO].
- **Findings (secondary):** Draft 2024 ISP Step Change carbon budget **681 Mt CO₂e** (AEMO webinar slides, https://www.aemo.com.au/-/media/files/major-publications/isp/2024/2024-isp-publication-webinar-presentation.pdf). Coal leaves the NEM entirely **by 2038** in the 2024 ISP (Ark Energy, *NSW Energy Market* briefing, August 2024: secondary). The 2026 ISP final was published around June 2026 (ESD News). No year-by-year emissions intensity was found.
- **Gap:** the Step Change emissions (Mt) and generation (TWh) by year, from the 2026 ISP inputs and assumptions workbook. They replace trajectory T1 in the scripts.
- **Reliability:** AEMO is the authoritative planner; Step Change is a scenario, not a forecast.

---

## Costs

### csiro2024_gencost2324
**Reference:** Graham, P., Hayward, J. and Foster, J., 2024. *GenCost 2023-24: Final report*. [pdf] Australia: CSIRO. Available at: https://www.csiro.au/-/media/Energy/GenCost/GenCost2023-24Final_20240522.pdf.
- **Findings (secondary):** First edition to include large-scale nuclear. It gives a development time of at least 15 years, with **deployment from 2040 at the earliest**, because Australia has no development pipeline and has legal, safety and security requirements to meet. Its capital cost assumes a continuous build programme after a higher-cost first unit. The 2030 SMR LCOE of **A$387–641/MWh (average A$514)** is attributed to "May" (the 2023-24 final) in trade press.
- **Check:** whether the 2040 statement covers SMRs or only large-scale nuclear; the SMR LCOE range and year.
- **Reliability:** national science agency, with AEMO. High.

### csiro2025_gencost2425
**Reference:** Graham, P., Hayward, J. and Foster, J., 2025. *GenCost 2024-25: Final report*. [pdf] Australia: CSIRO. Executive summary at: https://www.csiro.au/-/media/Energy/GenCost/GenCost2024-25Final_ES.pdf [full report URL TODO].
- **Findings (secondary):** Published 29 July 2025. SMR costs were aligned with Darlington, which fell inside GenCost's previous projected range; SMRs remain the highest-cost option. Wind and solar with storage and transmission remain the lowest-cost new build. A 2030 firmed wind and solar figure of about **A$102/MWh** (down from A$107) comes from trade press (ecogeneration).
- **Check:** the 2030 LCOE ranges (variable renewables with integration costs; SMR) and the WACC.

### csiro2026_gencost2526
**Reference (authors TO VERIFY):** Graham, P. and Hayward, J., 2026. *GenCost 2025-26: Final report*. [pdf] Australia: CSIRO. Available at: https://www.csiro.au/-/media/Energy/GenCost-2025-26-Final/GenCost_2025-26_Final_Report_20260715.pdf.
- **Findings (secondary):** Dated 15 July 2026; **the current edition, which should be the one the report cites**. It adds a System LCOE (SLCOE) metric and CSIRO's Simple Electricity Model. Nuclear cost trends are rising (turbine costs, US data-centre demand). SMRs remain the highest cost in the 2030 LCOE. The draft (16 Dec 2025) gave **A$91/MWh** as the average NEM cost at 82% renewables in 2030, including transmission (A$81 for generation only); this is a system average, not an LCOE.
- **Gap:** the 2030 SMR LCOE range, firmed-VRE LCOE/SLCOE, capital costs and build times. **Replace `smr_lcoe_aud` and `vre_firmed_lcoe_aud` with this edition's values.**

### kim_macfarlane2026
**Reference (TO VERIFY):** Kim, [initial] and Macfarlane, A., 2026. *Challenges of small modular reactors: a comprehensive exploration of [title TODO]*. [pdf] Available at: https://www.nirs.org/wp-content/uploads/2025/09/SMR-Costs_Challenges-of-SMRs-cost-waste_Kim-Macfarlane_2026.pdf.
- **Findings (secondary):** Cites CSIRO for an SMR LCOE of **A$198–349/MWh** (edition and year unknown).
- **Reliability:** hosted by an anti-nuclear NGO. Check whether it is peer-reviewed. Used only as a low-cost sensitivity.

### rba_f11
**Reference (incomplete):** Reserve Bank of Australia, 2025. *Historical Data: Exchange Rates (F11)*. [online] Sydney: RBA. Available at: [URL TODO, rba.gov.au].
- **Findings (secondary):** AUD→CAD mid-market rate **0.8938 on 12 May 2025** (Wise); 0.882–0.901 through May 2025 (freecurrencyrates). That gives **1.119 AUD per CAD**.
- **Check:** the RBA F11 rate for 8 May 2025.

---

## Life-cycle benchmarks (detail in `02_Research/briefs/benchmarks-for-sam.md`)

### unece2021
**Reference:** United Nations Economic Commission for Europe, 2021. *Carbon Neutrality in the UNECE Region: Integrated Life-cycle Assessment of Electricity Sources*. Geneva: United Nations. ISBN 978-92-1-117298-0 [TO VERIFY]. Available at: https://www.un-ilibrary.org/content/books/9789210014854.
- **Findings (secondary, several outlets agree):** Nuclear **5.1–6.4 g CO₂e/kWh**, the lowest of the technologies studied. Natural gas combined cycle **403–513**; hydropower 6–147; PV 8.0–83; CSP 27–122 (Nucleation Capital summary). Coal is reported as **751** (IGCC, USA) or **753 to 1095** depending on the outlet. No wind range was found. Covers 12 world regions; the printed edition is dated Geneva 2022.
- **Check:** the nuclear figure (which reactor and which region), the coal range, the wind range, and the GWP basis.

### ipcc2014_annex3
**Reference (TO VERIFY authors):** Schlömer, S. et al., 2014. Annex III: Technology-specific cost and performance parameters. In: *Climate Change 2014: Mitigation of Climate Change. Contribution of Working Group III to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change*. Cambridge: Cambridge University Press. [URL TODO, ipcc.ch].
- **Findings:** **None confirmed in the primary.** Run 7b (21/10) search leads, both secondary (Wikipedia's table citing IPCC 2014; LowCarbonPower blog reproducing the IPCC table): nuclear **min 3.7, median 12, max 110** g CO₂eq/kWh; coal (pulverised) **740 / 820 / 910**. The same blog shows a second coal set (670/760/870) under another heading, so the table must be opened to confirm which is Annex III. A 2026 arXiv preprint (not peer-reviewed; https://arxiv.org/pdf/2608.29717) says it checked coal at 820 and gas at 490 against the IPCC PDF.
- **Reference to complete:** the full author list and page range of Annex III from the chapter title page (only "Schlömer, S. et al." is confirmed). Table A.III.2 is the life-cycle table to cite.
- **Use:** benchmark (min/median/max) once Table A.III.2 is opened; until then stress test only, with [TO VERIFY].

### nrel2021_lca
**Reference:** National Renewable Energy Laboratory, 2021. *Life Cycle Greenhouse Gas Emissions from Electricity Generation: Update*. [pdf] Golden, CO: NREL. NREL/FS-6A50-80580 [TO VERIFY report number]. Available at: https://www.nrel.gov/docs/fy21osti/80580.pdf.
- **Findings (secondary):** Reviews about 3,000 LCAs and replaces the 2013 fact sheet; builds on the 2012 LCA Harmonization Project. CleanTechnica (2012) reports harmonised nuclear medians of **12–13 g CO₂e/kWh** (PWR and BWR). The 2021 nuclear median was not seen.
- **Check:** Figure 2 of the fact sheet (min, quartiles, median, max by technology) and the GWP basis.

---

## From analyst run 2


# Sources: analyst run 2 (law, regulation, licensing, party positions, route to practice for C1), 20/10/2026

To be merged into `02_Research/sources.md` by the coordinator. Each entry gives the Harvard reference, key findings, numbers, reliability, verification status and the section it supports. Parameter keys refer to `03_LCA_Calculations/parameters_run2.yaml`.

**Verification status for this whole file.** No source host could be opened from this session. WebFetch failed at DNS for legislation.gov.au, austlii.edu.au, aph.gov.au, cnsc-ccsn.gc.ca, claytonutz.com and en.wikipedia.org. curl got a proxy 403 for every host tried. Everything below comes from search-engine extracts, most of them restricted to the named primary domain. Under CLAUDE.md ("never cite from memory or a search snippet"), **none of these can be cited until a person opens the page and confirms it.** Quoted statutory words are as the extract gave them and must be checked against the Federal Register of Legislation (Commonwealth) or the state register. Each entry says what to check. Priority checks are marked **P1**.

Reliability scale: **Primary** (legislation, regulator, parliament, the company's own filing or release); **Secondary-good** (law firm, peer-reviewed, trade press citing a primary); **Secondary-weak** (news or advocacy: a pointer only).

---

## A. Australian legislation

### EPBC_Act_s140A (P1)
Australian Government, 1999 (as amended). *Environment Protection and Biodiversity Conservation Act 1999* (Cth), s 140A 'No approval for certain nuclear installations'. [online] Federal Register of Legislation, C2004A00485. Available at: https://www.legislation.gov.au/C2004A00485/latest/text [Accessed 20 October 2026; not opened]. Pointer: AustLII consolidation, https://classic.austlii.edu.au/au/legis/cth/consol_act/epabca1999588/s140a.html.
- **Findings (extract):** s 140A(1): "The Minister must not approve an action consisting of or involving the construction or operation of any of the following nuclear installations: (a) a nuclear fuel fabrication plant; (b) a nuclear power plant; (c) an enrichment plant; (d) a reprocessing facility." A carve-out stops paragraph (1)(b) applying to a "naval nuclear propulsion plant related to use in a conventionally-armed, nuclear-powered submarine". The parallel bars are s 37J (no declarations relating to nuclear actions) and s 146M (no approvals under strategic assessments). Clayton Utz (2025) also lists s 305(2)(d).
- **Status caveat:** The *Environment Protection Reform Act 2025* (assented 1 December 2025, commencing in stages to 1 December 2026) renamed "nuclear action" as "radiological exposure action" (Norton Rose Fulbright, 2025). No source seen says whether s 140A was renumbered or reworded. **Check the current compilation and its date.**
- **Reliability:** Primary, once opened.
- **Supports:** §3 (barriers), §8.1; slide 10.

### ARPANS_Act_s10 (P1)
Australian Government, 1998 (as amended). *Australian Radiation Protection and Nuclear Safety Act 1998* (Cth), s 10 'Prohibition on certain nuclear installations'. [online] Federal Register of Legislation, C2004A00383. Available at: https://www.legislation.gov.au/C2004A00383/latest/text [Accessed 20 October 2026; not opened]. Pointer: https://classic.austlii.edu.au/au/legis/cth/consol_act/arpansa1998487/s10.html.
- **Findings (extract):** s 10(1): nothing in the Act "is to be taken to authorise the construction or operation" of a nuclear fuel fabrication plant, a nuclear power plant, an enrichment plant or a reprocessing facility. s 10(1A) excludes naval nuclear propulsion plants for conventionally armed nuclear-powered submarines. s 10(2): "the CEO must not issue a licence under section 32 in respect of any of the facilities mentioned in subsection (1)."
- **Note:** The search returned a 2011 compilation as the Register's top hit. **Open the latest compilation.**
- **Reliability:** Primary, once opened.
- **Supports:** §3, §8.1; slide 10.

### ARPANSA_WhoWeRegulate (P1)
ARPANSA, n.d. *Who we regulate*. [online] Australian Radiation Protection and Nuclear Safety Agency. Available at: https://www.arpansa.gov.au/regulation-and-licensing/regulation/about-regulatory-services/who-we-regulate [Accessed 20 October 2026; not opened]. Companion page: ARPANSA, n.d. *Do I need a licence?* Available at: https://www.arpansa.gov.au/regulation-and-licensing/licensing/information-for-licence-applicants/do-i-need-a-licence.
- **Findings (extract):** The Act applies to "controlled persons": Commonwealth entities (departments; bodies set up for a public purpose under an Act, e.g. CSIRO and ANSTO; companies in which the Commonwealth holds a controlling interest) and their employees and contractors. Non-Commonwealth entities are regulated by state and territory regulators, not ARPANSA. The "Do I need a licence?" page repeats the s 10 prohibition.
- **Why it matters:** ARPANSA could only license a power reactor owned or controlled by the Commonwealth. The Coalition's 2024 plan was for Commonwealth-owned plants, which is why s 10 bites on that model. A privately owned SMR (e.g. at AGL's Liddell site) would fall to NSW, where the 1986 Act bans it.
- **Reliability:** Primary (regulator's own guidance), once opened. **Also confirm the definition of "controlled person" in ARPANS Act s 13.**
- **Supports:** §8.1.

### NSW_UMNFP_Act_1986 (P1)
New South Wales Government, 1986 (as amended). *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW), No 194, ss 8–9. [online] NSW Legislation. Available at: https://legislation.nsw.gov.au/view/whole/html/inforce/current/act-1986-194 [Accessed 20 October 2026; not opened].
- **Findings (extract):** s 8(2) makes it an offence to construct or operate a nuclear facility (current maximum penalty given as 1,000 penalty units). "Nuclear facility" (s 8(1)) includes "a nuclear reactor, whether or not designed for the purpose of generating electricity", plus enrichment, fabrication, reprocessing and storage installations. s 8(3) exceptions: the former Australian Atomic Energy Commission and its Commonwealth successors under a Commonwealth Act, research or medical waste facilities, and nuclear-powered vessels. s 9: nothing in any other Act authorises a state authority, including an electricity generator, to construct, operate, approve or permit a nuclear reactor for generating electricity.
- **Numbers:** maximum penalty 1,000 penalty units (`nsw_s8_max_penalty`).
- **Reliability:** Primary, once opened. **Check the s 8(3) wording: the "Commonwealth successor" exception could matter for a Commonwealth-owned plant.**
- **Supports:** §8.1 (the Liddell case).

### NSWParl_RepealBill2025 (P1)
Parliament of New South Wales, 2025–26. *Uranium Mining and Nuclear Facilities (Prohibitions) Repeal Bill 2025*: bill details. [online] Available at: https://www.parliament.nsw.gov.au/bills/Pages/bill-details.aspx?pk=18833 [Accessed 20 October 2026; not opened]. First print: https://www.parliament.nsw.gov.au/bill/files/18833/First%20Print.pdf.
- **Findings (extract):** A private member's bill (John Ruddick MLC, Libertarian), introduced 19 November 2025. It repeals the 1986 Act and amends the *Mining Act 1992* (s 10A) and the *Land and Environment Court Act 1979*. It passed the Legislative Council on 6 May 2026, unamended. Status: "In Legislative Assembly".
- **Numbers:** dates in `nsw_repeal_bill_*`.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1.

### NSWParl_LANoticePaper_2026
Parliament of New South Wales, Legislative Assembly, 2026. *Notice Paper* (business of the House) [number and date TO VERIFY]. [pdf] Available at: https://files.parliament.nsw.gov.au/fileapi/ParlFiles/GetArtifact/170%20NOM%20(combined).pdf?serverRelativeUrl=%2Fhp%2Fhousepaper%2F31312%2F170+NOM+%28combined%29.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** The bill is listed as awaiting its second reading speech: "Reported 27 May 2026 — Mr Roy Butler; lapses 28 November 2026".
- **Reliability:** Primary, once opened. The search engine itself flagged an inconsistent date in one notice paper, so check the latest paper.
- **Supports:** §8.1.

### NSW_Labor_UraniumPosition_2026
Australian Resources Review / ARR News, 2026. 'Liberal-Nationals backing nuclear, dithering on gas: Houssos', 8 May. [online] Available at: https://arr.news/2026/05/08/liberal-nationals-backing-nuclear-dithering-on-gas-houssos/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** All Liberal and National MLCs voted for the repeal bill. The Minns Labor Government opposed it in the Council and is expected to oppose it in the Assembly. A Labor statement says "NSW Labor has a long-standing position opposing uranium mining in this state and that has not changed."
- **Reliability:** Secondary-weak. **Replace with NSW Hansard for 6 May 2026 (LC division list).**
- **Supports:** §8.1.

### VIC_NAP_Act_1983
Victorian Government, 1983 (as amended). *Nuclear Activities (Prohibitions) Act 1983* (Vic), No 9923, s 8. [online] Victorian Legislation. Available at: https://www.legislation.vic.gov.au [exact URL TO VERIFY] [Accessed 20 October 2026; not opened]. Pointer: AustLII, https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/vic/consol_act/naa1983337/.
- **Findings (extract):** s 8 prohibits constructing or operating certain facilities, including nuclear reactors and nuclear power reactors, enrichment, conversion, fuel fabrication and reprocessing facilities. The exceptions were truncated in the extract.
- **Reliability:** Primary, once opened. The extract seen was a 2010 version. Premier Allan told Parliament on 1 April 2025 that Victoria's nuclear-free status dates from Labor legislation (Victorian Hansard, https://www.parliament.vic.gov.au/parliamentary-activity/hansard/hansard-details/HANSARD-2145855009-30321).
- **Supports:** §8.1 (Loy Yang stretch case only).

### QLD_NFP_Act_2007
Queensland Government, 2007 (as amended). *Nuclear Facilities Prohibition Act 2007* (Qld). [pdf] Queensland Legislation. Available at: https://www.legislation.qld.gov.au/view/pdf/inforce/current/act-2007-004 [Accessed 20 October 2026; not opened].
- **Findings (extract):** Prohibits constructing or operating a nuclear facility (maximum 1,665 penalty units). s 21: if the Minister is satisfied the Commonwealth has taken, or is likely to take, a step supporting or allowing a prohibited facility in Queensland, the Minister must take steps to hold a plebiscite.
- **Reliability:** Primary, once opened. The version seen was "current as at 3 July 2017".
- **Supports:** §8.1 (state veto points; Tarong and Callide).

### StateBans_Summary
Holding Redlich, n.d. *Nuclear law: Could Australia go nuclear?* [online] Available at: https://www.holdingredlich.com/nuclear-law-could-australia-go-nuclear [Accessed 20 October 2026; not opened]. The Parliamentary Library quick guide that this entry used to list is now a single entry, **APH_2024** (run 7b merge; factcheck B11).
- **Findings (extract):** South Australia has no ban on nuclear power plants, but its *Nuclear Waste Storage Facility (Prohibition) Act 2000* bans waste storage facilities and public funding for them. WA's *Nuclear Waste Storage and Transportation (Prohibition) Act 1999* bans storing and transporting certain nuclear waste; a 2007 WA bill to ban power plants did not pass. Tasmania and the ACT have no state-level power or waste bans.
- **Reliability:** The Parliamentary Library guide (APH_2024) is Primary-adjacent (parliamentary research) and should be the one cited for the state table; the law firm is Secondary-good.
- **Supports:** §8.1 (table of jurisdictions).

---

## B. Australian Parliament and party positions

### APH_SenateComposition_2026 (P1)
Parliament of Australia, 2026. *Senate composition*. [online] Available at: https://www.aph.gov.au/Senators_and_Members/Senators/Senate_composition [Accessed 20 October 2026; not opened].
- **Findings (extract):** As at 14/05/2026: ALP 30, Coalition 27, Greens 10, One Nation 4, plus Babet, Lambie, Payman, Pocock and Thorpe (one each). Total 76.
- **Numbers:** `senate_*`. The script checks that the parts sum to 76.
- **Reliability:** Primary, once opened. Check for any change after May 2026.
- **Supports:** §8.1 (repeal arithmetic).

### AEC_2025_Report
Australian Electoral Commission, 2025. *2025 federal election report*. [pdf] Canberra: AEC. Available at: https://www.aec.gov.au/Elections/federal_elections/2025/2025-Federal-Election-Report.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** House of Representatives: ALP 94 of 150 seats, Coalition 43 (Liberal 18, LNP 16, Nationals 9). Results as at the return of the writs, 12 June 2025.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1.

### ABC_2024_SevenSites
ABC News, 2024. 'Peter Dutton reveals seven sites for proposed nuclear power plants', 19 June. [online] Available at: https://www.abc.net.au/news/2024-06-19/dutton-reveals-seven-sites-for-proposed-nuclear-power-plants/103995310 [Accessed 20 October 2026; not opened].
- **Findings (extract):** The seven sites are Liddell and Mount Piper (NSW), Loy Yang (Vic), Tarong and Callide (Qld), Northern (SA, SMR only) and Muja (WA, SMR only). The plants would be Commonwealth-owned. First power 2035 with SMRs or 2037 with large plants. The article quotes CSIRO's view that "the earliest deployment would be from 2040".
- **Reliability:** Secondary-weak (news). **Find the Coalition's 19 June 2024 media release (liberal.org.au archive) and cite that instead.** For the CSIRO quote, cite GenCost (run 1's key), not the ABC.
- **Supports:** §3, §8.1; plan D4.

### ABC_2026_CoalitionEnergyPlan
ABC News, 2026. 'Coalition vows to "take a chainsaw" to climate laws and offshore wind', 23 September. [online] Available at: https://www.abc.net.au/news/2026-09-23/coalition-energy-plan-scrap-renewables-climate-laws/107184376 [Accessed 20 October 2026; not opened].
- **Findings (extract):** An eight-point plan under leader Angus Taylor. It would revoke four offshore wind zones and "repeal all legislative prohibitions on nuclear energy". The ABC notes this needs the Senate, where the Coalition has "no chance" without Labor or the Greens changing position. It also urges states to reconsider their bans (AI data centres are given as the rationale).
- **Reliability:** Secondary-weak. Pair with the party's own page (next entry).
- **Supports:** §8.1.

### Liberal_2026_EnergyPlan (P1)
Liberal Party of Australia, 2026. *Our Plan for Cheaper Power*. [online] Available at: https://www.liberal.org.au/our-plan/energy [Accessed 20 October 2026; not opened].
- **Findings (extract):** Commitments include lifting the nuclear ban, scrapping net zero mandates and doubling fuel reserves to 60 days, "under a Taylor-led Coalition government".
- **Reliability:** Primary for the party's position, once opened. **Check whether the seven 2024 sites are still named.** In October 2025 Ted O'Brien would not confirm a role for them (ABC, 4 October 2025).
- **Supports:** §8.1.

### ABC_2025_DeputyLeaderNuclear
ABC News, 2025. 'Deputy leader confident nuclear will be part of Coalition's energy policy', 4 October. [online] Available at: https://www.abc.net.au/news/2025-10-04/deputy-opposition-leader-confident-nuclear-in-energy-policy-mix/105848854 [Accessed 20 October 2026; not opened]. Related: AAP, 2025, 'Nuclear policy fate still unclear after coalition talks'.
- **Findings (extract):** After the May 2025 election the Liberals gave in-principle support to removing the federal moratorium as part of re-forming the Coalition with the Nationals. That stops short of the seven-plant policy. The 2026 Liberal leadership spill (13 February 2026) made Angus Taylor leader [TO VERIFY via the APH or party source].
- **Reliability:** Secondary-weak. Use only to describe the 2025 transition.
- **Supports:** §8.1.

### Bowen_Statements
Bowen, C., 2025. *Joint media release: Experts agree: nuclear only getting more expensive, slower for Australia's energy needs*. [online] Canberra: Minister for Climate Change and Energy. Available at: https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-experts-agree-nuclear-only-getting-more-expensive-slower-australias-energy-needs [Accessed 20 October 2026; not opened; date TO VERIFY]. Also: Bowen, C., *Speech to National Press Club* (date TO VERIFY), https://minister.dcceew.gov.au/bowen/speeches/speech-national-press-club-canberra-act.
- **Findings (extract):** The Government cites GenCost for first nuclear power "well into the 2040s". It says voters "thoroughly rejected" the Coalition's nuclear scheme, and that the policy would cause an "investment chill".
- **Reliability:** Primary for the Government's position, once opened. The dates are about one to two years old. No 2026 Labor statement was found.
- **Supports:** §8.1 (Labor position).

### Greens_2025_Plan
Australian Greens, 2025. *2035: Powering Past Coal & Gas* [title TO VERIFY]. [pdf] Available at: https://cdn.greens.org.au/cdn/ff/fk0q_VgBQA5t00ZlhkPcF6i2IEZByQHBjpMq1g6YdVQ/1744244709/public/2025-04/2035%20Powering%20Past%20Coal%20&%20Gas.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** "The Greens will vote to keep the prohibition on nuclear in our environment laws." A policy page states that nuclear fission "has no future in Australia".
- **Reliability:** Primary for the party's position, once opened.
- **Supports:** §8.1.

### SenateECLC_2023_NuclearProhibitions
Senate Environment and Communications Legislation Committee, 2023. *Environment and Other Legislation Amendment (Removing Nuclear Energy Prohibitions) Bill 2022 [Provisions]*. [online] Canberra: Parliament of Australia. Available at: https://www.aph.gov.au/Parliamentary_Business/Committees/Senate/Environment_and_Communications/Nuclearprohibitions [Accessed 20 October 2026; not opened].
- **Findings (extract):** A private senator's bill (Canavan and eight co-sponsors) to remove the prohibitions, referred on 27 October 2022. The report, tabled 11 August 2023, recommended that the bill not be passed; Coalition senators dissented. The Parliamentary Library said it would lapse at prorogation of the 47th Parliament.
- **Reliability:** Primary, once opened. **Confirm the lapse on the bill's ParlInfo page.**
- **Supports:** §8.1 (history of repeal attempts).

### NFCF_Bill_2017_EM
Parliament of Australia, 2017. *Nuclear Fuel Cycle (Facilitation) Bill 2017: Explanatory Memorandum*. [online] Available at: https://classic.austlii.edu.au/au/legis/cth/bill_em/nfcb2017288/memo_0.html [Accessed 20 October 2026; not opened].
- **Findings (extract):** Proposed repealing ARPANS s 10. Outcome not confirmed.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1 (one line: repeal has been attempted repeatedly).

### HouseSelectCttee_2025_Interim
House of Representatives Select Committee on Nuclear Energy, 2025. *Interim report* [title TO VERIFY]. Canberra: Parliament of Australia. Pointer: The Conversation (2025), 'New report skewers Coalition's contentious nuclear plan', https://theconversation.com/new-report-skewers-coalitions-contentious-nuclear-plan-and-reignites-australias-energy-debate-250912 [Accessed 20 October 2026; not opened].
- **Findings (extract):** The (Labor-majority) interim report concluded that nuclear "is not a viable option for Australia's energy needs", citing deployment time and cost. Whether a final report was tabled before the 2025 election is not confirmed.
- **Reliability:** Primary, once the report itself is opened. It is a political committee, so give its majority and dissent.
- **Supports:** §8.1 (optional).

### Twomey_2025_Override
Canberra Times, 2025. 'Dutton's nuclear power plan faces legal hurdles' [date TO VERIFY]. [online] Available at: https://www.canberratimes.com.au/story/8851241/duttons-nuclear-power-plan-faces-legal-hurdles/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** Professor Anne Twomey says the Commonwealth would have to legislate both to remove its own ban and to override the state bans. Under Constitution s 109 a valid federal law prevails over an inconsistent state law; the trading-corporations power (as used for NBN Co and Snowy Hydro) could support a Commonwealth corporation building and running plants. William Partlett warns of a High Court challenge.
- **Reliability:** Secondary-good (named constitutional experts quoted in news). For the report, cite s 109 itself and attribute the opinion to Twomey as quoted.
- **Supports:** §8.1 (what repeal would require).

### Minns_StateBan
Canberra Times, n.d. ''Nightmare scenario': states slam Dutton's nuclear plan' [date TO VERIFY]. [online] Available at: https://www.canberratimes.com.au/story/8668232/nightmare-scenario-states-slam-duttons-nuclear-plan/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** Premier Minns says the NSW prohibition will not be removed "under his watch", and argues nuclear would put at risk "$30-odd billion of private capital invested in renewable energy".
- **Reliability:** Secondary-weak. Look for a NSW Premier media release or Hansard.
- **Supports:** §8.1 (Liddell).

### AGL_Liddell_NoNuclear
Newcastle Herald, [2024, TO VERIFY]. 'AGL says Liddell site will not be used for nuclear power'. [online] Available at: https://www.newcastleherald.com.au/story/8557276/agl-says-liddell-site-will-not-be-used-for-nuclear-power [Accessed 20 October 2026; not opened].
- **Findings (extract):** AGL chief executive Damien Nicks: "As the owner of these sites, nuclear energy is not a part of these plans… There is no viable schedule for the regulation or development of nuclear energy in Australia." AGL is building a 500 MW / 1,000 MWh battery at Liddell (full operation early 2026 per RenewEconomy).
- **Reliability:** Secondary-weak. **Find the primary: an AGL ASX announcement or FY24 results briefing transcript.**
- **Supports:** §8.1, §8.5 (site owner as veto player); R4.3 (the grid-connection reuse idea meets the site owner's own plans).

### DefenceMin_2025_ANNPSR
Minister for Defence, 2025. *An AUKUS milestone – launch of the Australian Naval Nuclear Power Safety Regulator*, 1 November. [online] Available at: https://www.minister.defence.gov.au/media-releases/2025-11-01/aukus-milestone-launch-australian-naval-nuclear-power-safety-regulator [Accessed 20 October 2026; not opened]. Also: ARPANSA, 2025, *ARPANSA supports new naval nuclear power safety regulator*, https://arpansa.gov.au/arpansa-supports-new-naval-nuclear-power-safety-regulator.
- **Findings (extract):** The ANNPSR was established under the *Australian Naval Nuclear Power Safety Act 2024* and began operating on 1 November 2025. ARPANSA's HMAS Stirling licences transferred to it automatically.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1 (evidence that Australia can stand up a new nuclear regulator, and how long it took).

### APH_BillsDigest32_2023_24
Parliamentary Library, 2023. *Australian Naval Nuclear Power Safety Bill 2023* [and related bill], Bills Digest No. 32, 2023–24. [online] Available at: https://aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd2324a/24bd32 [Accessed 20 October 2026; not opened].
- **Use:** The bill's introduction date gives the "bill to operating regulator" interval [TODO: open it].
- **Supports:** §8.1.

### IAEA_Milestones
International Atomic Energy Agency, [2015 (Rev. 1) or later Rev. 2, TO VERIFY]. *Milestones in the Development of a National Infrastructure for Nuclear Power*. IAEA Nuclear Energy Series No. NG-G-3.1. [pdf] Vienna: IAEA. Available at: https://www-pub.iaea.org/MTCD/Publications/PDF/Pub1704_web.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** Three phases (before deciding; preparatory work after a policy decision; implementing the first plant), three milestones, 19 infrastructure issues including a legal framework and an independent regulator. Phase durations "depend on the degree of commitment and resources". **The often-quoted "10–15 years" figure was NOT found in the extract; do not use it unless found in the document.**
- **Reliability:** Primary, once opened.
- **Supports:** §8.1, §8.6 (the framework for Australia's route).

---

## C. Canada: licensing, codes, finance, procurement

### CNSC_DNNP_Page (P1)
Canadian Nuclear Safety Commission, 2026. *Darlington New Nuclear Project*. [online] Ottawa: CNSC. Available at: https://www.cnsc-ccsn.gc.ca/eng/reactors/new-reactor-power-plant-projects/new-reactor-power-plant-facilities/darlington-new-nuclear-project/ [Accessed 20 October 2026; not opened]. Also the project timeline page: .../darlington-new-nuclear-project/project-timeline/.
- **Findings (extract):** The CNSC began the EA in May 2007, run by a joint review panel together with the site-licence application. The licence to prepare site was issued on 17 August 2012. The licence to construct application was made in October 2022, "submitted in a number of packages over the course of several months". OPG "applied for 1 unit construction, with possibility of a future application for up to 3 additional units". The licence was issued April 2025, valid to 31 March 2035, with three regulatory hold points. In March 2026 OPG applied for a 20-year licence to operate, with a decision to follow a public hearing.
- **Reliability:** Primary, once opened.
- **Supports:** §4.2 (Leroy), §8.1, §8.6.

### CNSC_2025_LTCDecision (P1)
Canadian Nuclear Safety Commission, 2025. *Commission authorizes Ontario Power Generation Inc. to construct 1 BWRX-300 reactor at the Darlington New Nuclear Project site*, news release, 4 April. [online] Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html [Accessed 20 October 2026; not opened]. Companion: *Decision by the Commission…* (same date).
- **Findings (extract):** Licence PRCL 32.00/2035, valid to 31 March 2035, with four facility-specific licence conditions. It "does not authorize the operation". The two-part hearing ran virtually on 2 October 2024 and in person in Ajax on 8–10, 13 and 14 January 2025.
- **Reliability:** Primary, once opened. For the report, cite the Commission's *Record of Decision* (DEC 24-H3 [TO VERIFY number]) if it can be found.
- **Supports:** §8.1; slide 10.

### CNSC_RHP_Page
Canadian Nuclear Safety Commission, 2026. *Regulatory hold points for new reactor facilities*. [online] Available at: https://www.cnsc-ccsn.gc.ca/eng/reactors/regulatory-hold-points/new-reactors/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** RHP-1 is installation of the reactor building foundation, RHP-2 installation of the reactor pressure vessel, RHP-3 fuel-out commissioning. Removal authority was delegated to the CNSC Executive Vice-President and Chief Regulatory Operations Officer. "March 30, 2026: First regulatory hold point lifted for the Darlington New Nuclear Project."
- **Reliability:** Primary, once opened. OPG's project page has a conflicting "May 2025" RHP-1 entry; prefer the CNSC.
- **Supports:** §8.1, §8.6 (hold points as the natural gate for qualifying a new concrete).

### CNSC_2021_LPTSRenewal
Canadian Nuclear Safety Commission, 2021. *CNSC renews Ontario Power Generation's site preparation licence for its Darlington New Nuclear Project*, 12 October. [online] Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2021/10/cnsc-renews-ontario-power-generations-site-preparation-licence-for-its-darlington-new-nuclear-project.html [Accessed 20 October 2026; not opened].
- **Findings (extract):** Hearing held 10–11 June 2021. The renewed licence is valid to 11 October 2031.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1.

### CNSC_REGDOC_3_5_1
Canadian Nuclear Safety Commission, [2022?, TO VERIFY]. *REGDOC-3.5.1, Licensing Process for Class I Nuclear Facilities and Uranium Mines and Mills*, Version 2.1. [online] Available at: https://www.cnsc-ccsn.gc.ca/eng/acts-and-regulations/regulatory-documents/published/html/regdoc3-5-1-v2-1/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** Timelines set in regulation (24 months) apply to licences to prepare site. Expected review times for later stages are given in a table: the extract reads 32 months for a Class IA licence to construct, but another row reads 24 months and the extract was ambiguous.
- **Reliability:** Primary, once opened. **P1 if the 32-month comparison is used.**
- **Supports:** §8.1 (benchmark for the 29 months OPG took).

### CNSC_FAQ_NewReactors
Canadian Nuclear Safety Commission, n.d. *New reactor facility projects: FAQ*. [online] Available at: https://www.cnsc-ccsn.gc.ca/eng/resources/frequently-asked-questions/new-reactor-facilities/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** The two-part hearing takes about four months, and the Commission's decision can take up to 90 days after it. The duration depends on the environmental review, completeness of the application and open safety issues.
- **Reliability:** Primary, once opened.
- **Supports:** §8.1.

### GEH_NEDO33926 (P1 for C1)
GE-Hitachi Nuclear Energy, 2024. *BWRX-300 Steel-Plate Composite Containment Vessel (SCCV) and Reactor Building Structural Design*, NEDO-33926, Revision 2 (non-proprietary), 16 August. [pdf] US NRC ADAMS ML24110A134. Available at: https://www.nrc.gov/docs/ML2411/ML24110A134.pdf [Accessed 20 October 2026; not opened]. Also filed on the CNSC hearing record as CMD 24-H3 reference 2.5.45 (proprietary NEDC-33926P Rev. 2): https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD-24-H3-Ref-2-5-45-GEH-NEDC-33926P-BWRX-300-Steel-Plate-Composite-Containment-Vessel-SCCV-and-Reactor-Building-Structural-Design-Rev-2.pdf/object.
- **Findings (extract):** The topical report asks for NRC approval and CNSC acceptance of the diaphragm-plate steel-composite (DP-SC) approach for the containment vessel and reactor building. Non-containment DP-SC structures follow ANSI/AISC N690 (modified; the draft N690 N9.1.1(e) is cited). Containment criteria are adapted from the ASME Boiler and Pressure Vessel Code. Revision 2, Section 5.2.1, specifies "that self-consolidating concrete is used in the integrated RB DP-SC modules", with infill compressive strength "a function of reinforcement ratio per draft ANSI/AISC N690-XX". Self-consolidating concrete was used in the NRIC Phase 1 tests.
- **Why it matters for C1:** The infill concrete is specified through a code path that both regulators reviewed, built on AISC N690 and ASME, not mainly CSA N287. Any LC3 infill must meet the topical report's concrete requirements, or be justified as an equivalent through OPG's design-change process with CNSC oversight. **Check Section 6.2.1 "Concrete Infill" for cement type limits.**
- **Reliability:** Primary (vendor's licensing submission), once opened.
- **Supports:** §4.3, §5, §8.1, §8.6, §10.

### NRC_CNSC_2025_JointReport
US Nuclear Regulatory Commission and Canadian Nuclear Safety Commission, 2025. *CNSC–NRC Joint Report on GEH BWRX-300 Steel-Plate Composite Containment Vessel and Reactor Building Structural Design Topical Report*. ADAMS ML25325A075. [pdf] Available at: https://www.nrc.gov/docs/ML2532/ML25325A075.pdf [Accessed 20 October 2026; not opened]. Related: NRC (2024), *Safety evaluation… NEDO-33926*, ML24220A017.
- **Findings (extract):** The topical report gives an acceptable way to meet both regulators' requirements for DP-SC modules. It follows existing codes where they exist and fills the gaps with draft codes and test results.
- **Reliability:** Primary, once opened. **Find any conditions or limitations on materials.**
- **Supports:** §8.1, §8.6.

### CSA_N287_N291
CSA Group, 2024. *CSA N287.1:24, General requirements for concrete containment structures for nuclear power plants*; CSA Group, [2017?]. *CSA N287.2, Material requirements for concrete containment structures for nuclear power plants*; CSA Group, 2019 (R2024). *CSA N291:19, Requirements for nuclear safety-related structures*. [online] Toronto: CSA Group. Available at: https://www.csagroup.org/store/product/CSA_N287.1:24/ and https://www.csagroup.org/store/product/CSA%20N291:19/ [Accessed 20 October 2026; store pages not opened; standards are paywalled].
- **Findings (extract):** N287.2 sets materials requirements (concrete, reinforcement, steel components, liners, sealants) for **concrete** containment structures and is used together with N287.1. N291 covers safety-related structures of structural steel, reinforced concrete and reinforced masonry; its minimum design requirements follow CSA A23.3, S16, S304.1 and the National Building Code, with additional requirements referencing N287 and N289. CNSC REGDOC-2.5.2 lists A23.3 and N291 among related standards.
- **Implication (analyst inference, TO VERIFY):** The BWRX-300 containment is steel-plate composite, not a concrete containment, so N287 may not govern it directly. N291 is the likely Canadian standard for the safety-related reactor building and shafts. N291 in turn points to CSA A23.1/A23.2 and CSA A3001 for concrete materials. **Ask OPG or CNSC which standards the Licence Conditions Handbook names for DP-SC and shaft concrete.**
- **Reliability:** Primary (standards), but only scope statements were seen.
- **Supports:** §5, §8.1, §8.6.

### Hooton_2023_ACI
Hooton, R.D., 2023. *Changes to ASTM cement and concrete standards to…* [title truncated, TO VERIFY]. ACI Fall 2023 webinar slides. [pdf] Farmington Hills: American Concrete Institute. Available at: https://www.concrete.org/portals/0/files/pdf/webinars/ws_F23_NEU_DouglasHooton.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** "CSA A3001/ASTM C595/AASHTO M240 allow Type IT cements with up to 15% limestone together with any SCM including calcined clay." "Limestone contents higher than 15% would require a change." The performance specification ASTM C1157 would allow all LC3 combinations, but most US agencies do not accept it.
- **Why it matters:** An LC3 recipe with no more than 15% limestone fits an existing Canadian cement type, so the barrier is nuclear qualification, not the cement standard. A recipe with more limestone needs a standards change.
- **Reliability:** Secondary-good (a leading Canadian cement-standards researcher). Confirm against CSA A3001:23.
- **Supports:** §5, §8.6, §10.

### CSA_A3000_23
CSA Group, 2023. *CSA A3000:23, Cementitious materials compendium* (includes CSA A3001:23, *Cementitious materials for use in concrete*). [online] Available at: https://www.csagroup.org/store/product/2430659/ [Accessed 20 October 2026; not opened; paywalled].
- **Findings (extract):** Portland-limestone cements are capped at 15% limestone and designated GU, GUb, GUL and GULb, aligned with MSb and HSb for sulfate resistance.
- **Reliability:** Primary standard; contents seen only in a secondary extract.
- **Supports:** §5, §8.6.

### IJCSM_2026_NPPConcrete
[Authors TO VERIFY], 2026. 'Systematic evaluation of concrete placement reliability in heavily reinforced nuclear structures'. *International Journal of Concrete Structures and Materials* [journal TO VERIFY from DOI prefix s40069]. Available at: https://link.springer.com/article/10.1186/s40069-026-00964-8 [Accessed 20 October 2026; not opened].
- **Findings (extract):** Fly ash and ground granulated blast-furnace slag "are widely adopted in NPP concrete mixes" to cut heat of hydration and improve durability. "High replacement levels" are common in massive NPP concrete, which complicates control of the fresh concrete.
- **Reliability:** Secondary-good (peer-reviewed), once opened.
- **Authors (factcheck L17, A14):** still not found. Run 7b searched the DOI suffix and the title (21/10): no hit. The DOI should be 10.1186/s40069-026-00964-8; open the Springer page for the author list. If it cannot be completed by Q19, cut the citation or replace it with a peer-reviewed slag-in-nuclear-concrete source.
- **Supports:** §5, §8.6 (precedent: blended binders are normal in nuclear concrete; calcined clay is not yet).

### CIB_2022_Loan
Canada Infrastructure Bank, 2022. *CIB commits $970 million towards Canada's first Small Modular Reactor (SMR)*. [online] Toronto: CIB. Available at: https://cib-bic.ca/en/medias/articles/cib-commits-970-million-towards-canadas-first-small-modular-reactor/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** CAD 970 m, the CIB's largest clean-power investment to date, for Phase 1: design, site preparation, procurement of long-lead equipment and utility connections.
- **Reliability:** Primary, once opened.
- **Supports:** §8.2, §8.6.

### CGF_BOF_2025 (P1 for C1)
Canada Growth Fund and Building Ontario Fund, 2025. *Canada Growth Fund and Building Ontario Fund announce innovative equity investment in world-leading Ontario Power Generation SMR project*, 23 October. [online] Newswire.ca. Available at: https://www.newswire.ca/news-releases/canada-growth-fund-and-building-ontario-fund-announce-innovative-equity-investment-in-world-leading-ontario-power-generation-smr-project-862778443.html [Accessed 20 October 2026; not opened]. OPG version: https://www.opg.com/releases/cgf-and-bof-announce-innovative-equity-investment-in-world-leading-opg-smr-project/.
- **Findings (extract):** Up to CAD 2 bn from the CGF (up to 15%) and CAD 1 bn from the BOF (7.5%), with OPG the majority owner. Funds are released in two tranches: the first for SMR 1 and the second for SMRs 2–4 "once project milestones are met". The equity is held through DNNP LP.
- **Why it matters for C1:** The Units 2–4 tranche is milestone-conditional, so an embodied-carbon condition could ride on it.
- **Reliability:** Primary, once opened.
- **Supports:** §8.2, §8.6.

### CGF_InvestmentCriteria
Canada Growth Fund, 2025. *2025 Annual Report*. [pdf] Available at: https://medias.cgf-fcc.ca/images/cgf-2025-annual-report.pdf [Accessed 20 October 2026; not opened]. Also *Investment strategy*, https://www.cgf-fcc.ca/en/investment-strategy/.
- **Findings (extract):** The mandate includes to "reduce emissions while promoting economic growth". Performance metrics include financed emissions ("Scope 1, 2, and 3 where possible"), anticipated avoided emissions, permanent jobs and private capital catalysed. The fund also applies an additionality test.
- **Why it matters for C1:** Embodied emissions of construction materials fall within the financed-emissions metric the CGF already reports, so a low-carbon concrete condition fits its stated mandate [analyst inference, TO VERIFY that the metric covers project construction emissions].
- **Reliability:** Primary, once opened.
- **Supports:** §8.6.

### OPG_2025_Q1
Ontario Power Generation, 2025. *OPG reports 2025 first quarter financial results*, 13 May. [online] Toronto: OPG. Available at: https://www.opg.com/news-resources/newsroom/release/opg-reports-2025-first-quarter-financial-results/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** Ontario approved construction of the first of four SMRs on 8 May 2025. The four-unit cost is about CAD 20.9 bn including interest, escalation and contingency; the first unit is CAD 6.1 bn plus CAD 1.6 bn for shared systems.
- **Reliability:** Primary (company release), once opened. Run 1 may hold the same figures under another key; the coordinator should merge them.
- **Supports:** §3, §8.2.

### OPG_2026_Q1
Ontario Power Generation, 2026. *OPG reports 2026 first quarter financial results*. [online] Available at: https://www.opg.com/news-resources/newsroom/release/opg-reports-2026-first-quarter-financial-results/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** About CAD 585 m was received from the CGF and BOF in April 2026 as the first portion of the CAD 3 bn arrangement.
- **Reliability:** Primary, once opened.
- **Supports:** §8.2.

### OPG_OEB_EB-2025-0297_D2-4-1
Ontario Power Generation, 2025 (updated 21 May 2026). *EB-2025-0297, Exhibit D2, Tab 4, Schedule 1: Darlington New Nuclear Project overview*. [pdf] Filed with the Ontario Energy Board. Available at: https://files.opg.com/wp-content/uploads/2026/05/D2-04-01-Darlington-New-Nuclear-Project-Overview_Updated_20260521_260522_191835.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** Four BWRX-300 units, about 1,200 MW in total. Phase 1 is Unit 1 plus common facilities. Exhibit A1-4-3 gives the Unit 1 in-service date as October 2030 and 315 MW net per unit [TO VERIFY; conflicts with the deck's 300 MWe, so flag to Sam and Leroy].
- **Reliability:** Primary (regulatory filing), once opened. **The best place to find the Units 2–4 schedule and the approval steps.**
- **Supports:** §4.2, §8.1, §8.6. Interface item for Leroy and Sam (net MWe).

### ANS_2026_Darlington
American Nuclear Society, 2026. 'North American construction is back—smaller and faster—at OPG's Darlington', *Nuclear Newswire*, 5 June. [online] Available at: https://www.ans.org/news/2026-06-05/article-8047/north-american-construction-is-back-smaller-and-faster-at-opgs-darlington/ [Accessed 20 October 2026; not opened].
- **Findings (extract):** Lessons from Unit 1 will feed in as OPG works towards approval to progress Units 2–4, a milestone "expected in 2028".
- **Reliability:** Secondary-good (professional society). Replace with the OEB filing if it gives the same date.
- **Supports:** §8.6 (the decision window for C1).

### TBS_SECC (P1 for C1)
Treasury Board of Canada Secretariat, 2022 (amended 20 March 2025). *Standard on Embodied Carbon in Construction*. [online] Ottawa: TBS. Available at: https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32814 [Accessed 20 October 2026; not opened]. Also: TBS (2025) *Contracting Policy Notice 2025-6*, https://www.canada.ca/en/treasury-board-secretariat/services/policy-notice/2025-6.html; TBS, *Policy on Green Procurement*, https://www.tbs-sct.canada.ca/pol/doc-eng.aspx?id=32573.
- **Findings (extract):** In force 31 December 2022, with added requirements from 1 September 2025. Project ready-mixed concrete emissions must be "at least 10% less than" the regional industry-average EPD baseline, by strength class and volume; specialised mixes (high early strength, high performance, cold weather) are benchmarked at 130% of baseline. Scope (s 4.1): organisations covered by s 3 of the Policy on Green Procurement, which applies to "departments within the meaning of section 2 of the Financial Administration Act".
- **Why it matters for C1:** OPG is an Ontario Crown corporation and the CIB and CGF are federal Crown corporations, so **the standard probably does not apply to Darlington** [analyst inference from the scope clause, TO VERIFY]. It is a ready-made template that the CGF or Ontario could adopt as a contract condition, not an existing obligation. The plan's §2.1 point 4 ("Darlington has federal finance… that is the hook") needs rewording.
- **Note:** The 130% allowance for high-performance mixes matters: self-consolidating DP-SC infill could be classed as a specialised mix, which weakens the 10% requirement for exactly the concrete C1 targets.
- **Reliability:** Primary, once opened.
- **Supports:** §8.6, §4.3.

### TBS_GreeningProgress
Treasury Board of Canada Secretariat, 2025. *Progress on greening procurement: Other procurement*. [online] Available at: https://www.canada.ca/en/treasury-board-secretariat/services/innovation/greening-government/government-canada-progress-greening-procurement/other-procurement.html [Accessed 20 October 2026; not opened]. Also: TBS, *Greening Government Strategy: A Government of Canada Directive*, https://www.canada.ca/en/treasury-board-secretariat/services/innovation/greening-government/strategy.html.
- **Findings (extract):** Applies to federal construction projects of CAD 5 m or more using 100 m³ or more of ready-mixed concrete; Contracting Policy Notice 2022-3 said CAD 10 m. From 1 September 2025: projects using 200 t or more of structural or reinforcing steel must disclose its carbon and buy the lowest-emission option in each product category; new buildings over 2,000 m² need a whole-building LCA showing a 30% reduction, or the largest reduction possible within a 2% construction-cost premium. In 2024–25 one qualifying project cut ready-mix embodied carbon by 21% against its baseline. The Greening Government Strategy targets a 30% cut in embodied carbon of major construction from 2025.
- **Reliability:** Primary, once opened.
- **Supports:** §8.6 (benchmark: 10% concrete and 30% whole-asset targets against C1's saving; the 2% premium rule as a cost cap).

### ISED_2022_ConcreteRoadmap
Innovation, Science and Economic Development Canada and Cement Association of Canada, 2022. *Roadmap to Net-Zero Carbon Concrete by 2050*. [pdf] Ottawa: Government of Canada. Available at: https://ised-isde.canada.ca/site/clean-growth-hub/sites/default/files/documents/2022-11/roadmap-net-zero-carbon-concrete-2050_0.pdf [Accessed 20 October 2026; not opened].
- **Findings (extract):** Industry commitment of more than 15 Mt CO₂e cumulative reduction by 2030, then more than 4 Mt a year. SCMs can replace "on average, 30% or more" of cement with comparable quality and durability. The separate *Concrete Zero* plan (CAC, May 2023) projects reductions of 40% by 2030 and 59% by 2040 from a 2020 baseline.
- **Reliability:** Primary (government with industry), once opened.
- **Supports:** §8.6 (policy alignment; national context for LC3).

### CAC_2025_LowCarbonGuide
Cement Association of Canada, 2025. *A Guideline for Specifying Low Carbon Ready Mixed Concrete*, November. [pdf] Ottawa: CAC. Available at: https://cement.ca/wp-content/uploads/Concrete-Carbon-Guide_National_2025.pdf [Accessed 20 October 2026; not opened].
- **Use:** Model specification wording for an OPG procurement clause [TODO: open and extract].
- **Reliability:** Industry guidance (Secondary-good).
- **Supports:** §8.6.

### OPG_2020_ClimatePlan
Ontario Power Generation, 2020. *Climate Change Plan* [title TO VERIFY]. [pdf] Toronto: OPG. Available at: https://www.opg.com/wp-content/uploads/2020/11/OPG_ClimateChange2020_Final-FINAL-ua.pdf [Accessed 20 October 2026; not opened]. Also: OPG, 2023, *2023 strategic outlook for suppliers*, https://www.opg.com/news/2023-strategic-outlook-for-suppliers/.
- **Findings (extract):** OPG aims to be a net-zero carbon company by 2040, through reductions and offsets. Its 2023 supplier scorecard covers climate change and asks suppliers for goals and targets to reduce GHG emissions "created by their business and/or supply chain". No embodied-carbon or construction target was found.
- **Reliability:** Primary, once opened.
- **Supports:** §8.5, §8.6 (OPG's interest in C1).

### NortonRose_2025_EPBCReform
Norton Rose Fulbright, 2025. *Key amendments to the Environment Protection Reform Act 2025 and their implications for the EPBC Act*. [online] Available at: https://www.nortonrosefulbright.com/en-au/knowledge/publications/df336551/key-amendments-to-the-environment-protection-reform-act-2025-and-their-implications-for-the-epbc-act [Accessed 20 October 2026; not opened].
- **Findings (extract):** Passed the Senate on 27 November 2025 and the House on 28 November 2025, with Royal Assent on 1 December 2025; most changes commence during 2026 and all by 1 December 2026. "Nuclear action" is renamed "radiological exposure action", with new activity thresholds for naturally occurring radioactive material.
- **Reliability:** Secondary-good (law firm). **Use it to find the amending provisions, then check s 140A in the current compilation.**
- **Supports:** §8.1.

---

## From analyst run 3


# Sources: analyst run 3 (HHI for the BWRX-300 fuel supply chain), 20/10/2026

To be merged into `02_Research/sources.md` by the coordinator. Each entry: Harvard reference, key findings, the numbers it gives, reliability, verification status, and the section it supports. Parameter keys refer to `03_LCA_Calculations/parameters_run3.yaml`.

**Verification status for this whole file.** In this session no primary-source host could be opened: WebFetch and curl failed at the network level for world-nuclear.org, oecd-nea.org, iaea.org, justice.gov, ftc.gov, govinfo.gov, eia.gov and legislation.gov.au. The numbers below come from search-engine extracts that name these pages. Under CLAUDE.md ("never cite from memory or a search snippet") **none of them can be cited until a person opens the page and confirms them.** Each entry says what to check. Internal checks that passed are noted, because they make transcription errors unlikely, but they do not replace opening the source.

---

### WNA_mining
World Nuclear Association, [2026, TO VERIFY year of last update]. *World Uranium Mining Production*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/mining-of-uranium/world-uranium-mining-production [Accessed 20 October 2026; not opened, see status].
- **Findings:** Kazakhstan produces the largest share of mined uranium (39% in 2024), then Canada (24%) and Namibia (12%); about three-quarters of mine output comes from these three countries. A company table ranks Kazatomprom, Cameco and Orano first to third.
- **Numbers (tU):** 2024: Kazakhstan 23,270; Canada 14,309; Namibia 7,333; Australia 4,598; Uzbekistan 4,000 (est.); Russia 2,738; China 1,600 (est.); Niger 962; India 500 (est.); Ukraine 288 (est.); USA 260; South Africa 200 (est.); Others 155; world 60,213. 2023 world 54,433; 2022 world 49,614 (country rows for the eight largest producers also retrieved, see parameters). Companies 2024: Kazatomprom 12,463 tU (21%), Cameco 10,193 (17%), Orano 6,815 (11%).
- **Reliability:** High. WNA is an industry association, but this table compiles company and government production data and is the standard reference; the Red Book is the intergovernmental equivalent with a two-year lag. Several rows are WNA estimates (marked).
- **Internal check passed:** the thirteen 2024 rows sum exactly to 60,213 tU.
- **To verify:** every 2024 row; the page's update date; whether 2025 data have been added; the company table's year (the extract gives both 2024 and 2022).
- **Supports:** §8.3, Appendix B; `mining_by_country`, `mining_by_company_2024_pct`, `australia.production_2024_tU`.

### WNA_conversion
World Nuclear Association, [2024, TO VERIFY]. *Conversion and Deconversion*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/conversion-and-deconversion [Accessed 20 October 2026; not opened].
- **Findings:** Five commercial converters to UF₆. Cameco's Port Hope, Ontario plant is the only Canadian one. ConverDyn (Metropolis) is described as owned by Solstice Advanced Materials, spun off from Honeywell in October 2025 (so the page has been edited since late 2025, although the extract suggested the table is older).
- **Numbers (licensed capacity / production, tU):** Cameco (Canada, Port Hope) 12,500 / 11,375; CNNC (China, Lanzhou and Hengyang, est.) 15,000 / 13,489; ConverDyn (USA, Metropolis) 7,000 / 6,370; Orano (France, Pierrelatte and Malvési) 15,000 / 13,650; Rosatom (Russia, Seversk, est.) 12,500 / 11,375; total 62,000 / 56,259.
- **Reliability:** Medium–high. CNNC and Rosatom are WNA estimates. ConverDyn's 7,000 tU looks like an older licensed value; secondary sources give about 15,000 tU (see secondary_converdyn).
- **Internal check passed:** both columns sum to the stated totals.
- **To verify:** all five rows, table date, ConverDyn's current capacity.
- **Supports:** §8.3; `conversion_by_company`.

### WNA_enrichment
World Nuclear Association, [2025 or 2026, TO VERIFY]. *Uranium Enrichment*. [online] London: World Nuclear Association. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment [Accessed 20 October 2026; not opened]. Table cited there to World Nuclear Association (2025) *The Nuclear Fuel Report: Global Scenarios for Demand and Supply Availability 2025–2040* [title TO VERIFY].
- **Findings:** Four commercial enrichers plus small national plants. CNNC capacity is a WNA estimate assuming China builds enough for its domestic fleet.
- **Numbers (thousand SWU/yr, 2022 / 2025 / 2030):** Rosatom 27,100 / 29,133 / 29,810; Urenco 17,300 / 17,300 / 18,000; CNNC 10,613 / 13,789 / 18,230; Orano 7,500 / 7,500 / 10,000; Other (INB, JNFL) 128 / 355 / 1,744; total 62,641 / 68,076 / 77,784.
- **Derived:** Rosatom's share 43.3% (2022), **42.8% (2025)**, 38.3% (2030). This confirms, subject to verification, the "about 40–44%" in secondary sources.
- **Reliability:** Medium–high. This is the most-cited open dataset for enrichment. The 2030 figures are plans. Capacity is not output.
- **Internal check passed:** rows sum to the stated totals within 1 kSWU (rounding).
- **To verify:** all rows, especially CNNC and 2030; the Nuclear Fuel Report's title and year; any statement on the page giving Russia's share in words.
- **Supports:** §8.3, slide 13; `enrichment_by_company`.

### NEA_IAEA_2025
OECD Nuclear Energy Agency and International Atomic Energy Agency, 2025. *Uranium 2024: Resources, Production and Demand*. [pdf] Paris: OECD Publishing. Available at: https://www.oecd-nea.org/jcms/pl_103179/uranium-2024-resources-production-and-demand [Accessed 20 October 2026; not opened]. Pointers used: World Nuclear News (2025) "Invest now to secure long-term uranium future, Red Book says"; American Nuclear Society Nuclear Newswire, 10 April 2025.
- **Findings:** Australia has the largest identified recoverable resources (reasonably assured plus inferred): 28% of the world total at < USD 130/kgU and 24% at < USD 260/kgU, ahead of Kazakhstan (14%) and Canada (10%). World identified recoverable resources at < USD 260/kgU are 7,934,500 tU as of 1 January 2023.
- **Reliability:** High (intergovernmental, the standard reference). The shares above came through news reports of the Red Book, so the cost category and table number must be confirmed in the report.
- **To verify:** Australia's tonnage and share by cost category (table number), and the report's NEA publication number.
- **Supports:** §8.3, slide 13; `australia.share_identified_recoverable_resources_*_rb2024`. It corrects the Meeting 2 claim of "30% of the world's uranium reserves" (plan §11): the Red Book term is *identified recoverable resources*, not reserves, and the figure is 28% (< USD 130/kgU).

### NEA_IAEA_2026
OECD Nuclear Energy Agency and International Atomic Energy Agency, 2026. *Uranium 2026: Resources, Production and Demand*. [pdf] Paris: OECD Publishing. Available at: https://www.oecd-nea.org/jcms/pl_121658/uranium-2026-resources-production-and-demand [Accessed 20 October 2026; not opened]. Figures came through WNA's *Supply of Uranium* page (https://world-nuclear.org/information-library/nuclear-fuel-cycle/uranium-resources/supply-of-uranium) and the ANS Nuclear Newswire, 15 September 2026.
- **Findings:** The 31st edition covers 2023–2024. Identified recoverable resources at < USD 260/kgU are 8.105 million tU (+2.1% on the 2024 edition). As of 1 January 2025 there were 418 reactors (378 GWe) needing about 64,500 tU a year. Exploration and mine-development spending was USD 1.8 billion in 2023–2024.
- **Australia (WNA's tabulation, < USD 130/kgU, 1 Jan 2025):** 1,701,600 tU (29%); Kazakhstan 827,500 (14%); Canada 551,700 (9%). **Conflict:** another WNA page citing the same edition gives Australia 2,119,800 tU (27%), Kazakhstan 16% and Canada 8%. The two cannot both be right for one cost category. Probably one is < USD 130 and the other < USD 260, but this is unconfirmed.
- **Reliability:** High once opened. **This is now the latest edition.** The team should decide whether to cite 2024 (28%, as on slide 13) or 2026 (29% or 27%, depending on the category).
- **Supports:** §8.3; `australia.share_identified_recoverable_resources_usd130_rb2026`, `world_reactor_requirements_2025_tU`.

### GA_2026
Geoscience Australia, 2026. *Australia's Energy Commodity Resources 2026: Uranium and Thorium*. [online] Canberra: Geoscience Australia. Available at: https://www.ga.gov.au/aecr2026/uranium-and-thorium [Accessed 20 October 2026; not opened].
- **Findings (extract only):** says Australia has the world's largest uranium resources; gives Australia's total identified resources (the extract cut off the number and unit).
- **Reliability:** High (Australian Government primary source). It's the best Australian cross-check on the Red Book share.
- **To verify:** open it and record Australia's identified resources (kt U), its share of the world, and its production.
- **Supports:** §8.3 (gap).

### USDOJ_FTC_2023
U.S. Department of Justice and Federal Trade Commission, 2023. *Merger Guidelines*. [pdf] Washington, DC: DOJ and FTC, 18 December 2023. Available at: https://www.justice.gov/d9/2023-12/2023%20Merger%20Guidelines.pdf [Accessed 20 October 2026; not opened].
- **Findings:** markets with HHI greater than 1,800 are "highly concentrated". A merger is presumed to substantially lessen competition if it produces a highly concentrated market and raises the HHI by more than 100, or if it creates a firm with more than 30% share and raises the HHI by more than 100.
- **Reliability:** High (official). Law-firm summaries disagree on "greater than" vs "1,800 or greater". Quote the exact wording and section (Guideline 1, and section 2.1 on market concentration) from the PDF.
- **Supports:** §2 (methods), §8.3; `thresholds.doj_ftc_2023_highly_concentrated`.

### USDOJ_FTC_2010
U.S. Department of Justice and Federal Trade Commission, 2010. *Horizontal Merger Guidelines*. [online] Washington, DC: DOJ and FTC, 19 August 2010. Available at: https://www.justice.gov/atr/horizontal-merger-guidelines-08192010 [Accessed 20 October 2026; not opened].
- **Findings (section 5.3):** unconcentrated HHI < 1,500; moderately concentrated 1,500–2,500; highly concentrated > 2,500. In highly concentrated markets, mergers raising the HHI by more than 200 are presumed likely to enhance market power. Superseded by the 2023 Guidelines.
- **Reliability:** High (official, superseded). It's the scale the slide currently uses ("above 2,500").
- **Supports:** §2, §8.3; `thresholds.doj_ftc_2010_*`.

### US_PL118_62
United States Congress, 2024. *Prohibiting Russian Uranium Imports Act*, Public Law 118-62, 13 May 2024. [pdf] Washington, DC: U.S. Government Publishing Office. Available at: https://www.govinfo.gov/content/pkg/PLAW-118publ62/pdf/PLAW-118publ62.pdf [Accessed 20 October 2026; not opened]. (Statutes at Large citation TO VERIFY.)
- **Findings:** amends section 3112A of the USEC Privatization Act. From 90 days after enactment, it bans imports of unirradiated low-enriched uranium produced in Russia or by a Russian entity, including material obtained through swaps. The Secretary of Energy may waive the ban if there is no alternative viable source or if imports are in the national interest. Waivers end on 1 January 2028, and the ban ends on 31 December 2040.
- **Reliability:** High (statute), once opened. Whether annual waiver caps survived into the enacted text is unconfirmed.
- **Supports:** §8.3 (sanctions scenario); `us_russian_uranium_ban`.

### WNN_2024
World Nuclear News, 2024. Russia places 'tit-for-tat' ban on US uranium exports. *World Nuclear News*, [18 November 2024, TO VERIFY]. Available at: https://world-nuclear-news.org/articles/russia-places-ban-on-us-uranium-exports [Accessed 20 October 2026; not opened].
- **Findings:** on 15 November 2024 the Russian Government amended Decree No 313 of 9 March 2022 to temporarily restrict exports of enriched uranium to the US, except under one-off licences. Centrus reported that Tenex's general export licence had been rescinded.
- **Reliability:** Medium. Trade news, used only as a pointer to the Russian decree and Centrus's SEC Form 8-K (November 2024), which are the primary sources to cite.
- **Supports:** §8.3 (the risk runs both ways: supply can be withdrawn by the supplier as well as banned by the buyer).

### OPG_2023_fuel
Ontario Power Generation, 2023. [OPG selects first fuel suppliers for its small modular reactor; title and date TO VERIFY]. [press release] Toronto: OPG. Primary URL on opg.com still to be found. Pointer: Power Engineering, "OPG selects first fuel suppliers for its small modular reactors" (https://www.power-eng.com/nuclear/smrs/opg-selects-first-fuel-suppliers-for-its-small-modular-reactors/).
- **Findings:** announced at the World Nuclear Exhibition, Paris (late 2023). The first Darlington BWRX-300's fuel chain is Cameco (Saskatchewan mines and natural UF₆ from Port Hope), Urenco USA enrichment (Eunice, New Mexico), additional enriched uranium product from Orano (France), and fabrication by Global Nuclear Fuel–Americas (US). Ontario's minister described the fuel as "Saskatchewan uranium, enriched by our allies in the U.S. and France" (quote from the trade article; confirm in the OPG release).
- **Reliability:** Medium until the OPG release is found. The quote and the supplier split must be confirmed in it.
- **Supports:** §8.3 (the Darlington supply chain contains no Russian stage), §8.6 (dual-source enrichment contracts as a model).

### KAP_2025
Kazatomprom, 2025. *Integrated Annual Report 2024*. [pdf] Astana: NAC Kazatomprom JSC. Available at: https://www.kazatomprom.kz/storage/59/kap_iar_2024_eng_0205__clean.pdf [Accessed 20 October 2026; not opened].
- **Findings:** Kazatomprom says it was again the world's largest uranium producer on an attributable basis in 2024, at about 21% of global primary production according to UxC.
- **Reliability:** High for the company's own output; the 21% share is UxC's. It cross-checks WNA's 21%.
- **Supports:** Appendix B, company-level bound.

### APH_2024 (merged entry; replaces the Parliamentary Library half of StateBans_Summary)
Gibson, E., 2024. *Current prohibitions on nuclear activities in Australia: a quick guide*. Research Paper Series 2023–24, Quick Guide. [online] Canberra: Parliamentary Library, Parliament of Australia, 30 May. Available at: https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Quick_Guides/2023-24/NuclearActivitiesProhibitions (PDF copy: https://aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/pubs/rp/rp2324/Quick_Guides/NuclearActivitiesProhibitions) [Accessed 21 October 2026; not opened]. **[TO VERIFY]** title, author (Dr Emily Gibson) and date are from a search summary (run 7b); the run 3 title "Nuclear activities prohibitions: a quick guide" was the URL slug, not the page title. Check the series line on the title page.
- **Scope (search summary, run 7b):** maps Commonwealth, state and territory bans on nuclear activities for the domestic nuclear-energy debate; excludes the AUKUS submarine amendments and international safeguards obligations; defines a nuclear activity as any step in the fuel cycle.
- **Findings (extract):** EPBC Act s140A(1) bars the minister from approving a nuclear fuel fabrication plant, a nuclear power plant, an enrichment plant or a reprocessing facility. ARPANS Act s10 bars the CEO from licensing the same four. **Conversion plants are not on either list.** Some state laws (NSW; a 2007 Queensland bill) do cover conversion.
- **Reliability:** High (Parliamentary Library), but run 2 owns the law and must confirm the wording in the Acts themselves (Federal Register of Legislation, current compilations).
- **Supports:** §8.1, §8.3 (domestic conversion is the one front-end step that federal law doesn't prohibit by name; TO VERIFY with run 2).

### secondary_converdyn
Wikipedia, [n.d.]. *ConverDyn*; Strategist and Architect, [2025]. "There is no alternative" (Substack). [online] [Accessed 20 October 2026; extracts only].
- **Findings:** the Metropolis plant's capacity is given as about 15,000 tU/yr, or 15,000–17,600 tU/yr after a recent expansion.
- **Reliability:** Low. Used only as a sensitivity bound, never cited in the report. Replace with Solstice/ConverDyn or NRC licence data if found.
- **Supports:** Appendix B sensitivity; `conversion_by_company.converdyn_capacity_alt`.

---

## From analyst run 4 (deck sources)


# Sources: analyst run 4 (references for the slide deck), 20/10/2026

The coordinator should merge this into `02_Research/sources.md`. It covers the deck citations that `01_Report/factcheck.md` section C flags as "source not found" (S5, S7, S12, S21, S22, S34, S35, S36, S37, S41) and the entries on `references.html`. Each entry gives a Harvard reference, the deck figure it supports, the findings, the numbers, reliability, and verification status.

**Verification status for this whole file: no entry is verified.** No source page could be opened in this session.
- WebFetch failed at DNS (`ENOTFOUND`) for pnas.org, ourworldindata.org, poll.lowyinstitute.org and opg.com.
- curl through the session proxy got `CONNECT tunnel failed, response 403` for all of these: ourworldindata.org, archive.ourworldindata.org, pnas.org, pmc.ncbi.nlm.nih.gov, doi.org, api.crossref.org, web.archive.org, albertainnovates.ca, jaif.or.jp, sec.gov, canada.ca, nrc.gov, files.opg.com, unece.org, poll.lowyinstitute.org, energy.gov, gle-us.com and world-nuclear.org.
- The GitHub API is limited to this session's repositories, so OWID's data repository couldn't be read either.

All the content below comes from **search-engine summaries only**. Under CLAUDE.md ("never cite from memory or a search snippet") every entry is **[TO VERIFY]** until a team member opens the URL and checks the figure marked "Check". The URLs are the ones the search results returned. DOIs are given only where the search result showed them.

---

## S5: BWRX-300 concrete claim (slide 3, smr.html)

### GEH_AI_2021
McDonald, D., 2021. *BWRX-300 Small Modular Reactor* [presentation slides]. Alberta Innovates SMR Learning Series 3, Speaker 9. GE Hitachi Nuclear Energy. Available at: https://albertainnovates.ca/app/uploads/2021/03/AI-SMR-Learning-Series-3-Speaker-9-Doug-McDonald-GE.pdf [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Supports (deck):** ">50% less concrete per MW vs ESBWR".
- **Findings (search summary):** a GE Hitachi slide deck from Alberta Innovates' SMR Learning Series. The visible excerpt covers GEH's history and the BWRX-300's boiling-water design. **The excerpt didn't show the concrete comparison.**
- **Check:** find the slide that gives the concrete and building-volume reduction per MW against the ESBWR, and note its page number. If it isn't in this deck, cite GEH_JAIF_2018 instead.
- **Reliability:** vendor marketing claim, not independently verified. Present it as "GE Hitachi claims".

### GEH_JAIF_2018 (fallback for the same claim)
Sledzik, D., 2018. *[Title TO VERIFY: BWRX-300 presentation]* [presentation slides]. 51st JAIF Annual Conference, Tokyo. GE Hitachi Nuclear Energy. Available at: https://www.jaif.or.jp/cms_admin/wp-content/uploads/2018/04/51st-annual_David_Sledzik_en.pdf [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Findings (search summary):** "more than 50% less concrete per MW" than the ESBWR, and "more than 50% building volume reduction per MW". NucNet (2020; news, used only as a pointer) reports that the BWRX-300 "would use 50% less concrete and steel on a per MW basis" than the ESBWR.
- **Context:** the BWRX-300 (300 MWe) is derived from GEH's 1,520 MWe ESBWR (search summary).
- **Reliability:** vendor claim, as above.

---

## S7, S12: Darlington licence, approval and in-service date (slide 4, darlington.html)

### CNSC_2025_LTC
Canadian Nuclear Safety Commission, 2025. *Commission authorizes Ontario Power Generation Inc. to construct 1 BWRX-300 reactor at the Darlington New Nuclear Project site* [news release, April 2025]. Ottawa: CNSC. Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/commission-authorizes-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Companion: CNSC, 2025. *Decision by the Commission to authorize Ontario Power Generation Inc. to construct 1 BWRX-300 reactor at the Darlington New Nuclear Project site*. Available at: https://www.canada.ca/en/nuclear-safety-commission/news/2025/04/decision-by-the-commission-to-authorize-ontario-power-generation-inc-to-construct-1-bwrx-300-reactor-at-the-darlington-new-nuclear-project-site.html. The Record of Decision is DEC 24-H3 (search summary: dated 4 April 2025; document ID DAMZHJW66V33-166150894-455; at first available on request from the Commission Registry).
- **Supports (deck):** "Apr 2025: Canadian Nuclear Safety Commission grants the licence"; replaces NucNet (2025) and WNN (2022) on slide 4 and on the references slide (S12).
- **Findings (search summary):**
  - The licence covers **one** BWRX-300 in Clarington, Ontario.
  - The power reactor construction licence is **valid until 31 March 2035** and has 4 facility-specific conditions.
  - The hearing ran in two parts: virtual on 2 October 2024, then in person in Ajax in January 2025.
  - The Commission found it had met its duty to consult Indigenous peoples.
  - The licence **does not cover** fuel loading, commissioning with fuel, or operation; a separate Commission approval is needed for those.
- **Check:** the decision date (4 April 2025), the expiry date, and the wording on the duty to consult (useful for R3.3 First Nations consent).
- **Reliability:** primary regulator. High once opened.

### ON_2025_FID
Government of Ontario, 2025. *Ontario Leads the G7 by Building First Small Modular Reactor* [news release, 8 May 2025]. Toronto: Office of the Premier / Ministry of Energy and Mines [issuing office TO VERIFY]. Available at: [URL TO VERIFY, news.ontario.ca; title as reprinted at https://todaysnorthumberland.ca/2025/05/08/ontario-leads-the-g7-by-building-first-small-modular-reactor/] [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Supports (deck):** "May 2025" approval; C$20.9 bn for four units (1,200 MW); about C$17 m/MW; S7 "first ... in the G7".
- **Findings (search summary):**
  - Approved 8 May 2025: OPG may build the first of four BWRX-300s at Darlington.
  - The **C$20.9 bn** Darlington New Nuclear Project budget covers site preparation, engineering, design and construction of all four SMRs.
  - Unit 1 is **C$6.1 bn plus C$1.6 bn** for shared systems and infrastructure, **C$7.7 bn** in total (Radio-Canada).
  - Commercial operation is targeted for **2030**.
  - Claimed benefits: up to **18,000** Canadian jobs, **C$500 m a year** to Ontario's economy, and **80%** of project spending going to Ontario companies.
- **Wording for S7:** the release title (as reprinted) is "first Small Modular Reactor" in the G7. It says nothing about "grid-scale" or "licensed". The deck's "first grid-scale SMR licensed in the G7" goes beyond this. Either quote Ontario ("the first SMR in the G7") or attribute the extra words.
- **Check:** whether C$6.1 bn includes the C$1.6 bn; the exact G7 wording; the issuing ministry and URL.
- **Reliability:** government primary. High for budget and approval; jobs and GDP figures are government claims.

### OPG_DNNP / OPG_OEB_2025
Ontario Power Generation, n.d. *Darlington New Nuclear Project / Darlington SMR* [online]. Available at: https://www.opg.com/projects-services/projects/nuclear/smr/darlington-smr/ [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Ontario Power Generation, 2025. *EB-2025-0297, Exhibit A1-04-03: Overview of Nuclear Facilities* [Ontario Energy Board filing]. Toronto: OPG. Available at: https://files.opg.com/docs/eb-2025-0297-a1-04-03-overview-of-nuclear-facilities-pdf/ [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Ontario Power Generation, 2025. *2025 Q1 Financial Statements / OPG reports 2025 first quarter financial results*. Available at: https://oeb.ca/sites/default/files/2025%20Q1%20Financial%20Statements.pdf [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Supports (deck):** "Unit 1 is expected in service in 2030 (sources differ between end-2029 and October 2030)".
- **Findings (search summary):**
  - The OEB filing EB-2025-0297 (December 2025) gives a planned in-service date of **October 2030** for Unit 1.
  - OPG's Q1 2025 results say grid connection will be **by the end of 2030**.
  - An IESO 2024 connection document (https://www.IESO.ca/-/media/Files/IESO/Document-Library/regional-planning/East-Ontario/Connection-Approach-for-Small-Modular-Nuclear-Reactors.pdf) gave commercial operation in **2029**, with the grid connection energised in 2027. That schedule has been superseded.
  - A 2023 OPG release aimed to finish construction in 2028.
  - **No primary source for "end-2029" was found.**
- **Check:** Unit 1 in-service date in the OEB exhibit; Units 2–4 dates in the same filing. (A search summary said "all four planned SMRs scheduled to be in-service in 2030"; that reading looks wrong and needs checking.)
- **Reliability:** an OEB rate filing is primary and the most recent. Leroy owns the dates; see the note to Leroy below.

### CGF_BOF_2025 and CIB_2022 (S35)
These are already in `sources.md` (factcheck S35). Slide 11's "as Ontario and Canada are doing for Darlington" should cite them, not WNN 2025. No new entry needed.

---

## S21: Silex / Global Laser Enrichment tails re-enrichment (slide 8, materials-rd.html)

### NRC_GLE_PLEF
U.S. Nuclear Regulatory Commission, n.d. *Global Laser Enrichment, LLC (Paducah Laser Enrichment Facility)* [facility page]. Rockville, MD: NRC. Available at: https://www.nrc.gov/facilities-safety/facility-finder/fc/global-laser-enrichment-nc-lc [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Related Federal Register notices (not opened): https://public-inspection.federalregister.gov/2026-05955.pdf (draft EIS) and https://public-inspection.federalregister.gov/2026-04474.pdf (licensing board / hearing).
- **Supports (deck):** "SILEX ... is being commercialised in the US to re-enrich leftover depleted-uranium tails".
- **Findings (search summary):**
  - GLE submitted its environmental report on 13 June 2025 and its safety analysis report on 27 June 2025.
  - The application was **accepted for docketing on 4 August 2025**.
  - Review schedule: EIS by September 2026, safety evaluation report by January 2027, then a mandatory hearing (Commission order CLI-26-3, 4 March 2026).
  - A draft EIS has been issued for a 322-acre site about 5 miles west of Paducah, McCracken County, Kentucky.
  - The licence sought covers re-enrichment of depleted UF₆ tails and enrichment of natural UF₆ **up to 8 wt% U-235** by laser.
  - **No licence has been issued** as far as the search results show.
  - The NRC page states the ownership: **51% Silex Systems (Australia), 49% Cameco (Canada)**.
- **Check:** the licence status today (October 2026); whether the final EIS has been issued; the ownership wording; the enrichment limit.
- **Reliability:** primary regulator. High.

### GLE_DOE_2016
Global Laser Enrichment, n.d. *Business* [online]. Wilmington, NC: GLE. Available at: https://www.gle-us.com/business/ [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Pointer for the amendment (news; trace to a primary): World Nuclear News, 2020. *DOE amends UF6 sale agreement, outlines disposal plans*. Available at: https://world-nuclear-news.org/Articles/DOE-amends-agreement-for-UF6-sale,-outlines-dispos.
- **Findings (search summary):**
  - DOE's Office of Environmental Management and GLE signed a **long-term agreement in November 2016** for a large part of DOE's depleted-tails inventory: "over 200,000 MtU" (GLE's wording, as summarised), to be re-enriched at a proposed plant beside the closed Paducah Gaseous Diffusion Plant.
  - The agreement was **amended in 2020**. WNN calls the amendment a key condition of the GLE restructuring (Silex 51%, Cameco 49%).
  - A search summary dates completion of the restructuring to **2021**, giving February. **The month is unconfirmed.**
- **Check:** the agreement date and tails quantity; a Silex ASX announcement giving the completion date of the 51/49 restructure (silex.com.au, ASX: SLX).
- **Reliability:** company page, medium. Replace with DOE or Silex ASX primaries if they can be opened.
- **Wording (factcheck B15):** no lead supports the claim that it is commercialised in the US **because** of s 140A. Use: "...is being commercialised in the US; EPBC Act s 140A would bar such a plant in Australia." (The s 140A wording is in run 2.)

---

## S22: SMR waste volume (slide 8)

### Krall_2022
Krall, L.M., Macfarlane, A.M. and Ewing, R.C., 2022. Nuclear waste from small modular reactors. *Proceedings of the National Academy of Sciences of the United States of America*, 119(23), e2111833119. https://doi.org/10.1073/pnas.2111833119. Open access copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC9191363/ [Accessed 20 October 2026; neither opened]. **[TO VERIFY]**
- **Supports (deck):** "2 to 30 times more waste by volume per unit of energy" for three SMR designs (not the BWRX-300).
- **Findings (search summary of the abstract):**
  - Water-, molten-salt- and sodium-cooled SMR designs "will increase the volume of nuclear waste in need of management and disposal by factors of 2 to 30".
  - The three designs are NuScale (water), Terrestrial Energy IMSR (molten salt) and Toshiba 4S (sodium) [design names TO VERIFY in the paper]. The reference is an 1,100 MWe PWR.
  - The authors attribute the increase to neutron reflectors and chemically reactive fuels and coolants.
  - They add that repository performance depends on decay heat and the radiochemistry of spent fuel, where SMRs offer no benefit.
  - Press coverage (Stanford, via TechXplore) gives other per-energy multipliers: up to 35 times for short-lived low- and intermediate-level waste, and up to 30 times for long-lived waste. **Don't mix these with "2 to 30".**
- **Rebuttal:** NuScale said the paper used outdated design data (S&P Global, 2022; news pointer).
- **Check:** the abstract wording; whether "2 to 30" is normalised per unit of energy (the deck says "per unit of energy"); the three design names.
- **Reliability:** peer-reviewed, high, but disputed by the vendor. Present it as contested and specific to the three designs.

---

## S36: Australian polling (slide 12, social.html)

### Lowy_2024
Neelam, R., 2024. *Lowy Institute Poll 2024*. Sydney: Lowy Institute. Available at: https://poll.lowyinstitute.org/report/2024/ and chart https://poll.lowyinstitute.org/charts/australia-using-nuclear-power-to-generate-energy/ [Accessed 20 October 2026; not opened]. Also https://www.lowyinstitute.org/publications/2024-lowy-institute-poll/nuclear-power. **[TO VERIFY]** (Author attribution to Ryan Neelam is from a search summary; check the report's title page.)
- **Supports (deck):** "61% support, 37% oppose" nuclear power for electricity (2024).
- **Findings (search summary):** 61% "somewhat" or "strongly" support "Australia using nuclear power to generate electricity". 37% oppose.
- **Numbers:** strongly support 27%, somewhat support 34%, somewhat oppose 20%, strongly oppose 17%, don't know 2%.
- **Method:** national survey of **2,028** adults, **4–17 March 2024**, run by the Social Research Centre on the Life in Australia probability panel, margin of error **±2.2%**.
- **Earlier comparison:** in 2011, 35% supported and 62% opposed. The question wording differed (building nuclear power plants to cut emissions), so the years aren't directly comparable.
- **2025 / 2026:** **no electricity result was found.** The 2025 poll (fielded 3–16 March 2025, n = 2,117) and the 2026 poll asked about nuclear submarines (67% in 2025, 68% in 2026) and nuclear weapons (39% in favour in 2026), not electricity.
- **Check:** the chart page for any year after 2024; the exact question wording.
- **Reliability:** probability-panel survey, high.

---

## S37: Deaths per TWh (slide 12)

### OWID_deaths
Ritchie, H., 2020 [first published 2017; updated July 2022 per search summary; year TO VERIFY]. *What are the safest and cleanest sources of energy?* [online]. Our World in Data. Available at: https://ourworldindata.org/safest-sources-of-energy; chart: *Death rates from energy production per TWh*, https://ourworldindata.org/grapher/death-rates-from-energy-production-per-twh (archived copy: https://archive.ourworldindata.org/20260518-093348/grapher/death-rates-from-energy-production-per-twh.html) [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Supports (deck):** "0.03 deaths per TWh from nuclear, against 24.6 for coal".
- **Numbers (from a table in several secondary sources, attributed to OWID; unconfirmed):**

| Source | Deaths per TWh |
|---|---|
| Brown coal | 32.72 |
| Coal | **24.62** |
| Oil | 18.43 |
| Biomass | 4.63 |
| Gas | 2.82 |
| Hydropower | 1.3 |
| Wind | 0.04 |
| Nuclear | **0.03** |
| Solar | 0.02 |

  The deck's 24.6 matches 24.62 rounded. A Robeco Substack (March 2024) gives the same 0.03 / 24.6 / 18.4 / 2.8.
- **Caveats stated by OWID (search summary):** the fossil-fuel rates are based on European power plants with good pollution controls, so they are "likely to be very conservative", and global rates are probably higher. The nuclear figure includes Chernobyl and Fukushima. At these very low rates the uncertainties of nuclear, wind and solar overlap, so their ranking is fragile.
- **Check:** coal (24.62) and nuclear (0.03) on the live chart; whether the deck's "OWID 2024" should be the article's last-update year.
- **Reliability:** an aggregator; cite the underlying papers too (below).

### Markandya_Wilkinson_2007
Markandya, A. and Wilkinson, P., 2007. Electricity generation and health. *The Lancet*, 370(9591), pp. 979–990. https://doi.org/10.1016/S0140-6736(07)61253-7 [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Findings (search summary):** a fuel-cycle comparison using European ExternE methods. Health burdens are greatest for lignite, coal and oil, appreciably smaller for gas, and lower still for nuclear. OWID's fossil rates come from **Table 2**, including acute and chronic effects; chronic effects are 88–99% of deaths. Nuclear cancer deaths are estimated with the linear no-threshold model.
- **Check:** the Table 2 coal value per TWh and how OWID derived 24.62 from it.
- **Reliability:** peer-reviewed (Lancet), high; European plant basis.

### Sovacool_2016
Sovacool, B.K., Andersen, R., Sorensen, S., Sorensen, K., Tienda, V., Vainorius, A., Schirach, O.M. and Bjørn-Thygesen, F., 2016. Balancing safety with sustainability: assessing the risk of accidents for modern low-carbon energy systems. *Journal of Cleaner Production*, 112, pp. 3952–3965. [DOI TO VERIFY] [Not opened]. **[TO VERIFY]** (author initials TO VERIFY)
- **Findings (search summary):** an accident database for 1950–2014 covering eight low-carbon systems: 686 accidents, 182,794 deaths, US$265.1 bn damage. Hydro accounts for 97.2% of deaths and nuclear for 90.8% of damage.
- **Correction:** Child et al. (2020, *Renewable and Sustainable Energy Reviews*) report the nuclear-only figures as 172 incidents, US$241 bn and 4,803 deaths, and say the main conclusions are unaffected. OWID uses this paper for its solar and wind rates.
- **Reliability:** peer-reviewed, high; note the corrigendum.

---

## S34: NuScale / UAMPS Carbon Free Power Project (slide 11, cost.html)

### UAMPS_NuScale_2023
NuScale Power Corporation and Utah Associated Municipal Power Systems, 2023. *UAMPS and NuScale Power agree to terminate the Carbon Free Power Project* [joint press release, 8 November 2023], filed as Exhibit to NuScale Power Corp. Form 8-K. Washington, DC: U.S. Securities and Exchange Commission. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296623000256/uampsnuscalejointpressre.htm [Accessed 20 October 2026; not opened]. **[TO VERIFY]** (exact title and 8-K item TO VERIFY; the BusinessWire copy is https://www.businesswire.com/news/home/20231108847712/en/)
- **Supports (deck):** cancellation in November 2023; 462 MW.
- **Findings (search summary):** both parties agreed to terminate because the project "appears unlikely" to reach enough subscription to continue to deployment. The plan was **6 × 77 MWe = 462 MWe** at Idaho National Laboratory, cut back from 12 modules (720 MWe at 60 MWe each), with operation targeted for 2029.
- **Reliability:** company primary (SEC filing). High.

### NuScale_DCRA_2023 (the $89 price)
NuScale Power Corporation, 2023. *Amendment No. 3 to Development Cost Reimbursement Agreement* [exhibit to Form 10-Q / 424B3]. SEC. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296623000092/a101dcraamendment3execut.htm; and NuScale, 2023. *[Press release, January 2023, EX-99.1]*. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296623000008/pressreleasenuscalereach.htm [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Supports (deck):** "$58 → $89/MWh".
- **Findings (search summary):**
  - The amendment sets a **price target of US$89.00/MWh, in dollars of 1 July 2022**, for a 6-module, 462 MWe plant with dry cooling.
  - The earlier **US$58/MWh** target was in **2020 dollars** (POWER magazine).
  - The NuScale/Fluor Class 3 estimate put the total project cost at **US$9.24 bn** (other reports round to US$9.3 bn, up from US$5.3 bn).
  - Inflation Reduction Act benefits were estimated at about **US$2.8 bn**, which could lower the net project cost to **US$5.1 bn**.
- **IRA question:** yes, **US$89 already includes IRA support**. IEEFA (https://ieefa.org/resources/eye-popping-new-cost-estimates-released-nuscale-small-modular-reactor; analysis, not primary) says it is net of about **US$30/MWh** of IRA credits and the DOE's US$1.4 bn cost share, and that "the price would be much higher" without them.
- **Deck implications:**
  1. "+53%" compares 2020 dollars with July 2022 dollars, so some of the increase is general inflation. Say so, or label each figure with its dollar year.
  2. Say that $89 is **after** IRA credits, which strengthens the cost-risk argument.
  3. The factcheck notes E&E News gives $55, not $58. Use the DCRA/NuScale figure once it is opened.
- **Check:** the price-target clause and its dollar year in the DCRA amendment; whether the January 2023 NuScale release mentions the IRA.
- **Reliability:** SEC exhibits are primary, high. IEEFA is an advocacy analysis, medium.

### DOE_CFPP_2020 and the US$232 m
U.S. Department of Energy, Office of Nuclear Energy, 2020. *DOE Approves Award for Carbon Free Power Project* [16 October 2020]. Washington, DC: DOE. Available at: https://www.energy.gov/ne/articles/doe-approves-award-carbon-free-power-project [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
Pointer for the US$232 m (news; DOE spokesperson quoted): Northey, H. [author TO VERIFY], 2023. *NuScale cancels first-of-a-kind nuclear project as costs surge*. E&E News, 9 November 2023. Available at: https://www.eenews.net/articles/nuscale-cancels-first-of-a-kind-nuclear-project-as-costs-surge/.
- **Supports (deck):** "after US$232M of government funding / $232 million of Department of Energy funding".
- **Findings (search summary):**
  - The DOE cost-share award was **US$1.355 bn over 10 years** (UAMPS; DOE rounds to "up to $1.4 billion"), subject to appropriations. It was paid to Carbon Free Power Project LLC, wholly owned by UAMPS.
  - E&E News, quoting DOE, reports that DOE had **obligated US$232.8 m** of this. A DOE clarification adds that termination would cut DOE's net investment to **about US$50 m**, mainly by transferring project assets to DOE.
  - DOE's separate **US$579.7 m** support to NuScale for design development was unaffected.
- **Deck implication:** "US$232M" was the amount obligated, not lost. Say "about US$233 m obligated" (or "US$232.8 m") and note the reported net exposure of about US$50 m.
- **Check:** find a DOE primary for the US$232.8 m and the US$50 m (a DOE statement, budget justification or OIG report). Until then, cite E&E as reporting DOE's statement.
- **Reliability:** DOE award page is primary. The US$232.8 m is news quoting DOE, medium.

### PowerEng_2023 (the deck's current citation; secondary)
Power Engineering, 2023. *Facing mounting costs, NuScale cancels small modular reactor project in Utah* [online]. Available at: https://www.power-eng.com/nuclear/smrs/facing-mounting-costs-nuscale-cancels-small-modular-reactor-project-in-utah/ [not opened]. **[TO VERIFY]**
- Repeats $58 → $89, 6 × 77 MW = 462 MW, and E&E's $232 m. **Replace it with the primaries above** (R1.4: no reliance on news). The project was in Idaho (at INL), not Utah; UAMPS is the Utah buyer.

---

## UNECE life-cycle report (slides 2, 6, 9)

### UNECE_2021
United Nations Economic Commission for Europe, 2021. *Carbon Neutrality in the UNECE Region: Integrated Life-cycle Assessment of Electricity Sources*. ECE/ENERGY/141. Geneva: United Nations. ISBN 978-92-1-117298-0 [TO VERIFY]. Available at: https://unece.org/sites/default/files/2021-10/LCA-2.pdf; catalogue: https://digitallibrary.un.org/record/4020227; https://www.un-ilibrary.org/content/books/9789210014854 [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Title:** the deck's "Life Cycle Assessment of Electricity Generation Options" is the title used for the 2021 online PDF. The catalogued publication is the title above (©2021; UN Digital Library lists release in October 2022). **Use one title consistently.** Recommended: the catalogued title, year 2021.
- **Supports (deck):** nuclear "about 5 to 6 g per kWh"; "the fuel chain's front end ... reported to be nuclear's largest emitter".
- **Findings (search summary):**
  - Nuclear is **5.1–6.4 g CO₂e/kWh**, the lowest of the technologies assessed.
  - Coal runs from **751** (IGCC, USA) to **1,095 g/kWh**.
  - Twelve world regions and seven technologies are covered.
  - **Front end:** secondary summaries quote the report: "the fuel chain ('front-end') contributes most to the overall emissions". Nuclear varies little between regions because its model is only lightly regionalised.
  - **No percentage share** for the front end, or split between mining, conversion and enrichment, was found.
- **Check:** the front-end sentence and its page; any stage breakdown figure; the nuclear reactor type and region.
- **Reliability:** UN intergovernmental report, high.

---

## S41: WNA page titles (slide 13 and references slide)

### WNA_enrichment
World Nuclear Association, [2025, year TO VERIFY]. *Uranium Enrichment* [online]. London: WNA. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
### WNA_conversion
World Nuclear Association, [2025, year TO VERIFY]. *Conversion and Deconversion* [online]. London: WNA. Available at: https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/conversion-and-deconversion [Accessed 20 October 2026; not opened]. **[TO VERIFY]**
- **Fix for S41:** list these as **two separate references** with the titles above. "Conversion and Enrichment" is not a WNA page title.
- **Numbers:** see `sources_run3.md` (WNA_enrichment, WNA_conversion). Rosatom has about 42.8% of 2025 enrichment capacity on WNA's table; other summaries say "about 40%" or "over 44%".

---

## LC3 (slides 7, 8, 14)

### Scrivener_2018
Scrivener, K., Martirena, F., Bishnoi, S. and Maity, S., 2018. Calcined clay limestone cements (LC3). *Cement and Concrete Research*, 114, pp. 49–56. [DOI TO VERIFY; ScienceDirect or EPFL Infoscience: https://infoscience.epfl.ch/entities/publication/bd2ac65d-217a-46ed-992b-2bebd280d11b] [Not opened]. **[TO VERIFY]**
- **Supports (deck):** the definition only ("calcined clay and limestone replace part of the clinker"). The deck quotes no number from it.
- **Findings:** the bibliographic details (authors, title, volume, pages) match a 2025 reference list in *Engineering* (engineering.org.cn). No abstract content was seen.
- **Check:** the abstract's clinker-replacement level and CO₂ reduction claim, if the report quotes either. A related review is Sharma, M., Bishnoi, S., Martirena, F. and Scrivener, K., 2021, *Cement and Concrete Research* 149, 106564, https://doi.org/10.1016/j.cemconres.2021.106564 (not opened).
- **Reliability:** peer-reviewed, high (the authors lead the LC3 project).

---

## Values that differ from the deck

| Deck item | Deck value | What the leads show | Action |
|---|---|---|---|
| OWID coal | 24.6 deaths/TWh | 24.62 (secondary tables attributed to OWID) | Consistent; confirm on the live chart. Add the European-plants caveat. |
| NuScale price | $58 → $89/MWh (+53%) | $58 is in 2020 US$; $89 is in July 2022 US$ and already **net of IRA** (~$30/MWh) and the DOE cost share | Label the dollar years; say "after subsidies". |
| DOE funding | US$232M | US$232.8 m **obligated** of US$1.355 bn; reported net exposure after termination about US$50 m | Reword to "obligated"; find a DOE primary. |
| Project location | "Utah" (PowerEng title) | Site at INL, Idaho; UAMPS is Utah-based | Say "UAMPS (Utah) project in Idaho". |
| Unit 1 in service | 2030 (end-2029 vs Oct 2030) | OEB filing: Oct 2030; Q1 2025: grid by end-2030; 2029 only in a superseded 2024 IESO schedule | Keep 2030; drop "end-2029". |
| Lowy | 61% / 37% (2024) | Matches (27+34 / 20+17, 2% DK); no 2025 or 2026 electricity question found | Keep as 2024; say it is the latest. |
| "First G7 SMR" | "first grid-scale SMR licensed in the G7" | Ontario: "first SMR in the G7" | Quote Ontario's wording. |
| Krall | "2–30× by volume per unit of energy" | "factors of 2 to 30" in volume of waste needing management and disposal, for three designs | Confirm the per-energy normalisation; keep "three designs". |
| WNA title | "Conversion and Enrichment" | Two pages: "Uranium Enrichment"; "Conversion and Deconversion" | Split the reference. |
| UNECE title | "Life Cycle Assessment of Electricity Generation Options" | Catalogued as "Carbon Neutrality in the UNECE Region: Integrated Life-cycle Assessment of Electricity Sources" (ECE/ENERGY/141) | Pick one title across deck and report. |

## Interfaces
- **To Leroy (dates):** the latest lead for Darlington Unit 1 is October 2030 (OPG OEB filing EB-2025-0297, Dec 2025), against the "end-2029" in some sources. Please confirm in your timeline section; the deck uses 2030.

## Status by rubric ID
- **R1.4 (primary sources):** found primary URLs for 15 references (CNSC, Ontario, OPG/OEB, NRC, SEC, DOE, UNECE, PNAS, Lancet, JCP, Lowy). **Missing:** none opened; every entry needs a human check before it can be cited at HD.
- **R3.1 (economic):** NuScale/CFPP cost-risk case refined (dollar years, IRA-inclusive price, DOE obligation vs net exposure). **Missing:** DOE primary for US$232.8 m and US$50 m.
- **R3.2 (political):** GLE licensing status and ownership leads for the s 140A argument. **Missing:** Silex ASX primary and current NRC status.
- **R3.3 (social):** Lowy 2024 full breakdown and method; deaths per TWh with the underlying papers and caveats; CNSC duty-to-consult finding. **Missing:** confirmation that no newer Lowy electricity figure exists; the live OWID value.
- **R3.4 (regulation):** CNSC licence scope, validity and phase limits. **Missing:** the Record of Decision text.
- **R4.2:** LC3 citation confirmed bibliographically only. **Missing:** any quantitative LC3 claim from the paper.
- **R5.4 (Harvard):** full references drafted, with title fixes (WNA, UNECE). **Missing:** DOIs and years marked TO VERIFY.

---

## From analyst run 7a (job Q2, 21/10/2026)

Rubric coverage: R2.3, R2.7, R3.1, R4.3, R1.4

### eccc2026_industrial_trajectory
- **Reference (Harvard, TO VERIFY):** Environment and Climate Change Canada (2026) *Industrial carbon pricing in Canada*. Ottawa: Government of Canada. Available at: https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/putting-price-on-carbon-pollution/industry.html (Accessed: 21 October 2026) [NOT OPENED: proxy 403 / DNS failure on www.canada.ca, 21/10].
- **Pointer only:** International Carbon Action Partnership (2026) *Canada publishes new carbon price trajectory*. Available at: https://icapcarbonaction.com/en/news/canada-publishes-new-carbon-price-trajectory [NOT OPENED: proxy 403]. Carbon Pulse (21 May 2026) 'Canada softens industrial carbon price trajectory, caps benchmark at C$100 through 2029' (news, paywalled; pointer only).
- **Key findings (from two search summaries, 21/10; not citable until opened):** a new headline price trajectory for all industrial carbon pricing systems, published 19 May 2026 and effective 15 May 2026: C$95/t in 2026, C$100 in 2027–2029, C$115 in 2030, +C$3/yr to C$130 in 2035, then +1.5%/yr to C$140 in 2040. A full updated federal benchmark is to be published later in 2026. It replaces the 2021 path (C$65 in 2023, +C$15/yr to C$170 in 2030). The consumer fuel charge has been zero since 1 April 2025.
- **Numbers used:** `carbon_price_2026_cad` 95 (high 110 = old path); `carbon_price_2030_cad` 115 (high 170 = old path), in `parameters_run1.yaml`.
- **Reliability:** if confirmed on canada.ca, primary government source, high. Today it is a search lead only. **Conflict:** run 5 (`parameters_run5.yaml` `carbon_prices_cad` [95, 110, 170], labelled 2025/2026/2030) uses the superseded path; see plan.md §5 Interfaces.
- **Ontario applicability (gap):** Ontario's Emissions Performance Standards (O. Reg. 241/19) replaced the federal OBPS on 1 January 2022; the 2026 EPS excess-emissions charge was not found. Construction-material emissions are not facility emissions under the EPS (analyst inference, run 5, TO VERIFY), so C1's carbon value is a shadow value unless a funder or contract prices it.

### lca_results_2110
- **Reference:** our own model: lca-analyst (2026) *Life-cycle assessment of one BWRX-300 at Darlington, and the C1 LC3 initiative*. `03_LCA_Calculations/results/lca.md`, `lca_scenarios.csv`, `lca_montecarlo_summary.csv` (21 October 2026). Not an external source: cite as "this study, Appendix A/C".
- **Numbers used in Q2:** life cycle 4.18 g CO₂e/kWh median (P5–P95 3.05–5.85), C1 saving 1,734 t per unit (1,387–2,153), 5,201 t for Units 2–4 (4,161–6,458).
- **Reliability:** reproducible calculation; every input still TO VERIFY (lca-analyst).

---

## From analyst run 7b (21/10/2026; plan.md §7 job Q3)

Rubric coverage: R1.4, R1.3, R5.4, R4.3, R3.2, R2.3, R2.5, RB.6

**Access status.** curl through the proxy got `CONNECT tunnel failed, response 403` for every primary host tried (silex.com.au, nrc.gov, urenco.com, asx.com.au, arxiv.org, onlinelibrary.wiley.com, doi.org, crossref, link.springer.com, laccei.org, crsi.org, iso.org, nwmo.ca, legislation.gov.au, austlii, algoma.com, arcelormittal.com, federalregister.gov, gle-us.com). WebFetch failed at DNS for silex.com.au and arxiv.org. **Everything below comes from web-search summaries and is [TO VERIFY]** until a person opens the URL. Nothing here may ship without its marker resolved at Q19.

**Already in this file (no new entry needed; Q3 list item checked):** Krall_2022, Lowy_2024, OWID_deaths, Markandya_Wilkinson_2007, Sovacool_2016, UAMPS_NuScale_2023, NuScale_DCRA_2023, DOE_CFPP_2020, GEH_AI_2021 and GEH_JAIF_2018 (all in the run 4 block above). The factcheck rows that call them "not found" (S5, S22, S34, S36, S37) predate the run 4 merge.

### A. Standards and law

#### ISO_14040_2006
International Organization for Standardization, 2006. *ISO 14040:2006 Environmental management — Life cycle assessment — Principles and framework* (amended by ISO 14040:2006/Amd 1:2020). Geneva: ISO. [URL TODO: iso.org catalogue page] [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** principles and framework for LCA; one amendment (Amd 1:2020); the consolidated EN ISO 14040:2006+A1:2020 is listed by the Estonian standards body (EVS, https://www.evs.ee/en/evs-en-iso-14040-2006-a1-2020-consolidated) as valid from 2 November 2020. EVS notes it is not intended for contractual, regulatory or certification use.
- **Reliability:** the standard itself (paywalled). High for definitions; cite for structure only.
- **Supports:** §2, §6.1 (factcheck L1, L71: "structured on ISO 14040/44; screening study, not critically reviewed").

#### ISO_14044_2006
International Organization for Standardization, 2006. *ISO 14044:2006 Environmental management — Life cycle assessment — Requirements and guidelines* (amended by ISO 14044:2006/Amd 1:2017 and Amd 2:2020). Geneva: ISO. Available at: https://www.iso.org/standard/38498.html [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** two amendments (2017, 2020); ISO's page says the base edition was last reviewed and confirmed in 2022. The EN version is listed as A1:2018 + A2:2020 by one national body, so cite the ISO dates, not the EN ones.
- **Check:** the critical-review clause for comparative assertions disclosed to the public (needed for the L71 wording).
- **Supports:** §2, §6.1.

#### EN_15804_2019
European Committee for Standardization, 2019. *EN 15804:2012+A2:2019 Sustainability of construction works — Environmental product declarations — Core rules for the product category of construction products* (with corrigendum AC:2021). Brussels: CEN. Catalogue: https://iteh.eu/catalog/standards/cen/c98127b4-8dc2-48a4-9338-3e1366b16669/en-15804-2012a2-2019; BSI: https://knowledge.bsigroup.com/products/sustainability-of-construction-works-environmental-product-declarations-core-rules-for-the-product-category-of-construction-products-2 [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** core product-category rules for Type III declarations of any construction product; A2 approved by CEN on 21 July 2019. Modules A1–A3 = product stage; A4–A5 = construction stage (secondary guides; confirm in the standard).
- **Supports:** §6.1, Appendix A5 (factcheck L62: "cradle-to-gate (EN 15804 modules A1–A3)").

#### AU_Constitution_s109_s23
*Commonwealth of Australia Constitution Act 1900* (Imp) [regnal-year citation TO VERIFY on the Federal Register title page], covering clause 9 (the Constitution), ss 23 and 109. [online] Federal Register of Legislation [URL TODO]; AustLII copy of s 109: https://www.austlii.edu.au/au/legis/cth/consol_act/coaca430/s109.html [Not opened]. **[TO VERIFY]**
- **s 109 (wording in the AustLII extract):** "When a law of a State is inconsistent with a law of the Commonwealth, the latter shall prevail, and the former shall, to the extent of the inconsistency, be invalid."
- **s 23:** Senate voting. **Its wording did not appear in any extract this session**; open the text before §8.1 or Appendix B1.2 quotes it or relies on how a tied vote is resolved.
- **Harvard note:** Harvard (style guide) cites the Constitution by name and section, without an author: *Commonwealth of Australia Constitution Act 1900* (Imp) s 109.
- **Supports:** §8.1 (federal override of NSW s 8; factcheck A9, A26), App B1.2 (Senate arithmetic).

### B. Waste governance (Canada)

#### NWMO_2024_SiteSelection
Nuclear Waste Management Organization, 2024. *The Nuclear Waste Management Organization selects site for Canada's deep geological repository for used nuclear fuel* [news release], 28 November. Toronto: NWMO. Available at: https://www.nwmo.ca/News/The-Nuclear-Waste-Management-Organization-selects-site-for-Canadas-deep-geological-repository [Not opened]. **[TO VERIFY]**
- **Findings (search summary; several outlets agree, e.g. Bruce Power's reprint of 28 Nov 2024):** NWMO chose the Wabigoon Lake Ojibway Nation (WLON) and Township of Ignace area, Northwestern Ontario, after a 14-year process that began with 22 interested communities. Ignace residents and WLON members voted in favour. Repository more than 500 m deep; construction could start in the 2030s, with operation about 2040–2045. Still needs CNSC licences and a federal impact assessment. Reported cost about C$26 bn (2020 dollars) over 175 years; C$170 m over 81 years to the Ignace area (secondary).
- **What it supports:** Canada's plan is direct disposal of used fuel in a deep geological repository under NWMO's Adaptive Phased Management (APM) (factcheck L13). **Check:** the APM name and "used fuel, not reprocessed" wording on nwmo.ca (APM page), or cite NWMO (2005) *Choosing a Way Forward* if it can be opened [URL TODO].
- **Also useful for R3.3:** a working precedent of host-community and First Nation consent (willingness votes) for a nuclear facility.
- **Reliability:** primary (the implementing agency), once opened.
- **Supports:** §6.2 hotspot 3, T9, §8.4 (social licence precedent), §8.6.

### C. Silex / Global Laser Enrichment (factcheck B15, S21, L77; plan B15 go/cut)

#### NRC_GLE_PLEF (update to the run 4 entry above)
- **New lead (search summary, 21/10):** the NRC page sets the review schedule by Commission Order **CLI-26-3 (4 March 2026)**: EIS by September 2026, safety evaluation report by January 2027, then the mandatory hearing. GLE's CEO said at the World Nuclear Symposium 2026 (September, London) that GLE expects the licence in **early 2027** (reported in trade press; company statement, not the NRC's). No licence has been issued as far as the leads show.

#### Silex_ASX_2025_NRCacceptance
Silex Systems Limited, 2025. *[Title TO VERIFY: NRC accepts GLE's Paducah licence application for review]*. ASX announcement, 6 August. Sydney: ASX. Available at: https://announcements.asx.com.au/asxpdf/20250806/pdf/06mkwks19y2zck.pdf [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** the NRC completed its acceptance review of the Paducah Laser Enrichment Facility (PLEF) application in August 2025, so formal review could begin. GLE is 51% Silex, 49% Cameco.
- **Reliability:** primary (continuous-disclosure filing). High once opened.

#### Silex_ASX_2026_Offtake
Silex Systems Limited, 2026. *[Title TO VERIFY: Cameco exclusive offtake agreement for the Paducah Laser Enrichment Facility]*. ASX announcement, 16 September. Sydney: ASX. [URL TODO: ASX announcements platform, code SLX]. Pointer: World Nuclear News, *Cameco in offtake agreement for US laser enrichment plant*, https://www.world-nuclear-news.org/articles/cameco-in-offtake-agreement-for-us-laser-enrichment-plant [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** Cameco will buy **all** future PLEF output under an exclusive offtake: natural-grade UF₆ from re-enriched tails, LEU, LEU+ (5–10% U-235) and HALEU, priced at Cameco's average realised long-term price net of selling costs. Silex calls it a commercial pillar for a future final investment decision (so **no FID yet**).
- **Why it matters (R4.3):** Cameco is also OPG's uranium and conversion supplier for Darlington Unit 1 (OPG_2023_fuel). That gives a sourced chain: an Australian-invented enrichment technology → licensing in the US → output sold through Darlington's own fuel supplier, while EPBC s 140A and ARPANS s 10 bar an enrichment plant in Australia. **No lead says s 140A caused the offshore location**; do not write "because".
- **Reliability:** primary once opened; WNN is the pointer only.

#### Silex_ASX_2026_Incentives
Silex Systems Limited, 2026. *[Title TO VERIFY: Kentucky incentives package for GLE]*. ASX announcement, 27 March. [URL TODO: ASX platform; seen only as a third-party mirror, https://bulletin.webull.com/qbd/announcement/20260327/499501885/84e68402a13428a03783e2065957cc96.pdf, not to be cited]. **[TO VERIFY]**
- **Findings (search summary):** preliminary approval of a US$98.9 m (about A$144 m) state and county incentives package, conditional on investment and job thresholds.
- **Use:** optional (one clause in §8.2 on sub-national industrial policy). Low priority.

#### Not found (gap)
- **PLEF capacity in SWU/yr.** No Paducah-specific figure was found. The 6 million SWU figure belongs to GLE's 2012 NRC licence for the Wilmington plant (not built) and must not be used for Paducah. Tails feed: "over 200,000 t" of DOE tails (GLE, run 4) vs about 300,000 t DUF₆ in another summary; unreconciled.

### D. Ontario steel: blast furnace to EAF (factcheck L18)

#### Algoma_2026_BFclosure
Algoma Steel Group Inc., 2026. *[Q1 2026 results release / MD&A; title TO VERIFY]*. Sault Ste. Marie: Algoma Steel. [URL TODO: algomasteel.com investor page or SEC/SEDAR+ filing]. Pointer: CTV News Northern Ontario, *Tariffs, transition to electric furnace lead to Algoma Steel's $159M Q1 loss*, https://www.ctvnews.ca/northern-ontario/article/tariffs-transition-to-electric-furnace-lead-to-algoma-steels-159m-q1-loss/ [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** CEO Rajat Marwah is reported as saying Algoma **permanently closed its blast furnace on 18 January 2026**, ending coal-based steelmaking at Sault Ste. Marie. Algoma had announced on 1 December 2025 that it would close the blast furnace and coke plant and move fully to EAF steelmaking in early 2026, a year early, with about 1,000 layoffs (BNN Bloomberg, 1 Dec 2025, pointer).
- **Reliability:** news until the company filing is opened.

#### ArcelorMittal_Dofasco_2021
ArcelorMittal, 2021. *[Title TO VERIFY: ArcelorMittal and Government of Canada announce investment in decarbonisation technologies at ArcelorMittal Dofasco]* [press release], July. [URL TODO: corporate.arcelormittal.com]. Pointers: S&P Global (30 July 2021); Recycling Today; Steel Times International [Not opened]. **[TO VERIFY]**
- **Findings (search summary, 2021–22 sources):** Hamilton to move from blast furnace/BOF to a 2 Mst/yr DRI plant and a 2.4 Mst/yr EAF shop, targeted for about 2028; about C$1.765–1.8 bn, with C$400 m from the Government of Canada (amounts differ by outlet). **Current status not found.**
- **What L18 can and cannot say:** the leads support "Ontario's integrated steelmakers are moving from blast furnaces to EAFs (Algoma closed its blast furnace in January 2026; Dofasco plans to)". They do **not** show how much ground granulated blast-furnace slag Ontario concrete draws from these plants, or how much is imported. So §6.3 finding 3 should state the slag-supply point as a **risk**, not as an established shrinkage (the section's own TODO 7 option).
- **Supports:** §4.3, §6.3 finding 3, §10.

### E. Fuel supply (sizing §8.3; HHI source disagreement)

#### ANS_2026_Urenco
American Nuclear Society, 2026. 'Urenco to add 2.1 million SWU of enrichment capacity at its New Mexico plant', *Nuclear Newswire*, 2 June. Available at: https://www.ans.org/news/2026-06-02/article-8085/urenco-to-add-21-million-swu-of-enrichment-capacity-at-its-new-mexico-plant/ [Not opened]. **[TO VERIFY]** Primary to find: Urenco's own release of 2 June 2026 (urenco.com).
- **Numbers (search summary):** existing Urenco USA capacity **4.3 million SWU** (about a third of US demand); a separate **700,000 SWU** project due in **2027**; the new **2.1 million SWU** expansion starts construction in 2029, first cascades 2032, full installation 2036; installed capacity to exceed **7 million SWU** within a decade. Part of a Urenco-wide plan for +4.6 million SWU (US, Netherlands, Germany).
- **Reliability:** professional-society news reporting a company announcement. Company projections.
- **Parameters:** `parameters_run3.yaml` → `urenco_usa`.

#### WNU_2025_Platov
World Nuclear University, 2025. *[Title TO VERIFY: Enrichment]* [presentation slides by Platov, initials TO VERIFY]. WNU Summer Institute, 17 June. Available at: https://world-nuclear-university.org/SummerInsituteFiles/2025-06-17_WNU_Enrichment_Platov_final_62a48c29.pdf [Not opened]. **[TO VERIFY]**
- **Numbers (search summary):** Russia's four enrichment sites, thousand SWU/yr: 28,600 (2010), 26,600 (2015), 27,700 (2020), **27,100 (2025)**. Over 95% of SWU is produced by four companies.
- **Use:** second estimate of Rosatom's 2025 capacity in `hhi.py` (Russia 41.0% instead of 42.8%; HHI 2,935 vs 3,009).
- **Reliability:** training slides from an industry body; medium.

#### CRAI_2025 (source not identified)
[CRA International, 2025, as recorded in `briefs/supply-concentration.md` by run 3; title, URL and author unknown.]
- **Numbers (as recorded by run 3, not re-found):** Rosatom 26,200 and CNNC 11,000 thousand SWU/yr for 2025.
- **Status:** two searches in run 7b found no CRA International document with these figures. **Not citable.** If it is not found and opened by Q19, cut the CRAI row and report the range as WNU–WNA (41.0–42.8%).

### F. Author and reference completions (LCA; entries live in `sources_lca.md`, owned by the lca-analyst)

#### Sun_Kurosaki_2025 (completes `arxiv2025_smr_overview`; factcheck L10)
Sun, Y. and Kurosaki, K., 2025. *Technical overview of recent developments in small modular reactors in the United States*. arXiv:2504.02599 [physics.soc-ph], submitted 3 April. Available at: https://arxiv.org/abs/2504.02599 [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** two authors, both Kyoto University; 42 pages, 15 figures; SMRs defined as typically under 300 MWe. **Not peer-reviewed** (preprint), so the 870 MWt and 3.8%/4.95% enrichment values should be replaced by NEDO-33977 or another GEH document where possible.

#### Ng_2025_JIE (completes `ng2025_jie`; factcheck L32)
Ng, J.H.C., Vyawahare, P., Benavides, P.T., Gan, Y., Sun, P., Boardman, R., Marcinkoski, J. and Elgowainy, A., 2025. Life-cycle greenhouse gas emissions associated with nuclear power generation in the United States. *Journal of Industrial Ecology*, 29(3), pp. 719–732. https://doi.org/10.1111/jiec.70008 [Not opened]. **[TO VERIFY]**
- **Findings (search summary, RePEc record):** motivated by the IRA hydrogen tax credit (0.45 kg CO₂e/kg H₂ threshold). Projects a 33% (2035) and 46% (2050) fall in the carbon intensity of nuclear electricity relative to the current fuel cycle. The "3.0 g CO₂e/kWh fuel cycle" value and its scope (front end only vs whole fuel cycle) are **still unconfirmed**.

#### LACCEI_2026_2661 (factcheck L20; authors still missing)
[Authors TO VERIFY], 2026. Comparative life cycle assessment and structural performance analysis of eco-friendly LC3 cement for CO₂ reduction compared to Portland cement. In: *Proceedings of the 24th LACCEI International Multi-Conference for Engineering, Education and Technology*, Santiago, Chile, 15–17 July 2026. Contribution 2661. Available at: https://laccei.org/LACCEI2026-Chile/full-papers/Contribution_2661_final_a.pdf; metadata page https://laccei.org/LACCEI2026-Chile/meta/SP2661.html [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** compares OPC Type I with ternary LC3 for Latin America (environmental, mechanical, economic); concludes LC3 gives more structural performance per unit of emission. The summary says the authors are Peruvian researchers but gives no names. The **903.5 vs 513.5 kg CO₂e/t** values were not seen. **Open the metadata page for the author list.** Conference paper, not journal; medium reliability.

#### CancioDiaz_2017 (peer-reviewed replacement for ENR 2018 in `lc3_reduction_leads`)
Cancio Díaz, Y. et al., 2017. Limestone calcined clay cement as a low-carbon solution to meet expanding cement demand in emerging economies. *Development Engineering*, 2, pp. 82–91. https://doi.org/10.1016/j.deveng.2017.06.001 [Not opened]. **[TO VERIFY]** Only the first author was seen in the search summaries; copy the full author list from the article before the reference list is built (Q16).
- **Findings (search summary):** economic, environmental and social feasibility of five investment options for the Cuban cement industry over 15 years; LC3 cuts production cost by 15–25% against conventional options. **Its CO₂ reduction figure was not seen** (secondary sources give "up to 30%" or "up to 40%").
- **Recommendation for the lca-analyst:** ENR (trade press) should leave the five-estimate median. Without it the four remaining estimates are 33.6%, 36.6%, about 40% and 43.2%, median **38.3%** (vs 37% now). Cite Cancio Díaz et al. (2017) only for the qualitative feasibility case until its CO₂ number is read. A related peer-reviewed lead: Sánchez Berriel, S. et al., 2016, 'Assessing the environmental and economic potential of Limestone Calcined Clay Cement in Cuba', *Journal of Cleaner Production*, pp. 361–369 [volume TO VERIFY].

#### CRSI_2022_EPD (replaces `crsi2017_epd` 0.97 t CO₂e/t; factcheck L22, L65)
Concrete Reinforcing Steel Institute, 2022. *Environmental Product Declaration: Fabricated Steel Reinforcement* [industry-wide EPD; title TO VERIFY], issued September 2022, valid to September 2027. Schaumburg, IL: CRSI. Available at: https://www.crsi.org/sustainability/environmental-product-declaration/ (press release: https://www.crsi.org/wp-content/uploads/Press-Release-CRSI-Releases-Updated-EPD.pdf) [Not opened]. **[TO VERIFY]**
- **Findings (search summary):** cradle to fabricator gate; ISO 14025 and ISO 21930; covers ASTM A615 and A706 bar. **The EPD's own GWP per tonne was not seen.**
- **Interim lead (secondary, a state procurement document):** Minnesota Department of Administration, 2026, *Buy Clean Buy Fair GWP limits* (15 January 2026), https://mn.gov/admin/assets/2026-MNBuyCleanGWPLimits_2026-01-15_tcm36-721175.pdf, lists rebar at **0.755** (mill gate) and **0.854** (converted for fabricated product; scrap 3.0% A1 multiplier, A2 transport 0.049, A3 fabrication 0.027) in "ton CO₂e/ton steel". Whether this table derives from the CRSI 2022 EPD, and whether the tons are metric, is unconfirmed. These are **procurement limits, not industry averages**. Use only as a sensitivity bound until the EPD is opened.

### G. Red Book edition: proposal for team decision B9
- **Proposal:** cite **Red Book 2024 (NEA and IAEA, 2025): 28% at < USD 130/kgU**, because only that figure is tied to a named cost category. Add one clause: "the 2026 edition, as tabulated by the World Nuclear Association, gives 27–29% depending on the table (NEA and IAEA, 2026)". Every reading rounds to "about 28%", so the claim ("the largest share of any country") does not depend on the choice.
- **Switch rule:** if Victor opens *Uranium 2026* and confirms the < USD 130/kgU table, cite 2026 alone (latest edition) and update `parameters_run3.yaml` (`australia.share_identified_recoverable_resources_usd130_rb2026`), slide 13 and §8.3 together.
