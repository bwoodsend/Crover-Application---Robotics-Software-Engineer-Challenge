Encoders
--------

We'll start by looking at using the encoders exclusively.
These provide a series of velocities (both angular and linear) which, if
integrated with respect to time, should yield an approximation of the car's
absolute position and orientation.

Because the linear velocities are taken from the car's orientation rather than
a fixed *world* orientation, they will have to be rotated.
This will require the absolute orientation.
So the series of calculations will have to be in the following order:

*   Integrate the angular velocities to get absolute orientations.
*   Rotate the car's linear velocities by the absolute orientations.
*   Integrate the resultant *world* linear velocities to get absolute positions.

And the results.
Note in both cases, the initial position and orientation is assumed to be
correct.

.. plot::

    from encoder_plots import positional
    positional()


.. plot::

    from encoder_plots import orientation
    orientation()


.. plot::

    from encoder_plots import orientation_difference
    orientation_difference()


The estimated position and orientation follows the same shape well but a
*drifting* error can be seen to be gradually accumulating.
On their own, the encoders perform well in the short term but get progressively
less accurate over time.
