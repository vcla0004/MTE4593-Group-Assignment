Rubric coverage: R1.4, R3.5, R3.7, R2.7, RB.5

# I. Pass 3, batch 1b: fact-check (21/10/2026)

Scope: `8.6-implementation.md` (full, first check); commit 026b4b5 changes to §8.3, §8.4, §8.5 and Appendix B (B2 Result, B2.6, B6 correction, B8). **§3 and §8.1 were not touched by 026b4b5** (no diff), so nothing new to check there. Skipped: B7. Expected markers not flagged: "[C1 saving: per final §6]", Senate M1, GenCost.
Method: `python3 -I scripts/hhi.py` re-run (reproduces 195.6 tU, 137.7 tSWU, 3.20%, 77-301, 275-551). `social_licence.py` and `same_money.py` could not be re-run (no matplotlib in this sandbox); I checked their `results/*.md` against the text and recomputed the stance sums, route totals, deaths avoided, money shares and 8.6 lever scores by hand. All sources are "not opened" in sources.md, so every citation is unreachable-until-human; only the support in the source notes was checked.

## Must-fix (2)

| # | Where | Claim | Status | Evidence | Fix |
|---|---|---|---|---|---|
| M1 | §8.6 Qualification | "Steps 1 to 3 take about 18 to 24 months (our planning assumption, summing the durations above, route brief §6)" | Arithmetic not supported | The text gives step 1 = 6-9 months and step 2 = 6 months (sum 12-15); step 3 has no duration in the text. The brief (§6) gives 18-24 months from step 1 to licensing acceptance as its own estimate, not as a sum. | Drop "summing the durations above" or add step 3's duration (about 6-9 months) so the sum works. |
| M2 | §8.6 opening and ¶1 | L1 is "concrete at least 10% below the regional baseline" (T16), yet the pilot "saves 1,100/2,200/3,300 t" | Internal mismatch | 1,100/2,200/3,300 t = 20/40/60% x 50,000 m³ x (380 - 270 = 110 kg/m³), i.e. the full LC³ swap (29% below OPC), not a 10% floor (about 38 kg/m³, 380 t at 20%). The reader cannot tell which spec delivers the saving. | One clause: "L1 sets a 10% floor and invites LC³, which cuts 29% (380 to 270 kg/m³)", or state the saving is the LC³ case. |

## Should-fix (9)

| # | Where | Claim | Status | Evidence | Fix |
|---|---|---|---|---|---|
| S1 | §8.6 opening | "C1 can be built without delay if ..." | Overclaim | No delay-free result exists; §6/§7 break-even is 9-15 days and the 2028 approval date is secondary (ANS). | "with no added delay on the evidence available", and cite the §7 break-even. |
| S2 | §8.6 / §8.2 | §8.6 L1 first (T11 B), §8.2 says C plus A with B as fallback | Inconsistent (known, Q14) | §8.2 line 23. | Resolve in Q14; the changelog already flags it. |
| S3 | §8.6 T16 source, §8.5 source | "Ontario Power Generation (2025b)" | Citation key | Other sections use "(2025)" with no 2025a; sources.md has one OPG 2025 entry. | Assembly: assign 2025a/2025b consistently in the reference list. |
| S4 | §8.6 fuel | "Domestic enrichment needs the federal bans repealed (§8.1) and 15 or more years" | Ambiguous | EPBC s 140A / ARPANS s 10 are Australian. In a section about Darlington, a reader may take it as Canadian. | Add "in Australia". |
| S5 | §8.6 | "approval ... by the 2028 approval" | Weak source | Only ANS (2026), secondary ("expected in 2028"); brief TODO 9. [TO VERIFY] is present. R1.4 wants a primary source. | Find an OPG or Ontario primary, or write "reported". |
| S6 | §8.6 | "CNSC regulates safety, not climate" | Slight overstatement | The CNSC also regulates environmental protection under the Nuclear Safety and Control Act. The claim is marked "our inference". | "does not set climate conditions". |
| S7 | App B8.4 Limits | "C$170 m / 81 years = C$2.1 m a year, 0.65% of the C$26 bn lifecycle cost" | Ambiguous | 0.65% is 170/26,000 (the total), not 2.1 m a year (0.008%); also nominal against 2020 dollars (`social_licence.md` §3). | "C$170 m in total is 0.65% of ...". |
| S8 | App B6 Result | "On Ontario's average grid the SMR wins (-0.4x)" in bold | Needs hedge | `same_money.md` note: it rests on two placeholders (30 g/kWh renewables life cycle; IESO 2040) and the average (not marginal) factor. The caveat is in the paragraph under Table B27 but not in the Result. | Add "on two placeholders" to the Result sentence. |
| S9 | RB.5 (T16) | T16 scores, totals and the weight test (8/8/7; 11 and 11) | No appendix working | Hand-checked as correct (equal 8/8/7; enforceability x2: L1 10, L2 11, L3 10; speed x2: L1 11, L2 10, L3 9). No table in App B. | Add a 5-line T16 score table to App B (B3 style, hand calculation). |

