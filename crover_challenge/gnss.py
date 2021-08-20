import numpy as np


def rolling_mean(x, n=10):
    """Take a continuous average of a sequence of values. Each output value is
    defined as the average of the last ``n`` input values.

    The output array is shortened by ``n`` because the first ``n`` values don't
    have enough preceding values to average over.
    """
    if not n:
        return x
    cumulated = np.cumsum(x, axis=0)
    return (cumulated[n:] - cumulated[:len(cumulated)-n]) / n
