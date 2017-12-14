# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:21:54 2017

@author: Lucy
exercise_a
"""

file = open('filename', 'r')
count = 0
G = {}
GWMIN = []
total_weight = 0

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
while G:
    max_w = 0;
    # find max #
    for i in range(0, node_num):
        if i in G:
            keys = G[i].keys()
            for k in keys:
                key = k
            degree = len(G[i][key])
            if (key/(degree+1))> max_w:
                max_w = key/(degree+1)
                index = i
                add_element_key = key
    # add element to GWMIN #
    GWMIN.append(index)
    total_weight = total_weight + add_element_key
    
    # update neighboring one by one#
    for i in range(0, len(G[index][add_element_key])):
                
        # 1 and 6 #
        delete_index = G[index][add_element_key][i]
        keys = G[delete_index].keys()
        for k in keys:
            key = k
            
        # update 1 and 6's neighbor #
        for j in range(0, len(G[delete_index][key])):
            # no need to update added node #
            if G[delete_index][key][j] != index:
                need_update_index = G[delete_index][key][j]
                keys = G[need_update_index].keys()
                for k in keys:
                    need_update_key = k
                G[need_update_index][need_update_key].remove(delete_index)
                
        # remove 1 and 6 # 
        del G[delete_index]

    # remove the added element from G #
    del G[index]
    
                  
GWMIN.sort()
print ("MWIS:", GWMIN) 
print ("Total weight:", total_weight)   