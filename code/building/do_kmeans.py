"""
Build a GMM-MSM on tICA coordinates and plot the first two TICS with labels.
"""
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica.h5")
Xf = np.concatenate(X)

tica_model = utils.load("./tica.pkl")
dih_model = utils.load("./dihedrals/model.pkl")

n_first = 17
n_clusters = 9

slicer = featurizer.FirstSlicer(n_first)
clusterer = cluster.KMeans(n_clusters=n_clusters)
msm_model = msm.MarkovStateModel()

pipeline = make_pipeline(slicer, clusterer, msm_model)
s = pipeline.fit_transform(X)

p0 = make_pipeline(dih_model, tica_model, slicer)

trajectories = dataset.MDTrajDataset("./trajectories/*.h5")
selected_pairs_by_state = msm_model.draw_samples(s, 5)
samples = utils.map_drawn_samples(selected_pairs_by_state, trajectories)

for k, t in enumerate(samples):
    t.save("./pdbs/state%d.pdb" % k)


Y = p0.transform(samples)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')
plot(clusterer.cluster_centers_[:, 0], clusterer.cluster_centers_[:, 1], 'k+', markersize=12, markeredgewidth=3)
map(lambda k: annotate(k, xy=clusterer.cluster_centers_[k, 0:2], fontsize=24), arange(n_clusters))
#map(lambda y: plot(y[:, 0], y[:, 1], 'x', markersize=8, markeredgewidth=2), Y)
