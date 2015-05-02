# NOTE: THIS USES THE SYNTAX OF LATEST PULL REQUEST OF MSMB
# Do dihedral featurization and tICA, making a semi-motivated GUESS for the features, lagtime, and gamma
msmb DihedralFeaturizer --trjs "trajectories/*.h5" --transformed dihedrals --types "phi" "psi" "chi1" "chi2" --out dihedrals/model.pkl
msmb tICA -i dihedrals/ --transformed tica/tica -o tica/tica.pkl --lag_time 50 --gamma 0.01 --n_components 20

msmb KMeans -i tica.h5 -o cluster.pkl -t cluster.h5 --n_clusters 50
msmb MarkovStateModel -i cluster.h5 -o msm.pkl

msmb DihedralFeaturizer --trjs "trajectories/*.h5" --transformed dihedrals --types "phi" "psi" "chi1" "chi2" --out dihedrals/model.pkl
msmb tICA -i dihedrals/ --transformed tica/tica1 -o tica/tica1.pkl --lag_time 1 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica2 -o tica/tica2.pkl --lag_time 2 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica10 -o tica/tica10.pkl --lag_time 10 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica50 -o tica/tica50.pkl --lag_time 50 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica100 -o tica/tica100.pkl --lag_time 100 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica400 -o tica/tica400.pkl --lag_time 400 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica800 -o tica/tica800.pkl --lag_time 800 --gamma 0.01 --n_components 20
msmb tICA -i dihedrals/ --transformed tica/tica1600 -o tica/tica1600.pkl --lag_time 1600 --gamma 0.01 --n_components 20

#msmb tICA -i dihedrals/ --transformed tica/tica1600_5 -o tica/tica1600_5.pkl --lag_time 1600 --gamma 0.5 --n_components 20
