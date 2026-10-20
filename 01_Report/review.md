Rubric coverage: R1.2, R1.3, R1.4, R2.1, R2.3, R2.4, R2.6, R2.7, R3.2, R3.4, R3.5, R3.6, R3.7, R3.8, R4.3, R5.1, R5.2, R5.3, R5.4, R5.5, RB.2, RB.5

# Review

The examiner replaces this file at each review. Unresolved items below must carry over.

## Issues found in existing work (first logged 20/10/2026; carried over 20/10/2026)

### Fixed
- **Shared report draft (`MTE4593 Report.docx`):** removed the scandium figure caption (Figure 2) and the 21 scandium references left over from another project. The removed text is in `removed-scandium-content.txt` in case anyone needs it.
- **Item 7 (previous review): Aaron has been removed from the title slide** (factcheck.md S1, 20/10). Open residue: Sam's surname is missing from the title slide.

### For Sam (LCA files are Sam's, so not edited). Still open; no change seen in `README.md` or `factcheck.md`
1. `Assumptions.docx`, Site Choice: the Darlington project is in **Clarington, Ontario** (east of Toronto), not Ottawa.
2. `Assumptions.docx`, Manufacturing: **4,127.29 m³ isn't the volume bored by the tunnel boring machine.** It is the concrete (4,000 m³) plus the rebar (127.39 m³). Bored volume = tunnel length × cross-sectional area, from OPG or CNSC documents.
3. `Accounting.xlsx`: the concrete and steel rows are on the **"Nuclear Fuel LCA"** sheet. They belong on **"SMR Parts LCA"** (construction).
4. `Accounting.xlsx`: 9.6 million kg of concrete and 1,000 t of steel are **one construction milestone (the forebay shaft) only**, not the whole plant. Label them as partial, and source whole-plant quantities (e.g. GE Vernova Hitachi's UK design-assessment documents, or TVA's Clinch River construction permit application to the NRC). The deck repeats this error (slide 6, factcheck S17).

### For the team (shared notes). Still open
5. `SMR Research Notes.docx`: "Zero risk of meltdown" and "carbon neutral fuel source" overclaim. Use sourced wording (e.g. "passive safety reduces the risk of…", "low life-cycle emissions of X g CO₂e/kWh").
6. **Victor:** no "Meeting 3 20_10_26" minutes exist in `05_Meetings/` (plan D11). Record the postponed deck deadline (Thu 22 Oct), the report deadline (Fri 23 Oct), decision D1 (C1 plus Liddell, decided by Victor per plan §8) and the owners. Without the minutes, D1 is not a recorded team decision.

---

## Review of §8.1 and §8.3 (20/10)

Files reviewed: `01_Report/sections/8.1-law-regulation-licensing.md` (v2) and `01_Report/sections/8.3-supply-concentration.md` (v2). The fact-check (`factcheck.md`, 20/10) was run on **v1**. I re-checked each of its findings against v2 below.

Owner: **Victor** (yellow). The writer agent drafted both sections. The feedback is addressed to Victor, who owns the text.

### Verification caveat (CLAUDE.md rule 3)
**No primary source behind either section has been opened.** The fact-checker could not reach a single primary host (factcheck.md, "Method and access"), and every input in `parameters_run2.yaml` and `parameters_run3.yaml` is `verified: false`. Under rule 3, **no ID served by these sections can be marked HD**, however good the draft is. The tracker therefore shows Partial at most. Two grades are given below:
- **If verified:** what the section would earn if every cited fact checks out as drafted.
- **As it stands:** what a marker would give today. The [TO VERIFY] markers, news sources carrying claims and the missing Appendix B count against it.

The scripts are a strength. All re-run outputs are byte-identical, and every number in both sections matches `hhi.md`, `hhi_summary.csv` and `law_timelines.csv`.

### Grades per official criterion (scope: what these two sections contribute)

