"""Turn a shapeless point cloud into a wug without changing its summary statistics.

Same method as the Datasaurus Dozen (Matejka & Fitzmaurice, 2017): simulated
annealing. Each step nudges one random point; the move is kept only if
mean x, mean y, SD x, SD y and Pearson r are unchanged to 2 decimals, and
(usually) only if it brings the point closer to the target shape.

Usage:  python wug_datasaurus.py [--iters 400000] [--seed 1] [--frames]
Writes images/wug_datasaurus.png (start vs. wug), data/wug.csv, and with
--frames a series of PNGs in wug_frames/ for an animation.
"""
import argparse, os
import numpy as np
import matplotlib.pyplot as plt

TEAL, ORANGE, BLUE, GREY = "#4C827B", "#CD5909", "#1e66f5", "#9ca0b0"


# --- target shape: a wug (Berko, 1958), as line segments on a 0-100 grid ----
def arc(cx, cy, rx, ry, a0=0, a1=360, n=200):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[cx + rx * np.cos(t), cy + ry * np.sin(t)]

def seg(x0, y0, x1, y1, n=40):
    return np.c_[np.linspace(x0, x1, n), np.linspace(y0, y1, n)]

def wug_outline():
    parts = [
        arc(45, 42, 30, 24, 0, 360, 260),          # body
        arc(70, 66, 15, 14, -40, 200, 160),        # head (open where it meets the body)
        arc(74, 70, 1.2, 1.2, 0, 360, 12),         # eye (small, or it swallows points)
        seg(84, 70, 95, 66), seg(95, 66, 84, 61),  # beak
        seg(38, 18, 36, 6), seg(30, 6, 42, 6),     # left leg + foot
        seg(54, 18, 56, 6), seg(50, 6, 62, 6),     # right leg + foot
        seg(66, 80, 62, 92), seg(70, 80, 70, 93), seg(74, 79, 79, 90),  # tuft
        arc(20, 52, 7, 12, 90, 270, 60),           # tail bump
    ]
    return np.vstack(parts)


# --- statistics that must not change ---------------------------------------
def stats(x, y):
    return np.round([x.mean(), y.mean(), x.std(ddof=1), y.std(ddof=1),
                     np.corrcoef(x, y)[0, 1]], 2)

def dist_to_shape(px, py, shape):
    return np.sqrt(((shape - (px, py)) ** 2).sum(1)).min()


def anneal(x, y, shape, iters, rng, frames_every=0):
    target = stats(x, y)
    temp_max, temp_min = 0.4, 0.01
    frames = []
    for i in range(iters):
        temp = temp_max - (temp_max - temp_min) * i / iters   # linear cooling
        k = rng.integers(len(x))
        nx, ny = x[k] + rng.normal(0, 0.6), y[k] + rng.normal(0, 0.6)
        old_d = dist_to_shape(x[k], y[k], shape)
        new_d = dist_to_shape(nx, ny, shape)
        if new_d < old_d or rng.random() < temp:              # occasional uphill move
            ox, oy = x[k], y[k]
            x[k], y[k] = nx, ny
            if not np.array_equal(stats(x, y), target):       # stats changed: undo
                x[k], y[k] = ox, oy
        if frames_every and i % frames_every == 0:
            frames.append((x.copy(), y.copy()))
    return x, y, frames


def panel(ax, x, y, title):
    s = stats(x, y)
    ax.scatter(x, y, s=14, color=BLUE, alpha=0.8)
    ax.set(xlim=(-5, 105), ylim=(-5, 105), aspect="equal", xticks=[], yticks=[], title=title)
    ax.set_xlabel(f"mean x = {s[0]:.2f}   mean y = {s[1]:.2f}\nSD x = {s[2]:.2f}   SD y = {s[3]:.2f}   r = {s[4]:.2f}",
                  fontsize=10, family="monospace", color="#4c4f69")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iters", type=int, default=1_000_000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=180)
    ap.add_argument("--frames", action="store_true")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    shape = wug_outline()
    # start: a shapeless Gaussian cloud whose means, SDs and r match the wug
    # exactly (so the wug is reachable without changing the statistics)
    w = shape[np.linspace(0, len(shape) - 1, a.n).astype(int)]
    cov = np.cov(w.T)
    z = rng.normal(size=(a.n, 2))
    z -= z.mean(0)
    z = z @ np.linalg.inv(np.linalg.cholesky(np.cov(z.T))).T   # whiten exactly
    xy = z @ np.linalg.cholesky(cov).T + w.mean(0)
    x0, y0 = xy[:, 0], xy[:, 1]
    x, y, frames = anneal(x0.copy(), y0.copy(), shape, a.iters, rng,
                          frames_every=a.iters // 60 if a.frames else 0)

    plt.rcParams["font.family"] = "Georgia"
    fig, axes = plt.subplots(1, 2, figsize=(10, 5.6))
    panel(axes[0], x0, y0, "Start")
    panel(axes[1], x, y, "Wug")
    fig.tight_layout()
    os.makedirs("images", exist_ok=True)
    fig.savefig("images/wug_datasaurus.png", dpi=150)

    os.makedirs("data", exist_ok=True)
    np.savetxt("data/wug.csv", np.c_[x, y], delimiter=",", header="x,y", comments="", fmt="%.4f")

    if frames:
        os.makedirs("wug_frames", exist_ok=True)
        for j, (fx, fy) in enumerate(frames + [(x, y)]):
            f, ax = plt.subplots(figsize=(5, 5.6))
            panel(ax, fx, fy, "")
            f.tight_layout(); f.savefig(f"wug_frames/{j:03d}.png", dpi=100); plt.close(f)

    print("start:", stats(x0, y0), " wug:", stats(x, y))


if __name__ == "__main__":
    main()
