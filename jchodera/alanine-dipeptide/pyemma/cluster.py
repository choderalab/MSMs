#!/usr/bin/env python

import pyemma
import numpy as np
import mdtraj
import time
import os

# Source directory
#source_directory = '/cbio/jclab/projects/fah/fah-data/munged-with-time/no-solvent/11406' # CK2
source_directory = '11406' # CK2

################################################################################
# Load reference topology
################################################################################

print('Creating HDF5 trajectories...')
from msmbuilder.example_datasets import AlanineDipeptide
trajs = AlanineDipeptide().get().trajectories
trajectory_filenames = []
for i,traj in enumerate(trajs):
    fname = 'data/alanine_{0}.h5'.format(i)
    trajectory_filenames.append(fname)
    traj.save_hdf5(fname)

print ('loading reference topology...')
reference_pdb_filename = 'protein.pdb'
traj[0].save_pdb(reference_pdb_filename)

################################################################################
# Initialize featurizer
################################################################################

print('Initializing featurizer...')
import pyemma.coordinates
featurizer = pyemma.coordinates.featurizer(reference_pdb_filename)
featurizer.add_all()

################################################################################
# Define coordinates source
################################################################################

print('Defining coordinates source...')
import pyemma.coordinates
from glob import glob
coordinates_source = pyemma.coordinates.source(trajectory_filenames, features=featurizer)
print("There are %d frames total in %d trajectories." % (coordinates_source.n_frames_total(), coordinates_source.number_of_trajectories()))

################################################################################
# Cluster
################################################################################

print('Clustering...')
generator_ratio = 200
nframes = coordinates_source.n_frames_total()
nstates = int(nframes / generator_ratio)
stride = 1
metric = 'minRMSD'
initial_time = time.time()
clustering = pyemma.coordinates.cluster_uniform_time(data=coordinates_source, k=nstates, stride=stride, metric=metric)
final_time = time.time()
elapsed_time = final_time - initial_time
print('Elapsed time %.3f s' % elapsed_time)

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
its = msm.its(dtrajs, lags=lags, errors='bayes')
plots.plot_implied_timescales(its)

plt.savefig('plot.pdf')


