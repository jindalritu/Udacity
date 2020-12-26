#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle, sys
#sys.path.append("../final_project/")
enron_data = pickle.load(open("../final_project/final_project_dataset_unix.pkl", "rb"))
print(len(enron_data.keys()))
print(enron_data["SKILLING JEFFREY K"])
#print(sum(len(v) for v in enron_data.values()))
#print(enron_data["SKILLING JEFFREY K"]["poi"])
print(len(enron_data["SKILLING JEFFREY K"].keys()))
s = 0
count = 0
for k, v in enron_data.items():
    if v["poi"] == 1:
        s = s + 1

print("count of poi ==1", s)


# total no. of POI
f = open("../final_project/poi_names.txt", "r")
for line in f:
    if line.startswith("("):
         word = line.split("\n")

         count = count + 1

print(count)

print(enron_data['PRENTICE JAMES']['total_stock_value'])
print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print(sorted(enron_data.keys()))

print(enron_data['LAY KENNETH L']['total_payments'])
print(enron_data['SKILLING JEFFREY K']['total_payments'])
print(enron_data['FASTOW ANDREW S']['total_payments'])


#count no. of  folks having quantified salary
count_sal = 0
count_email = 0
count_ppl = 0
count_poi = 0
for user in enron_data:
    if enron_data[user]['salary'] != 'NaN' :
        count_sal = count_sal + 1
    if enron_data[user]['email_address'] != 'NaN' :
        count_email = count_email + 1
    if enron_data[user]['total_payments'] == 'NaN' :
        count_ppl = count_ppl + 1
    if enron_data[user]['poi'] == 1:
        if enron_data[user]['total_payments'] == 'NaN':
           count_poi = count_poi + 1

print(count_sal)
print(count_email)
print(count_ppl)
per_ppl = float(count_ppl/len(enron_data.keys()))*100
print("percentage of ppl having nan value", per_ppl)
print("count of poi having nan", count_poi)

per_poi = float(count_poi/s) * 100
print("percentage of poi having nan value", per_poi)





