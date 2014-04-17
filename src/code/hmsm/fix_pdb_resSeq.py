import numpy as np
import pandas as pd
import mdtraj as md


filename = "./system.subset.pdb"
t = md.load(filename)
top, bonds = t.top.to_dataframe()
top.resSeq += (310 - 43 - 1)  # Lose an extra 1 because PDB resSeq starts at 1, rather than zero
t._topology = md.Topology.from_dataframe(top, bonds)
t.save(filename)



"""
Somehow the resSeqs got set to be zero-indexed during one step in our conversion process.
Need to track this down later and raise an Issue
"""

for i in range(3):
    filename = "./PDB/State%d-mean.pdb" % i
    t = md.load(filename)
    top, bonds = t.top.to_dataframe()
    top.resSeq += (310 - 43)
    t._topology = md.Topology.from_dataframe(top, bonds)
    t.save(filename)





for i in range(800):
    filename = "./Trajectories/trj%d.h5" % i
    out_filename = "./NewTrajectories/trj%d.h5" % i
    print(filename)
    t = md.load(filename)
    top, bonds = t.top.to_dataframe()
    top.resSeq += (310 - 43)
    t._topology = md.Topology.from_dataframe(top, bonds)
    t.save(out_filename)
