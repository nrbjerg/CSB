from numpy import divide, diff, append, array, union1d, where
from error_estimate import error_estimate
import matplotlib.pyplot as plt
from function import f, exactValue
from simpsons import simpsons
from trapezoid import trapezoid

def adaptive_refinement(f,a,b,tol,kvadratur):
    """
    Now let us try to figure out the optimal subdivision of the
    intervals, but using error estimation
    """
    fs = 24 # font size
    m = 1 # number of intervals
    xi = array((a,b)) # coordinates of the subdivision of [a,b], including the endpoints
    current_err = float("inf")
    M = array([])
    err = array([])
    while True:
        I, E = error_estimate(xi, f, kvadratur)
        current_err = sum(E)
        M = append(M, m)
        err = append(err, current_err)
        h = diff(xi)
        if current_err<tol:
            # success
            # plot the error distribution
            plt.figure(0)
            plt.clf()
            plt.plot(0.5*(xi[0:-1]+xi[1:]), divide(E,h*(b-a)),'-x', lw=3, markersize=10)
            plt.xlabel('x',fontsize=fs)
            plt.ylabel('error',fontsize=fs)
            plt.draw()
            break
        # find the subintervals with large error; these we need to subdivide
        bigerr = where(E>h/(b-a)*tol)[0]
        xi_new = (xi[bigerr] + xi[bigerr+1])/2
        # add the new points to the existing ones
        xi = union1d(xi, xi_new)
        m  = len(xi)
        
    # plot the error behaviour vs expected m^(-2)
    plt.figure(1)
    plt.clf()
    plt.loglog(M, err, 'b-x',lw=3, markersize=10,label='Numerical error')
    plt.loglog(M, M**(-2),'g-',lw=3, markersize=10,label='M**(-2)')
    plt.xlabel('M',fontsize=fs)
    plt.ylabel('error',fontsize=fs)
    plt.legend()
    plt.grid(True)
    plt.draw()
    return m, sum(I), sum(E)

# Test error_estimate
if __name__ == "__main__":
    a = 0.0
    b = 3.0
    tol = 1.0E-08

    m, I, E = adaptive_refinement(f,a,b,tol, trapezoid)
    print(f"Integral ~ {I}, error = {exactValue-I}, error estimate = {E}, numberOfPoints = {m}")
    
    m, I, E = adaptive_refinement(f,a,b,tol, simpsons)
    print(f"Integral ~ {I}, error = {exactValue-I}, error estimate = {E}, numberOfPoints = {m}")
    # Output
    # Integral ~ 0.38645985553796314, error = -5.994726937075257e-11, error estimate = 3.143123284713624e-09, numberOfPoints = 65534
    # Integral ~ 0.3864598557684714, error = -2.904555485017113e-10, error estimate = 1.263274524962636e-09, numberOfPoints = 12