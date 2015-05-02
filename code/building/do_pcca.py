import scipy.spatial
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

clusterer = utils.load("./cluster.pkl")
microstate_model = utils.load("./msm.pkl")

labels = microstate_model.transform(clusterer.labels_)

n_macrostates = 5

pcca = lumping.PCCAPlus.from_msm(microstate_model, n_macrostates=n_macrostates)
macrostate_model = msm.MarkovStateModel()
macrostate_model.fit(pcca.transform(labels))


pipeline = make_pipeline(clusterer, microstate_model, pcca, macrostate_model)
s  = pipeline.transform(X)
sf = np.concatenate(s)
Xf = np.concatenate(X)


for i in range(n_macrostates):
    figure()
    f = hexbin(Xf[:, 0], Xf[:, 1], bins='log')
    hull = scipy.spatial.ConvexHull(Xf[sf == i, 0:2])
    scipy.spatial.convex_hull_plot_2d(hull, ax=f.axes)
    xlim(Xf[:, 0].min(), Xf[:, 0].max())
    ylim(Xf[:, 1].min(), Xf[:, 1].max())
