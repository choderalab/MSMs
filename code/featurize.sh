# NOTE: THIS USES THE SYNTAX OF LATEST PULL REQUEST OF MSMB
# Do dihedral featurization and tICA, making a semi-motivated GUESS for the features, lagtime, and gamma
msmb DihedralFeaturizer --trjs "trajectories/*.h5" --transformed dihedrals --types "phi" "psi" "chi1" "chi2" --out dihedrals/model.pkl
msmb tICA -i dihedrals/ --transformed tica -o tica.pkl --lag_time 50 --gamma 0.01 --n_components 20

msmb KMeans -i tica.h5 -o cluster.pkl -t cluster.h5 --n_clusters 50
msmb MarkovStateModel -i cluster.h5 -o msm.pkl

msmb tICA -i dihedrals/ --transformed tica1 -o tica1.pkl --lag_time 1 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica2 -o tica2.pkl --lag_time 2 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica10 -o tica10.pkl --lag_time 10 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica50 -o tica50.pkl --lag_time 50 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica100 -o tica100.pkl --lag_time 100 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica400 -o tica400.pkl --lag_time 400 --gamma 0.01 --n_components 20
