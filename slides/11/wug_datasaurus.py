"""Turn a shapeless point cloud into a wug without changing its summary statistics.

Same method as the Datasaurus Dozen (Matejka & Fitzmaurice, 2017): simulated
annealing. Each step nudges one random point; the move is kept only if
mean x, mean y, SD x, SD y and Pearson r are unchanged to 2 decimals, and
(usually) only if it brings the point closer to the target shape.

The target shape is the black ink of a line drawing (default images/Wug.png):
every dark pixel becomes a target point on a 0-100 grid.

Usage:  python wug_datasaurus.py [--image images/Wug.png] [--iters 1000000]
                                 [--n 260] [--seed 1] [--frames]
Writes images/wug_datasaurus.png (start vs. wug), the same with the
regression line (images/wug_datasaurus_fit.png), data/wug.csv, and with
--frames a series of PNGs in wug_frames/ for an animation.
"""
import argparse, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.spatial import cKDTree

BLUE = "#1e66f5"


# --- target shape: dark pixels of the drawing -------------------------------
def ink_points(path, dark=200):
    """Coordinates of the dark (line) pixels, scaled to a 0-100 grid, y up."""
    im = np.asarray(Image.open(path).convert("RGBA")).astype(int)
    rgb, alpha = im[..., :3], im[..., 3]
    ys, xs = np.nonzero((rgb.sum(2) < dark) & (alpha > 0))
    h, w = alpha.shape
    scale = 100 / max(h, w)
    return np.c_[xs * scale, (h - ys) * scale]


# --- statistics that must not change ---------------------------------------
def stats(x, y):
    return np.round([x.mean(), y.mean(), x.std(ddof=1), y.std(ddof=1),
                     np.corrcoef(x, y)[0, 1]], 2)


def anneal(x, y, tree, iters, rng, frames_every=0):
    target = stats(x, y)
    temp_max, temp_min = 0.4, 0.01
    frames = []
    for i in range(iters):
        temp = temp_max - (temp_max - temp_min) * i / iters   # linear cooling
        k = rng.integers(len(x))
        nx, ny = x[k] + rng.normal(0, 0.6), y[k] + rng.normal(0, 0.6)
        old_d = tree.query((x[k], y[k]))[0]
        new_d = tree.query((nx, ny))[0]
        if new_d < old_d or rng.random() < temp:              # occasional uphill move
            ox, oy = x[k], y[k]
            x[k], y[k] = nx, ny
            if not np.array_equal(stats(x, y), target):       # stats changed: undo
                x[k], y[k] = ox, oy
        if frames_every and i % frames_every == 0:
            frames.append((x.copy(), y.copy()))
    return x, y, frames


def panel(ax, x, y, title, fit=False):
    s = stats(x, y)
    ax.scatter(x, y, s=14, color=BLUE, alpha=0.8)
    if fit:                                       # least-squares line
        b, a = np.polyfit(x, y, 1)
        ax.plot([-5, 105], [a - 5 * b, a + 105 * b], color="#CD5909", lw=2.5)
    ax.set(xlim=(-5, 105), ylim=(-5, 105), aspect="equal", xticks=[], yticks=[], title=title)
    ax.set_xlabel(f"mean x = {s[0]:.2f}   mean y = {s[1]:.2f}\nSD x = {s[2]:.2f}   SD y = {s[3]:.2f}   r = {s[4]:.2f}",
                  fontsize=10, family="monospace", color="#4c4f69")
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", default="images/Wug.png")
    ap.add_argument("--iters", type=int, default=1_000_000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--n", type=int, default=260)
    ap.add_argument("--frames", action="store_true")
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    shape = ink_points(a.image)
    tree = cKDTree(shape)

    # start: a shapeless Gaussian cloud whose means, SDs and r match the
    # drawing exactly (so the wug is reachable without changing the statistics)
    w = shape[rng.choice(len(shape), a.n, replace=False)]
    cov = np.cov(w.T)
    z = rng.normal(size=(a.n, 2))
    z -= z.mean(0)
    z = z @ np.linalg.inv(np.linalg.cholesky(np.cov(z.T))).T   # whiten exactly
    xy = z @ np.linalg.cholesky(cov).T + w.mean(0)
    x0, y0 = xy[:, 0], xy[:, 1]

    x, y, frames = anneal(x0.copy(), y0.copy(), tree, a.iters, rng,
                          frames_every=a.iters // 60 if a.frames else 0)

    plt.rcParams["font.family"] = "Georgia"
    os.makedirs("images", exist_ok=True)
    for fit, out in [(False, "images/wug_datasaurus.png"), (True, "images/wug_datasaurus_fit.png")]:
        fig, axes = plt.subplots(1, 2, figsize=(10, 5.6))
        panel(axes[0], x0, y0, "Start", fit)
        panel(axes[1], x, y, "Wug", fit)
        fig.tight_layout()
        fig.savefig(out, dpi=150)
        plt.close(fig)

    os.makedirs("data", exist_ok=True)
    np.savetxt("data/wug.csv", np.c_[x, y], delimiter=",", header="x,y", comments="", fmt="%.4f")

    if frames:
        os.makedirs("wug_frames", exist_ok=True)
        for j, (fx, fy) in enumerate(frames + [(x, y)]):
            f, ax = plt.subplots(figsize=(5, 5.6))
            panel(ax, fx, fy, "")
            f.tight_layout(); f.savefig(f"wug_frames/{j:03d}.png", dpi=100); plt.close(f)

    print(f"{len(shape)} target pixels | start:", stats(x0, y0), " wug:", stats(x, y))


if __name__ == "__main__":
    main()
