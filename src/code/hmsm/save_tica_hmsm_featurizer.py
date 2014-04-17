import itertools
import numpy as np
import mdtraj as md
import msmbuilder as msmb

n_traj = 1
trj0 = md.load("./system.subset.pdb")

pair_indices = np.loadtxt("./AtomPairs.dat", 'int')

metric = msmb.metrics.AtomPairs(atom_pairs=pair_indices)
tica = msmb.reduce.tICA(1, prep_metric=metric)

for filename in ["./Trajectories/trj%d.h5" % i for i in range(n_traj)]:
    trj = md.load(filename)
    tica.train(trajectory=trj)

tica.solve()
print tica.vals[0:5]


tica.save("./tica.h5")
import mixtape.tica_featurizer
featurizer = mixtape.tica_featurizer.TICAFeaturizer("./tICA_metrics/tICAData-4000pairs-10lag.h5", n_tics=200)
featurizer.save("./tICA_metrics/tICAData-4000pairs-10lag.pkl")

#f = mixtape.featurizer.load("./tica.pkl")
