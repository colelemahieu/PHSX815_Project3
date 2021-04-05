# this file estimates p1 probability given the data

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from fractions import Fraction
from Random import Random

# get file input
p = sys.argv.index("-input")

# initialize number of experiments
nexp = 0

# count the number of experiments, file0
with open(sys.argv[p+1], "r") as file0:
    for line in file0:
        nexp +=1

# get the file data, file0
with open(sys.argv[p+1], "r") as file0:
    filestring = file0.read()
    filelist = filestring.split(" ")

# get rid of the \n symbols
filelist_b = []
for x in filelist:
    filelist_b.append(x.strip())

# delete empty spaces in the list
filelist_clean = [x for x in filelist_b if x]

# calculate number of rolls per experiment
rolls = len(filelist_clean)/nexp

# get arrays of float dice rolls
data = []
for i in range(0, len(filelist_clean)):
    data.append(float(filelist_clean[i]))

# make an array divided into subarrays for each experiment
array = np.array(data)
data_arr = np.reshape(array, (-1, rolls))

# loop over rolls for each experiment to calculate p1
guess = []

for i in range(0, nexp):
    ones = 0
    ones_tot = 0
    
    for j in range(0, rolls):
        if (data_arr[i][j]==1):
            ones = ones + 1
    cp1 = float(ones) / rolls
    guess.append(cp1)

# plot guesses
plt.figure()
plt.hist(guess, bins=15)

plt.show()
        

