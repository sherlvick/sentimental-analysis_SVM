#!/usr/bin/python
import pandas as pd
import sys
import pickle
import os
import pathlib
from numpy import loadtxt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm

def training():
    np.random.seed(100)

    Corpus = pd.read_csv("Test.csv", encoding='utf-8-sig')

    my_data = Corpus['text']
    my_data1 = Corpus['label']

    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', svm.SVC(C=5, kernel='rbf', degree=3, gamma=0.5)),
    ])
    #a = "Training...'\n"
    my_clf = text_clf.fit(my_data, my_data1)
    filename = 'Amz_5000_.sav'
    pickle.dump(my_clf, open(filename, 'wb'))

    abs=os.path.exists('Amz_5000_.sav')
    lis = ["Successful : Training model Saved", "Oh Snap! something's wrong", str(len(Corpus))]
    if abs is True:
        del lis[1]
        return lis
    if abs is False:
        del lis[0]
        return lis


