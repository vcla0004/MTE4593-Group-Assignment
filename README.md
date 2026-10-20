# MTE4593 Group Assignment: Small Modular Nuclear Reactors

Team: Victor, Sam, Leroy (Aaron left the unit). Drawdown solution: *Deploy Small Modular Nuclear Reactors*. Case study so far: the Darlington New Nuclear Project (GE Vernova Hitachi BWRX-300, Ontario Power Generation).

## Status as of 20 October 2026
| Part | State |
|---|---|
| Brief and rubric | Complete (`00_Brief/`) |
| Report (`01_Report/MTE4593 Report.docx`) | Outline only. Headings exist, no body text. Figure and references are scandium leftovers from another project |
| Research (`02_Research/`) | Notes and source links, roughly 15 links, mostly not yet summarised |
| LCA (`03_LCA_Calculations/`) | Assumptions started; spreadsheet has 2 rows (concrete, steel) with no emission factors |
| Presentation (`04_Presentation/`) | 5 slides, mostly copied from the brief. Slides now due Thursday 22 October (postponed) |
| Meetings (`05_Meetings/`) | 2 sets of minutes (13 Aug, 3 Sep). "Copy of Meeting Template" renamed to "Meeting 2 03_09_26" |

## Biggest gaps against the brief
1. **No specific materials-engineering initiative yet.** The brief requires location, scale, application and technology, and the marking rewards originality. "Analyse an SMR" alone won't satisfy it. Decide this first.
2. No sensitivity analysis, literature comparison, triple-bottom-line evaluation or appendix.
3. No Granta EduPack results yet.
4. **The report is due Friday 23 October 2026**, three days from 20 October.

## Fact checks on existing work
- **Darlington is in Clarington, Ontario** (east of Toronto), not Ottawa (`Assumptions.docx`, "Site Choice").
- **The tunnel boring machine volume is wrong.** 4,127.29 m³ is the concrete (4,000 m³) plus the rebar (127.39 m³), not the rock bored. Bored volume needs tunnel length × cross-section.
- The concrete and steel rows sit on the "Nuclear Fuel LCA" sheet and should move to "SMR Parts LCA". They also cover only the forebay shaft (from one construction update), not the whole plant, so label them as partial.
- "Zero risk of meltdown" in the notes overclaims. Use "passive safety reduces…" with a source.
- Mass conversions are correct: 4,000 m³ × 2,400 kg/m³ = 9.6 million kg, and 1,000 t ÷ 7,850 kg/m³ = 127.4 m³.

## How to use this folder with Claude
Open a Claude Code session on this folder (or its GitHub repo) and say, for example:
- "Examiner: make the plan" (creates `01_Report/plan.md`)
- "Policy analyst: research the Australian regulation section"
- "Policy analyst: calculate the HHI for uranium mining and enrichment"
- "Run the loop on section 3.3" (write, fact-check, mark, revise)

The workflow and rules are in `CLAUDE.md`. The agents are in `.claude/agents/`.
