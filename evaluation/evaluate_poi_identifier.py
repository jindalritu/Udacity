#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn import tree
from sklearn import metrics
from sklearn.model_selection import train_test_split
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,sort_keys = "../tools/python2_lesson14_keys_unix.pkl")
labels, features = targetFeatureSplit(data)
features_train, features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.3,random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print("prediction:",pred)
print("labels:",labels_test)
print("no of poi in test set:", sum(pred))
#print len([e for e in features_test if e == 1.0])
print("total no. of poi",len(features_test))
pred1 = [0 for e in pred if e == 1 or e == 0]
print(pred1)
print("accuracy is", metrics.accuracy_score(pred1, labels_test))
print("precision:",metrics.precision_score(labels_test,pred))
print("recall:", metrics.recall_score(labels_test, pred))

### your code goes here 


