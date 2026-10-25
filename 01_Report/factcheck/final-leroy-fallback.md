Rubric coverage: R1.4, R5.4, RB.3, RB.4, RB.7 (also R1.3, R4.2 where noted)

# Fact-check: Leroy fallback sections (§4.1, §4.2, §5, §10, Appendix E), 25/10/2026

Checked against `briefs/technology-projects-trl.md`, `briefs/materials-eol-future.md`, `sources_run8.md`, `sources_lca.md`, `12-references.md`, §6, §7, §8.1. Sections not edited. All brief sources are unopened search leads, so "verified" below means "matches the brief and its lead", not "primary source opened".

## Summary
- Numbers and claims in §4.1, §4.2, §5 and §10 match the briefs. Arithmetic is right: 9.24 bn / 462 MW = US$20,000/kW; 20.9 bn / 1,200 MW = C$17,400/kW; 50,000 / 300 = 167 m³/MWe; 50,000 m³ x 2.4 = 120,000 t; 2-5% = 2,400-6,000 t; 2029 + 3 + 8 = 2040.
- Consistency holds: Ostrołęka 50,000 m³ / 14,000 t (§4.3, §6); Unit 1 in service October 2030 (§7); Coalition 2035 vs CSIRO 2040 (§7, §8.1); 300/315 MWe and CF 0.90 (§2, §6).
- Citations: every author-year citation in the five files has an entry in `12-references.md`. The Ostrołęka entry has no URL (known, it is the PIS). Patent numbers in App E all appear in `sources_run8.md` (Pat_* entries) or the briefs. Exceptions are the details in must-fix 3 and 4 below.
- Web checks: TVA Clinch River permit issued 29 September 2026 after a 14-month review, no construction date, cost-sharing still under negotiation: CONFIRMED (WNN, GE Vernova, NeutronBytes, T&D World results). Linglong One: no report of criticality or grid connection found as of 20 May 2026 (IAEA data per OKDiario, a news secondary), target H1 2026 reported by Reuters (Dec 2025): consistent with the brief. BWRX-300 300 MWe vs 315 net: not re-checked, left as the brief states.
- Counts (about 45 checks): matches the brief 36; hedge overstated or unsupported detail 7 (must-fix 1-6); markers remaining 1 file (App E); not checkable 2 (NEDO-33926 code list; NuScale US$9.24 bn exhibit figure).

## Must-fix (exact replacement text)

### M1. Hedging: the opening of §4.1 and the T2 status column read as verified fact (§4.1)
Problem: all status entries (permit dates, "commercial operation December 2023", "cancelled November 2023") come from unopened leads. Linglong One, the other candidate "first land SMR", is missing, so the headline can be challenged.
Replace the first sentence of §4.1 with:
"**No light-water SMR is yet reported operating on land; the BWRX-300 is the Western design closest to doing so, and China's ACP100 (Linglong One) was still in commissioning, with no criticality reported, in May 2026.**"
Add directly under the T2 caption, before the table:
"*Status entries are as reported by regulators, vendors, utilities and trade press found by web search; we have not opened the primary documents.*"

### M2. Hedging: preprint presented as fact (§4.2)
Replace "Fuel is uranium dioxide enriched to 3.8% on average, 4.95% at most (Sun and Kurosaki, 2025)." with:
"Fuel is uranium dioxide, reported at 3.8% average and 4.95% maximum enrichment in a preprint review (Sun and Kurosaki, 2025)."
Also replace "It sits in a below-grade shaft" with "The reactor building sits in a below-grade shaft" (the pronoun currently points at the isolation condensers).

### M3. Patent attribution and freedom-to-operate overclaim (§4.1 and App E "What the patents show")
Problem: the shaft patent's assignee is "[TO VERIFY]" in `sources_run8.md` and App E; twelve web searches cannot show that freedom to operate is "low".
§4.1 replace "Appendix E found GE-Hitachi's isolation-condenser and shaft-construction systems in its own patent families, but no patent on the diaphragm-plate composite modules (from search summaries). LC³ appears in no core composition patent, while Sika and Construction Research & Technology patent admixtures that improve its workability, so C1's binder risk lies in qualification rather than freedom to operate (our inference)." with:
"Appendix E, from search summaries only, found isolation-condenser patents assigned to GE-Hitachi and a shaft-construction family that appears to be GE-Hitachi's, but no patent on the diaphragm-plate composite modules. It found no core LC³ composition patent, while Sika and Construction Research & Technology hold applications on LC³ workability and composition. This suggests, but does not establish, that C1's binder risk lies in qualification rather than patents; no freedom-to-operate search was done."
App E, last sentence of "What the patents show", replace "So for C1 the freedom-to-operate risk is low for the binder, and the commercial interest" with "So for C1 the patent risk for the binder looks low on these searches (no freedom-to-operate search was done), and the commercial interest".

