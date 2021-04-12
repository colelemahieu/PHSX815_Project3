import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from Random import Random

Nexp = 10
Nroll = 100

probA = 0.45

p1 = 0.0
for i in range(0,19):
    p1 = p1 + 0.05
    print(p1)
    if (abs(p1-probA)< 0.00000008):
        print("yes")
