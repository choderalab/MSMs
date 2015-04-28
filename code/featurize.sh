# NOTE: THIS USES THE SYNTAX OF LATEST PULL REQUEST OF MSMB
# Do dihedral featurization and tICA, making a semi-motivated GUESS for the features, lagtime, and gamma
msmb DihedralFeaturizer --trjs "trajectories/*.h5" --transformed dihedrals --types "phi" "psi" "chi1" "chi2" --out dihedrals/model.pkl
msmb tICA -i dihedrals/ --transformed tica -o tica.pkl --lag_time 50 --gamma 0.01 --n_components 10

msmb KMeans -i tica.h5 -o cluster.pkl -t cluster.h5 --n_clusters 50
msmb MarkovStateModel -i cluster.h5 -o msm.pkl
