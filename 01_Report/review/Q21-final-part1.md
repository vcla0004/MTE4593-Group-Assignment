Rubric coverage: R1.1–R1.5, R2.1–R2.7, R3.1–R3.8, R4.1–R4.4, R5.1–R5.5, RB.1–RB.8

# Q21 final pre-submission review, part 1 (examiner, 25/10/2026, 14:15 AEDT)

**Scope.** This review covers the whole assembled report except:
- §6, Appendix A and Appendix C: the LCA re-base, due 18:00.
- Leroy's §4.1, §4.2, §5, §10 and Appendix E: placeholders, due 18:00.

Those parts are covered here only where they block another section (§3 and §4 below).

**What I read.** `01_Report/assembly/draft-assembled.md`: the `--final` build on disk, with the title page, page breaks and `references-cited.md` as the reference list. It was rebuilt while I was reading it, and only the page-break blocks changed.

**Limits of this check:**
- **I could not run `assemble_draft.py`: there is no shell in this session.** All word counts here are my hand estimates (±10%). Before submission the coordinator must run the script (gate 1) and measure the rendered docx (gate 2).
- There are no page numbers until the docx is rendered, so evidence cites section and paragraph.
- "Current text" quotes come from the section files, which still carry the pre-assembly table labels (T15, T1, T6 …). The script renumbers these, so don't hand-edit them.

## 0. Verdict

On R3, Victor's sections and the shared sections are at HD level. On R2 they are sound.

Three things keep the printed report at D:
1. **Working debris is visible:** TODOs on the title page and in the AI declaration, a heading that reads "appendix-E-search-log.md", and in Appendix B a "Coordinator: merge …" note and a duplicate B8.3.
2. **The final reference list is missing at least 23 cited sources.** `check_refs.py` drops every narrative "Author (Year)" citation.
3. **§6 still carries the old C1 case**, which contradicts §4.3, §7, §9 and §11.

The must-fix list (§2) takes about 85 minutes of writer time plus 15 minutes of script work, and it removes about 110 body words net.

**Estimated mark: now ≈ 17.5/25 (70%, D).** With the must-fixes applied, and with §6 and Leroy's sections landing as specified in §4: **≈ 20/25 (80%, borderline HD).**

## 1. Grades per criterion

| Criterion (weight) | Now | If §2 and §4 are done | HD phrase being missed | Evidence | What reaches HD |
|---|---|---|---|---|---|
| R1 Research coverage (5%) | C/D, 3.4 | HD, 4.1 | "Comprehensive coverage of **all** significant and relevant aspects"; "a wide range of highly relevant sources" | **Strong:** §3 T1 (8 barriers, waste included); §8.1–8.5; synthesis in §7.2 ¶2 (Coalition 2035 vs CSIRO 2040), §8.2 Cost (C$198 vs OPG C$149 vs GenCost, not independent), §8.3 ¶2–3 (WNA vs WNU; Red Book 2024 vs 2026) and §8.4 ¶1 (61% vs 59%). **Missing:** technology state, projects, patents, materials chain, future materials (all Leroy placeholders). The printed list drops at least 23 cited sources | Leroy per §4a; M1 |
| R2 Technical (8%) | D−, 5.6 | HD−, 6.4 | "Calculations … appropriate to the scale of the proposal"; "Arguments are logical"; "where feasible, an eco-audit" | **In scope, strong:** §7 T6 and B5 (break-even), B4 (displacement), B6 (same money), §8.2 C1 ¶ (premium, abatement cost), B2.6 (fuel demand) and B7 (MCDA), each with a worked example and a reproduce command. **Against it:** (1) §6 still gives 1,740 t, 9–15 days and C$0.49–0.60 m, where every other section gives 2,200 t, 11.6–18.5 days and C$0.63–0.76 m. (2) C1's 20,000 m³ eligible volume is 97% of §6's whole-plant 20,700 m³. (3) §2 reads "Granta was used for [TODO-GRANTA]". (4) Scope and ratio slips (M5, M12) | §4b; M4, M5, M11, M12 |
| R3 Non-technical (6%) | HD−, 4.8 | HD, 5.0 | Met. Small gap on "supported by evidence": the C$149 and GenCost figures rest on "as reported" with no secondary named | §8.1 + T7 + B1; §8.2 + T8 + B6; §8.3 + T9 + B2; §8.4 + T10 + B8; §8.5 F8 + T11; §8.6 T12, sequencing, 130% trap; §9 T14 and robustness tests | M11, M14; P5 checks |
| R4 Originality (3%) | D, 2.1 | D+, 2.3 | "identifies less intuitive or indirect opportunities"; "new feasible ideas or connections that are not immediately apparent" | §4.3 "Why it is not the obvious choice": point 1 (DPSC infill problem) is good; point 2 argues displacement, not originality. Real connections exist but are scattered: schedule value (§7.1), tranche lever (§8.6), Silex/GLE (§8.3), 130% trap (§8.6). §10 is missing | M9; Leroy's §10 |
| R5 Presentation (3%) | P, 1.6 | HD−, 2.4 | "Professional level presentation"; "Consistent referencing"; "Very few errors in … formatting"; "appropriately structured" | Title page: "[TODO: student ID]" ×3 and "Sam [TODO: surname]". AI declaration is a TODO. A "## appendix-E-search-log.md" heading. App B: "Coordinator: merge …", "Moved sentence …", duplicate B8.3/B41, stale table labels. Text says "Figure F6", caption says "Figure 6". No §4 or §8 parent headings. The list lacks AISC, EFNARC, CRSI 2017, Steigerwald, IPCC 2006, Kazatomprom … | M1, M2, M3, P5 |

**RB items** (assessed through the criteria above)

