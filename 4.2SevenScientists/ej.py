# Import relevant modules
import pymc
import numpy as np
import math
# Priors on unknown parameters
mu = pymc.Normal('mu',0,0.001)
# el segundo parametro es 1/varianza = 1/sigma^2


# Observed Counts

values = [-27.020, 3.570, 8.191, 9.898, 9.603, 9.945, 10.056]

g = []
p = []
sigmas = []



for i in range(0, 7):
    #tau =  pymc.Gamma('tau', alpha=0.001, beta=0.001)
    tau = pymc.Uniform('tau' + str(i), 0.001, 1000, plot=False)
    p.append(tau)
    @pymc.deterministic(name='sigma%d' % i, plot=True)
    def temp_theta(t=tau):
        return 1.0/t
    sigmas.append(temp_theta)

    g.append( pymc.Normal('x' + str(i), mu=mu , tau=tau , value=np.array([values[i]]),observed=True))
