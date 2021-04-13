"""
This module defines the `romberg` function from page 145 in Guide²
Scientific Computing, 2nd edition.

"""

import numpy as np
from prg_midpoint import midsum

def romberg(fcn, a, b, epsilon: float = 0.00001):
    """
    Romberg integration based on the midpoint rule `ML` is the
    maximum level of the array. Output here is the full Romberg
    array.

    """

    N = 1
    # Generere de første to lag:
    R = [[(b - a) * (fcn(a) + fcn(b)) / 2], [0, 0]]
    M = midsum(fcn, a, b, N) # Ny midtpunkts intergration
    R[1][0] = (R[1 - 1][0] + M) / 2 # Den første indgang definieres på bagrund af indgangen over samt den nye midtpunkts intergration
    for k in range(1):
        R[1][k + 1] = ((4**(k + 1) * R[1][k] - R[1 - 1][k]) /
                        (4**(k + 1) - 1))
        N *= 2
    
    depth = 1
        
    while (abs(R[-2][-1] - R[-1][-1]) >= epsilon):
        depth += 1
        R.append([])
        M = midsum(fcn, a, b, N)
        R[depth].append((R[depth - 1][0] + M) / 2)
        for k in range(depth):
            R[depth].append(((4**(k + 1) * R[depth][k] - R[depth - 1][k]) /
                           (4**(k + 1) - 1)))
        N *= 2
    
    return R

if (__name__ == "__main__"):
    print(romberg(lambda x: 1 / (x + 2), -1, 1))