# -*- coding: utf-8 -*-
import random

"""
@author: Lucy
HW3b
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
    current_GWMIN = set()
    last_GWMIN = set()
    first = True
    check = [0]*node_num
    total_weight = 0
    while 1:
        change = False
        if first:
            ### initial set ###
            for i in range(0, node_num):
                if (random.randint(0, 1)):
                    last_GWMIN.add(i)
                    keys = G[i].keys()
                    for k in keys:
                        weight = k
                    total_weight = total_weight + weight
            first = False
            current_GWMIN = last_GWMIN.copy()
        else:
            last_GWMIN = current_GWMIN.copy()   
        # go through every node to see whether it decide or not #
        for key, value in G.items():
            if (random.randint(0, 1)):
                num = 0
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
                    
                    if neighbor_value < node_value:
                        num = num + 1
                    elif (i in last_GWMIN) == False:
                        num = num + 1
                    else:
                        continue
                # I join #
                if num == degree:
                    # not change decission #
                    if key in last_GWMIN:
                        # set flag to 1 #
                        check[key] = 1
                    else:
                        current_GWMIN.add(key)
                        total_weight = total_weight + weight
                        change = True
                # not join #
                else:
                    # not change decission #
                    if key not in last_GWMIN:
                        check[key] = 1
                    else:
                        current_GWMIN.remove(key)
                        total_weight = total_weight - weight
                        change = True
        if change:
            check = [0]*node_num
        if check.count(1) == node_num:
            break
    last_GWMIN = list(last_GWMIN)              
    last_GWMIN.sort() 
    if final.__contains__(tuple(last_GWMIN)):
        final[tuple(last_GWMIN)] = final[tuple(last_GWMIN)] + 1
    else:
        final[tuple(last_GWMIN)] = 1
    test = test - 1
    
for key, value in final.items():
    print (key, " ", value/1000)