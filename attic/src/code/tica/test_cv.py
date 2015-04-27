import mdtraj as md
import sklearn.cross_validation

trj = md.load("./Trajectories/trj0.h5")
cv = sklearn.cross_validation.KFold(len(trj), 2)
for train, test in cv:
    trj0 = trj[train]
    trj1 = trj[test]


metric = msmb.metrics.AtomPairs(atom_pairs=pair_indices[subset])
msmb.clustering.KMeans(metric)
