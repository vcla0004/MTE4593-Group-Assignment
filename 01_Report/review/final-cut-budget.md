Rubric coverage: R5.3, R1.5, R5.1 (primary); preserves R1.1–R1.4, R2.1–R2.7, R3.1–R3.8, R4.1–R4.4, R5.2, R5.4, R5.5, RB.1–RB.8

# Final-day cut budget (examiner, 25/10/2026)

**Page rule (corrected 25/10 by the coordinator).** The brief (`brief_text.txt` l. 87) says "15 – 20 pages of text, figures and graphs not included in limit". So **figures and graphs cost nothing**, and **tables count** (Victor's decision, H6).

**Problem.** Body now ≈ 11,400 prose + 3,600 table words (excluding the abstract), plus about 1,400 words of Leroy's sections still to come. At 500 words/page that is about 33 pages against the **19.5-page cap** (R5.3: "concise", 15–20 pages). The body has to lose about 44% of its words. Moving evidence to an appendix is the main tool, because appendices don't count.

**Target.** Body = **9,250 words (7,100 prose + 2,150 table) = 18.5 pages**. That leaves 1.0 page for headings, captions and table layout: tables render looser than prose, so the 500 words/page figure flatters them. Figures are free, so every drawn figure stays in the body.

**Gates (in this order).**
1. Run `python3 01_Report/assembly/assemble_draft.py`. Body total (excluding `0-abstract.md`) must be ≤ 9,500 words, with no section more than 10% over its target.
2. Open `draft-assembled.docx` and count the pages of **text and tables** from the §1 heading to the end of §11, leaving out any page area taken by figures. This count **overrides** the word estimate and must be ≤ 19.5.
3. If either gate fails, apply the reserve cuts (end of §2 below) in order until it passes.

**Per-section counts below are estimates.** I couldn't run the script, so I estimated them from the 22/10 assembled draft and scaled them to the reported totals (11,600 / 3,600). Re-run the script to get exact figures. The targets are firm.

## Global rules for every writer (apply while cutting)
- **Captions:** ≤ 30 words each, and "Source:" lines ≤ 25. No file paths or script names in body captions: write "this study, Appendix X". Citations that support numbers stay in the cells as short Harvard citations, and long source lists move to the appendix that holds the working.
- **Strip working text:** delete every rubric ID from the report text (§4.3 heading "(R4.1 to R4.3)"), every "[per final §…]" and "[C1 saving: per final §6]" once the re-base numbers are in, and every TODO. Replace "Appendix D" with "Appendix A1" (there is no Appendix D).
- **Moved material:** paste it **verbatim** into the named appendix subsection and leave a pointer "(Appendix Xn)" in the body. Delete nothing that is the only copy of a number.
- **Numbering:** tables and figures are renumbered **once**, at assembly, in order of appearance. Writers keep the current labels. Known clash: T10 is used for both the §7.1 schedule table and the §8.2 cost table. "Figure 8" becomes F8.
- **Ownership:** §6 and Appendices A and C are the LCA side, so **Victor only**; agents don't edit them. Leroy's sections are Leroy's; send him this budget. With the 2-agent limit:
  - **Writer A:** §1, §2, §3, §9, §11.
  - **Writer B:** §8.1–8.6 and the App B moves.
  - Either writer takes §4.3 and §7 once the re-based C1 numbers exist.
- **C1 re-base:** it replaces the old content; it doesn't add to it. The 20,700 m³ / 13,100 m³ / 1,734 t model becomes a one-sentence cross-check in §6.2, with its working in App A6. The headline is the Ostrołęka case: 50,000 m³ per unit, 40% eligible, 2,200 t (range 1,100–3,300).
  - **Flag:** §7.1 T10 (break-even days) and the §8.2 carbon value were computed for 1,734 t, and the 9–15 days rise with a 2,200 t saving. Re-run `schedule_value.py` and `initiative_cost.py` on `c1_cases` before quoting the days anywhere.

## 1. Budget table

Current figures are estimates (prose + table). Targets are prose + table.

| Section | Current (est.) | Target | Tables kept in body | Tables moved to appendix (or merged) | Figures kept |
|---|---:|---:|---|---|---|
| §1 Introduction | 560 + 0 | **250** + 0 | — | — | — |
| §2 Methods and data | 700 + 0 | **330** + 0 | — | — | — |
| §3 Barriers | 195 + 610 | **100 + 350** | T15 (trimmed, 8 rows) | — | — |
| §4.1 Technology, projects, patents (Leroy) | 0 (missing) | **330 + 120** | T2 projects/timeline/TRL (new, ≤ 6 rows) | Patent search log → App E | Optional timeline figure (free) |
| §4.2 BWRX-300 at Darlington (Leroy) | 0 (missing) | **200** + 0 | — | — | — |
| §4.3 Initiative | 475 + 225 | **270 + 150** | T1 (6 rows, re-based) | T1 "Value" row deleted (lives in §8.2) | — |
| §5 Materials, extraction to end-of-life (Leroy) | 0 (missing) | **350** + 0 | — | — | — |
| §6 LCA and eco-audit | 2,760 + 680 | **1,650 + 150** | T8 (≤ 4 rows, re-based) | T6 → App A2 (Table A2b); T8 S2b + three S3 steel rows + note → App A7; T9 → App C7 | F1, F2, F3, F4, F5 (all stay: figures are free) |
| §7 Carbon avoided | 1,580 + 70 | **760 + 70** | T10 (schedule) | Capital-cost-alone working → App B6.3 | F6, F7 **only if drawn** after the cuts are done (free); otherwise delete the placeholders and point to Tables B17, B20, B28 |
| §8.1 Law, regulation, licensing | 500 + 565 | **270 + 280** | T7 (4 rows, trimmed) | ANNPSR precedent, 2022 bill history → App B1.1/B1.4 | — |
| §8.2 Economics and finance | 840 + 365 | **470 + 160** | Cost table (5 rows) | T11 merged into §8.6 T16 | — |
| §8.3 Supply concentration | 600 + 70 | **330 + 70** | T3 | Most of the T3 note → App B2.4–B2.5 | — |
| §8.4 Social licence | 745 + 445 | **330 + 270** | T12 (5 rows) | T13 + its "Reading" → App B8.3; T12 source list → App B8 | — |
| §8.5 Stakeholders and money | 400 + 175 | **200 + 130** | T14 (4 rows) | — | F8 |
| §8.6 Implementation | 620 + 115 | **310 + 170** | T16 (merged with T11, 4 levers) | — | — |
| §9 TBL and MCDA | 955 + 280 | **450 + 230** | T4 (trimmed), T5 | — | — |
| §10 Future materials (Leroy) | 0 (missing) | **250** + 0 | — | — | — |
| §11 Conclusions | 465 + 0 | **250** + 0 | — | — | — |
| **Victor's and shared sections** | **11,395 + 3,600 = 14,995** | **8,000** | | | |
| **Leroy's sections** | 0 (≈ 1,400 planned) | **1,250** (incl. T2) | | | |
| **Body total** | **≈ 16,400 ≈ 33 p** | **9,250 (7,100 + 2,150) = 18.5 p**; figures free | | | F1–F5, F8 (+ F6/F7 if drawn) |

**Leroy: the target is 1,250 words, not 1,400.** Every extra 100 words must come out of your own four sections. A figure costs nothing, so a timeline figure can replace words.

## 2. Cuts per section, in priority order (do them in the order listed)

### §1 Introduction (560 → 250). Writer A
Keep for HD: the context (coal closing, the two sites), the four research questions, and the C1 pointer (R5.1 "leads with its point").
1. Delete **"Answer in brief"** (≈ 75): it duplicates the abstract and §11, and §11 is its home.
2. Delete **"Roadmap"** (≈ 70): the ToC does this job.
3. **"Context"** ¶ 150 → 80: keep Liddell (hedged closure, §4 below), NSW 640 g/kWh, Ontario 74 g/kWh, the SMR definition and "the BWRX-300 is the first SMR licensed for construction in an OECD country". Cut the Ontario 2014 date unless it is sourced; write "Ontario no longer burns coal for power (The Atmospheric Fund, 2025)".
4. **"The two sites"** 95 → 50: drop the "law bars" and CSIRO clauses (§3 and §8.1 hold them).
5. **"The initiative"** 80 → 30: one sentence, with the pointer to §4.3.

### §2 Methods and data (700 → 330). Writer A. Home of the displacement, HHI and MCDA methods
Keep for HD (R2.4 "methods clearly explained"): one short paragraph per method, with its working-appendix pointer.
1. **LCA ¶** 190 → 40: screening LCA following ISO 14040/44 principles, not critically reviewed; FU 1 MWh net at the grid connection; cradle to grave; "detail in §6.1". Everything else is in §6.1, which is its home.
2. **Displacement ¶** 270 → 110: keep the average vs marginal definitions, the grid-factor bases, the break-even formula and the start years. **Delete the GenCost reading** (A$230–382, A$387–641, 2.9×, 5.0×); §7.3 is its home. Add the assumption "300 MWe net (an OPG filing gives 315; within the sensitivity range)".
3. **HHI ¶** 120 → 70: keep the definition, the 1,800 threshold (2023) and the 2010 scale, and two caveats (capacity is not contracts; "without Russia" adds no capacity). The other caveats go to App B2.5.
4. **MCDA ¶** 120 → 70: keep the options, criteria, normalisation, the four weight sets (labelled as judgement) and the robustness tests. This becomes the MCDA method's home, so §9.2's Method ¶ shrinks to a pointer.
5. **Search strategy** line → "Search strategy and patent search: Appendix E." If App E is not in the repo at assembly, delete the line and every App E reference.
6. **Add** the data-quality sentence from §4 below (≈ 35 words).

### §3 Barriers (805 → 450). Writer A
Keep for HD (R1.2/RB.2 "key problems and challenges clearly defined"): **all 8 rows**, each with one number, one source, why it matters, and the C1 column (it also carries R3.5).
1. **T15 cells:**
   - "Number and source" ≤ 18 words.
   - "Why it matters" ≤ 15 words.
   - "Does C1 touch it?" ≤ 5 words ("No"; "Yes, as a constraint"; "Yes: C1's target").
2. Row-by-row:
   - **Row 1:** C$149–198/MWh, plus "NuScale cancelled 2023 (§8.2)" as 4 words. The NuScale story lives in §8.2.
   - **Row 2:** "2040 at the earliest" only. The Coalition 2035 vs CSIRO 2040 synthesis lives in §7.2.
   - **Row 3:** the hedged Senate wording (§4 below).
   - **Row 5:** re-based construction share and C1 saving.
   - **Row 7:** drop the 76,950 figure unless it is verified (§4 below); keep the AUKUS competition point with its source.
3. Lead ¶ 110 → 60: delete the "Table T15 gives each barrier…" restatement.
4. "Reading the table" 55 → 20: "C1 moves only rows 2 and 5; §7 and §8.6 test the schedule risk."
5. Caption + source line 45 → 20.

### §4.1 Technology, projects and patents (target 450 incl. T2). Leroy
Must deliver:
- RB.3 "current state of the technology".
- R1.1 timescales.
- R1.4 patents ("a wide range of highly relevant sources": the brief asks for patents and no patent search exists).

Content:
- **T2** (≤ 6 rows, ≤ 120 words): design, site, status or TRL, first-power date, source. Suggested rows: BWRX-300 Darlington; BWRX-300 TVA Clinch River; ACP100 Linglong One; NuScale CFPP (cancelled); one other.
- **Patents:** 3–4 named US patent numbers on SMR or BWRX-300 features, with one sentence on what they show. The search log goes to App E.
- **TRL:** one TRL statement with a source. §9.3 says TRL isn't scored because no TRL is in the report; give one.

Don't repeat:
- NuScale's cost story (§8.2): one clause at most.
- The Darlington licence months (§8.1 T7).
- The Coalition vs CSIRO dates (§7.2).

### §4.2 BWRX-300 at Darlington (target 200). Leroy
Give only the design facts that §4.3 and §6 rely on:
- 300 MWe (OPG filing 315 net) and natural circulation.
- DPSC steel-composite modules filled with self-consolidating concrete.
- The below-grade reactor building and shaft.
- Unit 1: licence April 2025, in service 2030.

Don't restate the cost (§8.2), the licence detail (§8.1) or C1 (§4.3).

### §4.3 Initiative (700 → 420). Writer, after the re-base numbers exist
Keep for HD:
- RB.1: location, scale, application, technology (T1).
- R4.1–R4.3: why it is not obvious.
- R4.4: the schedule-neutral condition.

Cuts:
1. **Re-base, then cut.**
   - Proposal ¶ 130 → 70 on the Ostrołęka basis: 50,000 m³/unit; 20/40/60% eligible gives 1,100/2,200/3,300 t, with 40% central; Units 2–4 total.
   - Framing: "pilot LC³ in eligible non-safety works first; steel-composite infill only if qualified".
   - Delete the 13,100 m³ / 1,740 t numbers from this section. The cross-check is in §6.2.
2. **T1** 260 → 150:
   - Rows: Location, Scale, Application, Technology, Saving (per unit, Units 2–4, clinker), Condition.
   - **Delete the "Value" row** (§8.2 is its home).
   - Delete the St Marys capability clause unless it is sourced, and the 2028 ANS clause (§8.1 lead is its home).
3. **¶1** 120 → 70. Keep one clause of the condition: "only if schedule-neutral: a delay of [re-run] days cancels it (§7.1)".
4. **"Why it is not the obvious choice"**: delete "(R4.1 to R4.3)" from the heading. 110 → 80:
   - Keep point 1: the infill problem is specific to modular construction.
   - Keep point 3: timing and schedule value. This is the R4.3 connection.
   - **Cut point 2** (Ontario slag scarcity) unless a source is found (§4 below).
5. **"What C1 does not address"** 105 → 30: one sentence pointing to the T15 C1 column and to steel as the next lever (§6.3, §10).

### §5 Materials from extraction to end-of-life (target 350). Leroy
Must deliver RB.4 "technical description of the material(s), from extraction to end-of-life", for three chains, about 110 words each:
- **Uranium:** mining and milling → conversion → enrichment → fabrication → spent fuel and direct disposal.
- **Cement and concrete:** limestone and clay → clinker or LC³ calcination → SCC infill → decommissioning, crushing and recycling.
- **Steel:** ore or scrap → BF-BOF or EAF → plate and rebar → activated or clean steel at decommissioning.

Cite §6.2 for the emissions shares; **don't quantify emissions here** (§6 is their home). Cross-reference F1 (the system boundary, §6.1) rather than adding a second flow diagram.

### §6 LCA and eco-audit (3,440 → 1,800). **Victor only** (LCA side)
Keep for HD (R2.2, R2.5, R2.7, RB.6):
- FU, reference flow, boundary, S0, cut-offs and impact category in text.
- The hotspot ranking.
- The C1 result with intervals.
- Why median not mode.
- Range of medians 3.3–4.2.
- Benchmarks and the top discrepancy reasons.
- F1–F5 (all stay in the body: figures are free).
- The extra 150 words over the first budget go to findings 3 and 4 and to §6.4. Don't add new material.

Cuts:
1. **T6 → App A2** as "Table A2b. Key assumptions" (verbatim, ≈ 330 table words). In §6.1, write one sentence: "Key inputs: Table A2b; all 40 ranged inputs: Table C2."
2. **T9 → App C7** ("Why our result differs from the benchmarks", ≈ 230). In §6.5, replace it with ≤ 60 words naming the three biggest reasons with their sizes:
   - Ore grade: about 2.8 g/kWh at global-average grade.
   - Centrifuge enrichment: 50 against 2,500 kWh/SWU.
   - Cut-offs and possibly low construction: these bias the result low.
3. **T8:** ≤ 4 rows after the re-base: LC³ at 20/40/60% eligibility, the slag fallback, and the old-model cross-check (1,734 t).
   - Move S2b, the three S3 steel rows and the T8 note → App A7 (Table A7b).
4. **F1 and F4 stay** (free). Their captions carry no table-like data: ≤ 30 words each.
5. **Finding 2** (170 → 50): keep "≈ 0.3–0.4% of the life cycle, ≈ 0.01 g/kWh; it doesn't change the climate case". The carbon value, % of capital, delay cost and premium break-even all move to §8.2, their home.
6. **Finding 4** (160 → 50): "Within the target structures concrete is about 3× the steel lever; low-carbon whole-plant steel could save up to 3,714 t but isn't shown to be feasible for nuclear-grade plate; it is the next lever (§10). Working: App A7."
7. **Finding 5** (95 → 25): "A delay of [re-run] days cancels it (§7.1, T10)."
8. Delete the closing TBL sentence of §6.3 (§9 T4 is its home).
9. **§6.2:**
   - Target-structure ¶ 130 → 40 (Ostrołęka basis plus "20,700 m³ geometric model as cross-check, App A6"). The okdiario geometry and its caveat go to App A3.
   - Delete the 196 tU / 138 tSWU sentence (§8.3 is its home).
   - Quantities ¶ 120 → 70: keep the vendor-vs-scale-penalty synthesis in one sentence (R1.3).
   - Hotspots 130 → 90; construction split 85 → 50.
10. **§6.4:** Monte Carlo ¶ 200 → 110 (drop the log-uniform case detail, which is in Table C2); tornado ¶ 110 → 80.
11. **§6 lead ¶** 150 → 70: drop the delay sentence (§7.1 is its home) and "No input has been checked" (the global sentence in §2 replaces it).
12. **§6.1 bullets:**
    - S0 90 → 50; boundary 75 → 50; cut-offs 55 → 35; impact category 65 → 35 (the US-grid CO₂-only aside goes to App A5).
    - Method ¶ 85 → 45, with **one** Granta sentence: "No Granta EduPack Eco Audit was run; an equivalent process-based model is used (Appendix A)."
    - If Granta is run today, use one result sentence plus A9 instead.
    - Delete the Granta TODO in §6.5.
13. Captions: F2, F3 and F5 ≤ 35 words each. F5 drops the drawing notes.

### §7 Carbon avoided (1,650 → 830). Writer, after `schedule_value.py` is re-run on the re-base
Keep for HD:
- R2.3 "benefits appropriate to the scale": per-unit displacement at both sites.
- R4.3: Ontario vs Liddell timing; schedule value.
- R2.7: average vs marginal; the drivers.
- R3.6: same money.

Cuts:
1. **F6 and F7 cost no pages but are not drawn.** Draw them only after every cut in this file is done (data in `results/displacement.md` §3, `schedule_value.md` §2 and `same_money.md` §5). Otherwise delete both placeholders and point to Tables B17, B20 and B28. Either way, captions ≤ 30 words.
   - If F7 is drawn, the four cost cases can leave the §7.3 prose: keep only 2.9×/10.9× in the text. That uses part of the extra 100 words.
2. **Delete the Method ¶ and its three bullets** (≈ 105); §2 is their home.
3. **Delete §7.4** (≈ 55); §9 T4 and §11 are its home.
4. **§7.3** 535 → 220:
   - Keep 2.9× and 10.9×, and the worst cases 5.7× and 4.9×.
   - The alternative reading becomes **one** sentence; this is the only place the A$387–641 reading appears.
   - "Capital cost alone" → App B6.3.
   - Delete "Check against our own costing" (§8.2 is its home).
   - "Why renewables come out ahead" 110 → 60.
5. **§7.2** 525 → 300:
   - Merge the three displacement bullets into one sentence: 1.50 / 0.165 / 0.80 Mt a year, 9.1× and 1.9×. The CER 20.6× variant goes to B4.
   - Timing 80 → 50. This is the **home** of Coalition 2035 vs CSIRO 2040 (R1.3).
   - "What moves the results" 70 → 30; caveats 65 → 30.
6. **§7.1:**
   - "In money" ¶ and bullets 140 → 70: one month's slip = C$33–110 m carrying cost (upper bound) + C$88 m of deferred output = [re-run]× C1's carbon value (§8.2).
   - Delete the superseded C$170/t sentence and the 10.9–118 kt bullet (they stay in B5).
   - Shadow-price ¶ 70 → 35.
   - T10 caption 55 → 25.
7. **Lead** 150 → 70.

### §8.1 Law, regulation and licensing (1,065 → 550). Writer B
Keep for HD (R3.2, R3.4):
- The three bans, the regulator gap, the site owner.
- The Senate arithmetic (in T7).
- 29 vs 32 months (in T7).
- NEDO-33926 / AISC N690 as C1's real licensing risk.
- The translation-to-practice close (R3.5).

Cuts:
1. **T7** 565 → 280. Four rows:
   - (1) Federal bans (s 140A and s 10 merged)
   - (2) Regulator for a private reactor
   - (3) NSW s 8
   - (4) Site (AGL)

   Delete the "Earliest legal start" row; the caption says "No row is resolved as at October 2026", and timing lives in §7.2. Cells ≤ 20 words; Darlington cells ≤ 12. Trim cell material:
   - ANNPSR precedent and the 2022 bill committee history → App B1.4 / B1.1.
   - The Norton Rose "2025 reforms not checked" clause → one line in the §11 limitations.
   - Partlett: keep "s 109 override" and drop the challenge commentary.

   Caption source list 70 → 20.
2. **"Canada" ¶** 170 → 100: drop the 29/32-month clause (T7 is its home).
3. **"Australia" ¶** 120 → 80: drop the Senate count (T7 and B1.2 are its home).
4. **"Translation to practice"** 110 → 45: "The non-safety pilot needs no nuclear qualification; infill qualification must start in 2027 (§8.6)." Delete the delay sentence (§7.1) and the 18–24-month detail (§8.6).
5. **Lead** 70 → 45.

### §8.2 Economics, finance and market barriers (1,205 → 630). Writer B
Keep for HD (R3.1):
- LCOE at four rates, the capital share, OPG at 4.9%.
- GenCost synthesis and its non-independence (R1.3).
- NuScale.
- Darlington finance.
- Barriers to entry: US market caps, DOE, China top-down, Australia.
- C1's economics: carbon value, premium break-even, abatement cost.

Cuts:
1. **Delete T11** and the "Solutions compared" ¶ (90 → 25: "Responses are compared and sequenced in §8.6, Table T16"). T11's rows are merged into §8.6 T16. This also resolves the open conflict over the contract clause's position (Q10).
2. **Cost table** 9 rows → 5:
   - Keep: our LCOE; OPG C$149; GenCost 2023-24 2030 (SMR / large / firmed VRE); vendor US$2,250/kW vs about US$12,600/kW; NuScale CFPP 58 → 89, cancelled.
   - Cut the overrun ×1.75 row (one clause in the Cost ¶: "a NuScale-size overrun gives C$317").
   - Cut the GenCost 2025-26 row (TODO) and the SMR ÷ renewables row (§7.3).
   - Cut the market-value row; it moves into the text.
   - "What it shows" ≤ 8 words. Caption 60 → 25.
3. **Cost ¶** 200 → 120: delete the 2.9×/5.0× sentence (§7.3).
4. **C1 ¶** 170 → 90. This is the **home** of the carbon value, the premium break-even (C$/m³), 0.07% of capital, "no one captures it (our inference)", the qualification-driven abatement cost (assumed C$1 m) and one clause on the cost of a day's delay. Recompute it for 2,200 t.
5. **Barriers to entry** 150 → 110. This is the **home** of "Liddell is private (AGL), so Commonwealth ownership or underwriting would be needed" (§8.5 cites it). Hedge China (§4 below).
6. **Risk and finance** 120 → 90; **lead** 40 → 30.

### §8.3 Supply concentration (670 → 400). Writer B
Keep for HD (R3.2, R1.3):
- HHI by stage (T3).
- Russia 41.0–42.8%; PL 118-62.
- The Urenco–Orano duopoly.
- Country vs company for mining.
- Darlington's fuel demand sized.
- Australia's resources vs no conversion or enrichment.
- Silex/GLE (R4.3).

Cuts:
1. **T3 note** 190 → 30: "High: > 1,800 (2023), > 2,500 (2010). Sensitivity and limits: Appendix B2.4–B2.5." The rest goes to B2.4/B2.5 verbatim. **Delete the Rosatom–Kazakh stakes clause** (unsourced); B2.5 lists it as not assessed.
2. **¶1** 85 → 50: delete the HHI re-definition (§2 is its home).
3. **¶3**: this is the **home** of 196 tU / 138 tSWU / 3.2% of Urenco USA. Keep the Red Book 2024 vs 2026 point as one clause (R1.3). 120 → 100.
4. **¶2** 110 → 80; **¶4** 100 → 80. ¶4 also absorbs "contracts cut exposure, not concentration" from §8.6.

### §8.4 Social licence (1,190 → 600). Writer B
Keep for HD (R3.3): polling against deaths per TWh, deaths avoided, Williams Treaties equity with the dated dissent, Barngarla, the NWMO route, jobs and AUKUS, the low-regret steps for Liddell (R3.7), and the route comparison stated as a result.

Cuts:
1. **T13 and its "Reading" ¶ → App B8.3** (≈ 170). In the body, one sentence: "Scored on legitimacy, legal risk, speed, public cost and fairness, consent-based routes beat top-down siting by 3–6 points under every weighting, and not building scores highest (Appendix B8.3)."
2. **T12 caption source list** (≈ 140) → ≤ 25 words. Put short citations in the cells that carry numbers; the full list goes to the head of App B8.
3. **T12** 6 rows → 5 (≈ 270):
   - **Delete the "Public view" row**; the text is the home of 61% vs 59%.
   - Keep: Safety (deaths/TWh and deaths avoided); Traditional Owners and consent; Residual dissent and litigation; Waste route (the **home** of C$26 bn and Ignace); Workforce (the **home** of jobs and AUKUS).
   - Cells ≤ 25 words.
4. **Consent ¶** 240 → 150; **perceived/actual ¶** 170 → 110 (older polls in one clause; delete the AEMO coal-exit clause, which §7.2 holds); **translation ¶** 100 → 70.

### §8.5 Stakeholders and money flows (575 → 330). Writer B
Keep for HD (R3.1, R3.3, R3.5): F8, the power-weighted stance numbers, who pays and who earns, and the actors who decide C1.

Cuts:
1. **T14** 6 rows → 4 (OPG share; CIB loan; equity tranches; First Nations loan). Delete the waste row (T12 is its home) and the Liddell row (one clause in the text). Caption 75 → 20.
2. **¶2** 130 → 60: delete the Commonwealth-ownership sentence and the ABC TODO (§8.2 is their home).
3. **F8 caption** 100 → 35. Delete the re-export instruction, and re-export the PNG so it reads "our judgement".
4. ¶1 70 → 55; ¶3 keep (≈ 45).

### §8.6 Implementation pathway (735 → 480). Writer B
Keep for HD (R3.7, R3.6):
- Levers compared and scored.
- The sequenced qualification path (18–24 months, starting 2027).
- The 130% trap.
- What happens if the evidence isn't ready.

Cuts and merge:
1. **Merge T11 into T16:** Lever | Who pays | Binding on OPG? | Time | Schedule risk | Score. Four levers:
   - L1 OPG specification for non-safety concrete (absorbs T11-B, the contract clause).
   - L2 tranche-2 milestone (= T11-A).
   - L3 shareholder direction.
   - L4 public funding for qualification on the Unit 1 mock-up (= T11-C).

   T11-D "do nothing" becomes one clause. **L4 is unscored** ("—", "enabling step for L1's infill extension"), unless the analyst adds it to the B3.1 script today. Don't print an unscripted score.

   The sequence becomes **L1 now → L4 in 2027 → L2 at the 2028 tranche**. Write it once, here.
2. **Lead ¶** 230 → 110: delete the 380/760/1,140 and 1,100/2,200/3,300 arithmetic (§4.3 T1 and §6.3 T8 are its home) and the Pillai detail. Keep the recommendation and the weight-test result.
3. **Delete the "Fuel supply" ¶** (≈ 85); §8.3 ¶4 is its home.
4. **Qualification and sequencing** 210 → 130: this is the **home** of the three steps and the 18–24 months.
5. **Federal standard ¶** 95 → 60: the **home** of the 130% trap.

### §9 TBL and MCDA (1,235 → 680). Writer A
Keep for HD:
- RB.8: T4 with traceability.
- R3.6: T5, the rank-reversal results, the honest scaling-artefact point, and SMR ≈ SMR + C1.
- The verdict and the limits.

Cuts:
1. **§9.2 Method ¶** 140 → 40: "Method in §2; working in Appendix B7; social-licence and legal scores from Appendix B8.3 and B3."
2. **T4** 260 → 170: cells ≤ 25 words. Drop numbers already in T5 or §7 where the cell can cite the section instead (keep one number per cell).
3. **§9.3 limits** 170 → 75: keep judgement weights and scores, the scaling artefact, TRL (cite Leroy's §4.1 TRL if delivered, otherwise one clause) and the GenCost basis. Delete the "4.2 base from earlier model" bullet after the re-base.
4. **§9.3 Darlington ¶** 85 → 40 (§11 lead says it); **Australia ¶** 65 → 45.
5. **Rank reversal** 140 → 80; **SMR + C1** 85 → 50; **status-quo artefact** 65 → 50; **renewables first** 70 → 50; **lead** 85 → 60; **9.1 intro** 45 → 20; **T5 caption** 50 → 25.

### §10 Future material properties and processes (target 250). Leroy
Must deliver RB.7. Give three items, each tied to one of our hotspots, saying what property or process is needed:
1. A low-clinker SCC mix that flows, stays cool in thick sections and is qualified for nuclear use (C1's gap).
2. Low-carbon nuclear-grade steel plate and forgings (H₂-DRI/EAF): the steel lever from §6.3.
3. Fuel-cycle processes: electrified conversion heat (our largest uncertainty) and laser enrichment (Silex/GLE, cite §8.3 and don't repeat it).

Don't restate §4.3's "why not obvious" or §11's levers.

### §11 Conclusions (465 → 250). Writer A
Keep for HD (R5.1, R4.4): the recommendation, the answers to the research questions (§11 is their **home**), the ranked levers, and the limitations.

Cuts:
1. **"Australia" ¶** (≈ 60): delete it and fold one clause into the lead (§9.3 holds it).
2. **RQ answers** 200 → 110: one sentence each.
3. **Ranked levers** 110 → 60: one line each.
4. **Limitations** 70 → 30: screening LCA, not critically reviewed; no Granta; judgement scores; inputs as per the §2 data-quality sentence; legislation as compiled (2025 EPBC reforms).

### Reserve cuts (apply in order only if a gate fails)
| # | Cut | Saves |
|---|---|---|
| R1 | T14 → App B8.4; replace it with 2 sentences (78% OPG / 22% public and First Nations). If time allows, draw it as a stacked-bar figure in the body (free) | 0.25 p |
| R2 | Leroy's T2 → a timeline figure (free) or App E, with 2 sentences in §4.1 | 0.25 p |
| R3 | T3 → a bar chart of HHI by stage against the 1,800 line (free) or App B2.3; three HHIs inline in §8.3 ¶1 | 0.15 p |
| R4 | T4 "Society" row merged into the "Net" row | 0.1 p |
| R5 | §8.2 cost table → App B6.3, with our LCOE and OPG's C$149 inline | 0.3 p |

The general reserve lever: **any table that is really a chart can become a figure at zero page cost** (cost comparison, HHI, money flows), provided it is captioned and sourced (R5.2). Never cut T15, T1, T8, T7, T10, T5 or F2/F3/F8: they carry RB.1, RB.2, R2.2, R2.7, R3.2, R3.6 and R5.2 ("LCA stage breakdown, sensitivity chart, stakeholder map, cost comparison, MCDA table").

## 3. Duplicated content: where each item stays

| Content | Now appears in | Stays in (home) | Everywhere else |
|---|---|---|---|
| C1 saving (t/unit, Units 2–4, clinker, % of life cycle) | Abstract, §1, §4.3 ¶2 + T1, §6 lead, §6.3, §8.2, §8.6, §9 T4 + text, §11 | **§6.3 T8** (result); **§4.3 T1** "Saving" row (spec) | One number and "(§6.3)", or nothing. §1 and §8.6 drop it |
| Break-even delay (days) | Abstract, §1, §4.3, §6 lead, §6.3 F5, §7 lead, T10, §8.1, §8.6, §11 | **§7.1 T10** | Abstract, §4.3 condition and §11 keep one clause; delete from §6 lead, §8.1 and §8.6 |
| C1 carbon value, % of capital, premium break-even, C$/day of delay | T1 Value, §6.3 F2, §7.1, §7.4, §8.2, §9 T4 | **§8.2 C1 ¶** | §7.1 keeps the monthly-delay ratio; delete the rest |
| GenCost reading (A$230–382 vs 89–125; 2.9×; A$387–641 → 5.0×) | §2, §7.3, §8.2 ¶ + 2 table rows, §9 T4, §11 | **§7.3** (reading and ratios); §8.2 cost table keeps the GenCost row only | Delete from §2 and the §8.2 prose |
| Senate 36 vs 39 | §3 row 3, §8.1 ¶2, T7 | **T7** (+ B1.2) | §3 row keeps the number (one per barrier); §8.1 prose deletes it |
| Licence 29 vs 32 months | §8.1 ¶3, T7 | **T7** | Delete from the prose |
| Coalition 2035 vs CSIRO 2040 | §3 row 2, §7.2, §8.1 T7 last row | **§7.2** | §3: "2040 at the earliest"; T7 row deleted |
| HHI definition | §2, §3 row 4, §8.3 ¶1 | **§2** | Delete |
| Lowy 61% vs 59% | §3 row 6, §8.4 ¶2, T12 row 1, §9 T4 | **§8.4 ¶2** | §3 keeps 59%; T12 row deleted; T4 cites §8.4 |
| 196 tU / 138 tSWU | §6.2, §8.3 | **§8.3 ¶3** | Delete from §6.2 |
| Waste C$26 bn, Ignace | §3 row 8, T12, T14 | **T12** waste row | §3 cites; T14 row deleted |
| Workforce / AUKUS | §3 row 7, T12, §8.4 ¶3 | **T12** workforce row | §3 cites |
| Liddell needs Commonwealth ownership (AGL private) | §8.2, §8.5 ¶2, T7 site row, T14 | **§8.2** barriers to entry | §8.5 one clause; T14 row deleted |
| Policy levers (tranche condition, contract clause, qualification funding) | §8.2 T11 + ¶, §8.6 T16 | **§8.6 merged T16** | §8.2 one-line pointer |
| Qualification steps, 18–24 months | §8.1 translation, §8.6 | **§8.6** | §8.1 one clause |
| Steel lever (566 / 3,714 t) | §4.3, §6.3 F4, T8 S3 rows, §11 | **§6.3 finding 4** (+ App A7) | §4.3 one clause; §11 keeps the ranked lever |
| "C1 doesn't touch X" | §3 column, §4.3, §8.3/§8.4 translation | **§3 T15 column** | §4.3 one sentence; §8.x keep only the R3.5 closing sentence |
| LCA FU, boundary, reference flow | §2, §6.1 | **§6.1** | §2 two sentences |
| RQ answers | §1, abstract, §11 | **§11** (+ abstract) | Delete §1 "Answer in brief" |
| Darlington vs Liddell displacement | §7.2, §9 T4, §11, §4.3 | **§7.2** | Others cite one range |
| TBL statements | §6.3 last ¶, §7.4 | **§9 T4** | Delete |

## 4. [TO VERIFY] markers: hedge or cut

Status: **0 primaries opened** (`factcheck/H-6-lca.md`, `human-checklist.md`). No bracketed marker may appear in the submission (R5.5). Every marker is either hedged or its claim is cut.

**Global sentence (§2, ≈ 35 words; then delete the inline markers covered by class A):**
> "Values are taken from the documents cited, or, where marked 'as reported', from the secondary source named. Where readings differ we give the range, and our own assumptions and inferences are labelled as such."

Don't write "verified" anywhere.

### A. Hedge as-is: delete the marker and keep the citation
Pattern: **(Author, year)** for the primary; **"(Primary, year, as reported by Secondary, year)"** where the number came from a secondary extract. Both go in the reference list.

This covers:
- Peer-reviewed and agency values: Gibon and Hahn Menacho; Parker et al.; EDF R&D; Carless et al.; Warner and Heath; UNECE 2021; Peterson et al.; CAC EPD; Slag Cement Association; EFNARC; Scrivener et al.
- IPCC AR5: add it to §6.5 in one clause as "IPCC AR5 median 12 g/kWh, range 3.7–110 (Schlömer et al., 2014)". This closes the plan's benchmark gap.
- Statute sections: EPBC s 140A, ARPANS s 10/s 13, NSW 1986 Act s 8/s 9, CSA A3001.
- Regulator and company dates: CNSC licence of 4 April 2025, valid to 2035; Ontario approval of 8 May 2025; OPG C$20.9 bn.
- Market and grid data: WNA capacities and HHIs; Red Book 2024 28%; DCCEEW 640; TAF 73.8 ("TAF's marginal factor, 343"); AEMO Step Change; RBA rate.
- Social and safety data: Lowy (Neelam, 2024); Griffith–Monash; OWID/Markandya and Wilkinson; Barngarla [2023] FCA 809; NWMO; Williams Treaties release (cite the release, not the BNN reprint).
- Finance: NuScale/UAMPS prices and costs; DOE US$800 m; IAEA "about 70 designs"; DOJ/FTC thresholds; PL 118-62; ECCC carbon price path.

### B. Hedge with a qualifier: wording to use
| Claim | Hedge wording |
|---|---|
| Senate count (M1) | "at most 36–37 of the 39 votes needed" (it fails on either count). Delete the aph.gov.au marker |
| Licence duration | "about 29 months, against the CNSC's expected 24–32 months (CNSC, 2022; 2025)" |
| 300 vs 315 MWe; Unit 1 in service | "300 MWe net assumed (315 in an OPG filing)"; "in service planned for 2030 (OPG, 2025)" |
| Units 2–4 approval 2028 | "expected in 2028, as reported (American Nuclear Society, 2026)" |
| Coalition 2035; China batch approvals; Liddell battery; Coalition pledge | "as reported by ABC News / Caixin Global / Newcastle Herald (year)", one clause each, never a load-bearing number |
| Darlington fuel chain has no Russian stage | "OPG's announced Unit 1 fuel suppliers (Cameco, Urenco USA, Orano, GNF-A) include no Russian firm, as reported (Power Engineering, 2023)" |
| Construction materials outside Ontario carbon pricing; Units 2–4 need a further authorisation; OPG not bound by the federal standard; s 8(3) not extending to a power reactor | "(our inference)" or "may", with no marker |
| Qualification cost C$1 m (C$1–3 m); 18–24 months; infill thicknesses; post-coal 30 g/kWh; renewables start 2028 | "(assumed)" |
| NEDO-33926 cement-type limit | "the public topical report does not, to our reading, state a cement-type limit"; or keep "whether it limits cement type is not yet known" |
| GenCost A$387–641 alternative | Keep as a conditional in §7.3 only: "if A$387–641 is the 2030 range, the ratios become 5.0× and 19.1×" |
| Liddell closure | "approved to close by April 2023 (Australian Energy Regulator, 2021) and closed that month (AGL Energy, 2023)". If no AGL source is found, drop "that month" and write "since closed" |
| SMR definition | "(International Atomic Energy Agency, 2024)": class A |
| Pillai et al. 2019 (C1 main case) and Ostrołęka PIS 2023 | **Cannot be cut** (C1's basis). Victor adds both entries to the references today |
| arXiv:2504.02599 (enrichment, burnup) | Cite with authors if found. Otherwise present 3.8% and 45 GWd/t as "(assumed; typical BWR reload values)" and drop the citation |

### C. Cut if not sourced before assembly (no primary or source exists)
| Claim | Location | Action if unsourced |
|---|---|---|
| Ontario slag supply shrinking (blast furnace to EAF) | §4.3 point 2; §6.3 finding 3 | Cut both. Finding 3 ends: "the specification should accept whichever low-clinker binder qualifies first" |
| St Marys Cement LC³ / calcined-clay capability | T1 | Cut the clause |
| Slag precedent in nuclear concrete, "[TODO: authors] 2026" | §6.3 finding 3 | Cut unless the Springer s40069-026-00964-8 authors are found |
| 76,950-worker shortfall (Defence Connect, n.d.) | §3 row 7; T12 | Cut the number. Keep the qualitative AUKUS-competition point with its sourced citation (Joint Standing Committee on Treaties, 2024) |
| Rosatom stakes in Kazakh mines | T3 note | Cut from the body (B2.5 "not assessed") |
| okdiario basemat geometry (37 m, 35 m) | §6.2 | Out of the body after the re-base (App A3 cross-check, labelled news-derived) |
| "Ontario coal ended 2014" | §1 | Cut the date (class A wording in §2 above) |
| Granta EduPack results or "due Thu" | §2, §6.1, §6.5, A9 | If not run: one sentence in §6.1 + §11 limitation; A9 retitled "Granta inputs prepared, not run". Never quote a Granta number |
| GenCost 2025-26 SMR values | §7.3, §8.2 table | Cut the row and the TODO; keep at most "still ranks SMRs highest-cost (Graham and Hayward, 2026)" |
| 2025 EPBC reforms changing s 140A | T7 | Cut from T7; one §11 limitation clause |
| Silex/GLE Paducah | §8.3 ¶4 | Context card: GO. Hedge class B ("NRC docketed the application in August 2025, as reported by Silex Systems, 2025") |

## 5. Rubric statement (this job)
- **R5.3 (concise, 15–20 pages):**
  - Produced: a per-section budget to 18.5 p of text and tables (figures excluded, per the brief), with gates, reserve cuts and the cut order.
  - Missing: execution and the rendered page check. It stays **Partial** until the docx body measures ≤ 19.5 p.
- **R1.5 (no irrelevant material):**
  - Produced: 21 duplicated items each given one home; working text (rubric IDs, TODOs, file paths, Granta "due" notes) listed for deletion.
  - Missing: execution.
- **R5.1 (logical flow):**
  - Produced: one home per item. §2 becomes the methods home and §11 the answers home, so each section leads with its point.
  - Missing: the post-cut flow read (Q21).
- **All other IDs:** each section lists the evidence its HD descriptor needs, and that evidence is kept or moved to an appendix, never deleted.
  - Risk to **RB.3, RB.4, RB.7 and R1.4 (patents):** they depend entirely on Leroy delivering §4.1, §5, §10 and App E inside 1,250 words.
  - Risk to **R2.3 and R4.3:** the C1 break-even days and carbon value must be re-run for the re-based saving before any section quotes them.
