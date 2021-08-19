import numpy as np

from crover_challenge.core import reduce, rotate


def cumulative_integrate(x, y):
    """Numerically integrate y with respect to x from x=0 to x=x for all values
    of x.
    """
    # This is just the trapezium rule for numerical integration.
    trapezium_areas = np.diff(x, axis=0) * reduce(y)
    return np.cumsum(trapezium_areas, axis=0)


def velocities_to_odometry(times, linear, angular,
                           initial_position=(0, 0), initial_orientation=0):
    """Analyse sequences of times, linear and angular velocities and calculate
    and estimate the absolute position and orientation.
    """

    orientations = cumulative_integrate(times, angular) + initial_orientation
    velocities = rotate(reduce(linear), orientations)
    positions = cumulative_integrate(reduce(times)[:, np.newaxis],
                                     velocities) + initial_position
    return positions, orientations
