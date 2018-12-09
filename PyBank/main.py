
# coding: utf-8

# In[1]:


import pandas as pd
import os

csv_path = '/Users/sarabi/Desktop/Class/UCBBEL201811DATA2/03-Python/Homework 3 Python/Instructions/PyBank/Resources/budget_data.csv'

read_csv = pd.read_csv(csv_path)

read_csv.head()


# In[2]:


read_csv.dtypes


# In[11]:


read_csv.shape


# In[7]:


unique_dates = read_csv['Date'].nunique()
#print(f"There are {unique_dates} months included in the dataset")


# In[10]:


Total = read_csv['Profit/Losses'].sum()
#print (Total)
#print(f"Total net amount of Profit/Losses over the entire periodis ${Total}.")


# In[14]:


Average = read_csv['Profit/Losses'].mean()
#print(Average)


# In[19]:


date_as_index = read_csv.set_index('Date')


# In[38]:


pL_delta = date_as_index.diff(periods=1)


# In[39]:


date_as_index['Change in P/L'] = pL_delta


# In[40]:


date_as_index.head()


# In[41]:


mean_of_pL = date_as_index['Change in P/L'].mean()


# In[42]:


#print(f"Average change in Profit/Losses between months over the entire period is {mean_of_pL}")


# In[72]:


max_pL = date_as_index['Change in P/L'].max()


# In[71]:


greaest_increase = date_as_index.loc[date_as_index['Change in P/L'] == 1926159, :]
date_greaest_increase = greaest_increase.index.values


# In[47]:


greaest_increase.head()


# In[75]:


min_pL = date_as_index['Change in P/L'].min()


# In[68]:


greaest_drop = date_as_index.loc[date_as_index['Change in P/L'] == -2196167.0, :]
date_greaest_drop =  greaest_drop.index.values


# In[51]:


#print(f"Greatest decrease in losses happened during Sep 2013.")


# In[76]:


print("Financial Analysis\n")
print("------------------\n")
print(f"Total Months: {unique_dates} \n")
print(f"Total: {Total} \n")
print(f"Average  Change: {mean_of_pL} \n")
print(f"Greatest Increase in Profits: {date_greaest_increase} , ${max_pL}  \n")
print(f"Greatest Decrease in Profits: {date_greaest_drop} , ${min_pL}  \n")




      

