#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset_unix.pkl", "rb") )
features = ["salary", "bonus"]
#data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()




#a = max([value["bonus"]
outlier =[]
for user, value in data_dict.items():
    if value["bonus"] != 'NaN':
        outlier.append((user, value["salary"]))


#max_value = max(outlier)
#print(max_value)
print(sorted(outlier,key=lambda x:x[1])[-3:])
#another way of doing
import pandas as pd
df = pd.DataFrame(data_dict)
print(df.head())
print(df.describe())
print(df.loc["salary",:].describe()) # here salary is object type
print(df.loc["salary",:].isnull().any())
print(df.loc["salary",:].str.isdigit())
df.loc["salary",:] = pd.to_numeric(df.loc["salary",:], errors="coerce")
#df.loc["bonus",:] = pd.to_numeric(df.loc["bonus",:],errors = "coerce")
### your code below
#print(df.loc["salary",:])
print(df.loc["salary",:].describe())  #here salary is float64 type

df = df.dropna(axis = 1)
print(df.loc["salary", :].astype("int").idxmax(axis=1))
