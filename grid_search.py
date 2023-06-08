import numpy as np
import pandas as pd

from sklearn import ensemble
from sklearn import metrics
from sklearn import model_selection
from sklearn import decomposition
from sklearn import preprocessing
from sklearn import pipeline


df = pd.read_csv("/home/kalikali/Downloads/train.csv")
X = df.drop("price_range", axis = 1).values
y = df.price_range.values

classifier = ensemble.RandomForestClassifier(n_jobs = -1)
param_grid = {
    "n_estimators" : [100, 200, 500, 1000],
    "max_depth" : [3, 5, 7],
    "criterion" : ["gini", "entropy"]
}

model = model_selection.GridSearchCV(
    estimator=classifier,
    param_grid=param_grid,
    scoring="accuracy",
    verbose = 10,
    n_jobs = 1,
    cv = 5
)

model.fit(X, y)

print(model.best_score_)
print(model.best_estimator_.get_params())