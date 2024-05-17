#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import seaborn as sns
from matplotlib import pyplot as plt
import os


# In[4]:


#importing data set of Vehicle information.
df = pd.read_csv("C:\\Users\\priya\\Downloads\\archive (3)\\data.csv")


# In[5]:


df.shape


# In[6]:


df.info


# In[7]:


df.describe


# In[8]:


df.isnull().sum()


# In[9]:


df


# In[10]:


df.Driven_Wheels


# In[11]:


df.Driven_Wheels.unique()


# In[12]:


#using aggregation function for counting total of Transmission Type individually.
df.groupby('Transmission Type')['Transmission Type'].agg('count')


# In[13]:


#for getting some values from starting.
df.head(3)


# In[14]:


#for getting some values from ending.
df.tail(3)


# In[15]:


#for removing null values.
df = df.dropna()


# In[16]:


df


# In[17]:


df.isnull().sum() #now there is no any null value in the dataset.


# In[18]:


#for calculating Engine HP value which is greater than 300
df[df['Engine HP'] > 300]


# In[19]:


#To find average of colums 
df['Engine Cylinders']/8084


# In[20]:


#Assining new variable
df_copy = df.copy()


# In[21]:


df_copy


# In[22]:


#for converting MSRP into million
df_copy['MSRP_in_million'] = df_copy['MSRP']/1000000


# In[23]:


df_copy.head()


# In[24]:


# finding vallue of Engine Cylinders which is less than 5 according to their index 
df[df['Engine Cylinders']<5].index


# In[25]:


#for neglating values of Engine Cylinders which is smaller than 4
df.drop(index=df[df['Engine Cylinders']<4].index)


# In[26]:


np.where(df['Engine Cylinders'] > 5, 'YES','NO')


# In[27]:


# for creating new column of Engine Cylinders_grt_5 
df['Engine Cylinders_grt_5'] = np.where(df['Engine Cylinders'] > 5, 'YES','NO')


# In[28]:


df


# In[29]:


#for finding outliers.
df.boxplot('Engine HP')
plt.show()


# In[30]:


# to find relation between 2 variables in the form of scatterplot and histograms.
sns.jointplot(x='MSRP_in_million',y='Engine HP',data=df_copy)
plt.show()


# In[31]:


# Histogram for single value i.e, Engine HP 
bar = df_copy['Engine HP']
plt.hist(bar)
plt.show()


# In[32]:


# For Checking skewness
sns.distplot(df_copy.MSRP_in_million)
plt.show()


# In[33]:


# Bar graph where, x-axis= engine hp and y-axis=No.of engines.
df_copy.groupby('Engine HP')['Engine HP'].count().plot.bar(color='purple')
plt.show()

