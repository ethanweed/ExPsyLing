"""Fake paired data (reaction times, two conditions) plotted several ways."""
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(11)
n = 20
base = rng.normal(600, 80, n)                  # big between-subject spread
before = base + rng.normal(0, 20, n)
after = base - 30 + rng.normal(0, 20, n)        # small, consistent effect
df = pd.DataFrame({"subject": np.arange(n), "Congruent": after, "Incongruent": before})
long = df.melt("subject", var_name="condition", value_name="rt")
diff = df.Incongruent - df.Congruent
t, p = stats.ttest_rel(df.Incongruent, df.Congruent)
print(f"t({n-1}) = {t:.2f}, p = {p:.2g}, mean diff = {diff.mean():.1f} ms")

TEAL, ORANGE, BLUE, GREY = "#4C827B", "#CD5909", "#1e66f5", "#9ca0b0"
pal = {"Congruent": TEAL, "Incongruent": ORANGE}
sns.set_theme(style="ticks", font="Georgia", font_scale=1.3)
YL = "Reaction time (ms)"

def save(fig, name):
    sns.despine(fig=fig); fig.tight_layout()
    fig.savefig(f"images/paired_{name}.png", dpi=150); plt.close(fig)

def ax1(): return plt.subplots(figsize=(6, 5))

fig, ax = ax1()
sns.barplot(long, x="condition", y="rt", hue="condition", palette=pal, errorbar="se", ax=ax)
ax.set(xlabel="", ylabel=YL); save(fig, "bar")

fig, ax = ax1()
sns.barplot(long, x="condition", y="rt", hue="condition", palette=pal, errorbar="se", ax=ax)
ax.set(xlabel="", ylabel=YL, ylim=(560, 640)); save(fig, "bar_zoom")

fig, ax = ax1()
sns.boxplot(long, x="condition", y="rt", hue="condition", palette=pal, width=0.5, ax=ax)
ax.set(xlabel="", ylabel=YL); save(fig, "box")

fig, ax = ax1()
sns.violinplot(long, x="condition", y="rt", hue="condition", palette=pal, inner=None, alpha=0.3, ax=ax)
sns.stripplot(long, x="condition", y="rt", hue="condition", palette=pal, size=7, jitter=0.08, ax=ax)
ax.set(xlabel="", ylabel=YL); save(fig, "violin_strip")

fig, ax = ax1()
sns.lineplot(long, x="condition", y="rt", units="subject", estimator=None, color=GREY, lw=1, ax=ax)
sns.stripplot(long, x="condition", y="rt", hue="condition", palette=pal, size=7, jitter=False, ax=ax, zorder=3)
sns.pointplot(long, x="condition", y="rt", color="black", errorbar="se", markers="D", ax=ax)
ax.set(xlabel="", ylabel=YL); ax.margins(x=0.15); save(fig, "lines")

fig, ax = ax1()
sns.violinplot(long, x="condition", y="rt", hue="condition", palette=pal, inner=None, alpha=0.3, ax=ax)
sns.lineplot(long, x="condition", y="rt", units="subject", estimator=None, color=GREY, lw=1, ax=ax)
sns.stripplot(long, x="condition", y="rt", hue="condition", palette=pal, size=7, jitter=False, ax=ax, zorder=3)
ax.set(xlabel="", ylabel=YL); save(fig, "violin_lines")

# raincloud: half-violin (cloud) facing out, box + points (rain), lines inside
fig, ax = ax1()
ys = np.linspace(long.rt.min() - 60, long.rt.max() + 60, 300)
for x, cond, side in [(0, "Congruent", -1), (1, "Incongruent", 1)]:
    v = df[cond]
    dens = stats.gaussian_kde(v)(ys)
    ax.fill_betweenx(ys, x + side * 0.15, x + side * (0.15 + dens / dens.max() * 0.35),
                     color=pal[cond], alpha=0.3, lw=0)
    ax.boxplot(v, positions=[x + side * 0.08], widths=0.06, showfliers=False,
               medianprops=dict(color="black"), boxprops=dict(color=pal[cond]),
               whiskerprops=dict(color=pal[cond]), capprops=dict(color=pal[cond]))
for a, b in zip(df.Congruent, df.Incongruent):
    ax.plot([0, 1], [a, b], color=GREY, lw=1)
ax.scatter(np.zeros(n), df.Congruent, color=TEAL, s=40, zorder=3)
ax.scatter(np.ones(n), df.Incongruent, color=ORANGE, s=40, zorder=3)
ax.set(xticks=[0, 1], xticklabels=["Congruent", "Incongruent"], xlim=(-0.6, 1.6), ylabel=YL)
save(fig, "raincloud")

fig, ax = ax1()
lo, hi = long.rt.min() - 20, long.rt.max() + 20
ax.plot([lo, hi], [lo, hi], color=GREY, ls="--")
below = df.Incongruent < df.Congruent
sns.scatterplot(df, x="Congruent", y="Incongruent", hue=below,
                palette={False: BLUE, True: "#d20f39"}, s=70, legend=False, ax=ax)
ax.set(xlim=(lo, hi), ylim=(lo, hi), aspect="equal",
       xlabel="Congruent RT (ms)", ylabel="Incongruent RT (ms)"); save(fig, "scatter")

fig, ax = ax1()
sns.stripplot(y=diff, color=BLUE, size=7, jitter=0.08, ax=ax)
sns.pointplot(y=diff, color=ORANGE, errorbar=("ci", 95), markers="D", ax=ax)
ax.axhline(0, color=GREY, ls="--")
ax.set(ylabel="Incongruent − Congruent (ms)", xticks=[]); save(fig, "diff")
