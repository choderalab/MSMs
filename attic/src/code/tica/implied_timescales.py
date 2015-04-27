import itertools
import os

n_states_list = [10, 25, 50, 100, 200]
weighted_list = ["weighted", "unweighted"]
n_pairs_list = [100, 500, 1000, 2000, 4000]
n_tics_list = [5, 10, 25, 100]
algorithm_list = ["kmeans", "kcenters"]

for (n_states, weighted, n_pairs, n_tics, algorithm) in itertools.product(n_states_list, weighted_list, n_pairs_list, n_tics_list, algorithm_list):
    cmd = "CalculateImpliedTimescales.py -l 1,125 -a %dpairs-%dtics-%dmeans-%s-%s/Assignments.h5 -o %dpairs-%dtics-%dmeans-%s-%s/ImpliedTimescales.dat -e 3 -p 2" % (n_pairs, n_tics, n_states, weighted, algorithm, n_pairs, n_tics, n_states, weighted, algorithm)
    print(cmd)
    os.system(cmd)
