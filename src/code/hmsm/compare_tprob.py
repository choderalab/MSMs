import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects

input_filename = "tica2.jsonlines"

models = list(iterobjects(input_filename))
df = pd.DataFrame(models)

for i in range(30):
    x = df.ix[i]
    T = np.array(x["transmat"])
    p = np.array(x["populations"])
    print(x)
    print(T)
    print(p)


input_filename = "atompairs.jsonlines"

models2 = list(iterobjects(input_filename))
df2 = pd.DataFrame(models2)
x2 = df2.ix[0]
T2 = np.array(x2["transmat"])
p2 = np.array(x2["populations"])

lag = df[df["n_states"] == 3].train_lag_time
tau = df[df["n_states"] == 3].timescales
