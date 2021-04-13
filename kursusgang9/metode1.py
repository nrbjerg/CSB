from typing import List
import numpy as np 
import math

from numpy.core import arrayprint 

def solve (y0: float, ts: List[float], f, h) -> List[float]:
    """ Implementation af løsnings metoden fra opgave 1 """
    ys = [y0]
    for i in range(0, len(ts) - 1):
        y2_3 = ys[i] + ((2 * h) / 3) * f(ts[i], ys[i]) # y[i + 2/3]
        ys.append(ys[i] + h / 4 * f(ts[i], ys[i]) + (3 * h) / 4 * f(ts[i] + (2 * h) / 3, y2_3)) # y[i + 1]

    return ys

y = lambda t: math.exp(t**3 / 3) # Analytisk løsning: y(t) = e^(t^3 / 3)
f = lambda y, t: t**2 * y # y'(t) = t^2 y(t)
y0 = 1

hs = [0.1 * 2**(-k) for k in range(0, 8)]
errors = []
for h in hs:
    ts = np.arange(0.0, 1.0, h).tolist()

    approximation = solve(y0, ts, f, h)
    errors.append(abs(approximation[-1] - y(ts[-1])))
    
# print(errors)

# Plot the results
import matplotlib.pyplot as plt 

plt.xscale("log")
plt.yscale("log")
plt.plot(hs, errors)
plt.legend(["fejl"])
plt.show()
