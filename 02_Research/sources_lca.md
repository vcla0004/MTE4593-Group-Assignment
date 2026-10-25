Rubric coverage: R1.4, R1.3, R2.4, R2.5, R2.7, RB.6, R5.4

# Sources for the LCA (section 6, Appendices A, C, D)

lca-analyst, 21/10/2026. Keys match `03_LCA_Calculations/parameters_lca.yaml`. Harvard format per `01_Report/style-guide.md`.

> **Access warning.** On 21/10/2026 the egress proxy refused every primary host tried from this session, through both WebFetch and curl (403 on CONNECT, or DNS failure): unece.org, ipcc.ch, nrel.gov, circularecology.com, sciencedirect.com, doi.org, environdec.com, nrmca.org, opg.com, nrc.gov, gevernova.com, pubs.acs.org, mdpi.com, preprints.org, world-nuclear.org, osti.gov, lc3.ch, worldsteel.org, wikipedia.org, link.springer.com, iaea.org, crossref, openalex, web.archive.org. **Every entry below is a WebSearch lead and is [TO VERIFY]**: the number was seen in a search-engine summary, not in the document. Do not cite any of them until a person opens the URL, confirms the figure (and its GWP basis), and changes `status` to `verified` in the YAML. Fields marked "Check" say exactly what to confirm. Search snippets are never citations.

Priority for a human check (biggest effect on the headline or the C1 result first): gibon2023 (conversion heat range), parker2016, edf2024_lca, cac2020_epd, lc3_reduction_leads, peterson2005, gevernova_bwrx300_claims, crsi2017_epd, sca_epd, then the benchmarks.

## A. Plant, design and quantities

### ostroleka2023_pis (MAIN-CASE inventory from 25/10/2026)
BWRX-300 Ostrołęka sp. z o.o., 2023. *Small Modular Nuclear Power Plant Project Information Sheet* (prepared by ORLEN Synthos Green Energy). [pdf] Warsaw, August 2023. Copy reported at: https://mepr.gov.ua/wp-content/uploads/2023/10/Project-Information-Card.pdf
- **Team-deck value:** Table 14, p. 83: 50,000 m³ concrete and 14,000 t steel per BWRX-300 unit. **[TO VERIFY]**: a 25/10 web search confirmed the document (investor, date, ToC) but not the table; the mepr.gov.ua copy did not resolve from this session. Check: the table number, page, whether the figures are per unit or per site, and whether the steel includes equipment.

### pillai2019_lc3 (MAIN-CASE concrete factors from 25/10/2026)
Pillai, R.G. et al., 2019. Service life and life cycle assessment of reinforced concrete systems with limestone calcined clay cement (LC3). *Cement and Concrete Research*, 118, pp. 111–119. https://doi.org/10.1016/j.cemconres.2018.11.019
- **Team-deck value:** Table 2, M50 mixes: OPC 380 vs LC³ 270 kg CO₂e/m³ (28-day 60.0 vs 56.7 MPa). **[TO VERIFY]**: a 25/10 search confirmed the paper (seven mixes, four M35 and three M50; LC3 footprint "significantly lower" than OPC) but not the per-m³ values; the IITM author copy did not resolve. Check: Table 2 values, GWP basis, Indian (not Ontario) inputs. Full author list to add from the paper (not invented here).

### gevernova_bwrx300_gd
GE Vernova Hitachi Nuclear Energy, n.d. *BWRX-300 General Description* (005N9751). [pdf] Wilmington, NC: GE Vernova. Available at: https://www.gevernova.com/content/dam/gevernova-nuclear/global/en_us/documents/carbon-free-power/005N9751-BWRX-300-General-Description.pdf
- **Lead:** 300 MWe net; steel-plate composite containment about 19 m outside diameter and 38 m high.
- **Check:** net vs gross MWe; thermal power; design life; any concrete or steel quantities. **[TO VERIFY]**

