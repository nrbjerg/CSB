# -*- coding: utf-8 -*-

# Code for E-OPG2-2021
import math
from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Regular euler
def euler (f, t, y, h, k1): # LTE: O(h^2)
    y1 = y + h*k1
    return y1, t + h
 
# Explicit trapez
def explicitTrapez(f, t, y, h, k1): # LTE: O(h^3)
    k2 = f(t + h, y + h * k1)
    y1 = y + h/2 * (k1 + k2)
    return y1, t + h

# equation parameters
g = 9.81

# initial conditions
x10 = 0 # Position
x20 = 40 # Hastighed

# time parameters
t_start = 0.0
t_stop = 8.0

# The system 
def fun(t, x):
    return np.array([x[1], -g - c*x[1]**2*np.sign(x[1])])

cs = np.linspace(0, 0.02, num = 50)
t_max = np.zeros(len(cs))
z_max = np.zeros(len(cs))
threshHold = 0.1

def computeMaximum (N: int, c: float, algorithm) -> (float):
    t_step = (t_stop - t_start)/N # h
    X1 = np.zeros(N + 1)
    X2 = np.zeros(N + 1)

    X1[0] = x10
    X2[0] = x20

    # initialize time variable
    t = t_start

    # solve
    for k in range(N):
        k1 = fun(t, np.array([X1[k], X2[k]]))
        y, t = algorithm(fun, t, np.array([X1[k], X2[k]]), t_step, k1)
        X1[k+1] = y[0] # Gem position
        X2[k+1] = y[1] # Gem hastighed
    
    index = np.where(X1 == np.amax(X1))[0][0]
    return (t + t_step * index, X1[index])

for idx, c in tqdm(enumerate(cs), unit = " simulation paremeters"):
    N = 12
    
    difference = np.inf
    while difference > threshHold:
        t_step = (t_stop - t_start)/N # h
        
        X1 = np.zeros(N + 1)
        X2 = np.zeros(N + 1)

        X1[0] = x10
        X2[0] = x20

        # initialize time variable
        t = t_start

        # compute difference
        difference = 0
        for k in range(N):
            k1 = fun(t, np.array([X1[k], X2[k]]))
            y1, _ = euler(fun, t, np.array([X1[k], X2[k]]), t_step, k1)
            y2, _ = explicitTrapez(fun, t, np.array([X1[k], X2[k]]), t_step, k1)

            # \sqrt((y1[0] - y2[0])^2 + (y1[1] - y2[1])^2)
            difference += np.linalg.norm(y1 - y2)
            
            X1[k + 1] = y1[0]
            X2[k + 1] = y1[1]
            
            t += t_step
        
        N *= 2
    
    t_max[idx], z_max[idx] = computeMaximum(N, c, explicitTrapez)
    
plt.plot(np.array(cs), t_max)
plt.plot(np.array(cs), z_max)

plt.legend(["t_max", "z_max"])
plt.xlabel("c value")
plt.grid()
plt.show()
