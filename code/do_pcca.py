from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

clusterer = utils.load("./cluster.pkl")
microstate_model = utils.load("./msm.pkl")

labels = microstate_model.transform(clusterer.labels_)

n_macrostates = 3

pcca = lumping.PCCAPlus.from_msm(microstate_model, n_macrostates=n_macrostates)
macrostate_model = msm.MarkovStateModel()
macrostate_model.fit(pcca.transform(labels))
