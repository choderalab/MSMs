import networkx as nx
import numpy as np
import pandas as pd
import mdtraj as md
from mixtape.utils import iterobjects

input_filename = "./hmms.jsonlines"

models = list(iterobjects(input_filename))
df = pd.DataFrame(models)

x = df.ix[0]

T = np.array(x["transmat"])
p = np.array(x["populations"])


g = nx.from_numpy_matrix(T)
graph_pos = nx.spring_layout(g)

edge_labels=dict([((u,v,),"%.3f" % d['weight']) for u,v,d in g.edges(data=True) if u != v])

pos = nx.spring_layout(g)
nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
nx.draw(g, pos)
pylab.show()
