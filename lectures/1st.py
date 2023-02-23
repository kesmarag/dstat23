#!/usr/bin/env python
# coding: utf-8

# # Πρώτο Εργαστήριο - ΜΕΜ205 Περιγραφική Στατιστική
# 
# ## 1. Jupyter Notebook
# Το Jupyter Notebook είναι μια εφαρμογή ανοικτού κώδικα που μας επιτρέπει να δημιουργούμε και να μοιράζομαστε έγγραφα που περιέχουν κώδικα, μαθηματικές εξισώσεις, γραφήματα και κείμενα. 
# 
# 
# 
# ###  Γνωριμία με το jupyter notebook
# 
# #### Jupyter Modes
# - Command Mode
# - Edit Mode
#   - Markdown
#   - Code
# 
# #### Hello Jupyter Notebook - Markdown (latex)
#   
# $$ \sum_{i=1}^N x_i$$
#   
# https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes
#   
# #### Hello Jupyter Notebook - Python
# 1. Γράφουμε κωδικά **Python** (μία ή περισσότερες γραμμές).
# 2. Εκτελούμε τον κώδικα με **Shift + Enter**.

# In[ ]:





# # title 
# this is a line. 
# $$E= mc^2$$

# In[1]:


print("Hello, Jupyter Notebook!")


# ## 2. Εισαγωγή στο Pandas

# In[3]:


import pandas as pd
get_ipython().system('pip install pandas')


# ### 2.1. DataFrame

# In[4]:


data_1 = {
 'name': ['Nick', 'Helen', 'Steve', 'Mary', 'George'],
 'age': [20, 19, 22, 21, 20],
 'field': ['Mathematics', 'Physics', 'Literature', 'Mathematics', 'Chemistry'],
 'os': ['Windows', 'Windows', 'Windows', 'Linux', 'MacOS']
}


# In[ ]:





# In[5]:


data_1


# In[6]:


dataset_1 = pd.DataFrame(data_1)


# In[7]:


dataset_1


# In[8]:


dataset_1.info()


# In[10]:


data_2 = [
 ['Nick', 20, 'Mathematics', 'Windows'],
 ['Helen', 19, 'Physics', 'Windows'],
 ['Steve', 22, 'Literature', 'Windows'],
 ['Mary', 21, 'Mathematics', 'Linux'],
 ['George', 20, 'Chemistry', 'MacOS']
]


# In[11]:


dataset_2a = pd.DataFrame(data_2)


# In[12]:


dataset_2a


# In[13]:


var_names = ["name", 'age', 'field', 'os']


# In[14]:


dataset_2b = pd.DataFrame(data_2, columns=var_names)


# In[15]:


dataset_2b


# #### DataFrame και αρχεία .csv

# 1. Δημιουργούμε το αρχείο students.csv με έναν editor.
# 2. Γράφουμε το έξης περιεχόμενο και κάνουμε save.
# 
# ```
# name,age,field_of_stydy,os
# Nick,20,Mathematics,Windows
# Helen,19,Physics,Windows
# Steve,22,Literature,Windows
# Mary,21,Mathematics,Linux
# George,20,Chemistry,MacOS
# ```

# In[16]:


dataset_3a = pd.read_csv('students.csv')


# In[17]:


dataset_3a


# In[20]:


dataset_3a.index.values


# In[22]:


dataset_3a.loc[1]


# In[23]:


dataset_3a.iloc[0]


# In[24]:


dataset_3b = dataset_3a.set_index('name')


# In[25]:


dataset_3b


# In[26]:


dataset_3b.index.values


# In[27]:


dataset_3b.loc['Nick']


# In[28]:


dataset_3b.iloc[1]


# In[44]:


dataset_3c = pd.read_csv('./students.csv', index_col='name')


# In[43]:


dataset_3c


# In[36]:


dataset_3d = dataset_3c.drop('os', axis=1)


# In[37]:


dataset_3d


# In[38]:


dataset_3e = dataset_3c.drop('Nick')


# In[39]:


dataset_3e


# In[ ]:




