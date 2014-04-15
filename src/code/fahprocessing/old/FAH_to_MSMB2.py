raise(Exception("This script is obsolete!"))

import shutil
import os
import tarfile
import tempfile
import mdtraj
import itertools
import pandas as pd

min_num_gen = 50

source_dir = "/cbio/jclab/projects/fah/fah-data/PROJ8900/"
destination_dir = "./Trajectories/"

provenance_file = file("./provenance.csv", 'a')

traj = mdtraj.load("./system.pdb")
top, bonds = traj.top.to_dataframe()
top = top[top.chainID == 0]
atom_indices = top.index.values

k = 0

for run in itertools.count():
    if not os.path.exists(source_dir + "/RUN%d/" % run):
        break

    for clone in itertools.count():
        if not os.path.exists(source_dir + "/RUN%d/CLONE%d/" % (run, clone)):
            break

        for gen in itertools.count():                 
            xtc_filename = staging_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen)
            if not os.path.exists(xtc_filename):
                break

        num_gen = gen
        traj = mdtraj.load([source_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen) for gen in range(num_gen)], top="./system.pdb", atom_indices=atom_indices)
        
        if num_gen >= min_num_gen:
            out_filename = destination_dir + "/trj%d.lh5" % k
            traj.save_legacy_hdf(out_filename)

            provenance = pd.DataFrame([[run, clone, num_gen]], index=[k], columns=["run", "clone", "num_gen"])
            provenance.to_csv(provenance_file, header=False)
            provenance_file.flush()
            
            k += 1    
