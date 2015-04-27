import itertools
import numpy as np
import mdtraj as md
import msmbuilder as msmb

trj0 = md.load("./system.subset.pdb")
trajectories = [md.load("./Trajectories/trj%d.h5" % i) for i in range(5)]

#atom_indices = np.arange(trj0.n_atoms)
atom_indices = np.array([i for i, atom in enumerate(trj0.top.atoms) if atom.element.symbol != "H"])
pair_indices = np.array(list(itertools.combinations(atom_indices, 2)))

n_choose = 1000
n_trials = 10
for i in range(n_trials):
    pair_indices_subset = pair_indices[np.random.choice(len(pair_indices), n_choose, replace=False)]
    metric = msmb.metrics.AtomPairs(atom_pairs=pair_indices_subset)
    tica = msmb.reduce.tICA(1, prep_metric=metric)
    for trj in trajectories:
        tica.train(trajectory=trj)
    tica.solve()
    print tica.vals[0:5]
