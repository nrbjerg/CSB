from simpsons import simpsons
from midpoint import midpoint
from trapezoid import trapezoid
from function import exactValue, f
import matplotlib.pyplot as plt
import numpy as np

errors = {"n": [], "simpsons": [], "midpoint": [], "trapezoid": []}

for i in range(2, 14):
    n = 2**i
    print(n)
    x = np.linspace(0, 3, n)
    
    errors["n"].append(n)
    errors["simpsons"].append(abs(simpsons(x, f) - exactValue))
    errors["midpoint"].append(abs(midpoint(x, f) - exactValue))
    errors["trapezoid"].append(abs(trapezoid(x, f) - exactValue))
    
# plot
plt.style.use("ggplot")

plt.xscale("log")
plt.yscale("log")

plt.plot(errors["n"], errors["simpsons"], color = "blue")
plt.plot(errors["n"], errors["midpoint"], color = "red")
plt.plot(errors["n"], errors["trapezoid"], color = "green")

plt.legend(["simpsons", "midpoint", "trapezoid"])
plt.show()