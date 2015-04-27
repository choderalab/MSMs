hmsm save-featurizer --top system.subset.pdb -d AtomPairs.dat -f atompairs.pkl 
hmsm fit-ghmm -k 3 -l 1 --dir Trajectories/ --ext h5 --top system.subset.pdb --featurizer atompairs.pkl --out atompairs.jsonlines
hmsm means-ghmm --featurizer atompairs.pkl --dir Trajectories/ --top system.subset.pdb  --ext h5 --filename atompairs.jsonlines --n-states 3 --lag-time 1 --o samples-atompairs.csv


hmsm save-featurizer --top system.subset.pdb -a AtomIndices.dat -f atomindices.pkl 
hmsm fit-ghmm -k 3 -l 1 --dir Trajectories/ --ext h5 --top system.subset.pdb --featurizer atomindices.pkl --out atomindices.jsonlines
hmsm means-ghmm --featurizer atomindices.pkl --dir Trajectories/ --top system.subset.pdb  --ext h5 --filename atomindices.jsonlines --n-states 3 --lag-time 1 --o samples-atomindices.csv


#hmsm save-featurizer --top system.subset.pdb -d AtomPairs.dat -f atompairs.pkl 
hmsm fit-ghmm -k 3 -l 1 --dir Trajectories/ --ext h5 --top system.subset.pdb --featurizer tica.pkl --out tica.jsonlines
hmsm means-ghmm --featurizer tica.pkl --dir Trajectories/ --top system.subset.pdb  --ext h5 --filename tica.jsonlines --n-states 3 --lag-time 1 --o samples-tica.csv


hmsm fit-ghmm -k 2 -l 1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60 --dir Trajectories/ --ext h5 --top system.subset.pdb --featurizer atompairs.pkl --out atompairs.jsonlines
hmsm means-ghmm --featurizer atompairs.pkl --dir Trajectories/ --top system.subset.pdb  --ext h5 --filename atompairs2.jsonlines --n-states 2 --lag-time 1 --o samples-atompairs.csv


hmsm fit-ghmm -k 2 -l 1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,55,60 --dir Trajectories/ --ext h5 --top system.subset.pdb --featurizer tica.pkl --out tica.jsonlines
