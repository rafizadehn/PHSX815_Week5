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

    
    ### PART 1 - plot target function f(x) and proposed function g(x)

    # generates x values to be evaluted by the defined function f(x)
    
    xs = np.linspace(0, 1, 1000)
    ys = f(xs)
    
    # create the plot

    plt.plot(xs, ys, label = "target function f(x)", color = 'blue', linestyle ='-', linewidth = 3)
    plt.plot([xmin, xmax], [max(ys), max(ys)],label = "proposed function g(x)" , color = 'red', linestyle = '-', linewidth = 3)
    plt.title("Plotted Functions", fontsize = 15, fontweight = 'bold')
    plt.fill_between(xs, ys, 0, alpha = 0.2)
    plt.xlim(min(xs),max(xs))
    plt.ylim(0, 1.2*max(ys))
    plt.xlabel("x-values", fontsize = 15)
    plt.ylabel("y-values", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.legend(fontsize = 15, loc = 'upper right')
    plt.show()


    ### PART 2 - perform rejection sampling

    # uses defined sample function that generates random x and y values for sampling
    # returns:
    # x and y values for visualization of points. not needed for analysis.
    # an array of booleans that tracks which randomly generated points are 'hits' and 'misses'
    # an array that gives the actualy value of each hit and miss

    x, y, hits, samples = sample(f, Nsample, xmin, xmax, max(ys))
    x_c, y_c, hits_c, samples_c = sample(f, int(Nsample*0.1), xmin, xmax, max(ys))

    # create the scatter plots

    # scatter plot for Nsample 

    plt.subplot(1, 2, 2)
    plt.plot(xs, ys, label = "target function f(x)", color = 'blue', linestyle = '-', linewidth = 3)
    plt.fill_between(xs, ys, 0, alpha = 0.2)
    plt.plot([xmin, xmax], [max(ys), max(ys)],label = "proposed function g(x)" , color='red', linestyle='-', linewidth=3)
    plt.scatter(x, y, c=hits, cmap="RdYlGn", vmin=-0.1, vmax=1.1, lw=0, s=15, label = "randomly generated points")
    plt.xlabel("x-values", fontsize = 15)
    plt.ylabel("y-values", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.title("Rejection Sampled Points (Nsample = " + str("{:.0e}".format(Nsample))+")", fontsize = 15, fontweight = 'bold') 
    plt.xlim(xmin, max(xs))
    plt.ylim(0, 1.2*max(ys))
    plt.legend(fontsize = 15)
    
    # scatter plot for Nsample/10, just for educational purposes

    plt.subplot(1, 2, 1)
    plt.plot(xs, ys, label = "target function f(x)", color = 'blue', linestyle = '-', linewidth = 3)
    plt.fill_between(xs, ys, 0, alpha = 0.2)
    plt.plot([xmin, xmax], [max(ys), max(ys)],label = "proposed function g(x)" , color='red', linestyle='-', linewidth=3) 
    plt.scatter(x_c, y_c, c=hits_c, cmap="RdYlGn", vmin=-0.1, vmax=1.1, lw=0, s=15, label = "randomly generated points")
    plt.xlabel("x-values", fontsize = 15)
    plt.ylabel("y-values", fontsize = 15)
    plt.title("Rejection Sampled Points (Nsample = " + str("{:.0e}".format(Nsample*0.1))+")", fontsize = 15, fontweight = 'bold')
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.xlim(xmin, max(xs))
    plt.ylim(0, 1.2*max(ys))
    plt.legend(fontsize = 15)
 
    plt.show()
    
    # the efficiency is the number of hits / the total number of draws,
    # which is the same as the mean of the boolean array 'hits'
    # this prints the efficiency

    print(f"Efficiency was {hits.mean() * 100:0.1f}%")
 
    ### PART 3 - plot the sample distribution
   
    # plot for Nsample

    plt.subplot(1, 2, 2)
    plt.plot(xs, ys)
    plt.hist(samples, density = True, alpha = 0.2, label = "sample points distribution", bins = 50, linewidth = 1, edgecolor = 'k')
    plt.xlim(xmin, xmax)
    plt.ylim(0, 1.5)
    plt.title("Histogram of Sampled Points (Nsample = " + str("{:.0e}".format(Nsample))+")", fontsize = 15, fontweight = 'bold') 
    plt.xlabel("x-values", fontsize = 15)
    plt.ylabel("y-values", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.legend(fontsize = 15, loc = 'upper right')

    # plot for Nsample/10

    plt.subplot(1, 2, 1)
    plt.plot(xs, ys)
    plt.hist(samples_c, density = True, alpha = 0.2, label = "sample points distribution", bins = 50, linewidth = 1, edgecolor = 'k')
    plt.xlim(xmin, xmax)
    plt.ylim(0, 1.5)
    plt.title("Histogram of Sampled Points (Nsample = " + str("{:.0e}".format(Nsample*0.1))+")", fontsize = 15, fontweight = 'bold')
    plt.xlabel("x-values", fontsize = 15)
    plt.ylabel("y-values", fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
    plt.legend(fontsize = 15, loc = 'upper right')

    plt.show()

    ### PART 4 - normalize data for probability distribution
    
    # the code for this is borrowed from Dr. Rogan 
    # (I promise to give it back)

    # plot for Nsample

    plt.subplot(1, 2, 2)
    weights = np.ones_like(samples) / len(samples)
    n = plt.hist(samples,weights=weights,alpha=0.3,label="samples from f(x)",bins=50, linewidth = 1, edgecolor = 'k')
    plt.ylabel("Probability Density", fontsize = 15)
    plt.xlabel("x-values", fontsize = 15)
    bin_width = n[1][1] - n[1][0]
    hist_max = max(n[0])
    plt.ylim(min(bin_width*f(xmax), 1./float(Nsample+1)),1.5*max(hist_max, bin_width*f(0)))

    x = np.arange(xmin,xmax,0.001)
    y_norm = list(map(Plot_f,x,np.ones_like(x)*bin_width))
    plt.plot(x,y_norm,color='blue', linewidth = 3, label = "normalized target function f(x)")
    plt.title("Probability Density with Monte Carlo (Nsample =" + str("{:.0e}".format(Nsample))+")", fontsize = 15, fontweight = 'bold')
    plt.legend(fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
 
    # plot for Nsample/10

    plt.subplot(1, 2, 1)
    weights_c = np.ones_like(samples_c) / len(samples_c)
    n_c = plt.hist(samples_c,weights=weights_c,alpha=0.3,label="samples from f(x)",bins=50, linewidth = 1, edgecolor = 'k')
    plt.ylabel("Probability Density", fontsize = 15)
    plt.xlabel("x-values", fontsize = 15)
    bin_width_c = n_c[1][1] - n_c[1][0]
    hist_max_c = max(n_c[0])
    plt.ylim(min(bin_width*f(xmax), 1./float((Nsample*0.1)+1)),1.5*max(hist_max, bin_width*f(0)))

    x = np.arange(xmin,xmax,0.001)
    y_norm = list(map(Plot_f,x,np.ones_like(x)*bin_width_c))
    plt.plot(x,y_norm,color='blue', linewidth = 3, label = "normalized target function f(x)")
    plt.title("Probability Density with Monte Carlo (Nsample =" + str("{:.0e}".format(Nsample*0.1))+")", fontsize = 15, fontweight = 'bold') 
    plt.legend(fontsize = 15)
    plt.tick_params(axis = 'both', labelsize = 13)
 
    plt.show()

