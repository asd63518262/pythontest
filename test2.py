#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "请输入节点个数和边的个数:"
node =  raw_input()
node = node.split(' ')
node_number = int(node[0])
edge_number = int(node[1])
print "起点和终点以及权值："
edge_weight = []
for i in range(edge_number):
    one_edge_weight = raw_input()
    one_edge_weight = one_edge_weight.split(' ')
    edge_weight.append(one_edge_weight)
print edge_weight
edge_weight_att = []
for node in range(node_number):
    weight_att = []
    for node2 in range(node_number):
        if node2 != node:
            weight_att.append(float('inf'))
        else:
            weight_att.append(0)
    for i in range(len(edge_weight)):
        one_edge_weight = edge_weight[i]
        if node == int(one_edge_weight[0]):
            end = int(one_edge_weight[1])
            weight = int(one_edge_weight[2])
            weight_att[end] = weight
    edge_weight_att.append(weight_att)
edge_weight = edge_weight_att #邻接矩阵
print "邻接矩阵"
for node in range(node_number):
    one_node_edge_array = edge_weight[node]
    print one_node_edge_array

def min_path(node_start,edge_weight):
    #初始化
    target = []
    target.append(node_start)
    dis = tuple(edge_weight[node_start])
    dis_attemp = edge_weight[node_start]
    dis_attemp[node_start] = float('inf')
    while (len(target) <= node_number):
        min_weight = min(dis_attemp)
        if min_weight == float('inf'):
            break
        place = dis_attemp.index(min_weight)
        target.append(place)
        second_node_weight_array = edge_weight[place]
        for node_second in range(node_number):
            sum_weight = min_weight + second_node_weight_array[node_second]
            if sum_weight < dis_attemp[node_second]:
                dis_attemp[node_second] = sum_weight
                dis = list(dis)
                dis[node_second] = sum_weight
                dis =  tuple(dis)
        dis_attemp[place] = float('inf')
    return dis

print min_path(0,edge_weight)









