import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects
import mixtape.ghmm
import os

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


trj0 = md.load("./system.subset.pdb")
atom_indices = np.loadtxt("./AtomIndices.dat", "int")

#n_traj = 348
n_traj = 131
scores = np.zeros(n_traj)
for i in range(n_traj):
    print(i)
    traj = md.load("./Trajectories/trj%d.h5" % i)
    traj.superpose(trj0, atom_indices=atom_indices)
    diff2 = (traj.xyz[:, atom_indices] - trj0.xyz[0, atom_indices])**2
    data = np.sqrt(np.sum(diff2, axis=2))
    scores[i] = model.score([data]) / float(len(data))


cutoff = 500.
k = 0
for i in range(n_traj):
    if scores[i] > cutoff:
        shutil.copy("./Trajectories/trj%d.h5" % i, "./subset/Trajectories/trj%d.h5" % k)
        k += 1
