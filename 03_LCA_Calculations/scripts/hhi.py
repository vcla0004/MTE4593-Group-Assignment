# Rubric coverage: R3.2, R2.1, R2.4, R2.7, R3.8, RB.5
"""Herfindahl-Hirschman index (HHI) for the BWRX-300 fuel supply chain.

Stages: uranium mining (by country, and a bounded estimate by company), conversion (by company)
and enrichment (by company). Sensitivity: with and without Russia (sanctions/ban scenario),
without Russia and China (market open to a Western buyer), data year, treatment of the
"Other" rows, and an alternative ConverDyn capacity.

Method
  share_i = 100 * q_i / sum(q)                      (percent)
  HHI     = sum(share_i ** 2)                       (0 to 10,000)
  N_eq    = 10,000 / HHI                            (equivalent number of equal-sized suppliers)
  "Without X": X's quantity is removed and shares are renormalised over the remaining suppliers,
  i.e. the market a buyer barred from X can still draw on (capacity is assumed not to expand).
  Residual / "Other" rows: upper bound treats the row as one supplier; lower bound treats it as
  infinitely many small suppliers (contributes ~0 to HHI).

Inputs : 03_LCA_Calculations/parameters_run3.yaml
Outputs: 03_LCA_Calculations/results/hhi.md, results/hhi_summary.csv
Run    : python3 -I 03_LCA_Calculations/scripts/hhi.py
"""
from __future__ import annotations

import csv
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
PARAMS = ROOT / "parameters_run3.yaml"
RESULTS = ROOT / "results"


def load() -> dict:
    with PARAMS.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def shares(q: dict[str, float]) -> dict[str, float]:
    total = sum(q.values())
    return {k: 100.0 * v / total for k, v in q.items()}


def hhi(q: dict[str, float], atomistic: tuple[str, ...] = ()) -> float:
    """HHI in points. Keys in `atomistic` count towards the total but add ~0 to the sum of squares."""
    s = shares(q)
    return sum(v ** 2 for k, v in s.items() if k not in atomistic)


def drop(q: dict[str, float], *keys: str) -> dict[str, float]:
    return {k: v for k, v in q.items() if k not in keys}


def classify(h: float, t: dict) -> tuple[str, str]:
    t23 = t["doj_ftc_2023_highly_concentrated"]["value"]
    lo10 = t["doj_ftc_2010_unconcentrated_below"]["value"]
    hi10 = t["doj_ftc_2010_highly_concentrated"]["value"]
    c2023 = "highly concentrated" if h > t23 else "not highly concentrated"
    if h < lo10:
        c2010 = "unconcentrated"
    elif h <= hi10:
        c2010 = "moderately concentrated"
    else:
        c2010 = "highly concentrated"
    return c2023, c2010


def share_table(q: dict[str, float], unit: str) -> list[str]:
    s = shares(q)
    rows = [f"| Supplier | {unit} | Share (%) | Share² |", "|---|---:|---:|---:|"]
    for k, v in sorted(q.items(), key=lambda kv: -kv[1]):
        rows.append(f"| {k} | {v:,.0f} | {s[k]:.2f} | {s[k] ** 2:,.1f} |")
    rows.append(f"| **Total / HHI** | {sum(q.values()):,.0f} | 100.00 | **{sum(x ** 2 for x in s.values()):,.0f}** |")
    return rows


def main() -> None:
    p = load()
    t = p["thresholds"]
    out: list[str] = []
    summary: list[dict] = []

    def record(stage: str, scenario: str, h: float, note: str = "") -> None:
        c23, c10 = classify(h, t)
        summary.append({"stage": stage, "scenario": scenario, "hhi": round(h),
                        "n_equivalent": round(10000 / h, 1), "doj_ftc_2023": c23,
                        "doj_ftc_2010": c10, "note": note})

    # ---------------- Mining by country ----------------
    m = p["mining_by_country"]
    m24 = {k: float(v) for k, v in m[2024].items()}
    listed_sum = sum(m24.values())
    assert abs(listed_sum - m["world_total"][2024]) < 1, "2024 rows do not sum to world total"

    record("Mining (country)", "2024 base", hhi(m24))
    record("Mining (country)", "2024 base, 'Others' atomistic", hhi(m24, ("Others",)), "lower bound")
    record("Mining (country)", "2024 without Russia", hhi(drop(m24, "Russia")))
    record("Mining (country)", "2024 without Russia and China", hhi(drop(m24, "Russia", "China")))
    record("Mining (country)", "2024 without Russia, China and Niger", hhi(drop(m24, "Russia", "China", "Niger")),
           "Niger: exports disrupted since the 2023 coup (Orano/Somair; secondary)")

    year_rows = []
    for yr in (2022, 2023):
        q = {k: float(v) for k, v in m[yr].items()}
        resid = m["world_total"][yr] - sum(q.values())
        q["Rest of world (residual)"] = resid
        hi_b = hhi(q)
        lo_b = hhi(q, ("Rest of world (residual)",))
        year_rows.append((yr, resid, lo_b, hi_b, shares(q)["Russia"]))
        record("Mining (country)", f"{yr} (residual bounds)", (lo_b + hi_b) / 2,
               f"range {lo_b:,.0f} to {hi_b:,.0f}")
        q_nr = drop(q, "Russia")
        record("Mining (country)", f"{yr} without Russia (residual bounds)",
               (hhi(q_nr) + hhi(q_nr, ("Rest of world (residual)",))) / 2,
               f"range {hhi(q_nr, ('Rest of world (residual)',)):,.0f} to {hhi(q_nr):,.0f}")

    # Mining by company (bounded; only top three shares known)
    mc = p["mining_by_company_2024_pct"]
    known = {k: float(v) for k, v in mc.items() if k not in ("source", "verified")}
    rest = 100.0 - sum(known.values())
    lo_c = sum(v ** 2 for v in known.values())
    cap = min(known.values())  # remaining firms are each no larger than the third-ranked firm
    n_full, rem = divmod(rest, cap)
    hi_c = lo_c + n_full * cap ** 2 + rem ** 2
    record("Mining (company)", "2024 bounds (top 3 known)", (lo_c + hi_c) / 2,
           f"range {lo_c:,.0f} to {hi_c:,.0f}; STRETCH, partial data")

    # ---------------- Conversion ----------------
    cv = p["conversion_by_company"]
    cap_q = {k: float(v) for k, v in cv["capacity"].items()}
    prod_q = {k: float(v) for k, v in cv["production"].items()}
    alt_q = dict(cap_q, ConverDyn=float(cv["converdyn_capacity_alt"]["value"]))
    record("Conversion", "capacity base", hhi(cap_q))
    record("Conversion", "capacity without Russia", hhi(drop(cap_q, "Rosatom")))
    record("Conversion", "capacity without Russia and China", hhi(drop(cap_q, "Rosatom", "CNNC")),
           "market open to a Western buyer")
    record("Conversion", "production base", hhi(prod_q))
    record("Conversion", "production without Russia", hhi(drop(prod_q, "Rosatom")))
    record("Conversion", "capacity, ConverDyn 15,000 tU (alt.)", hhi(alt_q), "secondary source; sensitivity only")
    record("Conversion", "ConverDyn alt., without Russia", hhi(drop(alt_q, "Rosatom")))
    record("Conversion", "ConverDyn alt., without Russia and China", hhi(drop(alt_q, "Rosatom", "CNNC")))

    # ---------------- Enrichment ----------------
    en = p["enrichment_by_company"]
    oth = ("Other_INB_JNFL",)
    enr = {yr: {k: float(v) for k, v in en[yr].items()} for yr in (2022, 2025, 2030)}
    for yr, q in enr.items():
        assert abs(sum(q.values()) - en["stated_total"][yr]) <= 1.5, f"{yr} enrichment rows != total"
        tag = "base" if yr == 2025 else "year sensitivity"
        record("Enrichment", f"{yr} capacity ({tag})", hhi(q), f"Other atomistic: {hhi(q, oth):,.0f}")
        record("Enrichment", f"{yr} without Russia", hhi(drop(q, "Rosatom")),
               f"Other atomistic: {hhi(drop(q, 'Rosatom'), oth):,.0f}")
        record("Enrichment", f"{yr} without Russia and China", hhi(drop(q, "Rosatom", "CNNC")),
               f"market open to a Western buyer; Other atomistic: {hhi(drop(q, 'Rosatom', 'CNNC'), oth):,.0f}")

    # ---------------- Key shares ----------------
    s_m24 = shares(m24)
    s_cv = shares(cap_q)
    s_cv_w = shares(drop(cap_q, "Rosatom", "CNNC"))
    s_en = {yr: shares(q) for yr, q in enr.items()}
    s_en_w = shares(drop(enr[2025], "Rosatom", "CNNC"))
    au = p["australia"]
    req = p["world_reactor_requirements_2025_tU"]["value"]
    mine_cover = 100 * m["world_total"][2024] / req

    # ---------------- Write markdown ----------------
    out += [
        "Rubric coverage: R3.2, R2.1, R2.4, R2.7, R3.8, R3.5, RB.5",
        "",
        "# HHI for the BWRX-300 fuel supply chain (Appendix B working)",
        "",
        "Generated by `03_LCA_Calculations/scripts/hhi.py` from `parameters_run3.yaml`. Do not edit by hand; "
        "rerun the script after changing a parameter.",
        "",
        "> **Verification status: NOT YET CITABLE.** Every input was taken from search-engine extracts of the "
        "named World Nuclear Association, NEA/IAEA and US government pages, because none of those hosts could be "
        "opened from the analyst's session. Internal checks passed (2024 mining rows sum exactly to the world "
        "total of 60,213 tU; conversion and enrichment rows sum to their stated totals). Victor or the "
        "fact-checker must open each page, confirm the numbers and set `verified: true` before any value goes "
        "into the report or slides.",
        "",
        "## 1. Method",
        "",
        "- Share of supplier *i*: s_i = 100 × q_i / Σq (percent). HHI = Σ s_i² (0 to 10,000). "
        "Equivalent number of equal suppliers N_eq = 10,000 / HHI.",
        "- Mining is measured by country (2024 mine output, tU); conversion by company (licensed capacity, "
        "tU as UF₆ per year; production as a check); enrichment by company (capacity, thousand SWU per year, "
        "2025 base, 2022 and 2030 as sensitivity).",
        "- \"Without Russia\": Russian supply is removed and shares are renormalised over the rest, i.e. the "
        "market left to a buyer barred from Russian material, with no new capacity. \"Without Russia and China\": "
        "also removes CNNC, whose enrichment capacity WNA estimates on the assumption that it serves China's own "
        "fleet; this approximates the market open to a Canadian or Australian utility.",
        "- Rows of \"Others\" or a residual are bounded: one supplier (upper bound) vs many small suppliers "
        "(lower bound, ~0). The difference is below 3 points in every 2024/2025 case.",
        "- Thresholds: US DOJ and FTC (2023) *Merger Guidelines*: HHI > 1,800 is highly concentrated. "
        "The superseded 2010 *Horizontal Merger Guidelines*: < 1,500 unconcentrated, 1,500–2,500 moderately "
        "concentrated, > 2,500 highly concentrated. Both are reported because the mining result falls between "
        "them. These are antitrust screens for merger review; here they are used as a recognised scale for supply "
        "concentration, not as a legal test.",
        "",
        "## 2. Headline results",
        "",
        "| Stage (2024/2025 base) | HHI | 2023 guideline | 2010 guideline | Without Russia | Without Russia and China |",
        "|---|---:|---|---|---:|---:|",
    ]

    def get(stage: str, scen: str) -> dict:
        return next(r for r in summary if r["stage"] == stage and r["scenario"] == scen)

    for stage, base, nr, nrc in [
        ("Mining (country)", "2024 base", "2024 without Russia", "2024 without Russia and China"),
        ("Conversion", "capacity base", "capacity without Russia", "capacity without Russia and China"),
        ("Enrichment", "2025 capacity (base)", "2025 without Russia", "2025 without Russia and China"),
    ]:
        b, r1, r2 = get(stage, base), get(stage, nr), get(stage, nrc)
        out.append(f"| {stage} | **{b['hhi']:,}** | {b['doj_ftc_2023']} | {b['doj_ftc_2010']} | "
                   f"{r1['hhi']:,} ({r1['doj_ftc_2010']} under 2010) | {r2['hhi']:,} |")

    out += [
        "",
        f"- Russia's share: mining {s_m24['Russia']:.1f}% (country output, 2024); conversion "
        f"{s_cv['Rosatom']:.1f}% (capacity); enrichment **{s_en[2025]['Rosatom']:.1f}%** (2025 capacity; "
        f"{s_en[2022]['Rosatom']:.1f}% in 2022; {s_en[2030]['Rosatom']:.1f}% planned for 2030).",
        "- Removing Russia **raises** the HHI at every stage: the remaining market is smaller and still "
        "dominated by a few suppliers. Under the 2010 scale, 2024 mining moves from moderately to highly "
        "concentrated (the 2023-data case stays just below 2,500; see section 4).",
        f"- Without Russia and China, enrichment is an Urenco–Orano duopoly: Urenco {s_en_w['Urenco']:.1f}%, "
        f"Orano {s_en_w['Orano']:.1f}% (N_eq = {get('Enrichment', '2025 without Russia and China')['n_equivalent']}).",
        f"- Canada (Cameco, Port Hope) holds {s_cv['Cameco']:.1f}% of world conversion capacity and "
        f"{s_cv_w['Cameco']:.1f}% of the capacity open to a Western buyer; Canada mined {s_m24['Canada']:.1f}% of "
        "world uranium in 2024. Canada has no enrichment plant.",
        f"- Australia: {au['share_identified_recoverable_resources_usd130_rb2024']['value']}% of identified "
        "recoverable resources at < USD 130/kgU (Red Book 2024; "
        f"{au['share_identified_recoverable_resources_usd130_rb2026']['value']}% in Red Book 2026 as tabulated "
        f"by WNA, TO VERIFY), but {s_m24['Australia']:.1f}% of 2024 mine output ({au['production_2024_tU']['value']:,} tU) "
        "and 0% of conversion and enrichment capacity.",
        f"- Mine output in 2024 ({m['world_total'][2024]:,} tU) equalled {mine_cover:.0f}% of reactor requirements "
        f"at 1 January 2025 ({req:,} tU, Red Book 2026, TO VERIFY); the rest comes from secondary supply "
        "(inventories, down-blending, re-enriched tails), which this HHI does not cover.",
        "",
        "## 3. Working: shares and squared shares",
        "",
        "### 3.1 Mining by country, 2024 (tU)",
        "",
        *share_table(m24, "tU"),
        "",
        "### 3.2 Mining by country, 2024, without Russia",
        "",
        *share_table(drop(m24, "Russia"), "tU"),
        "",
        "### 3.3 Mining by country, earlier years (only the eight largest rows retrieved; residual bounded)",
        "",
        "| Year | Residual (tU) | HHI lower bound | HHI upper bound | Russia share (%) |",
        "|---|---:|---:|---:|---:|",
    ]
    for yr, resid, lo_b, hi_b, rs in year_rows:
        out.append(f"| {yr} | {resid:,.0f} | {lo_b:,.0f} | {hi_b:,.0f} | {rs:.1f} |")
    out += [
        "",
        "### 3.4 Mining by company, 2024 (STRETCH, partial)",
        "",
        f"Only the top three shares were retrieved: {', '.join(f'{k} {v:.0f}%' for k, v in known.items())} "
        f"(sum {sum(known.values()):.0f}%). Lower bound (remaining {rest:.0f}% atomistic): {lo_c:,.0f}. "
        f"Upper bound (remaining {rest:.0f}% split into firms no larger than the third-ranked, {cap:.0f}%): "
        f"{hi_c:,.0f}. Either way the company-level HHI is below 1,500 (unconcentrated under 2010; "
        "not highly concentrated under 2023): concentration in mining is a **country** (geopolitical) risk, "
        "not a firm-level market-power risk. Kazatomprom's 21% is attributable production; Kazakhstan's 38.6% "
        "country share includes joint ventures with Cameco, Orano, Uranium One (Rosatom) and Chinese partners "
        "[TO VERIFY ownership detail].",
        "",
        "### 3.5 Conversion by company, licensed capacity (tU as UF₆/yr)",
        "",
        *share_table(cap_q, "tU/yr"),
        "",
        "Without Russia:",
        "",
        *share_table(drop(cap_q, "Rosatom"), "tU/yr"),
        "",
        "Without Russia and China:",
        "",
        *share_table(drop(cap_q, "Rosatom", "CNNC"), "tU/yr"),
        "",
        "### 3.6 Enrichment by company, 2025 capacity (thousand SWU/yr)",
        "",
        *share_table(enr[2025], "kSWU/yr"),
        "",
        "Without Russia:",
        "",
        *share_table(drop(enr[2025], "Rosatom"), "kSWU/yr"),
        "",
        "Without Russia and China:",
        "",
        *share_table(drop(enr[2025], "Rosatom", "CNNC"), "kSWU/yr"),
        "",
        "## 4. Sensitivity (all scenarios)",
        "",
        "| Stage | Scenario | HHI | N_eq | 2023 guideline | 2010 guideline | Note |",
        "|---|---|---:|---:|---|---|---|",
    ]
    for r in summary:
        out.append(f"| {r['stage']} | {r['scenario']} | {r['hhi']:,} | {r['n_equivalent']} | "
                   f"{r['doj_ftc_2023']} | {r['doj_ftc_2010']} | {r['note']} |")
    out += [
        "",
        "Reading the sensitivity:",
        "- **Data year** (enrichment 2022 → 2030; mining 2022 → 2024) moves the HHI by a few hundred points but "
        "never changes the 2023-guideline class: enrichment and conversion are highly concentrated in every year.",
        "- **Capacity vs production** (conversion) changes the HHI by less than 10 points.",
        "- **ConverDyn's capacity** (7,000 vs 15,000 tU) is the largest single data uncertainty for conversion; "
        "the higher value lowers the HHI but all conversion cases stay above 1,800.",
        "- **Removing Russia** is the dominant effect at every stage and always increases concentration.",
        "",
        "## 5. Limitations",
        "",
        "- Capacity is not supply: nameplate SWU includes capacity Rosatom uses for underfeeding and tails "
        "re-enrichment, and CNNC's figures are WNA estimates. Secondary supply is excluded.",
        "- Company-level enrichment concentration hides plant location: Urenco operates in the UK, Germany, the "
        "Netherlands and the USA; Orano only in France.",
        "- Mining by country ignores ownership (e.g. Rosatom's Uranium One stakes in Kazakh mines) and transport "
        "routes for Kazakh exports [TO VERIFY]; the company-level bound partly addresses ownership.",
        "- Merger-guideline thresholds are antitrust screens; their use here is an analogy for supply risk.",
        "",
    ]

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "hhi.md").write_text("\n".join(out), encoding="utf-8")
    with (RESULTS / "hhi_summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()))
        w.writeheader()
        w.writerows(summary)

    for r in summary:
        print(f"{r['stage']:<18} {r['scenario']:<45} {r['hhi']:>6,}  {r['doj_ftc_2023']:<24} {r['doj_ftc_2010']}")
    print(f"Russia enrichment share 2025: {s_en[2025]['Rosatom']:.2f}%  (2022 {s_en[2022]['Rosatom']:.2f}%, "
          f"2030 {s_en[2030]['Rosatom']:.2f}%)")


if __name__ == "__main__":
    main()
