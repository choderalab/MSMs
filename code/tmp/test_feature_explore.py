import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline
import mdtraj as md

tica_lagtime = 1600

trajectories = dataset.MDTrajDataset("./trajectories/*.h5")
t0 = trajectories[0][0]

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica/tica%d.h5" % tica_lagtime)
Xf = np.concatenate(X)

tica_model = utils.load("./tica/tica%d.pkl" % tica_lagtime)
dih_model = utils.load("./dihedrals/model.pkl")


d = dih_model.describe_features(t0)
d = pd.DataFrame(d)

d.ix[argsort(tica_model.eigenvectors_[:, 0])[0:5]]
d.ix[argsort(tica_model.eigenvectors_[:, 0])[-5:]]
