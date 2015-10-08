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
featurizer.add_backbone_torsions()

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
running_tica = coor.tica(lag=100, dim=100)

################################################################################
# Cluster
################################################################################

print('Clustering...')
clustering = coor.cluster_kmeans(k=100, stride=50)
coor.pipeline([coordinates_source,running_tica,clustering])

dtrajs = clustering.dtrajs

# Save discrete trajectories.
clustering.save_dtrajs(output_format='npy', extension='.npy')

################################################################################
# Make tics plot
################################################################################
tics = running_tica.get_output()[0]

z,x,y = np.histogram2d(tics[:,0],tics[:,1], bins=50)
F = -np.log(z+1)
extent = [x[0], x[-1], y[0], y[-1]]

plt.contourf(F.T, 50, cmap=plt.cm.hot, extent=extent)
plt.xlabel('tic1')
plt.ylabel('tic2')
plt.plot(clustering.clustercenters[:,0],clustering.clustercenters[:,1], linewidth=0, marker='o')

plt.savefig('tic1_tic2.pdf')

################################################################################
# Make eigenvalues plot
################################################################################

plt.clf()
eigenvalues = (running_tica.eigenvalues)**2

plt.plot(eigenvalues)

plt.savefig('eigenvalues.pdf')

################################################################################
# Make timescale plot
################################################################################

plt.clf()
lags = [1,2,5,10,20,50]
its = pyemma.msm.its(dtrajs, lags=lags, errors='bayes')
mplt.plot_implied_timescales(its)

plt.savefig('implied_timescales.pdf')


