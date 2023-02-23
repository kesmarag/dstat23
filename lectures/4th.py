#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## pandas' describe() function

# $$X \sim \mathcal N(1,2^2)$$

# In[9]:


x = 1.0 + 2.0 * np.random.randn(100000000)


# In[10]:


dataset = pd.DataFrame(x)


# In[11]:


dataset.head()


# In[12]:


dataset.describe()


# $$\mathrm{count} \leftrightarrow N$$
# $$\mathrm{mean} \leftrightarrow \bar{X}, \ \mathrm{std} \leftrightarrow s$$
# $$ 25\% \leftrightarrow Q_1, \ 50\% \leftrightarrow M \equiv Q_2,\ 75\% \leftrightarrow Q_3$$

# ## Μέτρα Ασυμμετρίας

# Μέτρο ασυμμετρίας Pearson
# $$\tilde{Sk}_p = \frac{3(\bar{X}-M)}{s}$$

# In[13]:


dataset.mean()


# In[14]:


dataset.median()


# In[15]:


dataset.std()


# In[16]:


pearson = 3*(dataset.mean()-dataset.median())/dataset.std()


# In[17]:


pearson


# Μέτρο ασυμμετρίας Bowley
# $$Sk_b = \frac{(Q_3 - M)-(M-Q_1)}{Q_3-Q_1}$$

# In[18]:


Q_1 = dataset.quantile(0.25)
M = dataset.median()
Q_3 = dataset.quantile(0.75)
bowley = ((Q_3 - M) - (M - Q_1))/(Q_3-Q_1)


# In[19]:


bowley


# ## Καμπύλη Lorenz - Συντελεστής Gini

# In[20]:


wage = np.array([5000, 10000, 15000, 20000, 50000])

wage = np.insert(wage, 0, 0.0)


# In[21]:


df = pd.DataFrame(wage, columns=['x'])


# In[22]:


df


# $$\Phi_n = \frac{\sum_{j=1}^{n} x_j}{\sum_{j=1}^{N} x_j}$$

# In[24]:


df['x'].sum()


# In[25]:


df['x'].cumsum()


# In[30]:


df['Phi'] = df['x'].cumsum()/df['x'].sum()


# In[31]:


df


# In[33]:


np.array(range(len(wage)))


# $$RF_n = \frac{n}{N}$$

# In[34]:


df['RF'] = np.array(range(len(wage)))/(len(wage)-1)


# In[35]:


df


# $$\{(RF_n,\Phi_n)\}_{n=1}^N$$

# In[37]:


df.plot(x='RF',y='Phi')
plt.plot((0,1),(0,1))


# In[38]:


df['Phi'][:-1].values


# In[39]:


df['Phi'][1:].values


# $$\Sigma \Phi_n = \Phi_n + \Phi_{n-1}$$

# In[40]:


SPhi = df['Phi'][1:].values + df['Phi'][:-1].values


# In[41]:


SPhi


# In[42]:


SPhi = np.insert(SPhi, 0, 0.0)


# In[43]:


SPhi


# In[44]:


df['SPhi'] = SPhi


# In[45]:


df


# $$\Delta RF_n = RF_n - RF_{n-1}$$

# In[46]:


DRF = df['RF'][1:].values - df['RF'][0:-1].values


# In[47]:


DRF = np.insert(DRF, 0, 0.0)


# In[48]:


df['DRF'] = DRF


# In[49]:


df


# In[50]:


df['SPhi_DRF'] = df['SPhi'] * df['DRF']


# In[51]:


df


# In[52]:


Gini = 1 - df['SPhi_DRF'].sum()


# In[53]:


Gini


# In[ ]:




