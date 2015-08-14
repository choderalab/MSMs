# import libraries

import matplotlib
matplotlib.use('Agg')

import mdtraj as md
import matplotlib.pyplot as plt
import numpy as np

from msmbuilder import dataset

import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")

# load trajectories

trajectories = dataset.MDTrajDataset("trajectories/*.h5")

# define empty lists

difference = []
rmsd = []

for traj in trajectories:

    #append hydrogen bond distance for all frames in all trajectories to list 'difference'

    k295e310 = md.compute_contacts(traj, [[28,43]])
    e310r409 = md.compute_contacts(traj, [[43,142]])
    difference.append(e310r409[0] - k295e310[0])

    #append RMSD of activation loop from 2SRC structure for all frames in all trajectories to list 'rmsd'

    SRC2 = md.load("../reference-structures/SRC_2SRC_A.pdb")

    Activation_Loop_SRC2 = [atom.index for atom in SRC2.topology.atoms if (138 <= atom.residue.index <= 158)]
    Activation_Loop_Src = [atom.index for atom in traj.topology.atoms if (138 <= atom.residue.index <= 158)]

    SRC2.atom_slice(Activation_Loop_SRC2) 
    traj.atom_slice(Activation_Loop_Src)

    rmsd.append(md.rmsd(traj,SRC2,frame=0))

#flatten these lists of arrays

flattened_difference = np.asarray([val for sublist in difference for val in sublist])
flattened_rmsd = np.asarray([val for sublist in rmsd for val in sublist])

#plot

sns.kdeplot(flattened_rmsd,flattened_difference[:,0],shade=True,log=True)
plt.xlabel('RMSD Activation Loop (nm)')
plt.ylabel('d(E310R409) - d(K295-E310) (nm)')

plt.savefig('plot_conf_src_all.png')
