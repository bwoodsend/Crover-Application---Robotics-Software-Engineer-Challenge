Methods
=======

A roadmap of the code, pointing to where the key calculations take place.

* Interpolating the timestamps is necessary to meaningfully compare positions
  and orientations derived at different times. In most cases, ``numpy.interp()``
  can be used directly. For positions (which are multidimensional), a small
  ``crover_challenge.core.interpolate_points()`` wrapper is used.

* A *rolling average* (``crover_challenge.gnss.RollingMean()``) is used to
  efficiently reduce the noisy output of the GNSS sensor. This is loosely
  inspired by digital low-pass filters used in digital audio processing.

* Integration is needed to convert angular velocities to orientations
  and linear velocities to positions. For this I use the `Trapezoidal Rule`_,
  (``crover_challenge.encoders.CumulativeIntegral()``) but modified slightly to
  give a *total so far* for each input value rather than only a final total
  position/orientation.

* Quaternions are new to me. I opted to convert the quaternions in the CSV files
  straight to angles and then to rotation matrices with which I am more
  familiar. These conversions are done by
  ``crover_challenge.core.quaternion_z_angle()`` and
  ``crover_challenge.core.rotate()`` respectively. In the long run, it would be
  good to learn how to use quaternions directly.

* To assess accuracy, I use a simple mean of each distance between real and
  estimated positions where the real positions must first be interpolated to
  normalise the mismatch in timestamps used by the sensors and the ground truth
  table. This metric is defined in ``writeup/analysis.position_error()``.


.. _`Trapezoidal Rule`: https://en.wikipedia.org/wiki/Trapezoidal_rule
