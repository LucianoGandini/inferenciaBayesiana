#from pymc.examples import example
import example
from pymc.Matplot import plot
from pymc import MCMC

M = MCMC(example)

M.sample(iter=10000, burn=1000, thin=10)
plot(M)
