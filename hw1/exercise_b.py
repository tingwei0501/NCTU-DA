# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:21:54 2017

@author: Lucy
exercise_b
"""

file = open('filename', 'r')
count = 0
num = 0
G = {}
current_GWMIN = set()
last_GWMIN = set([0])

################################################
""" handle data input """
for line in file:
    line = line.split()
    
    if count == 0:
        node_num = int(line[0])
    if count == 1:
        for i in range(0, node_num):
            G[i] = {int(line[i]):[]}
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

################################################
""" compute GWMIN """
while current_GWMIN != last_GWMIN:
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
        node_value = weight/(degree+1)
        
        for i in value[weight]:
            keys = G[i].keys()
            for k in keys:
                neighbor_weight = k
            neighbor_degree = len(G[i][neighbor_weight])
            neighbor_value = neighbor_weight/(neighbor_degree+1)
            
            # neighbors not join #
            if (i in last_GWMIN) == False:
                num = num + 1
            # neighbor joined, compare value #
            elif node_value > neighbor_value:
                num = num + 1
            # same value, compare id #
            elif node_value == neighbor_value and key < i:
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