from numpy import *
from function import f, exactValue

def midpoint(xi,f,F=[]):
    """
    Use midpoint quadrature based on the subdivision xi

    Input:
    xi: location of nodes, defining the subdivision of the interval
    (including the endpoints)
    f:  function to integrate
    F:  antiderivative (for computing errors)

    Output:

    I = the numerical approximation to the integral on each subinterval
    E = error (absolute value) on each subinterval (only if F is known)
    """
    m = len(xi)-1
    E = zeros(m)
    I = zeros(m)
    for i in range(m):
        hi = xi[i+1]-xi[i]
        ci = (xi[i+1]+xi[i])/2
        Ii_midpoint      = hi* f(ci)
        if F:
            Ii_exact     = F(xi[i+1])-F(xi[i]) # in reality we of course do not know this
            E[i]         = abs(Ii_midpoint-Ii_exact)
        I[i] = Ii_midpoint
    return I, E

# Test midpoint
if __name__ == "__main__":
    a = 0
    b = 3
    i = 2
    x = linspace(a, b, i)
    I, _ = midpoint(x, f)
    while (abs(sum(I) - exactValue) >= 10E-8):
        i += 1
        x = linspace(a, b, i)
        I, _ = midpoint(x, f)
        
    print(f"Number of points {i}")