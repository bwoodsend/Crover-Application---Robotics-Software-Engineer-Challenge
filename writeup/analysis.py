from pathlib import Path

import numpy as np
from matplotlib import pylab

from crover_challenge.core import interpolate_points

DATA = Path(__file__, "../../data").resolve()

odom = np.loadtxt(DATA / "odom.csv", skiprows=1, delimiter=",")
gnss = np.loadtxt(DATA / "gnss.csv", skiprows=1, delimiter=",")
ground_truth = np.loadtxt(DATA / "ground_truth.csv", skiprows=1, delimiter=",")

# Convert the quaternion orientation to a regular angle.
# https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles#Quaternion_to_Euler_angles_conversion
q3, q0 = ground_truth[:, [5, 6]].T
ground_truth_orientations = np.arctan2(2 * (q0 * q3 + 0), 1 - 2 * (0 + q3**2))


def path(positions, orientations=None, label="", color=""):
    """Plot a series of positions."""
    # Draw the path.
    pylab.plot(*positions.T, linewidth=.5, label=label, c=color)

    # Mark the start and end of the path with an arrow.
    ends = positions[[0, -1]]
    if orientations is None:
        pylab.scatter(*ends.T, s=.4, c=color)
    else:
        end_orientations = orientations[[0, -1]]
        pylab.quiver(*ends.T,
                     np.cos(end_orientations),np.sin(end_orientations),
                     color=color, scale=.4, units="xy")


def orientation_plot(times, thetas, label="", color=""):
    """Plot a series of angles against time."""

    # Modulo angles into the range -π to π...
    thetas = (thetas + np.pi) % (2 * np.pi) - np.pi
    # ...but split the plots so that there is no vertical line every time we
    # jump from -π to π or vice-versa.
    break_at = np.nonzero(np.abs(np.diff(thetas)) > np.pi)[0]
    start = 0
    for end in break_at:
        pylab.plot(times[start:end], thetas[start:end], c=color)
        start = end + 1
    pylab.plot(times[start:], thetas[start:], label=label, c=color)


def position_error(points, times):
    """Get an overall average error for an estimated path."""
    # Resample the "truth" points so that they use the same times as the
    # smoothened GNSS points.
    truth_points = interpolate_points(times, ground_truth[:, 0],
                                      ground_truth[:, [1, 2]])
    # Get an overall deviation error.
    return np.hypot(*(points - truth_points).T).mean()
