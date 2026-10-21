Rubric coverage: RB.5, R2.4, R3.8, R2.1, R2.3, R2.7, R4.3, R3.1, R3.6, RB.6 (also supports R3.2, R3.4, R1.3, R5.2)

<!--
CHANGELOG
- v2.1, 21/10/2026 (writer, Q8). B6 re-based on `same_money.md` after the GenCost 2030 re-run (SMR A$306, 230–382; renewables A$107, 89–125): text, Table B24 and Tables B25–B28 replaced, alternative reading (A$514 / A$102) kept as sensitivity rows; B5.4 "45×" replaced by the scripted 44× (44–223×). TODOs 11 and 12 closed (the GenCost table and carbon price remain [TO VERIFY]). Rubric items: R2.3, R3.1, RB.5, RB.6.
- v2, 21/10/2026 (writer, Q4). Appended B4 (displacement), B5 (schedule value, including C1's break-even and the 30–223× derivation) and B6 (same money), Tables B15–B28, from Q2's re-based `results/` files; working for §7 and §6.3 finding 5 (factcheck L47; review audit §2, R2 and R4 rows). The rest of v1 is unchanged.
- B6 states both GenCost readings: §7 uses run 5's 2030 reading (rows in Table B28); Tables B26–B27 are still on run 1's A$514 basis until `same_money.py` is re-run [TO VERIFY: GenCost table/year]. Carbon price: federal path C$95/C$115 [TO VERIFY]; the superseded path is shown for comparison only.
- One hand calculation (the 45× low end on the current price path, B5.4) is flagged for scripting. Remaining TODO 10 is now partly done (LCOE and MCDA still to come).
- v1, 20/10/2026 (writer). First draft of Appendix B1–B3, cited from §8.1 and §8.3.
  - review.md A10 and top priority 2; factcheck.md A3, A10 and blocking item 6: the Senate arithmetic, licensing durations, HHI working and route scores now exist in an appendix. The §8.1 and §8.3 pointers are updated to "Appendix B1/B2/B3".
  - factcheck.md A3: the majority of 39 is stated as "all 76 senators voting". review.md §8.1 point 2: the "36 even with every other crossbencher" robustness check is shown (B1.2).
  - review.md §8.3 point 1 and T3 point 6: each HHI result carries both its 2023 and its 2010 class, and the "scale, not legal test" caveat is stated (B2.1, B2.3).
  - factcheck.md B3/B18: the mining-by-company case (1,118) is shown as the one case below 1,800, with its working (B2.4).
  - factcheck.md A10, review.md §8.1 point 6: the route scores are labelled as our qualitative judgement, with the weight test (B3).
  - Not done here: the CRAI enrichment row (review.md §8.3 point 2; analyst must add it to hhi.py and sources.md first), and the other Appendix B calculations listed in plan §3 (displacement, schedule value, same money, LCOE, MCDA).
- Presentation items: R5.1 (each subsection opens with its result); R5.2 (Tables B1–B14, caption and source above each table, as review.md asks); R5.3 (prose kept to the steps; appendices do not count towards the page limit, plan §1 [confirm, T2]); R5.4 (Harvard, same author forms as §8.1 and §8.3); R5.5 (Australian English).
- Every input is unverified. All [TO VERIFY] markers from the briefs, results and parameter files are kept.
-->

## Appendix B. Working for the policy and supply-chain analysis

This appendix gives the full working behind §8.1 (law and licensing), §8.3 (fuel-supply concentration) and §7 (displacement, the value of schedule and the same money). Every number is produced by a script in `03_LCA_Calculations/scripts/` from a parameter file, so it can be re-run. **No input has yet been checked against its primary source** (`status: TO VERIFY` in `parameters_run1.yaml`, `parameters_run2.yaml` and `parameters_run5.yaml`; `verified: false` in `parameters_run3.yaml`).

| Subsection | Script (run from the repository root) | Inputs | Output |
|---|---|---|---|
| B1 Legal and political pathway | `python3 -I 03_LCA_Calculations/scripts/law_timelines.py` | `03_LCA_Calculations/parameters_run2.yaml` | `03_LCA_Calculations/results/law_timelines.csv` |
| B2 Supply concentration (HHI) | `python3 -I 03_LCA_Calculations/scripts/hhi.py` | `03_LCA_Calculations/parameters_run3.yaml` | `03_LCA_Calculations/results/hhi.md`, `hhi_summary.csv` |
| B3 Routes to a licensable SMR in Australia | none (qualitative scoring) [TODO: move into the MCDA script, analyst run 7] | Law brief §5 | This appendix |
| B4 Displacement | `python3 -I 03_LCA_Calculations/scripts/displacement.py` | `03_LCA_Calculations/parameters_run1.yaml` | `03_LCA_Calculations/results/displacement.md` |
| B5 Value of schedule | `python3 -I 03_LCA_Calculations/scripts/schedule_value.py` | `parameters_run1.yaml` (cost inputs read from `parameters_run5.yaml`) | `results/schedule_value.md` |
| B6 Same money | `python3 -I 03_LCA_Calculations/scripts/same_money.py` | `parameters_run1.yaml` | `results/same_money.md` (cross-check: `results/lcoe.md`) |

---

### B1. Legal and political pathway

**Result.** Three laws bar an SMR at Liddell, and each has a different veto holder. On current party positions, the federal repeal is 7 Senate votes short (3 short even with every other crossbencher), and the NSW repeal bill is stalled. For comparison, Darlington's licence to construct took about 29 months, 17.9 years after its environmental assessment began.

#### B1.1 The three legal barriers and what removes each

*Table B1. The legal barriers to an SMR at Liddell, what removes each, and who holds the veto.*
*Source: legislation as named [TO VERIFY wording in the current compilations]; ARPANSA (n.d.); Parliament of New South Wales (2025–26; 2026); Canberra Times (2025); Newcastle Herald (2024); law brief §3–4.*

| # | Barrier | Instrument and effect (as extracted) | What removes it | Who decides (veto holder) | Status, October 2026 |
|---|---|---|---|---|---|
| 1 | Federal environmental approval | *Environment Protection and Biodiversity Conservation Act 1999* (Cth) s 140A (parallel bars in ss 37J and 146M): the Minister "must not approve" an action involving the construction or operation of a nuclear power plant [TO VERIFY] | Amendment of ss 37J, 140A and 146M | Commonwealth Parliament; in practice the Senate (B1.2) | In force. Whether the 2025 EPBC reforms changed s 140A is unchecked (Norton Rose Fulbright, 2025) [TO VERIFY] |
| 2 | Federal radiation licensing | *Australian Radiation Protection and Nuclear Safety Act 1998* (Cth) s 10(2): the CEO "must not issue a licence" for a nuclear power plant [TO VERIFY]. ARPANSA licenses only Commonwealth-controlled bodies (s 13, "controlled person") (ARPANSA, n.d.) [TO VERIFY] | Repeal of s 10, **and** a regulator with power over private operators (route choice, B3) | Commonwealth Parliament (Senate) | In force. A Senate committee recommended against the 2022 repeal bill (Senate Environment and Communications Legislation Committee, 2023) [TO VERIFY]; the bill lapsed at prorogation [TODO: source needed: ParlInfo bill page] |
| 3 | State ban | *Uranium Mining and Nuclear Facilities (Prohibitions) Act 1986* (NSW) s 8: offence to build or operate a nuclear reactor, except for the s 8(3) exceptions (the Commonwealth's AAEC successors, such as ANSTO); s 9: other Acts do not authorise a state authority to build or approve one [TO VERIFY] | NSW repeal, or a Commonwealth override under Constitution s 109 [TODO: add the Constitution to sources.md], which may face a High Court challenge (Canberra Times, 2025) [TO VERIFY] | NSW Parliament (Legislative Assembly), or the Commonwealth | Repeal bill passed the Legislative Council; stalled in the Assembly (B1.3) |
| (4) | Site (not a law) | AGL owns Liddell and has ruled out nuclear there (Newcastle Herald, 2024) [TO VERIFY] | AGL's consent, or compulsory acquisition by the Commonwealth | AGL, or the Commonwealth | AGL opposed |

Order of removal: federal repeal (1 and 2) → choice of regulator → state repeal or override (3) → site (4) → environmental assessment → licensing (law brief §4). Each step has a different veto holder, so all must agree.

#### B1.2 Senate arithmetic for federal repeal

*Table B2. Senate composition used for the repeal arithmetic.*
*Source: Parliament of Australia (2026) [TO VERIFY; composition as at 14 May 2026]; `parameters_run2.yaml`.*

| Party or group | Seats | Position on repeal | Source of position |
|---|---:|---|---|
| Australian Labor Party | 30 | Opposed | Bowen (2025) [TO VERIFY date; no 2026 statement found] |
| Coalition | 27 | For | Liberal Party of Australia (2026); ABC News (2026) [TO VERIFY] |
| Australian Greens | 10 | Opposed | Australian Greens (2025) [TO VERIFY] |
| One Nation | 4 | Assumed for | **Assumption** [TODO: source needed: ABC, 31 August 2026, is in the law brief but not in sources.md] |
| Senator Babet | 1 | Assumed for | **Assumption** (no source) |
| Lambie, Payman, Pocock, Thorpe | 4 (1 each) | Not assumed | — |
| **Total** | **76** | | Script asserts the parts sum to 76 |

Steps (`law_timelines.py`):

| Step | Working | Result |
|---|---|---|
| 1. Majority needed, all 76 voting | ⌊76 / 2⌋ + 1 (a tied vote fails, Constitution s 23 [TO VERIFY wording]) | **39** |
| 2. Largest pro-repeal bloc (upper bound) | Coalition 27 + One Nation 4 + Babet 1 | **32** |
| 3. Shortfall | 39 − 32 | **7** |
| 4. Bloc plus every other crossbencher | 32 + 4 | **36** (still 3 short) |
| 5. Can repeal pass without Labor or the Greens? | 36 ≥ 39? | **No** |
| 6. Would the Greens alone be enough (arithmetic only)? | 32 + 10 = 42 ≥ 39? | Yes, but the Greens oppose (policy, not arithmetic) |
| 7. Opposed bloc | Labor 30 + Greens 10 = 40 ≥ 39 | A blocking majority on its own |

Result 4 makes the conclusion independent of the One Nation and Babet assumption. In the House, Labor holds 94 of 150 seats (Australian Electoral Commission, 2025) [TO VERIFY], so a repeal bill would also need the Government's support there.

#### B1.3 NSW repeal bill status

*Table B3. Progress of the NSW repeal bill (private member's bill).*
*Source: Parliament of New South Wales (2025–26; 2026) [TO VERIFY]; `parameters_run2.yaml`.*

| Event | Date | Note |
|---|---|---|
| Introduced in the Legislative Council | 19 November 2025 | — |
| Passed the Legislative Council | 6 May 2026 | About 5.5 months after introduction (law brief §4). All Liberal and National MLCs voted for it [TO VERIFY] |
| Legislative Assembly | Awaiting the second reading speech (notice paper reported 27 May 2026) | The Minns Labor Government opposes repeal and holds an Assembly majority [TO VERIFY; Minns quote is secondary, Canberra Times (n.d.)] |
| Lapses | 28 November 2026 | Unless the Assembly acts first [TO VERIFY against the latest notice paper] |

#### B1.4 Licensing timelines: Darlington (Canada)

*Table B4. CNSC licensing milestones for the Darlington New Nuclear Project.*
*Source: Canadian Nuclear Safety Commission [CNSC] (2021; 2025; 2026a; 2026b) [TO VERIFY]; `parameters_run2.yaml`.*

| Milestone | Date | Parameter key |
|---|---|---|
| Environmental assessment begins (joint review panel) | May 2007 (taken as 1 May) | `dnnp_ea_start` |
| Licence to prepare site issued | 17 August 2012 | `dnnp_lpts_issued` |
| Site licence renewed, valid to 11 October 2031 | 12 October 2021 | `dnnp_lpts_renewed` |
| Licence-to-construct application (one unit, in packages) | October 2022 (taken as 31 October) | `dnnp_ltc_application` |
| Hearing part 2 begins (Ajax) | 8 January 2025 | `dnnp_ltc_hearing_part2_start` |
| Licence to construct issued (PRCL 32.00/2035, one BWRX-300) | 4 April 2025 | `dnnp_ltc_decision` |
| Regulatory hold point 1 lifted (reactor building foundation) | 30 March 2026 | `dnnp_rhp1_lifted` |
| Licence to construct expires | 31 March 2035 | `dnnp_ltc_expiry` |

Method: months = days between two dates ÷ (365.25 / 12); years = months ÷ 12.

*Table B5. Licensing durations calculated from Table B4.*
*Source: `03_LCA_Calculations/results/law_timelines.csv`.*

| Quantity | Dates used | Result |
|---|---|---|
| Application to licence to construct | 31 Oct 2022 → 4 Apr 2025 (886 days) | **29.1 months** (2.43 years) |
| Sensitivity: application day unknown within October | 1 Oct 2022 → 4 Apr 2025 | 29.1–30.1 months |
| Against CNSC's expected review time (32 months, REGDOC-3.5.1 (CNSC, [year TO VERIFY]); extract ambiguous, another row reads 24 months) | 29.1 − 32 | −2.9 months (faster) [TO VERIFY benchmark] |
| Hearing part 2 to decision | 8 Jan 2025 → 4 Apr 2025 | 2.8 months |
| Environmental assessment start to licence to construct | May 2007 → 4 Apr 2025 | **17.9 years** (elapsed, not continuous review) |
| Licence validity from issue | 4 Apr 2025 → 31 Mar 2035 | 10.0 years |
| Licence validity remaining at the report date | 20 Oct 2026 → 31 Mar 2035 | 8.4 years |
| Licence to construct to RHP-1 lifted | 4 Apr 2025 → 30 Mar 2026 | 11.8 months |

The licence covers one unit. Units 2–4 need a further Commission authorisation, with approval to proceed reported as expected in 2028 (American Nuclear Society, 2026) [TO VERIFY; secondary, and the type of approval is not stated]. No source gives the Units 2–4 review time.

Australian comparator: the naval nuclear regulator (ANNPSR) began operating on 1 November 2025 under a 2024 Act (Minister for Defence, 2025) [TO VERIFY], about two years after its Act for a narrower scope [TODO: bill introduction date from Bills Digest No. 32, 2023–24, to give an exact interval].

---

### B2. Supply concentration: Herfindahl–Hirschman index (HHI) working

**Result.** On the 2023 US merger guidelines, mining by country (2,341), conversion (2,111) and enrichment (3,009) are all "highly concentrated". On the superseded 2010 guidelines only enrichment is; mining and conversion are "moderately concentrated". Removing Russia raises the HHI at every stage. Removing Russia and China leaves enrichment as a Urenco–Orano duopoly (5,621). The one case below 1,800 is mining by company (1,118), so mining concentration is a country (geopolitical) risk rather than a market-power risk.

#### B2.1 Method

1. Share of supplier *i*: s*ᵢ* = 100 × q*ᵢ* / Σq (per cent), where q is output or capacity.
2. HHI = Σ s*ᵢ*² (range 0 to 10,000; one supplier = 10,000).
3. Equivalent number of equal-sized suppliers: N_eq = 10,000 / HHI.
4. Measures: mining by country (2024 mine output, tU); conversion by company (licensed capacity, tU as UF₆ per year; production as a check); enrichment by company (capacity, thousand SWU per year; 2025 base, 2022 and 2030 as sensitivity).
5. "Without Russia": Russian supply removed and the remaining shares renormalised, with no new capacity (the market open to a buyer barred from Russian material). "Without Russia and China" also removes CNNC, whose capacity WNA estimates on the assumption that it serves China's own fleet; this approximates the market open to a Canadian or Australian utility.
6. "Others" or residual rows are bounded: one supplier (upper bound) or many small suppliers (lower bound, about 0). The difference is below 3 HHI points in every 2024/2025 case.
7. Shares are squared before rounding, so squaring a rounded share in the tables can differ by less than 1 point.

*Table B6. HHI thresholds used as a scale.*
*Source: US Department of Justice and Federal Trade Commission (2023; 2010) [TO VERIFY wording].*

| Guideline | Unconcentrated | Moderately concentrated | Highly concentrated | Status |
|---|---|---|---|---|
| *Merger Guidelines* (2023), §2.1 | — | — | HHI > 1,800 [TO VERIFY: "greater than" or "1,800 or greater"] | Current |
| *Horizontal Merger Guidelines* (2010), §5.3 | < 1,500 | 1,500–2,500 | > 2,500 | Superseded; reported because mining and conversion fall between the two thresholds |

These are antitrust screens for merger review. Here they are used as a recognised scale for supply concentration, not as a legal test.

**Worked example (enrichment, 2025).**
1. Rosatom's share = 100 × 29,133 / 68,077 = 42.79%; squared = 1,831.3.
2. Repeat for Urenco, CNNC, Orano and Other; sum = 1,831.3 + 645.8 + 410.3 + 121.4 + 0.3 = **3,009**. N_eq = 10,000 / 3,009 = 3.3.
3. Without Russia: total = 68,077 − 29,133 = 38,944 kSWU. Urenco's share = 100 × 17,300 / 38,944 = 44.42%; and so on. HHI = **3,599**.
4. Without Russia and China: total = 38,944 − 13,789 = 25,155 kSWU. Urenco 68.77%, Orano 29.82%, Other 1.41%. HHI = **5,621** (N_eq = 1.8).

#### B2.2 Inputs and shares

*Table B7. Uranium mine output by country, 2024.*
*Source: World Nuclear Association (2026) [TO VERIFY year and every row; several rows are WNA estimates]; calculated in `hhi.py` (`results/hhi.md` §3.1–3.2). Internal check: the rows sum exactly to 60,213 tU.*

| Country | tU | Share (%) | Share² | Share without Russia (%) | Share² |
|---|---:|---:|---:|---:|---:|
| Kazakhstan | 23,270 | 38.65 | 1,493.5 | 40.49 | 1,639.2 |
| Canada | 14,309 | 23.76 | 564.7 | 24.90 | 619.8 |
| Namibia | 7,333 | 12.18 | 148.3 | 12.76 | 162.8 |
| Australia | 4,598 | 7.64 | 58.3 | 8.00 | 64.0 |
| Uzbekistan | 4,000 | 6.64 | 44.1 | 6.96 | 48.4 |
| Russia | 2,738 | 4.55 | 20.7 | — | — |
| China | 1,600 | 2.66 | 7.1 | 2.78 | 7.7 |
| Niger | 962 | 1.60 | 2.6 | 1.67 | 2.8 |
| India | 500 | 0.83 | 0.7 | 0.87 | 0.8 |
| Ukraine | 288 | 0.48 | 0.2 | 0.50 | 0.3 |
| USA | 260 | 0.43 | 0.2 | 0.45 | 0.2 |
| South Africa | 200 | 0.33 | 0.1 | 0.35 | 0.1 |
| Others | 155 | 0.26 | 0.1 | 0.27 | 0.1 |
| **Total (tU) / HHI** | **60,213** (57,475 without Russia) | 100.00 | **2,341** | 100.00 | **2,546** |

Without Russia and China, the mining HHI is 2,686 (`hhi_summary.csv`; `hhi.py` does not print the share table for this case).

*Table B8. Mining by country, earlier years (only the eight largest rows retrieved; residual bounded).*
*Source: World Nuclear Association (2026) [TO VERIFY]; `results/hhi.md` §3.3.*

| Year | Residual (tU) | HHI lower bound | HHI upper bound | Russia's share (%) |
|---|---:|---:|---:|---:|
| 2022 | 1,083 | 2,368 | 2,372 | 5.1 |
| 2023 | 1,204 | 2,243 | 2,248 | 5.0 |

*Table B9. Conversion by company, licensed capacity (tU as UF₆ per year).*
*Source: World Nuclear Association (2024) [TO VERIFY year and rows; CNNC and Rosatom are WNA estimates]; `results/hhi.md` §3.5.*

| Company (country) | tU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| CNNC (China) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | — | — |
| Orano (France) | 15,000 | 24.19 | 585.3 | 30.30 | 918.3 | 43.48 | 1,890.4 |
| Cameco (Canada) | 12,500 | 20.16 | 406.5 | 25.25 | 637.7 | 36.23 | 1,312.7 |
| Rosatom (Russia) | 12,500 | 20.16 | 406.5 | — | — | — | — |
| ConverDyn (USA) | 7,000 | 11.29 | 127.5 | 14.14 | 200.0 | 20.29 | 411.7 |
| **Market total (tU/yr) / HHI** | **62,000** | 100.00 | **2,111** | 49,500 | **2,674** | 34,500 | **3,615** |

*Table B10. Enrichment by company, 2025 capacity (thousand SWU per year).*
*Source: World Nuclear Association (2025) [TO VERIFY year and rows; CNNC is a WNA estimate; 2030 figures are plans]; `results/hhi.md` §3.6.*

| Company | kSWU/yr | Share (%) | Share² | Without Russia (%) | Share² | Without Russia and China (%) | Share² |
|---|---:|---:|---:|---:|---:|---:|---:|
| Rosatom | 29,133 | 42.79 | 1,831.3 | — | — | — | — |
| Urenco | 17,300 | 25.41 | 645.8 | 44.42 | 1,973.4 | 68.77 | 4,729.8 |
| CNNC | 13,789 | 20.26 | 410.3 | 35.41 | 1,253.7 | — | — |
| Orano | 7,500 | 11.02 | 121.4 | 19.26 | 370.9 | 29.82 | 888.9 |
| Other (INB, JNFL) | 355 | 0.52 | 0.3 | 0.91 | 0.8 | 1.41 | 2.0 |
| **Market total (kSWU/yr) / HHI** | **68,077** | 100.00 | **3,009** | 38,944 | **3,599** | 25,155 | **5,621** |

Russia's enrichment share is 43.3% in 2022 and 38.3% in the 2030 plans (World Nuclear Association, 2025) [TO VERIFY]. [TODO: analyst. Add the CRAI (2025) Rosatom and CNNC capacities to `hhi.py` and `sources.md`, and report Russia's share as a range (review.md §8.3 point 2; R1.3).]

#### B2.3 Headline results

*Table B11. HHI of the uranium front end by stage, with and without Russia and China.*
*Source: `03_LCA_Calculations/results/hhi.md` §2 and `hhi_summary.csv`, from the inputs in Tables B7–B10 [all TO VERIFY].*

| Stage (measure, base year) | HHI | N_eq | 2023 class | 2010 class | Without Russia | Without Russia and China | Russia's share |
|---|---:|---:|---|---|---:|---:|---:|
| Mining (output by country, 2024) | 2,341 | 4.3 | Highly | Moderately | 2,546 (highly under both) | 2,686 | 4.5% |
| Conversion (capacity by company, [year TO VERIFY]) | 2,111 | 4.7 | Highly | Moderately | 2,674 (highly under both) | 3,615 | 20.2% |
| Enrichment (capacity by company, 2025) | **3,009** | 3.3 | Highly | Highly | 3,599 | **5,621** | **42.8%** |

Shares for the two producer countries in the comparison: Canada mined 23.8% of world uranium in 2024 and holds 20.2% of world conversion capacity (36.2% of the capacity open to a Western buyer), with no enrichment. Australia mined 7.6% (4,598 tU) and has no conversion or enrichment capacity. Australia holds 28% of identified recoverable resources at < USD 130/kgU (OECD NEA and IAEA, 2025) [TO VERIFY; Red Book 2026 gives 29% or 27% in two WNA tabulations; team to choose the edition, §8.3 TODO 4].

#### B2.4 Sensitivity

*Table B12. HHI under every tested scenario.*
*Source: `03_LCA_Calculations/results/hhi_summary.csv` [inputs TO VERIFY].*

| Stage | Scenario | HHI | N_eq | 2023 class | 2010 class | Note |
|---|---|---:|---:|---|---|---|
| Mining (country) | 2024 base | 2,341 | 4.3 | Highly | Moderately | |
| Mining (country) | 2024 base, "Others" atomistic | 2,341 | 4.3 | Highly | Moderately | Lower bound |
| Mining (country) | 2024 without Russia | 2,546 | 3.9 | Highly | Highly | |
| Mining (country) | 2024 without Russia and China | 2,686 | 3.7 | Highly | Highly | |
| Mining (country) | 2024 without Russia, China and Niger | 2,778 | 3.6 | Highly | Highly | Niger: exports disrupted since the 2023 coup (secondary) [TO VERIFY] |
| Mining (country) | 2022 (residual bounds) | 2,370 | 4.2 | Highly | Moderately | Range 2,368–2,372 |
| Mining (country) | 2022 without Russia | 2,601 | 3.8 | Highly | Highly | Range 2,598–2,603 |
| Mining (country) | 2023 (residual bounds) | 2,246 | 4.5 | Highly | Moderately | Range 2,243–2,248 |
| Mining (country) | 2023 without Russia | 2,460 | 4.1 | Highly | Moderately | Range 2,457–2,462 |
| **Mining (company)** | **2024 bounds (top three known)** | **1,118** | **8.9** | **Not highly** | **Unconcentrated** | **Range 851–1,384; partial data** |
| Conversion | Capacity base | 2,111 | 4.7 | Highly | Moderately | |
| Conversion | Capacity without Russia | 2,674 | 3.7 | Highly | Highly | |
| Conversion | Capacity without Russia and China | 3,615 | 2.8 | Highly | Highly | Market open to a Western buyer |
| Conversion | Production base | 2,109 | 4.7 | Highly | Moderately | |
| Conversion | Production without Russia | 2,672 | 3.7 | Highly | Highly | |
| Conversion | ConverDyn 15,000 tU (alternative) | 2,015 | 5.0 | Highly | Moderately | Secondary source; sensitivity only |
| Conversion | ConverDyn alternative, without Russia | 2,514 | 4.0 | Highly | Highly | |
| Conversion | ConverDyn alternative, without Russia and China | 3,356 | 3.0 | Highly | Highly | |
| Enrichment | 2022 capacity | 3,065 | 3.3 | Highly | Highly | |
| Enrichment | 2022 without Russia | 3,707 | 2.7 | Highly | Highly | |
| Enrichment | 2022 without Russia and China | 5,722 | 1.7 | Highly | Highly | Market open to a Western buyer |
| Enrichment | 2025 capacity (base) | 3,009 | 3.3 | Highly | Highly | |
| Enrichment | 2025 without Russia | 3,599 | 2.8 | Highly | Highly | |
| Enrichment | 2025 without Russia and China | 5,621 | 1.8 | Highly | Highly | Market open to a Western buyer |
| Enrichment | 2030 capacity (plans) | 2,724 | 3.7 | Highly | Highly | |
| Enrichment | 2030 without Russia | 3,299 | 3.0 | Highly | Highly | |
| Enrichment | 2030 without Russia and China | 4,827 | 2.1 | Highly | Highly | Market open to a Western buyer |

Reading:
- **Data year** moves the HHI by a few hundred points but never changes the 2023 class. Enrichment and conversion are highly concentrated in every year tested.
- **Capacity versus production** (conversion) changes the HHI by less than 10 points.
- **ConverDyn's capacity** (7,000 or 15,000 tU) is the largest data uncertainty for conversion. The higher value lowers the HHI to 2,015, still above 1,800.
- **Threshold choice** matters for mining and conversion only: both are "highly" concentrated on the 2023 scale and "moderately" on the 2010 scale. Enrichment is highly concentrated on both.
- **Removing Russia** is the dominant effect at every stage, and it always increases concentration.

**Mining by company (the one case below 1,800).** Only the top three 2024 shares were retrieved: Kazatomprom 21%, Cameco 17%, Orano 11% (World Nuclear Association, 2026) [TO VERIFY company-table year]; Kazatomprom's 21% is cross-checked by Kazatomprom (2025) [TO VERIFY]. Together they hold 49%.
1. Lower bound (the other 51% held by many small firms): 21² + 17² + 11² = 441 + 289 + 121 = **851**.
2. Upper bound (the other 51% split into firms no larger than the third-ranked, 11%, i.e. four at 11% and one at 7%): 851 + 4 × 11² + 7² = 851 + 484 + 49 = **1,384**.
3. Central value reported by `hhi.py`: the midpoint, (851 + 1,384) / 2 = **1,118** (N_eq = 8.9).

Both bounds are below 1,500, so firms are not concentrated even though countries are. Kazakhstan's 38.6% country share includes joint ventures with Cameco, Orano, Uranium One (Rosatom) and Chinese partners [TO VERIFY ownership detail].

#### B2.5 Limitations

- Capacity is not supply. Nameplate SWU includes capacity Rosatom uses for underfeeding and tails re-enrichment, and CNNC's figures are WNA estimates.
- Secondary supply (inventories, down-blending, re-enriched tails) is excluded. Mine output in 2024 (60,213 tU) met about 93% of reactor requirements (64,500 tU at 1 January 2025; OECD NEA and IAEA, 2026) [TO VERIFY].
- Company-level enrichment shares hide plant location: Urenco operates in the UK, Germany, the Netherlands and the USA; Orano only in France.
- Mining by country ignores ownership (for example, Rosatom's Uranium One stakes in Kazakh mines) and the transport routes for Kazakh exports [TO VERIFY]. The company-level bound only partly addresses ownership.
- Fuel fabrication was not assessed.
- The HHI is a world-market measure. It is not yet sized to Darlington's own fuel demand [TODO: Leroy/analyst. BWRX-300 core loading, reload fraction, cycle length and enrichment, to give SWU/yr for four units; §8.3 TODO 6].

---

### B3. Routes to a licensable SMR in Australia: scored comparison

**Result.** The ranking depends on the weights: route C (cooperative state repeal) ranks first on equal weights and when durability is valued more; route A (Commonwealth-owned plant) ranks first when regulator readiness is valued more. Under the 2026 Senate (B1.2), none of the three routes is open. **These scores are our own qualitative judgement from the evidence in B1, not sourced scores.** They feed the "feasibility" criterion of the §9 MCDA.

*Table B13. Three routes scored against four non-technical objectives (1 = poor, 3 = good).*
*Source: our qualitative judgement (law brief §5), from the evidence cited in the table.*

| Objective | A. Commonwealth-owned plant under ARPANSA (the Coalition's 2024 model) | B. Federal licensing law for private operators, overriding the states | C. Cooperative: state repeal plus a state or joint regulator |
|---|---|---|---|
| Legal changes needed (not scored) | EPBC and ARPANS repeal, plus a s 109 override of NSW (or NSW repeal) | EPBC and ARPANS repeal, a new federal Act and a s 109 override | EPBC and ARPANS repeal, NSW repeal and a NSW regulator Act |
| Fewest veto points | **2**: Senate; site owner | **1**: Senate; High Court; site owner | **1**: Senate; NSW Parliament; site owner |
| Regulator readiness | **3**: builds on ARPANSA, which already regulates Commonwealth entities such as ANSTO (ARPANSA, n.d.) [TO VERIFY] | **2**: a new body, as with the ANNPSR (Minister for Defence, 2025) [TO VERIFY] | **1**: NSW has no nuclear regulator |
| Durability (low exposure to political reversal) | **1**: one government's decision; the next can sell or cancel | **1**: as A, plus litigation risk (Canberra Times, 2025) [TO VERIFY] | **3**: both levels of government committed |
| Social licence | **1**: states rejected it in 2024 [TODO: source needed; Canberra Times (n.d.) on Minns is a secondary lead] | **1**: overrides the states | **3**: the states consent, if they do |
| **Total (of 12)** | **7** | **5** | **8** |

Route A's description currently rests on ABC News (2024), a weak secondary source [TODO: replace with the Coalition's 19 June 2024 release, factcheck A8].

*Table B14. Weight test: totals when one objective counts double (maximum 15).*
*Source: calculated from Table B13 (law brief §5).*

| Weighting | A | B | C | Ranking |
|---|---:|---:|---:|---|
| Equal weights (base, of 12) | 7 | 5 | 8 | C, A, B |
| Regulator readiness × 2 | 7 + 3 = **10** | 5 + 2 = 7 | 8 + 1 = 9 | A, C, B |
| Durability × 2 | 7 + 1 = 8 | 5 + 1 = 6 | 8 + 3 = **11** | C, A, B |

Reading: route B ranks last under all three weightings tested. The choice between A and C is a choice between speed (an existing regulator) and durability (both levels of government committed). That is a political judgement, not a technical one. Whichever route is assumed, an Australian SMR scores lowest on time to first power in the §9 MCDA.

---

### B4. Displacement: CO₂e avoided by one BWRX-300, Darlington vs Liddell

**Result.** At static grid factors, one unit avoids 1.50 Mt CO₂e a year on the NSW grid average. That is 9.1× what it avoids on Ontario's 2024 average (0.165 Mt), but only 1.9× its avoidance on Ontario's marginal factor (0.80 Mt). Valued over the years each plant could actually run, the gap mostly closes:
- Darlington Unit 1 from 2030 avoids **1.01–6.80 Mt to 2050**.
- Liddell from 2040 avoids **0.67–3.85 Mt to 2050**: less than Darlington on the Step Change proxy, and comparable on the slow transition.
- Liddell wins clearly only if the NEM stops decarbonising (frozen grid, 16.54 Mt).

The grid trajectory, the start year and the post-coal floor dominate the result. The SMR's own life-cycle value moves it by a few per cent. Script: `python3 -I 03_LCA_Calculations/scripts/displacement.py`, with inputs in `parameters_run1.yaml` and output in `results/displacement.md`.

#### B4.1 Method

1. Annual output of one unit: E = P × 8,760 h × CF = 300 MW × 1,000 kW/MW × 8,760 h × 0.90 = **2,365,200,000 kWh (2.365 TWh) a year**.
2. CO₂e avoided in year *y*: A(*y*) = E × (EF_grid(*y*) − EF_SMR) / 10⁶ t. EF is in g CO₂e/kWh, and EF_SMR = 4.2 g/kWh (our Monte Carlo median, §6; 90% interval 3.0–5.8).
3. The cumulative total is the sum of A(*y*) from the first full year of operation to 2035, to 2050 (inclusive), or to the end of a 60-year life.
4. Each grid trajectory is linear between its anchor points and flat afterwards. These are our constructions, not AEMO or IESO series:

| Case | Path | Role |
|---|---|---|
| ON-avg-traj | 73.8 g/kWh (2024) → 15 (2040) | Ontario average |
| ON-marginal-declining | 343 (2024) → 15 (2050) | Ontario marginal; assumes gas leaves the margin by 2050 |
| ON-avg-flat, ON-marginal-flat | 2024 values held | Upper bounds |
| NEM-T1 (Step Change proxy) | 640 (2025) → 30 floor (2038) | Central NEM case |
| NEM-T2 (slow) | 640 (2025) → 30 (2050) | Slow transition |
| NEM-T0 (frozen) | 640 held | Upper bound |
| UB-Bayswater; UB-coal-LCA | 990; 1,000 held | Coal upper bounds |

**Worked example 1 (static, NSW 2025).** 2,365,200,000 × (640 − 4.2) / 10⁶ = **1,503,794 t a year**.

**Worked example 2 (cumulative, Liddell from 2040 on NEM-T1).** The NEM is at its 30 g/kWh floor from 2038, so each year avoids 2,365,200,000 × (30 − 4.2) / 10⁶ = 61,022 t.
- To 2050 (11 years, 2040–2050): 11 × 61,022 = **671 kt**.
- Whole life (60 years): 60 × 61,022 = **3.66 Mt**.

*Table B15. Inputs to B4–B6.*
*Source: `03_LCA_Calculations/parameters_run1.yaml` and the references named; status as in the YAML.*

| Input | Central (range) | Source | Status |
|---|---|---|---|
| Net output | 300 MWe (290–300) | Assumption (the deck's value; an OEB filing may give 315) | Placeholder |
| Capacity factor; design life | 0.90 (0.80–0.95); 60 years (40–80) | Assumption | Placeholder |
| SMR life cycle | 4.2 g/kWh (3.0–5.8) | This study (§6, Appendix C) | From results; inputs TO VERIFY |
| Ontario average, 2024 | 73.8 g/kWh (73–73.8) | The Atmospheric Fund (2025) | TO VERIFY |
| Ontario average, 2022; 2023 | 35; 53 g/kWh | Canada Energy Regulator (n.d.); Government of Ontario (n.d.) | TO VERIFY |
| Ontario average, 2040 | 15 g/kWh | Independent Electricity System Operator (2024) | TO VERIFY |
| Ontario marginal, 2024 | 343 g/kWh (343–472) | The Atmospheric Fund (2025); high = gas generation, The Atmospheric Fund (2021) | TO VERIFY (definition ambiguous) |
| Year gas leaves Ontario's margin | 2050 (2040–2060) | Assumption | Assumption |
| NSW/ACT grid, 2025 (scope 2) | 640 g/kWh | Department of Climate Change, Energy, the Environment and Water (2025) | TO VERIFY |
| NEM coal exit (T1); slow exit (T2) | 2038; 2050 | Australian Energy Market Operator (2024); assumption | TO VERIFY (secondary); assumption |
| NEM floor after coal | 30 g/kWh (0–80) | Assumption | Assumption |
| Bayswater, sent out | 990 g/kWh | Australian Energy Market Operator (2025) | TO VERIFY (old value) |
| Coal, life cycle | 1,000 g/kWh (751–1,095) | United Nations Economic Commission for Europe (2021) | TO VERIFY |
| Start years | Darlington Unit 1 2030; Units 2–4 2035 (2034–2036); Liddell 2035 (Coalition claim), 2040 (CSIRO earliest), 2045 (late case) | Government of Ontario (2025); Ontario Power Generation (2025); ABC News (2024); Graham, Hayward and Foster (2024); assumption | Placeholders (Leroy) |

#### B4.2 Results

*Table B16. Annual CO₂e avoided by one unit at static grid factors.*
*Source: `results/displacement.md` §2 [inputs TO VERIFY].*

| Displaced electricity | EF (g/kWh) | Avoided (t a year) | Ratio to Ontario average 2024 |
|---|---:|---:|---:|
| Ontario average 2022 (CER) | 35 | 72,848 | 0.4× |
| Ontario average 2023 (energy snapshot; the deck's value) | 53 | 115,422 | 0.7× |
| Ontario average 2024 (TAF) | 74 | 164,618 | 1.0× |
| Ontario marginal (TAF 2024) | 343 | 801,330 | 4.9× |
| Ontario gas-fired generation (TAF 2021) | 472 | 1,106,441 | 6.7× |
| NSW/NEM average 2025 (NGA Factors, scope 2) | 640 | 1,503,794 | 9.1× |
| Bayswater coal, sent out | 990 | 2,331,614 | 14.2× |
| Coal, life cycle (UNECE) | 1,000 | 2,355,266 | 14.3× |
| Gas combined cycle, life cycle (UNECE) | 458 | 1,073,328 | 6.5× |

*Table B17. Cumulative CO₂e avoided by one unit, by site, start year and grid trajectory (Figure F6 data).*
*Source: `results/displacement.md` §3 [inputs TO VERIFY].*

| Site | Start | Grid case | Year-1 EF (g/kWh) | To 2035 | To 2050 | Whole life |
|---|---|---|---:|---:|---:|---:|
| Darlington Unit 1 | 2030 | ON-avg-traj | 52 | 544 kt | 1.01 Mt | 2.01 Mt |
| Darlington Unit 1 | 2030 | ON-avg-flat | 74 | 988 kt | 3.46 Mt | 9.88 Mt |
| Darlington Unit 1 | 2030 | ON-marginal-declining | 267 | 3.29 Mt | 6.80 Mt | 7.80 Mt |
| Darlington Unit 1 | 2030 | ON-marginal-flat (upper bound) | 343 | 4.81 Mt | 16.83 Mt | 48.08 Mt |
| Liddell | 2035 | NEM-T0 frozen (upper bound) | 640 | 1.50 Mt | 24.06 Mt | 90.23 Mt |
| Liddell | 2035 | NEM-T1 Step Change proxy | 171 | 394 kt | 1.64 Mt | 4.33 Mt |
| Liddell | 2035 | NEM-T2 slow | 396 | 927 kt | 7.90 Mt | 10.59 Mt |
| Liddell | 2040 | NEM-T0 frozen (upper bound) | 640 | 0 | 16.54 Mt | 90.23 Mt |
| Liddell | 2040 | NEM-T1 Step Change proxy | 30 | 0 | 671 kt | 3.66 Mt |
| Liddell | 2040 | NEM-T2 slow | 274 | 0 | 3.85 Mt | 6.84 Mt |
| Liddell | 2045 | NEM-T0 frozen (upper bound) | 640 | 0 | 9.02 Mt | 90.23 Mt |
| Liddell | 2045 | NEM-T1 Step Change proxy | 30 | 0 | 366 kt | 3.66 Mt |
| Liddell | 2045 | NEM-T2 slow | 152 | 0 | 1.23 Mt | 4.53 Mt |
| Liddell | 2040 | UB-Bayswater flat (upper bound) | 990 | 0 | 25.65 Mt | 139.90 Mt |
| Liddell | 2040 | UB-coal-LCA flat (upper bound) | 1,000 | 0 | 25.91 Mt | 141.32 Mt |

*Table B18. All four Darlington units (Unit 1 from 2030; Units 2–4 from 2035).*
*Source: `results/displacement.md` §4 [inputs TO VERIFY].*

| Grid case | To 2035 | To 2050 | Whole life |
|---|---:|---:|---:|
| ON-avg-traj | 751 kt | 2.63 Mt | 7.00 Mt |
| ON-avg-flat | 1.48 Mt | 11.36 Mt | 39.51 Mt |
| ON-marginal-declining | 4.71 Mt | 18.77 Mt | 23.14 Mt |
| ON-marginal-flat (upper bound) | 7.21 Mt | 55.29 Mt | 192.32 Mt |

*Table B19. One-at-a-time sensitivity, Liddell central case (start 2040, NEM-T1). Central: 671 kt to 2050; 3.66 Mt over the whole life.*
*Source: `results/displacement.md` §5 [inputs TO VERIFY].*

| Parameter | Range | To 2050 (low → high input) | Whole life (low → high input) |
|---|---|---|---|
| Capacity factor | 0.80–0.95 | 597 → 709 kt | 3.25 → 3.86 Mt |
| Net output | 290–300 MWe | 649 → 671 kt | 3.54 → 3.66 Mt |
| SMR life cycle (our 95th → 5th percentile) | 5.8–3.0 g/kWh | 630 → 702 kt | 3.43 → 3.83 Mt |
| SMR life cycle, UNECE midpoint instead of ours | 5.75 vs 4.2 g/kWh | 631 → 671 kt | 3.44 → 3.66 Mt |
| SMR life cycle, stress (IPCC lead, unconfirmed) | 110–12 g/kWh | −2.08 Mt → 468 kt | −11.35 → 2.55 Mt |
| NEM floor after coal exit | 0–80 g/kWh | −109 kt → 1.97 Mt | −596 kt → 10.76 Mt |
| Coal exit year (T1) | 2035–2045 | 671 kt → 1.75 Mt | 3.66 → 4.74 Mt |
| Design life | 40–80 years | 671 → 671 kt | 2.44 → 4.88 Mt |
| Start year | 2035–2045 | 1.64 Mt → 366 kt | 4.33 → 3.66 Mt |
| Grid trajectory | T1 → T0 (frozen) | 671 kt → 16.54 Mt | 3.66 → 90.23 Mt |

Reading:
- **Order-of-magnitude drivers.** The grid trajectory, the start year and the post-coal floor each move the result by an order of magnitude. Under T1 the SMR spends its whole life displacing the residual mix, so the floor is in effect the displaced intensity.
- **Minor drivers.** Capacity factor, net output and our life-cycle interval move it by a few per cent.
- **When the SMR's own value matters.** Only in the 110 g/kWh stress case, or on a near-zero floor, where the result turns negative.

#### B4.3 Limitations
1. **Boundary mismatch.** The grid factors (NGA scope 2, TAF, CER) count combustion at the power station only, while the SMR value is life cycle, so displacement is slightly understated. The UNECE coal row gives the boundary-consistent upper bound.
2. **Average vs marginal.** A new baseload unit displaces what is on the margin when it runs. In Ontario that is mostly gas, so the marginal factor is the better short-run estimate. Over a 60-year life the margin decarbonises, which makes the flat-marginal case an upper bound.
3. **Counterfactual.** In both grids the real alternative is other new supply, not today's grid forever (B6).
4. **Liddell closed in April 2023** (Australian Energy Regulator, 2021) [TO VERIFY closure date]. An SMR on the site displaces the NEM mix, so Bayswater is an upper bound only, and Bayswater's own closure date is [TODO: AGL].
5. **Placeholders.** Net output, capacity factor, design life and start years await Leroy's sourced data. 315 MWe is not yet in the sensitivity [TODO].

---

### B5. Value of schedule: the CO₂e and dollar cost of delay, and C1's break-even

**Result.** On Ontario's average factor, C1's per-unit saving (1,734 t) is cancelled by **9.2–14.6 days** of delay to that unit (gross–net). On the marginal factor it is cancelled by **1.3–1.4 days**. Even all of Units 2–4's saving (5,201 t) is cancelled by 28–44 days (average) or 4.0–4.2 days (marginal) of delay to a single unit. In money, a one-month slip of Units 2–4 costs **30–223 times** C1's carbon value. Script: `python3 -I 03_LCA_Calculations/scripts/schedule_value.py`, with output in `results/schedule_value.md`. The carrying-cost and deferred-output inputs are read from `parameters_run5.yaml`.

#### B5.1 Method

1. Output of one unit: monthly M = E / 12 = 197,100,000 kWh; daily D = E / 365 = 6,480,000 kWh.
2. **Gross loss** per month of delay = M × (EF_grid(start) − EF_SMR) / 10⁶ t. This is the displacement that does not happen while the plant is late, and it matches carbon budgets to 2035 or 2050.
3. **Net loss** per month = M × (EF_grid(start) − EF_grid(start + life)) / 10⁶ t. A late plant still runs its full life, so the lost month returns at the end of life, on a cleaner grid. On a flat grid this gives zero by construction, which is an artefact of assuming the grid never changes.
4. **Break-even delay** for a saving S (t CO₂e) = S / (loss per day), on both bases.

**Worked example (one of Units 2–4, start 2035, ON-avg-traj).**
1. Grid factor in 2035: EF(2035) = 73.8 − (73.8 − 15) × 11/16 = 33.4 g/kWh.
2. Gross loss: 6,480,000 × (33.4 − 4.2) / 10⁶ = **189 t a day**, so the break-even is 1,734 / 189 = **9.2 days**.
3. Net loss: 6,480,000 × (33.4 − 15) / 10⁶ = **119 t a day**, so the break-even is 1,734 / 119 = **14.6 days**.

**Marginal case.** EF(2035) = 343 − (343 − 15) × 11/26 = 204.2 g/kWh. The gross loss is 6,480,000 × 200.0 / 10⁶ = 1,296 t a day, so the break-even is 1,734 / 1,296 = **1.3 days**.

#### B5.2 CO₂e lost per month of delay

*Table B20. CO₂e lost per month of delay, one unit (Figure F6 inset data).*
*Source: `results/schedule_value.md` §2 [inputs TO VERIFY]. "None" = flat grid, so the month is recovered at the end of life.*

| Site, start year | Grid case | EF at start (g/kWh) | EF at end of life | Gross t/month | Net t/month | Days to cancel 1 kt (gross / net) |
|---|---|---:|---:|---:|---:|---|
| Darlington Unit 1, 2030 | ON-avg-traj | 52 | 15 | 9,372 | 7,243 | 3.2 / 4.2 |
| Darlington Unit 1, 2030 | ON-avg-flat | 74 | 74 | 13,718 | 0 | 2.2 / none |
| Darlington Unit 1, 2030 | ON-marginal-declining | 267 | 15 | 51,859 | 49,730 | 0.6 / 0.6 |
| Darlington Unit 1, 2030 | ON-marginal-flat | 343 | 343 | 66,777 | 0 | 0.5 / none |
| Darlington Units 2–4 (each), 2035 | ON-avg-traj | 33 | 15 | 5,750 | 3,622 | 5.3 / 8.4 |
| Darlington Units 2–4 (each), 2035 | ON-marginal-declining | 204 | 15 | 39,426 | 37,297 | 0.8 / 0.8 |
| Darlington Units 2–4 (each), 2035 | ON-marginal-flat | 343 | 343 | 66,777 | 0 | 0.5 / none |
| Liddell, 2035 | NEM-T0 frozen | 640 | 640 | 125,316 | 0 | 0.2 / none |
| Liddell, 2035 | NEM-T1 Step Change proxy | 171 | 30 | 32,831 | 27,746 | 0.9 / 1.1 |
| Liddell, 2035 | NEM-T2 slow | 396 | 30 | 77,224 | 72,139 | 0.4 / 0.4 |
| Liddell, 2040 | NEM-T0 frozen | 640 | 640 | 125,316 | 0 | 0.2 / none |
| Liddell, 2040 | NEM-T1 Step Change proxy | 30 | 30 | 5,085 | 0 | 6.0 / none |
| Liddell, 2040 | NEM-T2 slow | 274 | 30 | 53,178 | 48,092 | 0.6 / 0.6 |

A one-month slip of all three of Units 2–4 loses:
- 17,251 t gross / 10,865 t net (ON-avg-traj);
- 118,278 / 111,892 t (ON-marginal-declining);
- 200,332 / 0 t (ON-marginal-flat).

**Break-even sensitivity** (Units 2–4, ON-marginal-declining; central 1,226 t a day net, 0.8 days per kt):
- capacity factor 0.80 or 0.95: 0.9 or 0.8 days per kt;
- marginal factor 472 g/kWh (gas generation): 0.6 days per kt;
- gas off the margin by 2040: 1.5 days per kt; by 2060: 0.7 days per kt (`results/schedule_value.md` §5).

#### B5.3 Break-even delay for C1

*Table B21. Days of delay that cancel C1's LC3 saving (Units 2–4, start 2035).*
*Source: `results/schedule_value.md` §6. Saving 1,734 t per unit (90% interval 1,387–2,153) and 5,201 t for Units 2–4 (4,161–6,458), from `lca_scenarios.csv` and `lca_montecarlo_summary.csv` (§6.3). Brackets give the range over the saving's interval only.*

| Grid case (factor type) | Gross t/day per unit | Net t/day per unit | (a) Per unit, gross days | (a) Per unit, net days | (b) Programme saving, one unit late: gross days | (b) Net days |
|---|---:|---:|---|---|---|---|
| ON-avg-traj (average, declining to 2040) | 189 | 119 | 9.2 (7.3–11.4) | 14.6 (11.6–18.1) | 27.5 (22.0–34.2) | 43.7 (34.9–54.2) |
| ON-avg-flat (average, held at 2024) | 451 | 0 | 3.8 (3.1–4.8) | none (flat grid) | 11.5 (9.2–14.3) | none (flat grid) |
| ON-marginal-declining (gas leaves the margin by 2050) | 1,296 | 1,226 | 1.3 (1.1–1.7) | 1.4 (1.1–1.8) | 4.0 (3.2–5.0) | 4.2 (3.4–5.3) |
| ON-marginal-flat (held at 2024) | 2,195 | 0 | 0.8 (0.6–1.0) | none (flat grid) | 2.4 (1.9–2.9) | none (flat grid) |

The two cases:
- **(a)** compares one unit's saving with a delay to that unit. All three units' saving against a three-unit slip gives the same answer, because both scale by 3.
- **(b)** compares all of Units 2–4's saving with a delay to only one unit, for example when the first LC3 pour holds one unit's critical path.
#### B5.4 C1's carbon value against one month's delay

*Table B22. C1's carbon value (Units 2–4) against the value of the CO₂e lost in a one-month slip of all three units.*
*Source: `results/schedule_value.md` §7. Carbon prices: federal headline industrial trajectory (Environment and Climate Change Canada, 2026) [TO VERIFY]; the superseded 2021 path is shown for comparison only.*

| Carbon price (C$/t) | Basis | C1 carbon value, Units 2–4 (C$ m, 90% interval) | CO₂e lost in a one-month slip, average factor (C$ m, gross / net) | Same, marginal factor (C$ m, gross / net) |
|---:|---|---|---|---|
| **95** | **2026, current path (used)** | **0.49 (0.40–0.61)** | 1.64 / 1.03 | 11.24 / 10.63 |
| 110 | 2026, superseded path | 0.57 (0.46–0.71) | 1.90 / 1.20 | 13.01 / 12.31 |
| **115** | **2030, current path (used)** | **0.60 (0.48–0.74)** | 1.98 / 1.25 | 13.60 / 12.87 |
| 170 | 2030, superseded path | 0.88 (0.71–1.10) | 2.93 / 1.85 | 20.11 / 19.02 |

Working: carbon value = saving × price. For example, 5,201 t × C$95/t = C$0.49 m, and 5,201 × 115 = C$0.60 m. C1's concrete would be placed in about 2029–2033, so the 2030 price is the relevant one; 2026 is today's price.

**Direct cost of a one-month slip of Units 2–4** (inputs from `parameters_run5.yaml`; all TO VERIFY or assumptions):
- **Deferred output:** 3 × 300 MW × 8,760 h × 0.90 / 12 = 591,300 MWh × C$149/MWh (OPG's reported LCOE [TO VERIFY]) = **C$88 m**. The output is deferred, not lost, so this is a cash-flow cost to OPG and ratepayers, not a social loss of that size.
- **Carrying cost:** C$13.2 bn (Units 2–4: C$20.9 bn less C$7.7 bn for Unit 1 and common infrastructure) × r / 12. At r = 3, 5, 7 and 10%, that is **C$33, 55, 77 and 110 m**. It is an upper bound, because it assumes all the capital is already spent.

**How the 30–223× in §7 is derived:**
- **Low end:** the lowest monthly cost (C$33 m) over the largest carbon value we can construct (C$1.10 m, the 95th-percentile saving at the superseded C$170/t) = 30×.
- **High end:** the highest cost (C$110 m) over the central value at C$95/t (C$0.49 m) = 223×.
- **On the current path alone** (largest value C$0.743 m: 6,458 t × C$115/t), the low end is C$33.0 m / 0.743 = **44.4×** and the high end C$110.0 m / 0.494 = **222.6×**, i.e. 44–223× (`results/schedule_value.md` §7). The 30× in §7 uses the superseded C$170/t and is therefore the conservative bound.
- **In carbon alone,** the slip loses 10,865–118,278 t against C1's 5,201 t, which is 2.1–22.7 times the saving.

This agrees with `results/initiative_cost.md` §5 (run 5): one day of delay costs C$1.8–2.9 m, against C1's total carbon value of under C$1 m.

#### B5.5 Year-scale delays

*Table B23. CO₂e avoided to 2050 lost per year of delay, one unit.*
*Source: `results/schedule_value.md` §4 [inputs TO VERIFY].*

| Site | Grid case | Start A | Start B | Avoided to 2050 (A) | Avoided to 2050 (B) | Lost | Lost per year of delay |
|---|---|---:|---:|---:|---:|---:|---:|
| Liddell | NEM-T0 frozen | 2035 | 2040 | 24.06 Mt | 16.54 Mt | 7.52 Mt | 1.50 Mt |
| Liddell | NEM-T1 Step Change proxy | 2035 | 2040 | 1.64 Mt | 0.67 Mt | 0.97 Mt | 0.19 Mt |
| Liddell | NEM-T2 slow | 2035 | 2040 | 7.90 Mt | 3.85 Mt | 4.06 Mt | 0.81 Mt |
| Liddell | NEM-T2 slow | 2040 | 2045 | 3.85 Mt | 1.23 Mt | 2.61 Mt | 0.52 Mt |
| Darlington Unit 1 | ON-avg-traj | 2030 | 2032 | 1.01 Mt | 0.80 Mt | 0.22 Mt | 0.11 Mt |
| Darlington Unit 1 | ON-marginal-declining | 2030 | 2032 | 6.80 Mt | 5.59 Mt | 1.21 Mt | 0.61 Mt |

#### B5.6 Limitations
1. Average factors understate what a late baseload unit would have displaced in Ontario, where gas is on the margin.
2. The net basis assumes the plant's life is fixed in years, not extended.
3. The carbon value is realised only if someone prices it. Construction-material emissions appear to fall outside Ontario's Emissions Performance Standards (analyst inference, run 5) [TO VERIFY].
4. The carrying cost is an upper bound for an early slip.
5. Every input is provisional.

---

### B6. Same money: Darlington's budget spent on firmed renewables

**Result.** On GenCost 2023-24's 2030 costs, the same annual spend as one SMR unit (A$0.72 bn a year) buys **2.9×** the energy from firmed renewables (6.8 TWh a year against 2.37). For a Liddell SMR from 2040 on the slow trajectory, those renewables avoid **10.9×** more CO₂e to 2050 (5.7× in the worst case tested for renewables). Across the Liddell cases the ratio is 5.3–26.0×, so renewables avoid more CO₂e by 2050 in every case tested. On the alternative reading (SMR A$514/MWh), the ratios are 5.0× and 19.1× (9.3–45.8× across cases). Script: `python3 -I 03_LCA_Calculations/scripts/same_money.py`, with output in `results/same_money.md`.

**Basis of the tables.** The script now runs on the 2030 reading: SMR A$306/MWh (range 230–382) and firmed renewables A$107/MWh (89–125), from a news report of GenCost 2023-24 (Graham, Hayward and Foster, 2024, as reported) that gives A$387–641 as the SMR's **2023** value and A$230–382 as its **2030** value [TO VERIFY: GenCost table/year; the news pointer is in `sources_run5.md`, not sources.md]. Run 1's A$514 (387–641) / A$102 is kept as the alternative reading, in the sensitivity rows of Table B28 only. If Victor finds the table says otherwise, change `smr_lcoe_aud` and `vre_firmed_lcoe_aud` in `parameters_run1.yaml` and re-run; every table here regenerates.

#### B6.1 Inputs and method

*Table B24. Cost inputs and the two GenCost readings.*
*Source: `parameters_run1.yaml`; `results/lcoe.md` §5; references as named. All TO VERIFY or assumptions.*

| Input | Central (used in §7) | Alternative reading (sensitivity only) | Source |
|---|---|---|---|
| SMR LCOE | A$306/MWh (230–382), 2030 | A$514 (387–641), the 2023 value | Graham, Hayward and Foster (2024), as reported [TO VERIFY: GenCost table/year] |
| Firmed renewables LCOE | A$107/MWh (89–125), solar and wind with integration costs, 2030; 153 = high case, assumption | A$102 | Graham, Hayward and Foster (2024) [TO VERIFY] |
| Low SMR lead (sensitivity) | A$198/MWh | — | Kim and Macfarlane (2026) (edition unknown) [TO VERIFY] |
| Darlington budget | C$20.9 bn for four units; Unit 1 plus common infrastructure C$7.7 bn | — | Government of Ontario (2025) [TO VERIFY] |
| Exchange rate | 1.119 AUD/CAD (1.10–1.13) | — | Reserve Bank of Australia (2025) [TO VERIFY] |
| Discount rate; annuity | 7% real (3–10%); 30 years (30–60) | — | Assumption |
| First year of renewables output | 2028 (2027–2030) | — | Assumption [TODO: GenCost/AEMO lead times] |
| Renewables life cycle | 30 g/kWh (8–83) | — | Assumption (range: UNECE PV, United Nations Economic Commission for Europe, 2021) |

**Method A: what the Darlington capital would buy.**
1. Capital recovery factor: CRF(r, n) = r(1 + r)ⁿ / ((1 + r)ⁿ − 1). CRF(7%, 30) = 0.07 × 7.612 / 6.612 = 0.0806.
2. Annual capital charge = budget (A$) × CRF.
3. Capital-only LCOE = charge / annual output.
4. Firmed renewables bought with that charge = charge / renewables LCOE.

Worked example (one unit, simple share):
1. Budget: C$5.225 bn × 1.119 = A$5.85 bn.
2. Annual charge: 5.85 bn × 0.0806 = A$471 m a year.
3. Capital-only LCOE: 471 m / 2,365,200 MWh = **A$199/MWh**.
4. Renewables bought: 471 m / A$107 = 4.40 TWh, which is **1.9×** the SMR's 2.37 TWh.

The result is a lower bound on the renewables' advantage, because it ignores the SMR's operating and fuel costs.

**Method B: LCOE ratio and CO₂e per dollar.**
1. Energy ratio = SMR LCOE / renewables LCOE: 306 / 107 = **2.9×**.
2. CO₂e per A$1 m = (10⁶ / LCOE) MWh × (EF_grid − EF_technology) kg/MWh / 1,000. Example (SMR, NSW 640 g/kWh, A$306): 3,268 MWh × 635.8 / 1,000 = 2,078 t.
3. Cumulative comparison: the annual spend = SMR output × SMR LCOE, and the renewables bought with it = spend / renewables LCOE, from 2028. Each technology's avoided CO₂e is summed on the same trajectory (B4.1), net of its own life-cycle intensity (4.2 or 30 g/kWh).

#### B6.2 Results

*Table B25. Method A: what Darlington's capital would buy (7%, 30-year annuity).*
*Source: `results/same_money.md` §2 [inputs TO VERIFY].*

| Budget case | Annual capital charge (A$ m) | SMR capital-only LCOE (A$/MWh) | SMR output (TWh a year) | Firmed renewables bought (TWh a year) | Renewables / SMR energy |
|---|---:|---:|---:|---:|---:|
| Four units, C$20.9 bn | 1,885 | 199 | 9.46 | 17.61 | 1.9× |
| One unit, simple share | 471 | 199 | 2.37 | 4.40 | 1.9× |
| Unit 1 plus common infrastructure, C$7.7 bn | 694 | 294 | 2.37 | 6.49 | 2.7× |

Capital-only LCOE for one unit across discount rates (30-year / 60-year annuity): 3%, A$126 / 89; 7%, A$199 / 176; 10%, A$262 / 248 per MWh (`results/same_money.md` §2).

*Table B26. Method B (SMR A$306, renewables A$107 per MWh): CO₂e avoided per dollar, Liddell/NEM.*
*Source: `results/same_money.md` §3 [inputs TO VERIFY].*

| Displaced grid intensity (g/kWh) | Case | SMR t CO₂e per A$1 m | Renewables t CO₂e per A$1 m | SMR A$/t (gross) | Renewables A$/t (gross) |
|---:|---|---:|---:|---:|---:|
| 640 | NSW 2025 average | 2,078 | 5,701 | 481 | 175 |
| 274 | NEM-T2 in 2040 | 882 | 2,280 | 1,134 | 439 |
| 80 | Post-coal mix + 50 (illustrative) | 248 | 467 | 4,037 | 2,140 |

*Table B27. Cumulative CO₂e avoided for the same annual spend as one SMR unit (A$0.72 bn a year buys 6.8 TWh a year of firmed renewables from 2028, against the SMR's 2.37 TWh).*
*Source: `results/same_money.md` §4 [inputs TO VERIFY]. The alternative reading (A$514 / A$102; A$1.22 bn buys 11.9 TWh) gives Liddell ratios of 10.1×, 45.8×, 19.1× and 9.3× for the first four rows (Table B28).*

| Site | Grid case | SMR start | SMR to 2035 | SMR to 2050 | Renewables to 2035 | Renewables to 2050 | Renewables / SMR to 2050 |
|---|---|---:|---:|---:|---:|---:|---:|
| Liddell | NEM-T0 frozen | 2040 | 0 | 16.54 Mt | 33.01 Mt | 94.90 Mt | 5.7× |
| Liddell | NEM-T1 Step Change proxy | 2040 | 0 | 0.67 Mt | 16.50 Mt | 17.46 Mt | 26.0× |
| Liddell | NEM-T2 slow | 2040 | 0 | 3.85 Mt | 24.43 Mt | 41.76 Mt | 10.9× |
| Liddell | NEM-T2 slow | 2035 | 0.93 Mt | 7.90 Mt | 24.43 Mt | 41.76 Mt | 5.3× |
| Darlington (indicative, GenCost costs) | ON-avg-traj | 2030 | 0.54 Mt | 1.01 Mt | 0.88 Mt | −0.39 Mt | −0.4× |
| Darlington (indicative, GenCost costs) | ON-marginal-declining | 2030 | 3.29 Mt | 6.80 Mt | 11.82 Mt | 19.26 Mt | 2.8× |

The negative Ontario-average row arises because, once Ontario's average falls below the renewables' assumed 30 g/kWh life-cycle value, extra renewables add emissions against that average and the SMR's lower life-cycle value wins. This is a real property of a near-clean grid. But it rests on two placeholders (the renewables' life-cycle value and IESO's 2040 figure) and on the average rather than the marginal factor.

*Table B28. Sensitivity of the same-money result (Liddell, NEM-T2 slow, SMR from 2040). Figure F7 data.*
*Source: `results/same_money.md` §5 [inputs TO VERIFY]. Bold rows are run 5's reading, which §7 uses.*

| Case (SMR / renewables LCOE, A$/MWh) | Energy ratio | Renewables / SMR CO₂e to 2050 |
|---|---:|---:|
| **GenCost 2023-24, 2030 midpoints (306 / 107)** | **2.9×** | **10.9×** |
| **2030 low SMR, high renewables (230 / 153)** | **1.5×** | **5.7×** |
| Run 1 central, the alternative reading (514 / 102) | 5.0× | 19.1× |
| SMR LCOE low (387 / 102) | 3.8× | 14.4× |
| SMR LCOE high (641 / 102) | 6.3× | 23.9× |
| Low SMR lead (198 / 102) | 1.9× | 7.4× |
| Renewables LCOE low (514 / 91) | 5.6× | 21.4× |
| Renewables LCOE high (514 / 153, assumption) | 3.4× | 12.8× |
| Worst case for renewables tested (198 / 153) | 1.3× | 4.9× |
| SMR starts 2035 (514 / 102) | 5.0× | 9.3× |
| Renewables start 2030 (514 / 102) | 5.0× | 15.9× |
| Renewables life cycle 83 g/kWh (514 / 102) | 5.0× | 15.4× |
| SMR life cycle 5.8 g/kWh, our 95th percentile (514 / 102) | 5.0× | 19.3× |

#### B6.3 Check against our own LCOE and OPG's figure

Our Darlington LCOE (`results/lcoe.md`; case B, 60 years, vendor operating costs, CF 0.90) is C$112/151/198/280 per MWh at 3/5/7/10% real (A$125/169/221/313).
- **Against GenCost:** A$221 at 7% sits just below GenCost 2023-24's 2030 SMR range (A$230–382) [TO VERIFY]. Two reasons it should sit low: Darlington is a four-unit site with shared infrastructure, whereas GenCost prices a generic single Australian SMR; and GenCost 2025-26 reports revising Darlington's capital downwards for interest during construction (Graham and Hayward, 2026) [TO VERIFY]. At 10% (A$313) our figure falls in the upper half of GenCost's range.
- **Against OPG:** OPG's reported four-unit average of C$149/MWh [TO VERIFY] is reproduced at a real discount rate of 4.9%. That rate is consistent with a ratepayer-backed Crown utility, not with merchant finance.
- **Cost ratio:** on our 7% value against GenCost 2024-25's firmed-renewables lead, the SMR/renewables cost ratio is 221 / 101 = 2.2× (`results/lcoe.md` §5).
- **Full working:** in `results/lcoe.md` [TODO: an Appendix B subsection for the LCOE with §8.2].

#### B6.4 Limitations
1. Adding several TWh a year of firmed renewables would itself change the NEM trajectory, so the comparison holds only at the margin of the stated trajectory.
2. The LCOE of firmed renewables rises with their share, and GenCost's integration costs cover this only up to the shares it models.
3. Darlington's budget is in nominal Canadian dollars (2025 announcement), while GenCost is in real Australian dollars. Method A is therefore an order-of-magnitude cross-check, not a precise conversion.
4. Renewable assets last about 25–30 years [TO VERIFY, GenCost]. No replacement falls before 2050, but a whole-life comparison would need one.
5. The Ontario rows use Australian costs and are indicative only. Ontario-specific costs were a STRETCH item in the plan and were not done.

---

### IDs covered (towards the HD descriptor) and what is still missing

- **RB.5 (full calculations in an appendix, results summarised in the main text).**
  - Produced: the working behind every number in §8.1 and §8.3 (Senate arithmetic, licensing durations, HHI shares and sensitivity, route scores), each traced to a script output, with the commands to re-run.
  - Produced (v2): the working behind §7 (B4–B6): formulas, worked examples, every input with its source and status (Table B15), all result tables, sensitivities and limitations.
  - Missing: input verification; the LCOE subsection (with §8.2) and the MCDA (B7, Q14); one consistent GenCost basis in B6 after the re-run.
- **R2.1, R2.3, R2.7, R4.3 (v2, supporting §7).**
  - Produced: displacement per unit and for four units; C1's break-even days and carbon value against the cost of delay, sized to Units 2–4; average vs marginal factors, seven trajectories, one-at-a-time sensitivities, and the saving's 90% interval carried through.
  - Missing: AEMO/IESO series in place of the constructed trajectories; 315 MWe in the sensitivity; verified grid factors and carbon price.
- **R3.1, R3.6, RB.6 (v2, supporting §7, §8.2, §9).**
  - Produced: same-money Methods A and B, both GenCost readings, and our LCOE checked against GenCost and OPG.
  - Missing: the GenCost 2023-24 table check and the GenCost 2025-26 values.
- **R2.4 ("methods are clearly explained and easy to follow").**
  - Produced: stated formulas (months, Senate majority, HHI, N_eq, renormalisation, residual bounds), a worked enrichment example, and the threshold sources with the "scale, not legal test" caveat.
  - Missing: §2 (methods) is not written, so the main text still has no method summary; the B3 weight test is not scripted.
- **R3.8 ("supported by evidence and quantitative/qualitative analysis").**
  - Produced: quantitative tables for the political and supply arguments, the qualitative route scoring clearly labelled as judgement, and every unverified input marked.
  - Missing: no primary source opened; One Nation, Babet and the 2024 state rejection still lack sources.
- **R2.7 and R1.3 (supporting).** Produced: all sensitivity rows, both threshold classes, the company-versus-country contrast, and the limitations. Missing: the CRAI range for Rosatom; the Red Book edition decision.
- **R3.6 (supporting).** Produced: the scored route comparison with a weight test, ready for §9. Missing: the §9 MCDA itself.

### Remaining TODOs

1. **[TO VERIFY, P1]** Open the primaries behind Tables B1–B4 and B7–B10 (factcheck.md human checklist). Set `verified: true` / the verified status, re-run both scripts, and update any value that moves.
2. **[TODO: source needed]** One Nation's position (ABC, 31 August 2026) into `sources.md`; Babet stays an assumption. The 2022 bill's lapse (ParlInfo). The 2024 state rejection of route A. The Coalition's 19 June 2024 release for route A.
3. **[TODO: sources.md]** Add the *Commonwealth of Australia Constitution Act* (ss 23 and 109).
4. **[TODO: analyst]** Add the CRAI (2025) enrichment row to `hhi.py` and `sources.md`; report Russia's share as a range in B2.2.
5. **[TODO: analyst]** Put the B3 scoring and weight test in a script (with the §9 MCDA, run 7) so it is reproducible.
6. **[TODO: Leroy/analyst]** BWRX-300 fuel data, to size Darlington's SWU/yr against Urenco USA and Orano capacity (B2.5).
7. **[TODO: team decision]** Red Book edition for Australia's resource share (B2.3).
8. **[TODO: Leroy, references]** Disambiguate CNSC 2026a (project page) and 2026b (hold-point page); fix "Parliament of New South Wales, 2025–26" to a single year with a suffix; confirm the WNA page years; give REGDOC-3.5.1 its year.
9. **[TODO: bill date]** ANNPSR bill introduction date (Bills Digest No. 32, 2023–24), to give the "Act to operating regulator" interval exactly.
10. **[TODO: coordinator]** Displacement, schedule value and same money are now B4–B6 (v2). Still to write: the LCOE subsection (with §8.2) and B7 MCDA (Q14).
11. **[TO VERIFY: GenCost table/year, Victor]** If A$230–382 is confirmed as GenCost 2023-24's 2030 SMR value, set `smr_lcoe_aud` 306 (230–382) and `vre_firmed_lcoe_aud` 107 (89–125) in `parameters_run1.yaml`, re-run `same_money.py`, and replace Tables B26–B28 so all of B6 is on one basis.
12. **[TO VERIFY, Victor]** The federal carbon price path (C$95 in 2026, C$115 in 2030) on canada.ca; then have run 5 align `parameters_run5.yaml` and re-run `initiative_cost.py`. Script the 45× current-path figure (B5.4) in `schedule_value.py`.
13. **[TO VERIFY]** The B4–B6 inputs in Table B15 and Table B24 (TAF 2025 average and marginal definition; NGA 2025; CER; IESO 2040; AEMO coal exit; AER/AGL Liddell closure; RBA rate; OPG C$149/MWh, whose `opg_oeb_lcoe_lead` entry must be merged from `sources_run5.md` into sources.md; the Bayswater closure date).
14. **[TODO: Leroy]** Net MWe (300 vs 315: add 315 to the B4 sensitivity), capacity factor, design life and start years.
15. **[Before submission]** Strip the [TO VERIFY]/[TODO] markers and the changelog comment; set the final table numbers.
