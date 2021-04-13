# histogram.py:
#   Plot a histogram of Logistic map iterates on the interval.
# Modified version of script from 
# http://csc.ucdavis.edu/~chaos/courses/nlp/

# Import modules
from numpy import *
from pylab import * # plotting

# Define the Logistic map's function 
def LogisticMap(r,x):
    return r * x * (1.0 - x)

# Parameters: Select one by uncommenting it, leaving others commented out
# 

#r = 3.5699456718695445
# r = 3.8
# r = 2.9
#r = 2

for r in np.arange(2.99999, 3.0, 0.4):
    # The domain in x that we'll look at
    xlow = 0.0
    xhigh = 1.0

    # Set the initial condition
    state = 0.1

    # The number of histogram bins over that domain
    nBins = 1000

    # The bin size
    xInc  = (xhigh-xlow)/float(nBins)

    # Setup histogram arrays
    # Note how we make sure x = 1.0 is included
    x = linspace(xlow, xhigh, nBins, endpoint=True)

    # This is the array in which we store the bin counts
    p = zeros((nBins),float)

    print 

    # Setup the plot
    # It's numbered 1 and is 8 x 6 inches.
    figure(1,(12,9))
    TitleString = 'Logistic map histogram at r = %g' % r
    title(TitleString)
    xlabel('x')       # set x-axis label
    ylabel('Prob(x)') # set y-axis label


    # Iterate to throw away
    nTransients = 200

    # Iterates over which to accumulate histogram counts
    # Lots!
    nIterates = 2000000

    # Let's get started
    for n in range(nTransients):
        state = LogisticMap(r,state)
    for n in range(nIterates):
        state = LogisticMap(r,state)
        index = int((nBins) * state)
        p[index] = p[index] + 1

    # Normalize the histogram
    p = p / float(nIterates)


    # Plot the histogram
    plot(x, p, 'b-', antialiased=True)

    # Display plot in window
    savefig(f"images/{round(r * 10)}.jpg")