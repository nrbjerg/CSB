# -*- coding: utf-8 -*-

# Code for E-OPG2-2021
import numpy as np
import matplotlib.pyplot as plt

# Euler step
def modified_euler(f ,t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    y1 = y + h/2 * (k1 + k2)
    return y1, t + h

# equation parameters
g = 9.81
# c = 0
# c = 0

# initial conditions
x10 = 0 # Position
x20 = 40 # Hastighed

# time parameters
t_start = 0.0
t_stop = 8.0
N = 25
t_step = (t_stop - t_start)/N # h
T = np.linspace(t_start, t_stop, N+1)

# The system 
def fun(t, x):
    return np.array([x[1], -g - c*x[1]**2*np.sign(x[1])])

cs = np.linspace(0, 0.02, num = 100)
t_max = np.zeros(len(cs))
z_max = np.zeros(len(cs))

for idx, c in enumerate(cs):
    X1 = np.zeros(N + 1)
    X2 = np.zeros(N + 1)

    X1[0] = x10
    X2[0] = x20

    # initialize time variable
    t = t_start

    # solve
    for k in range(N):
        y, t = modified_euler(fun, t, np.array([X1[k], X2[k]]), t_step)
        X1[k+1] = y[0] # Gem position
        X2[k+1] = y[1] # Gem hastighed
    
    index = np.where(X1 == np.amax(X1))[0][0]
    t_max[idx] = t + t_step * index
    z_max[idx] = X1[index]
    
plt.plot(np.array(cs), t_max)
plt.plot(np.array(cs), z_max)

plt.legend(["t_max", "z_max"])
plt.xlabel("c value")
plt.grid()
plt.show()
