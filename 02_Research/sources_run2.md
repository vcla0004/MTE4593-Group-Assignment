Rubric coverage: R1.4, R3.2, R3.4, R3.5, R3.7, R3.8, R5.4

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
Holding Redlich, n.d. *Nuclear law: Could Australia go nuclear?* [online] Available at: https://www.holdingredlich.com/nuclear-law-could-australia-go-nuclear [Accessed 20 October 2026; not opened]. Also: Parliamentary Library, 2024. *Current prohibitions on nuclear activities in Australia: a quick guide*, 30 May. [online] Available at: https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Quick_Guides/2023-24/NuclearActivitiesProhibitions.
- **Findings (extract):** South Australia has no ban on nuclear power plants, but its *Nuclear Waste Storage Facility (Prohibition) Act 2000* bans waste storage facilities and public funding for them. WA's *Nuclear Waste Storage and Transportation (Prohibition) Act 1999* bans storing and transporting certain nuclear waste; a 2007 WA bill to ban power plants did not pass. Tasmania and the ACT have no state-level power or waste bans.
- **Reliability:** The Parliamentary Library guide is Primary-adjacent (parliamentary research) and should be the one cited; the law firm is Secondary-good.
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
