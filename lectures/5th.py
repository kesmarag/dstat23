#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# ### Δημιουργία τυχαίου δείγματος 1024 στοιχείων από την $\mathcal N (2,5^2)$

# In[2]:


dataset = pd.DataFrame(5*np.random.randn(1024)+2, columns=['x'])


# In[3]:


dataset.head()


# ### Υπολογισμός του συντελεστή ασυμμετρίας Fisher-Pearson

# $$G_1 = \frac{N^2}{(N-1)(N-2)}\frac{\frac{1}{N}\sum_{n=1}^N(x_n-\bar{X})^3}{s^3} $$

# In[4]:


dataset.skew()


# Με τη len() λαμβάνουμε πόσα στοιχεία έχει το σύνολο δεδομένων

# In[11]:


N = len(dataset)


# Υπολογισμός του $\sum_{n=1}^N(x_n-\bar{X})^3$

# In[7]:


((dataset - dataset.mean())**3).sum()


# In[ ]:


((dataset - dataset.mean())**3).sum()


# In[8]:


sum3 = ((dataset - dataset.mean())**3).sum()


# In[9]:


s = dataset.std()


# In[12]:


G1 = N**2 / ((N-1)*(N-2)) * (1/N) * sum3 / s**3


# In[13]:


G1


# ### Υπογογισμός του μέτρου κύρτωσης

# $$\mathrm{kurt} = \frac{\frac{1}{N}\sum_{n=1}^N(x_n-\bar{X})^4}{s^4}-3$$

# In[14]:


dataset.kurt()


# ### Άσκηση : Υπολογισμός του $\sum_{n=1}^N(x_n-\bar{X})^4$

# In[ ]:


sum4 = ((dataset-dataset.mean())**4).sum()


# In[ ]:


sum4


# In[ ]:


kurt = (1/N * sum4)/s**4 - 3


# In[ ]:


kurt


# ### Άσκηση : Υπολογίστε τη μέση τιμή, τη διάμεσο, τα τεταρτημόρια για το dataset

# In[ ]:


dataset.describe()


# ### Άσκηση : Δημιουργήστε το Box-and-Whisker plot για το dataset

# In[ ]:


dataset.plot.box()


# ## scipy.stats

# In[18]:


import scipy.stats as st


# ### z-scores

# $$z = \frac{x-\bar{X}}{s}$$

# In[15]:


x1 = 1.0


# In[16]:


z1 = (x1 - dataset.mean())/dataset.std()


# In[17]:


z1


# ### Υπολογισμός του $P(Z \leq z_1)$ με την scipy.stats

# In[19]:


P1 = st.norm.cdf(z1)


# In[20]:


P1


# In[22]:


z1 = -8/9
z2 = 4/3
P1 = st.norm.cdf(z1)
P2 = st.norm.cdf(z2)
P2-P1


# In[23]:


z1 = -1.602


# In[24]:


P1 = st.norm.cdf(z1)


# In[25]:


P1


# In[ ]:





# ### Άσκηση : Επιλύστε με χρήση των pandas και scipy.stats
# Σε ένα δημοψήφισμα με απάντηση ΝΑΙ / ΟΧΙ, το ΟΧΙ συγκέντρωσε το 60% των συνολικών ψήφων. Ποιά η πιθανότητα σε ένα τύχαιο δείγμα 500 ψηφοφόρων το ΝΑΙ να συγκεντρώνει τουλάχιστον το 50%;

# In[ ]:


p = 0.6


# In[ ]:


sigma_p_hat = (0.6*(1-0.6)/500)**(1/2)


# In[ ]:


z = (0.5-p)/sigma_p_hat


# In[ ]:


z


# In[ ]:


st.norm.cdf(z)


# In[ ]:




