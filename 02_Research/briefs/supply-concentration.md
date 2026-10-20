Rubric coverage: R3.2, R3.5, R3.6, R3.7, R3.8, R2.1, R2.7, R1.3, R1.4, R4.3

# Brief: supply concentration and geopolitics of the BWRX-300 fuel chain (report §8.3, slide 13)

Analyst run 3, 20/10/2026. Working: `03_LCA_Calculations/results/hhi.md` (script `scripts/hhi.py`, inputs `parameters_run3.yaml`, sources `02_Research/sources_run3.md`).

> **Status: NOT YET CITABLE.** The primary pages (WNA, NEA/IAEA, DOJ/FTC, govinfo) could not be opened from this session because of network restrictions. All numbers come from search extracts of those pages, and they pass internal sum checks. **Before the writer or the deck uses them, Victor or the fact-checker must open the five key pages** (checklist at the end) and set `verified: true` in `parameters_run3.yaml`. If any value changes, rerun `python3 -I 03_LCA_Calculations/scripts/hhi.py`.

## Question
How concentrated is each front-end stage of the fuel chain for a BWRX-300 (mining, conversion, enrichment)? How much worse does it get if Russian supply is lost? What does that mean for building the reactor at Darlington compared with an Australian coal site, and what non-technical measures reduce the risk?

