# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import sys, os, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from statistics import mean

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))
sys.path.append('data_project')

df = pd.read_csv('data_project/Iris.csv')

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

X = df.drop(columns=['Id', 'Species'])
y = df['Species']

forest_accuracy = []
tree_accuracy = []

for i in range(50):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5)
    forest = RandomForestClassifier(n_estimators=100)
    forest.fit(X_train, y_train)

    tree = DecisionTreeClassifier()
    tree.fit(X_train, y_train)

    forest_pred = forest.predict(X_test)
    tree_pred = tree.predict(X_test)

    forest_accuracy.append(accuracy_score(y_test, forest_pred))
    tree_accuracy.append(accuracy_score(y_test, tree_pred))
print(f'Forest: {mean(forest_accuracy)}\nTree {mean(tree_accuracy)}')
