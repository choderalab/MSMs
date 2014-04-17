import shutil
import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects
import mixtape.ghmm
import mixtape.featurizer
import os

name = "atomindices"
json_filename = "./%s.jsonlines" % name
feature_filename = "./%s.pkl" % name

models = list(iterobjects(json_filename))
df = pd.DataFrame(models)

x = df.ix[0]

T = np.array(x["transmat"])
p = np.array(x["populations"])

featurizer = mixtape.featurizer.load(feature_filename)

model = mixtape.ghmm.GaussianFusionHMM(3, featurizer.n_features)
model.means_ = x["means"]
model.vars_ = x["vars"]
model.transmat_ = x["transmat"]
model.populations_ = x["populations"]




trj0 = md.load("./system.subset.pdb")
atom_indices = np.loadtxt("./AtomIndices.dat", "int")

n_traj = 348
#n_traj = 131
scores = np.zeros(n_traj)
for i in range(n_traj):
    print(i)
    traj = md.load("./Trajectories/trj%d.h5" % i)
    features = featurizer.featurize(traj)
    scores[i] = model.score([features]) / float(len(features))

cutoff = 500.0  # atomindices
#cutoff = 0.0  # atompairs
k = 0
for i in range(n_traj):
    if scores[i] > cutoff:
        print(i, k)
        shutil.copy("./Trajectories/trj%d.h5" % i, "./subset_%s/Trajectories/trj%d.h5" % (name, k))
        k += 1
