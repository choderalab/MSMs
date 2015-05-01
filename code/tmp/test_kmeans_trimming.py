from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")
Xf = np.concatenate(X)

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

n_first = 17
n_clusters = 50

slicer = featurizer.FirstSlicer(n_first)
clusterer = cluster.KMeans(n_clusters=n_clusters)
msm_model = msm.MarkovStateModel()

pipeline = make_pipeline(slicer, clusterer, msm_model)
s = pipeline.fit_transform(X)

