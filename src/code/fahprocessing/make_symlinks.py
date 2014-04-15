import shutil
import os
import tarfile
import itertools
import glob

source_dir = "/cbio/jclab/projects/kyleb/fah/8900/PROJ8900/"
staging_dir = "/cbio/jclab/projects/kyleb/fah/8900/longtraj_symlinks_PROJ8900/"
min_gens = 250

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

for run in itertools.count():
    if not os.path.exists(source_dir + "/RUN%d/" % run):
        break
    mkdir(staging_dir + "/RUN%d/" % run)
    for clone in itertools.count():
        if not os.path.exists(source_dir + "/RUN%d/CLONE%d/" % (run, clone)):
            break
        mkdir(staging_dir + "/RUN%d/CLONE%d/" % (run, clone))
        n_gens = len(glob.glob("%s/RUN%d/CLONE%d/frame-*.xtc" % (source_dir, run, clone)))
        print(run, clone, n_gens)
        if n_gens < min_gens:
            continue
        for gen in range(n_gens):
            in_filename = source_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen)
            out_filename = staging_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen)
            if not os.path.exists(in_filename):
                break
            if not os.path.exists(out_filename):
                print("Linking %s to %s." % (in_filename, out_filename))
                os.symlink(in_filename, out_filename)
                
