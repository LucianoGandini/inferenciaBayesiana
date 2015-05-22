# Import relevant modules
import pymc
import numpy as np
import math

# Priors hiperparametros
alpha = pymc.Uniform('alpha', 0.01, 3)

players_priors = []
games = []
ns = [2, 4, 6]
observations = {1: {1: 0, 2: 0, 3: 0 },
                2: {1: 1, 2: 0, 3: 1 },
                3: {1: 1, 2: 4, 3: 6 },
                4: {1: 2, 2: 3, 3: 6 }
                }

for i in range(1, 5): # priors en jugadores (1 a 4)
    player_dist = pymc.Beta("player " + str(i), alpha, alpha)
    players_priors.append(player_dist)

    for j in range(1, 4):
        print (i, j)
        game = pymc.Binomial("k"+ str(i) + str(j), p=player_dist, n=ns[j-1], value=observations[i][j], observed=True)
        games.append(game)
