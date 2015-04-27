import numpy as np
import pandas as pd
import mdtraj as md
import itertools

trj0 = md.load("./system.subset.pdb")
atom_indices = np.arange(trj0.n_atoms)
pair_indices = np.array(list(itertools.combinations(atom_indices, 2)))

traj = md.load("./Trajectories/trj%d.h5" % 0)[0:1]
d = md.geometry.compute_distances(traj, pair_indices, periodic=False) ** 2.

d2 = np.zeros((trj0.n_atoms, trj0.n_atoms))
for k, (i, j) in enumerate(pair_indices):
    d2[i, j] = d[0, k]
    d2[j, i] = d[0, k]
