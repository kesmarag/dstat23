#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # Τυχαίο δείγμα 300 επιβατών του Τιτανικού

# In[2]:


dataset = pd.read_csv("./titanic_300.csv")


# ### Με την head() λαμβάνουμε τα 5 πρώτα στοιχεία (preview)

# In[3]:


dataset.head()


# ### Με την tail() λαμβάνουμε τα 5 τελευταία στοιχεία (preview)

# In[4]:


dataset.tail()


# ###  Εμφάνιση τυχαίου στοιχείου του δείγματος

# In[7]:


dataset.iloc[np.random.randint(300)]


# In[20]:


dataset.iloc[232]


# ### Ιστόγραμμα των ηλικίων θεωρώντας Κ ηλικιακές κλάσεις (από τον κανόνα του Sturges)

# In[8]:


dataset['Age']


# In[10]:


dataset["Age"].hist(bins=10)


# ### Απαρίθμηση των εμφανίσεων κάθε φύλου στο δείγμα

# In[11]:


dataset["Sex"].value_counts()


# In[12]:


dataset["Sex"].value_counts().plot.pie()


# In[13]:


dataset["Sex"].value_counts()


# ### Απαρίθμηση των επιζόντων και των θυμάτων (0-θύμα, 1-επιζών) στο δείγμα

# In[14]:


dataset["Survived"].value_counts()


# In[15]:


dataset["Survived"].value_counts().plot.pie()


# In[ ]:





# In[ ]:




