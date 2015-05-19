import os
import osprey.config, osprey.trials
import pandas as pd
import seaborn as sns

name = "gmm"
#name = "kmeans"
sysname = os.path.split(os.path.split(os.getcwd())[0])[1]

key0 = "slicer__first"
key1 = {"gmm":"clusterer__n_components", "kmeans":"clusterer__n_clusters", "tica":"tica__gamma"}[name]

config = osprey.config.Config("./%s.yaml" % name)
df = config.to_dataframe()

figure()
X = df.pivot_table(index=key0, columns=key1, values="mean_test_score")
sns.heatmap(X, square=True, cmap='rainbow')
title("Test Score %s; best=%.3f" % (name, df.mean_test_score.max()))

savefig("./%s_%s_test.png" % (sysname, name), bbox_inches="tight")

figure()
X = df.pivot_table(index=key0, columns=key1, values="mean_train_score")
sns.heatmap(X, square=True, cmap='rainbow')
title("Train Score %s; best=%.3f" % (name, df.mean_train_score.max()))

savefig("./%s_%s_train.png" % (sysname, name), bbox_inches="tight")

Y = df[[key0, key1, "mean_test_score"]].sort("mean_test_score").dropna()
Y


