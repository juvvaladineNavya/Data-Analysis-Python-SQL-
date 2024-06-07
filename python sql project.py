#!/usr/bin/env python
# coding: utf-8

# In[70]:


get_ipython().system('pip install kaggle')


# In[71]:


import sys
get_ipython().system('{sys.executable} -m pip install kaggle')


# In[72]:


import kaggle

get_ipython().system('kaggle datasets download ankitbansal06/retail-orders -f orders.csv')


# In[73]:


#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file


# In[74]:


#read data from the file
import pandas as pd
import numpy as np
df = pd.read_csv('orders.csv')


# In[75]:


#Accessing data frame
df.head()


# In[76]:


# accessing specific row
fifth_row = df.iloc[4:8]

print(fifth_row)


# In[77]:


df.iloc[:,4]


# In[78]:


df['Ship Mode'].unique()


# In[79]:


# handle null valuespresent in shipmode column

df['Ship Mode'].replace(['Not Available', 'unknown'],np.nan,inplace= True)


# In[80]:


df['Ship Mode'].unique()


# In[81]:


#rename columns names ..make them lower case and replace space with underscore
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')


# In[82]:


df.columns


# In[83]:


df.head(5)


# In[85]:


#derive new columns discount , sale price and profit

#df['discount']= df['list_price']*df['discount_percent']*0.01
#df['sale_price']= df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head()


# In[86]:


df.dtypes


# In[89]:


#convert order date from object data type to datetime

df['order_date'] = pd.to_datetime(df['order_date'],format = '%Y-%m-%d')


# In[92]:


df.dtypes


# In[ ]:


# dropping the columns

df.drop(columns=['discount_percent','list_price','cost_price'],inplace = True)


# In[95]:


df.head()


# In[97]:


import pandas as pd

from sqlalchemy import create_engine
import urllib.parse


host =  'localhost:3306'  # Unless different
user = 'root'        # Unless Different
password =urllib.parse.quote_plus('NavyaMysql@10a')
database =  'pythonsqlproject'


engine = create_engine('mysql+pymysql://' + user + ':' + password + "@" + host + "/" + database)


# In[102]:


df.to_sql('df_orders', con=engine, index=False, if_exists='append')


# In[101]:


#to check total number of rows
df.info()


# In[103]:


df


# In[104]:


df.to_csv('cleaned_orders.csv', index=False)


# In[ ]:




