from numpy import log, cos, sin, tan, sqrt, zeros, linspace, sum, pi
from function import f, exactValue

def simpsons(xi,f):
    """
    Use simpsons quadrature based on the subdivision xi

    Input:
    xi: location of nodes, defining the subdivision of the interval
    (including the endpoints)
    f:  function to integrate

    Output:

    I = the numerical approximation to the integral on each subinterval
    """
    m = len(xi)-1
    I = zeros(m)
    for i in range(m):
        hi = xi[i+1]-xi[i]
        ci = (xi[i+1]+xi[i])/2
        I[i] = (hi / 6) * (f(xi[i]) + 4*f(ci) + f(xi[i+1]))
    return I

# Test midpoint
if __name__ == "__main__":
    a = 0
    b = 3
    i = 3
    x = linspace(a, b, i)
    I = simpsons(x, f)
    while (abs(I - exactValue) >= 10E-8):
        i += 1
        x = linspace(a, b, i)
        I = simpsons(x, f)
    
    print(f"Number of points {i}")