## Answer
1. **Every front-end stage is "highly concentrated" under the current US DOJ/FTC (2023) threshold (HHI > 1,800).** Enrichment is the worst: HHI **3,009** (2025 capacity), which is also highly concentrated under the older 2010 threshold (> 2,500). Mining by country is 2,341 and conversion by company is 2,111 (WNA_mining; WNA_conversion; WNA_enrichment; USDOJ_FTC_2023; USDOJ_FTC_2010).
2. **Russia (Rosatom/TENEX) holds 42.8% of world enrichment capacity in 2025** (29,133 of 68,076 thousand SWU/yr). The figure was 43.3% in 2022 and is planned to be 38.3% in 2030 (WNA_enrichment). This confirms the 40–44% in secondary sources, subject to verification. Russia also holds 20.2% of conversion capacity, but only 4.5% of mine output by country.
3. **Sanctions make concentration worse.** Removing Russia (the US *Prohibiting Russian Uranium Imports Act*, PL 118-62: ban from August 2024, waivers end 1 January 2028; and Russia's November 2024 counter-restriction) raises the HHI at every stage: enrichment 3,599, conversion 2,674, mining 2,546. For a Western utility, CNNC's capacity is also effectively unavailable, since WNA sizes it for China's own fleet. That leaves enrichment as an **Urenco–Orano duopoly (Urenco 68.8%, Orano 29.8%; HHI 5,621, about 1.8 equivalent suppliers)** (US_PL118_62; WNN_2024).
4. **Mining risk is about countries, not companies.** At company level the HHI is 851–1,384 (bounded from the top three shares only), which is unconcentrated. The country HHI is driven by Kazakhstan's 38.6%.
5. **Australia has the resource but not the industry.** It holds 28% of identified recoverable resources at < USD 130/kgU (Red Book 2024; NEA_IAEA_2025), the largest share of any country. That is 29% in the 2026 edition as tabulated by WNA, although a second WNA page gives 27% (NEA_IAEA_2026; conflict, TO VERIFY). Yet Australia mined only 7.6% of world output in 2024 (4,598 tU) and has **0% of conversion and 0% of enrichment** capacity.
6. **Darlington is far better placed than an Australian reactor.** OPG's first BWRX-300 fuel chain avoids Russia entirely: Cameco's Saskatchewan uranium, converted at Port Hope, Ontario; enriched by Urenco USA (New Mexico), with additional enriched product from Orano (France); and fabricated by GNF-Americas in the US (OPG_2023_fuel). Canada supplies 23.8% of world mine output and owns 20.2% of world conversion capacity (36.2% of the non-Russian, non-Chinese capacity). Only enrichment and fabrication cross a border, and both go to treaty allies. An Australian BWRX-300 would export ore concentrate for conversion *and* enrichment *and* fabrication. Two of those steps (enrichment and fuel fabrication) are named in EPBC s140A and ARPANS s10, so they cannot be built at home under current law. Conversion is not on either federal list (APH_2024; run 2 to confirm), but some state Acts cover it.

## Numbers table (for T3 and slide 13)

| Stage | Measure (base year) | HHI | Class (2023 / 2010) | Russia share | HHI without Russia | HHI without Russia and China | Australia share | Canada share |
|---|---|---:|---|---:|---:|---:|---:|---:|
| Mining | Country output, tU (2024) | **2,341** | High / Moderate | 4.5% | 2,546 | 2,686 | 7.6% | 23.8% |
| Conversion | Company capacity, tU/yr (WNA table) | **2,111** | High / Moderate | 20.2% | 2,674 | 3,615 | 0% | 20.2% (Cameco) |
| Enrichment | Company capacity, kSWU/yr (2025) | **3,009** | High / High | **42.8%** | 3,599 | 5,621 | 0% | 0% |

Resources: Australia 28% of identified recoverable resources at < USD 130/kgU (Red Book 2024). Thresholds: > 1,800 highly concentrated (DOJ/FTC 2023); 1,500–2,500 moderate and > 2,500 high (DOJ/FTC 2010).

**Sensitivity** (full table in `results/hhi.md` §4):
- Enrichment ranges from 2,724 (2030 plans) to 3,065 (2022).
- Mining ranges from 2,246 to 2,370 across 2022–2024.
- Conversion falls to 2,015 if ConverDyn's capacity is 15,000 rather than 7,000 tU.
- No case drops below 1,800.
- Removing Russia is the largest effect at every stage.

**Slide 13 values:** enrichment HHI **≈ 3,000** (3,009); Russian enrichment share **≈ 43%** (42.8%, 2025 capacity). The slide's note says "above 2,500 counts as highly concentrated". That is the superseded 2010 threshold, so change it to "above 1,800 (US DOJ/FTC 2023)", or name the 2010 guidelines. Enrichment is highly concentrated under both.

## Translation to practice (R3.5)
- **Darlington:** supply concentration is a **price and contract risk, not a build-stopper**. The chain already avoids Russia, and OPG split enrichment between Urenco and Orano. The remaining exposure is the Urenco–Orano duopoly (HHI 5,621 outside Russia and China). New SWU capacity is coming (WNA's table has Orano rising from 7,500 to 10,000 kSWU and Urenco from 17,300 to 18,000 by 2030; the Georges Besse II extension detail is from a secondary extract, TO VERIFY). Units 2–4 will buy fuel in a tighter Western market as US utilities replace Russian SWU before the 2028 waiver deadline.
- **Australian coal site (Liddell):** supply concentration adds a **sovereign-risk barrier on top of the legal ban**. Every front-end step after mining would be offshore. Australia's resource share (28%) gives bargaining power only as a supplier of concentrate, not as a fuel buyer.
- **Link to the initiative (R4.3):** the front end is the largest life-cycle hotspot (plan §2.1, C3, TO VERIFY with Sam). The same front end is the most concentrated market. Laser enrichment of tails (C3: Australian-invented, commercialised in the US because of s140A) is where supply security and decarbonisation meet. That makes it future work for §10.

## Non-technical solutions, compared (R3.6, R3.7)

| Option | Supply security | Cost | Legal in Australia now? | Time to effect | Comment |
|---|---|---|---|---|---|
| Long-term, dual-source contracts with allied enrichers (Urenco + Orano), as OPG did | High within the duopoly | Medium (term premium) | Yes (it's a purchase) | Immediate | Proven model (OPG_2023_fuel). Doesn't reduce the HHI, only the exposure |
| Strategic inventory of enriched product or fabricated fuel (e.g. 2–3 reloads) | High against short disruptions | Working-capital cost | Yes (storage of fuel needs an ARPANSA licence; TO VERIFY with run 2) | 1–3 years | Size it in SWU and tU per reload once Leroy/Sam give the BWRX-300 reload data (gap) |
| Domestic conversion plant (Australia) | Medium: removes one hop | High; a plant around 12,500 tU/yr is Cameco-scale | Not named in s140A or s10 (TO VERIFY); state bans may apply | 10+ years | Would make Australia a converter for allies. The demand case rests on exports, not on one SMR |
| Domestic enrichment (Australia) | Highest | Very high | **No** (s140A, s10) | 15+ years, after law change | Needs repeal. Silex/GLE technology is being commercialised in the US instead (C3) |
| Equity in allied capacity (e.g. offtake-linked investment in Urenco USA, Orano or GLE expansions) | Medium–high | Medium | Yes | 3–7 years | Uses Australia's resource leverage. Canada–US fuel cooperation is the precedent [TO VERIFY] |

**Implementation steps (for §8.6):**
1. Make dual-source, allied-only enrichment contracts a condition of any public finance (as in OPG's model).
2. Hold a strategic fuel inventory sized in reloads.
3. Commission a feasibility study of domestic conversion. It's the only front-end step not named in the federal bans (TO VERIFY), and it builds on Australia's 28% resource share.
4. Treat enrichment as an alliance procurement question (AUKUS partners), not a domestic build, unless s140A and s10 are amended.

## Disagreements between sources (R1.3)
- **Russia's enrichment share:** 42.8% (WNA, 2025 capacity) vs "~40%+" on the slide and 40–44% in secondary sources. The spread is the year (38.3% in 2030 to 43.3% in 2022) and capacity vs output.
- **Rosatom and CNNC capacity:** an older CRAI (2025) table gives Rosatom 26,200 and CNNC 11,000 kSWU for 2025, against WNA's 29,133 and 13,789. Using CRAI's figures would lower Russia's share. Report WNA and mention the range.
- **Australia's resource share:** 28% (Red Book 2024, < USD 130) vs 29% and 27% (two WNA tabulations of Red Book 2026). The Meeting 2 note says "30% of reserves". Use the Red Book term *identified recoverable resources* and name the edition and cost category.
- **ConverDyn's capacity:** 7,000 tU (WNA table) vs about 15,000 tU (secondary). The sensitivity covers both.

## Gaps
1. **Verification (blocking):** the primary pages must be opened (checklist below).
2. BWRX-300 annual fuel need (tU of enriched uranium per reload, enrichment %, cycle length) to size SWU per year and a strategic reserve. **Request to Leroy** (plant data) and Sam (fuel-cycle stage) via plan §5.
3. Mining by company, complete 2024 table (only the top three retrieved), and Rosatom's (Uranium One) stakes in Kazakh mines. STRETCH.
4. Kazakh export routes via Russia (Trans-Caspian route as the alternative): not researched.
5. Exact EPBC s140A and ARPANS s10 wording, and whether NSW's *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* bans conversion. **Run 2 owns this.**
6. Geoscience Australia AECR 2026: Australia's identified resources (an Australian primary cross-check).
7. Fabrication concentration (GNF, Framatome, Westinghouse) not computed. Only BWR-fuel fabricators matter for the BWRX-300 (STRETCH).

## Verification checklist (open each page; tick in `parameters_run3.yaml`)
- [ ] WNA *Uranium Enrichment*: the four company rows plus Other, 2022/2025/2030, and the totals
- [ ] WNA *Conversion and Deconversion*: five company rows, capacity and production, and the table date
- [ ] WNA *World Uranium Mining Production*: 2024 country rows and the world total; the company table and its year
- [ ] NEA/IAEA *Uranium 2024* (and *Uranium 2026*): Australia's tonnage and % by cost category, with the table number
- [ ] DOJ/FTC 2023 *Merger Guidelines* (exact 1,800 wording, section number) and 2010 *Horizontal Merger Guidelines* section 5.3
- [ ] PL 118-62 text: start date, waiver end and sunset
- [ ] OPG press release on the Darlington SMR fuel suppliers (title, date, the minister's quote)
