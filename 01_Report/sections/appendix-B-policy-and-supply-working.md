Rubric coverage: RB.5, R2.4, R3.8 (also supports R2.1, R2.7, R3.2, R3.4, R3.6, R1.3, R5.2)

<!--
CHANGELOG
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

This appendix gives the full working behind §8.1 (law and licensing) and §8.3 (fuel-supply concentration). Every number is produced by a script in `03_LCA_Calculations/scripts/` from a parameter file, so it can be re-run. **No input has yet been checked against its primary source** (`status: TO VERIFY` in `parameters_run2.yaml`; `verified: false` in `parameters_run3.yaml`).

| Subsection | Script (run from the repository root) | Inputs | Output |
|---|---|---|---|
| B1 Legal and political pathway | `python3 -I 03_LCA_Calculations/scripts/law_timelines.py` | `03_LCA_Calculations/parameters_run2.yaml` | `03_LCA_Calculations/results/law_timelines.csv` |
| B2 Supply concentration (HHI) | `python3 -I 03_LCA_Calculations/scripts/hhi.py` | `03_LCA_Calculations/parameters_run3.yaml` | `03_LCA_Calculations/results/hhi.md`, `hhi_summary.csv` |
| B3 Routes to a licensable SMR in Australia | none (qualitative scoring) [TODO: move into the MCDA script, analyst run 7] | Law brief §5 | This appendix |

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

### IDs covered (towards the HD descriptor) and what is still missing

- **RB.5 (full calculations in an appendix, results summarised in the main text).**
  - Produced: the working behind every number in §8.1 and §8.3 (Senate arithmetic, licensing durations, HHI shares and sensitivity, route scores), each traced to a script output, with the commands to re-run.
  - Missing: input verification; the other Appendix B calculations in plan §3 (displacement, schedule value, same money, LCOE, MCDA), which have results files but no appendix text yet.
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
10. **[TODO: coordinator]** Write the remaining Appendix B subsections (displacement, schedule value, same money, LCOE, MCDA) from `results/`, or re-letter them as a separate appendix.
11. **[Before submission]** Strip the [TO VERIFY]/[TODO] markers and the changelog comment; set the final table numbers.
