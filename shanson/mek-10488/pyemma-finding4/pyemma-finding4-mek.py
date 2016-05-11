import matplotlib
matplotlib.use('Agg')

import pyemma
import pyemma.coordinates as coor
import pyemma.plots as mplt

import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

from glob import glob
import os

# Source directory for MEK simulations
source_directory = '/cbio/jclab/projects/fah/fah-data/munged/no-solvent/10488'

################################################################################
# Load reference topology
################################################################################

print ('loading reference topology...')
reference_pdb_filename = 'reference.pdb'
reference_trajectory = os.path.join(source_directory, 'run0-clone0.h5')
traj = md.load(reference_trajectory)
traj[0].save_pdb(reference_pdb_filename)

################################################################################
# Initialize featurizer
################################################################################

print('Initializing backbone torsions featurizer...')
featurizer = coor.featurizer(reference_pdb_filename)
featurizer.add_chi1_torsions()

################################################################################
# Define coordinates source
################################################################################

trajectory_files = glob(os.path.join(source_directory, '*0.h5'))
coordinates_source = coor.source(trajectory_files,featurizer)
print("There are %d frames total in %d trajectories." % (coordinates_source.n_frames_total(), coordinates_source.number_of_trajectories()))

################################################################################
# Do tICA
################################################################################

print('tICA...')
running_tica = coor.tica(lag=1600, dim=100)
coor.pipeline([coordinates_source,running_tica])

################################################################################
# Make eigenvalues plot
################################################################################

plt.clf()
eigenvalues = (running_tica.eigenvalues)**2

sum_eigenvalues = np.sum(eigenvalues[0:2])

print "This is the sum of the first two eigenvalues: %s." % sum_eigenvalues

plt.plot(eigenvalues)
plt.xlim(0,4)
plt.ylim(0,1.2)
plt.annotate('sum first two: %s.' % sum_eigenvalues, xy=(0.25,0.1))
plt.savefig('pyemma-eigenvalues.png')

################################################################################
# Make tics plot
################################################################################

plt.clf()
tics = running_tica.get_output()
tics = np.vstack(tics)

plt.hexbin(tics[:,0], tics[:, 1], bins='log')
plt.title("Dihedral tICA Analysis")
plt.xlabel("tic1")
plt.ylabel("tic2")

plt.savefig("pyemma-finding4-mek.png", bbox_inches="tight")
