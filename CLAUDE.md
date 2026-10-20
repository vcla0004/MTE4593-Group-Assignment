# MTE4593 Group Assignment: Small Modular Nuclear Reactors

Monash MTE4593 Materials and Sustainability, S2 2026, Assignment 2 (team, 30%).
Report is worth 25% (15-20 pages of text; figures, graphs and appendices not counted). Presentation is worth 5%.
**Slide deck due Thursday 22 October 2026** (postponed; the presentation is in the week 11 workshop). **Report due Friday 23 October 2026.** The official marking rubric is `00_Brief/rubric.md`; follow it exactly. Prioritise what the rubric rewards most, within the time left.
Read `README.md` for current status.

## The rubric is the contract (read before anything else)
`00_Brief/rubric.md` (the official Assignment 2 Report Marking Rubric 2026) is the single standard for all work. Nothing else (style preferences, agent judgement, "good practice") can override it.
1. **Start from the rubric.** Before any task, read `00_Brief/rubric.md` and `01_Report/rubric-tracker.md`, and name the rubric IDs (R1.1 … R5.5, RB.1 … RB.8) the task serves. If a task serves no rubric ID, don't do it.
2. **Tag every output.** Every plan item, research brief, result file and section draft starts with a `Rubric coverage:` line listing the IDs it serves.
3. **Done means HD with evidence.** A section is done only when the examiner has marked every ID it serves as HD in `rubric-tracker.md`, citing section and page, and the fact-checker has confirmed that evidence.
4. **Weight effort by marks.** Technical (R2, 8%) and non-technical (R3, 6%) come first, then research coverage (R1, 5%), originality (R4, 3%) and presentation (R5, 3%).
5. **Use the rubric's words.** Reviews quote the HD descriptor phrase being missed, not a general opinion.

## Team and task split
Split taken from the "Potential tasks" section of `02_Research/SMR Research Notes.docx`, by highlight colour.

| Colour | Owner | Owns |
|---|---|---|
| Yellow | Victor | Stakeholder analysis, money flows, market analysis (barriers to entry, US startup market caps, China top-down funding, possible government programs, state of industry), government regulation review, perceived vs actual safety |
| Red | Sam | Granta EduPack LCA: SMR bill of materials, eCO2 per life-cycle stage, nuclear fuel LCA vs conventional nuclear, coal comparison |
| Green | Leroy | Planned projects and timelines, Google Patents review of US SMR designs, timescales to maturity and rollout |
| Yellow (added) | Victor | Herfindahl-Hirschman index for uranium and enrichment supply (unassigned in the notes; fits with the supply-chain work) |

Aaron left the unit and is no longer in the group. Remove his name from the presentation title slide.

## Agent workflow
Sam (LCA) and Leroy (projects, patents, timescales) do their own work. The agents support Victor's sections, the shared sections, and quality control for the whole report.

Agents can't call each other. The main Claude session is the coordinator: it calls each agent in turn, and the agents pass work to each other through files in this repo.

| Agent | Reads | Writes |
|---|---|---|
| `examiner` | Brief, rubric, everything in the report | `01_Report/plan.md`, `01_Report/review.md`, `01_Report/rubric-tracker.md` (sole owner) |
| `policy-economics-analyst` | `plan.md`, Sam's results | `02_Research/sources.md`, `02_Research/briefs/`, `03_LCA_Calculations/` (parameters, scripts, results) |
| `writer` | `plan.md`, briefs, results, `review.md`, `factcheck.md` | `01_Report/sections/` |
| `fact-checker` | Sections, sources, scripts | `01_Report/factcheck.md` |

Standard loop (say "run the loop on section X"):
1. `examiner` writes or updates the plan.
2. `policy-economics-analyst` produces the evidence for the open items.
3. `writer` drafts or revises the section.
4. `fact-checker` verifies it.
5. `examiner` marks it. If it isn't at HD on every criterion, go back to step 2 or 3 with the review.

All agents run on Opus at high effort (set in each agent file). Run the examiner at **max** effort for the first plan and the final pre-submission review.

Teammates' sections in `01_Report/sections/` are fact-checked and reviewed too, but feedback goes to the owner in `review.md` and the agents never rewrite their work.
Scope work to the person asking. When Victor asks, prioritise the yellow sections, but flag anything that blocks the whole report.

## Rules every agent follows
- Never invent sources, quotes, numbers, Granta EduPack outputs, or meeting decisions. Every figure needs a citation or a calculation in `03_LCA_Calculations/`. If something is unknown, write `[TODO: ...]`.
- Granta EduPack runs only on the team's machines. Agents prepare inputs and checks but never fabricate its results.
- Keep teammates' work intact. Suggest changes to their sections in `review.md`; don't silently rewrite them.
- Personal opinions in the research notes (e.g. voting intentions) are brainstorming only and stay out of the report.
- Australian English spelling. Style rules: `01_Report/style-guide.md`.
- Follow Monash's AI-use rules for this unit; the team decides how AI use is declared.

## Folders
- `00_Brief/`: brief PDF, text copy, **official report rubric** (PDF, text, and the HD checklist in `rubric.md`)
- `01_Report/`: report draft (.docx), plan, reviews, style guide, section drafts in `sections/`
- `02_Research/`: notes, `sources.md` (annotated bibliography), research briefs per topic
- `03_LCA_Calculations/`: team spreadsheet and assumptions, `parameters.yaml` (every number, with its source key), `scripts/` (Python, reproducible), `results/`
- `04_Presentation/`: slides
- `05_Meetings/`: minutes and template
- `06_Reference_Examples/`: example or past HD reports, when found
