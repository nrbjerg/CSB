import numpy as np
from function import f, exactValue

def midpoint(xi,f):
    """
    Use midpoint quadrature based on the subdivision xi

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
        ci = (xi[i+1]+xi[i])/2
        I[i] = hi * f(ci)
    return sum(I)

# Test midpoint
if __name__ == "__main__":
    a = 0
    b = 3
    i = 65536
    x = np.linspace(a, b, i)
    I = midpoint(x, f)
    while (abs(I - exactValue) <= 1.1E-10):
        i -= 4
        x = np.linspace(a, b, i)
        I = midpoint(x, f)
    
    print(f"Number of points {i}")
