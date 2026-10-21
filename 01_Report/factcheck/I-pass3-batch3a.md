Rubric coverage: R1.4, R2.4, R2.6, R3.6, RB.8, R5.4

# Fact-check I, pass 3, batch 3a: §1, §2, §9 and Appendix B7 (Tables B29-B34)

Checked 21/10/2026 (fact-checker). Scope: `sections/1-introduction.md`, `2-methods-data.md`, `9-tbl-mcda.md`, and B7 of `appendix-B-policy-and-supply-working.md` only. Placeholders "[C1 saving: per final §6]" and "[per final ...]" not flagged, as agreed. Primary hosts are blocked, so no source was opened. Status "supported (secondary)" means the repo's sources file records the claim, not that a primary was read.

## Reproduction
`python3 -I 03_LCA_Calculations/scripts/mcda.py --c1-case new_2200` re-run: `results/mcda.md` and `results/mcda_scores.csv` come out **byte-identical** (diff clean). Every score in T5, B31, B32, B34 matches. I recomputed by hand: the B7.2 worked example (2.0766 -> 29.7), A$0.724 bn/yr, 6.76 TWh, 5.31 and 57.69 Mt per A$bn, 0.0155 and 0.0122 g/kWh, A$0.038/MWh, 1.419e11 kWh, 10.9x, 2.9x, 12x and 15x. All correct. 17 input cases x 4 = 68 tests, 66 with renewables first (the two exceptions are W2 under the worst-case-for-renewables and status-quo-social-14 changes): matches the text.

## MUST-FIX (4)
| # | Where | Problem | Evidence | Fix |
|---|---|---|---|---|
| M1 | §9 opening paragraph | Absolute claim contradicted by the same section: "No weight set, input change or +/-50% weight test we ran puts an SMR first." The random-weight run puts an SMR option first in 0.16% of draws, and §9.2 itself says an SMR ranks first at >=94% life-cycle weight. | `mcda.md` §5 (first-share SMR 0.00035 + SMR+C1 0.00125; threshold 0.936) | "No named weight set, input change or +/-50% test puts an SMR first (it needs about 94% of the weight on life-cycle CO2e)." |
| M2 | §9.2 "Rank reversal" | "an SMR option in 0.1%": SMR (0.035%) + SMR+C1 (0.125%) = 0.16%, which rounds to 0.2%. The three shares then sum to 100.0 only as 85.4 + 14.5 + 0.2 (B7.4 shows 0.1% and 0.0% separately, which is right). | script output `first-share`, `mcda.md` §5 | "in 0.2% (SMR 0.0%, SMR + C1 0.1%)". |
| M3 | §1 Context, "Liddell ... shut in April 2023 (Australian Energy Regulator, 2021)" | A 2021 AER decision can only support the *planned* closure date, not that the unit shut. sources.md (`aer2021_liddell`) says the actual 28 April 2023 date comes from news (Newcastle Herald, RenewEconomy) and "AGL's own release would be better". Cited source does not support "shut". | sources.md L87-91 | Cite AGL's release or the AER 2021 notice for "approved to run to April 2023" and add a primary/AGL source for the closure; or write "scheduled to close in April 2023 and closed on 28 April". |
| M4 | §1 "up to about 300 MWe ... (International Atomic Energy Agency, 2024)" | **Source not found.** No IAEA 2024 SMR entry exists in `sources*.md` (only Milestones NG-G-3.1 and Red Book). A cited reference with no bibliography entry fails R5.4 and R1.4. | Grep of sources*.md: no `IAEA` SMR/ARIS 2024 key | Add the entry (IAEA, *Advances in Small Modular Reactor Technology Developments*, ARIS booklet, 2024 edition) to sources.md with [TO VERIFY], or cite the definition from the Red Book/IAEA glossary. |

