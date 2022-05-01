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


path = "p2p-Gnutella05.txt"


# In[3]:


G = nx.read_edgelist(path,nodetype=int,create_using=nx.DiGraph())
print(nx.info(G))


# In[4]:


components = max(nx.strongly_connected_components(G),key=len)


# In[5]:


N_G = len(components)
print("Number of nodes in G:",N_G)


# In[6]:


N = G.number_of_nodes()
print("Number of nodes in Network:",N)


# In[7]:


print("N_G/N =",N_G/N)

