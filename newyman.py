# Cole Le Mahieu Project 3

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from math import *
from Random import Random

# instantiate Random class
random = Random()

# default number experiments, measurements
Nexp = 500
Nroll = 100

# default slices to pull out of neymann construction
probA = 0.3
probB = 0.6

# user can input value for experiment or measurement number
if "-Nexp" in sys.argv:
    p = sys.argv.index("-Nexp")
    Ne = int(sys.argv[p+1])
    if Ne > 0:
        Nexp = Ne
if "-Nroll" in sys.argv:
    p = sys.argv.index("-Nroll")
    Nt = int(sys.argv[p+1])
    if Nt > 0:
        Nroll = Nt

# user can also input the two probability slices if desired
if "-sliceA" in sys.argv:
    p = sys.argv.index("-sliceA")
    sA = float(sys.argv[p+1])
    if sA > 0:
        probA = sA
if "-sliceB" in sys.argv:
    p = sys.argv.index("-sliceB")
    sB = float(sys.argv[p+1])
    if sB > 0:
        probB = sB

# arrays in which to collect data for our 2D histogram
p1_true_arr = []
p1_guess_arr = []

# arrays in which to save 2 slices
sliceA = []
sliceB = []

# loop through different p1 values and calculate our best guess each time
p1 = 0
for i in range(0,19):
    p1 = p1 + 0.05
    diff = 1 - p1
    prob = float(diff) / 5
    p2 = prob
    p3 = prob
    p4 = prob
    p5 = prob

    for j in range(0, Nexp):
        ones = 0

        for k in range(0, Nroll):
            x = random.DiceRoll(p1,p2,p3,p4,p5)
            if (x==1):
                ones = ones + 1
        cp1 = float(ones) / Nroll
        p1_true_arr.append(p1)
        p1_guess_arr.append(cp1)

        # fill our 2 slices
        if (abs(p1-probA) < 0.00000008):
            sliceA.append(cp1)
        if (abs(p1-probB) < 0.00000008):
            sliceB.append(cp1)


# plotting
plt.figure()
plt.hist2d(p1_true_arr, p1_guess_arr)
plt.title("Neyman Construction for $P_{1}$ (%i rolls per exp)" %(Nroll))
plt.xlabel("True Probability Value")
plt.ylabel("Estimated Probability Value")

# fits for slices 1 and 2
(muA, sigmaA) = norm.fit(sliceA)
(muB, sigmaB) = norm.fit(sliceB)

# slice 1
plt.figure()
nA, binsA, patchesA = plt.hist(sliceA, normed=1)
yA = mlab.normpdf(binsA, muA, sigmaA)
lA = plt.plot(binsA, yA, "r", linewidth=2)

leftA, rightA = plt.xlim()
bottomA, topA = plt.ylim()
plt.text(leftA+.05*(rightA-leftA), .9*topA, "$\\mu$ = %.3f" %(muA), fontweight="bold")
plt.text(leftA+.05*(rightA-leftA), .85*topA, "$\\sigma$ = %.3f" %(sigmaA), fontweight="bold")
plt.title("Neyman Slice for $P_{1}$ = %.2f (%i rolls per exp)" %(probA, Nroll))
plt.xlabel("Estimated Probability from Data")
plt.ylabel("Relative Frequency")

# slice 2
plt.figure()
nB, binsB, patchesB = plt.hist(sliceB, normed=1)
yB = mlab.normpdf(binsB, muB, sigmaB)
lB = plt.plot(binsB, yB, "r", linewidth=2)

leftB, rightB = plt.xlim()
bottomB, topB = plt.ylim()
plt.text(leftB+.05*(rightB-leftB), .9*topB, "$\\mu$ = %.3f" %(muB), fontweight="bold")
plt.text(leftB+.05*(rightB-leftB), .85*topB, "$\\sigma$ = %.3f" %(sigmaB), fontweight="bold")
plt.title("Neyman Slice for $P_{1}$ = %.2f (%i rolls per exp)" %(probB, Nroll))
plt.xlabel("Estimated Probability from Data")
plt.ylabel("Relative Frequency")

plt.show()
        
                


