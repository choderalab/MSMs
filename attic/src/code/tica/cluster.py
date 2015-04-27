import itertools
import os

n_states_list = [10, 25, 50, 100, 200]
weighted_list = ["weighted", "unweighted"]
n_pairs_list = [100, 500, 1000, 2000, 4000]
n_tics_list = [5, 10, 25, 100]
algorithm_list = ["kmeans", "kcenters"]

for (n_states, weighted, n_pairs, n_tics, algorithm) in itertools.product(n_states_list, weighted_list, n_pairs_list, n_tics_list, algorithm_list):
    cmd = "Cluster.py -o %dpairs-%dtics-%dmeans-%s-%s/ tica -f tICAData%d-%s.h5 -n %d %s -k %d" % (n_pairs, n_tics, n_states, weighted, algorithm, n_pairs, weighted, n_tics, algorithm, n_states)
    print(cmd)
    os.system(cmd)
