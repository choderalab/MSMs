import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects
import mixtape.ghmm
import os

#os.system("hmsm fit-ghmm -k 3 -l 1 --dir Trajectories/ --ext h5 -a AtomIndices.dat --top system.subset.pdb")

input_filename = "./hmms.jsonlines"

models = list(iterobjects(input_filename))
df = pd.DataFrame(models)

x = df.ix[0]

T = np.array(x["transmat"])
p = np.array(x["populations"])


model = mixtape.ghmm.GaussianFusionHMM(3, 1252)
model.means_ = x["means"]
model.vars_ = x["vars"]
model.transmat_ = x["transmat"]
model.populations_ = x["populations"]

