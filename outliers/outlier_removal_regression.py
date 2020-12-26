#!/usr/bin/python

import random
import numpy
import matplotlib.pyplot as plt
import pickle

from outlier_cleaner import outlierCleaner


### load up some practice data with outliers in it
ages = pickle.load( open("practice_outliers_ages_unix.pkl", "rb") )
net_worths = pickle.load( open("practice_outliers_net_worths_unix.pkl", "rb") )



### ages and net_worths need to be reshaped into 2D numpy arrays
### second argument of reshape command is a tuple of integers: (n_rows, n_columns)
### by convention, n_rows is the number of data points
### and n_columns is the number of features
ages       = numpy.reshape( numpy.array(ages), (len(ages), 1))
net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))
from sklearn.model_selection import train_test_split
ages_train, ages_test, net_worths_train, net_worths_test = train_test_split(ages, net_worths, test_size=0.1, random_state=42)

### fill in a regression here!  Name the regression object reg so that
### the plotting code below works, and you can see what your regression looks like


from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(ages_train, net_worths_train)
print(len(ages_train))
print("slope", reg.coef_)






try:
    plt.plot(ages, reg.predict(ages), color="blue")
except NameError:
    pass
plt.scatter(ages, net_worths)
plt.show()

### identify and remove the most outlier-y points
cleaned_data = []

predictions = reg.predict(ages_train)
cleaned_data = outlierCleaner(predictions, ages_train, net_worths_train )
"""""
age = numpy.array([e[0] for e in cleaned_d])

net = numpy.array([e[1] for e in cleaned_d])
age      = numpy.reshape( age,(-1,1))
net = numpy.reshape( age, (-1,1))

reg2 = linear_model.LinearRegression()
reg2.fit(age,  net)

"""""






### only run this code if cleaned_data is returning data


    #reg2 = linear_model.LinearRegression()
if len(cleaned_data) > 0:
    ages, net_worths, errors = zip(*cleaned_data)
    #print(str(ages))
    #print(str(net_worths))
    ages = numpy.reshape( numpy.array(ages), (len(ages), 1)).astype(numpy.float32)
    net_worths = numpy.reshape( numpy.array(net_worths), (len(net_worths), 1))

    try:
        reg2 = linear_model.LinearRegression()
        reg2.fit(ages, net_worths)
        plt.plot(ages, reg2.predict(ages), color="red")
    except NameError:
        print("you don't seem to have regression imported/created,")
        print("   or else your regression object isn't named reg")
        print( "   either way, only draw the scatter plot of the cleaned data")
        plt.scatter(ages, net_worths)
    plt.xlabel("ages")
    plt.ylabel("net worths")
    plt.show()


else:
    print("outlierCleaner() is returning an empty list, no refitting to be done")

print("new slope after removing outlier", reg2.coef_)

print("score after removing outlier",reg2.score(ages_test, net_worths_test))

