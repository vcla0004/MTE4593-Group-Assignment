Rubric coverage: see entries

## Method and access

- **Network.** No source could be opened. WebFetch failed at DNS (`ENOTFOUND`) for legislation.gov.au, classic.austlii.edu.au, justice.gov, world-nuclear.org, wnn.world-nuclear.org, pmc.ncbi.nlm.nih.gov, silex.com.au and archive.ourworldindata.org. Curl through the proxy returned no connection (code 000) for legislation.gov.au, ftc.gov, govinfo.gov, nrc.gov, canada.ca, aph.gov.au, concrete.org, ans.org, lowyinstitute.org, ourworldindata.org, pnas.org, en.wikipedia.org, parliament.nsw.gov.au, abc.net.au, newcastleherald.com.au, web.archive.org, iaea.org and osti.gov. The proxy log also shows earlier 403 denials for unece.org, ipcc.ch, nrel.gov and dcceew.gov.au.
- **Web search.** I ran WebSearch for alternative copies. Search summaries are recorded below as *leads* but never as verification. **No citation is marked "verified".** Every externally sourced claim is "unreachable (needs a human check)" unless the bibliography or our own results show a problem, which is marked separately.
- **Scripts.** I re-ran `hhi.py`, `displacement.py`, `schedule_value.py`, `same_money.py` and `law_timelines.py` with `python3 -I` from `03_LCA_Calculations`. All exit 0. All six result files are **byte-identical** to the versions before the run (diffed against a scratch copy). Every computed number below is checked against these outputs.
- **Status key.**
  - Citations: **verified**, **not supported**, **source not found**, **unreachable** (needs a human check).
  - Numbers and claims: **calc OK** (matches script output), **error** (wrong), **inconsistent** (differs across files), **overclaim**.

---

