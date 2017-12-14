# -*- coding: utf-8 -*-
import random

"""
@author: Lucy
HW3a
"""

file = open('test2.txt', 'r')
count = 0
G = {}

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
final = {}
test = 1000
while test>0:
    GWMIN = set()
    first = True
    total_weight = 0
    check = [0]*node_num
    while 1:
        if first:
            ### initial set ###
            for i in range(0, node_num):
                if (random.randint(0, 1)):
                    GWMIN.add(i)
                    keys = G[i].keys()
                    for k in keys:
                        weight = k
                    total_weight = total_weight + weight
            first = False
    
        num = 0
        node = random.randint(0,node_num-1)
        keys = G[node].keys()
        for k in keys:
            weight = k
        degree = len(G[node][weight])
        node_value = weight/(degree+1)
        
        for i in G[node][weight]:
            keys = G[i].keys()
            for k in keys:
                neighbor_weight = k
            neighbor_degree = len(G[i][neighbor_weight])
            neighbor_value = neighbor_weight/(neighbor_degree+1)
            if neighbor_value < node_value:
                num = num + 1
            elif (i in GWMIN) == False:
                num = num + 1
            else:
                continue   
        # I join #
        if num == degree:
            # not change decission #
            if node in GWMIN:
                # set flag to 1 #
                check[node] = 1
            else:
                GWMIN.add(node)
                total_weight = total_weight + weight
                check = [0]*node_num
        # not join #
        else:
            # not change decission #
            if node not in GWMIN:
                check[node] = 1
            else:
                check = [0]*node_num
                GWMIN.remove(node)
                total_weight = total_weight - weight
        if check.count(1) == node_num:
            break
        
    GWMIN = list(GWMIN)              
    GWMIN.sort()    
    if final.__contains__(tuple(GWMIN)):
        final[tuple(GWMIN)] = final[tuple(GWMIN)] + 1
    else:
        final[tuple(GWMIN)] = 1
        
    test = test-1
    
for key, value in final.items():
    print (key, " ", value/1000)