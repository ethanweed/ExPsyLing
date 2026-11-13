"""Annotated example figures for 'How to read a figure' slides (fake data)."""
import numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)
TEAL, ORANGE, BLUE, GREY = "#4C827B", "#CD5909", "#1e66f5", "#9ca0b0"
sns.set_theme(style="ticks", font="Georgia", font_scale=1.3)
ANNOTATE = False   # True: orange teaching labels; False: blank for live annotation
ARW = dict(arrowstyle="->", color=ORANGE, lw=1.8)

def note(ax, text, xy, xytext, **kw):
    if not ANNOTATE:
        return
    ax.annotate(text, xy=xy, xytext=xytext, color=ORANGE, fontsize=13,
                fontweight="bold", arrowprops=ARW, **kw)

def save(fig, name):
    sns.despine(fig=fig); fig.tight_layout()
    fig.savefig(f"images/read_{name}.png", dpi=150); plt.close(fig)

# 1. paired t-test ---------------------------------------------------------
n = 15
base = rng.normal(600, 60, n)
a, b = base + rng.normal(0, 15, n), base + 35 + rng.normal(0, 15, n)
fig, ax = plt.subplots(figsize=(7, 5.5))
for y0, y1 in zip(a, b):
    ax.plot([0, 1], [y0, y1], color=GREY, lw=1)
ax.scatter(np.zeros(n), a, color=TEAL, zorder=3); ax.scatter(np.ones(n), b, color=ORANGE, zorder=3)
m, se = [a.mean(), b.mean()], [stats.sem(a), stats.sem(b)]
ax.errorbar([0, 1], m, yerr=se, color="black", marker="D", ms=8, lw=2.5, zorder=4)
i = np.argmax(a)
note(ax, "one line = one person", ((0.5), (a[i] + b[i]) / 2), (0.05, a.max() + 45))
note(ax, "mean ± SE", (1, m[1]), (1.12, m[1] - 80))
note(ax, "most lines go up\n= consistent effect", (0.7, np.sort(b)[2] - 10), (1.1, a.min() - 10))
ax.set(xticks=[0, 1], xticklabels=["Congruent", "Incongruent"], xlim=(-0.3, 1.7),
       ylabel="Reaction time (ms)")
save(fig, "paired")

# 1b. independent samples t-test ---------------------------------------
# own generator so adding this figure doesn't change the others
r2 = np.random.default_rng(7)
d = pd.DataFrame({"group": np.repeat(["Native", "L2"], 15),
                  "rt": np.concatenate([r2.normal(600, 60, 15), r2.normal(650, 60, 15)])})
fig, ax = plt.subplots(figsize=(7, 5.5))
sns.stripplot(d, x="group", y="rt", hue="group", palette=[TEAL, ORANGE], size=7,
              jitter=0.12, ax=ax)
sns.pointplot(d, x="group", y="rt", color="black", errorbar="se", markers="D",
              linestyles="none", ax=ax)
ax.set(xlabel="", ylabel="Reaction time (ms)", xlim=(-0.5, 1.5))
save(fig, "indep")

# 2. one-way ANOVA ---------------------------------------------------------
groups = ["Control", "Drug A", "Drug B"]
d = pd.DataFrame({"group": np.repeat(groups, 20),
                  "score": np.concatenate([rng.normal(mu, 8, 20) for mu in (50, 58, 62)])})
fig, ax = plt.subplots(figsize=(7, 5.5))
sns.stripplot(d, x="group", y="score", color=GREY, size=6, jitter=0.12, alpha=0.8, ax=ax)
sns.pointplot(d, x="group", y="score", color=ORANGE, errorbar=("ci", 95), markers="D",
              linestyles="none", ax=ax)
gm = d.score.mean()
ax.axhline(gm, color=TEAL, ls="--")
if ANNOTATE: ax.text(2.45, gm, "grand\nmean", color=TEAL, va="center", fontsize=12)
ctrl = d[d.group == "Control"].score
note(ax, "spread within groups\n= noise", (0, ctrl.max()), (-0.4, ctrl.max() + 12))
note(ax, "spread between means\n= signal", (2, d[d.group == "Drug B"].score.mean()), (1.1, 25))
ax.set(xlabel="", ylabel="Score", xlim=(-0.5, 2.9), ylim=(20, d.score.max() + 22))
save(fig, "anova1")

# 3. two-way ANOVA (interaction plot) --------------------------------------
cells = {("Easy", "Native"): 520, ("Hard", "Native"): 560,
         ("Easy", "L2"): 560, ("Hard", "L2"): 680}
rows = [(t, g, rng.normal(mu, 40)) for (t, g), mu in cells.items() for _ in range(25)]
d = pd.DataFrame(rows, columns=["task", "group", "rt"])
fig, ax = plt.subplots(figsize=(7, 5.5))
sns.pointplot(d, x="task", y="rt", hue="group", palette=[TEAL, ORANGE], errorbar="se",
              markers=["o", "s"], dodge=0.1, ax=ax)
