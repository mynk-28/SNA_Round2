#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv
import random


# In[2]:


path = "out.FLIXSTER"
file=open(path)


# In[3]:


G = nx.Graph()
l=0
for i in file:
    if l>=1:
        f = i.split()
        f[0]=int(f[0])
        f[1]=int(f[1])
        G.add_edge(f[0],f[1])
    l += 1
n = G.number_of_nodes()


# In[4]:


components = max(nx.connected_components(G),key=len)


# In[5]:


N_G = len(components)
print("Number of nodes in G: ",N_G)


# In[6]:


N = G.number_of_nodes()
print("Number of nodes in Network: ",N)


# In[7]:


print("N_G/N = ",N_G/N)


# In[ ]:




