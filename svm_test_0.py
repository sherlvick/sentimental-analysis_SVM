#!/usr/bin/python
import pandas as pd
import sys
import pickle
from numpy import loadtxt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm

np.random.seed(1000)


# df1 = pd.read_csv("out512.csv",encoding='utf-8-sig')

# getting input
def testing(anal1):
    my_test_data = []
    '''
    my_test_data1 = [ ]
    #input_string = input(anal1)
    #print (anal1)
    input_string1 = int(input("1.For GOOD - 1 " + '\n'"2.For BAD - 0 "+'\n'))

    if input_string1 == 1:
        my_test_data1.append("__label__2 ")
    elif input_string1 == 0:
        my_test_data1.append("__label__1 ")
    '''
    my_test_data.append(anal1)
    print(my_test_data, '\n')

    # my_test_data = df1['text']
    # my_test_data1 = df1['label']

    filename = 'Amz_5000_.sav'
    # pickle.dump(classifier, open(filename, 'wb'))
    my_clf = pickle.load(open(filename, 'rb'))

    print("Done! \nClassifying test set...")

    predicted = my_clf.predict(my_test_data)
    print(predicted, '\n')
    '''
    accuracy_var = np.mean(predicted == my_test_data1)*100
    print('accuracy is : ',np.mean(predicted == my_test_data1)*100)
    '''
    return predicted