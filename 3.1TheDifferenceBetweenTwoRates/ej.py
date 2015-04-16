# Import relevant modules
import pymc
import numpy as np

# Priors on unknown parameters
theta1 = pymc.Beta('theta1',1,1)
theta2 = pymc.Beta('theta2',1,1)


# Observed Counts

#k1 ~ dbin(theta1,n1)

#k2 ~ dbin(theta2,n2)

k1 = pymc.Binomial('k1', n=100, p=theta1, value=95,observed=True)

k2 = pymc.Binomial('k2', n=50, p=theta2, value=1,observed=True)


# Difference between Rates

#delta <- theta1 - theta2


# Arbitrary deterministic function of parameters
@pymc.deterministic
def delta(a=theta1, b=theta2):
    """delta = theta1 + theta 2"""
    return a - b
