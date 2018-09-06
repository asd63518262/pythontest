#!/usr/bin/python
# -*- coding: UTF-8 -*-
node_number =  int(raw_input())
time = [];
for node in range(node_number):
    node_time = raw_input()
    node_time = node_time.split(',')
    time.append(int(node_time[1]))
print time
edge_number = int(raw_input())
edge_weight = []
for i in range(edge_number):
    one_edge_weight = raw_input()
    one_edge_weight = one_edge_weight.split(',')
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

#计算最短时间
def min_path_long(node_start,node_stop,edge_weight,time):
    target = []
    target.append(node_start)
    dis = tuple(edge_weight[node_start])
    dis_attemp = list(dis)
    dis_attemp[node_start] = float('inf')
    while (len(target) <= node_number):
        min_weight = min(dis_attemp)
        if min_weight == float('inf'):
            break
        place = dis_attemp.index(min_weight)
        target.append(place)
        second_node_weight_array = edge_weight[place]
        for node_second in range(node_number):
            if ((min_weight/time[place])%2 == 0):
                sum_weight = min_weight + second_node_weight_array[node_second]
            else:
                sum_weight = min_weight + second_node_weight_array[node_second] + time[place] - min_weight%time[place]
            if sum_weight < list(dis)[node_second]:
                dis_attemp[node_second] = sum_weight
                dis = list(dis)
                dis[node_second] = sum_weight
                dis =  tuple(dis)
        dis_attemp[place] = float('inf')
    return dis[node_stop]

for node_start in range(node_number):
    for node_end in range(node_number):
        print min_path_long(node_start,node_end,edge_weight,time)