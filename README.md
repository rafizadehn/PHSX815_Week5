# PHSX 815: Week 2
## Rejection Sampling 

This repository includes a script that creates a sample-able distribution from a non-trivial function.

---

### RejectionSampling.py

To generate a distribution that can be sampled from a function that is harder to invert, a process called Rejection Sampling is used. In this case, the form $f(x)=x^x$ is used. To run this in Linux, open the containing folder in the terminal and run:

> $ python3 RejectionSampling.py

The default number of samples generated are 10,000, but this can be changed with the `-Nsample` argument. For example,

> $ python3 RejectionSampling.py -Nsample 100000 

The script will generate a plot for each step of this process to demonstrate how the distribution is generated. First, the script plots the function so the sampling in the next step can be easier visualized. We choose the range [0,1] for the x-axis for ease as the randomly generated values are within the same range.


Next, the rejection sampling process is performed. This is done by generated random points on the 2D plane and determining whether it is within the curve (a hit) or whether it is between the curve and the proposal distribution (a miss) which is a uniform line at y = 1.2. To visualize this, each point within the curve is plotted green and those outside of the curve are plotted red. 


The ratio of the number of hits to total number of draws is calculated for each particular x-vlaue and plotted into a histogram. This forms a distribution that conforms very closely to the function we are evaluating. The higher the number of samples we choose, the better this histogram fits the curve.

To convert this to a probability distribution, we simply take into account the width of each bin and graph the normalized probability for each bin, shown below.


The code for much of this file is provided by [Dr. Christopher Rogan (corgan) on GitHub](https://github.com/crogan/PHSX815_Week5/tree/master/python).

