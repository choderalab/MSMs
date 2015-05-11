These are initial passes of using do_gmm.py to make sense of MSMs of Src and Abl.

General procedure was:
```
 python make_symlinks.py 
msmb DihedralFeaturizer --transformed dihedrals --out ./dihedrals/model.pkl --types phi psi chi1 chi2 --trjs 'trajectories/*.h5'
 msmb tICA -i dihedrals --out tica1600 --transformed tica1600 --n_components 4 --lag_time 1600
mkdir pdbs
python do_gmm_SMH.py 
```
The dihedral and tica features already made can be found in:

/home/hansons/sims/src/MSMs/
/home/hansons/sims/abl/MSMs/

