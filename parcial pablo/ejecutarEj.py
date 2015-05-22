import pymc
import ej
import numpy as np

S = pymc.MCMC(ej, db='pickle')
S.sample(iter=10000, burn=5000, thin=2)

alpha =  np.array([x for x in S.trace('alpha')])
p1 = np.array([x for x in S.trace('player 1')])
p2 = np.array([x for x in S.trace('player 2')])
p3 = np.array([x for x in S.trace('player 3')])
p4 = np.array([x for x in S.trace('player 4')])

print "alpha --- mean: " + str(np.mean(alpha)) + "std: " + str(np.std(alpha))
print "p1 --- mean: " + str(np.mean(p1)) + "std: " + str(np.std(p1))
print "p2 --- mean: " + str(np.mean(p2)) + "std: " + str(np.std(p2))
print "p3 --- mean: " + str(np.mean(p3)) + "std: " + str(np.std(p3))
print "p4 --- mean: " + str(np.mean(p4)) + "std: " + str(np.std(p4))

pymc.Matplot.plot(S)
