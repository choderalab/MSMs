import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

timestep = 0.25

df = {}
for tica_lagtime in [1, 2, 10, 50, 100, 400, 800, 1600]:
    tica_model = utils.load("./tica/tica%d.pkl" % tica_lagtime)
    df[tica_lagtime * timestep] = tica_model.timescales_ * timestep

df = pd.DataFrame(df)

figure()
df.ix[0].plot(style='o')
df.ix[1].plot(style='o')
df.ix[2].plot(style='o')
yscale('log')
xscale('log')
df.ix[0].plot(style='b')
ylabel("Timescales [ns]")
xlabel("Lagtime [ns]")
title("Top 3 Implied Timescales")
savefig("implied_timescales.png", bbox_inches="tight")