mL2 = d[(d.group == "L2") & (d.task == "Hard")].rt.mean()
mN = d[(d.group == "Native") & (d.task == "Hard")].rt.mean()
note(ax, "lines not parallel\n= interaction", (0.6, 640), (-0.2, 690))
note(ax, "gap between lines\n= main effect of group", (1.0, (mL2 + mN) / 2), (1.08, 600))
note(ax, "lines slope up\n= main effect of task", (0.5, 537), (0.35, 470))
ax.set(xlabel="Task difficulty", ylabel="Reaction time (ms)", ylim=(450, 720), xlim=(-0.3, 1.7))
ax.legend(title="Group", frameon=False, loc="lower right", bbox_to_anchor=(1, 0.0))
save(fig, "anova2")

# 4. linear regression -----------------------------------------------------
x = rng.uniform(0, 10, 40); y = 2 + 0.8 * x + rng.normal(0, 1.5, 40)
fig, ax = plt.subplots(figsize=(7, 5.5))
sns.regplot(x=x, y=y, color=BLUE, line_kws=dict(color=ORANGE, lw=2.5), ax=ax)
b1, b0 = np.polyfit(x, y, 1)
if ANNOTATE: ax.plot([4, 6, 6], [b0 + b1 * 4] * 2 + [b0 + b1 * 6], color="black", lw=2.5, zorder=5)
note(ax, f"slope ≈ {b1:.1f}:\ny rises {b1:.1f} per unit of x", (6, b0 + b1 * 5), (6.8, 2.5))
note(ax, f"intercept ≈ {b0:.1f}\n(y when x = 0)", (0, b0), (0.3, 7.5))
k = np.argmax(np.abs(y - (b0 + b1 * x)))
if ANNOTATE: ax.plot([x[k]] * 2, [y[k], b0 + b1 * x[k]], color=GREY, ls=":", lw=2)
note(ax, "residual", (x[k], (y[k] + b0 + b1 * x[k]) / 2), (x[k] + 1.2, y[k] - 4.5) if y[k] > b0 + b1 * x[k] else (x[k] + 1.2, y[k] + 4))
note(ax, "band = uncertainty\nabout the line", (9.6, b0 + b1 * 9.6 + 0.6), (7.5, 14))
ax.set(xlabel="Predictor (x)", ylabel="Outcome (y)", xlim=(-0.3, 10.3), ylim=(-1, 16))
save(fig, "lm")

# 5. logistic regression ---------------------------------------------------
x = rng.uniform(0, 10, 80)
p = 1 / (1 + np.exp(-(x - 5) * 1.1)); y = rng.binomial(1, p)
fig, ax = plt.subplots(figsize=(7, 5.5))
sns.regplot(x=x, y=y, logistic=True, color=BLUE, y_jitter=0.03,
            line_kws=dict(color=ORANGE, lw=2.5), scatter_kws=dict(alpha=0.6), ax=ax)
ax.axhline(0.5, color=GREY, ls="--", lw=1)
note(ax, "data are 0 or 1", (2, 0.02), (0.2, 0.25))
note(ax, "curve = predicted\nprobability of a 1", (6.5, 0.85), (6.8, 0.45))
note(ax, "50% point", (5, 0.5), (1.2, 0.65))
note(ax, "steeper S\n= stronger effect", (5.6, 0.68), (2.3, 0.9))
ax.set(xlabel="Word frequency (log)", ylabel="P(correct)", ylim=(-0.08, 1.1))
save(fig, "logit")

# 7. logistic regression, categorical predictors --------------------------
r3 = np.random.default_rng(3)
def trials(p, subj, n_trials=20):
    """0/1 responses: each participant gets their own p around the cell p."""
    rows = []
    for s in range(subj):
        ps = 1 / (1 + np.exp(-(np.log(p / (1 - p)) + r3.normal(0, 0.5))))
        rows += [(s, r) for r in r3.binomial(1, ps, n_trials)]
    return rows

# (a) one factor, three levels
rows = []
for cond, p in [("Easy", 0.9), ("Medium", 0.75), ("Hard", 0.5)]:
    rows += [(cond, f"{cond}{s}", r) for s, r in trials(p, 15)]
d = pd.DataFrame(rows, columns=["difficulty", "subject", "correct"])
subj = d.groupby(["difficulty", "subject"], sort=False).correct.mean().reset_index()
fig, ax = plt.subplots(figsize=(6, 5.5))
sns.stripplot(subj, x="difficulty", y="correct", color=GREY, size=6, jitter=0.12, alpha=0.8, ax=ax)
sns.pointplot(d, x="difficulty", y="correct", color=ORANGE, errorbar=("ci", 95), markers="D",
              linestyles="none", ax=ax)
ax.set(xlabel="Task difficulty", ylabel="P(correct)", ylim=(0, 1.02))
save(fig, "logit_cat1")

# (b) two factors, 2 x 2
rows = []
for (task, grp), p in {("Easy", "Native"): 0.95, ("Hard", "Native"): 0.85,
                       ("Easy", "L2"): 0.85, ("Hard", "L2"): 0.55}.items():
    rows += [(task, grp, r) for _, r in trials(p, 15)]
d = pd.DataFrame(rows, columns=["task", "group", "correct"])
fig, ax = plt.subplots(figsize=(6, 5.5))
sns.pointplot(d, x="task", y="correct", hue="group", palette=[TEAL, ORANGE],
              errorbar=("ci", 95), markers=["o", "s"], dodge=0.1, ax=ax)
ax.set(xlabel="Task difficulty", ylabel="P(correct)", ylim=(0, 1.02))
ax.legend(title="Group", frameon=False, loc="lower left")
save(fig, "logit_cat2")
