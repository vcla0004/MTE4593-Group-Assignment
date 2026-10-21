Rubric coverage: see entries

## Whole-project audit (21/10)

Examiner, Wed 21/10/2026. Scope: every output in the repo.
- Sections: §6 v2, §8.1 v2.1, §8.3 v2.1, Appendices A v2, B v1 and C v2.
- The deck: 15 slides and their `<aside>` notes, checked against `00_Brief/presentation_rubric_text.txt`.
- `factcheck.md` A–H, this file, `rubric-tracker.md`, `03_LCA_Calculations/results/*`, `02_Research/briefs/*`, and `plan.md` §3, §4, §6 and §7.

**Decisions applied.** D1 stays C1. My §6-review recommendation is now the default framing: **low-clinker self-consolidating infill for the DPSC modules and forebay shafts of Units 2–4, with LC3 as the target binder and a qualified slag blend as the fallback, specified only if schedule-neutral.** Victor can overrule it. It still has to go into the Meeting 3 minutes, because `05_Meetings/` has no such file.

**Teammates.** Sam is absent; Victor owns his sections (CLAUDE.md, 21/10). **Leroy has delivered nothing in the repo.** There is no §4, §5 or §10 file, no TRL or timeline table, no patent log, no BWRX-300 plant or fuel data, and the master .docx is still headings only (README). His plan deadlines of Tue 21:00 and Wed 12:00 have both passed.

**Verification.** Not one primary has been opened (factcheck A–C: 0 of 92 verified; H: 0 of 79). **Appendix B v1 has never been fact-checked.** Under CLAUDE.md rule 3, every ID is Partial at most.

### 1. Estimated mark out of 25

| Criterion (weight) | Now: grade, marks | Queue completed, inputs unverified, no Granta | Queue completed + P1 primaries opened + Granta run |
|---|---|---|---|
| R1 Research coverage (5%) | P, about 2.4 | D, about 3.6 | D (high), about 3.8 |
| R2 Technical analysis (8%) | P, about 4.4 (§6 is D quality, but §7 and the economic benefit are absent) | D (high), about 6.2 | HD (low), about 6.6 |
| R3 Non-technical (6%) | Unsatisfactory–P, about 2.4 (2 of 6 §8 subsections; no §9) | D, about 4.5 | HD (low), about 4.8 |
| R4 Originality (3%) | P, about 1.5 (no §4.3) | D, about 2.2 | D (high), about 2.3 |
| R5 Presentation (3%) | Unsatisfactory, about 1.2 (no assembled report, no reference list, 210 markers) | C–D, about 2.1 | D, about 2.25 |
| **Total** | **about 11.5–12 / 25 (fail)** | **about 18–18.5 / 25 (D)** | **about 19.5–20 / 25 (borderline HD)** |

The jump from 12 to 18 comes almost entirely from **writing the missing sections**, not from polishing the existing ones. About 13.5 of 18.25 planned text pages are still unwritten, and the freeze is Thu 21:00.

### 2. Each criterion's biggest gap (HD phrase being missed)

