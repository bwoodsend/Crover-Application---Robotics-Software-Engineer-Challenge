import numpy as np


def reduce(x):
    """Shrink a sequence by 1 element by interpolating between values."""
    return (x[:-1] + x[1:]) / 2


def rotate(xy, theta):
    """Apply a rotation (in radians) to a point."""
    assert xy.shape == (2,)

    rotation = np.empty((2, 2))
    rotation[0, 0] = np.cos(theta)
    rotation[0, 1] = np.sin(theta)
    rotation[1, 0] = -np.sin(theta)
    rotation[1, 1] = np.cos(theta)

    return xy @ rotation


def interpolate_points(times, times_p, values_p):
    """Resample a points+time series."""
    # This is just a multidimensional wrapper for np.interp() which is 1D only.
    return np.transpose([np.interp(times, times_p, i) for i in values_p.T])



def quaternion_z_angle(x, y, z, w):
    """Convert the quaternion rotation about the z axis to a regular angle in
    radians."""
    # https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles#Quaternion_to_Euler_angles_conversion
    return np.arctan2(2 * (w * z + x * y), 1 - 2 * (y**2 + z**2))
