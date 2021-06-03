import numpy as np
from function import f, exactValue

def trapezoid(xi, f, F=[]):
    """
    Use trapezoid quadrature based on the subdivision xi
    Input:
    xi: location of nodes, defining the subdivision of the interval
    (including the endpoints)
    f:  function to integrate


    Output:

    I = the numerical approximation to the integral on each subinterval

    """
    m = len(xi)-1
    I = np.zeros(m)
    for i in range(m):
        hi = xi[i+1]-xi[i]
        I[i] = hi/2*(f(xi[i])+f(xi[i+1]))
    return I

## Test Trapezoid
if __name__ == "__main__":
    a = 0
    b = 3
    i = 2
    x = np.linspace(a, b, i)
    I = trapezoid(x, f)
    while (abs(I - exactValue) >= 10E-8):
        i += 1
        x = np.linspace(a, b, i)
        I = trapezoid(x, f)
    
    print(f"Number of points {i}")
