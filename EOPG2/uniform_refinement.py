from numpy import sin, cos, log, array, linspace, append
import matplotlib.pyplot as plt
from trapezoid import trapezoid
from midpoint import midpoint

def uniform_refinement(f, a, b, F):
    # Run quadratures on uniform subdivisions and see how the error behaves
    h = array([])
    err = array([])
    for i in range(10):
        m  = 2**i # number of subintervals
        xi = linspace(a, b, m+1) # endpoints of the intervals
        #I, E = trapezoid(xi, f, F)
        I, E = midpoint(xi, f, F) # Dosnt work with the current version (It needs to return the error aswell)
        h   = append(h, xi[1]-xi[0])
        err = append(err, sum(E))
    # plot the error behaviour vs expected h^2
    plt.figure(0)
    plt.clf()
    fs = 24
    plt.loglog(h, err, '-x', h, h**2,'-',lw=3,markersize=10)
    plt.xlabel('h',fontsize=fs)
    plt.ylabel('error',fontsize=fs)
    plt.legend(['Numerical error', 'h^2'],loc=4)
    plt.grid(True)
    plt.draw()
    # plot the error distribution for the last subdivision
    plt.figure(1)
    plt.clf()
    plt.plot(0.5*(xi[0:-1]+xi[1:]), h[-1]/(b-a)*E,'-x',lw=2,markersize=10)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel('x',fontsize=fs)
    plt.ylabel('error',fontsize=fs)
    plt.grid(True)
    plt.draw()

    plt.show()
    return sum(I), m

# Test function uniform_refinement
if __name__ == "__main__":
    a = 0.
    b = 1.

    # test 1
    f = lambda x: cos(x)
    F = lambda x: sin(x)
    # test 2
    #f = lambda x: sqrt(x)
    #F = lambda x: x*sqrt(x)*2./3.
    # test 3
    f = lambda x: log(x)
    F = lambda x: log(x)*x - x if x>0 else 0
    #
    I = uniform_refinement(f, a, b, F)
