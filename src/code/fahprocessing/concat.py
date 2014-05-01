import os
import glob
import mdtraj as md

class Everything(object):
    def __contains__(self, other):
        return True

run_whitelist = [0, 102, 104, 107, 122, 134, 139, 143, 144, 151, 155, 184, 1, 23, 2, 33, 35, 37, 38, 39, 43, 58, 60, 62, 65, 70, 71, 73, 74, 77, 79, 83, 87, 99]
#run_whitelist = Everything()

source_dir = "./nowater/"
out_dir = "./concat_apr30_2/"

stride = 2

top = md.load("./system.subset.pdb")

start_files = glob.glob(source_dir + "/run*-clone*-frame-000.xtc")
for filename in start_files:
    print(filename)
    filename = filename.split("/")[2]
    print(filename)
    run = int(filename.split("-")[0][3:])
    if run not in run_whitelist:
        continue
    clone = int(filename.split("-")[1][5:])
    num_gens = len(glob.glob(source_dir + "/run%d-clone%d-frame-*.xtc" % (run, clone)))
    print(run, clone, num_gens)
    filenames = [source_dir + "/run%d-clone%d-frame-%.3d.xtc" % (run, clone, gen) for gen in range(num_gens)]
    out_filename = out_dir + "/run%d-clone%d.h5" % (run, clone)
    if not os.path.exists(out_filename):
        trj = md.load(filenames, top=top, stride=stride)
        trj.save(out_filename)
