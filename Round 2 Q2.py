#!/usr/bin/env python
# coding: utf-8

# In[1]:


from networkx import *
import matplotlib.pyplot as plt
import math
import itertools
import networkx as nx
from queue import Queue
import numpy as np
import numpy.random
import pylab
import random
print('CREATING BARABASI ALBERT MODEL\n')
g = barabasi_albert_graph(10000, 250)

print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('ASSIGNING ACTIVATION PROBABILITIES\n')
set_edge_attributes(g, values=0, name='weight')
arr = [[False] * 10000 for i in range(10000)]
vis = set()
q = Queue()
vis.add(0)
q.put(0)

while not q.empty():
    u = q.get()

    vis.add(u)
    x = 1
    f = 0

    for v in g.neighbors(u):
        if v not in vis:
            vis.add(v)
            q.put(v)

        if arr[u][v] is True or arr[v][u] is True:
            x -= g[u][v]['weight']
        else:
            f += 1

    k = 0
    lst = np.random.dirichlet(np.ones(f), size=1).tolist()[0]

    for v in g.neighbors(u):
        if arr[u][v] is False or arr[v][u] is False:
            arr[u][v] = arr[v][u] = True
            g[u][v]['weight'] = lst[k] * max(x, 0)
            k += 1


print('\n----------------------------------------------------------------------------------------------------------------------\n')
print('RUNNING ICM ALGORITHM\n')

nodes =[]
num_steps = []

for itr in range(0, 10):
    r = random.randint(0, 10000)
    vis = set()
    q = Queue()
    q.put(r)
    activated = []
    activated.append(r)
    steps = 0
    print("Initial set - " + str(activated))

    while not q.empty():
        steps += 1
        u = q.get()

        for v in g.neighbors(u):
            if v not in activated:
                rand = random.uniform(0, 1)
                if rand < g[u][v]['weight']:
                    q.put(v)
                    activated.append(v)

    print("Steps - " + str(steps))
    print("Activated nodes - " + str(activated))
    num_steps.append(steps)
    nodes.append(len(activated))
    print()

    
print("The average number of steps are" , sum(num_steps)/10)
print("The average number of activated nodes are ", sum(nodes)/10)


# In[2]:


nx.draw_random(g, with_labels = True)
plt.savefig("fig1.png")

