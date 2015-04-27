import numpy as np
import pandas as pd
import mdtraj as md

trj0 = md.load("./system.subset.pdb")

top, bonds = trj0.top.to_dataframe()
i0 = np.where((top.name == "CB") & (top.resSeq == 310))[0][0]
i1 = np.where((top.name == "CB") & (top.resSeq == 409))[0][0]
indices = np.array([[i0, i1]])


n_traj = 131
all_distances = []
for i in range(n_traj):
    print(i)
    traj = md.load("./Trajectories/trj%d.h5" % i)
    d = md.geometry.compute_distances(traj, indices, periodic=False)
    all_distances.extend(d[:,0])
    
all_distances = np.array(all_distances)
