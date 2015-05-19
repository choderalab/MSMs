import os
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition, outlier

sysname = os.path.split(os.getcwd())[-1]
dt = 0.25
tica_lagtime = 400
regularization_string = "_012"

X0 = dataset.dataset("./tica/tica%d%s.h5" % (tica_lagtime, regularization_string))

slicer = featurizer.FirstSlicer(2)
X = slicer.transform(X0)
Xf = np.concatenate(X)

trimmer = outlier.OneClassSVMTrimmer(nu=0.00001, gamma=3.0)
%time trimmer.fit(X)


%time Xt = trimmer.transform(X)

Xf2 = np.concatenate(Xt)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')
plot(Xf2[:, 0], Xf2[:, 1], 'kx')
