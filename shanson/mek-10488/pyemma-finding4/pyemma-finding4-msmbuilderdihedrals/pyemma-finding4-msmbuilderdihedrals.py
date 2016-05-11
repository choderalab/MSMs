import matplotlib
matplotlib.use('Agg')

import pyemma
import pyemma.coordinates as coor
import pyemma.plots as mplt

import numpy as np
import mdtraj as md
import matplotlib.pyplot as plt

from msmbuilder.featurizer import DihedralFeaturizer

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
# Define msmbuilder to pyemma translator
################################################################################

def msmbuilder_to_pyemma(msmbuilder_dih_featurizer,trajectory):
    ''' accepts an msmbuilder.featurizer.DihedralFeaturizer object + a trajectory (containing the topology
    this featurizer will be applied to) and spits out an equivalent PyEMMA featurizer '''

    all_indices = []
    for dih_type in msmbuilder_dih_featurizer.types:
        func = getattr(md, 'compute_%s' % dih_type)
        indices,_ = func(trajectory)
        all_indices.append(indices)

    indices = np.vstack(all_indices)
    sincos = msmbuilder_dih_featurizer.sincos

    pyemma_feat = coor.featurizer(trajectory.topology)
    pyemma_feat.add_dihedrals(indices,cossin=sincos)

    return pyemma_feat

################################################################################
# Initialize featurizer
################################################################################

msmb_featurizer = DihedralFeaturizer(types=["phi", "psi", "chi1", "chi2"])

print('Initializing msmbuilder dihedrals featurizer...')
# create a PyEMMA featurizer
featurizer = msmbuilder_to_pyemma(msmb_featurizer,traj)

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
running_tica = coor.tica(lag=1600, dim=4)
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

#############################################################################
# find the input features with the strongest correlation with tics
##############################################################################
feature_descriptors = featurizer.describe()
tica_correlations = running_tica.feature_TIC_correlation
n_tics = tica_correlations.shape[1]
best_indicator_indices = [np.argmax(np.abs(tica_correlations[:,i])) for i in range(n_tics)]
best_indicators = [feature_descriptors[ind] for ind in best_indicator_indices]
best_indicators_corr = [tica_correlations[best_indicator_indices[i],i] for i in range(n_tics)]

print("These are the input features most strongly correlated with each tIC:")
for i in range(n_tics):
    print('\ttIC{0}: {1}\n\t\twith correlation of {2:.3f}'.format(i+1,best_indicators[i],best_indicators_corr[i]))

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

plt.savefig("pyemma-finding4-msmbuilderdihedrals-mek.png", bbox_inches="tight")
