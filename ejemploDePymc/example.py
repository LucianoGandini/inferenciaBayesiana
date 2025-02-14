from pymc import DiscreteUniform, Exponential, deterministic, Poisson, Uniform
import numpy as np

# disasters_array =   \
#      np.array([ 4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
#                    3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
#                    2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
#                    1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
#                    0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
#                    3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
#                    0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])

dist1 = np.random.poisson(1, 10)
dist2 = np.random.poisson(5, 20)
disasters_array = np.concatenate([dist1, dist2])


switchpoint = DiscreteUniform('switchpoint', lower=0, upper=30, doc='Switchpoint[year]')

early_mean = 1#dist1.mean() #Exponential('early_mean', beta=1.)
late_mean = 5#dist2.mean() #Exponential('late_mean', beta=1.)

@deterministic(plot=False)
def rate(s=switchpoint, e=early_mean, l=late_mean):
    ''' Concatenate Poisson means '''
    out = np.empty(len(disasters_array))
    out[:s] = e
    out[s:] = l
    return out

disasters = Poisson('disasters', mu=rate, value=disasters_array, observed=True)
