from numpy import divide, diff, append, array, union1d, where
from error_estimate import error_estimate
import matplotlib.pyplot as plt
from function import f, exactValue
from simpsons import simpsons

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
    tol = 1.0E-08

    m, I, E = adaptive_refinement(f, 0.0, 1.5, tol, simpsons)
    print(f"Integral ~ {I}, error estimate = {E}, numberOfPoints = {m}")
    m, I, E = adaptive_refinement(f, 1.5, 3.0, tol, simpsons)
    print(f"Integral ~ {I}, error estimate = {E}, numberOfPoints = {m}")
    
    # Integral ~ -0.9425985975757181, error = 1.329058453053734, error estimate = 3.142930585393379e-09, numberOfPoints = 16384
    # Integral ~ 1.3290584529338703, error = -0.9425985974558544, error estimate = 3.143213689196797e-09, numberOfPoints = 16385
