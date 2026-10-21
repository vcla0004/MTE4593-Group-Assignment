Rubric coverage: R1.4, R3.1, R2.3, RB.6, R3.6, R3.7, R5.4

# Sources: analyst run 5 (economics and finance, §7 and §8.2), 21/10/2026

The coordinator merges this into `02_Research/sources.md`. Keys match `03_LCA_Calculations/parameters_run5.yaml`. Keys already defined elsewhere are reused, not repeated: `OPG_2025_Q1`, `OPG_2026_Q1`, `CIB_2022_Loan`, `CGF_BOF_2025`, `OPG_OEB_EB-2025-0297_D2-4-1`, `TBS_GreeningProgress` (sources.md); `NuScale_DCRA_2023`, `UAMPS_NuScale_2023`, `DOE_CFPP_2020`, `CNSC_2025_LTC` (sources_run4.md); `csiro2024_gencost2324`, `csiro2025_gencost2425`, `csiro2026_gencost2526`, `rba_f11` (sources_run1.md).

**Access status. No entry below was opened.** On 21/10 the proxy refused (CONNECT 403) or DNS failed for csiro.au, sec.gov, canada.ca, cib-bic.ca, opg.com, lc3.ch, arxiv.org, osti.gov, ncbi.nlm.nih.gov, and every mirror or secondary host tried (newsreel.com.au, claytonutz.com, minister.dcceew.gov.au, howtostoreelectricity.com). A GenCost 2024-25 copy at windenergy.org.nz was found but not tried. GitHub access to the Steigerwald dataset repository was refused. Every finding is from a **web-search summary**, so every entry is **[TO VERIFY]** under CLAUDE.md. Each entry says what to check.

---

## GenCost: updates to the run-1 entries

