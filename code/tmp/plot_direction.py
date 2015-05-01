from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")
Xf = np.concatenate(X)

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

hexbin(Xf[:, 0], Xf[:, 1], bins='log')

for k, x in enumerate(X):
    a, b = np.array_split(x, 2)
    plot(a[:, 0], a[:, 1], 'k')
    plot(b[:, 0], b[:, 1], 'w')
