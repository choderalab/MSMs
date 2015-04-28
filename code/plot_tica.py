from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

Xf = np.concatenate(X)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')

clusterer = utils.load("./cluster.pkl")

hexbin(Xf[:, 0], Xf[:, 1], bins='log')
plot(clusterer.cluster_centers_[:, 0], clusterer.cluster_centers_[:, 1], 'kx', markersize=16)
