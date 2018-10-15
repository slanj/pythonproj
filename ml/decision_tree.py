import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

'''
Imagine that you are a medical researcher compiling data for a study.
You have collected data about a set of patients,
all of whom suffered from the same illness.
During their course of treatment, each patient responded
to one of 5 medications, Drug A, Drug B, Drug c, Drug x and y.
'''

my_data = pd.read_csv("drug200.csv", delimiter=",")

X = my_data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']].values
# print(X[0:5])

'''
As you may figure out, some features in this dataset are categorical
such as Sex or BP.
Unfortunately, Sklearn Decision Trees do not handle categorical variables.
But still we can convert these features to numerical values.
pandas.get_dummies() Convert categorical variable into dummy/indicator variables.
'''

from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit(['LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit(['NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3])

# print(X[0:5])

y = my_data["Drug"]

from sklearn.model_selection import train_test_split
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, y, test_size=0.3, random_state=3)

# We will first create an instance of the DecisionTreeClassifier called drugTree.
# Inside of the classifier, specify criterion="entropy"
# so we can see the information gain of each node.

drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree.fit(X_trainset,y_trainset)

predTree = drugTree.predict(X_testset)

from sklearn import metrics
import matplotlib.pyplot as plt
print("DecisionTrees's Accuracy: ", metrics.accuracy_score(y_testset, predTree))

guessed = y_testset == predTree
intercept = y_testset[guessed]
score = len(intercept) / len(y_testset)

print("Accuracy calculated by hand: ", score)

# Lets visualize the tree
# from sklearn.externals.six import StringIO
# import pydotplus
# import matplotlib.image as mpimg
# from sklearn import tree

# dot_data = StringIO()
# filename = "drugtree.png"
# featureNames = my_data.columns[0:5]
# targetNames = my_data["Drug"].unique().tolist()
# out=tree.export_graphviz(drugTree,feature_names=featureNames, out_file=dot_data, class_names= np.unique(y_trainset), filled=True,  special_characters=True,rotate=False)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# graph.write_png(filename)
# img = mpimg.imread(filename)
# plt.figure(figsize=(100, 200))
# plt.imshow(img,interpolation='nearest')