| Criterion | HD phrase missed | Evidence | What closes it (queue job) |
|---|---|---|---|
| **R2 (8%)** | "Calculations of efficiencies, resource usage and potential environmental or **economic benefits** are **appropriate to the scale of the proposal**" | §6 sizes C1 well. But the analysis that carries the thesis (**what one BWRX-300 displaces at Darlington vs Liddell, the carbon value of schedule, and the same money on firmed renewables**) exists only in `results/displacement.md`, `schedule_value.md` and `same_money.md`, and is not in the report. C1's economic benefit is a TODO. §8.3 still ignores the 196 t U and 138 tSWU a year that `lca_baseline.md` already gives. `parameters_run1.yaml` still uses the UNECE placeholder (5.75), not our 4.2 | Q2 (re-base, carbon value), Q4 (§7 + App B4–B6), Q3/Q7 (§8.3 sizing) |
| **R3 (6%)** | "Provides **strong evaluation and comparison of solutions** based on relevant non-technical objectives"; "**Comprehensive** and detailed discussion of the major **economic**, political, **social**… factors" | Only §8.1 and §8.3 exist. §8.2 (economics), §8.4 (social), §8.5 (stakeholders) and §8.6 (implementation) are missing. The only scored comparison is App B3 (three Australian legal routes), which is in an appendix. The §9 MCDA (status quo vs SMR vs SMR + C1 vs firmed renewables) does not exist | Runs 5–6 → Q6; Q10 (§8.6); Q12 → Q14 (§9 MCDA) |
| **R1 (5%)** | "**Comprehensive coverage of all significant and relevant aspects** of the topic. **The key problems and challenges are clearly defined**" | No §3 barriers section. No technology, projects or timescales (§4.1–4.2, Leroy). No materials extraction to end-of-life (§5, Leroy). No patents, although the brief explicitly asks for them | Q10 (§3); G1 → Q5 → Q9 (Leroy's sections or fallback) |
| **R4 (3%)** | "Provides **new feasible ideas or connections** that are not immediately apparent from the chosen technology" | §4.3 is not written, so the initiative is stated only on slide 5. The best connection (1.4–15 days of delay cancel a unit's saving) sits in §6.3 finding 5, with no working in Appendix B. The Silex connection is unsourced, and so is the slag-supply case for LC3 over slag (L18) | Q10 (§4.3), Q4 (App B5), Q3 (Silex, slag sources) |
| **R5 (3%)** | "Report is **appropriately structured and concise**. **Consistent referencing**" | No assembled document, abstract, §1, §2, §11 or reference list. There are two bibliographies to merge, 210 [TODO]/[TO VERIFY] markers, table numbers that clash (T7 in §8.1, T8–T9 in §6, T1–T6 planned), and the 20/10 caption fixes in §8.1/§8.3 are unapplied | Q16, Q19 |

### 3. Report sections against the `plan.md` §3 outline

Status key: **Missing** = no draft. **Drafted** = a draft exists but has not been reviewed in its current version. **Reviewed** = the examiner has marked the current version (fixes may still be open). No section is Done: Done requires HD on every ID plus fact-checked evidence.

| § | Section (budget, pages) | Owner | Status | Note / next job |
|---|---|---|---|---|
| — | Title page, abstract, table of contents | Shared (writer) | Missing | Q16. Title page needs Victor's and Sam's student IDs and Sam's surname |
| 1 | Introduction (0.75) | Shared | Missing | Q16 |
| 2 | Methods and data (1.0) | Shared: Victor (LCA, displacement, HHI, MCDA); **Leroy** (literature and patent search) | Missing | Q16. The search-log paragraph **depends on Leroy** (fallback: Q5's Appendix E log) |
| 3 | Barriers (1.25) | Victor (Leroy feeds time and TRL) | Missing | Q10. Time-to-deploy barrier **depends on Leroy** (fallback: Q5) |
| 4.1 | Technology, projects and patents (1.25) | **Leroy** | Missing | **Depends on Leroy.** Fallback G1 → Q5 → Q9 |
| 4.2 | The BWRX-300 at Darlington (0.5) | **Leroy** | Missing | **Depends on Leroy.** Fallback G1 → Q5 → Q9 |
| 4.3 | The initiative (0.75) | Victor (took over Sam's technical part) | Missing | Q10, default D1 wording |
| 5 | Materials, extraction to end-of-life (1.5) | **Leroy** (lead) | Missing | **Depends on Leroy.** Fallback G1 → Q5 → Q9 |
| 6 | LCA and eco-audit (3.5) | Victor (took over Sam's) | Reviewed (v2); v3 writer pass running | Q1 → Q8 for the script-dependent fixes |
| 7 | Carbon avoided: Ontario vs Liddell, schedule, same money (1.75) | Victor | Missing (results and brief exist) | Q2 → Q4 |
| 8.1 | Law, regulation and licensing (0.6) | Victor | Reviewed (v2); **20/10 fixes not applied** (file is v2.1, pointers only) | Q7 |
| 8.2 | Economics, finance, market barriers (0.85) | Victor | Missing (run 5 running) | Q6 |
| 8.3 | Supply concentration and geopolitics (0.5) | Victor | Reviewed (v2); **20/10 fixes not applied** | Q3 → Q7 |
| 8.4 | Social licence (0.6) | Victor | Missing (run 6 running) | Q6 |
| 8.5 | Stakeholders and money flows (0.35 + F8) | Victor | Missing (run 6 running) | Q6 |
| 8.6 | Implementation pathway (0.35) | Victor | Missing (route-to-practice brief §5–6 ready) | Q10 |
| 9 | TBL evaluation and MCDA (1.25) | Victor (lead); scores from Sam and **Leroy** | Missing | Q12 → Q14. TRL and timing scores **depend on Leroy** (fallback: Q5 table) |
| 10 | Future material properties and processes (0.75) | **Leroy** (lead) | Missing | **Depends on Leroy.** Fallback G1 → Q5 → Q9 |
| 11 | Conclusions and recommendations (0.75) | Shared | Missing | Q16 |
| — | References | Shared; **Leroy** formats | Missing | Q16 (writer merges `sources.md` and `sources_lca.md`) |
| A | LCA inventory and calculations | Victor | Reviewed (v2) | Q8 (L65, ENR, Granta or cut) |
| B | Policy, supply, displacement, schedule, same money, MCDA working | Victor | **Drafted (v1, B1–B3 only; never fact-checked or reviewed)** | Q11 fact-check; Q4 adds B4–B6; Q14 adds B7 (MCDA) |
| C | Sensitivity | Victor | Reviewed (v2) | Q8 (conversion-heat alternative row) |
| D | Assumptions table | Shared (generated) | Missing | Q16a |
| E | Literature and patent search log | **Leroy** | Missing | **Depends on Leroy.** Fallback: Q5 |
| — | Master .docx assembly | **Leroy** (integrator, D7) | Missing (headings only) | **Depends on Leroy.** Fallback: Q19 (coordinator, pandoc) |

**Leroy fallback (gate G1, Wed 18:00).** If no Leroy file is in `01_Report/sections/` (or sent to Victor) by Wed 18:00, I recommend Victor take over Leroy's green sections on the same terms as Sam's. That means new files labelled "drafted for Leroy; Leroy may reclaim", Leroy's own files left intact, and the decision recorded in CLAUDE.md and the Meeting 3 minutes. The scope is:
- analyst run 8 (Q5) for evidence;
- the writer (Q9) for §4.1, §4.2, §5 and §10;
- Q5's Appendix E for the search log;
- the coordinator (Q19) for assembly.

The patent search is the weakest part of the fallback. If `patents.google.com` is blocked from the agents' sessions, the log records the attempt, §4.1 carries one hedged paragraph, and R1.4 loses a little. **Victor should message Leroy now**, so that the 18:00 cut-off comes as no surprise to him. This is a recommendation, not a decision: only Victor and the team can reassign Leroy's work.

### 4. The deck against the presentation rubric (due Thu 22/10; submit by 15:00 per D8)

Fixed since the 20/10 fact-check: S8, S9 (2030, OEB), S16, S28/S45 (Q5 now 2040, about 5 years), S30, S39, S42 (5× labelled "at GenCost costs", 2× on Darlington capital), S43 (Environmental now "Mixed"), L67, L68, L70 ("cross-check pending"), L71, L72, L74, the placeholders S13/S18, and Aaron removed.

**Still open, by rubric criterion:**

**Visual communication (2%).** HD needs "Effective use of figures, images and other visual material" and slides "without unnecessary text or clutter".
- There is **no image or figure on any slide** (`<img>`/`<svg>` count = 0). F2 (stage breakdown), F3 (tornado) and F5 (benchmarks) exist as PNGs and should go on slides 7 and 8. A credited BWRX-300 or Darlington photo belongs on slide 3 or 4.
- Slide 13 should be an HHI bar chart, not two big numbers and a sentence.
- Slide 14 is a text table: replace it with the §9 MCDA chart once Q12 exists.

**Teamwork and questions (1%).** HD needs "All members contribute effectively and respond confidently and thoughtfully to questions".
- Sam is absent, and slides 6–8 say "Victor or Leroy". If Leroy is also absent, **one person presents 15 minutes**, which caps this criterion at about P whatever the content. Decide the speaker plan by Thu 12:00 and update `04_Presentation/README.md` (it still lists Sam for slides 6–8).
- **Q2 in the verdict notes still says LC3 "must be qualified under Canada's CSA N287 standards"** (S44). That contradicts §8.1 and slides 5 and 8 (AISC N690 / CSA N291). A wrong answer under questioning costs marks here.

**Engagement (2%).** Timing is about 14.25 minutes and acceptable. The notes are long; trim each to what is said aloud.

**Content and consistency defects** (they cost credibility in Q&A and must match the report):

| Slide | Issue | Fix |
|---|---|---|
| 1 | Sam has no surname (S1) | Add it |
| 3 | GEH (2021) source not in `sources.md` (S5); 300 vs 315 MWe unresolved (S3) | Add the entry; keep 300 and say "about" until the OEB filing is opened |
| 4 | Title "the first SMR in the G7" is unsourced (S7) | "the first grid-scale SMR licensed for construction in the G7", with source, or drop it |
| 5 | Title does not carry the D1 default framing | "Low-clinker infill for Darlington Units 2–4: LC3 target, slag fallback, only if schedule-neutral" |
| 7 | Notes claim "within the same target structures LC3 saves more than steel would". This rests on my **unscripted** 0.57 kt check (§6 review point 4) | Script it (Q1) and quote it, or cut the clause. Also "1,390 to 2,150" (L75) and "nuclear bars widened to be visible" (L76) |
| 8 | Silex unsourced (B15); "reported to be nuclear's largest emitter" (L77) | Source by Thu 12:00 or cut the card. Use "the fuel front end, about two-thirds of our LCA total (§6)" |
| 9 | Notes "adds about 6 g"; the source line credits UNECE for the nuclear value (L79) | "about 4 g (our model)"; re-base after Q2 |
| 11 | "even with Darlington's real costs included" unverified; NuScale rests on Power Engineering (trade press, S34); the notes' A$387–641 is the 2023-24 edition while the slide cites 2025-26 | Cite the GenCost 2025-26 PDF and UAMPS/DOE; one edition throughout |
| 12 | Lowy 2024 and OWID 24.6 not in `sources.md` (S36, S37); no First Nations evidence | Take the numbers from run 6; check for a 2025/2026 Lowy result |
| 13 | 28% edition undecided (B9); "the largest share" unverified | Team decision; same wording as §8.3 |
| 14 | Ratings are "preliminary judgement"; Q2 wrong (above) | Replace with the §9 MCDA result (Q12/Q14) before 15:00, or keep "preliminary" on-slide |
| 15 | Four news or trade sources; "Ontario Government 2024" no longer cited; missing CNSC 2025, Government of Ontario 2025, OPG 2025, TAF 2025, CER, CGF/BOF 2025, US NRC (GLE), Lowy, OWID; not alphabetical; no URLs (S46) | Rebuild from `sources.md` in the style-guide Harvard form |

### 5. Fact-checker findings still unresolved (summary; full lists below)

- **§8.1 and §8.3:** every item in the 20/10 "Still unresolved" tables below. In addition, none of the 20/10 examiner fixes has been applied: both files are v2.1, which only changed the Appendix B pointers.
- **§6 and Appendices A and C:** every item in the 21/10 "Still unresolved" table below. The running writer pass covers the text items. L31, L64, L66, E1, the like-for-like steel row and the conversion-heat test need the lca-analyst (Q1).
- **Appendix B:** never fact-checked (Q11). It inherits A4, A8, A9, A20, A22, A24, A26, B2, B9 and B19 by citation.
- **Deck:** see section 4.
- **Cross-cutting:** 0 primaries verified. This is the single largest risk to every R1.4, R2.x and R3.8 mark and to the HD ceiling.

### 6. Feedback to teammates (by name; no edits made to their work)

- **Leroy:** you own RB.3, RB.4 and RB.7 and most of R1.1. That is §4.1, §4.2, §5 and §10 (4.0 pages), Appendix E (patent log), the master .docx, slides 1–5 and the BWRX-300 plant and fuel data. Nothing is in the repo. Send whatever you have by **Wed 18:00**, even as rough notes; after that the fallback in section 3 starts. Most useful first: the project, timeline and TRL table (Darlington U1–U4, Clinch River, Linglong One, NuScale/UAMPS); net MWe (300 vs 315); capacity factor; burnup and reload data; and 5–10 logged patents. If you are presenting on Thursday, confirm by Thu 12:00.
- **Sam:** nothing new is required. Your `Assumptions.docx` and `Accounting.xlsx` are untouched. The corrected versions (`Accounting_corrected.csv`, Appendix A4) are new files. If you return before Thu 21:00, the fastest high-value job is the **Granta Eco Audit cross-check** (`granta_inputs.md`, under 1 hour).
- **Victor:** see section 7 and the human jobs H1–H6 in `plan.md` §7.

### 7. Top five priorities (whole project)

| # | What | Owner | By | IDs |
|---|---|---|---|---|
| 1 | **Write the missing R3 core**: §8.2 and §8.4–8.5 (from runs 5–6), §8.6, then the §9 MCDA (run 9) with the deck's slide 14 synced to it | Victor (analyst runs 5, 6, 9; writer Q6, Q10, Q14) | Thu 14:00 | R3.1, R3.3–R3.8, RB.8, R4.4 |
| 2 | **Put §7 in the report**: re-base on 4.2 g/kWh, add C1's carbon value, draft §7 and Appendix B4–B6. This is the analysis that carries the thesis and most of R2.3/R4.3 | Victor (analyst Q2; writer Q4) | Thu 02:00 | R2.1, R2.3, R2.6, R2.7, R4.3, R3.1, RB.5 |
| 3 | **Leroy gate at Wed 18:00**: get his drafts, or trigger the fallback (Q5 → Q9) for §4.1, §4.2, §5, §10 and Appendix E | Victor (decision); analyst run 8; writer | Gate Wed 18:00; drafts Thu 11:00 | RB.3, RB.4, RB.7, R1.1, R1.4, R4.2 |
| 4 | **Open the P1 primaries** (the factcheck human checklist, LCA order first: Gibon 2023, Parker 2016, EDF 2024, the OPG basemat story or NEDO-33926, the CAC EPD, UNECE 2021, IPCC AR5; then EPBC s 140A, ARPANS s 10, WNA tables, the OEB filing), set `verified`, re-run. Run Granta or cut it | Victor (human) | Thu 12:00 | R1.4, R2.1, R2.2, R2.7, R3.8, RB.6; the HD ceiling |
| 5 | **Frame and finish**: §3 barriers, §4.3 initiative (D1 default), §2, §1, §11, abstract, one merged reference list, assembly with markers stripped and tables renumbered | Victor (writer Q10, Q16; coordinator Q19) | Thu 21:00 | R1.2, RB.1, RB.2, R4.1, R2.4, R5.1–R5.5 |

### 8. Rubric checklist (status after this audit; "done" needs verified HD evidence, so nothing is done)

- **Done:** none.
- **Partial (28):** R1.1, R1.2, R1.3, R1.4, R2.1–R2.7, R3.2, R3.4, R3.5, R3.6, R3.7, R3.8, R4.2, R4.3, R4.4, R5.1–R5.5, RB.2, RB.5, RB.6.
- **Missing (9):** R1.5 (judged at the freeze), R3.1, R3.3, R4.1, RB.1, RB.3, RB.4, RB.7, RB.8.
- **Change since the last review:**
  - R3.6 moves from Missing to Partial, because App B3 now holds a scored comparison with a weight test, in the appendix only.
  - R2.4 and RB.5 gain App B1–B3.
  - R2.2 is unchanged.
  - No ID moves up a band.

### 9. What this audit produced, and what is still missing (per ID)

- **R1.1–R1.4, RB.2, RB.3, RB.4, RB.7.**
  - Produced: section-by-section status with owners; the Leroy dependency and its fallback (gate G1, Q5, Q9).
  - Missing: §3, §4, §5, §10; the patent log; verified primaries.
- **R2.1–R2.7, RB.5, RB.6.**
  - Produced: the finding that §7 is the largest unclaimed R2 mark, because its results exist but the text does not; the stale 5.75 g/kWh placeholder; the unapplied §8.3 sizing; the unscripted steel check now quoted on slide 7.
  - Missing: Q1, Q2, Q4 and Q8 outputs; verification; Granta.
- **R3.1–R3.8, RB.8.**
  - Produced: R3.6 to Partial (App B3); a queue for §8.2 and §8.4–§9.
  - Missing: all of those drafts.
- **R4.1–R4.4, RB.1.**
  - Produced: the D1 default applied to the tracker, the deck and the queue.
  - Missing: §4.3, the App B5 working, and the Silex and slag sources.
- **R5.1–R5.5, R1.5.**
  - Produced: the assembly checklist (markers, numbering, bibliography merge) and the deck's visual and teamwork gaps.
  - Missing: the assembled report and the reference list.
- **Presentation rubric.**
  - Produced: open defects by criterion, with fixes.
  - Missing: images and figures on the slides, the speaker plan, Q2.

---

