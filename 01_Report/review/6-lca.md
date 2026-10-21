Rubric coverage: see entries

## Review of §6 and Appendices A, C (21/10)

Rubric coverage: R2.1, R2.2, R2.3, R2.4, R2.5, R2.6, R2.7, RB.5, RB.6, R1.3, R1.4 (also R4.1–R4.4, RB.1, RB.8, R5.2–R5.5)

Files reviewed:
- `01_Report/sections/6-lca-eco-audit.md` (v2)
- `appendix-A-lca-inventory.md` (v2)
- `appendix-C-sensitivity.md` (v2)
- `factcheck.md` §H (run on **v1**; each finding re-checked against v2 below)
- `03_LCA_Calculations/results/lca.md`, `parameters_lca.yaml`, and figures F3 and F5 (viewed)

**Owner: Victor.** He took over Sam's red sections on 21/10 (CLAUDE.md), so this feedback is addressed to him. Sam's `Assumptions.docx` and `Accounting.xlsx` stay as he left them. "For Sam" items 1–4 above are now carried out in `Accounting_corrected.csv` and Appendix A4, so they are **closed for the report** and remain open only in Sam's own files.

### Verification caveat (CLAUDE.md rule 3)
None of the LCA primaries has been opened (factcheck §H: 0 verified, 29 unreachable, 7 with no source found). No Granta run exists. **Nothing that §6 serves can go above Partial.** Each criterion therefore gets two grades:
- **If verified:** every input checks out as drafted.
- **As it stands:** what a marker would give today.

The engineering itself is sound. The scripts re-run byte-identical, and every hand check passes (L35–L54).

### Grades per official criterion (scope: what §6 and Appendices A and C contribute)

| Criterion | If verified | As it stands | HD phrase being missed | Evidence |
|---|---|---|---|---|
| **R2 Technical (8%)** | **D (high), about 78%**. HD (about 83–85%) with fixes 3–5 below | **C (high)** | "Calculations of… **potential environmental or economic benefits**"; "Arguments are logical, **well justified and consider all important aspects**"; "**where feasible, an eco-audit**" | **Strengths:** this is the strongest work in the report. The FU, reference flow, boundary, cut-offs and impact basis are stated (§6.1, T6). It has a bottom-up fuel mass balance (A8), a 40-input tornado, a 20,000-draw Monte Carlo with seed and distributions, the median-vs-mode skew explained (C5), and T9 giving the sign and size of each discrepancy. **Gaps:** (a) **no economic benefit**: the abatement cost is a TODO, so R2.3's "economic" half is empty; (b) **the steel comparison is not like-for-like** (finding 4; see fix 3); (c) **the counterfactual baseline is never justified**: S0 is pure GU cement, but if OPG's mixes already contain slag, S1 is business as usual and LC3's real increment is about 100–180 t; (d) **Granta is feasible for this team, and the brief says "in particular, use Granta EduPack"**, yet A9 is empty |
| **R1 Research (5%)** | **D** | **C** | "**synthesis** of a wide range of **highly relevant** sources" | Good synthesis: vendor claim vs scale penalty, Parker vs Gibon on ore grade, EDF vs our construction share, Carless on SMR vs large reactor (§6.2, §6.5, T9). Defects: the geometry that sets 69% of the C1 concrete is cited to "Ontario Power Generation (2026)" but was read in a news report (okdiario). Under Harvard you cite what you read, so this is a misattribution until the OPG story or NEDO-33926 is found. ENR (trade press) is one of the five LC3 estimates. Three references have no author (arXiv 2025, LACCEI 2026, the 2026 nuclear-concrete paper). IPCC AR5, the plan's named benchmark (plan §4.1), is absent |
| **R4 Originality (3%)**, §6's share | **D** | **C** | "identifies **less intuitive or indirect** opportunities"; "**new feasible ideas or connections**" | §6.3 finding 5 (1.4–15 days of delay cancel the saving) is the report's best non-obvious connection, and the honest 0.3% finding serves R4.4. But the case for LC3 *over slag* (shrinking Ontario slag supply) is still unsourced (L18). Without it, "LC3" adds nothing over slag on carbon |
| **R5 Presentation (3%)**, §6's share | **D** | **C** | "**high-quality** figures/tables"; "clear… for a general audience" (brief) | Each subsection leads with its result, and table captions sit above the tables. Defects: **F3 labels are Python variable names** (`conversion_heat_kwh_per_kgU`, `lc3_gwp_reduction`, …), which is not professional. F3 and F5 carry their own "Figure F3./F5." titles, which will duplicate the Word captions. **F5 still plots a UNECE point at 5.8 and attributes "3.7–110" to Warner and Heath** (L66, L31 open). The lead sentence switches units ("4.2 kg CO₂e per MWh… UNECE's 5.1–6.4 g/kWh"). The headline is 0.3% but T8 shows 0.45%: correct and footnoted, but a skim-reader sees a contradiction. Mode, mean and median vocabulary is dense for a general reader. §6 is about 3.6 pages against a 3.5-page budget (acceptable) |

