#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    ## sort cleaned_data according to errors i.e 2
    ## discard the 10% point having highest error or consider the points having smallest error
    errors = (net_worths - predictions)**2

    cleaned_data = zip(ages, net_worths, errors )

    cleaned_data = sorted(cleaned_data, key=lambda x:x[2])
    print(cleaned_data)
    cleaned_data = cleaned_data[:81]


    #limit = int(len(net_worths) * 0.1)
    #res = zip(*cleaned_data)
    #print(str(res))
    return cleaned_data