### csiro2024_gencost2324 (update; entry in sources_run1.md)
- **New finding (NucNet, 23 May 2024, pointer: https://www.nucnet.org/news/report-warns-on-levelised-cost-of-electricity-from-smrs-5-4-2024; also Yahoo "One Big Chart"):** SMR LCOE **A$387–641/MWh in 2023**, falling to **A$230–382/MWh by 2030**. Large-scale nuclear A$155–252 (2023), **A$141–233 (2030)**. Solar and wind with integration costs **A$89–125 (2030)** (Capital Brief gives 82–120; Yahoo 73–128).
- **Conflict:** run 1 entered 387–641 (average 514) as the 2030 value (`smr_lcoe_aud` in `parameters_run1.yaml`). If NucNet is right, that is the 2023 value. **Check:** the 2030 SMR row in the LCOE figure/table of the final report (https://www.csiro.au/-/media/Energy/GenCost/GenCost2023-24Final_20240522.pdf).

### dcceew_bowen_release_gencost2425
Bowen, C. and Husic, E., [2025, date TO VERIFY]. *Joint media release: Experts agree: Nuclear only getting more expensive, slower for Australia's energy needs*. Canberra: Minister for Climate Change and Energy. Available at: https://minister.dcceew.gov.au/bowen/media-releases/joint-media-release-experts-agree-nuclear-only-getting-more-expensive-slower-australias-energy-needs [Accessed 21 October 2026; not opened].
- **Findings (search summary):** SMR power in 2030 "would be up to $487MWh", excluding a possible "first of a kind" premium; large-scale nuclear "no earlier than 2040", A$145–238/MWh from then; firmed renewables A$80–122/MWh in 2030 at 80% variable generation.
- **Reliability:** ministerial release, political. Use only to find the GenCost table it quotes (probably 2024-25 final, 29 July 2025). Never cite it for the number.

### cec2025_gencost2526_draft
Clean Energy Council, 2025. *CSIRO GenCost report reaffirms firmed renewables as most practical option for Australia* [media release, December 2025]. Available at: https://cleanenergycouncil.org.au/news-resources/csiro-gencost-report-reaffirms-firmed-renewables-as-most-practical-option-for-australia [not opened].
- **Findings (search summary):** quoting the 2025-26 consultation draft: large-scale nuclear **A$200–328/MWh**, solar PV A$52–88, onshore wind A$78–129 (indicative levelised generation costs; year TO VERIFY).
- **Reliability:** industry advocate. Pointer to the draft (https://www.csiro.au/-/media/Energy/GenCost-2025-26-Draft/GenCost2025-26ConsultDraft_20251216-FINAL.pdf).

### csiro2026_gencost2526 (update; entry in sources_run1.md)
- **New findings (CSIRO news release, July 2026, search summary):** SMRs remain "the highest cost"; large-scale nuclear is "slightly higher in cost than gas with CCS"; SMR capital costs "continue to be based on the Darlington project"; the Australian interpretation of Darlington's capital cost "has been revised downwards" to reflect interest during construction. Futures markets suggest A$80–90/MWh system generation cost by 2030 (system average, not an LCOE). Authors listed as Graham, P., Hayward, J. and Foster, J. (2026) in one summary; run 1 had Graham and Hayward. **Check authors.**
- **GAP:** no 2030 or 2050 SMR, large-nuclear or firmed-VRE LCOE from the 2025-26 final was found. An accessible text version exists: https://www.csiro.au/-/media/Energy/GenCost-2025-26-Final/GenCost_2026-26_Final_accessible-report.txt (not opened). **Victor: this one file closes the biggest gap in §8.2.**

---

## Darlington: LCOE, capital basis, opex

### opg_oeb_lcoe_lead
Ontario Power Generation, [2026]. *[Interrogatory response giving the DNNP levelised cost], EB-2025-0297* [OEB filing; exhibit and date TO VERIFY]. Pointers: Sollid, J.C., [2026]. LinkedIn post (https://dk.linkedin.com/in/sollid); Gramwzielone.pl, [2026]. *Ile będzie kosztować energia z SMR? Znamy pierwsze szacunki dla BWRX-300* (https://www.gramwzielone.pl/?p=20380125) [not opened].
- **Findings (search summary):** OPG projects an average LCOE of **C$149/MWh (2024$)** across the four units (about €95/MWh in 2025€). Unit 1 and common infrastructure are at OPG's Release Quality Estimate (Class 3); Units 2–4 are Class 4. Overnight cost about €8,200/kW on average, falling from about €10,700/kW (Unit 1) to €6,900/kW (Unit 4) (Sollid's analysis). The Consumers Council of Canada asked (letter, 27 February 2026) for the LCOE to go on the public record, so it may have been confidential at first.
- **Reliability:** if found on the OEB record, primary and high. LinkedIn and Gramwzielone are pointers only.
- **Supports:** `lcoe.md` §5 (benchmark), `initiative_cost.md` §5.

### wnn2025_dnnp_budget (pointer only)
World Nuclear News, 2025. *Canada's first SMR project: How is CAD20.9 billion cost calculated?* Available at: https://world-nuclear-news.org/articles/what-is-the-budget-for-canadas-first-smr-project [not opened].
- **Findings (search summary):** C$20.9 bn includes interest, escalation and contingency; Unit 1 C$6.1 bn excludes the C$1.6 bn of shared infrastructure (C$7.7 bn together). No split of interest, escalation or contingency was published. World Nuclear Report and The Globe and Mail call it "2024 dollars", which conflicts with "including escalation". **Check in OPG's FID material.**
- **Reliability:** trade news, pointer.

### rao2026_smr_opex
Rao, P., Kaffine, D.T. and Hodge, B.-M., 2026. *The consequences of high SMR operating costs in electricity markets*. arXiv preprint 2609.08929. Available at: https://arxiv.org/pdf/2609.08929 [not opened].
- **Findings (search summary of the appendix table):** BWRX-300 (300 MWe), manufacturer-advertised: fixed O&M **US$16.00/MWh**, variable O&M **US$3.55/MWh** (Lazard 2024 assumption), fuel **US$8.44/MWh**, investment US$2,250,000/MWe. Across SMR concepts, fixed O&M runs US$21,900–632,998 per MW-yr and fuel US$3.39–17.42/MWh. Table built on Steigerwald et al. (2023).
- **Reliability:** preprint, not peer-reviewed; vendor data. Medium-low. Dollar year TO VERIFY. Note how far the vendor's US$2,250/kW is from Darlington's C$17,400/kW.

### steigerwald2023_smr_costs
Steigerwald, B., Weibezahn, J., Slowik, M. and von Hirschhausen, C., 2023. Uncertainties in estimating production costs of future nuclear technologies: a model-based analysis of small modular reactors. *Energy*, 281, 128204. [Title wording and DOI TO VERIFY.] Reply to comments: *Energy* 313 (2024), 133828.
- **Findings (search summary):** construction-cost estimates for 15 SMR projects (19 concepts in the supplement); Monte Carlo on investment cost, WACC and wholesale prices; finds industry expectations far below expected costs. Disputed by Nøland and Hjelmeland (comment), answered by the authors.
- **Reliability:** peer-reviewed, high; contested. Use for the R1.3 synthesis (vendor vs independent costs).

### nei2025_costs_context / nei2020_costs_context
Nuclear Energy Institute, 2025. *Nuclear Costs in Context* [February 2025; 2023 data]. Washington, DC: NEI. Available at: https://www.nei.org/ (PDF "2024-Costs-in-Context-final.pdf") [not opened]. Older edition with 2019 data [year and URL TO VERIFY].
- **Findings (search summary):** US fleet average total generating cost **US$31.76/MWh (2023)** = fuel 5.32 + capital 7.06 + operating 19.38 (EUCG data). 2019 data: multi-unit sites US$28.38 vs **single-unit sites US$38.40**.
- **Reliability:** industry body using utility benchmark data; medium-high for existing large reactors, not for SMRs.

---

## Ontario and Canada: prices and programmes

### eccc_benchmark
Environment and Climate Change Canada, [2021, updated]. *The federal carbon pollution pricing benchmark*; and ECCC, *Update to the Pan-Canadian Approach to Carbon Pollution Pricing 2023–2030*. Ottawa. Available at: https://www.canada.ca/en/environment-climate-change/services/climate-change/pricing-pollution-how-it-will-work/federal-carbon-pollution-pricing-benchmark.html and .../carbon-pollution-pricing-federal-benchmark-information/federal-benchmark-2023-2030.html [not opened].
- **Findings (search summary):** minimum price rises C$15/t a year to **C$170/t in 2030**; ICAP gives **C$95 (2025)** and **C$110 (2026 compliance)**. On 14 March 2025 the government refocused pricing on industry; the fuel charge was set to zero from 1 April 2025; it will consult on the minimum national stringency standards.
- **Reliability:** primary, high, once opened; the 2026–2030 path may change.

### enbridge_eps
Enbridge Gas, n.d. *Federal carbon pricing* [online; Ontario EPS excess-emissions charge schedule]. Available at: https://www.enbridgegas.com/business-industrial/commercial-industrial/large-volume-services-rates/federal-carbon-pricing [not opened].
- **Findings (search summary):** Ontario's Emissions Performance Standards replaced the federal OBPS on 1 January 2022; excess-emissions charge C$50 (2022) … C$95 (2025), C$110 (2026) … C$170 (2030), payable only on emissions above a facility's limit.
- **Reliability:** utility page, medium. Replace with the Ontario regulation (O. Reg. 241/19) [TO VERIFY].

### finance_canada_ceitc
Department of Finance Canada, 2023. *Budget 2023* (Clean Electricity and Clean Technology ITCs). Pointer: MLT Aikins, 2023. *Feds aim to boost investment in clean technology and electricity* (https://www.mltaikins.com/insights/feds-aim-to-boost-investment-in-clean-technology-and-electricity/) [not opened].
- **Findings (search summary):** the Clean Electricity ITC covers non-emitting generation including SMRs and large nuclear, and is open to non-taxable entities including Crown corporations (so OPG could qualify); expected cost C$6.3 bn over four years from 2024-25 and C$19.4 bn 2028-29 to 2034-35. The Clean Technology ITC gives up to 30% for SMR equipment, phased out by 2034. **The 15% CE-ITC rate was not confirmed.**
- **Reliability:** law-firm summary of the budget; check the enacted Income Tax Act provisions.

### niagara2025_tender
City of Niagara Falls, 2025–26. *Ready mix concrete tender: bid price summaries* (incl. RFT-MW-OPS-26-12). Available at: https://niagarafalls.bidsandtenders.ca/ (documents cfe3a410-… and 2da2cc52-…) [not opened].
- **Findings (search summary):** 32 MPa concrete bids about **C$167–290/m³** before HST (four bidders; extraction misaligned). A 2023 Sault Ste. Marie tender gave C$545–595/m³ all-in, on a different basis.
- **Reliability:** primary procurement record, but municipal commodity concrete; low relevance to nuclear SCC. Used only to scale a % premium to C$/m³.

### cleanenergycanada2025_lowcarbon
Clean Energy Canada, 2025. *Building Toward Low Cost and Carbon* [report, April 2025]. Vancouver: Clean Energy Canada (Simon Fraser University). Available at: https://cleanenergycanada.org/wp-content/uploads/2025/04/Report_BuildingLowCostLowCarbon-V4-1.pdf [not opened].
- **Findings (search summary):** lower-carbon equivalents are available in Canada "at the same cost or a negligible premium" across almost all materials and case studies; concrete cutting carbon by up to 32% for no price increase; most premiums under C$3,000 of material budget.
- **Reliability:** advocacy think tank; case studies are buildings, not nuclear. Medium-low for our case. Supports the 0% premium scenario only.

---

## LC3 costs

### lc3_2019_financial
LC3 Project, 2019. *Financial attractiveness of LC3*. Lausanne: EPFL / LC3 project. Available at: https://lc3.ch/wp-content/uploads/2020/10/2019-LC3FinancialAttractiveness-WEB.pdf; summary https://lc3.ch/financial-attractiveness-of-lc3/ [not opened].
- **Findings (search summary):** LC3 "production cost is up to 25% lower compared to OPC", without carbon incentives, from energy and materials savings; modelled cash costs about US$30–47/t cement; clay transport distance (US$4/t within 10 km, US$17/t at 200 km) drives profitability. A Cuban study (lead) gives 15–25%.
- **Reliability:** promoter's feasibility study, medium-low; not Ontario prices.

### rmi2024_lc3
RMI, 2024. *The Business Case for LC3*. Boulder, CO: RMI. Available at: https://rmi.org/wp-content/uploads/dlm_uploads/2024/12/the_business_case_for_LC3_report.pdf [not opened].
- **Findings (search summary):** compares LC3 cost (US$/t) with local cement benchmarks in North America, Europe, Latin America and Africa (seven scenarios); LC3 is more profitable than OPC because calcined clay is cheaper than clinker. **The North America numbers were not visible. Check:** the North America scenario. This is the best candidate to replace the assumed premium.
- **Reliability:** NGO analysis, medium.

---

## Market and programmes

### nuscale_10k_2025
NuScale Power Corporation, 2026. *Form 10-K for the fiscal year ended 31 December 2025*. Washington, DC: SEC. Available at: https://www.sec.gov/Archives/edgar/data/1822966/000182296626000018/smr-20251231.htm [not opened].
- **Findings (search summary):** non-affiliate market value about **US$5.3 bn at 30 June 2025**; about 318.6 m Class A and 19.4 m Class B shares at 20 February 2026; revenue **US$31.5 m** (2024: 37.0), about US$23.9 m from a related party; loss from operations **US$689.6 m** (2024: 138.7), driven by G&A of US$609.8 m; cash and investments about US$1.3 bn; US$750 m raised through the at-the-market programme in Q4 2025. The earnings release (26 Feb 2026) mentions NRC approval of the uprated 77 MWe module and a non-binding ENTRA1–TVA agreement for up to 6 GW. A Reuters-sourced lead gives a net loss of US$355.8 m. **Check** which loss line to quote.
- **Reliability:** SEC filing, primary, high.

### oklo_10k_2025
Oklo Inc., 2026. *Form 10-K for the fiscal year ended 31 December 2025* (filed 17 March 2026). SEC. Available at: https://www.sec.gov/Archives/edgar/data/1849056/000162828026018698/oklo-20251231.htm [not opened].
- **Findings (search summary of a boardroomalpha.com mirror):** non-affiliate market value about **US$7 bn at 30 June 2025**; 173,568,788 shares at 13 March 2026.
- **Reliability:** primary once opened; the figure came from a mirror.

### oklo_10q_q3_2025
Oklo Inc., 2025. *Form 10-Q, quarter ended 30 September 2025*. SEC [URL TO VERIFY]. Pointer: Tiger Brokers news ("Reports Zero Revenue in Q3").
- **Findings (search summary):** zero revenue in Q3 2025; quarterly net loss US$29.7 m (prior year 9.96 m).

### nano_10k_fy2025
NANO Nuclear Energy Inc., 2025. *Form 10-K for the fiscal year ended 30 September 2025*. SEC. Available at: https://www.sec.gov/Archives/edgar/data/1923891/000149315225028285/form10-k.htm [not opened].
- **Findings (search summary quoting the cover page):** non-affiliate market value **US$703,834,174** at 31 March 2025 (closing price US$26.46); 50,474,294 shares at 16 December 2025. Fiscal 2025 net loss about US$40.1 m (Webull lead).

### doe2025_gen3smr
U.S. Department of Energy, 2025. *Energy Department Selects TVA and Holtec to Advance Deployment of U.S. Small Modular Reactors* [December 2025]. Washington, DC: DOE. Available at: https://www.energy.gov/articles/energy-department-selects-tva-and-holtec-advance-deployment-us-small-modular-reactors; programme page https://www.energy.gov/ne/generation-iii-small-modular-reactor-program [not opened].
- **Findings (search summary):** US$900 m Gen III+ SMR solicitation (re-issued March 2025); **US$400 m each to TVA** (BWRX-300 at Clinch River, Tennessee) and **Holtec** (two SMR-300s at Palisades, Michigan); US$100 m left for later. ANS report dated 3 December 2025.
- **Reliability:** primary, high, once opened.

### iaea2024_smr_catalogue
International Atomic Energy Agency, 2024. *Small Modular Reactors: Advances in SMR Developments 2024*. Vienna: IAEA; and the *SMR Technology Catalogue 2024* (ARIS) https://aris.iaea.org/Publications/SMR_catalogue_2024.pdf [not opened].
- **Findings (search summary):** about 70 active designs (the catalogue, as cited by an arXiv paper); IAEA DG: "more than 80 SMR designs"; OECD NEA dashboard tracked 129 designs in January 2026 (lead).
- **Supports:** vendor concentration: many designs, two or three with funded construction in the OECD.

### china_state_council_2026
Caixin Global, 2026. *Beijing clears eight new reactors as China accelerates nuclear buildout* (1 August 2026); Yicai Global, 2026. *China Approves Eight New Nuclear Reactors Worth USD24 Billion*. Pointers to State Council approval notices [not opened].
- **Findings (search summary):** on 31 July 2026 the State Council approved eight units in four projects (Jinqimen II, Taipingling III, Laiyang I, Zhuanghe I), total investment about CNY 160–170 bn, built by the state-owned CNNC, CGN and SPIC; 10 units approved in 2025. Linglong One (ACP100, 125 MWe, CNNC, Hainan): commercial operation expected H1 2026 per a CNNC official (Reuters, Dec 2025); IAEA PRIS showed no grid connection as of 20 May 2026 (lead). **No cost figure for Linglong One was found.**
- **Reliability:** business news; replace with NDRC/State Council notices or CNNC annual report. The state-led model (annual batch approvals, state-owned builders, about CNY 20 bn a unit) is the contrast with the Western financing model.

### ieefa2023_nuscale
Schlissel, D. [author TO VERIFY], 2023. *Eye-popping new cost estimates released for NuScale small modular reactor*. IEEFA. Available at: https://ieefa.org/resources/eye-popping-new-cost-estimates-released-nuscale-small-modular-reactor [not opened]. Same lead as in sources_run4.md: the US$89/MWh is net of about US$30/MWh of IRA credits. Advocacy analysis, medium.

### lca_results_2110 (internal)
lca-analyst, 2026. `03_LCA_Calculations/results/lca.md` (21/10/2026). Internal result, inputs TO VERIFY. LC3 saving 1,730 t CO₂e per unit (1,390–2,150), 5,200 t for Units 2–4; target volume 13,081 m³ per unit.
