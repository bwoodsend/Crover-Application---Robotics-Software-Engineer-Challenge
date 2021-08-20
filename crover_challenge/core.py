import numpy as np


def reduce(x):
    """Shrink a sequence by 1 element by interpolating between values."""
    return (x[:-1] + x[1:]) / 2


def rotate(xy, theta):
    """Apply a rotation (in radians) to a series of points."""
    assert len(xy) == len(theta)
    assert xy.ndim == 2

    rotations = np.empty((len(theta), 2, 2))
    rotations[:, 0, 0] = np.cos(theta)
    rotations[:, 0, 1] = np.sin(theta)
    rotations[:, 1, 0] = -np.sin(theta)
    rotations[:, 1, 1] = np.cos(theta)

    return (xy[:, np.newaxis] @ rotations)[:, 0]


def interpolate_points(times, times_p, values_p):
    """Resample a points+time series."""
    # This is just a multidimensional wrapper for np.interp() which is 1D only.
    return np.transpose([np.interp(times, times_p, i) for i in values_p.T])