**How much a real Granta Eco Audit cross-check would add under R2.2.** The descriptor wording ("eco-audit **or equivalent analysis**") is already met by the model. However:
- The brief singles out Granta, and this unit teaches it, so a marker can treat its absence as a missed instruction.
- **Direct gain:** filling Table A10 (four rows, a screenshot, and the ±30% reading rule already written) lifts R2 by about half a band, about **+0.3–0.5 / 25**.
- **Downside it removes:** a marker who docks a band for "didn't use the unit's tool" would cost about 0.6–0.8 / 25.
- **Cost:** under one hour (`granta_inputs.md`). Per hour, it is the cheapest mark left in the report.
- If it can't be run by Thu 12:00, cut A9 and every Granta sentence, rather than leave TODO cells.

**Estimated contribution to the 25 marks** (the share §6 and Appendices A and C can carry: about 55% of R2, 15% of R1, 20% of R4 and 18% of R5, about 6.3 marks in all):
- **As it stands:** about **4.0 / 25**
- **If verified, as drafted:** about **4.8 / 25**
- **Verified, with fixes 3–5:** about **5.1 / 25**
- **Plus the Granta cross-check:** about **5.4–5.5 / 25**, close to the ceiling for this scope

### Fact-checker §H findings: status in v2

**Resolved in v2:** L14 (wording), L18 (reduced to a risk), L23, L25 (wording), L26, L48, L55, L56, L57, L58 (wording), L59, L60, L61, L62 (wording), L63, L65.

**Still unresolved: §6 and Appendices A and C**

| # | Issue | Owner | Fix |
|---|---|---|---|
| L2–L8, L11, L12, L15, L16, L19–L21, L24, L27, L29, L30, L33 | Primaries unopened | Victor (human) | Open them in this priority order: Gibon 2023 (the 26–665 conversion range drives +0.97 of the +1.58 mean–mode gap), Parker 2016, EDF 2024 shares, CAC EPD region, Peterson 2005, the LC3 five. Set `status: verified` and re-run |
| L9 | 37 m / 35 m / 953 t geometry rests on a news report, cited as OPG | Victor | OPG story URL or NEDO-33926 dimensions by Thu 12:00. Otherwise cite the news report as read and keep the caveat |
| L1, L13 | ISO 14040/44 and NWMO not in `sources.md`; EN 15804 also missing (A5) | Analyst | Add the three entries |
| L10, L17 | Authorless citations (arXiv 2025, 2026 concrete paper; also LACCEI) | Analyst | Add the authors, or replace with NEDO-33977/GEH documents |
| L20 | ENR (trade press) in the LC3 median | Analyst | Replace with a peer-reviewed LCA, or drop it and re-take the median of four |
| L22 | CRSI 2017 superseded | Analyst | Use the 2022 EPD value |
| L28 | Two titles for UNECE (2021) | Victor | Pick one, and use it in §6.5, F5 and slide 7 |
| L31, L66 | F5: UNECE point at 5.8; "Warner & Heath range 3.7–110" footnote | lca-analyst | Redraw UNECE as a range only. Drop 3.7 or attribute it to IPCC AR5 once verified |
| L32 | Ng et al. scope (front end or whole fuel cycle) | Victor | Confirm before comparing it with our front end |
| L64 | `lca.md` §7 still says every construction-quantity input moves the total by < 0.07. It also still says "hybrid" (§1, §10.6, §11), "construction 7%" (§0), and that Unit 1's forebay is "already placed" (§0) | lca-analyst | Correct `lca.md` so nothing is re-copied from it |
| L67–L79 | Slides 5–9 | Victor | See "Slides" under the thesis section below. L70 (Granta claim) and L71 (ISO conformance) must change before Thursday 15:00 |
| New (E1) | T8 note: Monte Carlo shares for S1/S2b/S3 are missing | lca-analyst | Add them, so the headline 0.3% and the table use one basis |

