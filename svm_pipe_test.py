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
from sklearn.metrics import confusion_matrix
import pylab as plt

def testing1(anal):
    np.random.seed(1000)
    df1 = pd.read_csv(anal, encoding='utf-8-sig')

    '''#getting input
    my_test_data = [ ]
    my_test_data1 = [ ]
    n = int(input("Enter no. of reviews:"))
    for i in range(n):
        input_string = str(input("Enter reviews for products :"+'\n'
                        "1.Novel"+'\n'
                        "2.Tablet"+'\n'
                        "3.Movie"+'\n'
                        "4.Cloth"+'\n'
                        "5.Phone"+'\n'
                        "F**k off ;-)"+'\n'
                        "Think of your own..."))
        input_string1 = str(input("Please enter your true sentiment for above reviews:" + '\n'
                                                                                  "1.For GOOD - __label__2 " + '\n'
                                                                                                       "2.For BAD - __label__1 "+'\n'))
    my_test_data.append(input_string)
    my_test_data1.append(input_string1)
    print(my_test_data,'\n')'''

    my_test_data = df1['text']
    my_test_data1 = df1['label']

    filename = 'Amz_5000_.sav'
    # pickle.dump(classifier, open(filename, 'wb'))
    my_clf = pickle.load(open(filename, 'rb'))

    print("Done! \nClassifying test set...")

    predicted = my_clf.predict(my_test_data)
    print(predicted, '\n')
    accuracy_answer = np.mean(predicted == my_test_data1) * 100
    print('accuracy is : ', accuracy_answer, '%')
    lis = [accuracy_answer,my_test_data1,predicted]
    return lis

def conf_matrix(a,b):
    labels = ['__label__1 ', '__label__2 ']
    cm = confusion_matrix(a, b, labels)
    print(cm)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(cm)
    plt.title('Confusion matrix of the classifier')
    fig.colorbar(cax)
    ax.set_xticklabels([''] + labels)
    ax.set_yticklabels([''] + labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    lis1 = [cm,plt]
    return lis1

