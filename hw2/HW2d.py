# -*- coding: utf-8 -*-
import random

"""
@author: Lucy
HW2b
"""

file = open('test1.txt', 'r')
count = 0
G = {}
current_GWMIN = set()
last_GWMIN = set([0])
SAMPLE = []
first = True
V = [] # values
################################################
""" handle data input """
for line in file:
    line = line.split()
    if count == 0:
        node_num = int(line[0])
    if count == 1:
        for i in range(0, node_num):
            weight = int(line[i])
            G[i] = {weight:[]}
            V.append(weight)
    elif count > 1 and count <= (node_num+1):
        for i in range(0, node_num):
            # not integer, str #
            if line[i] == '1':
                keys = G[count-2].keys()
                # get weight of node #
                for k in keys:
                    key = k
                G[count-2][key].append(i)
    count = count + 1
    
for key, value in G.items():
    V[key] = V[key]/(len(value[V[key]])+1)

################################################
""" compute GWMIN """
while current_GWMIN != last_GWMIN:
    
    if first:
        for i in range(0, node_num):
            if (random.randint(0, 1)):
                last_GWMIN.add(i)
        for cur in range(0, len(V)):
            same_value = set()
            for i in range(cur, len(V)):
                keys = G[i].keys()
                for k in keys:
                    weight = k
                if (cur!=i) and (V[cur]==V[i]) and (cur in G[i][weight]):
                    same_value.add(i)
                    same_value.add(cur)
            if len(same_value)!=0:
                SAMPLE.append(list(same_value))
        if len(SAMPLE)!=0:
            for i in SAMPLE:
                if (set(i) & last_GWMIN):
                    last_GWMIN = last_GWMIN-set(i)
                last_GWMIN.add(random.choice(i))
        first = False
    else:
        last_GWMIN = current_GWMIN.copy()
    
    current_GWMIN.clear()
    total_weight = 0
    
    # from node 0 to node n-1 #
    for key, value in G.items():
        num = 0
        # check if neighbors join #
        keys = value.keys()
        for k in keys:
            weight = k
        degree = len(value[weight])
        for i in value[weight]:
            keys = G[i].keys()
            for k in keys:
                neighbor_weight = k
            neighbor_degree = len(G[i][neighbor_weight])
            if V[i] < V[key]:
                num = num + 1
            elif (i in last_GWMIN) == False:
                num = num + 1
            else:
                continue
        # neighbors not join, then I join #
        if num == degree:
            current_GWMIN.add(key)
            total_weight = total_weight + weight

last_GWMIN = list(last_GWMIN)              
last_GWMIN.sort()
print ("MWIS:", last_GWMIN) 
print ("Total weight:", total_weight)