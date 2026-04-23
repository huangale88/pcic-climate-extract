import numpy as np

def kde_1d(x, grid, bw=None):
    """
    Simple 1D Gaussian KDE.

    Parameters
    ----------
    x : array-like
        Sample data.
    grid : array-like
        Points at which to evaluate the density.
    bw : float, optional
        Bandwidth. If None, Silverman's rule is used.

    Returns
    -------
    density : ndarray
        Estimated probability density on grid.
    """
    x = np.asarray(x)
    x = x[np.isfinite(x)]

    if bw is None:
        bw = 1.06 * x.std() * len(x) ** (-1 / 5)

    bw = max(bw, 1e-6)

    diff = grid[:, None] - x[None, :]
    density = np.exp(-0.5 * (diff / bw) ** 2).sum(axis=1)
    density /= (len(x) * bw * np.sqrt(2 * np.pi))
    return density
