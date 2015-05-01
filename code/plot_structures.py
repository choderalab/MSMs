import mdtraj as md
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

trj0 = md.load("traj-refine_implicit_md.xtc", top="topol-renumbered-implicit.pdb")
trj0 = trj0[0:50]

X = dataset.dataset("./tica.h5")
Xf = np.concatenate(X)

dih_model = utils.load("./dihedrals/model.pkl")
tica_model = utils.load("./tica.pkl")

pipeline = make_pipeline(dih_model, tica_model)
x0 = pipeline.transform([trj0])[0]

hexbin(Xf[:, 0], Xf[:, 1], bins='log')
plot(x0[:, 0], x0[:, 1], 'kx')
map(lambda k: annotate(k, xy=x0[k, 0:2], fontsize=14), arange(len(x0)))
