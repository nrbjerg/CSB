"""
This module defines the `midsum` function used in
'ex_all_three_rules.py' to re-create Example 6 from page 137 in Guide²
Scientific Computing, 2nd edition.

"""

import numpy as np

def midsum(fcn, a, b, N):
    """
    Computes the midpoint rule for the integral of the function `fcn`
    over [a, b] using N subdivisions.

    """

    h = (b - a) / N
    s = fcn(a + h / 2)
    for k in range(1, N):
        s += fcn(a + (k + 1 / 2) * h)
    return s * h