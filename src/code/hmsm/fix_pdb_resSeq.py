import numpy as np
import pandas as pd
import mdtraj as md

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
