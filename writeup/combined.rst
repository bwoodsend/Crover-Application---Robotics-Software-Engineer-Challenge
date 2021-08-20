Combining GNSS with the Encoders?
---------------------------------

The encoders give a good short-term approximation of the car's position but
become progressively less accurate with time.
The GNSS sensor does the opposite - it's output is noisy in the short-term but
stays on course long-term.
Can we use the GNSS estimates to correct the drifts in the encoder's estimates
and thus get a best of both worlds?

I've briefly tried a few approaches at doing this but none of them have worked
and I've ran out of time.
The biggest obstacle was countering drift in rotation as the GNSS does not
provide an approximate absolute rotation and small uncertainties in orientation
propagate to large errors in the encoder's estimated position.

My most promising looking idea was to take the most recent approximate positions
from the encoders and GNSS (interpolating one of them so that the timestamps
match), finding the best fit transform which would map encoder points to GNSS's
(which I have done before in AutoIDD_) then applying that transform to the
encoder's approximate positions and orientations.

.. _AutoIDD: https://pubmed.ncbi.nlm.nih.gov/32169756/

