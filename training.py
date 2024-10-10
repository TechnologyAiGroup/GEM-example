import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import GridSearchCV,cross_validate
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
import joblib

name  = "b20"
file_ = "msl10_1"

train = pd.read_csv(f'{name}/{file_}.csv')
target='y'
fault_col = 'fault'
x_columns = [x for x in train.columns if x not in [target, fault_col]]
X = train[x_columns]
y = train['y']


rf0 = HistGradientBoostingClassifier(
    class_weight='balanced',
    random_state=10
    )

rf0.fit(X,y)

joblib.dump(rf0, f'{name}/hgb.model')