| Criterion | If verified | As it stands | HD phrase being missed | Evidence |
|---|---|---|---|---|
| **R3 Non-technical (6%)** | **D** | **C** | "Provides **strong evaluation and comparison of solutions** based on relevant non-technical objectives"; "Considers **implementation issues and non-technical solutions**… **supported by evidence**" | Political and legal coverage is detailed and quantified (Senate 32 vs 39; T7; HHI by stage). But the only scored comparisons (routes A/B/C; supply options; levers L1–L5) are **outside the report text**: the route scoring sits in the "Note for §9", the supply options are only in the brief, and L1–L5 are deferred to §8.6, which does not exist. Each section offers one mitigation (mock-up qualification; dual sourcing) and no comparison. "Supported by evidence" fails today: 0 primaries are verified, and ABC (2026), the Canberra Times (2025), the Newcastle Herald (2024) and ANS (2026) still carry claims |
| **R2 Technical (8%)** | **D** | **C** | "Calculations… **appropriate to the scale of the proposal**"; "**Methods are clearly explained and easy to follow**"; "Uncertainties… **realistically estimated and discussed**" | T3 is genuine quantitative analysis, with reproducible sensitivity ranges and stated limits. But (a) the HHI is a world-market number that is never sized to Darlington's own fuel demand (SWU/yr, tU/yr against Urenco USA and Orano capacity); (b) the method lives only in `hhi.md`, and §2 and Appendix B are unwritten; (c) the classification depends on the threshold, and the text doesn't say so: under the 2010 guidelines, mining (2,341) and conversion (2,111) are only "moderately concentrated" (`hhi.md` §2). The lead's "highly concentrated" therefore holds only on the 2023 scale |
| **R1 Research (5%)** | **D** | **C** | "**synthesis** of a wide range of highly relevant sources"; R1.3 "**disagreements between sources explained**"; R1.4 "No reliance on news" | Strong source mix (Acts, CNSC, NRC–CNSC joint report, GEH topical report, DOJ/FTC, WNA, Red Book, PL 118-62). But the three source disagreements already in the briefs are absent from the text: Red Book 2024 (28%) vs 2026 (29%/27%); WNA vs CRAI Rosatom capacity; Coalition 2035 vs CSIRO 2040. Silex/GLE has no source at all |
| **R4 Originality (3%)** | **C** (D once Silex is sourced) | **P–C** | "Provides **new feasible ideas or connections** that are not immediately apparent" | The one non-obvious connection is that s 140A keeps an Australian enrichment technology offshore. It is **unsourced** (TODO, factcheck B15), so it can't count even under the "if verified" condition. The second leg (front end = emissions hotspot) was correctly cut. What remains: "price risk at Darlington, sovereign risk in Australia" and "C1 does not reduce fuel risk". Both are sound but modest |
| **R5 Presentation (3%)** | **D** | **C** | "**Consistent referencing**"; "appropriately structured and **concise**" | Each paragraph leads with its point, and both are within budget (about 0.6 and 0.5 pages). Defects: the tables have a placeholder line *and* a caption, and the caption sits below the table; news-outlet author forms; "Parliament of New South Wales, 2025–26" is not a Harvard year; the Constitution is not in `sources.md`; there is a duplicate APH entry (B11); and CNSC 2026a/2026b are not yet disambiguated |

