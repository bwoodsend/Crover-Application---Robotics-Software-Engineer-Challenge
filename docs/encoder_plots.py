"""Analyse and plot the performance of the pure encodings approach."""

import pylab

from crover_challenge.encoders import velocities_to_odometry
from analysis import *

linear = odom[:, [1, 2]]
angular = odom[:, 3]
times = odom[:, 0] / 1e9

positions, orientations = velocities_to_odometry(
    times, linear, angular, ground_truth[0, [1, 2]], ground_truth[0, 5]
)


def positional():
    pylab.title("Estimated and Real Positions of the Car")
    path(positions, orientations, "encoders", color="r")
    path(ground_truth[:, [1, 2]], ground_truth_orientations,
         label="ground truth", color="c")
    pylab.legend()
    pylab.xlabel("$x$")
    pylab.ylabel("$y$")
    pylab.show()


def orientation():
    pylab.title("Estimated and Real Orientations of the Car")
    orientation_plot(times[:-1], orientations, label="encoders", color="r")
    orientation_plot(ground_truth[:, 0] / 1e9, ground_truth_orientations,
                     label="Ground Truth", color="c")
    pylab.legend()
    pylab.ylabel("Orientation $z$")
    pylab.xlabel("Time (seconds)")
    pylab.show()
