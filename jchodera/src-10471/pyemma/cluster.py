#!/usr/bin/env python

import pyemma
import numpy as np
import mdtraj
import os

# Source directory
source_directory = '/cbio/jclab/projects/fah/fah-data/munged/no-solvent/10471'

################################################################################
# Load reference topology
################################################################################

print ('loading reference topology...')
reference_pdb_filename = 'reference.pdb'
reference_trajectory = os.path.join(source_directory, 'run0-clone0.h5')
traj = mdtraj.load(reference_trajectory)
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

import pyemma.coordinates
from glob import glob
trajectory_filenames = glob(os.path.join(source_directory, 'run0-clone94.h5'))
coordinates_source = pyemma.coordinates.source(trajectory_filenames, features=featurizer)
print("There are %d frames total in %d trajectories." % (coordinates_source.n_frames_total(), coordinates_source.number_of_trajectories()))

################################################################################
# Cluster
################################################################################

print('Clustering...')
generator_ratio = 100
nframes = coordinates_source.n_frames_total()
nstates = int(nframes / generator_ratio)
stride = 4
metric = 'minRMSD'
clustering = pyemma.coordinates.cluster_uniform_time(data=coordinates_source, k=nstates, stride=stride, metric=metric)
dtrajs = clustering.dtrajs

# Save discrete trajectories.
dtrajs_dir = 'dtrajs'
clustering.save_dtrajs(output_dir=dtrajs_dir, output_format='npy', extension='.npy')

################################################################################
# Make timescale plots
################################################################################

from pyemma import msm
from pyemma import plots

lags = [1,2,5,10]
its = msm.its(dtrajs, lags=lags, errors='bayes')
plots.plot_implied_timescales(its)

import matplotlib.pyplot as plt

plt.savefig('plot.pdf')


