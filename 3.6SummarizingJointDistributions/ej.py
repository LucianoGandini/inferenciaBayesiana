# Import relevant modules
import pymc
import numpy as np

# Priors on unknown parameters
theta = pymc.Beta('theta1',1,1)

n = pymc.DiscreteUniform('n',1,500)

# Observed Counts

#k1 ~ dbin(theta1,n1)

#k2 ~ dbin(theta2,n2)
k = []


values = [16, 18, 22, 25, 27]

for i in range(0, 5):
    k.append( pymc.Binomial('k', n=n, p=theta, value=np.array([values[i]]),observed=True))


# Difference between Rates

#delta <- theta1 - theta2


# Arbitrary deterministic function of parameters
# @pymc.deterministic
# def delta(a=theta1, b=theta2):
#     """delta = theta1 + theta 2"""
#     return a - b
