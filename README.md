# PHSX815_Project3

## Instructions

### Part I

#### Step 1
Use rollDice.py to generate data and pipe it to a text file.

Optional: the user can specify non-default values for the probability of rolling a 1, number of experiments, and number of rolls per experiment using "-prob1", "-Nexp", and "-Nroll", respectively.

eg: "python rollDice.py -prob1 .75 -Nroll 25 -Nexp 100 > data.txt"

#### Step 2
Use Analysis.py with the argument "-input" to plot a histogram and Gaussian fit of the estimated probability for rolling a 1 from the data.

eg: "python Analysis.py -input data.txt"


### Part II
Use "python neyman.py" to generate the Neyman Construction for P_1 and plot two slices from it.

Optional: Specify which two slices are plotted using "-sliceA" and "-sliceB". However, the probability slices must be from 0.05 to 0.95 in increments of 0.05. Numbers of experiments performed and number of rolls per experiment can also be specified with "-Nexp" and "-Nroll" respectively.

eg: "python neyman.py -Nexp 500 -Nroll 100 -sliceA 0.55 -sliceB 0.85"

