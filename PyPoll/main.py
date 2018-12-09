
# coding: utf-8

# In[1]:


import pandas as pd
import os

csv_path = '/Users/sarabi/Desktop/Class/UCBBEL201811DATA2/03-Python/Homework 3 Python/Instructions/PyPoll/Resources/election_data.csv'
read_csv = pd.read_csv(csv_path)
print(read_csv.shape)
read_csv.head()


# In[2]:


read_csv.dtypes


# In[3]:


votes_casts = read_csv['Voter ID'].nunique()
print(votes_casts)


# In[4]:


read_csv['Candidate'].value_counts()


# In[5]:


candidates = read_csv.groupby('Candidate').count()
candidates


# In[10]:


percentages = candidates["County"]/votes_casts
candidates["Percentages"] = percentages



# In[11]:


candidates.sort_values(['County'], ascending=[False],inplace=True)


# In[21]:


display_candidates = candidates[["Percentages","Voter ID"]]


# In[12]:


candidates_w = candidates.index.values


# In[13]:


winner = candidates_w[0]
winner


# In[15]:


candidates.head()


# In[24]:


print(f"Election Results \n")
print(f"------------------------- \n")
print(f"Total Votes: {votes_casts} \n")
print(f"------------------------- \n")
print(display_candidates.head())
print(f"------------------------- \n")
print(f"Winner: {winner}")
print(f"------------------------- \n")








