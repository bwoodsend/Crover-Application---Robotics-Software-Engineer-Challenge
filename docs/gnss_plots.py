import numpy as np
import pylab

from crover_challenge.gnss import rolling_mean
from crover_challenge.core import interpolate_points, reduce
from analysis import *


def show_smoothened(n):
    """Calculate, plot and evaluate the effect of rolling average smoothing on
    GNSS data.
    """
    points = rolling_mean(gnss[:, [1, 2]], n)

    # Resample the "truth" points so that they use the same times as the
    # smoothened GNSS points.
    times = gnss[n:, 0]
    truth_points = interpolate_points(times, ground_truth[:, 0],
                                      ground_truth[:, [1, 2]])
    # Get an overall deviation error.
    error = np.hypot(*(points - truth_points).T).mean()

    if n:
        pylab.title(
            f'GNSS position, "last {n}" rolling average. '
            f'Mean error: {error:.3f}')
        path(points, color="r", label="GNSS")
    else:
        pylab.title(f"Raw GNSS position vs real position. "
                    f"Mean error: {error:.3f}")
        path(points, color="r", label="GNSS")
    path(ground_truth[:, [1, 2]], label="Ground Truth", color="c")

    pylab.legend()
    pylab.xlabel("$x$")
    pylab.ylabel("$y$")

    pylab.show()
