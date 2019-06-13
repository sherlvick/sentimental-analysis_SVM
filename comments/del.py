# importing pandas module
import nltk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("B07QLZQH29.csv")
#print(data.head())
#print(data[0:6])
out_dataframe = pd.DataFrame({'text' : data['body'],
                              'label' : data['rating']})
x = out_dataframe.copy()
c = 0
for i in x['label']:
    if i==5 or i==4:
        x['label'].iloc[c] = '__label__2 '
        c += 1
    elif i==1 or i==2:
        x['label'].iloc[c] = '__label__1 '
        c += 1
    elif i==3:
        x.drop(x.index[c],axis = 0,inplace = True)
        #c += 1
x.to_csv('Test1.csv',index=True, encoding='utf-8-sig')


'''
#handling missing cells
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan , strategy = 'constant' , fill_value = 'none')
imputer = imputer.fit(X[:,0:6])
X[:,0:6] = imputer.transform(X[:,0:6])
#print(imputer)
#print(X)
out_dataframe = pd.DataFrame(X)

#labelling index for existing column
out_dataframe.columns = ['rate','link','text']
out_dataframe['rate'] = out_dataframe[out_dataframe.columns[0]]
out_dataframe['link'] = out_dataframe[out_dataframe.columns[1]]
out_dataframe['text'] = out_dataframe[out_dataframe.columns[2]]

del out_dataframe['link']#deleting column by index

out_dataframe.to_csv('Test.csv',index=True, encoding='utf-8-sig')

'''