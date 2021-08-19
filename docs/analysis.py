from pathlib import Path

import numpy as np
from matplotlib import pylab

DATA = Path(__file__, "../../data").resolve()

odom = np.loadtxt(DATA / "odom.csv", skiprows=1, delimiter=",")
gnss = np.loadtxt(DATA / "gnss.csv", skiprows=1, delimiter=",")
ground_truth = np.loadtxt(DATA / "ground_truth.csv", skiprows=1, delimiter=",")

# Convert the quaternion orientation to a regular angle.
# https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles#Quaternion_to_Euler_angles_conversion
q3, q0 = ground_truth[:, [5, 6]].T
ground_truth_orientations = np.arctan2(2 * (q0 * q3 + 0), 1 - 2 * (0 + q3**2))


def path(positions, orientations, label="", color=""):
    """Plot a series of positions."""
    # Draw the path.
    pylab.plot(*positions.T, linewidth=.5, label=label, c=color)

    # Mark the start and end of the path with an arrow.
    ends = positions[[0, -1]]
    end_orientations = orientations[[0, -1]]
    pylab.quiver(*ends.T, np.cos(end_orientations), np.sin(end_orientations),
                 color=color, scale=.4, units="xy")


def orientation_plot(times, thetas, label="", color=""):
    """Plot a series of angles against time."""

    # Modulo angles into the range 0 to 2π...
    thetas = thetas % (2 * np.pi)
    # ...but split the plots so that there is no vertical line every time we
    # jump from 2π to 0 or vice-versa.
    break_at = np.nonzero(np.abs(np.diff(thetas)) > np.pi)[0]
    start = 0
    for end in break_at:
        pylab.plot(times[start:end], thetas[start:end], c=color)
        start = end + 1
    pylab.plot(times[start:], thetas[start:], label=label, c=color)
