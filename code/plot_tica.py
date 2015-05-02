from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

tica_lagtime = 1600

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica/tica%d.h5" % tica_lagtime)

tica_model = utils.load("./tica/tica%d.pkl" % tica_lagtime)

Xf = np.concatenate(X)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')

tica_model.timescales_

