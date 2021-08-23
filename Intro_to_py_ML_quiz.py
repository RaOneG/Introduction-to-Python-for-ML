#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[7]:


# Question 1
A = [1,2,3,4,5,6]
B = [13, 21, 34]
A.extend(B)
A


# In[8]:


# Question 2
import numpy as np
np.identity(3)


# In[9]:


data = pd.read_csv('https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv')
data.head()


# In[10]:


# Question 3
data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean()


# In[11]:


# Question 4
std = data['fuel_mmbtu_per_unit'].describe()['std']
seventy_fifth = data['fuel_mmbtu_per_unit'].describe()['75%']
print(f'standard deviation = {std:.2f} and 75th percentile = {seventy_fifth:.2f}')


# In[12]:


# Question 5
skewness = data['fuel_qty_burned'].skew(skipna=True)
kurtosis = data['fuel_qty_burned'].kurtosis(skipna=True)
print(f'skewness = {skewness:.2f} and kurtosis = {kurtosis:.2f}')


# In[13]:


# Question 6
print(data.isnull().sum())
percentage = data.isnull().sum().max() / len(data) * 100
print(f'percentage = {percentage:.3f}')


# In[14]:


# Question 9
data_coal = data.loc[data['fuel_type_code_pudl'] == 'coal']
sum_cost_coal_by_year = data_coal.groupby('report_year')['fuel_cost_per_unit_burned'].sum()
year_1994 = sum_cost_coal_by_year[1994]
year_1998 = sum_cost_coal_by_year[1998]
percentage_change = ((year_1994 - year_1998)/year_1994)*100
print(f'percantage change = {percentage_change:.0f}%')


# In[15]:


# Question 10
data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()

