from numpy import *


def error_estimate(xi,f, kvadratur):
    """
    Estimate the integration error for adaptive integration

    Input:
    xi: location of nodes, defining the subdivision of the interval
    (including the endpoints)
    f:  function to integrate


    Output:

    I = the numerical approximation to the integral on each subinterval
    E = error estimate on each interval
    """
    xi_mid = (xi[0:-1] + xi[1:])/2
    xi_fine = union1d(xi, xi_mid)
    I_coarse = kvadratur(xi,f)
    I_fine = kvadratur(xi_fine,f)
    m = len(xi)-1
    E = zeros(m)
    for i in range(m):
        # estimate the error (see formula (5.38) in the book)
        E[i] = 4/3*abs(I_coarse[i]-I_fine[2*i+1]-I_fine[2*i])*3.0
    return I_coarse, E
