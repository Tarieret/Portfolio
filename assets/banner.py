# Import & Load
# Generates assets/img/banner-light.svg and banner-dark.svg: a top-down 2-D KDE drawn as a
# topographic contour map, in Monokai Pro Light / Monokai Pro colours, with some bands shaded in
# and the underlying sample points drawn faintly underneath.

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import gaussian_filter
from matplotlib.colors import LinearSegmentedColormap, to_rgb

W, H = 44.68, 7.0            # banner shape (data units)
PX = 30                      # grid cells per unit, equal in x and y so the smoothing is round
SEED = 5                     # change for a different landscape
LINE_WIDTH = 3.4
N_LEVELS = 10
SHADED_BANDS = {2, 5, 8}     # which bands between contour lines get a soft fill (0 = lowest)
SHADE_ALPHA = 0.30
N_POINTS = 1200              # faint sample points drawn under the contours (the data the KDE is built from)
POINTS = {"light": ("#918c8e", 0.55), "dark": ("#c1c0c0", 0.35)}   # colour, opacity

# Monokai Pro colours, low ground -> high ground (green, blue, purple, pink, orange, yellow)
HUES = {
    "light": ["#269d69", "#1c8ca8", "#7058be", "#e14775", "#e16032", "#cc7a0a"],   # Monokai Pro Light
    "dark":  ["#a9dc76", "#78dce8", "#ab9df2", "#ff6188", "#fc9867", "#ffd866"],   # Monokai Pro (dark theme)
}
BACKGROUNDS = {"light": "#faf4f2", "dark": "#2d2a2e"}

def muted(colour, bg, soften=0.08, desat=0.9):
    """Desaturate a colour, then blend it a little toward the page background."""
    c = np.array(to_rgb(sns.desaturate(colour, desat)))
    return tuple((1 - soften) * c + soften * np.array(to_rgb(bg)))

# ---- the data: points sampled from broad, overlapping hills, then a round-kernel KDE ----
rng = np.random.default_rng(SEED)
n_hills = 22
hills = np.column_stack([rng.uniform(-3, W + 3, n_hills), rng.uniform(-2, H + 2, n_hills)])
pts = np.vstack([rng.normal(c, rng.uniform(1.8, 3.6), (rng.integers(300, 900), 2)) for c in hills])

nx, ny = int(W * PX), int(H * PX)
hist, _, _ = np.histogram2d(pts[:, 1], pts[:, 0], bins=[ny, nx], range=[[0, H], [0, W]])
density = gaussian_filter(hist, sigma=1.1 * PX)                  # KDE = histogram * Gaussian kernel
density = (density - density.min()) / (density.max() - density.min())
gx, gy = np.meshgrid(np.linspace(0, W, nx), np.linspace(0, H, ny))
levels = np.linspace(0.08, 0.92, N_LEVELS)

for theme, bg in BACKGROUNDS.items():
    cmap = LinearSegmentedColormap.from_list(theme, [muted(h, bg) for h in HUES[theme]])
    band_colours = [cmap(i / (len(levels) - 2)) for i in range(len(levels) - 1)]
    fill_colours = [(c[0], c[1], c[2], SHADE_ALPHA) if i in SHADED_BANDS else (0, 0, 0, 0)
                    for i, c in enumerate(band_colours)]

    fig, ax = plt.subplots(figsize=(W * 0.5, H * 0.5))
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.set_aspect("equal"); ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    shown = pts[np.random.default_rng(SEED).choice(len(pts), N_POINTS, replace=False)]
    p_colour, p_alpha = POINTS[theme]
    ax.scatter(shown[:, 0], shown[:, 1], s=9, color=p_colour, alpha=p_alpha, lw=0, zorder=0)
    ax.contourf(gx, gy, density, levels=levels, colors=fill_colours)
    ax.contour(gx, gy, density, levels=levels, cmap=cmap, linewidths=LINE_WIDTH)
    fig.savefig(f"assets/img/banner-{theme}.svg", transparent=True)
    plt.close(fig)
