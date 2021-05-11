# -*- coding: utf-8 -*-

# Code for E-OPG2-2021
import numpy as np
import matplotlib.pyplot as plt

# Euler step
def euler(f, t, y, h):
    k1 = f(t, y)
    y1 = y + h*k1
    return y1, t + h

def corrected_euler(f, t, y, h):
    k1 = f(t, y)
    k2 = f(t + h/2, y + h * k1 / 2)
    y1 = y + h * k2
    return y1, t + h

def modified_euler(f ,t, y, h):
    k1 = f(t, y)
    k2 = f(t + h, y + h * k1)
    y1 = y + h/2 * (k1 + k2)
    return y1, t + h

# equation parameters
g = 9.81
c = 0
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

for e in [euler, corrected_euler, modified_euler]:
    X1 = np.zeros(N + 1)
    X2 = np.zeros(N + 1)

    X1[0] = x10
    X2[0] = x20

    # initialize time variable
    t = t_start

    # solve
    for k in range(N):
        y, t = e(fun, t, np.array([X1[k], X2[k]]), t_step)
        X1[k+1] = y[0] # Gem position
        X2[k+1] = y[1] # Gem hastighed
        
    plt.plot(T, X1)
    plt.plot(T, X2)

# Explicit 
X1 = np.zeros(N + 1)
X2 = np.zeros(N + 1)

X1[0] = x10
X2[0] = x20

# initialize time variable
t = t_start

# solve
for k in range(N):
    t += t_step
    X1[k+1] = -g * t**2 / 2 + x20 * t # Gem position
    X2[k+1] = -g * t + x20 # Gem hastighed
    
plt.plot(T, X1)
plt.plot(T, X2)

plt.legend(np.array([["z_" + e, "v_" + e] for e in ["euler", "corrected_euler", "modified_euler"] + ["z_explicit", "v_explicit"]]).flatten())
plt.grid()
plt.show()
