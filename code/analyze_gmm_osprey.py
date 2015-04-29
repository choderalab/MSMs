import osprey.config, osprey.trials
import pandas as pd
import seaborn as sns

config = osprey.config.Config("./config.yaml")

session = config.trials()
items = [cursor.to_dict() for cursor in session.query(osprey.trials.Trial).all()]
df = pd.DataFrame(items).set_index('id')

for key in df.iloc[0].parameters.keys():
    df[key] = df.parameters.map(lambda x: x[key])


X = df.pivot_table(index="slicer__first", columns="gmm__n_components", values="mean_test_score")
sns.heatmap(X, square=True, cmap='rainbow')

Y = df[["slicer__first", "gmm__n_components", "mean_test_score"]].sort("mean_test_score")
Y