### M4. App E: unsupported patent details (not in `sources_run8.md` or the briefs)
- P4 relevance cell: replace "Calcining low-kaolinite (<40%), iron-bearing clays at 600-1,000 °C widens the clay supply for LC³ (§5)" with "Reported to cover calcined clays of lower kaolinite content (below 40%), which would widen the clay supply for LC³ (§5)".
- P5 relevance cell: replace "LC³ with ≥40% kaolin clay calcined at 700-800 °C: consistent with the LC³ project's calcination window" with "Listed by ZKG as LC³ using low-temperature calcined clay; details not seen".
- P6 assignee: replace "Construction Research & Technology GmbH (Master Builders Solutions, formerly BASF)" with "Construction Research & Technology GmbH". Replace "the major admixture suppliers are commercialising LC³ (§10)" with "an admixture supplier is patenting LC³ compositions (§10)".

### M5. App E: markers and internal wording must go before submission
Remaining visible markers: the "[TO VERIFY ...]" strings in rows P2, P3, P4, P5 (assignee, year, title cells). Also the internal path "Full references: `02_Research/sources_run8.md`" and the instruction-style sentence in E1.
- P2 assignee/year cells: "Not confirmed (search summary only); inventors named as Hunt, Dahlgren and Marquino" / "n.d."
- P3 assignee: "Not confirmed; inventors include Kirby and McDonald (GE-Hitachi staff)". Year "2020" stays.
- P4 assignee/year: "Outotec (as listed)" / "2014".
- P5: replace row text with "KR 10-2843101 B1 | Limestone calcined clay cement using low-temperature calcined clay (title as listed by ZKG) | Not confirmed | n.d. | ..." using the replacement relevance cell in M4.
- E1, last sentence: replace "Assignees, dates and claims must be checked on the patent pages before the report relies on them." with "Assignees, dates and claims are as given in search summaries; the patent pages were not opened, so they are indicative only."
- Last line: replace "Full references: `02_Research/sources_run8.md`." with "Literature sources are listed in the reference list."
- Also add to the reference list or drop: Daehn et al. (2017) and BR3 (EPJ-N 2020) appear in E4 without a reference entry; replace "Daehn et al. (2017), via a 2025 review" and "BR3 (EPJ-N 2020)" with "a 2025 review of copper in steel scrap" and "a Belgian BR3 decommissioning study" if no entry is added.
- The line "*Drafted for Leroy; Leroy may reclaim.*" is Victor's call; the examiner should treat it as a deliberate disclosure, not a marker.

### M6. Hedging: code claim stated as fact (§10 T4 row 1)
Replace "qualification under NEDO-33926, which rests on AISC N690 (GE-Hitachi Nuclear Energy, 2024)" with "qualification under NEDO-33926, which reportedly rests on a modified AISC N690 (GE-Hitachi Nuclear Energy, 2024)". The brief marks the cement-type limits in NEDO-33926 §6.2.1 as not opened.

## Should-fix (not blocking)
- §4.1: "Darlington's construction licence took 29 months" (Oct 2022 to Apr 2025 is nearer 30); write "about 29 months". Same "about" for "8 years" is fine.
- §4.1 T2 caption cites NuScale (2023) for US$9.24 bn; the brief marks the exhibit figure as unopened. Add "as reported" after "US$9.24 bn".
- §4.2 and §6 both give the 167 vs 69 m³/MWe cross-check (R5.3 repetition); keep the §6 version if length bites.
- Ostrołęka reference has no URL; Systematic evaluation (2026) is cited by title (acceptable in Harvard when no author).
- §5 "Slag ... Not assessed" cell and the "no LC³ heat data found" gap are honest and match the brief; keep.

## Items verified against the brief (no change)
300 MWe / 315 net / CF 95% vendor vs 0.90 used; 60-year life; 7-day isolation condenser claim (hedged as GEH's statement); DP-SC description; ESBWR 69 m³/MWe; Ostrołęka 167 m³/MWe and 14,000 t; NuScale cancelled 8 Nov 2023, US460 approved May 2025; HTR-PM grid December 2021, commercial operation December 2023; Clinch River 29 September 2026 (web-confirmed); Darlington C$20.9 bn, Unit 1 October 2030, Units 2-4 approval expected 2028; Coalition 2035 vs CSIRO 2040; LC³ 380 vs 270 kg CO₂e/m³, 56.7 vs 60.0 MPa; slag 146.6 kg CO₂e/t; steel 2.33 / 0.68 t CO₂/t; Eu-152 about 35 cm; "a few per cent"; Krall 2-30x (contested); Synroc 1,000 °C / 30 MPa; Silex/GLE licence application accepted August 2025. The 23,100 t steel figure is correctly not used.

## Rubric IDs
- R1.4: sources are primary or regulator-grade where possible, but all unopened; M1-M6 make the hedging honest. Missing: a human opening of CNSC, OEB and NRC documents.
- R5.4: all citations have reference entries; Ostrołęka lacks a URL; App E patents are not in the reference list (acceptable as a log).
- RB.3: state of technology and TRL table present; add Linglong One clause (M1).
- RB.4: T3 and steel/EOL text cover extraction to end-of-life; europium/cobalt gap stated.
- RB.7: T4 gives needs and tests; key data gap (LC³ heat of hydration) stated.
