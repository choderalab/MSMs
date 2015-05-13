from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline

n_clusters = 2

trajectories = dataset.MDTrajDataset("./trajectories/*.h5")

clusterer = cluster.MiniBatchKMedoids(n_clusters=n_clusters, metric="rmsd")
clusterer.fit(trajectories)
