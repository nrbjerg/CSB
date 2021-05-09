from customMidpoint import midpoint
from trapezoid import trapezoid
from simpsons import simpsons
from function import f, exactValue
import numpy as np

m, t, s = [], [], []
n = 12
ns = [2**i for i in range(n)]

for i in range(n):
    xi = np.linspace(0, 3, 2**i)
    
    m.append(abs(midpoint(xi, f) - exactValue))
    t.append(abs(trapezoid(xi, f) - exactValue))
    s.append(abs(simpsons(xi, f) - exactValue))
    
import matplotlib.pyplot as plt 

plt.style.use("ggplot")

plt.loglog(ns, m)
plt.loglog(ns, t)
plt.loglog(ns, s, c = "tab:green")

plt.legend(["midpoint", "trapezoid", "simpsons"])
plt.xlabel("M (Number of intervals)")
plt.ylabel("Numerical error")
plt.show()