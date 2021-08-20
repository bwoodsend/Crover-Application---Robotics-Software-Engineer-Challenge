import numpy as np
import pylab

from crover_challenge.gnss import RollingMean
from crover_challenge.core import interpolate_points, reduce
from analysis import *


def smoothened_path_error(n):
    """
    Calculate the mean absolute hypotenuse error of a simple rolling average smoothing on
    GNSS data.
    :param n: number of points to include in the average
    :return: mean square root error against ground truth,
             smoothed path
    """
    mean = RollingMean(n)

    # Stream the values into the rolling mean. Record the averages.
    smooth_path = np.empty((len(gnss), 2))
    for (i, xy) in enumerate(gnss[:, [1, 2]]):
        smooth_path[i] = mean.new_value(xy)

    error = position_error(smooth_path, gnss[:, 0] / 1e9)
    return error, smooth_path


def show_smoothened(n):
    """Calculate, plot and evaluate the effect of rolling average smoothing on
    GNSS data.
    """
    error, smooth_path = smoothened_path_error(n)
    if n:
        pylab.title(
            f'GNSS position, "last {n}" rolling average. '
            f'Mean error: {error:.3f}')
        path(smooth_path, color="r", label="GNSS")
    else:
        pylab.title(f"Raw GNSS position vs real position. "
                    f"Mean error: {error:.3f}")
        path(smooth_path, color="r", label="GNSS")
    path(ground_truth[:, [1, 2]], label="Ground Truth", color="c")

    pylab.legend()
    pylab.xlabel("$x$")
    pylab.ylabel("$y$")

    pylab.show()


def show_smooth_path_error():
    """ Show a chart of average error wrt window size """
    MAX_N = 50
    path_error_table = np.empty((MAX_N, 2))
    for n in range(MAX_N):
        error, _ = smoothened_path_error(n)
        path_error_table[n] = (n, error)
    pylab.title("Error wrt rolling average window size")
    pylab.plot(path_error_table[:, 0], path_error_table[:, 1])
    pylab.ylabel("Mean absolute error")
    pylab.xlabel("Window size $n$")
    pylab.show()


def show_smooth_path_error_over_time(n):
    """ Show a chart of average error of a path over time """
    _, smooth_path = smoothened_path_error(n)
    # T = number of time points
    T = len(smooth_path)
    path_error_table = np.empty((T, 1))
    for t in range(1, T):
        error = position_error(smooth_path[:t], gnss[:t, 0])
        path_error_table[t] = error
    pylab.title("Positional error over time, $n=5$")
    pylab.plot(path_error_table)
    pylab.ylabel("Mean absolute positional error")
    pylab.xlabel("Time point")
    pylab.show()


"""
from gnss_plots import show_smooth_path_error_over_time
show_smooth_path_error_over_time(5)
"""
