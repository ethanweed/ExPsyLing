"""Re-draw the misleading TV bar charts with the y-axis starting at 0."""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

plt.rcParams.update({"font.family": "Georgia", "font.size": 14})
charts = {
    "buzz1": dict(title="Obamacare enrollment", labels=["As of March 27", "March 31 goal"],
                  values=[6_000_000, 7_066_000], color="#1f4fa8", ylabel="Sign-ups",
                  fmt=lambda v: f"{v:,.0f}", tick=lambda v, _: f"{v/1e6:.0f}M"),
    "buzz2": dict(title="Top tax rate if Bush tax cuts expire", labels=["Now", "Jan. 1, 2013"],
                  values=[35, 39.6], color="#d9a520", ylabel="Top tax rate (%)",
                  fmt=lambda v: f"{v:g}%", tick=lambda v, _: f"{v:.0f}%"),
    "buzz3": dict(title="R.A. Dickey knuckleball velocity", labels=["2012", "2013"],
                  values=[77.3, 75.3], color="#1f4fa8", ylabel="Velocity (mph)",
                  fmt=lambda v: f"{v} mph", tick=lambda v, _: f"{v:.0f}"),
}
for name, c in charts.items():
    fig, ax = plt.subplots(figsize=(6.25, 4.69))
    bars = ax.bar(c["labels"], c["values"], color=c["color"], width=0.55)
    for b, v in zip(bars, c["values"]):
        ax.text(b.get_x() + b.get_width() / 2, v + max(c["values"]) * 0.015, c["fmt"](v),
                ha="center", va="bottom", fontsize=14)
    ax.set_ylim(0, max(c["values"]) * 1.15)
    ax.yaxis.set_major_formatter(FuncFormatter(c["tick"]))
    ax.set(title=c["title"], ylabel=c["ylabel"])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    fig.savefig(f"images/fixed_{name}.png", dpi=150)
    plt.close(fig)
