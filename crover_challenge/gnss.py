import collections


class RollingMean:
    """Take a continuous average of a series of values. Each output value is
    defined as the average of the last ``n`` input values.

    For the first ``n - 1`` values, the output will be an average of less
    values.
    """
    def __init__(self, n=10):
        self.n = n
        self._recent = collections.deque(maxlen=n)
        self._recent_total = 0

    def new_value(self, x):
        """Add a new reading, return the current average."""
        if self.n == 0:
            return x

        # To avoid having to repeatedly sum ``self._recent``, its total is
        # instead tracked separately - incrementing it for each new value in and
        # decrementing it for each old value dropped.y
        if len(self._recent) == self.n:
            self._recent_total -= self._recent[0]
        self._recent_total += x
        self._recent.append(x)

        return self.current

    @property
    def current(self):
        """The current average of the last ``n`` values."""
        return self._recent_total / len(self._recent)
