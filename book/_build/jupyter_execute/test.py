#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame()
df['t'] = np.arange(0,12+1)
df['dK(t)'] = [0, 12.9, 13.0, 23.0, 25.0, 25.0, 32.0, 36.7, 38.6, 39.3, 39.9, 40.5, 9.0]
df['K(t)'] = df['dK(t)'].cumsum()
fig, ax = plt.subplots(1, 1, figsize=(9, 3), dpi=100)
ax.scatter(df['t'], df['K(t)'])
ax.set_xlim(left=0)
ax.set_ylim(0, max(df['K(t)']))
ax.set_ylabel('$m(t)$')
ax.set_xlabel('$t$')
plt.show()

