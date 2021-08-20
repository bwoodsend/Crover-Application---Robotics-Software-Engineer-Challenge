"""Analyse and plot the performance of the pure encodings approach."""
import numpy as np
import pylab

from crover_challenge.encoders import EncoderToOdometry
from analysis import *

linear = odom[:, [1, 2]]
angular = odom[:, 3]
times = odom[:, 0] / 1e9


encoder_to_odometry = EncoderToOdometry(ground_truth[0, [1, 2]],
                                        ground_truth[0, 5])
# Simulate a realtime application by feeding readings in individually. Log each
# estimated position and orientation.
positions = np.empty((len(times), 2))
orientations = np.empty(times.shape)
for (i, time) in enumerate(times):
    positions[i], orientations[i] = \
        encoder_to_odometry.new_reading(time, linear[i], angular[i])


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
    orientation_plot(times, orientations, label="encoders", color="r")
    orientation_plot(ground_truth[:, 0] / 1e9, ground_truth_orientations,
                     label="Ground Truth", color="c")
    pylab.legend()
    pylab.ylabel("Orientation $z$")
    pylab.xlabel("Time (seconds)")
    pylab.show()
