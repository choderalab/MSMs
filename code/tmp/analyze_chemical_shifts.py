from fitensemble.nmr_tools.chemical_shifts import ppm_atom_uncertainties
import seaborn as sns
import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline
import mdtraj as md

tica_lagtime = 1600

trajectories = dataset.MDTrajDataset("./trajectories/*.h5")
t0 = trajectories[0][0]
n = len(trajectories)

shifts = [pd.read_hdf("./shifts.h5", "trj%d" % k) for k in range(n)]

n_frames = min(s.shape[1] for s in shifts)

shifts = [s.iloc[:, 0:n_frames] for s in shifts]

min(s.shape[1] for s in shifts)
max(s.shape[1] for s in shifts)

mu = sum(s for s in shifts) / float(len(shifts))
mu2 = sum(s ** 2 for s in shifts) / float(len(shifts))

#sigma = (mu2 - mu ** 2) ** 0.5
sigma = ppm_atom_uncertainties.ix[mu.reset_index().name]
sigma.index = mu.index


dz = (mu.iloc[:, -1] - mu.iloc[:, 0]) / sigma

dz.plot()

bfactors = np.zeros(t0.n_atoms)
for k, atom in enumerate(t0.top.atoms):
    name, resSeq = atom.name, atom.residue.resSeq
    try:
        value = abs(dz[resSeq, name])
        bfactors[k] = value
    except KeyError:
        pass

t0.save_pdb("./bfactor.pdb", bfactors=bfactors)
