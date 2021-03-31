import numpy as np
import matplotlib.pyplot as plt
from prg_romberg import romberg

a = 0
b = 1

h = abs(a - b)

# Case 1
#f = lambda x : np.cos(x)
#F = lambda x : np.sin(x)

# Case 2
f = lambda x: np.sqrt(x)
F = lambda x: 2/3 * x**1.5

ML = 6
Q_rmb = romberg(f, a, b, ML)
I = F(b)-F(a)
err_romb = np.abs(np.diag(Q_rmb)-I)/np.abs(I)
err_tpz  = np.abs(Q_rmb[:,0]-I)/np.abs(I)

lengths = np.array([h / (2**(n - 1)) for n in range(ML)])

plt.xscale("log")

plt.semilogy(lengths, err_tpz,label='Trapez')
plt.semilogy(lengths, err_romb,label='Romberg')
plt.legend(["Trapez", "Romberg"])
plt.grid(True)
plt.show()
