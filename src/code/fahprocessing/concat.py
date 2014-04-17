import os
import glob
import mdtraj as md

source_dir = "./nowater/"
out_dir = "./concat_apr15/"

top = md.load("./system.subset.pdb")

start_files = glob.glob(source_dir + "/run*-clone*-frame-000.xtc")
for filename in start_files:
    print(filename)
    filename = filename.split("/")[2]
    print(filename)
    run = int(filename.split("-")[0][3:])
    clone = int(filename.split("-")[1][5:])
    num_gens = len(glob.glob(source_dir + "/run%d-clone%d-frame-*.xtc" % (run, clone)))
    print(run, clone, num_gens)
    filenames = [source_dir + "/run%d-clone%d-frame-%.3d.xtc" % (run, clone, gen) for gen in range(num_gens)]
    out_filename = out_dir + "/run%d-clone%d.h5" % (run, clone)
    if not os.path.exists(out_filename):
        trj = md.load(filenames, top=top)
        trj.save(out_filename)