### Feedback for Victor, paragraph by paragraph

1. **Lead.**
   - Use one unit (g CO₂e/kWh) throughout; say once in §6.1 that it equals kg/MWh.
   - Add the clause that carries the thesis: "a delay of about 1.4–15 days to one unit would cancel its saving". At the moment the lead ends on caveats, not on the finding. [R5.1, R4.3]
2. **§6.1 Goal and scope.** Sound. Three additions:
   - **Define the baseline counterfactual**: "S0 = what OPG would otherwise specify". Then state whether NEDO-33926 or OPG's mix already permits supplementary cementitious materials [TO VERIFY]. If it does, S0 must include them, or the savings are overstated. This is the one structural gap in the goal and scope. [R2.5, R2.6]
   - Grid transmission isn't a cut-off; the FU is set at the grid connection, so it is outside the boundary. Move it.
   - Cite ISO 14040/44 and EN 15804 (L1, L62).
3. **§6.2 Quantities.**
   - The honesty about scaling is right.
   - The one sentence a marker will probe: 13,100 m³ of the 20,700 m³ (63%) sits in the target structures. Say in one clause why that is plausible for a BWRX-300 (below-grade reactor building plus forebay vs a small turbine island), or flag it as a limitation. Leroy's EIS or Clinch River quantities would settle it.
4. **§6.3, finding 4 (steel): the logic fault to fix first.**
   - S3 low moves **all 9,900 t** of plant steel, including turbine and RPV forgings, to the **BCCA hot-rolled *sections* limit (1.22 t/t)** (`parameters_lca.yaml`, `ef_plate_other` note). It then compares the result with LC3 in **13,100 m³ of three structures**. That is not like-for-like, and a sections factor is not a feasible factor for forgings or nuclear plate.
   - **Examiner's check (not for the report until the analyst scripts it):** in the C1 target structures alone, the same factors give about 953 t × (1.73 − 1.22) + 1,000 t × (0.97 − 0.89) ≈ **0.57 kt**, against LC3's 1.73 kt.
   - **Fix:** add a like-for-like S3 row in `lca_scenarios.py` (low-carbon steel in the target structures only). Relabel the whole-plant row "upper bound: all steel at best-practice EAF sections factors". Reword: "Across the whole plant, steel is the larger construction lever (up to about 2× LC3); within the structures C1 targets, LC3 is the larger lever." [R2.6, R2.3]
5. **§6.3, finding 2: the economic half of R2.3.**
   - Add one sourced line now: the saving's carbon value at a stated price (e.g. the federal OBPS benchmark for 2026 [TO VERIFY]) per unit and for Units 2–4. Set it against Darlington's CAD 20.9 bn and against the cost of one month's delay (`schedule_value.md`).
   - That turns "its cost has not been estimated" into a quantified economic finding, without needing the LC3 price premium.
   - The full $/t abatement cost can follow in §8.2. [R2.3, R3.1]
6. **§6.3, finding 3 (slag).**
   - Correct and honest. Add: if OPG's baseline already uses slag (point 2), "slag vs LC3" becomes "LC3 vs business as usual", with an increment within noise.
   - So the *carbon* case is for low-clinker infill; the case for *LC3 specifically* rests only on slag supply (unsourced, L18). **Victor:** source the Ontario blast-furnace closures by Thu 12:00, or say plainly "whichever binder qualifies first". [R2.6, R4.2]
7. **§6.4.** Good. One HD tightener for "realistically estimated":
   - The 4.2 headline depends on choosing a triangular 26/26/665 distribution for conversion heat (+0.97 g/kWh).
   - Report the Monte Carlo median with conversion heat held at a sourced central value, or under a log-uniform alternative: one sentence and one script flag.
   - That shows the headline isn't an artefact of one distribution choice. [R2.7]
