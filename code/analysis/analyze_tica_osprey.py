import osprey.config, osprey.trials
import pandas as pd
import seaborn as sns

name = "tica"

key0 = "tica__gamma"

config = osprey.config.Config("./%s.yaml" % name)
df = config.to_dataframe()

plot(df.tica__gamma, df.mean_test_score, 'bo', label="test")
plot(df.tica__gamma, df.mean_train_score, 'ro', label="train")
xlabel(r"$\gamma$")
ylabel("Score")
legend(loc=0)

savefig("tica_cross_validation.png", bbox_inches="tight")
