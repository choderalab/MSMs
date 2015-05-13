"""
Build a dataframe with frame statistics.
"""

import collections
import glob
import mdtraj as md
import os
import pandas as pd

dt = 0.25

MIN_LENGTHS = collections.defaultdict(lambda : 1000 * 4)
MIN_LENGTHS[10478] = 500 * 4

projects = [10466, 10467, 10468, 10478]
names = {10466:"T4", 10467:"src", 10468:"abl", 10478:"setd8"}

data = []
for project in projects:
    path = "%s/%d/" % (os.environ["FAH_DATA_PATH"], project)
    min_length = MIN_LENGTHS[project]
    filenames = [filename for filename in glob.glob(path + "run*.h5")]
    lengths = [len(md.open(filename)) for filename in filenames]
    trimmed_lengths = [length for length in lengths if length > min_length]
    trimmed_ns = sum(trimmed_lengths) * dt
    n_traj = len(lengths)
    n_trimmed = len(trimmed_lengths)
    name = names[project]
    data.append(dict(project=project, frames=sum(lengths), trimmed_frames=sum(trimmed_lengths), trimmed_ns=trimmed_ns, n_trimmed=n_trimmed, n_traj=n_traj, name=name))

data = pd.DataFrame(data).set_index("project")

print data.to_html()
