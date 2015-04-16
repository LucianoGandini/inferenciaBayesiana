import pymc
import ej

S = pymc.MCMC(ej, db='pickle')
S.sample(iter=10000, burn=5000, thin=2)
pymc.Matplot.plot(S)
