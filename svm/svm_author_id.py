#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
from sklearn import svm
from sklearn import metrics

import math
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train1 = features_train[:math.floor(len(features_train)/100)]
labels_train1 = labels_train[:math.floor(len(labels_train)/100)]
#clf = svm.SVC(kernel="linear")
clf = svm.SVC(kernel="rbf", C=10000)

t0 = time()
clf.fit(features_train1, labels_train1)
print("training time is", round(time()-t0, 3), "sec")
t0 = time()
pred = clf.predict(features_test)
print("predicted value is", pred)

print("testing time is", round(time()-t0, 3), "sec")
#print(pred[10])
#print(pred[26])
#print(pred[50])
count_chris = 0
for i in pred:
    if i == 1:
        count_chris += 1

print("count", count_chris)



print("accuracy", metrics.accuracy_score(pred, labels_test))







""""
for C in [10.0, 100.0, 1000.0, 10000.0]:
    features_train, features_test, labels_train, labels_test = preprocess()
    features_train1 = features_train[:len(features_train) // 100]
    labels_train1 = labels_train[:len(labels_train) // 100]
    pred = my_svm(features_train1, features_test, labels_train1, labels_test, kernel="rbf", C=C, gamma='auto')
    print('/n/n')
    
"""




