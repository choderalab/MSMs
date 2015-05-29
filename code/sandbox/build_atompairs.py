import numpy as np
import mdtraj as md
import msmbuilder.featurizer, msmbuilder.utils

t = md.load("./trajectories/run0-clone1.h5")[0]

atom_indices, pair_indices = msmbuilder.featurizer.subset_featurizer.get_atompair_indices(t, keep_atoms=None, exclude_atoms=np.array([]))

dih_model = msmbuilder.utils.load("./dihedrals/model.pkl")
n_features = dih_model.transform(t)[0].shape[1]

rnd_pairs = pair_indices[np.random.random_integers(0, len(pair_indices) - 1, n_features)]

np.savetxt("./AtomPairs.dat", rnd_pairs, "%d")

"""
msmb AtomPairsFeaturizer --trjs "trajectories/*.h5" --transformed atompairs --out atom_pairs.pkl --exponent -1 --pair_indices=./AtomPairs.dat
msmb tICA -i atompairs/ --transformed atompairstica/tica400 -o atompairstica/tica400.pkl --lag_time 400 --gamma 0.01 --n_components 20
"""
