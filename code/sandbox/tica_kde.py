from sklearn.covariance import EllipticEnvelope
import sklearn.neighbors
from sklearn.svm import OneClassSVM
import os
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

sysname = os.path.split(os.getcwd())[-1]
dt = 0.25
tica_lagtime = 400
regularization_string = "_012"

X0 = dataset.dataset("./tica/tica%d%s.h5" % (tica_lagtime, regularization_string))

slicer = featurizer.FirstSlicer(2)
X = slicer.transform(X0)

Xf = np.concatenate(X)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')




Xf_train = Xf[::100]

svm = OneClassSVM()
svm.fit(Xf_train)





kde = sklearn.neighbors.kde.KernelDensity()
kde.fit(Xf)

scores = map(lambda x: kde.score(x), X)



ind0 = (Xf[:, 0] > 0.75) & (Xf[:, 0] < 0.92) & (Xf[:, 1] > 0.63) & (Xf[:, 1] < 1.10)
Xf0 = Xf[ind0]
Xf0.shape

kde0 = sklearn.neighbors.kde.KernelDensity()
kde0.fit(Xf0)

scores = map(lambda x: kde0.score(x), X)

clusterer = cluster.GMM(n_components=3)
clusterer.fit(X)
clusterer.means_



svm = OneClassSVM()
svm.fit(Xf)

env = EllipticEnvelope()
env.fit(Xf)
