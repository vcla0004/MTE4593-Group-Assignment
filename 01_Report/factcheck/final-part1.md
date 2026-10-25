Rubric coverage: R1.4, R2.3, R2.7, R5.4, R5.5

# Final fact-check, part 1 (Q20), 25/10/2026

Scope: 0, 1, 2, 3, 4.3, 8.4, 8.5, 8.6, 9, 11 and `appendix-B-moved-from-8.4-8.6.md`. Only must-fix items are listed. Nothing edited.

## Checks that passed
- **C1 numbers (focus 1).** 2,200 t/unit (1,100–3,300), 6,600 t Units 2–4, 20,000 m³ eligible, 11.6–18.5 / 1.7–1.8 days, C$0.63–0.76 m, C$10.4–12.7/m³ (in §8.2), C$152/t (§8.2), 0.37%, 15× at 18.5 days, 20–175× (§11) and MCDA 80.1/52.4/29.7/29.7 all match `c1_deck_case.md` and `mcda.md` (re-run of `mcda.py --c1-case new_2200` reproduced them). No stale value (1,734; 5.2 kt; 9–15 days; 14.6; C$0.49; 12×) and no `[C1 saving: per final §6]` marker remains in the 11 files.
- **Markers (focus 3).** The only in-body marker is `[TODO-GRANTA]` in §2. The "Remaining TODOs" and "IDs covered" blocks are stripped by `assemble_draft.py` (DROP_HEADINGS). The `[Figure F8 …]` line in §8.5 needs the PNG at assembly.
- **§8.6 vs §8.2 (focus 4).** Resolved. §8.2 now points to T16, the contract clause is absorbed in L1, and "L1 now, L4 in 2027, L2 at the 2028 tranche" matches §8.1 ("qualification must start in 2027, slag the fallback"). T16 weight test recomputes (L1 8/11 speed-doubled, L2 8/11 enforceability-doubled, L3 7). Step durations sum to 18–24 months. T14 shares (78 / 4.6 / 14.4 / 3.3%) recompute.
- "Pilot LC³ in eligible non-safety works first" is worded the same way in the abstract, §1, §4.3, §8.6, §9 and §11.
- **Not checkable.** Pillai et al. (2019) M50 380 vs 270 kg CO₂e/m³ and Ostrołęka Table 14 (50,000 m³): both hosts refused (doi.org; am.lrv.lt via search lead). Still `[TO VERIFY]` in `sources.md`. Human check needed. Candidate Ostrołęka copy: https://am.lrv.lt/media/viesa/saugykla/2024/2/oHCKCUp7Lrs.pdf (English, Warsaw, August 2023; unopened).

## Must-fix