## SHOULD-FIX (12)
| # | Where | Problem | Evidence | Fix |
|---|---|---|---|---|
| S1 | §2, B33 (alternative GenCost reading) | "the alternative reading, A$387-641, gives 5.0x": 5.0x is 514/**102** (the 2024-25 renewables figure), not against 89-125 (mid 107), which gives 4.8x. Also run 1's own note says NucNet gives 387-641 as the **2023** SMR value, not 2030, so this "reading" is probably a misreading, not an alternative. | `same_money.md` L84 (514/102 = 5.0x); `parameters_run1.yaml` L299 note; WebSearch lead (NucNet, 5/4/2024): 230-382 for 2030, 387-641 for 2023 [secondary, TO VERIFY] | Say "A$514 against A$102 gives 5.0x" and that 387-641 may be the 2023 value; keep [TO VERIFY]. If the NucNet lead holds, the central reading is the only one. |
| S2 | §2, T4, T5, B29 (GenCost 2030 SMR 230-382 and 89-125) | Central cost input rests on trade-press leads (NucNet, Klaxon); Capital Brief reports 82-120 for renewables. GenCost PDF never opened. Marked [TO VERIFY] in §2 and T5 note but T4's cost cell states it flat. | sources.md L103-107; `parameters_run1.yaml` L314 | Keep marker in T4 (its note says "All inputs [TO VERIFY]": acceptable) and put the access limit in B7.6 item 5; a human should open the PDF (human-checklist). |
| S3 | §2 Displacement | Ontario marginal factor "343 g/kWh (2024)" is stated as the marginal factor; sources.md says the TAF slide wording is "ambiguous (average vs marginal)". | sources.md L44 | "343 g/kWh (2024; TAF slide labelled 'Historical Annual MEF') [TO VERIFY]". |
| S4 | §1 Context | "the design furthest along in an OECD country": a superlative with no comparison source (NuScale holds a US design approval). | none in sources | "the first SMR licensed for construction in an OECD country" (CNSC 2025 supports that). |
| S5 | §1 Initiative | "Concrete is the largest material by mass in a reactor building, and its cement is the main embodied-carbon source in construction": two unsourced general claims. | none | Cite §5/§6 (concrete share of the unit's mass and of embodied CO2e) or soften to "the largest material by mass in our inventory". |
| S6 | §1 Answer in brief | "a few days of delay cancel the saving": break-even is 9.2-14.6 days on Ontario's average factor (1.3-1.4 on the marginal). Nine to fifteen days is not "a few". | `schedule_value.md` L66-77; B5.3 | "about one to two weeks (1-2 days on the marginal factor)" once final §7 lands. |
| S7 | §1 and §9 CSIRO "2040 at the earliest" | Applied to SMRs, but sources.md records that the statement may cover only *large-scale* nuclear; the first-power year drives the time criterion and the 10.9x. | sources.md L107 "Check: whether the 2040 statement covers SMRs" | Keep [TO VERIFY]; §9 limits already flags it. Open GenCost 2023-24 sect. on nuclear development time. |
| S8 | T4 Environment cell | "Unit 1 avoids 1.0-6.8 Mt CO2e to 2050" takes the two *declining*-grid cases; the flat cases are 3.46 and 16.83 Mt. Range is selective and unlabelled. | `displacement.md` §3 | Add "(declining-grid cases)" or give 1.0-17 Mt. Same for Liddell "0.67-3.9 Mt" (excludes frozen 16.5 Mt): label "declining-grid cases". |
| S9 | B7 header | "593 rows" in `mcda_scores.csv`: file has 593 lines including the header, so 592 data rows. | `wc -l` | "592 rows". |
| S10 | §9 IDs-covered block | R2.4 "Missing: §2 (methods summary) not yet written": §2 now exists. Stale. | `sections/2-methods-data.md` | Update at next pass. |
| S11 | B33 "Worst case for renewables (SMR A$198, renewables A$153)" | Appendix text gives no basis. 198 is run 1's `smr_lcoe_low_alt_aud` and 153 an unsourced assumption; neither is in the GenCost range cited (230-382, 89-125). A reader cannot reproduce the case from B7. | `parameters_run1.yaml` L300, L322 (source: assumption) | One sentence: "SMR at the low end of the older range; renewables at A$153 (our assumption: 43% above the GenCost midpoint)". |
| S12 | §2 and B7.2 Dodgson et al. (2009); IEA (2022); ISO 2006a/b | Cited claims ("standard compensatory model", "linear additive and 0-1 local scales") are from memory of the method, not confirmed in the text; Dodgson and IEA entries still sit in `sources_run9.md` and ISO entries in sources.md are both "2006" with no a/b. Reference list needs a/b suffixes and the merge. | sources_run9.md L10; sources.md L931-938 | Merge at Q19; open Dodgson ch. 6. Already in TODOs: keep. |

## OK (verified or consistent)
| Item | Result |
|---|---|
| T4 numbers: 4.2 (3.0-5.8); 1,734-2,200 t, 0.29-0.37%; C$0.49-0.60 m (95-115 C$/t x 5,202 t); C$1.8-2.9 m/day; C$198 (112-280); stance +1.07 / -1.03; 10.9x; 2.9x; 3,009; three routes 5-8 of 12 (A 6 / B 5 / C 8) | Match `lca.md`, `initiative_cost.md` §5, `schedule_value.md` L104, `lcoe.md`, `social_licence.md` L78/L96, `mcda.md` §8 |
| T4 vs §6-§8 (context card T4 check) | Consistent: 61% / 59% (§8.4), C$700 m (§8.4/8.5), Russian stage (§8.3, [TO VERIFY] there), A 6 / B 5 / C 8 after the M2 correction (the mcda.md text records it). C$0.88 m (superseded C$170 path) correctly not used. |
| T5 / B31 / B32 (80.1, 85.9, 63.7, 89.3; 52.4, 41.7, 60.0, 55.0; 29.7, 24.0, 43.6, 20.4; 0/0/2/0 of 14) | Exact match to `mcda.md` §4-5 and the csv |
| §9.2 rank reversal: 56 tests, 2 flips both W2 to status quo; 94% (0.936); 85.4 / 14.5 shares; 66 of 68; 4.200 -> 4.188 / 4.185 | Match (see M2 for the 0.1%) |
| §9 scaling artefact (global scales: renewables > SMR > status quo in all four sets) | Matches `mcda.md` §6 last row |
| B29-B30, B7.2 worked example and C1 arithmetic | Match / recomputed |
| B34 (gaps -0.0016/-0.0017/-0.0015/-0.0012; free +0.00038/+0.00024/+0.00049/+0.00073; 25.5 kt; 12x and 15x) | Match `mcda.md` §7 |
| §2 reference flow 1.419e8 MWh; 2.365 TWh/yr; HHI definition and DOJ/FTC thresholds (2023 > 1,800; 2010 1,500 and 2,500; mining 2,341 between them) | Correct; DOJ/FTC entry in sources.md (not opened) |
| §1 facts: Liddell 2,000 MW; NSW 0.64 kg/kWh (NGA 2025, via ASIC example, secondary); Ontario 73.8 g/kWh; OPG C$20.9 bn for four units; CNSC licence to construct one unit (4 April 2025); Unit 1 October 2030 (OEB filing EB-2025-0297, sources.md L451-679) | Supported by sources.md (secondary); Ontario coal 2014 correctly carries a TODO |
| Cross-section: §9 cites Table T13, Appendix B3 route C, §8.6 (2027 start, 2028 decision, mock-up, slag fallback) | All exist and agree |
| Table-number clashes | T4 and T5 are free (renumber at Q19 as noted). **FYI outside scope:** T10 is used twice (§7 and §8.2). |

## Counts
Must-fix 4, should-fix 12, OK 10 groups. All MCDA numbers reproduce; the problems are wording, citations and unsourced context claims, not arithmetic.

## Rubric IDs (what this batch produced towards HD, and what is missing)
- **R1.4:** §2 names ISO, DOJ/FTC, Dodgson, IEA, GenCost, TAF; all are primary or intergovernmental, but none was opened (M4, S2, S12). Missing: IAEA entry, search log (App E), opened primaries.
- **R2.4:** method, formulas, worked example and reproduce command are present and reproduce exactly; Missing: S11 (worst-case basis), final §6/§7 numbers.
- **R2.6:** verdict follows from T4/T5 and states its conditions; Missing: M1 (overclaim) and the status-quo scaling caveat is present (good).
- **R3.6:** four-option MCDA with rank-reversal and random weights is evidenced and exact; Missing: TRL criterion and elicited weights (disclosed).
- **RB.8:** T4 traced to §6-§8 and consistent; Missing: final C1 figures, S8 range labels.
- **R5.4:** Harvard in-text style consistent; Missing: M3/M4 citation fixes, a/b suffixes and merging of the Dodgson and IEA entries.
