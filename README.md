# PHSX815_Project3

### Instructions

#### Step 1
Use rollDice.py to generate data and pipe it to a text file. If desired, the user can specify non-default values for the probability of rolling a 1, number of experiments, and number of rolls per experiment using "-prob1", "-Nexp", and "-Nroll", respectively.

eg: "python rollDice.py -prob1 .75 -Nroll 25 -Nexp 100 > data.txt"

#### Step 2
Use Analysis.py with the argument "-input" to plot a histogram of the estimated probability for rolling a 1 from the data.

eg: "python Analysis.py -input data.txt"