| # | File and place | Problem | Exact replacement |
|---|---|---|---|
| 1 | §9.2 "Rank reversal" | "0.2% of 20,000 random weight sets" disagrees with `mcda.md` §5 (SMR 0.0% + SMR+C1 0.1%) and App B7 (0.1%) | "…or in 0.1% of 20,000 random weight sets." |
| 2 | §4.3 lead, sentence 2 | "the design calls for a self-consolidating mix (GE-Hitachi Nuclear Energy, 2024)" is not supported: the `sources.md` entry for NEDO-33926 has no finding on self-consolidating concrete, and a search of its public descriptions found none | "The infill must flow between closely spaced plates, so we assume a self-consolidating mix, which is cement-rich (our inference; GE-Hitachi Nuclear Energy, 2024, describes the DPSC design)." |
| 3 | §4.3 T1 "Condition" row | NEDO-33926 is GE-Hitachi (2024), not the joint NRC–CNSC report; the cited entry does not carry the code claim | "Schedule-neutral. Infill qualified under the topical report NEDO-33926, which rests on AISC N690 and ASME rather than mainly CSA N287 (GE-Hitachi Nuclear Energy, 2024; US Nuclear Regulatory Commission and Canadian Nuclear Safety Commission, 2025); otherwise slag or the current mix" |
| 4 | §4.3 "Why it is not the obvious choice", second point | "a Darlington unit avoids about as much CO₂e to 2050 as a Liddell unit" overstates: `displacement.md` gives 1.0–6.8 Mt against 0.67–3.9 Mt (Darlington 1.5–1.8× larger) | "counted from when each plant could actually run, a Darlington unit avoids 1.0–6.8 Mt CO₂e to 2050 and a Liddell unit 0.67–3.9 Mt, the same order of magnitude (§7), and Darlington is where a qualified mix can be built." |
| 5 | §1 Context, last sentence | "first SMR licensed for construction in an OECD country (CNSC, 2025)": the CNSC release does not say "OECD", and `sources.md` records that Ontario's own wording is only "first SMR in the G7" | "The BWRX-300 received a Canadian Nuclear Safety Commission licence to construct at Darlington in April 2025 (Canadian Nuclear Safety Commission, 2025)." |
| 6 | §3 T15 row 1 | C$149 is only a reported OEB figure (`lcoe.md`: "reportedly… [TO VERIFY, lead via LinkedIn]") yet is attributed to "OPG 2025", whose suffix is also ambiguous | "**C$149–198/MWh** (OPG's figure as reported, Ontario Power Generation, 2026b; this study)" |
| 7 | Unsuffixed "Ontario Power Generation, 2025" in §1 (two uses) and §2 | No such entry; the list has 2025a/b/c (see `12-references.md` note 1) | In §1 and §2 use "Ontario Power Generation, 2025a" (Q1 results: C$20.9 bn and 2030 grid connection). §3 row 2 already reads 2025b: change to 2025a for Unit 1 in 2030. |
| 8 | §3 T15 row 3 | "At most 36–37 of 39 Senate votes needed" reads as if 36–37 votes suffice | "No more than 36–37 of the 39 Senate votes needed to repeal the federal bans" |
| 9 | Moved appendix, B8 head list | "Australian Energy Market Operator (2024)" has no entry; the reference is 2025 | "Australian Energy Market Operator (2025)" |
| 10 | `12-references.md`, entries cited in these sections with placeholders left in the text. These will print as unfinished references (R5.4) | See replacements | **Ostrołęka:** replace "[URL TODO]" with "[pdf] Warsaw, August 2023. Available at: https://am.lrv.lt/media/viesa/saugykla/2024/2/oHCKCUp7Lrs.pdf [Accessed 25 October 2026]" only after a human has opened it and confirmed Table 14, p. 83. **Essential Research 2019** (cited in §8.4 for "16–20 points lower"; date unconfirmed): if not confirmed, delete "; Essential Research, 2019" from §8.4 and the entry. **Australian Council of Trade Unions 2024** (appears only in the B8 list): delete the name from the list and the entry. **AEC 2019, Conference Board 2021, OPG 2026b, Slovic DOI:** a human must complete them; otherwise delete the cited claim. Do not invent titles. |

## Flags for the coordinator (not section errors)
- **Appendix B and §6, Apps A and C still carry the old case.** Appendix B has 18 hits for 1,734 / 5.2 kt / 9.2–14.6 days / "12×", and §6 has 10 hits. §9's note says App B7.5 "should read 15× at 18.5 days", which is not yet done. These are Victor's LCA pass, but they will contradict §4.3, §7 and §9 if left.
- **Duplicate B8.3.** `appendix-B-policy-and-supply-working.md` already has B8.3 (Table B39, T13 with per-criterion scores, line 921). Merge the moved "Reading" sentence into it instead of pasting a second T13. Its totals (7 / 11 / 11 / 14 and the weighted columns) match.
- §3 row 5 sets "7.5% of life-cycle emissions is construction" (old 20,700 m³ model) beside the deck-case 2,200 t. Fine only if §6 keeps 7.5%.
- T16 "tranche 2 (around 2028)" is our inference (the CGF/BOF source gives milestones only); add "(our inference)" if space allows.

## Rubric evidence (by ID)
- **R1.4.** Primary and industry sources are visible in the list (NEDO-33926, CNSC–NRC report, OEB exhibit, treaties report). Gap: items 2, 3 and 10 (unopened primaries and placeholder entries). Not yet HD until items 10 and the Pillai/Ostrołęka human check are closed.
- **R2.3.** The C1 quantities match `c1_deck_case.md` across all 11 files. Gap: Appendix B and §6 are not re-based; Pillai and Ostrołęka are unverified.
- **R2.7.** Error and limit statements hold (rank-reversal counts 56 and 68, 2 and 2 flips, 94% threshold recompute). Gap: item 1.
- **R5.4.** Gaps: items 7, 9, 10.
- **R5.5.** Consistency across files is good for the 11 files; the open gap is the stale Appendix B/§6 values above.
