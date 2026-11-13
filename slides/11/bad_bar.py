"""A deliberately terrible bar plot of the paired data."""
import numpy as np, matplotlib.pyplot as plt
from matplotlib import font_manager
from mpl_toolkits.mplot3d import Axes3D  # noqa

rng = np.random.default_rng(11)
n = 20
base = rng.normal(600, 80, n)
incon = base + rng.normal(0, 20, n)
con = base - 30 + rng.normal(0, 20, n)
means = [con.mean(), incon.mean()]

names = {f.name for f in font_manager.fontManager.ttflist}
font = "Comic Sans MS" if "Comic Sans MS" in names else "fantasy"
plt.rcParams["font.family"] = font

fig = plt.figure(figsize=(9, 6.5), facecolor="#7a9a00")
ax = fig.add_subplot(projection="3d", facecolor="#b07000")
floor = 575                                   # broken y-axis: start well above 0
cols = ["#3c9a00", "#c25a00"]   # red-green pair, same lightness
for i, (m, c) in enumerate(zip(means, cols)):
    ax.bar3d(i, 0, floor, 0.6, 0.6, m - floor, color=c, edgecolor="black",
             shade=True, alpha=0.9, hatch="//")
    ax.text(i + 0.3, 0.3, m + 3, f"{m:.7f} ms!!!", color="#3c9a00", fontsize=13,
            fontweight="bold")
ax.set_zlim(floor, 615)
ax.set_xticks([0.3, 1.3]); ax.set_xticklabels(["CONG.", "INCONG."], rotation=35, color="#c25a00")
ax.set_yticks([0, 0.3, 0.6]); ax.set_yticklabels(["depth", "more depth", "???"], color="#5f8f00")
ax.set_zlabel("RT(?)", color="#b04a00", fontsize=16)
ax.view_init(elev=28, azim=-62)
ax.grid(True, lw=3)
for a in (ax.xaxis, ax.yaxis, ax.zaxis):
    a.pane.set_facecolor("#8fa000"); a.pane.set_edgecolor("#c03000"); a.pane.set_linewidth(4)
fig.suptitle("WOW!!! INCONGRUENT IS WAY SLOWER!!!", fontsize=24, color="#c04000",
             fontweight="bold", rotation=3)
fig.text(0.5, 0.03, "Data: trust me  |  error bars: optional", ha="center",
         fontsize=12, color="#5a7a00", style="italic")
from matplotlib.patches import Patch
fig.legend([Patch(color=c) for c in cols], ["Congruent (green)", "Incongruent (red)"],
           loc="upper left", fontsize=12, shadow=True, facecolor="#9a8a00", title="LEGEND")
fig.savefig("images/paired_bad_bar.png", dpi=150, facecolor=fig.get_facecolor())