8. **§6.5.**
   - Add IPCC AR5 WGIII Annex III (min/median/max) once verified. It is the benchmark a marker expects (plan §4.1).
   - T9 is excellent. Keep it.
9. **Figures.**
   - F3: replace the variable names with plain labels ("Conversion heat (kWh/kg U)").
   - F3: mark the left axis centre as "mode case 2.70", so it doesn't contradict the 4.2 headline.
   - F3 and F5: remove the embedded "Figure F3./F5." titles; Word captions carry them.
   - F5: apply L66 and L31.
   - [R5.2]

**Appendix A.** Exemplary for RB.5/R2.4. Every formula has a worked example, and the reproduce commands are verified (L53). Remaining fixes:
- A3: cite the geometry as read (L9).
- A5: drop or replace ENR.
- A9/A10: run Granta, or cut both.
- A4 row 4 (tunnel boring) can stay a TODO only if A7's uplift sentence says so explicitly (it does).

**Appendix C.** HD-capable for R2.7 once the inputs are verified. Add the conversion-heat alternative run (point 7) as a row in Table C2.

### Thesis question: keep C1, reframe as a materials package, or switch?

**Recommendation: keep C1, with a minimal sharpening, not a broadening.** Rename it "**low-clinker self-consolidating infill for the DPSC modules and forebay shafts of Units 2–4: LC3 as the target binder, a qualified slag blend as the fallback, specified only if schedule-neutral**". Make the honest findings the thesis. **Do not** fold low-carbon steel into the initiative, and **do not** switch. **Victor decides**, and the decision goes in the Meeting 3 minutes (item 6 above).

| Option | R4.1 beyond obvious | R4.2 indirect opportunity | R4.3 new connections | R4.4 feasibility | R2.3 sized to proposal | Verdict |
|---|---|---|---|---|---|---|
| **Keep C1 (sharpened)** | Medium-high: the DPSC SCC infill problem and the schedule test are not "greener concrete" | Developed: 1,291 of 1,734 t comes from the cement-rich SCC infill; qualification route | **Strong**: 1.4–15 days of delay cancel the saving; the federal procurement lever | **Exactly what the brief invites**: "small, real, conditional", shown with numbers | Strong: 13,100 m³, Units 2–4, clinker avoided | **Recommended** |
| Reframe as a package (LC3/slag + low-carbon steel) | **Weaker**: "greener concrete + greener steel" reads as the rubric's named non-example ("use better steel") | Dilutes the DPSC infill story | No new connection | Steel feasibility for nuclear plate and forgings unshown (residuals, qualification) | **Weaker**: whole-plant steel is scaled, not measured, and the 2× is an upper bound on a sections factor (point 4) | Reject. Keep steel as the quantified "next lever" in §10 |
| Switch (to C2 steel, or C3 tails re-enrichment) | C2 fails R4.1 outright; C3 is high | C3 high | C3 high (and §8.3 already uses it) | C3 unquantifiable by Friday (proprietary laser energy) | Breaks every number in §6, §8.1, §8.3 and the deck, due tomorrow | Reject |

Why this is the right call: the brief says a proposal need not be net beneficial, and that clearly showing why it is limited is "valid and useful". The LCA has turned C1 into exactly that kind of finding. In order of size, the materials levers that matter for an SMR's climate value are: (1) not delaying the plant, (2) the fuel front end (ore grade, conversion energy, the enrichment grid; 64% of the total), (3) steel across the whole plant, (4) concrete. That ranking is a non-obvious, quantified conclusion. A package initiative would bury it.

**What changes**
- **§4.3:**
  - Use the sharpened statement above, in the brief's "better example" form, with the numbers: about 1,700 t per unit, about 5,200 t for Units 2–4, about 6,900 t clinker, about 0.3%.
  - Lead with the DPSC infill problem and the schedule-neutral condition (plan §10 risk row), not with emissions per m³.
  - State what C1 does **not** address: cost, Australian law, the fuel front end.
  - Say that slag is the fallback because the carbon results cannot separate the two binders.
  - Drop any claim that LC3 beats slag on carbon.
