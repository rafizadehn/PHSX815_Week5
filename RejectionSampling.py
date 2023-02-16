import numpy as np
import sys
import matplotlib.pyplot as plt

#sys.path.append(".")
#from Random import Random 

#global variables
bin_width = 0.
xmin = 0.
xmax = 1.
#random = Random()

# Normal distribution with mean zero and sigma = 1
# Note: multiply by bin width to match histogram
def f(x):
	return x**x + 0.2

def Plot_f(x,bin_width):
	return bin_width*f(x)

# Uniform (flat) distribution scaled to function max
# Note: multiply by bin width to match histogram
def Flat(x):
	return max(x)
	
def PlotFlat(x,bin_width):
	return bin_width*Flat(x)

# Get a random X value according to a flat distribution
def SampleFlat():
	return xmin + (xmax-xmin)*random.rand()

def sample(function, Nsample, xmin, xmax, ymax):
    #rand = random.rand(seed)
    samples = []
    x1 = np.random.uniform(low=xmin, high=xmax, size=Nsample)
    y1 = np.random.uniform(low=0, high=ymax, size=Nsample)
    passed = (y1 < function(x1)).astype(int)
    while len(samples) < Nsample:
        samples += x1[y1 < function(x1)].tolist()
    return x1, y1, passed, samples[:Nsample]

#main function
if __name__ == "__main__":

	# default number of samples
    Nsample = 10000

    # default seed
    seed = 5555

	# read the user-provided seed from the command line (if there)
	#figure out if you have to have -- flags before - flags or not
    if '-Nsample' in sys.argv:
        p = sys.argv.index('-Nsample')
        Nsample = int(sys.argv[p+1])
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-Nsample] number" % sys.argv[0])
        print
        sys.exit(1)  


    xs = np.linspace(0, 1, 1000)
    ys = f(xs)
    
    plt.plot(xs, ys, label = "Function")
    plt.fill_between(xs, ys, 0, alpha = 0.2)
    plt.xlim(min(xs),max(xs))
    plt.ylim(0, max(ys))
    plt.xlabel("x-values")
    plt.ylabel("f(x)")
    plt.legend()
    plt.show()
	
    x, y, passed, samples = sample(f, Nsample, xmin, xmax, max(ys))
    
    plt.plot(xs, ys)
    plt.fill_between(xs, ys, 0, alpha = 0.2)
    plt.scatter(x, y, c=passed, cmap="RdYlGn", vmin=-0.1, vmax=1.1, lw=0, s=15)
    plt.xlabel("x-values")
    plt.ylabel("f(x)")
    plt.xlim(xmin, max(xs))
    plt.ylim(0, max(ys))
    plt.show()
 
    print(f"Efficiency was {passed.mean() * 100:0.1f}%")
   
    plt.plot(xs, ys)
    plt.hist(samples, density = True, alpha = 0.2, label = "Sample Distribution", bins = 50, linewidth = 1, edgecolor = 'k')
    plt.xlim(xmin, xmax)
    plt.ylim(0, 1.5)
    plt.show()

    #normalize data for probability distribution
    weights = np.ones_like(samples) / len(samples)
    n = plt.hist(samples,weights=weights,alpha=0.3,label="samples from f(x)",bins=50, linewidth = 1, edgecolor = 'k')
    plt.ylabel("Probability / bin")
    plt.xlabel("x")
    bin_width = n[1][1] - n[1][0]
    hist_max = max(n[0])

    plt.ylim(min(bin_width*f(xmax), 1./float(Nsample+1)),1.5*max(hist_max, bin_width*f(0)))

    x = np.arange(xmin,xmax,0.001)
    y_norm = list(map(Plot_f,x,np.ones_like(x)*bin_width))
    #y_norm = list(map(Plot_f(x,bin_width))
    plt.plot(x,y_norm,color='green',label='given f(x)')
	
    #plt.plot(x,y_flat,color='red',label='proposal g(x)')
    plt.title("Density estimation with Monte Carlo")
    plt.legend()
    plt.show()

