import numpy as np
import pandas as pd
import mdtraj as md

#os.system("hmsm  means-ghmm --filename hmms.jsonlines --lag-time 1 --n-states 3 -o out.csv --dir Trajectories --top system.subset.pdb --ext h5 -a AtomIndices.dat")

df = pd.read_csv("./out.csv")
for k, row in df.iterrows():
    trj = md.load(row["filename"])[row["index"]]
    trj.save("./PDB/State%d-mean.pdb" % row["state"])
