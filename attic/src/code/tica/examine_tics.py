import itertools
import numpy as np
import mdtraj as md
import msmbuilder as msmb

n_traj = 735
tica = msmb.reduce.tICA.load("./tICAData.h5")

tics = []
for filename in ["./Trajectories/trj%d.h5" % i for i in range(n_traj)]:
    print(filename)
    trj = md.load(filename)
    tics.append(tica.project(trajectory=trj, which=arange(100)))

