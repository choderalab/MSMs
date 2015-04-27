import shutil
import os
import tarfile
import itertools
import glob

class Everything(object):
    def __contains__(self, other):
        return True

run_whitelist = [0, 102, 104, 107, 122, 134, 139, 143, 144, 151, 155, 184, 1, 23, 2, 33, 35, 37, 38, 39, 43, 58, 60, 62, 65, 70, 71, 73, 74, 77, 79, 83, 87, 99]
#run_whitelist = Everything()

source_dir = "/cbio/jclab/projects/fah/fah-data/PROJ8900/"
staging_dir = "./PROJ8900/"
min_gen = 250

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

for run in itertools.count():
    if run not in run_whitelist:
        continue
    if not os.path.exists(source_dir + "/RUN%d/" % run):
        break
    mkdir(staging_dir + "/RUN%d/" % run)
    for clone in itertools.count():
        if not os.path.exists(source_dir + "/RUN%d/CLONE%d/" % (run, clone)):
            break
        mkdir(staging_dir + "/RUN%d/CLONE%d/" % (run, clone))

        n_gens = len(glob.glob("%s/RUN%d/CLONE%d/results-*.tar.bz2" % (source_dir, run, clone)))
        print(run, clone, n_gens)
        if n_gens < min_gen:
            continue

        for gen in itertools.count():
            in_filename = source_dir + "/RUN%d/CLONE%d/results-%.3d.tar.bz2" % (run, clone, gen)
            out_filename = staging_dir + "/RUN%d/CLONE%d/frame-%.3d.xtc" % (run, clone, gen)
            if not os.path.exists(in_filename):
                break
            if not os.path.exists(out_filename):
                print("Extracting %s to %s." % (in_filename, out_filename))
                archive = tarfile.open(in_filename, mode='r:bz2')
                archive.extract("positions.xtc")            
                shutil.move("positions.xtc", out_filename)
                
