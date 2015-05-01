#!/bin/bash

msmb AtomIndices -d --heavy -p *.pdb -o AtomIndices.txt
msmb DihedralFeaturizer --transformed dihedral_features --types "phi" "psi" "chi2" --top *.pdb --trjs "*.h5"
msmb tICA -i dihedral_features --out tica_model --transformed tica_trajs --n_components 4

python make_msm_fig.py
