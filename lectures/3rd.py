#!/usr/bin/env python
# coding: utf-8

# # Πείραμα μέτρησης ταχύτητας του φωτός

# In[1]:


import pandas as pd


# In[2]:


L = [28, 26, 33, 24, 34,-44, 27, 16, 40, -2, 29,
     22, 24, 21, 25, 30, 23, 29, 31, 19, 24, 20,
     36, 32, 36, 28, 25, 21, 28, 29, 37, 25, 28,
     26, 30, 32, 36, 26, 30, 22, 36, 23, 27, 27,
     28, 27, 31, 27, 26, 33, 26, 32, 32, 24, 39,
     28, 24, 25, 32, 25, 29, 27, 28, 29, 16, 23]


# In[3]:


x = pd.DataFrame(L)


# In[4]:


x


# ### Υπολογισμός του πρώτου τεταρτημόριου Q1

# In[5]:


Q1 = x.quantile(0.25)


# In[6]:


Q1


# ### Άσκηση 1 : Υπολογίστε Διάμεσο Μ, το Q3 και το IQR

# In[7]:


M = x.median()
Q2 = x.quantile(0.5)
Q3 = x.quantile(0.75)


# In[8]:


M


# In[9]:


Q2


# In[10]:


Q3


# In[11]:


IQR = Q3-Q1


# In[12]:


IQR


# ### Άσκηση 2:  Δημιουργήστε το Box-and-Whisker plot

# In[13]:


x.plot.box()


# In[ ]:




