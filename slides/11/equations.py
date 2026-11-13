"""Render the lie-factor and data-density formulas as SVGs.

Images instead of MathML: Brightspace re-renders math with MathJax and
ignores our sizing, so formulas came out huge and overlapped images.
"""
import matplotlib.pyplot as plt

plt.rcParams.update({"mathtext.fontset": "dejavuserif", "svg.fonttype": "path"})
TEXT = "#4c4f69"
eqs = {
    "eq_lie_factor": r"$\mathrm{lie\ factor} = \dfrac{\mathrm{size\ of\ effect\ shown\ in\ graph}}{\mathrm{size\ of\ effect\ in\ data}}$",
    "eq_data_density": r"$\mathrm{data\ density} = \dfrac{\mathrm{number\ of\ data\ points}}{\mathrm{area\ of\ data\ graphic}}$",
}
for name, tex in eqs.items():
    fig = plt.figure()
    fig.text(0, 0, tex, fontsize=24, color=TEXT)
    fig.savefig(f"images/{name}.svg", bbox_inches="tight", pad_inches=0.05, transparent=True)
    plt.close(fig)