| ID | Now | Evidence and what is missing |
|---|---|---|
| RB.1 | HD | §4.3 ¶2 and T2 give all four elements: Darlington Units 2–4 at Clarington; 50,000 m³ per unit, 20,000 m³ eligible, 2,200 t per unit, 6,600 t in total; non-safety works first, DPSC infill only if qualified; LC³ (Pillai et al., 2019) with slag as fallback; schedule-neutral. Ostrołęka and Pillai have not been opened (P5) |
| RB.2 | HD | §3 T1: eight barriers, each with a number, source, why it matters and whether C1 touches it |
| RB.3 | Partial | Done: "how … to address these barriers" (§3 T1 C1 column, §4.3). Missing: "current state of your chosen technology" (Leroy §4.1–4.2) |
| RB.4 | Missing | The brief asks for a "Technical description of the production and usage of the improved material(s) … from extraction and processing through to end-of-life". No body text covers LC³ production or end of life (Leroy §5) |
| RB.5 | D | App B1–B8 give formula, inputs, worked example, sensitivity and reproduce command. Open: App A/C pending; App B debris (M2) |
| RB.6 | D | §8.2 Cost ¶, T8 and B6.3 compare our LCOE with OPG and GenCost and explain the gap. §6.5's IPCC AR5 row is still a TODO (§4b) |
| RB.7 | Missing | The brief: "Suggest any new materials properties and process solutions". §10 is missing, yet §4.3, §6.3, §8.3 and §11 all point to it |
| RB.8 | HD | §9: T13 (every cell traced), T14, rank-reversal tests and the verdict. Fact-checked (final-part1) |

**Estimated mark /25:**
- **Now:** 3.4 + 5.6 + 4.8 + 2.1 + 1.6 = **17.5**.
- **Projected:** 4.1 + 6.4 + 5.0 + 2.3 + 2.4 = **20.2**.
- R2 moves only if §6 becomes consistent. R1, RB.3, RB.4 and RB.7 move only if Leroy delivers.

## 2. Must-fix list (about 85 writer-minutes plus 15 script minutes), ranked by marks per word

Every item that adds body words names its offset. The net ledger is at the end of this section.

| Rank | Item | IDs | Owner | Min | Net body words |
|---|---|---|---|---|---|
| 1 | M1 Complete the reference list | R5.4, R1.4 | Coordinator + writer B | 20 | +5 (caption) |
| 2 | M2 Strip working debris from App B | R5.5, R1.5, R2.4 | Writer B | 20 | 0 (App B about −200) |
| 3 | M3 Final-build script fixes | R5.5, R5.1, R2.4 | Coordinator | 15 | −7 |
| 4 | M4 Granta sentence | R2.2, R5.5 | Writer A | 2 | +4 (+5 in §11) |
| 5 | M5 C1 scope and ratio consistency | R2.6, R5.1 | Writer A/B | 10 | +4 |
| 6 | M6 §11 answers RQ4 in full | R5.1, R1.2 | Writer A | 3 | −7 |
| 7 | M9 §4.3 states the originality | R4.1, R4.3 | Writer A | 3 | +4 |
| 8 | M7 §8.6 to budget | R5.3, R1.5 | Writer B | 8 | −59 |
| 9 | M14 In-text author forms | R5.4 | Writer A/B | 10 | −10 |
| 10 | M11 T13 overclaim; MCDA option defined | R2.6, R3.6 | Writer A | 3 | +9 |
| 11 | M12 + M13 §7.3 condition; duplicate Liddell closure | R2.7, R1.5 | Writer A | 3 | −10 |
| 12 | M8 §8.3 and §8.5 offsets | R5.3, R1.4 | Writer B | 5 | −33 |
| 13 | M10 §1/§2 abbreviation and date | R5.3 | Writer A | 3 | −16 |

The title page and the AI declaration are human items (P5).

### M1. Complete the reference list (R5.4 "Consistent referencing")

**Problem 1: the final list drops cited sources.** `check_refs.py` line 47 does not allow "(" between the author and the year, so it drops every narrative "Author (Year)" citation. The `--final` build then prints that filtered list. At least these 23 cited sources are missing:
- AISC (2022); CNSC (2021; 2026a; 2026b); Cement Association of Canada (2022); CRSI (2017); EFNARC (2005)
- Geneski et al. (n.d.); Slag Cement Association (n.d.); Steigerwald et al. (2023); IPCC (2006); Canada Energy Regulator (n.d.)
- Government of Ontario (n.d.); IESO (2024); TAF (2021); Kim and Macfarlane (2026); Bowen (2025); ABC News (2026)
- Kazatomprom (2025); AEC (2019); Municipality of Clarington (2024); DISER (2020); Parliament of NSW (2025)

**Fix.**
1. Delete `01_Report/assembly/references-cited.md` before running `assemble_draft.py --final`. The script then falls back to `12-references.md`, cleaned.
2. In `12-references.md`, delete the six entries that are cited nowhere: Defence Connect (n.d.); International Atomic Energy Agency (2015); Ng et al. (2025); Parliamentary Library (2023); Treasury Board of Canada Secretariat (2025); US Nuclear Regulatory Commission (n.d.).

