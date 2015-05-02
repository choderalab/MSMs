"""
Make trajectory symlinks in local trajectories directory.
"""

import glob
import mdtraj as md
import os

PROJECT = 10466
MIN_LENGTH = 1000 * 4

PATH = "/home/kyleb/dat/fah_data/%d/" % PROJECT

filenames = [filename for filename in glob.glob(PATH + "run*.h5") if len(md.open(filename)) > MIN_LENGTH]

try:
    os.mkdir("./trajectories/")
except:
    pass

for filename in filenames:
    base_filename = os.path.split(filename)[1]
    out_filename = "./trajectories/%s" % (base_filename)
    if not os.path.exists(out_filename):
        os.symlink(filename, out_filename)