## OK (verified)

| Item | Result |
|---|---|
| B2.6 working and Table B35 | 372,414 kWh/kg, 6.35 t, 48.9 tU, 34.4 tSWU; 195.6 tU, 137.7 tSWU; 3.20/2.75/1.97/0.56/0.20% match `hhi.md` §6.2 and re-run. Feed 7.701 and 5.422 SWU/kg are standard values for 3.8%/0.25%. |
| B2.6 sensitivity and reserve | 113-199 (one at a time, 112.7-198.6), 77-301, 1.79-7.00%, 275-551 tSWU, 6-13% all match. 51-102 t enriched consistent. |
| B2 Result mining by company | 851-1,384 -> "about 850-1,400", midpoint 1,118; matches `hhi.md` §3.4. |
| B6 correction | Row 5 of Table B27 is ON-avg-traj, -0.4x; marginal 2.8x; Liddell range 4.9-26.0x; alt 5.0x/19.1x, 9.3-45.8x. All match `same_money.md`. |
| B8.1 / B36 | 24.62/0.03 = 820.7 ("about 820"); gas 94x; 58.2, 77.3, 6.6, 26.4; 0.07 deaths a year (one per 14 years). Match `social_licence.md` §2. |
| B8.2 / B37-B38 | Sums 46/43 = +1.07 and -37/36 = -1.03 recomputed; 7 high-power with 0 opposed; 4 with 3 opposed; Wonnarua +/-0.17 correct. |
| B8.3 / B39 | All totals recomputed (7/11/11/14; 8/14/14/17; 9/12/12/17; 8/13/14/16; 9/13/12/17). "3 to 6 points" holds (4, 6, 3, 5-6, 3-4). R3 wins only on fairness x2. |
| B8.4 / B40 | 9.6, 4.8, 4.6, 3.3, 77.7% (sum 100.0); 16.23 by subtraction; C$17.4 m/MW. |
| §8.4 edits | T12/T13 cross-references to B8.1 and B8.3 resolve. Slovic (1987) is in `sources_run6.md` (P1, [TO VERIFY], not opened): "extreme of the dread factor" is in the source note; the "unknown" factor wording is as in the paper. Poll gaps 16-20 and 59 vs 51% match `social_licence.md` §1. Wonnarua: now "no public position located", consistent with B8.2. |
| §8.5 edits | +1.07 / -1.03, "none of seven", "three of the four" all match B37-B38. 78% subtraction matches. |
| §8.3 edit | Pointer to B2.6 correct. |
| §8.6 numbers | 1,100/2,200/3,300 = 20/40/60% x 50,000 m³ x 110 kg/m³ (see M2 for the spec). Lever scores and weight test as above. 130% rule and "federal departments" scope match TBS_SECC (sources.md l.462-465). CGF/BOF tranche 2 "once project milestones are met" matches CGF_BOF_2025. Dual-sourcing (Urenco and Orano) matches OPG_2023_fuel via the brief. |

## Rubric evidence
- **R3.7 / R3.5:** present (levers, sequence, 2027 start against the 2028 approval). Gaps to HD: M1, M2, S1, S5; qualification cost is an admitted gap ("uncosted" is stated, good for R3.8).
- **R1.4:** TBS, CGF/BOF, CNSC are primary but none opened; the 2028 date is secondary (S5). Human open-and-check needed.
- **R2.7:** B6 now states the Ontario sign flip and its placeholders (S8 to tighten); B2.6 gives sensitivity and envelope. Meets the descriptor.
- **RB.5:** B2.6 and B8 supply full working; T16 does not (S9).

Counts: must-fix 2, should-fix 9, OK 11 groups.
