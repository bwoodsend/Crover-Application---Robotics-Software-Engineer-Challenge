GNSS
----

The output of the GNSS doesn't require any calculation to use so here it is
as-is.

.. plot::

    from gnss_plots import show_smoothened
    show_smoothened(0)

Clearly, the output is very noisy.
The sample rate is much higher than we'd usually need so we can
cut through at least some of the noise by taking *rolling* averages.
To do this, redefine each GNSS point as the mean of it and *a few* of the
preceding points,
where the value of *a few* is a parameter we can experiment with.

.. plot::

    from gnss_plots import show_smoothened
    show_smoothened(10)


With the above smoothing, the noise is improved.
Whilst this car still wouldn't last long in a busy car park,
it's at least now visible that the estimated path does indeed follow the true
path  -- it's a loose fit but without the incremental errors the encoders faced.
Let's keep increase the smoothing factor.

.. plot::

    from gnss_plots import show_smoothened
    show_smoothened(25)

Whilst this GNSS path *looks* satisfyingly smoother, its overall error is
higher.
This is because a side effect of these long-rolling averages is an inertia that
makes the estimated path appear to cut or at least be lethargic whilst taking
corners.

In summary, a short rolling average of GNSS readings can be used to track the
car's long-term position but for short maneuvers, it would be less suitable.


.. note::

    This approach assumes that GNSS readings will come in in reasonable
    consistent intervals.
    Should it be long periods between readings then this rolling average must be
    adapted to recognise and discard old data.
