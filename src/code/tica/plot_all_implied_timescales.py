import pandas as pd
import itertools
import os

n_states_list = [10, 25, 50, 100, 200]
weighted_list = ["weighted", "unweighted"]
n_pairs_list = [100, 500, 1000, 2000, 4000]
n_tics_list = [5, 10, 25, 100]
algorithm_list = ["kmeans", "kcenters"]

data = []
for (n_states, weighted, n_pairs, n_tics, algorithm) in itertools.product(n_states_list, weighted_list, n_pairs_list, n_tics_list, algorithm_list):
    try:
        x, y = np.loadtxt("%dpairs-%dtics-%dmeans-%s-%s/ImpliedTimescales.dat" % (n_pairs, n_tics, n_states, weighted, algorithm)).T
    except:
        continue
    x = x.reshape((-1, 3))[:,0].astype('int')
    y = y.reshape((-1, 3))
    d = pd.DataFrame(y, index=x)
    timescales = d.max(1)
    for lag, time in timescales.iterkv():
        data.append([lag, time, n_states, weighted, n_pairs, n_tics, algorithm])

columns = ["lag", "timescale", "n_states", "weighted", "n_pairs", "n_tics", "algorithm"]
d = pd.DataFrame(data, columns=columns)
#q = d
#q = d[d.lag == 10]
#q[q.algorithm == "kmeans"] / q[q.algorithm == "kcenters"]


#d_kmeans = d[d.algorithm == "kmeans"].groupby(["lag", "n_states", "weighted", "n_pairs", "n_tics"]).mean()
#d_kcenters = d[d.algorithm == "kcenters"].groupby(["lag", "n_states", "weighted", "n_pairs", "n_tics"]).mean()
#rho = d_kmeans / d_kcenters
#rho = rho.reset_index()


for ((n_pairs, n_tics, n_states), grp1) in d.groupby(["n_pairs", "n_tics", "n_states"])[0:10]:
    plt.figure()
    plt.title("%s %s %s" % ((n_pairs, n_tics, n_states)))
    for ((weighted, algorithm), grp2) in grp1.groupby(["weighted", "algorithm"]):
        plt.plot(grp2.lag, grp2.timescale, 'o', label="%s-%s" % (weighted, algorithm))
    
for ((n_pairs, n_tics, n_states, weighted, algorithm), grp2) in grp1.groupby(["n_pairs", "n_tics", "n_states", "weighted", "algorithm"]):
    print(n_pairs, n_tics)
