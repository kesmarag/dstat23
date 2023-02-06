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


# ### Εφαρμογή του κανόνα του Sturges
# $$K = 1 + 3.322 * \log(N)$$

# In[8]:


K = round(1+3.322*np.log10(300))


# In[9]:


K


# ### Ιστόγραμμα των ηλικίων θεωρώντας Κ ηλικιακές κλάσεις (από τον κανόνα του Sturges)

# In[10]:


dataset['Age']


# In[14]:


dataset["Age"].hist(bins=K)


# ### Απαρίθμηση των εμφανίσεων κάθε φύλου στο δείγμα

# In[15]:


dataset["Sex"].value_counts()


# In[16]:


dataset["Sex"].value_counts().plot.pie()


# In[17]:


dataset["Sex"].value_counts().plot.lllll()


# ### Απαρίθμηση των επιζόντων και των θυμάτων (0-θύμα, 1-επιζών) στο δείγμα

# In[18]:


dataset["Survived"].value_counts()


# In[19]:


dataset["Survived"].value_counts().plot.pie()


# In[20]:


dataset["Survived"].value_counts().plot.bar()


# In[ ]:




