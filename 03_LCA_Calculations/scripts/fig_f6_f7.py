# Rubric coverage: R5.2, R2.1, R2.3, R3.6
"""Figures F6 and F7 (section 7), drawn from the results files so they always match the tables.

F6: CO2e avoided to 2050 by one BWRX-300, Darlington Unit 1 (from 2030) vs Liddell (from 2040; 2035 shown),
    read from results/displacement.md section 3 (Tables B17/B20).
F7: same money at Liddell (NEM-T2 slow, SMR from 2040): firmed renewables / SMR ratio of energy bought and of
    CO2e avoided to 2050, four cost cases, read from results/same_money.md section 5 (Table B28).
Style from scripts/lca_plot.py (imported read-only). No embedded titles; units on the axes; sized for half-page width.
Run: python3 -I 03_LCA_Calculations/scripts/fig_f6_f7.py   -> results/F6_displacement.png, results/F7_same_money.png
"""
from pathlib import Path
import importlib.util
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results"
spec = importlib.util.spec_from_file_location("lca_plot", ROOT / "scripts" / "lca_plot.py")
lp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lp)
plt = lp.plt


def mt(s):
    s = s.strip()
    x = float(re.sub(r"[^\d.\-]", "", s))
    return x / 1000 if s.endswith("kt") else x


def disp_rows():
    rows = {}
    for line in (RES / "displacement.md").read_text().splitlines():
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) == 7 and c[1].isdigit() and c[0] in ("Darlington U1", "Liddell"):
            rows[(c[0], int(c[1]), c[2])] = mt(c[5])  # to 2050
    return rows


def sm_rows():
    rows = {}
    for line in (RES / "same_money.md").read_text().splitlines():
        c = [x.strip() for x in line.strip("|").split("|")]
        if len(c) == 3 and c[1].endswith("x") and c[2].endswith("x"):
            rows[c[0]] = (float(c[1][:-1]), float(c[2][:-1]))
    return rows


def f6():
    r = disp_rows()
    cases = [  # label, key, colour, upper bound?
        ("Darlington, Ontario average\n(declining to 2040)", ("Darlington U1", 2030, "ON-avg-traj"), lp.BLUE, False),
        ("Darlington, marginal gas\n(leaves margin by 2050)", ("Darlington U1", 2030, "ON-marginal-declining"), lp.BLUE, False),
        ("Darlington, marginal held\nflat (upper bound)", ("Darlington U1", 2030, "ON-marginal-flat"), lp.BLUE, True),
        ("Liddell 2040, Step Change\nproxy", ("Liddell", 2040, "NEM-T1-StepChange-proxy"), lp.ORANGE, False),
        ("Liddell 2040, slower\ntransition", ("Liddell", 2040, "NEM-T2-slow"), lp.ORANGE, False),
        ("Liddell 2035, slower\ntransition", ("Liddell", 2035, "NEM-T2-slow"), lp.ORANGE, False),
        ("Liddell 2040, grid frozen\nat 640 g/kWh (upper bound)", ("Liddell", 2040, "NEM-T0-frozen"), lp.ORANGE, True),
    ]
    lp.style()
    plt.rcParams.update({"font.size": 8, "axes.grid.axis": "x"})
    fig, ax = plt.subplots(figsize=(3.6, 3.3))
    y = list(range(len(cases)))[::-1]
    for yi, (lab, k, col, ub) in zip(y, cases):
        val = r[k]
        ax.barh(yi, val, color="white" if ub else col, edgecolor=col, hatch="///" if ub else None, linewidth=1, height=0.65)
        ax.text(val + 0.25, yi, f"{val:.2f}" if val < 1 else f"{val:.1f}", va="center", fontsize=7.5, color=lp.INK)
    ax.set_yticks(y, [c[0] for c in cases], fontsize=7.5)
    ax.set_xlabel("CO$_2$e avoided to 2050, one unit (Mt)")
    ax.set_xlim(0, 19.5)
    ax.grid(axis="y", visible=False)
    ax.set_axisbelow(True)
    lp.save(fig, RES / "F6_displacement.png")


def f7():
    r = sm_rows()
    cases = [
        ("GenCost 2030 midpoints\n(SMR A\\$306, renewables A\\$107/MWh)", "Central: GenCost 2023-24 2030 midpoints (306 / 107)"),
        ("Worst case for renewables\n(SMR A\\$230, renewables A\\$153/MWh)", "Worst case for renewables on the 2030 reading (230 / 153)"),
        ("Alternative reading\n(SMR A\\$514, renewables A\\$102/MWh)", "Alternative reading, run 1 original (514 / 102)"),
        ("Lowest SMR lead\n(SMR A\\$198, renewables A\\$153/MWh)", "Lowest SMR lead, worst case tested (198 / 153)"),
    ]
    lp.style()
    plt.rcParams.update({"font.size": 8, "axes.grid.axis": "x"})
    fig, ax = plt.subplots(figsize=(3.6, 2.9))
    h = 0.36
    for i, (lab, key) in enumerate(cases):
        yi = len(cases) - 1 - i
        e, c = r[key]
        ax.barh(yi + h / 2, e, height=h, color=lp.AQUA, label="Energy bought" if i == 0 else None)
        ax.barh(yi - h / 2, c, height=h, color=lp.VIOLET, label="CO$_2$e avoided to 2050" if i == 0 else None)
        ax.text(e + 0.3, yi + h / 2, f"{e:.1f}×", va="center", fontsize=7.5, color=lp.INK)
        ax.text(c + 0.3, yi - h / 2, f"{c:.1f}×", va="center", fontsize=7.5, color=lp.INK)
    ax.axvline(1, color=lp.MUTED, linewidth=0.8, linestyle="--")
    ax.set_yticks(range(len(cases))[::-1], [c[0] for c in cases], fontsize=7.5)
    ax.set_xlabel("Firmed renewables ÷ one SMR, same spend (ratio, ×)")
    ax.set_xlim(0, 22)
    ax.grid(axis="y", visible=False)
    ax.set_axisbelow(True)
    ax.legend(loc="lower right", fontsize=7.5)
    lp.save(fig, RES / "F7_same_money.png")


if __name__ == "__main__":
    f6()
    f7()
    print("wrote", RES / "F6_displacement.png", RES / "F7_same_money.png")
