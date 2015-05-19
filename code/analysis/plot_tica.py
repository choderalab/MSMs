import os
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

sysname = os.path.split(os.getcwd())[-1]
dt = 0.25
tica_lagtime = 400
#regularization_string = ""
regularization_string = "_012"

dih = dataset.NumpyDirDataset("./dihedrals/")
X = dataset.dataset("./tica/tica%d%s.h5" % (tica_lagtime, regularization_string))

tica_model = utils.load("./tica/tica%d%s.pkl" % (tica_lagtime, regularization_string))

Xf = np.concatenate(X)

hexbin(Xf[:, 0], Xf[:, 1], bins='log')

tica_model.timescales_

title("tICA: lagtime %d (%.3f)" % (tica_lagtime, dt * tica_lagtime))
xlabel("Slowest tIC")
ylabel("Second Slowest tIC")
savefig("./%s_tica_lag%d%s.png" % (sysname, tica_lagtime, regularization_string), bbox_inches="tight")
