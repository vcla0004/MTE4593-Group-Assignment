Rubric coverage: R1.4, R3.2, R3.8, R2.1, R5.4

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

### APH_2024
Parliamentary Library, 2024. *Nuclear activities prohibitions: a quick guide*. [online] Canberra: Parliament of Australia, 30 May 2024. Available at: https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Quick_Guides/2023-24/NuclearActivitiesProhibitions [Accessed 20 October 2026; not opened].
- **Findings (extract):** EPBC Act s140A(1) bars the minister from approving a nuclear fuel fabrication plant, a nuclear power plant, an enrichment plant or a reprocessing facility. ARPANS Act s10 bars the CEO from licensing the same four. **Conversion plants are not on either list.** Some state laws (NSW; a 2007 Queensland bill) do cover conversion.
- **Reliability:** High (Parliamentary Library), but run 2 owns the law and must confirm the wording in the Acts themselves (Federal Register of Legislation, current compilations).
- **Supports:** §8.1, §8.3 (domestic conversion is the one front-end step that federal law doesn't prohibit by name; TO VERIFY with run 2).

### secondary_converdyn
Wikipedia, [n.d.]. *ConverDyn*; Strategist and Architect, [2025]. "There is no alternative" (Substack). [online] [Accessed 20 October 2026; extracts only].
- **Findings:** the Metropolis plant's capacity is given as about 15,000 tU/yr, or 15,000–17,600 tU/yr after a recent expansion.
- **Reliability:** Low. Used only as a sensitivity bound, never cited in the report. Replace with Solstice/ConverDyn or NRC licence data if found.
- **Supports:** Appendix B sensitivity; `conversion_by_company.converdyn_capacity_alt`.
