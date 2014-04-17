import numpy as np
import pandas as pd
import mdtraj as md
import itertools

trj0 = md.load("./system.subset.pdb")
atom_indices = np.array([i for i, atom in enumerate(trj0.top.atoms) if ((atom.element.symbol != "H")|(atom.name == "H"))])

pair_indices = np.array(list(itertools.combinations(atom_indices, 2)))

n_choose = 4000

pair_indices_subset = pair_indices[np.random.choice(len(pair_indices), n_choose, replace=False)]

np.savetxt("./AtomPairs%d.dat" % n_choose, pair_indices_subset, "%d")
