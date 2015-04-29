import osprey.config, osprey.trials
import pandas as pd
import seaborn as sns

n_clusters_key = "clusterer__n_clusters"  # This will change depending on the type of clustering

config = osprey.config.Config("./config.yaml")

session = config.trials()
items = [cursor.to_dict() for cursor in session.query(osprey.trials.Trial).all()]
df = pd.DataFrame(items).set_index('id')

for key in df.iloc[0].parameters.keys():
    df[key] = df.parameters.map(lambda x: x[key])


X = df.pivot_table(index="slicer__first", columns=n_clusters_key, values="mean_test_score")
sns.heatmap(X, square=True, cmap='rainbow')

Y = df[["slicer__first", n_clusters_key, "mean_test_score"]].sort("mean_test_score")
Y