### gevernova_bwrx300_claims
GE Vernova, n.d. *BWRX-300 Small Modular Reactor*. [online] Available at: https://www.gevernova.com/nuclear/carbon-free-power/bwrx-300-small-modular-reactor ; and Power Engineering, 2020. *GE Hitachi nuclear venture enters NRC licensing phase for small modular reactor design*. [online] Available at: https://www.power-eng.com/nuclear/ge-hitachi-nuclear-venture-enters-nrc-licensing-phase-for-small-modular-reactor/
- **Lead:** the design is claimed to need "~50% less concrete per unit of energy produced"; earlier wording "about 50% less building volume per MW", relative to the ESBWR; a DOE-funding release says "more than 50% less concrete and steel on a per MW basis compared with the ESBWR". Manufacturer projections, not measured quantities.
- **Use:** low bound of `concrete_intensity_m3_per_mwe` and `steel_intensity_t_per_mwe`. **[TO VERIFY]**

### peterson2005
Peterson, P.F., Zhao, H. and Petroski, R., 2005. *Metal and concrete inputs for several nuclear power plants* (UCBTH-05-001). [pdf] Berkeley: University of California, Berkeley. Available at: https://fhr.nuc.berkeley.edu/wp-content/uploads/2014/10/05-001-A_Material_input.pdf
- **Lead (via World Nuclear Association, *Energy Return on Investment*):** per rated MWe, Gen II PWR 75 m³ concrete and 36 t steel; ABWR 138 m³ and 46 t; EPR 128 m³ and 44.3 t; ESBWR 69 m³ and 33 t. The report's introduction: 1970s US plants needed 40 t steel and 90 m³ concrete per MW(average) at 0.9 capacity factor; the ESBWR uses 73% of the steel and 50% of the concrete of the ABWR.
- **Check:** the per-plant table; whether figures include equipment steel; rated vs average MW. **[TO VERIFY]**

### opg_forebay_update
Ontario Power Generation, 2025. *Darlington New Nuclear Project construction update* (quoted in `03_LCA_Calculations/Assumptions.docx`). [online] Available at: https://www.opg.com/projects-services/projects/nuclear/smr/darlington-smr/
- **Quote (as pasted by Sam):** "close to 4000 cubic metres of concrete and nearly 1000 tonnes of reinforcing steel have been placed in the forebay shaft as part of the installation of grade beams, the underdrain system, backfill operations, the base slab, and tower crane."
- **Check:** the dated update page; whether the forebay serves one unit or all four. **[TO VERIFY]**

### opg_basemat_story
Ontario Power Generation, 2026. *Laying the foundation for the G7's first small modular reactor*. [online] 30 April. Available at: https://www.opg.com/news-and-media/story/laying-the-foundation-for-the-g7s-first-small-modular-reactor [Accessed 21 October 2026; identified by web search, **page not opened**: opg.com refused by the proxy (DNS failure via WebFetch, 403 via curl)].
- **Lead (search-engine summaries of the OPG page, 21/10/2026):** on 22 April 2026 a crawler crane lowered the Unit 1 basemat module into the reactor-building shaft "35 metres below ground"; the module is 37 m in diameter, weighs about 2.1 million lb (= 952.5 t), and is the shared foundation of the reactor building and containment, built from Diaphragm Plate Steel Composite. Consistent secondary reports: World Nuclear News, *Darlington SMR project's foundation module milestone* (about 953 t; https://world-nuclear-news.org/articles/darlington-smr-nuclear-project-foundation-module-milestone, not opened); Vozpópuli (about 1,050 short tons); okdiario (July 2026, the original lead, which misdescribes the module as a "reactor").
- **Status:** the OPG primary now replaces okdiario as the reference to cite **once a person opens it**. Until then, cite it as read: "(Ontario Power Generation, 2026, as reported by World Nuclear News) [TO VERIFY]", or keep the news-report caveat in §6.2 (factcheck L9). **[TO VERIFY]**
- **Check:** 37 m diameter; 35 m depth; 2.1 million lb; date. NEDO-33926 Rev. 2 (NRC ML24110A134, not opened) would give the basemat and shaft-wall thicknesses that are still assumptions (`rb_basemat_thickness_m`, `rb_wall_thickness_m`).

