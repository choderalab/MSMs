"""
Make trajectory symlinks in local trajectories directory.
Looks for FAH data at the location given by environment variable
FAH_DATA_PATH
"""

import glob
import mdtraj as md
import os

RUN = None  # Set to either None or the run number of interest.
PROJECT = 10468
MIN_LENGTH = 1000 * 4  # kinase, T4
#MIN_LENGTH = 400 * 4  # setd8

PATH = "%s/%d/" % (os.environ["FAH_DATA_PATH"], PROJECT)

filenames = [filename for filename in glob.glob(PATH + "run*.h5") if len(md.open(filename)) > MIN_LENGTH]

try:
    os.mkdir("./trajectories/")
except:
    pass

for filename in filenames:
    if RUN is None or "run%d" % RUN in filename:
        base_filename = os.path.split(filename)[1]
        out_filename = "./trajectories/%s" % (base_filename)
        if not os.path.exists(out_filename):
            os.symlink(filename, out_filename)
