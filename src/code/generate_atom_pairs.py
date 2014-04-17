import itertools
import numpy as np
import mdtraj as md

trj = md.load("./system.subset.pdb")

top, bonds = trj.top.to_dataframe()

cond1 = (top.name == "CA") & (top.resSeq >= 139) & (top.resSeq <= 175)
#cond2 = (top.name == "CA") & (top.resSeq % 10 == 0)
cond3 = (top.name == "CA") & (top.resSeq >= 43) & (top.resSeq <= 56)
cond4 = (top.name == "CA") & (top.resSeq % 20 == 0)

cond5 = (top.name == "CA") & (top.resSeq % 10 == 0)
cond6 = (top.name == "CA") & (top.resSeq >= 139) & (top.resSeq <= 175)

#atom_indices = np.where(cond1 | cond2 | cond3)[0]
atom_indices = np.where(cond5 | cond6)[0]
atom_pairs = list(itertools.combinations(atom_indices, 2))

np.savetxt("./AtomPairs.dat", atom_pairs, "%d")