**Estimated contribution to the 25 marks** (weighted by each criterion's share that these 1.1 pages can carry):
- **If verified, as drafted:** about **3.5 / 25**.
- **With the fixes below:** about **4.0 / 25**, close to the ceiling for this scope.
- **As it stands:** about **2.5–3 / 25**.

**Whole report:** not markable yet. Only 2 of about 20 sections exist. Submitted as is, it would be **Unsatisfactory (< 12.5 / 25)**.

### Fact-checker findings: status in v2

**Resolved in v2 (wording now matches the evidence):** A1 (lead), A2, A3, A4 (labelled as an assumption), A6, A11, A12, A13, A14 (cut), A15, A17 (softened), A20, A21, A23, A25, B1, B3/B18, B4, B6, B12, B13/B14 (cut), B17 (flagged).

**Still unresolved: §8.1**

| # | Issue | Owner | Fix |
|---|---|---|---|
| A1 (residual) | The 2028 Units 2–4 milestone still rests on ANS (trade press). The type of approval is unknown | Victor | Open OPG's OEB filing D2-4-1 (factcheck P1). Cite it and name the approval type |
| A5 | No Labor statement from 2026; Bowen's date is TO VERIFY | Victor | Add a dated 2025–26 ministerial statement |
| A4 (residual) | One Nation's position has a source in the law brief (ABC, 31 Aug 2026) that is not in `sources.md` or the text | Analyst → Victor | Add the entry and cite it. Babet stays a stated assumption |
| A7 | ARPANS s 13 ("controlled person") is not cited | Victor | Cite s 13 alongside ARPANSA (n.d.) |
| A8 | ABC (2024) for route A (now in the §9 note) | Victor | Replace with the Coalition's 19 June 2024 release before §9 uses it |
| A9 | T7's "may face a High Court challenge" rests on the Canberra Times | Victor | Cite Constitution s 109 plus Twomey/Partlett as quoted, with the date verified |
| A10 | Appendix B does not exist; it is cited three times | Victor (writer) | Write Appendix B now: `law_timelines.csv` rows and the route table. The data exist, so this is a cheap fix |
| A16 | Whether CSIRO's "2040 at the earliest" covers SMRs; which GenCost edition to cite | Victor | Open the GenCost 2023-24 PDF (P1) and quote it |
| A18, A19 | The wording of EPBC s 140A and ARPANS s 10, and the effect of the 2025 EPBC reform | Victor | P1 human check (legislation.gov.au) |
| A22 | The NSW repeal bill's status and its lapse date | Victor | Latest LA notice paper |
| A24 | AGL's position and battery status rest on the Newcastle Herald | Victor | AGL ASX release |
| A26 | The Constitution is not in `sources.md` | Analyst | Add the entry |

**Still unresolved: §8.3**

| # | Issue | Owner | Fix |
|---|---|---|---|
| B2 | DOJ/FTC "> 1,800" wording, §2.1 | Victor | P1 human check |
| B8 | OPG fuel-chain claim: primary not identified | Victor | Find the OPG 2023 release, or cite Power Engineering openly as secondary |
| B9 | Red Book edition (28% vs 29%/27%) | **Team decision** (Victor proposes) | Pick one edition and cost category. Use it in §8.3, slide 13 and `hhi.md` |
| B11 | Duplicate APH entries in `sources.md` | Analyst | Merge them under the page's own title |
| B15 | Silex/GLE: no source | Victor / analyst | Silex ASX release plus the NRC Paducah docket by **Thu 12:00**, or cut the sentence |
| B19 | WNA page years | Leroy (references) | Confirm, and add suffixes if two share a year |

**Deck items that block Thursday (from the fact-check; listed so they aren't lost)**

| Owner | Slides and fixes |
|---|---|
| Victor | S8 (Ontario approved Unit 1, not 4 units); S42 (5× is Method B, and Darlington's own capital gives about 2×); S43 ("Environmental: Strong" contradicts `same_money.md`); S30 (NSW s 8(3) exceptions); S39 (3,600 is not the duopoly case); S28/S45 (2040, not "late 2030s") |
| Sam | S13, S18 (placeholders); S16 ("ash-concrete" should be LC3) |
| Leroy | S4 ("more than half as much" inverts the slide); S9 (end-2029 vs 2030 start); S20/S44 (CSA N287 should be the GEH topical report / AISC N690) |

### §8.1 Law, regulation and licensing: feedback for Victor, paragraph by paragraph

1. **Lead.** Good: it now states the contrast and matches the body. One gap: "accepted as a design change before Units 2–4 are approved" is never explained. The reader doesn't learn that the licence to construct covers **one** unit, so Units 2–4 need a licence amendment or a new licence with a hearing (route brief §3, an inference to confirm with the CNSC).
   - **Fix:** add one sentence to the Canada paragraph: "The licence to construct covers one unit; Units 2–4 need a further Commission authorisation, and C1 would be reviewed inside it." [R3.4]
2. **"Australia."** The arithmetic is right, but the robustness point is left out. `law_timelines.csv` shows that **even with every other crossbencher the bloc reaches only 36**, 3 short.
   - **Fix:** add "(36 even with every other crossbencher)". This turns an assumption-dependent claim into one that holds whatever One Nation and Babet do. That is the "realistically estimated" behaviour R2.7 rewards. [R3.8, R2.7]
   - **Fix:** state the date of the Senate composition ("as at 14 May 2026").
   - The ARPANSA/NSW sentences stop before the point. Say what follows: **a privately owned SMR at Liddell would remain a criminal offence under NSW s 8 even after federal repeal**. Only a Commonwealth-owned operator could fit the s 8(3) exemption, and whether a *power* reactor would is [TO VERIFY]. That is why route A exists. Without this sentence the s 8(3) detail is just trivia. [R3.5, R3.2]
3. **"Canada."** Two missed opportunities that are already in the evidence:
   - **Benchmark the 29 months.** CNSC REGDOC-3.5.1 gives an expected 32 months for a Class IA licence to construct, so OPG was about 3 months faster (`law_timelines.csv`, `ltc_vs_cnsc_expected_months` = −2.9; `CNSC_REGDOC_3_5_1` is in `sources.md`). A number against a norm is evaluation, not description. [R3.8, R1.3]
   - **Say what governs the infill.** The section never names the governing code. The route brief establishes that the DP-SC infill is governed by GEH NEDO-33926 (self-consolidating concrete, strength per draft AISC N690), not CSA N287. The deck says N287 on three slides (S15, S20, S44).
     - **Fix:** one sentence naming NEDO-33926 / AISC N690 as the governing specification. Then say plainly that whether §6.2.1 limits cement type is **not yet known** [TO VERIFY]. That unknown is the real licensing risk for C1. [R3.4, R2.6]
4. **"Translation to practice."** This paragraph needs a number, and it has none. The route brief puts the critical path (mix development → mock-up → design-change acceptance) at about **18–24 months**, which means work must start in **2027** to meet a 2028 approval (an assumption; label it). `schedule_value.md` gives the CO₂e cost of each month of delay. Quote one figure, so "schedule-neutral" becomes a tested condition, not an adjective. [R3.7, R3.8, R4.4]
   - **R1.3:** "treats CSIRO's 2040 as optimistic" should set it against the Coalition's 2024 claim of first SMR power by 2035 (law brief §8; cite the party release). That is the plan's named source disagreement, and it costs one clause.
   - **R3.7:** the ANNPSR precedent (a new naval regulator operating about two years after its Act; `DefenceMin_2025_ANNPSR` is in `sources.md`) is the only evidence that the regulator step is achievable. Add it to the "independent regulator early" sentence.
5. **Table T7.** A good table, and it earns R5.2 once tidied up.
   - Delete the bracketed placeholder line, and put the caption **above** the table in the style-guide form ("Table N. …" then "Source: …").
   - The "Site" row rests entirely on the Newcastle Herald. A news source carrying a veto claim is exactly what R1.4 penalises.
   - Add a "Veto holder" emphasis or a final row summarising "earliest legal start: none in this Parliament". The table currently ends without its conclusion.
6. **"Note for §9."** This is the best R3.6 material in either section, and it is not in the report. Don't paste it into §8.1 (page budget). It must appear as a **scored table in §9 or Appendix B**, labelled "our qualitative judgement", with the weight test. Until then R3.6 stays Missing.

### §8.3 Supply concentration and geopolitics: feedback for Victor, paragraph by paragraph

1. **Lead.**
   - "*Its* Herfindahl–Hirschman index" has no singular antecedent; use "Each stage's HHI".
   - More importantly, the claim is threshold-dependent and the text hides it. Add: "on the 2023 guidelines; under the 2010 guidelines only enrichment (3,009) is highly concentrated, while mining and conversion are moderately concentrated". Also add one clause saying the merger thresholds are used **as a scale for supply risk, not as a legal test** (`hhi.md` §1). §2 isn't written, so for now this is the only place the caveat can go. [R2.7, R2.6, R2.4]
   - "Price risk vs sovereign risk" is a good framing. Keep it.
2. **"Sanctions make it worse."** Correct and quantified, and the mining-by-company sentence is now the best synthesis point in the section. Two additions:
   - **Russia's 4.5% of mining understates its exposure.** Kazakhstan (38.6%) includes Rosatom's Uranium One joint ventures, and Kazakh exports transit Russia (`hhi.md` §5; supply brief gaps 3–4). One sourced clause, or one stated limitation, is needed. Otherwise a marker who knows the industry will read the mining row as naïve. [R3.2, R2.7]
   - **Source disagreement (R1.3):** WNA gives Rosatom 29,133 kSWU; CRAI (2025) gives 26,200 (supply brief). **Analyst:** add a CRAI row to `hhi.py` and report Russia's share as a range. One sentence in the text, with the working in Appendix B.
3. **"Darlington and Liddell compared."**
   - "EPBC s 140A and ARPANS s 10 bar enrichment and fuel fabrication… An Australian SMR would **therefore** import every processed fuel stage" is a non sequitur for conversion. Conversion is not named in either Act ([TO VERIFY], TODO 5). Australia lacks it for economic reasons, not legal ones.
     - **Fix:** "would import enrichment and fabrication by law, and conversion because no plant exists".
     - This also opens the one legal front-end option (a domestic conversion feasibility study), which belongs in the R3.7 comparison.
   - The Red Book figure (28%) must name its edition, and the 2026 disagreement needs one clause (B9; team decision).
4. **"Translation to practice."**
   - The Silex sentence carries the section's only R4.3 claim, and it has **no source**. Source it by Thu 12:00 (Silex ASX release; NRC Paducah docket) or cut it.
   - If it is sourced, connect it to Darlington: GLE is 49% Cameco, OPG's own supplier. That turns it from an Australian curiosity into a Western supply option for the project in the initiative. [R4.3]
   - The single mitigation (dual sourcing) is not "strong evaluation and comparison of solutions". The supply brief already has a five-option table (dual sourcing, strategic inventory, domestic conversion, domestic enrichment, equity in allied capacity) scored on security, cost, legality and time.
     - **Fix:** put a compact version in §8.6 or as a second table here. Tables don't count towards the page limit (plan §1). [R3.6, R3.7]
5. **Sizing to the proposal (R2.3).** Nothing in §8.3 is sized to C1 or to Darlington: no tU/yr, SWU/yr or reload mass, and no share of Urenco USA capacity.
   - **Leroy:** supply BWRX-300 core loading, reload fraction, cycle length and enrichment (plan §5, run 3 request, due Wed 12:00).
   - **Analyst:** convert them into SWU/yr for four units and a 2-reload strategic reserve.
   - Without this, §8.3 describes the market, not our project's exposure to it.
6. **Table T3.**
   - Add a "Class (2023 / 2010)" column. It makes the threshold dependence visible at no cost in text.
   - Delete the placeholder line, and put the caption above the table in the style-guide form.
   - The "[year TO VERIFY]" in the conversion row must be closed before Thursday 21:00 (B19).
7. **Fabrication not assessed.** That is honest, but for a BWR the fabricators are few (GNF, Westinghouse, Framatome; supply brief gap 7), and the plan's R1.1 list includes the fuel cycle. If no data arrive, add one sourced sentence on BWR-fuel fabricators. Otherwise state it as a limitation in §11.

### Feedback to teammates arising from these sections (no edits made to their work)
- **Leroy:**
  - BWRX-300 fuel data for §8.3 sizing (point 5 above), due Wed 12:00.
  - Reference disambiguation for both sections (§8.1 TODO 9; §8.3 TODO 7): CNSC 2026a/b; Parliament of NSW 2025–26 → a single year with a suffix; the WNA page years.
  - Deck: S4, S9, S20/S44, which conflict with §8.1's governing-code finding.
- **Sam:**
  - §8.3 deliberately no longer claims that the front end dominates the footprint. Your §6 hotspot table (plan §2.5 item 7) decides whether that claim returns.
  - Send the fuel-cycle stage shares as soon as you have them; R4.3 depends on it.
  - Deck placeholders S13 and S18.

### Rubric checklist (status after this review; "done" requires verified HD evidence, so nothing is done)

| ID | Status | Note |
|---|---|---|
| R1.1 | Missing | Only politics/law and supply chain are drafted (§8.1, §8.3) |
| R1.2 | Partial | T7 defines the legal barriers and why each matters; §3 (barriers) not written |
| R1.3 | Partial | §8.3 country-vs-company mining contrast; three known disagreements not in the text |
| R1.4 | Partial | Primaries cited but 0 verified; four news sources carry claims |
| R1.5 | Missing | Judged at the freeze. Nothing irrelevant in §8.1/§8.3, but the §9 note must not ship in §8.1 |
| R2.1 | Partial | T3, Senate arithmetic; inputs unverified |
| R2.2 | Missing | No Granta output |
| R2.3 | Missing | §8.3 not sized to Darlington's fuel demand; §6 and §7 not drafted |
| R2.4 | Missing | HHI method only in `results/hhi.md`; §2 and Appendix B not written |
| R2.5 | Missing | §6.1 not drafted |
| R2.6 | Missing | Earned in §6, §7, §9, §11. In §8.3 the logic is sound except for "therefore" (conversion); §8.1 is sound |
| R2.7 | Partial | T3 sensitivity and limits; threshold dependence and the CRAI range not discussed |
| R3.1 | Missing | §8.2 not drafted |
| R3.2 | Partial | §8.1 and §8.3 cover it in detail; unverified; Kazakh/Rosatom exposure missing |
| R3.3 | Missing | §8.4 not drafted |
| R3.4 | Partial | CNSC timelines; Units 2–4 step not explained; workforce and waste absent |
| R3.5 | Partial | Both sections end on translation to practice; unverified |
| R3.6 | Missing | Route scoring only in a note; supply options and L1–L5 not in the text |
| R3.7 | Partial | One mitigation per section; the comparison is deferred to an unwritten §8.6 |
| R3.8 | Partial | Quantitative in both sections; evidence unverified |
| R4.1 | Missing | §4.3 not drafted |
| R4.2 | Missing | §4.3, §5, §10 not drafted |
| R4.3 | Partial (at risk) | Silex connection unsourced; Darlington vs Liddell contrast present |
| R4.4 | Missing | §9–§11 not drafted |
| R5.1 | Partial | Both sections lead with their point |
| R5.2 | Partial | T3 and T7 exist; caption format to fix; no figures yet |
| R5.3 | Partial | Both within budget; whole-report page count unknown |
| R5.4 | Partial | Harvard in-text; author-form and year defects; no reference list yet |
| R5.5 | Partial | One grammar slip ("Its HHI"); markers to strip before submission |
| RB.1 | Missing | §4.3 not drafted |
| RB.2 | Partial | Legal and supply barriers only; §3 not drafted |
| RB.3 | Missing | §4 not drafted |
| RB.4 | Missing | §5 not drafted |
| RB.5 | Missing | Appendix B cited but absent (working exists in `results/`) |
| RB.6 | Missing | No LCA value to benchmark |
| RB.7 | Missing | §10 not drafted |
| RB.8 | Missing | §9 not drafted |

### Top five priorities

| # | What | Owner | By | IDs |
|---|---|---|---|---|
| 1 | **Open the P1 primaries** for §8.1/§8.3: EPBC s 140A, ARPANS s 10 and s 13, NSW Act ss 8–9, APH Senate composition, CNSC LTC decision, WNA enrichment/conversion/mining tables, DOJ/FTC 2023, OEB D2-4-1. Set `verified: true`, re-run `law_timelines.py` and `hhi.py`, and tell the fact-checker. Without this, nothing in either section can go above Partial | Victor | Wed 18:00 | R1.4, R3.8, R2.1, all of §8.1/§8.3 |
| 2 | **Write Appendix B** (Senate arithmetic, route scoring with the weight test, and the HHI working from `hhi.md` §2–5 with the CRAI row added). Move the route scores into the §9 MCDA plan. All the data exist | Victor (writer + analyst) | Wed 21:00 | RB.5, R2.4, R3.6 |
| 3 | **Put a scored comparison of non-technical solutions in the text**: the supply-option table (5 options) and levers L1–L5, in §8.6 or as tables in §8.3/§8.1 | Victor (writer) | Wed 21:00 | R3.6, R3.7 |
| 4 | **Close or cut the R4.3 claim**: source Silex/GLE (ASX release, NRC docket) and link it to Cameco/OPG, or delete the sentence and the slide-8 equivalent | Victor (analyst) | Thu 12:00 | R4.3, R1.4 |
| 5 | **Size §8.3 to the proposal and fix the threshold honesty**: Leroy's BWRX-300 fuel data → SWU/yr for four units and a reserve; add the 2010-vs-2023 class column and the "scale, not legal test" caveat; fix the conversion "therefore" | Leroy (data, Wed 12:00); Victor (text, Wed 21:00) | Wed 21:00 | R2.3, R2.7, R2.6 |

The cheap §8.1 fixes go with priority 1's re-draft:
- "36 even with every crossbencher";
- the REGDOC 32-month benchmark;
- name NEDO-33926 / AISC N690;
- the Units 2–4 licensing step;
- the 18–24-month critical path;
- Coalition 2035 vs CSIRO 2040;
- ANNPSR;
- caption fixes.

### What this review produced, and what is still missing (per ID)
- **R3.2, R3.4, R3.5, R3.7, R3.8.** Produced: conditional (D) and current (C) grades; paragraph-level fixes; status set to Partial in the tracker. Missing: verification; the solution comparisons in the text; workforce and waste governance (§8.4).
- **R3.6.** Produced: identified that all scored comparisons sit outside the text. Missing: the §9 MCDA and Appendix B tables.
- **R2.1, R2.3, R2.4, R2.6, R2.7.** Produced: the threshold-dependence, sizing, method-location and conversion-logic faults. Missing: SWU sizing, Appendix B, §2 methods, the CRAI sensitivity.
- **R1.2, R1.3, R1.4.** Produced: the three omitted source disagreements; the news sources still carrying claims. Missing: §3 barriers; verified primaries.
- **R4.3.** Produced: the at-risk status and how to rescue it (the Cameco/OPG link). Missing: a source.
- **R5.1–R5.5.** Produced: caption, author-form, year and grammar defects. Missing: the reference list; the whole-report page count.
- **RB.2, RB.5.** Produced: status. Missing: §3; Appendix B.
