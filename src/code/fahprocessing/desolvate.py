import shutil
import os
import mdtraj
import itertools

min_num_gen = 325
stride = 10

source_dir = "./PROJ8900/"
out_dir = "./nowater/"


traj = mdtraj.load("./system.pdb")
top, bonds = traj.top.to_dataframe()
top = top[top.chainID == 0]
atom_indices = top.index.values

top = traj.top

k = 0

for run in itertools.count():
    if not os.path.exists(source_dir + "/RUN%d/" % run):
        break

    for clone in itertools.count():
        if not os.path.exists(source_dir + "/RUN%d/CLONE%d/" % (run, clone)):
            break

        for gen in itertools.count():                 
            xtc_filename = source_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen)
            if not os.path.exists(xtc_filename):
                break
        print(run, clone)
        num_gen = gen
        if num_gen >= min_num_gen:
            for gen in range(num_gen):
                out_filename = out_dir + "/run%d-clone%d-frame-%.3d.xtc" % (run, clone, gen)
                if not os.path.exists(out_filename):
                    trj = mdtraj.load(source_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen), top=top, atom_indices=atom_indices, stride=stride)
                    trj.save(out_filename)
