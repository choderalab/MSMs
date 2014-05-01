import shutil
import os
import mdtraj
import itertools

class Everything(object):
    def __contains__(self, other):
        return True

run_whitelist = [0, 102, 104, 107, 122, 134, 139, 143, 144, 151, 155, 184, 1, 23, 2, 33, 35, 37, 38, 39, 43, 58, 60, 62, 65, 70, 71, 73, 74, 77, 79, 83, 87, 99]
#run_whitelist = Everything()

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
    if run not in run_whitelist:
        continue
    
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
