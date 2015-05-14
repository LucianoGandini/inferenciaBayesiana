import pymc
import ej

S = pymc.MCMC(ej, db='pickle')
S.sample(iter=10000, burn=5000, thin=2)
pymc.Matplot.plot(S)
#pymc.Matplot.autocorrelation(S)
#pymc.Matplot.discrepancy_plot(theta, name='theta', report_p=True)
