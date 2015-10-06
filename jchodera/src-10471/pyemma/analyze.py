#!/usr/bin/env python

import pyemma
import numpy as np
import mdtraj
import os

# Source directory
source_directory = '/cbio/jclab/projects/fah/fah-data/munged/no-solvent/10471'

################################################################################
# Load discrete trajectories
################################################################################

from pyemma import msm


################################################################################
# Make timescale plots
################################################################################

from pyemma import msm
from pyemma import plots

lags = [1,2,5,10,20,50,100,200]
its = msm.its(dtrajs, lags=lags)
plots.plot_implied_timescales(its)
