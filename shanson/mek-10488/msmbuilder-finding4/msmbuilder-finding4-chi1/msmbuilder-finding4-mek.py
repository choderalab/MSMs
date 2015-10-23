import matplotlib
matplotlib.use('Agg')

from msmbuilder.dataset import dataset
from msmbuilder import msm, featurizer, utils, decomposition

import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

from glob import glob
import os

# Source directory for MEK simulations
source_directory = '/cbio/jclab/projects/fah/fah-data/munged/no-solvent/10488'

################################################################################
# Load trajectories
################################################################################

print ('loading trajectories...')
filenames = glob(os.path.join(source_directory, '*0.h5'))
trajectories = [md.load(filename) for filename in filenames]
print "We are analyzing %s trajectories." % len(trajectories)

################################################################################
# initialize dihedral and tICA features
################################################################################

print('initializing dihedral and tICA features...')
dihedrals = featurizer.DihedralFeaturizer(types=["chi1"]).transform(trajectories)
print "We are using %s chi1 dihedral features." % len(dihedrals[0])
tica = decomposition.tICA(n_components = 4,lag_time= 1600)
X = tica.fit_transform(dihedrals)

################################################################################
# Make eigenvalues plot
################################################################################

plt.clf()
eigenvalues = (tica.eigenvalues_)**2

sum_eigenvalues = np.sum(eigenvalues[0:2])

print "This is the sum of the first two eigenvalues: %s." % sum_eigenvalues

plt.plot(eigenvalues)
plt.xlim(0,4)
plt.ylim(0,1.2)
plt.annotate('sum first two: %s.' % sum_eigenvalues, xy=(0.25,0.1))
plt.savefig('msmb-eigenvalues.png')

################################################################################
# plot first two tics
################################################################################

plt.clf()

Xf = np.concatenate(X)
plt.hexbin(Xf[:,0], Xf[:, 1], bins='log')
plt.title("Dihedral tICA Analysis")
plt.xlabel("tic 1")
plt.ylabel("tic 2")

plt.savefig("msmbuilder-finding4-mek.png", bbox_inches="tight")

