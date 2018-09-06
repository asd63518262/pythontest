#!/usr/bin/python
# -*- coding: UTF-8 -*-
nodeNumber = int(raw_input())
matrix =  raw_input()
edge_number = int(matrix[0])
edge_matrix = []
for i in range(edge_number):
    edge = raw_input()
    edge_matrix.append(edge)

new_edge_matrix = [];
node = 0
while (node < nodeNumber):
    node_edge_matrix = []
    for edge in edge_matrix:
        node_array = edge.split(' ')
        if (int(node_array[0]) == node):
            node_edge_matrix.append(int(node_array[1]))
    new_edge_matrix.append(node_edge_matrix)
    node = node + 1


##每个节点的路径数目
def routh_number(node,adjacent_matrix):
    node_list = []
    node_list.append(node)
    routh_number_att = 0
    while (1):
        if (len(node_list) > 0):
            node_list_attempt = []
            for node_att in node_list:
                routh_number_att = routh_number_att + len(adjacent_matrix[node_att])
                node_list_attempt = node_list_attempt + adjacent_matrix[node_att]
            node_list = node_list_attempt
        elif (len(node_list) == 0):
            break
    return routh_number_att

def max_routh_number(node_number,adjacent_matrix):
    routh_node_number = []
    for node in range(node_number):
        routh_node_number_att = routh_number(node,adjacent_matrix)
        routh_node_number.append(routh_node_number_att)
    return max(routh_node_number)

print "最多路径是：", max_routh_number(nodeNumber,new_edge_matrix)

















