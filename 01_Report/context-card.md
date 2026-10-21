# Context card (read this first, instead of the big logs)

Rubric coverage: all (shared context; every agent reads this)
Updated: 21/10/2026. The coordinator keeps it current. If a number here disagrees with a results file, the results file wins: flag the mismatch.

## Deadlines
- Slide deck on Moodle: **Thu 22/10**. Content freeze: **Thu 21:00**. Report: **Fri 23/10**, by 15:00 (exact time to be confirmed with the tutor).
- Work queue and owners: `01_Report/plan.md` §7 (revised 21/10). Read **only your own Q row** (`grep -n "| Q<n> |" 01_Report/plan.md`).

## Decisions in force
- **Initiative (C1):** low-clinker SCC infill for the DPSC modules and forebay shaft of **Darlington Units 2–4**, Clarington, Ontario. LC3 is the target binder, a slag blend the fallback, and it is specified **only if schedule-neutral**. Steel is not part of the initiative.
- **Australian comparison site:** Liddell, NSW (a closed coal plant).
- **Team:** Victor; Leroy (**G1 resolved 21/10: Victor says Leroy has sent work, so Q5 and Q9 are skipped**; his files are not in the repo yet: once Victor adds them to `01_Report/sections/` they go to Q11 batch 2 and Q13); Sam (absent, so Victor owns Sam's sections from 21/10); Aaron (left the unit).
- **Defaults until Victor says otherwise:** Red Book 2024 edition; GenCost reading = 2030 SMR at A$230–382/MWh (same money ≈ 2.9×; the alternative is 5×); carbon price = federal path C$95/t (2026), C$115/t (2030).
- **Granta EduPack:** not yet run. Never claim results. The method is a "screening LCA following ISO 14040/44 principles (not critically reviewed)".

## Key numbers (all provisional [TO VERIFY] until a primary source is opened)
| Quantity | Value | Source file |
|---|---|---|
| Net output, capacity factor | 300 MWe (OEB filing may say 315 net), CF 0.90 → 2.365 TWh/yr | parameters_run1.yaml |
| Life-cycle intensity | **4.2 g CO₂e/kWh** median, 90% 3.0–5.8; mode 2.7. Not robust to conversion heat: report the "range of medians 3.3–4.2". UNECE 5.1–6.4 | results/lca.md, lca_uncertainty.md |
| Biggest hotspot | Uranium mining and milling, 29%; conversion 26% (wide range) | results/lca.md |
| Concrete per unit | 20,700 m³ (MC 90% 15,050–36,521); C1 target ≈ 13,100 m³ | results/lca.md |
| C1 saving | ≈ 1,734 t CO₂e/unit (1,390–2,150); 5.2 kt for Units 2–4; ≈ 0.3% of life cycle; 6,900 t clinker | results/lca.md |
| Slag vs LC3; steel | Shares of the life cycle: S1 slag 0.28%, S2 LC3 0.29%, S2b 0.46%. Low-C steel in the same structures saves 566 t/unit (a floor; MC median 941); whole-plant steel upper bound 3,714 t | results/lca_scenarios.md |
| Displacement, one unit | NSW 1.50 Mt/yr; Ontario 0.073–0.165 Mt/yr (average), 0.8–1.1 (marginal) | results/displacement.md |
| Liddell to 2050 | 0.67–3.85 Mt (first power ≈ 2040) | results/displacement.md |
| Schedule break-even | 9–15 days of delay per unit cancels C1 (average factor); 1.3–1.4 days (marginal) | results/schedule_value.md |
| LCOE (own) | C$112/151/198/280 per MWh at 3/5/7/10% real (4.9% reproduces OPG's C$149) | results/lcoe.md |
| C1 carbon value | C$0.49–0.88m; one day of delay costs C$1.8–2.9m | results/initiative_cost.md |
| Darlington | C$20.9bn for 4 units (Unit 1 approved May 2025); Unit 1 in service Oct 2030; licence took 29 months | sources.md |
| HHI | Enrichment 3,009 (3,599 without Russia; 5,621 without Russia and China); mining 2,341; conversion 2,111; threshold 1,800 (DOJ/FTC 2023) | results/hhi.md |
| Supply | Russia 41.0–42.8% of enrichment (HHI 2,935–3,009 across sources); four units need 196 tU and 138 tSWU a year (3.2% of Urenco USA); Silex/GLE: GO (Cameco takes all Paducah output), cut if no primary by Thu 12:00; Australia 28% of resources, 7.6% of 2024 output, no conversion or enrichment | results/hhi.md |
| Law | EPBC s140A, ARPANS s10, NSW 1986 Act s8; Senate needs 39, the pro-repeal bloc is ≤ 32 | briefs/law-and-regulation.md |
| Social | Lowy 2024: 61% support / 37% oppose; OWID deaths/TWh 0.03 nuclear vs 24.62 coal; Williams Treaties FNs' C$700m loan to equity (23/06/2026) | briefs/social-licence-stakeholders.md |

## Coordinator handoff (for a fresh session)
- Done: Wave 1 (Q1, Q2, Q3, Q7), runs 5 and 6, §6 v3, Q4 (§7 + App B4–B6), Q6 (§8.2, §8.4, §8.5; all over budget). Nothing running. Draft preview: `01_Report/draft-preview.docx` (rebuild with pandoc). Victor's speech: `04_Presentation/victor-speech.md`.
- Known loose ends for Q8: align §6's break-even to 9.2–14.6 days; re-run `same_money.py` on GenCost 2030 (B26–B27 still on A$514); script the 45× hand calculation; draw F6/F7; re-run C$15/m³ in `initiative_cost.py`.
- Done 21/10 evening: Q8 prep (f3d4ab8: same_money on GenCost 2030, 45× → 44× (44–223×), C$15.2/m³ break-even, 9.2–14.6 days); Q10 (§3 with T15, §4.3 with T1, §8.6 with T16–T17; §8.6 ≈0.55 p, over budget: cut T17 first). Q10 open: §8.2 treats the OPG contract clause as fallback, §8.6 uses it first (resolve in Q14); St Marys LC3, Ontario slag, qualification cost and 2028-approval primary unsourced.
- Running: Q8 writer (§6 v4, Apps A/C, plus number drop-in to §7, App B5/B6, §8.2).
- Next: Q8 writer (after Q8 prep); then Wave 3 (Q11–Q21) in `plan.md` §7. G1 done (Leroy delivered; Q5/Q9 skipped).
- Deck: live at https://claude.ai/artifact/58LWT4feZJTcLrq3pi7KQH. Source in `04_Presentation/deck-source/`. Sync any slide edit to both.
- Commit and push after every job (a stop hook enforces it).

## Where things are
- **Sections:** `01_Report/sections/`. **Results:** `03_LCA_Calculations/results/`. **Briefs:** `02_Research/briefs/`.
- **Fact-check log**, split by topic: `01_Report/factcheck/` (index in `01_Report/factcheck.md`). **Reviews**, split by topic: `01_Report/review/` (index in `01_Report/review.md`).
- **Bibliography:** `02_Research/sources.md` (large). **Never read it whole.** Grep for the key or author you need. New entries from a run go in that run's `sources_runN.md`.
- **Deck source:** `04_Presentation/deck-source/project/slides/`.

## Network (don't waste calls)
The environment blocks these hosts, and WebFetch and curl fail on them. **Don't try them.** Use WebSearch leads, tagged [TO VERIFY]:
unece.org, ipcc.ch, nrel.gov, csiro.au, aemo.com.au, dcceew.gov.au, legislation.gov.au, aph.gov.au, world-nuclear.org, oecd-nea.org, iaea.org, ourworldindata.org, ontario.ca, opg.com, ieso.ca, cer-rec.gc.ca, taf.ca, canada.ca, cnsc-ccsn.gc.ca, nrc.gov, sec.gov, doi.org, ncbi.nlm.nih.gov, archive.org, circularecology.com, rba.gov.au, lowyinstitute.org.
If Victor allows any host, this list is updated: try only hosts not on it.

## Output rules (keep it short)
- Report back in the word limit you're given. No restating the task.
- Changelogs: at most 5 lines per revision.
- Fact-checks and reviews cover **only what changed** since the last check of that file (diff against the previous version noted in its changelog), plus anything flagged as still open.
