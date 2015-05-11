"""
Plot the first two TICS with ensembler models.
"""
#Note ensembler models are still after implicit refine.
import matplotlib
matplotlib.use('Agg')

from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt
import mdtraj as md

tica_lagtime = 1600

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica%d.h5" % tica_lagtime)
Xf = np.concatenate(X)

tica_model = utils.load("./tica%d.pkl" % tica_lagtime)

#Load trajectory with ensembler models
t_models = md.load("../ensembler-models/traj-refine_implicit_md.xtc", top = "../ensembler-models/topol-renumbered-implicit.pdb")

#Now make dihedrals of this.
dihedrals_models = featurizer.DihedralFeaturizer(types=["phi", "psi", "chi1", "chi2"]).transform([t_models])
x_models = tica_model.transform(dihedrals_models)

#Now plot on the slow MSM features found before.
plt.plot(x_models[0][:, 0], x_models[0][:, 1], 'o', markersize=5, label="ensembler models", color='white')
plt.title("Dihedral tICA Analysis - Abl")
plt.xlabel("Slowest Coordinate")
plt.ylabel("Second Slowest Coordinate")
plt.legend()

plt.hexbin(Xf[:, 0], Xf[:, 1], bins='log')

plt.savefig('fig_abl_ensembler.png')
