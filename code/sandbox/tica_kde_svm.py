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

Xf0 = np.concatenate(X)
Xf = Xf0[::50]



hexbin(Xf0[:, 0], Xf0[:, 1], bins='log')

svm = OneClassSVM(nu=0.15)
svm.fit(Xf)


y = svm.predict(Xf)

plot(Xf[y==1][:, 0], Xf[y==1][:, 1], 'kx')
plot(Xf[y==-1][:, 0], Xf[y==-1][:, 1], 'wx')

clusterer = cluster.GMM(n_components=3)


yi = map(lambda x: svm.predict(x), X)


from msmbuilder.cluster import MultiSequenceClusterMixin, BaseEstimator
from sklearn.svm import OneClassSVM

class OneClassSVMTrimmer(MultiSequenceClusterMixin, OneClassSVM, BaseEstimator):
    def partial_transform(self, traj):
        """Featurize an MD trajectory into a vector space.

        Parameters
        ----------
        traj : mdtraj.Trajectory
            A molecular dynamics trajectory to featurize.

        Returns
        -------
        features : np.ndarray, dtype=float, shape=(n_samples, n_features)
            A featurized trajectory is a 2D array of shape
            `(length_of_trajectory x n_features)` where each `features[i]`
            vector is computed by applying the featurization function
            to the `i`th snapshot of the input trajectory.

        See Also
        --------
        transform : simultaneously featurize a collection of MD trajectories
        """
        pass

    def transform(self, traj_list, y=None):
        """Featurize a several trajectories.

        Parameters
        ----------
        traj_list : list(mdtraj.Trajectory)
            Trajectories to be featurized.

        Returns
        -------
        features : list(np.ndarray), length = len(traj_list)
            The featurized trajectories.  features[i] is the featurized
            version of traj_list[i] and has shape
            (n_samples_i, n_features)
        """
        return [self.partial_transform(traj) for traj in traj_list]


trimmer = OneClassSVMTrimmer()
trimmer.fit(X[0:10])
