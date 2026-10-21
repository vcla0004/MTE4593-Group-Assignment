# Rubric coverage: R5.2, R2.4
"""Common chart style for F1-F5 (one palette and style for the report and slides; plan section 3)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Reference categorical palette (light mode), fixed order; text never wears series colour.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
INK, INK2, MUTED, GRID, SURFACE = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#ffffff"


def style():
    plt.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "font.family": "DejaVu Sans", "font.size": 9.5,
        "axes.edgecolor": GRID, "axes.labelcolor": INK2, "axes.titlecolor": INK,
        "axes.titlesize": 11, "axes.titleweight": "bold", "axes.titlelocation": "left",
        "xtick.color": INK2, "ytick.color": INK2, "axes.grid": True, "grid.color": GRID,
        "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False, "legend.fontsize": 9,
    })


def save(fig, path, source_note=None):
    if source_note:
        fig.text(0.01, -0.035, source_note, fontsize=7.5, color=MUTED, ha="left", va="bottom")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
