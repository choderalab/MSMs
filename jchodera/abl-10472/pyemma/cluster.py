#!/usr/bin/env python

import pyemma
import numpy as np
import mdtraj
import time
import os

# Source directory
source_directory = '/cbio/jclab/projects/fah/fah-data/munged3/no-solvent/10472' # Abl single

################################################################################
# Load reference topology
################################################################################

print ('loading reference topology...')
reference_pdb_filename = 'protein.pdb'
reference_trajectory = os.path.join(source_directory, 'run0-clone0.h5')
traj = mdtraj.load(reference_trajectory)
traj[0].save_pdb(reference_pdb_filename)

################################################################################
# Initialize featurizer
################################################################################

print('Initializing featurizer...')
import pyemma.coordinates
featurizer = pyemma.coordinates.featurizer(reference_pdb_filename)
#featurizer.add_all() # all atoms
featurizer.add_selection( featurizer.select_Backbone() )
print('Featurizer has %d features.' % featurizer.dimension())

################################################################################
# Define coordinates source
################################################################################

nskip = 40 # number of initial frames to skip

import pyemma.coordinates
from glob import glob
trajectory_filenames = glob(os.path.join(source_directory, 'run*-clone*.h5'))
coordinates_source = pyemma.coordinates.source(trajectory_filenames, features=featurizer)
print("There are %d frames total in %d trajectories." % (coordinates_source.n_frames_total(), coordinates_source.number_of_trajectories()))

################################################################################
# Cluster
################################################################################

print('Clustering...')
generator_ratio = 250
nframes = coordinates_source.n_frames_total()
nstates = int(nframes / generator_ratio)
stride = 1
metric = 'minRMSD'
initial_time = time.time()
clustering = pyemma.coordinates.cluster_uniform_time(data=coordinates_source, k=nstates, stride=stride, metric=metric)
#clustering = pyemma.coordinates.cluster_kmeans(data=coordinates_source, k=nstates, stride=stride, metric=metric, max_iter=10)
#clustering = pyemma.coordinates.cluster_mini_batch_kmeans(data=coordinates_source, batch_size=0.1, k=nstates, stride=stride, metric=metric, max_iter=10)
final_time = time.time()
elapsed_time = final_time - initial_time
print('Elapsed time %.3f s' % elapsed_time)

# Save cluster centers
np.save('clustercenters', clustering.clustercenters)

# Save discrete trajectories.
dtrajs = clustering.dtrajs
dtrajs_dir = 'dtrajs'
clustering.save_dtrajs(output_dir=dtrajs_dir, output_format='npy', extension='.npy')

################################################################################
# Make timescale plots
################################################################################

import matplotlib as mpl
mpl.use('Agg') # Don't use display
import matplotlib.pyplot as plt

from pyemma import msm
from pyemma import plots

lags = [1,2,5,10,20,50]
#its = msm.its(dtrajs, lags=lags, errors='bayes')
its = msm.its(dtrajs, lags=lags)
plots.plot_implied_timescales(its)

plt.savefig('plot.pdf')


