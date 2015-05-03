import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition
from sklearn.pipeline import make_pipeline
import mdtraj as md

tica_lagtime = 1600

trajectories = dataset.MDTrajDataset("./trajectories/*.h5")

for k, traj in enumerate(trajectories):
    print("*" * 80)
    print("Calculating shifts for trajectory %d" % k)
    print("*" * 80)
    shifts = md.compute_chemical_shifts(traj[::400], model="ppm")
    shifts.to_hdf("./shifts.h5", "trj%d" % k)
