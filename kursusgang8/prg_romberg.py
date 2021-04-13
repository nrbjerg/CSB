"""
This module defines the `romberg` function from page 145 in Guide²
Scientific Computing, 2nd edition.

"""

import numpy as np
from prg_midpoint import midsum

def romberg(fcn, a, b, ML):
    """
    Romberg integration based on the midpoint rule `ML` is the
    maximum level of the array. Output here is the full Romberg
    array.

    """

    N = 1
    R = np.zeros((ML, ML))
    R[0, 0] = (b - a) * (fcn(a) + fcn(b)) / 2
    for L in range(1,ML):
        M = midsum(fcn, a, b, N)
        R[L, 0] = (R[L - 1, 0] + M) / 2
        for k in range(L):
            R[L, k + 1] = ((4**(k + 1) * R[L, k] - R[L - 1, k]) /
                           (4**(k + 1) - 1))
        N *= 2
    return R
