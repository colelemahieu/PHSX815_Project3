# program to roll Dice

# import packages
from __future__ import print_function
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction
from Random import Random

# instantiate Random class
random = Random()

# default values for p1, experiment and measurement number
p1 = Fraction(1,6)
Nexp = 12
Nroll = 10

# user can input value for p1, experiment or measurement number
if "-prob1" in sys.argv:
    p = sys.argv.index("-prob1")
    prob1 = float(sys.argv[p+1])
    if (prob1 > 0 and prob1 < 1):
        p1 = prob1
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

# the remaining dice roll outcomes are given equal probability
diff = 1 - p1
prob = float(diff) / 5
p2 = prob
p3 = prob
p4 = prob
p5 = prob

# output rolls
for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.DiceRoll(p1,p2,p3,p4,p5), end=" ")
            print(" ")