### cnsc_cmd24_h3_1b
Canadian Nuclear Safety Commission, 2024. *CMD 24-H3-1B* (staff presentation, DNNP). [pdf] Ottawa: CNSC. Available at: https://api.cnsc-ccsn.gc.ca/dms/digital-medias/CMD-24-H3-1B.pdf/object
- **Lead:** "Designed for a 60-year operational life". NucNet (2025, https://www.nucnet.org/news/go-ahead-for-project-to-build-canada-s-first-small-modular-reactors-5-4-2025) reports Ontario saying 65 years. **[TO VERIFY]**

### arxiv2025_smr_overview
Authors TBC, 2025. *Technical overview of recent developments in small modular reactors in the United States*. arXiv:2504.02599. Available at: https://arxiv.org/pdf/2504.02599
- **Lead:** BWRX-300 870 MWt / 300 MWe net; 240 GNF2 assemblies; UO₂ in Zircaloy-2; average enrichment 3.8%, maximum 4.95%; 12–24-month cycles. Preprint, not peer reviewed; replace with NEDO-33977 (CNSC docket, CMD24-H3 reference) or GEH documents. **[TO VERIFY]**

### geneski_cns
Geneski, N., McKellar, J.M. and Atkinson, K.D., n.d. Life cycle environmental impacts of small modular reactors: BWRX-300 Darlington project. *Proceedings of the Canadian Nuclear Society*. Available at: https://proceedings.cns-snc.ca/index.php/pcns/article/view/7692
- **Lead (abstract):** construction GHG for concrete and steel scaled from a large reactor; "steel production, particularly for turbine plant equipment, produces more greenhouse gas emissions than concrete production". Early-stage; no numbers seen. Our result agrees in direction (steel about 2x concrete). **[TO VERIFY year and numbers]**

## B. Concrete and cement

### cac2020_epd
Cement Association of Canada, 2022. *Environmental Product Declaration: General Use (GU) and Portland-Limestone (GUL) Cements* (regionalised industry average, 2020 data; ASTM-verified). [pdf] Available at: https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blt9992df315e96e31c/697b1f51f6a61062618f5048/919.CAC_General_Use_(GU)_and_Portland-Limestone_(GUL)_Cements.pdf
- **Lead:** GWP100 (IPCC 2013) GU 796 / 854 / 898 kg CO₂e/t for West / Central / East; GUL 732 / 798 / 864.
- **Check:** which region contains Ontario; year of issue; clinker factor. **[TO VERIFY]**

### stmarys_bowmanville_epd
NRMCA, 2021. *Environmental Product Declaration EPD 20046: St Marys Cement, Bowmanville plant*. [pdf] Available at: https://www.nrmca.org/wp-content/uploads/2021/09/NRMCA_EPD20046StMarys_EPD_BOW_Sep2021.pdf
- **Lead:** covers GU, MS, MH and GUL (Type IL) from Bowmanville, Clarington. No GWP seen. **Best local factor once opened; replaces `ef_gu_cement`.** **[TO VERIFY]**

### sca_epd
Slag Cement Association, n.d. *Industry-average EPD for slag cement* (USA and Canada). [pdf] Available at: https://www.lafarge.ca/sites/canada/files/images/sca_epd_for_slag_cement.pdf
- **Lead:** 146.6 kg CO₂e/t (4.6 raw material, 57.0 transport, 85 manufacturing). Lafarge NewCem plant EPD: 93.4 kg CO₂e/t (https://lafarge.ca/en/lafarge-drives-sustainable-construction-enhanced-epd-certifications-onecemr-and-newcemr-cements). **[TO VERIFY]**

### crmca2022_ontario_epd
Canadian Ready-Mixed Concrete Association, 2022. *Industry-wide EPD for ready-mixed concrete, Ontario* (EPD 351, valid to 27 July 2027). [pdf] Available at: https://www.rmcao.org/wp-content/uploads/2023/04/CRMCA-EPD-Ontario-20220803.pdf
- **Lead:** 35 MPa baseline with air 334.49 kg CO₂e/m³; 35 MPa industry benchmark (6% slag, 4% fly ash) 417.05 kg CO₂e/m³ (Concrete Ontario summaries). Used only as a check on the per-m³ model. **[TO VERIFY]**

### efnarc2005
EFNARC, 2005. *The European Guidelines for Self-Compacting Concrete: Specification, Production and Use*. Farnham: EFNARC.
- **Lead (secondary, a 2024 Egyptian journal article):** typical SCC powder content 360–500 kg/m³. **[TO VERIFY]**

### scrivener2018
Scrivener, K., Martirena, F., Bishnoi, S. and Maity, S., 2018. Calcined clay limestone cements (LC3). *Cement and Concrete Research*, 114, pp.49–56. Available at: https://doi.org/10.1016/j.cemconres.2017.08.017 (copy: https://www.devalt.org/Pdf/L2_SixThemePdfs/Calcined_clay_limestone_cements_(LC3).pdf)
- **Lead:** kaolinitic clay is the only SCM available in the quantities needed; LC3 composition about 50% clinker, 30% calcined clay, 15% limestone, 5% gypsum; the "about 40% CO₂ reduction" appears in an EPFL abstract, not confirmed in the paper text. **Check:** composition, CO₂ claim and its basis. **[TO VERIFY]**

### lc3_reduction_leads
Five leads for the LC3 binder GWP cut vs OPC (parameter `lc3_gwp_reduction`), all **[TO VERIFY]**:
- ENR, 2018. *Clay and limestone cement could cut carbon emissions* (7 May 2018): "30% less CO₂". https://digital.bnpmedia.com/article/Construction+Materials/3078554/494167/article.html
- Development Alternatives, n.d. *LC3 Sustainability Assessment* (ver 1.14): 700 / 520 / 465 kg CO₂/t for OPC / PPC / LC3 (34% cut). https://devalt.org/images/L2_ProjectPdfs/Report%20-%20LC3%20Sustainability%20Assessment_ver1.14.pdf
- LC3 project, 2015. *LCA of LC3: India team progress* (industry meeting, Sept 2015): 856 vs 543 kg CO₂/t (37%). https://lc3.ch/wp-content/uploads/2023/03/LCA-of-LC3-India-team-progress-Industry-meeting-Sep-2015.pdf
- EPFL Graphsearch abstract of Scrivener et al. (2018): about 40%. https://graphsearch.epfl.ch/en/publication/286379
- LACCEI, 2026. Contribution 2661: cradle-to-gate 903.5 vs 513.5 kg CO₂e/t (43%). https://laccei.org/LACCEI2026-Chile/full-papers/Contribution_2661_final_a.pdf

### hooton2023_csa_a3001
(Already in `sources_run2.md` as Hooton_2023_ACI and CSA_A3000_23.) CSA A3001 Type IT: up to 15% limestone with any SCM including calcined clay. LC3-50's 15% limestone sits at that cap. **[TO VERIFY]**

## C. Steel

### crsi2017_epd
Concrete Reinforcing Steel Institute, 2017. *Industry-wide EPD for fabricated steel reinforcing bar* (superseded by EPD 362, 20 Sept 2022, valid to 19 Sept 2027). [pdf] Available at: https://www.astm.org/v3/assets/blt5eb0a2cb04534832/blt4900ac0ff22764a2/697b1fc25e3544dd57d83a3d/362.EPD_for_CRSI_EPD_FINAL_2017-08-28.pdf
- **Lead (CRSI presentation to CDOT, 2022):** 2017 EPD GWP 0.97 t CO₂e/t. **Check:** the 2022 EPD value (should replace 0.97). **[TO VERIFY]**

### bcca2022_limits
American Institute of Steel Construction, 2022. *Buy Clean California quick guide*. [pdf] Available at: https://www.aisc.org/contentassets/937a380ddd404a2da0c48669d438bf3b/quickguide_buycleancali2022.pdf
- **Lead:** GWP limits (t CO₂e/t): rebar 0.89 mill gate, 0.98 with US-average fabrication; hot-rolled sections 1.01 / 1.22; plate 1.49 / 1.73. These are policy ceilings, not industry averages; used as North American proxies. **[TO VERIFY]**

### ice_v3
Circular Ecology, 2019. *Inventory of Carbon and Energy (ICE) database v3.0*. Bath: Circular Ecology. Values via IStructE, 2020/2022. *A brief guide to calculating embodied carbon* and *How to calculate embodied carbon*, 2nd ed. London: IStructE. https://www.istructe.org/IStructE/media/Public/TSE-Archive/2020/A-brief-guide-to-calculating-embodied-carbon.pdf
- **Lead:** rebar 1.99, steel sections 1.55 kg CO₂e/kg (world average); C32/40 concrete 25% GGBS 0.120, 50% GGBS 0.089 kg CO₂e/kg; CEM I 300 kg/m³ mix about 353 kg CO₂e/m³ (v3 beta slides). **[TO VERIFY]**

## D. Fuel cycle

### parker2016
Parker, D.J., McNaughton, C.S. and Sparrow, G.A., 2016. Life cycle greenhouse gas emissions from uranium mining and milling in Canada. *Environmental Science & Technology*, 50(17), pp.9746–9753. Available at: https://pubs.acs.org/doi/10.1021/acs.est.5b06072
- **Lead:** Saskatchewan mine-mills 81, 64 and 34 kg CO₂e/kg U₃O₈ at 0.74%, 1.54% and 4.53% U₃O₈; production-weighted 42 at 3.81%; 24 with hydro electricity. Press summary: about 1 g CO₂e/kWh, which our model reproduces (1.02 g/kWh mode case). **Check:** authors and pages. **[TO VERIFY]**

### gibon2023
Gibon, T. and Hahn Menacho, Á., 2023. Parametric life cycle assessment of nuclear power for simplified models. *Environmental Science & Technology*, 57(38), pp.14194–14205. Available at: https://doi.org/10.1021/acs.est.3c03190 (open copy: https://pmc.ncbi.nlm.nih.gov/articles/PMC10537461/)
- **Lead:** global 2020 average 6.1 g CO₂e/kWh (scenarios 5.4–122); mining and milling 46%; centrifuge 50 kWh/SWU (40–100), diffusion 2,500 (2,400–3,000); conversion 11.8 kWh electricity (10.3–16.9) and 26 kWh heat (26–665) per kg U; fabrication 36 kWh/kg (36–50); 6.74 SWU/kg fuel (WNA). **Check:** volume/pages; the distribution of conversion heat (it dominates our uncertainty). **[TO VERIFY]**

### ipcc2006_gl
IPCC, 2006. *2006 IPCC Guidelines for National Greenhouse Gas Inventories*, Vol. 2 Energy, Ch. 2, Table 2.2. Hayama: IGES.
- **Lead:** natural gas default 56,100 kg CO₂/TJ (= 0.202 kg/kWh). **[TO VERIFY]**

### epa_power_profiler
US EPA, 2024. *Power Profiler: terms, calculations and data sources*. [pdf] Available at: https://www.epa.gov/system/files/documents/2024-04/power-profiler-terms-calculations-and-data-sources.pdf ; US EPA, n.d. *Greenhouse Gas Equivalencies Calculator: calculations and references*. https://www.epa.gov/energy/ghg-equivalencies-calculator-calculations-and-references
- **Lead:** US annual average 823.1 lb CO₂/MWh (0.373 kg/kWh; eGRID vintage unclear, CO₂ only); eGRID2022 national marginal 1,405.3 lb CO₂/MWh (0.637 kg/kWh). **[TO VERIFY]**

### taf2025
(In `sources.md`.) Ontario 2024 average 73.8 g CO₂e/kWh; marginal 343. **[TO VERIFY]**

## E. Literature stage data and benchmarks

### edf2024_lca
EDF R&D, 2024. Life cycle assessment of nuclear power in France: EDF case study. *EPJ Nuclear Sciences & Technologies*, 10, art. 5. Available at: https://www.epj-n.org/10.1051/epjn/2024005 (authors TBC)
- **Lead:** 3.7 g CO₂eq/kWh for the French fleet (2019 data); sensitivity 2.9–4.6; 60-year life lowers it 8% vs 40 years. Shares (as reported by World Nuclear News and Euronuclear, not the abstract): upstream 57%; "production" 28% (construction 16%, operation 9%, decommissioning 3%); downstream 15% by difference. Used for `om_g_per_kwh`, `decom_g_per_kwh`, `backend_g_per_kwh`. **Check:** the shares in the paper; whether downstream includes reprocessing. **[TO VERIFY]**

### unece2021
(In `sources.md`.) UNECE, 2021. *Life Cycle Assessment of Electricity Generation Options*. Geneva: UNECE. https://unece.org/sites/default/files/2021-10/LCA-2.pdf. Nuclear 5.1–6.4 g CO₂e/kWh; "the fuel chain (front-end) contributes most". **[TO VERIFY]**

### carless2016
Carless, T.S., Griffin, W.M. and Fischbeck, P.S., 2016. The environmental competitiveness of small modular reactors: a life cycle study. *Energy*, 114, pp.84–99. Available at: https://ideas.repec.org/a/eee/energy/v114y2016icp84-99.html
- **Lead:** Westinghouse SMR mean 9.1 g CO₂e/kWh (90% CI 5.9–13.2); AP1000 8.4 (5.5–12.1); SNUPPS 13.6 (10.5–17.3); without the fuel cycle the SMR and AP1000 are effectively equal. (Carless's thesis gives 7.4 (4.5–11.3); cite the paper.) **[TO VERIFY]**

### warner_heath2012
Warner, E.S. and Heath, G.A., 2012. Life cycle greenhouse gas emissions of nuclear electricity generation: systematic review and harmonization. *Journal of Industrial Ecology*, 16(S1), pp.S73–S92. Available at: https://doi.org/10.1111/j.1530-9290.2012.00472.x
- **Lead:** 27 studies, 99 LWR estimates; harmonised median 12 g CO₂e/kWh (from 13), IQR 17 (from 23), maximum 110. **[TO VERIFY]**

### ng2025_jie
Ng, et al., 2025. Life-cycle greenhouse gas emissions associated with nuclear power generation in the United States. *Journal of Industrial Ecology*, 29(3), pp.719–732. Available at: https://onlinelibrary.wiley.com/doi/full/10.1111/jiec.70008
- **Lead:** GREET; 3.0 g CO₂e/kWh for the US nuclear fuel cycle; electricity across the fuel chain 53% of it. **Check:** full author list; whether 3.0 includes the plant. **[TO VERIFY]**

### ipcc2014_annex3, nrel2021_lca
(In `sources.md`.) Values not confirmed even in a search result; stress tests only. IPCC AR5 WGIII Annex III Table A.III.2 nuclear min 3.7 / median 12 / max 110 (as commonly quoted) are held as `bm_ipcc2014_*` in `parameters_lca.yaml`; F5 draws them only when set to `verified`. **3.7 is not a Warner and Heath (2012) figure** (factcheck L31). **[TO VERIFY]**