**Problem 2: six cited sources have no entry anywhere.** Add them. Square brackets mark descriptions, not invented titles.
- OECD Nuclear Energy Agency and International Atomic Energy Agency, 2026. *Uranium 2026: Resources, Production and Demand*. [pdf] Paris: OECD Publishing. Available at: https://www.oecd-nea.org/jcms/pl_121658/uranium-2026-resources-production-and-demand [Accessed 20 October 2026]. (sources.md l. 548; cited in B2.5)
- Power Engineering, 2023. OPG selects first fuel suppliers for its small modular reactors. *Power Engineering*. [online] Available at: https://www.power-eng.com/nuclear/smrs/opg-selects-first-fuel-suppliers-for-its-small-modular-reactors/. (sources.md l. 586; cited in §8.3)
- Silex Systems Limited, 2025. [ASX announcement on the NRC's acceptance of GLE's Paducah licence application], 6 August. Sydney: ASX. Available at: https://announcements.asx.com.au/asxpdf/20250806/pdf/06mkwks19y2zck.pdf. (sources.md l. 971)
- Silex Systems Limited, 2026. [ASX announcement on Cameco's offtake agreement for the Paducah Laser Enrichment Facility], 16 September. Sydney: ASX. (sources.md l. 976)
- World Nuclear News, 2026. Cameco in offtake agreement for US laser enrichment plant. *World Nuclear News*. [online] Available at: https://www.world-nuclear-news.org/articles/cameco-in-offtake-agreement-for-us-laser-enrichment-plant. (the secondary named in M8b)
- World Nuclear University, 2025. [Enrichment: WNU Summer Institute presentation slides], 17 June. Available at: https://world-nuclear-university.org/SummerInsituteFiles/2025-06-17_WNU_Enrichment_Platov_final_62a48c29.pdf. (sources.md l. 1011; cited in §8.3, B2.2)
- Under a new subheading `### Cases` after Legislation: *Barngarla Determination Aboriginal Corporation RNTBC v Minister for Resources* [2023] FCA 809 (Federal Court of Australia, Charlesworth J, 18 July 2023). Available at: https://www.judgments.fedcourt.gov.au/judgments/Judgments/fca/single/2023/2023fca0809 [Accessed 21 October 2026]. (sources_run6.md l. 199)

**Problem 3: citations and entries that don't match.**
- **T8 vendor row.** US$2,250/kW is uncited; Rao et al. is its source (economics brief l. 67). In the §8.2 caption source line, change "Graham, Hayward and Foster (2024); Steigerwald et al. (2023)." to "Graham, Hayward and Foster (2024); Rao, Kaffine and Hodge (2026); Steigerwald et al. (2023)." (+5 words, offset in M8c.)
- **B6.3.** "GenCost 2024-25 gives an SMR value of up to A$487 (`results/lcoe.md` §5)" becomes "… A$487 (Graham, Hayward and Foster, 2025; `results/lcoe.md` §5)".
- **Hooton.** Victor opens the URL (concrete.org is not blocked) and copies the title. Otherwise, replace "*Changes to ASTM cement and concrete standards to…* [title truncated in source entry]." with "[Webinar slides on changes to ASTM cement and concrete standards]."
- **Parliament of NSW, list entry.** "Parliament of New South Wales, Legislative Assembly, 2026. *Notice Paper*." becomes "Parliament of New South Wales, 2026. *Legislative Assembly Notice Paper*."
- **Parliament of NSW, App B Tables B1 and B3.** "(2025–26; 2026)" becomes "(2025; 2026)".

### M2. Strip working debris from Appendix B (R5.5 "Very few errors in … formatting"; R1.5)

Edits in `appendix-B-policy-and-supply-working.md`:

1. **Intro table, row B3.** "none: hand calculation (qualitative scoring; totals checked in fact-check batch 1a) | Law brief §5 |" becomes "none: hand calculation (qualitative scoring) | Table B13 |".
2. **Internal brief references.** Delete:
   - "; law brief §3–4" (Table B1 source)
   - " (law brief §4)" twice (B1.1 order of removal; Table B3 row 2)
   - " (law brief §5)" twice (Tables B13 and B14 sources)
   - " (route brief §5)" twice (B3.1)
3. **B1.2 step 4.** The current text is arithmetically unclear: 32 + 6 = 38, not 37. "**36** (3 short); at most 37 (2 short) if a count of six other crossbenchers is used" becomes "**36** (3 short); **37** (2 short) on the alternative count in step 7".
4. **B2.5.** Delete "*Note moved from §8.3 (Table T3).* " and keep the rest of the paragraph.
5. **Table B35** becomes **Table B12a**. It currently sits between B12 and B13.
6. **B14a caption.** "*Table B14a. T16 lever scores and weight test.*" becomes "*Table B14a. Lever scores and weight test for Table T16.*"
7. **"The deck's value".**
   - Table B15: "Assumption (the deck's value; an OPG filing gives 315)" becomes "Assumption (an OPG filing gives 315)".
   - Table B16: "Ontario average 2023 (energy snapshot; the deck's value)" becomes "Ontario average 2023 (energy snapshot)".
8. **Table B29, legal row.** "route A rescored to 6 after fact-check M2, which leaves this input unchanged" becomes "route A scores 6, which leaves this input unchanged".
9. **B8.3.**
   - Heading: "#### B8.3 Social-licence routes for an SMR at Liddell (Table T13)" loses " (Table T13)". That old table is no longer in the body, and the label now means §9's table.
   - Table B39 source: append "; route models from Newcastle Herald (2024b), NWMO (2024a; 2024c) and Williams Treaties First Nations et al. (2026)". This is the only citation of Newcastle Herald 2024b.
   - Reading: append "R4 (no SMR) scores highest under every weighting, so on social licence alone the Australian SMR case is weaker than the alternative (§9)."
10. **B8 head.** After the B8 Result paragraph, paste the source list from the moved file, from "Sources for Table T12 (Social licence at Darlington and at Liddell): Neelam (2024); …" to "… Slovic (1987)."
    - Delete "Australian Energy Market Operator (2025); " from it: no T12 cell uses AEMO.
    - Don't copy "Deaths avoided are calculated …" or "Two T12 items shortened in the body: …".
11. **B8 Limits.** "Job and waste figures in T12 (CBoC, NWMO) are taken from the briefs" becomes "Job and waste figures in Table T12 (Conference Board of Canada, 2021; NWMO, n.d.) are taken from those sources".
12. **B8.2 heading.** "(Figure 8)" becomes "(Figure F8)".
13. **`assemble_draft.py` line 49.** Delete `"appendix-B-moved-from-8.4-8.6.md",`. That file holds the "Coordinator: merge …" note, the duplicate B8.3 and Table B41, and the "Moved sentence …" line. Items 9 and 10 have already taken what is worth keeping.

### M3. Final-build script (coordinator; R5.5, R5.1 "appropriately structured")

**(a) Appendix references to body tables.**
- **The fault.** Appendices are not renumbered, so they still use the old labels: B3.1 "Table T16" (now T12), B7 "Tables T4 and T5" (T13, T14), B8.4 "(Table T14)" (T11), "Table T12" in B8 (T10), and App C "Table T8" and "Table T9" (T4, T5).
- **Why not by hand.** Leroy's T2 will shift every number again, so fix it in the script.
- **Why this regex.** It touches only "Table(s) T…" and leaves the grid cases NEM-T1, T1 and T2 alone.
```python
# renumber_tables(): last line
    return out, first
# main():
    parts, first = renumber_tables(parts)
APP_T = re.compile(r"\b(Tables?) T(\d+[a-z]?)(?:( and )T(\d+[a-z]?))?\b")
def renum_app(text, first):
    def sub(m):
        s = f"{m.group(1)} T{first.get(m.group(2), m.group(2))}"
        return s + (f"{m.group(3)}T{first.get(m.group(4), m.group(4))}" if m.group(4) else "")
    return APP_T.sub(sub, text)
# in the appendix loop:
            parts.append(renum_app(clean(f.read_text(encoding="utf-8")), first))
```

**(b) Figure labels.** The text says "Figure F6", but captions print "Figure 6.". In `figure()`, change `f"![Figure {n}. {caption}]…"` to `f"![Figure F{n}. {caption}]…"`. This matches the "Table T6." style.

**(c) Parent headings.** §4.1–4.3 and §8.1–8.6 are level-2 headings with no parent, so the contents page reads "3, 4.1, 4.2, 4.3, 5 … 7, 8.1". Fix it right after `body` is built in `main()`. Skip the PARENT line if Leroy's file already opens with "## 4 ".
```python
PARENT = {"4.1-technology-projects.md": "## 4 The technology and the initiative\n\n",
          "8.1-law-regulation-licensing.md": "## 8 Non-technical factors affecting translation to practice\n\n"}
if name[:2] in ("4.", "8."):
    body = re.sub(r"^(#{2,5}) ", r"#\1 ", body, flags=re.M)
body = PARENT.get(name, "") + body
```

**(d) Appendix E.** If `appendix-E-search-log.md` is not in `sections/` at the final build:
- Remove it from APPENDICES. Otherwise the placeholder prints the raw filename as a heading.
- Delete §2's "**Search strategy and patent search:** Appendix E." (−7).

**(e) References.** See M1, step 1.

### M4. §2 Granta sentence (R2.2; the brief says "use Granta EduPack … where it is feasible")

- **Current:** "The screening model is scripted in Python and Granta was used for [TODO-GRANTA]."
- **If not run by the freeze:** "No Granta EduPack Eco Audit was run; the equivalent scripted model is in §6.1 and Appendix A." (+4)
  - Also in §11: "A screening LCA, not critically reviewed;" becomes "A screening LCA, not critically reviewed, with no Granta EduPack run;" (+5, offset by M6).
- **If Victor runs it:** "Granta EduPack's Eco Audit cross-checks the construction materials of the C1 structures (Appendix A9)."
- §6.1 must say the same thing (§4b).

### M5. C1 scope and ratio consistency (R2.6 "Arguments are logical"; R5.1)

- **(a) §4.3 ¶1.** "…, cancels C1's whole saving (§7.1)." becomes "…, cancels that unit's saving (§7.1)." The whole Units 2–4 saving takes 35–55 days (T6).
- **(b) §4.3 T2 Saving cell.** "about 0.4% of a unit's life cycle" becomes "about 0.37% of a unit's life cycle".
- **(c) §7 lead.** The ratio is carrying cost alone (B5.4), not carrying cost plus deferred output.
  - Current: "A one-month slip of Units 2–4 costs C$33–110 m in carrying cost and defers about C$88 m of output: 29–175 times the carbon value of C1's whole saving."
  - New: "A one-month slip of Units 2–4 costs C$33–110 m in carrying cost alone, 29–175 times the carbon value of C1's whole saving, and defers about C$88 m of output." (+1)
- **(d) §11 lever 1.** "costs 20–175 times C1's carbon value (§7)" becomes "costs 29–175 times C1's carbon value (§7)". The 20× low end includes the superseded C$170/t path; §7 and B5.4 use the current path.
- **(e) §9.2 "SMR + C1 …" paragraph.** At Darlington 18.5 days is exactly the break-even, a 1× ratio (§7.1); the 15× figure is the Liddell displacement (B7.5).
  - Current: "An 18.5-day slip would leave 15 times the saving unavoided (Appendix B7.5), so schedule neutrality decides whether C1 helps."
  - New: "At Liddell, an 18.5-day slip would forgo CO₂e equal to 15 times the saving (Appendix B7.5), so schedule neutrality decides whether C1 helps." (+4)
- **(f) §3 T1 row 4.** "Russia holds 42.8% of enrichment (§8.3)" becomes "Russia holds 41–43% of enrichment (§8.3)".
- **(g) §11 RQ3.** "A Darlington unit avoids 1.0–6.8 Mt" becomes "Darlington Unit 1 avoids 1.0–6.8 Mt", as in §7.2 and T13.

### M6. §11 answers RQ4 in full (R5.1 "logical flow"; R1.2)

RQ4 asks which barriers decide and whether an SMR beats firmed renewables. §11 answers only the second half.
- **RQ4.**
  - Current: "Renewables rank first under all four weight sets (equal weights: 80 against 30 for an SMR, with or without C1)."
  - New: "Law (three bans), cost (C$149–198/MWh) and time (2040 at the earliest) decide; firmed renewables rank first under all four weight sets (80 against 30 with equal weights)." (+6)
- **Offset in RQ2.** "(1,100–3,300 at 20–60% eligible; BWRX-300 Ostrołęka sp. z o.o., 2023; Pillai et al., 2019)" becomes "(1,100–3,300; §4.3)" (−12).
- **Offset in RQ1.** Delete the second "(§6)" (−1).

### M7. §8.6 to budget (R5.3 "concise")

My estimate puts §8.6 about 21% over its 480-word target.
- **(a) Lead (−37).**
  - Delete: "If enforceability counts double, L2 leads with 11; if speed counts double, L1 leads with 11; the recommendation is the same under both. L1 is C1's pilot step, not an add-on: a 10% floor invites LC³, whose full saving is 1,100–3,300 t CO₂e per unit (§4.3; Pillai et al., 2019)."
  - Replace with: "Doubling either enforceability or speed changes which leads, not the recommendation (Appendix B3.1)."
- **(b) Qualification paragraph (−22).**
  - Current: "Step 1, in 2027, develops slag and LC³ self-consolidating mixes (about 6 to 9 months). Step 2 is a full-scale mock-up trial off Unit 1's critical path (about 6 months), funded by L4. Step 3 is the design-change evaluation, submitted with the Units 2–4 licensing package ahead of the approval expected in 2028, as reported (American Nuclear Society, 2026); it takes about 6 to 9 months (assumed)."
  - New: "Step 1 (2027) develops slag and LC³ self-consolidating mixes (6–9 months); step 2 trials them on a full-scale mock-up off Unit 1's critical path (about 6 months, funded by L4); step 3, the design-change evaluation, goes with the Units 2–4 licensing package (6–9 months, assumed)."
  - The 2028 approval stays cited in §8.1's lead.

### M8. Offsets in §8.3 and §8.5 (R5.3; R1.4)

- **(a) §8.3.** Delete the line under T9: "*Note: High is above 1,800 (2023) and above 2,500 (2010). Sensitivity and limits: Appendix B2.4–B2.5.*" (−18). The lead already gives both scales, and the caption cites Appendix B2.
- **(b) §8.3.** "(Silex Systems Limited, 2026, as reported)" becomes "(Silex Systems Limited, 2026, as reported by World Nuclear News, 2026)" (+5). §2's own rule requires the secondary to be named.
- **(c) §8.5 ¶2 (−20).**
  - Current: "That model needs a publicly owned utility with a regulated rate base. Liddell has a private owner, so it would need Commonwealth ownership or underwriting (§8.2), with taxpayers carrying the cost risk under the Coalition's 2024 model, as reported by ABC News (2024)."
  - New: "That model needs a publicly owned utility with a regulated rate base; Liddell's private owner would need Commonwealth ownership or underwriting instead (§8.2)."
  - §8.2 is the home of the ownership point, and ABC News (2024) stays cited in §7.2 and B3.

### M9. §4.3 states the originality (R4.1 "Goes beyond obvious applications"; R4.3)

- **Replace the second point of "Why it is not the obvious choice":** "Second, C1's value depends on timing rather than on the concrete: counted from when each plant could actually run, a Darlington unit avoids 1.0–6.8 Mt CO₂e to 2050 and a Liddell unit 0.67–3.9 Mt, the same order of magnitude (§7), and Darlington is where a qualified mix can be built."
- **With:** "Second, C1's value is set by schedule, not by the concrete: under three weeks of delay to a unit cancels its saving (§7.1), so C1 is a qualification programme timed to Unit 1 mock-ups rather than a binder swap. Third, its lever is financial: the Units 2–4 equity tranche can carry the condition (§8.6)." (+4)
- The displacement comparison keeps its home in §7.2.

### M10. §1/§2 abbreviation and date (R5.3)

- **§1.** "(Department of Climate Change, Energy, the Environment and Water, 2025)" becomes "(Department of Climate Change, Energy, the Environment and Water [DCCEEW], 2025)" (+1).
- **§2 and §7.2 ¶1.** The same citation becomes "(DCCEEW, 2025)" (−8 each).
- **§2.** "Start years are October 2030 at Darlington" becomes "Start years are 2030 at Darlington" (−1), as in §1, §3, §7.2 and B15.

### M11. T13 overclaim; define the MCDA option (R2.6, R3.6)

- **(a) §9.1 T13, Economy row, Liddell cell.** "No private owner could finance a first unit." becomes "A first unit would need Commonwealth ownership or underwriting (our inference, §8.2)." (+4)
- **(b) §2 MCDA.** "(status quo, SMR at Liddell, SMR plus C1, firmed renewables)" becomes "(status quo, one SMR at Liddell, the same SMR built with C1's concrete, firmed renewables)" (+5).
  - Why: C1 is defined for Darlington, but the MCDA applies it to a Liddell unit, and the text never says so.

### M12 and M13. §7 (R2.7; R1.5)

- **M12, §7.3.** 4.9× needs both conditions (Table B28: 198/153).
  - Current: "They still avoid 5.7× more in the worst case we tested for them, and 4.9× if the SMR costs only A$198 (Appendix B6, Table B28)."
  - New: "They still avoid 5.7× more in the worst case we tested for them (SMR A$230, renewables A$153), and 4.9× with the SMR at A$198 (Appendix B6, Table B28)." (+5)
- **M13, §7.2 ¶4 (−15).** "Liddell was approved to close by April 2023 (Australian Energy Regulator, 2021) and has since closed, so an SMR there would displace the NEM mix, not Liddell's coal." becomes "An SMR at Liddell would displace the NEM mix, not Liddell's coal (§1)."

### M14. In-text author forms (R5.4)

- **§1.** "…licence to construct at Darlington in April 2025 (Canadian Nuclear Safety Commission, 2025)." becomes "…Canadian Nuclear Safety Commission (CNSC) licence to construct at Darlington in April 2025 (CNSC, 2025)." (−2)
  - Why: "CNSC" is used from §8.1 T7 onward but is defined only in §8.4.
- **§8.4.** "the Canadian Nuclear Safety Commission (CNSC) found" becomes "the CNSC found" (−5).
- **§8.6.** "A Canadian Nuclear Safety Commission licence condition" becomes "A CNSC licence condition" (−4).
- **§4.3 T2 Condition.** "US Nuclear Regulatory Commission and Canadian Nuclear Safety Commission, 2025" becomes "US Nuclear Regulatory Commission and CNSC, 2025" (−3), as in §8.1.
- **§8.3, B2.3 and B2.5.** "OECD NEA and IAEA" (never defined) becomes "OECD Nuclear Energy Agency and International Atomic Energy Agency" (+4 in the body).

**Net word ledger (body):**

| Change | Words |
|---|---:|
| M1 caption | +5 |
| M3d | −7 |
| M4 | +4 |
| M4 §11 clause | +5 |
| M5 | +4 |
| M6 | −7 |
| M7 | −59 |
| M8 | −33 |
| M9 | +4 |
| M10 | −16 |
| M11 | +9 |
| M12/M13 | −10 |
| M14 | −10 |
| **Net** | **≈ −110** |

**Pages, from my estimates:**
- In-scope sections are now about 6,400 words (budget 6,200), or about 6,300 after the fixes.
- Over the 10% tolerance today: §8.6 (+21%), §2 (+16%) and §8.3 (+11%). The fixes bring each within it.
- With §6 at 1,800 and Leroy at 1,250 words, the body is about 9,350, against the 9,500 gate.
- The script counts figure-caption lines as prose, so gate 1 is conservative. Gate 2 (rendered pages ≤ 19.5) governs.

**Reserve cuts if a gate fails**, applied before the final-cut-budget's R1–R5:
- §9.3 Limits: delete "The status quo's lead over the SMR depends on the scaling; only "renewables first" is robust to it." (−19; it repeats the scaling-artefact paragraph).
- §3 lead: "At Darlington, Ontario, cost and schedule bind. At Liddell, the closed New South Wales coal plant we use as the Australian comparison, law comes first and every later barrier is still open (§8.1–8.5)." becomes "At Darlington cost and schedule bind; at Liddell law comes first and every later barrier is still open (§8.1–8.5)." (−14)

## 3. Cross-section consistency problems

| # | Problem | Where | Exact fix |
|---|---|---|---|
| X1 | Month's-slip ratio: 29–175× (current carbon-price path) against 20–175× (includes the superseded C$170 path) | §7 lead; §11 lever 1 | M5c, M5d |
| X2 | 18.5 days "cancels" the saving (§7.1 T6) against "leaves 15 times the saving unavoided" (§9.2). These are two sites, and §9.2 doesn't say so | §9.2 | M5e |
| X3 | §4.3 says 11.6–18.5 days cancels "C1's whole saving". T6 says that delay cancels one unit's saving; the whole saving takes 35–55 days | §4.3 ¶1 | M5a |
| X4 | Share of the life cycle: 0.37% (abstract, §9, §11, B7.5); "about 0.4%" (T2); "0.3%" (§6) | T2; §6 | M5b; §4b |
| X5 | Russia's enrichment share: 42.8% (§3 row 4) against 41.0–42.8% (§8.3, B2) | §3 T1 | M5f |
| X6 | §6 (lead, §6.3 T4, findings 2 and 5, closing sentence, F3 caption) uses the old case: 1,740 t, 5,200 t, 9–15 days, 1.3–1.4 days, C$0.49–0.60 m, C$12.6–15.2/m³. Every other section uses the deck case: 2,200 t, 6,600 t, 11.6–18.5 days, 1.7–1.8 days, C$0.63–0.76 m, C$10.4–12.7/m³ | §6 | §4b items 1–2 |
| X7 | C1's eligible 20,000 m³ is 40% of Ostrołęka's 50,000 m³, but §6 models the whole plant as 20,700 m³ and 9,900 t of steel (Ostrołęka: 14,000 t). These numbers depend on the answer: 4.2 g/kWh (B4.1, B6, B7 MCDA), 7.5% construction (§3 row 5), 0.37%, and 3,714 t (§11 lever 3) | §6 vs §4.3/T2 | §4b item 2: one decision, then every dependent number updated in one pass |
| X8 | "LC³" in §1–§11 against "LC3" in §6, App A and App C | §6, Apps A, C | §4b |
| X9 | Appendices cite body tables by their old labels: B2.5 T3, B3.1 T16 ×2, B7 T4/T5, B8.3 T13, B8.4 T14, B8 T12 ×4, App C T8/T9 | Apps B, C | M3a; M2 items 4, 6, 9, 11 |
| X10 | Text says "Figure F1–F8"; captions say "Figure 1–8"; B8.2 says "(Figure 8)" | All | M3b; M2 item 12 |
| X11 | Appendix table order: B35 sits in B2.6 between B12 and B13. B39 and B41 duplicate each other | App B | M2 items 5 and 13 |
| X12 | Author forms: CNSC (undefined before §8.4); "US NRC and CNSC" (§8.1) against the full name (§4.3); "OECD NEA and IAEA"; "Parliament of New South Wales" against the list's "…, Legislative Assembly"; "(2025–26; 2026)" | §1, §4.3, §8.1, §8.3, §8.4, §8.6, App B | M14; M1 |
| X13 | "as reported" with no secondary named breaks §2's own rule ("from the secondary source named"). Cases: GenCost (§7.3, B6, B24); OPG's C$149 (§3 row 1, §7.1, B5.4, B6.3); Silex 2026 (§8.3); Graham and Hayward 2026 (B6.3) | §3, §7, §8.3, App B | Victor opens GenCost 2023-24 and the OEB interrogatory (P5), then deletes "as reported". Otherwise name the secondary: NucNet (2024) for GenCost, as in sources_run5.md l. 14; WNN for Silex (M8b) |
| X14 | "a Darlington unit" (§11) against "Darlington Unit 1" (§7.2, T13) for the same 1.0–6.8 Mt | §11 | M5g |
| X15 | "October 2030" (§2) against "2030" (§1, §3, §7.2, B15) | §2 | M10 |
| X16 | Net-output range: 300 MWe (290–300) in B15 and B19, against (300–315) in §6 T3 | App B vs §6 | §4b: use one range |
| X17 | Pointers to content that doesn't exist yet: "Appendix E" (§2); "(§10)" in §4.3, §6.3, §8.3 and §11; "(§4.1–4.3, §5)" in §1 | §1, §2, §4.3, §8.3, §11 | §10 must contain the three items in §4a. If §10 or App E doesn't arrive, delete those pointers (M3d) |
| X18 | T8's vendor US$2,250/kW has no source. Rao et al. (2026) is in the list but cited nowhere | §8.2 T8 | M1 |
| X19 | B6.3 names "GenCost 2024-25" with no citation. The entry (Graham, Hayward and Foster, 2025) exists | App B6.3 | M1 |
| X20 | Headings: there is no §4 or §8 parent heading | All | M3c |

## 4. What §6 and Leroy's sections must contain (send these lists as they are)

### 4a. Leroy: §4.1, §4.2, §5, §10, App E (due 18:00; **≤ 1,250 words in total, tables included**; figures are free)

Use these filenames in `01_Report/sections/`: `4.1-technology-projects.md`, `4.2-bwrx300-darlington.md`, `5-materials-life-cycle.md`, `10-future-materials.md`, `appendix-E-search-log.md`. Cite as (Author, Year), add every new entry to `12-references.md`, write in Australian English, and leave no [TODO] or [TO VERIFY] markers.

**§4.1 Technology, projects, patents (≤ 450 words, including T2 at ≤ 120 table words).** Serves RB.3 ("current state of your chosen technology"), R1.1 (technology, timescales) and R1.4 (patents).
- [ ] One paragraph on where SMRs stand: about 70 designs (IAEA, 2024, already cited), and which are licensed or under construction. Don't redefine "SMR" (§1 does).
- [ ] Table T2 with the caption written as "*Table T2. …*" so the assembly renumbers it. At most six rows, with these columns: design | site | status | first power | source. Suggested rows:
  - BWRX-300 Darlington: licence 4 April 2025; Unit 1 in 2030 (CNSC, 2025; OPG, 2025a).
  - BWRX-300 at TVA Clinch River.
  - ACP100 Linglong One.
  - NuScale CFPP, cancelled 2023 (one cell only).
  - One European project.
- [ ] One TRL statement for the BWRX-300, with a source (§9 says TRL is not scored).
- [ ] 3–4 named US patents (number, assignee, year), one sentence each on what it protects and what it means for C1. Steel-plate composite modules and passive cooling are good targets. Entry format: "Assignee, Year. *Title*. US Patent X,XXX,XXX."
- [ ] One sentence on how the proposal addresses the barriers, pointing to §3 T1 (rows 2 and 5) and §4.3.
- [ ] Don't repeat NuScale costs (§8.2), licence months (§8.1 T7) or Coalition 2035 vs CSIRO 2040 (§7.2).

**§4.2 BWRX-300 at Darlington (≤ 200 words).** Serves RB.3.
- [ ] Design facts: 300 MWe (315 net in an OPG filing); natural-circulation BWR with passive isolation condensers; DPSC steel-composite modules filled with self-consolidating concrete; below-grade reactor building and shaft. Use sourced dimensions only.
- [ ] Unit 1: licence 4 April 2025, in service 2030, exactly as in §1, §3 and §7.2.
- [ ] If you have OPG, EIS or Clinch River concrete and steel quantities per unit, send them to the LCA member today. They settle X7.
- [ ] Leave out cost (§8.2), licensing detail (§8.1) and C1 (§4.3).

**§5 Materials from extraction to end-of-life (≤ 350 words, about 110 per chain).** Serves RB.4, which asks for "production and usage of the improved material(s) … from extraction and processing through to end-of-life".
- [ ] **LC³ concrete first: it is the improved material.** Limestone and clay; calcining the clay vs clinkering (temperatures and clinker share, cited to Scrivener et al., 2018, which is already in the list); self-consolidating infill (flow, heat of hydration in thick sections, shielding); end of life (activated concrete near the core; crushed and recycled as aggregate).
- [ ] **Uranium:** mining and milling (Saskatchewan ore), then conversion, enrichment and fabrication with the suppliers §8.3 names, then spent fuel and NWMO direct disposal. Give one material property or process fact per stage.
- [ ] **Steel:** ore or scrap, BF-BOF or EAF, plate and rebar, then activated vs clean steel at decommissioning.
- [ ] Cite §6.2 for emission shares and **don't quantify emissions** (§6 is their home). Use Figure F1 for the boundary; add no second flow diagram unless it replaces words.

**§10 Future material properties and processes (≤ 250 words).** Serves RB.7 and R4.2.
- [ ] (1) A low-clinker self-consolidating mix that flows, stays cool in thick sections, shields and can be qualified for nuclear use. §4.3 points here.
- [ ] (2) Low-carbon nuclear-grade steel plate and forgings (H₂-DRI/EAF), quoting §6.3's re-based whole-plant steel figure. §11 lever 3 points here.
- [ ] (3) Fuel-cycle processes: low-carbon conversion heat (the largest uncertainty, §6.4) and laser enrichment (Silex/GLE). §8.3 points here for "EPBC s 140A would bar such a plant in Australia".
- [ ] For each item: the property or process, the hotspot it addresses, one cited §6 number (don't recompute it), and its readiness or barrier.

**App E (R1.4).**
- [ ] The search log: databases, search strings, dates, hits and inclusion rules.
- [ ] The patent search: Google Patents query, date, hits and the patents kept.
- [ ] If App E isn't coming, tell Victor, so that App E and §2's pointer are deleted (M3d).

### 4b. LCA team member (Victor): §6, App A, App C (due 18:00; §6 ≤ 1,800 words, 1,650 prose plus 150 table)

**R1.1, R2.3, R2.6: consistency with the rest of the report.**
- [ ] **C1 numbers identical to the other sections:**
  - 2,200 t per unit (1,100–3,300 at 20/40/60% of 50,000 m³; 380 vs 270 kg CO₂e/m³, Pillai et al., 2019).
  - 6,600 t for Units 2–4.
  - 0.37% of the life cycle.
  - Break-even 11.6–18.5 days on the average factor and 1.7–1.8 days on the marginal factor, cited to §7.1 and T6.
  - No C$ values in §6 (their home is §8.2). Delete these from finding 2: C$0.16–0.20 m, C$0.49–0.60 m, 0.004%, C$12.6–15.2/m³, and the closing TBL sentence.
- [ ] **Settle X7 explicitly.** Choose one:
  - (a) Adopt Ostrołęka's 50,000 m³ and 14,000 t as the plant inventory and re-run. Then send the new median, construction share and whole-plant steel bound to the coordinator, so that §3 row 5 (7.5%), B4.1/B6/B7 (4.2 g/kWh), the 0.37% and §11 lever 3 (3,714 t) all change in one pass.
  - (b) Keep 20,700 m³ and say in one sourced sentence why Ostrołęka's figure is larger (whole site vs nuclear island).
  - Don't leave both numbers in the report unexplained.
- [ ] Keep the headline (median 4.2 g/kWh; range of medians 3.3–4.2; UNECE 5.1–6.4), or flag every downstream use if it moves.
- [ ] Keep the hotspot ranking and the vendor-vs-scale synthesis sentence (R1.3).
- [ ] Use one net-output range, the same as Table B15 (X16).

**RB.4 support.**
- [ ] The F1 stages and §6.2 shares match Leroy's three §5 chains, so he can cite §6.2 rather than recompute.

**RB.6.**
- [ ] Add IPCC AR5 to §6.5: "IPCC AR5 median 12 g/kWh, range 3.7–110 (Schlömer et al., 2014)". The entry is already in the list.
- [ ] Move T9 to App C7, leaving ≤ 60 words on the three largest discrepancy reasons.

**R2.2.**
- [ ] One Granta sentence that matches §2 (M4). Either drop the TODO from the A9 heading or cut A9.

**R5.5.**
- [ ] Remove every [TO VERIFY] and [TODO] in §6, App A and App C (about 100 now), using the hedges in final-cut-budget §4:
  - "[TODO: authors] (2025)" becomes "Sun and Kurosaki (2025)".
  - "Ontario Power Generation (2025)" becomes "(2025c)".
  - okdiario (2026): add an entry or cut the claim.
  - EN 15804: add an entry or cut the clause.
  - The ISO TODO: cite International Organization for Standardization (2006a; 2006b).
- [ ] "LC3" becomes "LC³" everywhere except inside quoted titles.
- [ ] F1–F5 captions: ≤ 35 words, no "| File: …" path, and no TODO in F5.
- [ ] Keep the pre-assembly labels ("Table T6/T8/T9", "[Figure F1. …]") so the script renumbers them.
- [ ] When T6 and T9 move out of the body, change every "Table T6" and "Table T9" reference (in §6 and App C) to "Table A2b" and "Table C7". Otherwise the old labels survive renumbering and collide with the new body T6 (§7) and T9 (§8.3).

**R5.3.**
- [ ] Move T6 to App A2 (as Table A2b) and T9 to App C7; cut T8 to ≤ 4 rows.
- [ ] Delete the 196 tU sentence (its home is §8.3).

## 5. Rubric checklist (done = meets HD as the marker will read it)

- **R1:** R1.2 done; R1.3 done (keep §6.2's synthesis sentence); R1.5 partial (App B debris, M2); R1.1 partial (Leroy); R1.4 partial (patents missing; list incomplete, M1).
- **R2:** R2.1, R2.3, R2.4, R2.5, R2.6 and R2.7 partial (D): HD-level within scope, held back by §6 (X6, X7) and by M2, M5 and M11; R2.2 partial (no Granta run; §2 TODO).
- **R3:** R3.1–R3.8 all done. R3.6 needs M11b for clarity; R3.1 carries the "as reported" risk (X13).
- **R4:** R4.3 and R4.4 done; R4.1 and R4.2 partial (M9; §10).
- **R5:** R5.1 partial (M6, X20); R5.2 partial (X10, X11, §6 captions); R5.3 partial (unmeasured; M7, M8, M10); R5.4 partial (M1, M14); R5.5 partial (title page, declaration, App E heading, App B debris, §6 markers).
- **RB:** RB.1, RB.2 and RB.8 done; RB.5 and RB.6 partial; RB.3 partial; RB.4 and RB.7 missing (Leroy).

## 6. Fact-checker findings still unresolved

- **final-part1 item 10.**
  - Incomplete entries: Ostrołęka (no URL), AEC 2019, Conference Board 2021, OPG 2026b (no URL), Slovic (no DOI). Human to complete; don't invent.
  - Ostrołęka and Pillai have not been opened. These two carry RB.1 and every C1 number.
- **final-part1 flags.**
  - Duplicate B8.3: still present (M2 items 9 and 13).
  - §6 is still on the old case (X6).
  - §3 row 5's 7.5% depends on §6 (X7).
  - T12's "around 2028" should carry "(our inference)" if space allows.
- **Human checks still open from Q13** (every input is still unverified: 0 primaries opened):
  - Senate composition (M1, aph.gov.au); the hedge holds on either count.
  - GenCost 2023-24 table (S12).
  - REGDOC-3.5.1 durations (S3).
  - NRC GLE page.
  - OEB interrogatory with C$149/MWh.
- **New: no fact-checker pass on the final-cut text** (25/10) of §7, §8.1, §8.2, §8.3 or App B1–B7, since final-part1 excluded them.
  - I recomputed their numbers against B4–B7 and `c1_deck_case.md`. All agree except the §7 lead ratio basis (M5c) and the §7.3 4.9× condition (M12).
  - Q20 part 2 should cover them together with §6 and Leroy's files after 18:00.

## 7. Top five priorities

1. **Coordinator, now (15 min).**
   - M3: appendix table labels, figure labels, §4 and §8 parent headings, App E placeholder.
   - M1: build the list from `12-references.md`.
   - M2 item 13: drop the moved file from the build.
2. **Writer B, now (about 45 min).** M2 (App B cleanup), M1 (entries and in-text fixes), M7, M8 and M14.
3. **Writer A, now (about 30 min).** M4, M5, M6, M9, M10, M11, M12 and M13.
4. **Leroy and Victor (LCA), by 18:00.** Deliver to the §4a and §4b lists. Victor (LCA) also makes the X7 decision and sends any changed downstream numbers to the coordinator in one message.
5. **Victor (human), before the final build.**
   - Fill in the three student IDs and Sam's surname (`assemble_draft.py`, TITLE) and write the AI-use declaration (DECLARATION).
   - Open: the Hooton slides (title); the GenCost 2023-24 table; the OEB interrogatory (C$149); and the Ostrołęka PIS (Table 14, p. 83) and Pillai et al. (2019).
   - Optionally, run the Granta cross-check (`granta_inputs.md`, under 1 h).
   - Then run gate 1 (≤ 9,500 body words) and gate 2 (≤ 19.5 rendered pages), apply the reserve cuts if either fails, and call Q21 part 2 (examiner) on §6 and Leroy's sections.

## 8. Rubric statement (this job)

- **All IDs.**
  - *Produced:* a grade per criterion and per RB item, with the HD phrase that is missed; 14 must-fixes, each with exact replacement text and a net-word count; 20 cross-section fixes; checklists for §6 and for Leroy; the updated tracker.
  - *Still missing:* execution of M1–M14; §6, App A and App C (re-base); Leroy's §4.1, §4.2, §5, §10 and App E; the measured page gates; the human checks in P5.
- **Most at risk:**
  - RB.4, RB.7 and R1.1 (Leroy).
  - R2.1–R2.7 (the §6 decision on X7).
  - R5.4 and R5.5 (M1, M2, M3 and the title page). These are cheap but visible on every page the marker opens.
