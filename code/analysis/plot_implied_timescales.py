import pandas as pd
from msmbuilder import example_datasets, cluster, msm, featurizer, lumping, utils, dataset, decomposition

timestep = 0.25

df = {}
for tica_lagtime in [1, 2, 10, 50, 100, 400, 800, 1600]:
    tica_model = utils.load("./tica%d.pkl" % tica_lagtime)
    df[tica_lagtime * timestep] = tica_model.timescales_
    X = dataset.dataset("./tica%d.h5" % tica_lagtime)
    Xf = np.concatenate(X)
    figure()
    hexbin(Xf[:, 0], Xf[:, 1], bins='log')
    title("Lagtime %f ns " % (tica_lagtime * timestep))

df = pd.DataFrame(df)

figure()
df.ix[0].plot(style='o')
yscale('log')
xscale('log')
df.ix[0].plot()
