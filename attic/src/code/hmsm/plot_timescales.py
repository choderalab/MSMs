import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects

timestep = 1.0
n_states = 2
input_filename = "HMM/4000pairs-lag10.jsonlines"

models = list(iterobjects(input_filename))


models = [model for model in models if model["n_states"] == n_states]

lagtimes = np.array([model["train_lag_time"] for model in models]) * timestep
timescales = np.array([model["timescales"] for model in models]) * timestep

plot(lagtimes, timescales[:,0], 'o')
