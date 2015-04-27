import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects, assign
import mixtape.ghmm, mixtape.featurizer
import sklearn.hmm
import os

name = "tica"
json_filename = "./%s.jsonlines" % name
feature_filename = "./%s.pkl" % name

featurizer = mixtape.featurizer.load(feature_filename)

models = list(iterobjects(json_filename))
df = pd.DataFrame(models)

x = df.ix[0]
T = np.array(x["transmat"])
p = np.array(x["populations"])
n_states = len(p)


model = mixtape.ghmm.GaussianFusionHMM(n_states, featurizer.n_features)
model.means_ = x["means"]
model.vars_ = x["vars"]
model.transmat_ = x["transmat"]
model.populations_ = x["populations"]


means = model.means_
covars = model.vars_

#n_traj = 348
#n_traj = 131
n_traj = 1
all_assignments = []
all_probs = []
for i in range(n_traj):
    print(i)
    traj = md.load("./Trajectories/trj%d.h5" % i)
    ass, probs = assign(featurizer, traj, model)
    ass_assignments.extend(ass)
    all_probs.extend(probs)
    
all_assignments = np.array(all_assignments)
all_probs = np.array(all_probs)



traj = md.load("./Trajectories/trj%d.h5" % 50)
traj.superpose(trj0, atom_indices=atom_indices)
diff2 = (traj.xyz[:, atom_indices] - trj0.xyz[0, atom_indices]) ** 2
data = np.sqrt(np.sum(diff2, axis=2))
ass = hmm.predict(data)


rmsd = md.rmsd(traj, trj0)
