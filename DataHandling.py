#Data Handling

import pandas as pd

items = pd.Series(['chairs','labels', 'tables'])
items

items = pd.Series(['chairs','labels', 'tables'],index=['OR 001','OR 002','OR 003'])
items

names = pd.Series(['Joe','Tom', 'Jane'])
names

dframe = {'Name':['Joe','Tom','Jane'],
          'Items':['Chair','labels','tables']
         }
purchases = pd.DataFrame(dframe)

purchases

mdata = pd.read_csv('Marketing.csv')

mdata.head()
mdata.head(10)
mdata.tail()
mdata.tail(2)
mdata.info()
mdata.head()
mdata.shape
