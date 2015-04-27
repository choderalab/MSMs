import mdtraj.io
import mdtraj as md
import numpy as np

ass = md.io.loadh("./Data100/Assignments.Fixed.h5")["arr_0"]

k = 0
for i in range(500):
    print(i)
    ind = np.where(ass[i] != -1)[0]
    if len(ind) <= 1:
        continue
    start = ind[0]
    end = ind[-1]
    trj = md.load("./Trajectories/trj%d.h5" % i)[start:end]
    trj.save("./goodtrimmed/Trajectories/trj%d.h5" % k)
    k += 1
