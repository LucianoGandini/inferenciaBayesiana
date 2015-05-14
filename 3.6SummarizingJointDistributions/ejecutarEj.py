import pymc
import ej
import numpy as np
from scipy.stats import mode

S = pymc.MCMC(ej, db='pickle')
a = S.sample(iter=10000, burn=5000, thin=2)
n =  [x for x in S.trace('n')]
t1 = [x for x in S.trace('theta1')]


#
# pymc.Matplot.plot(S)

import matplotlib.pyplot as plt
plt.scatter(x=n, y=t1)

# plt.plot([np.mean(n)], [np.mean(t1)], 'ro')
# plt.plot([mode(n)[0][0]], [mode(t1)[0][0]], 'go')

plt.show()
#pymc.Matplot.autocorrelation(S)
#pymc.Matplot.discrepancy_plot(theta, name='theta', report_p=True)
