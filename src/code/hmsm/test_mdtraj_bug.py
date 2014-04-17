import numpy as np
import pandas as pd
import mdtraj as md

filename = "./test.h5"
filename2 = "./test2.h5"

t = md.load(filename)[0:3]

top, bonds = t.top.to_dataframe()
print(top[0:10])
top.resSeq += (310 - 43)
t._topology = md.Topology.from_dataframe(top, bonds)

top, bonds = t.top.to_dataframe()
print(top[0:10])


t.save(filename2)

t2 = md.load(filename2)
top, bonds = t2.top.to_dataframe()
print(top[0:10])
