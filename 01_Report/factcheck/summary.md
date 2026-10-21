Rubric coverage: see entries

## Summary

**Counts by status.** Tables A–C have 92 rows. Each row is counted once, under its most serious status. Rows with a substantive problem are usually also unreachable.

| Status | Count | Rows |
|---|---:|---|
| Verified (citation opened and confirmed) | **0** | Network blocked every primary host |
| Unreachable (needs a human check), no other problem found | 21 | A5, A7, A8, A9, A13, A16, A18, A19, A21, A22, A23, A24, A25, B2, B6, B9, B11, B19, S2, S19, S33 |
| Not supported (by the cited or recorded source, or by our own results) | 5 | A1, A17, A20, B13, S43 |
| Source not found (not in sources.md, or reference incomplete) | 17 | A4, A10, A14, A26, B8, B15, S5, S7, S12, S21, S22, S27, S34, S35, S36, S37, S41 |
| Calc or logic OK (re-run matches the text) | 17 | A3, A11, A12, B4, B5, B7, B10, B16, B17, B18, S1, S10, S23, S26, S31, S38, S47 |
| Error (factually or arithmetically wrong) | 8 | B3, B12, S4, S8, S16, S30, S39, S42 |
| Inconsistent (across section, slides and results) | 9 | S3, S9, S15, S20, S28, S32, S40, S44, S45 |
| Overclaim or wording | 12 | A2, A6, A15, B1, B14, S6, S11, S14, S17, S24, S25, S29 |
| Placeholder on slide | 2 | S13, S18 |
| Format (R5.4) | 1 | S46 |
| **Total** | **92** | |

**Blocking issues**
1. **No citation in §8.1, §8.3 or the deck is verified.** Every primary host is blocked from this environment. Victor must open the P1 items in the Human checklist before the examiner can mark anything HD (CLAUDE.md rule 3).
2. **B3:** "No sensitivity case falls below 1,800" is false (mining by company, 1,118). It appears in the §8.3 text and the T3 note.
3. **B15 / S21:** Silex/GLE has no source, and the causal "because s 140A" is unsupported. The §8.3 R4.3 claim and slide 8 depend on it.
4. **B13 / B14:** the UNECE front-end finding is not recorded in sources.md, and "fuel dominates footprint" pre-empts Sam's LCA.
5. **A1:** §8.1's lead sentence ("needs only…") is unsupported and contradicts the section body.
6. **A10:** Appendix B (Senate arithmetic, route scoring, HHI working) is cited but does not exist.
7. **Slides (Thursday):** S8, S42, S30, S39, S16, S4, S20/S44, S28, S9, and the placeholders S13 and S18.

---

## Rubric IDs: what this check produced and what is still missing

- **R1.4.** Produced: every citation traced to sources.md, with hosts recorded. Missing: zero primaries verified (network); news sources still carry claims A1, A6, A8, A9, A24 and S12.
- **R2.1, R3.8, RB.5.** Produced: all five scripts re-run, outputs byte-identical, every number in §8.1, §8.3 and slides 4, 9, 13 and 14 traced. Missing: `verified: true` on the inputs; Appendix B not written; B3 to fix.
- **R2.6, R3.6.** Produced: S43 (the verdict contradicts `same_money.md`) and A10 (route scoring has no appendix). Missing: the MCDA.
- **R2.7, RB.6.** Produced: benchmark checks (section E); the 315 MWe gap in the sensitivity. Missing: Sam's LCA value, which can't be benchmarked yet.
- **R3.2, R3.4, R3.5, R3.7.** Produced: per-ID evidence gaps (section G). Missing: the fixes listed against A1, A2, A4, A6 and B12.
- **R4.3.** Produced: shows both legs of the §8.3 connection are unsupported (B13, B15). Missing: sources.
- **R5.2, R5.4, presentation rubric.** Produced: slide errors, placeholders, missing images, uneven speaker time, reference-list defects. Missing: the team's edits.

*I did not edit `rubric-tracker.md`; the examiner owns it. No item can be marked "Fact-checked" yet, because no primary source has been opened.*

---

