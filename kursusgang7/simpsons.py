from numpy import log, cos, sin, tan, sqrt, zeros, linspace, sum, pi
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
    I = zeros(m)
    for i in range(m):
        hi = xi[i+1]-xi[i]
        ci = (xi[i+1]+xi[i])/2
        I[i] = (hi / 6) * (f(x[i]) + 4*f(ci) + f(x[i+1]))
    return sum(I)

# Test midpoint
if __name__ == "__main__":
    a = 0
    b = 1
    # Opgave 1
    # f = lambda x: cos(x)
    # f = lambda x: sqrt(x)
    # f = lambda x: log(x) if (x != 0) else 0
    # Opgave 2
    # f = lambda x: sqrt(1 + (3 * x**2)**2)
    # f = lambda x: sqrt(1 + (1 + tan(x)**2)**2)
    # f = lambda x: sqrt(1 + (1/(x**2 + 1))**2)
    i = 1
    x = linspace(a, b, i)
    I = midpoint
    for n in [2, 4, 8, 16]:
        x = linspace(a, b, n)
        I = midpoint(x, f)
        print(f"N: {n}, intergal: {I}")
