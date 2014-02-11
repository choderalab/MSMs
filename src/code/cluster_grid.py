import itertools
import os

n_ev_list = [3, 5, 10, 15, 20]
n_states_list = [100, 500, 1000]

for n_ev, n_states in itertools.product(n_ev_list, n_states_list):
    path = "%dmeans-%dev" % (n_states, n_ev)
    cmd = "Cluster.py -p ProjectInfo.yaml -o %s tica -f tICAData.h5 -n %d atompairs -a AtomPairs.dat kmeans -k %d" % (path, n_ev, n_states)
    os.system(cmd)
    cmd = "BuildMSM.py -l 1 -a %s/Assignments.h5 -o %s" % (path, path)
    os.system(cmd)
    cmd = "CalculateImpliedTimescales.py -l 1,40 -e 4 -p 4 -a %s/Assignments.Fixed.h5 -o %s/ImpliedTimescales.dat" % (path, path)
    os.system(cmd)
