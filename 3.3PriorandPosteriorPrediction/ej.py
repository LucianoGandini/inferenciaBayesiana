# Import relevant modules
import pymc
import numpy as np

# Priors on unknown parameters
theta = pymc.Beta('theta1',1,1)


# Observed Counts

#k1 ~ dbin(theta1,n1)

#k2 ~ dbin(theta2,n2)

k = pymc.Binomial('k', n=10, p=theta, value=np.array([3,1,4,5]),observed=True)


# Difference between Rates

#delta <- theta1 - theta2


# Arbitrary deterministic function of parameters
# @pymc.deterministic
# def delta(a=theta1, b=theta2):
#     """delta = theta1 + theta 2"""
#     return a - b