- **§6:** fixes 2–7 above. Findings 3 and 4 reworded as described. No structural change.
- **§9 (TBL/MCDA):**
  - "SMR" and "SMR + C1" differ by about 0.3% on the environmental criterion, so show that C1 does not change any ranking.
  - Add a schedule/deliverability criterion, and score C1's feasibility on qualification risk.
  - Verdict: "adopt C1 only as a schedule-neutral specification qualified on Unit 1 mock-ups; otherwise specify the slag blend".
  - R4.4 is earned here.
- **§10:** low-carbon steel (EAF/DRI-EAF plate with residual-element control) as the next lever, with both S3 rows (like-for-like and whole-plant upper bound). Conversion-energy data and ore grade as the fuel-cycle levers.
- **Slides (due Thu 15:00; wording only):**
  - Slide 5: the sharpened initiative title; "about 21,000 m³ per unit (90% interval 15,000–36,500); 13,100 m³ targeted" (L67, L68).
  - Slide 6: remove or condition the Granta claim (L70); "structured on ISO 14040/44, screening study" (L71); forebay and module data as inputs, not a check (L72).
  - Slide 7: "just below UNECE's range" (L56); Appendices A and C (L74); "slag nearly matches; whole-plant low-carbon steel up to about 2×".
  - Slide 12: SCC LC3 infill qualification, and low-residual EAF plate.
  - Slide 13: the ranked-levers conclusion.

### Top five priorities (§6 and Appendices A, C)

| # | What | Owner | By | IDs |
|---|---|---|---|---|
| 1 | Open the P1 LCA primaries (Gibon 2023, Parker 2016, EDF 2024, OPG basemat or NEDO-33926, CAC EPD, Peterson 2005, UNECE 2021, IPCC AR5 Annex III). Set `verified`, re-run the three scripts, tell the fact-checker | Victor | Thu 12:00 | R1.4, R2.1, R2.7, RB.6 |
| 2 | Run the Granta Eco Audit cross-check (`granta_inputs.md`, under 1 h) and fill A10 with a screenshot; otherwise cut A9 and every Granta mention (report and slide 6) | Victor (or Leroy, if his machine has EduPack) | Thu 12:00 | R2.2 |
| 3 | Fix the comparison logic: define the S0 counterfactual (§6.1); add the like-for-like steel row and relabel the whole-plant S3 row as an upper bound; reword findings 3 and 4 | Victor (lca-analyst scripts; writer text) | Thu 12:00 | R2.6, R2.3, R2.5 |
| 4 | Add the economic benefit (carbon value at a sourced price vs the cost of delay) and the conversion-heat alternative Monte Carlo run | Victor (analyst) | Thu 18:00 | R2.3, R2.7, R3.1 |
| 5 | Figures and references: F3 plain labels and the mode-case marker; F5 redraw (L66, L31); cite the geometry as read; add ISO, EN 15804 and NWMO; complete the authorless references; replace ENR and CRSI 2017 | lca-analyst, analyst; Leroy (format) | Thu 18:00 | R5.2, R5.4, R1.4 |

The thesis decision (keep C1, sharpened) should be taken **before** the slides are finalised on Thursday morning, so that §4.3, §9 and slides 5, 7 and 13 are written once.

### What this review produced, and what is still missing (per ID)
- **R2.1, R2.4, R2.7, RB.5.** Produced: conditional grade (D high to HD-capable) and current grade (C high); the conversion-distribution test. Missing: verified inputs; Appendix B (schedule-value working); §2 methods.
- **R2.2.** Produced: the value of the Granta cross-check (+0.3–0.5 / 25; removes a downside of 0.6–0.8). Missing: the run.
- **R2.3, R2.5, R2.6.** Produced: the baseline-counterfactual gap, the like-for-like steel fault (with the examiner's check), and the economic-benefit fix. Missing: those changes; Leroy's plant data.
- **RB.6, R1.3, R1.4.** Produced: the IPCC AR5 gap, the misattributed geometry citation, and the trade-press and authorless references. Missing: verification.
- **R4.1–R4.4, RB.1, RB.8.** Produced: the thesis recommendation, weighed against each R4 check and R2.3, with the changes to §4.3, §6, §9, §10 and the slides. Missing: Victor's decision and minutes; the §4.3 and §9 drafts.
- **R5.2–R5.5.** Produced: figure, unit, caption and page-length defects. Missing: the fixes.
