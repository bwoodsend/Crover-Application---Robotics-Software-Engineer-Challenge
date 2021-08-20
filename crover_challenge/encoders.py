import numpy as np

from crover_challenge.core import rotate


class CumulativeIntegral:
    """Numerically integrate y with respect to x from x=0 to x=x for all values
    of x.
    """
    def __init__(self, initial):
        self.integral = initial
        self._last_x = 0
        self._last_y = None

    def new_reading(self, x, y):
        """Supply a new value of x and y to include in the integral."""
        if self._last_y is None:
            self._last_y = y

        # This is just the trapezium rule for numerical integration.
        trapezium_area = (x - self._last_x) * (y + self._last_y) / 2
        self._last_y = y
        self._last_x = x
        self.integral += trapezium_area
        return self.integral


class EncoderToOdometry:
    """Analyse sequences of times, linear and angular velocities and calculate
    and estimate the absolute position and orientation.
    """
    def __init__(self, initial_position=(0, 0), initial_orientation=0):
        self._position = CumulativeIntegral(np.asarray(initial_position))
        self._orientation = CumulativeIntegral(initial_orientation)

    def new_reading(self, time, linear, angular):
        """Supply a new linear and angular velocity."""
        self._orientation.new_reading(time, angular)
        velocity = rotate(linear, self._orientation.integral)
        self._position.new_reading(time, velocity)
        return self._position.integral, self._orientation.integral

    @property
    def position(self):
        """The current absolute position."""
        return self._position.integral

    @property
    def orientation(self):
        """The current absolute orientation."""
        return self._orientation.integral
