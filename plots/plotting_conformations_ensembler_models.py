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

#Load trajectory with ensembler models
t_models = md.load("../ensembler-models/traj-refine_implicit_md.xtc", top = "../ensembler-models/topol-renumbered-implicit.pdb")

#define 'difference' as hydrogen bond distance

k295e310 = md.compute_contacts(t_models, [[28,43]])
e310r409 = md.compute_contacts(t_models, [[43,142]])
difference = e310r409[0] - k295e310[0]

#define 'rmsd' as RMSD of activation loop from 2SRC structure

SRC2 = md.load("../reference-structures/SRC_2SRC_A.pdb")

Activation_Loop_SRC2 = [atom.index for atom in SRC2.topology.atoms if (138 <= atom.residue.index <= 158)]
Activation_Loop_Src = [atom.index for atom in t_models.topology.atoms if (138 <= atom.residue.index <= 158)]

SRC2.atom_slice(Activation_Loop_SRC2)
t_models.atom_slice(Activation_Loop_Src)

difference = difference[:,0]

rmsd = md.rmsd(t_models,SRC2,frame=0)

#plot
#plt.plot(rmsd, difference, 'o', markersize=5, label="ensembler models", color='black')
sns.kdeplot(rmsd,difference,shade=True,log=True)
plt.xlabel('RMSD Activation Loop (nm)')
plt.ylabel('d(E310-R409) - d(K295-E310) (nm)')
plt.ylim(-2,2)
plt.xlim(0.3,1.0)

plt.savefig('plot_conf_src_ensembler_density.png')
