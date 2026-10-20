Rubric coverage: R1.4, R1.3, R2.3, R2.7, R3.1, R3.6, R4.3, RB.6

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
- **Findings:** **None confirmed.** The values commonly quoted for nuclear (min 3.7, median 12, max 110 g CO₂e/kWh) did not appear even in a search result on 20/10. A 2026 arXiv preprint (not peer-reviewed; https://arxiv.org/pdf/2608.29717) says it checked coal at 820 and gas at 490 against the IPCC PDF.
- **Use:** stress test only until Table A.III.2 is opened.

### nrel2021_lca
**Reference:** National Renewable Energy Laboratory, 2021. *Life Cycle Greenhouse Gas Emissions from Electricity Generation: Update*. [pdf] Golden, CO: NREL. NREL/FS-6A50-80580 [TO VERIFY report number]. Available at: https://www.nrel.gov/docs/fy21osti/80580.pdf.
- **Findings (secondary):** Reviews about 3,000 LCAs and replaces the 2013 fact sheet; builds on the 2012 LCA Harmonization Project. CleanTechnica (2012) reports harmonised nuclear medians of **12–13 g CO₂e/kWh** (PWR and BWR). The 2021 nuclear median was not seen.
- **Check:** Figure 2 of the fact sheet (min, quartiles, median, max by technology) and the GWP basis.
