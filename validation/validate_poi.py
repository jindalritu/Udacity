#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit



data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = '../tools/python2_lesson13_keys_unix.pkl')
labels, features = targetFeatureSplit(data)
clf = tree.DecisionTreeClassifier()
clf.fit(features,labels)
print("accuracy:",clf.score(features, labels))



### it's all yours from here forward!  

features_train, features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)

print("accuracy:",clf.score(features_test,labels_test))

