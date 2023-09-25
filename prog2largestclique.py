#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 02:10:57 2022

@author: sharikaloganathan
"""
import random
import copy
import datetime
import matplotlib.pyplot as plt
from tabulate import tabulate

class Graph(): 
    def __init__(self, n):
        self.V = n
        self.graph = {}
        self.MAX = 10000
        self.store = [0] * self.MAX
        self.max_store = [0] * self.MAX
        self.d = [0] * self.MAX
        self.m = 0
        for i in range(1,n+1):
            self.graph[i] = []
        
    def drawGraph(self, n, m):
        i = 0
        while i < m:
            v1 = random.choice(range(1,n+1))
            v2 = random.choice(range(1,n+1))
            if v2 in self.graph[v1] or v1 in self.graph[v2]:
                continue
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
            self.d[v1] += 1
            self.d[v2] += 1
            i += 1
        return self.graph
    
    def print_max_independentSet(self, maxSet) :
        print("Largest Independent Set:", end = " ")
        for i in maxSet:
            print(str(i), end =" ")
        print("")
            
    def findgraphSets(self, graph):
        if(len(graph) == 0):
            return []
        if(len(graph) == 1):
            return [list(graph.keys())[0]]
        vCurrent = list(graph.keys())[0]
        graph2 = dict(graph) 
        del graph2[vCurrent]
        res1 = self.findgraphSets(graph2) 
        for v in graph[vCurrent]:    
            if v in graph2:
                del graph2[v]
        res2 = [vCurrent] + self.findgraphSets(graph2)
        if(len(res1) > len(res2)):
            return res1
        return res2
                
    def is_clique(self, b):
        for i in range(1, b):
            for j in range(i + 1, b):
                if self.store[i] not in self.graph.keys() or self.store[j] not in self.graph[self.store[i]]:
                    return False 
        return True
    
    def print_max_cli(self, n, s) :
        print("Largest Clique:", end = " ")
        for i in range(1,n) :
            print(str(s[i]), end = " ")
        print("")

    def findCliques(self, i, l, s) :
        max_ = 0
        for j in range(i+1, n+1) :
            if (self.d[j] >= s - 1) :
                self.store[l] = j
                if self.is_clique(l + 1) :
                    max_ = max(max_,l)
                    max_ = max(max_, self.findCliques(j, l + 1, max_)[0])
                if l == max_ and max_ > s and self.m < l:
                    self.m = l
                    self.max_store = self.store.copy()
        return max_, self.max_store

num = []
time1 = []
time2 = []
mapDict1 = {}
mapDict2 = {}
mapDict3 = {}
for i in range(10):
    n = random.randint(2, 20)
    e = n-1
    g = Graph(n)
    graph = g.drawGraph(n, e)
    startTime = datetime.datetime.now()
    max_l, arr = g.findCliques(0, 1, 0)
    g.print_max_cli(max_l + 1, arr)
    endTime = datetime.datetime.now()
    timediff1 = endTime-startTime
    time1.append(timediff1)
    startTime = datetime.datetime.now()
    g.print_max_independentSet(g.findgraphSets(graph))
    endTime = datetime.datetime.now()
    timediff2 = endTime-startTime
    time2.append(timediff2)
    num.append(n)
    mapDict1[n] = [timediff1,timediff2]
    mapDict2[n*e] = [timediff1,timediff2]
    mapDict3[e] = [timediff1,timediff2]
    
    
p = []
q = []
r = []
timestamp = []
for i in sorted(mapDict1.keys()):
    p.append(mapDict1[i][0])
    q.append(i) 
    r.append(mapDict1[i][1])
timestamp1 = []     
for i in p:
    timestamp1.append(i.total_seconds())
timestamp2 = []
for i in r:
    timestamp2.append(i.total_seconds())
    
headers = ['n', 'Largest Clique', 'Largest Independent Set']  
table = zip(q, timestamp1, timestamp2)
print(tabulate(table, headers=headers, floatfmt=".4f"))  

plt.plot(q, timestamp1, marker="o", color="red", label="Largest Clique")
plt.plot(q, timestamp2, marker="o", color="blue", label="Largest Independent Set")
plt.grid(visible=True, which='major', color='g', linestyle='--')
plt.show()

p = []
q = []
r = []
timestamp = []
for i in sorted(mapDict2.keys()):
    p.append(mapDict2[i][0])
    q.append(i) 
    r.append(mapDict2[i][1])
timestamp1 = []     
for i in p:
    timestamp1.append(i.total_seconds())
timestamp2 = []
for i in r:
    timestamp2.append(i.total_seconds())
    
headers = ['n*m', 'Largest Clique', 'Largest Independent Set']  
table1 = zip(q, timestamp1, timestamp2)
print(tabulate(table1, headers=headers, floatfmt=".4f"))  

plt.plot(q, timestamp1, marker="o", color="red", label="Largest Clique")
plt.plot(q, timestamp2, marker="o", color="blue", label="Largest Independent Set")
plt.grid(visible=True, which='major', color='g', linestyle='--')
plt.show()





mapDict = {}
mapDict1 = {}
mapDict2 = {}
for i in range(10):
    n = random.randint(2, 5000)
    e = n-1#
    g = Graph(n)
    graph = g.drawGraph(n, e)
    startTime = datetime.datetime.now()
    max_l, arr = g.findCliques(0, 1, 0)
    g.print_max_cli(max_l + 1, arr)
    endTime = datetime.datetime.now()
    timediff1 = endTime-startTime
    time1.append(timediff1)
    num.append(n)
    mapDict[n] = [timediff1]
    mapDict1[n*e] = [timediff1]
    mapDict2[e] = [timediff1]

p = []
q = []
r = []
for i in sorted(mapDict.keys()):
    p.append(mapDict[i][0])
    q.append(i) 
timestamp = []
for i in p:
    timestamp.append(i.total_seconds())  
headers = ['n', 'Largest Clique']  
table = zip(q, timestamp1)
print(tabulate(table, headers=headers, floatfmt=".4f"))  

plt.plot(q, timestamp, marker="o", color="red", label="Largest Clique")
plt.grid(visible=True, which='major', color='g', linestyle='--')
plt.show()


p = []
q = []
r = []
for i in sorted(mapDict1.keys()):
    p.append(mapDict1[i][0])
    q.append(i) 
timestamp1 = []
for i in p:
    timestamp1.append(i.total_seconds())  
headers = ['n*m', 'Largest Clique']  
table1 = zip(q, timestamp1)
print(tabulate(table1, headers=headers, floatfmt=".4f"))  

plt.plot(q, timestamp1, marker="o", color="red", label="Largest Clique")
plt.grid(visible=True, which='major', color='g', linestyle='--')
plt.show()

p = []
q = []
r = []
for i in sorted(mapDict2.keys()):
    p.append(mapDict2[i][0])
    q.append(i) 
timestamp1 = []
for i in p:
    timestamp1.append(i.total_seconds())  
headers = ['m', 'Largest Clique']  
table2 = zip(q, timestamp1)
print(tabulate(table2, headers=headers, floatfmt=".4f"))  

plt.plot(q, timestamp1, marker="o", color="red", label="Largest Clique")
plt.grid(visible=True, which='major', color='g', linestyle='--')
plt.show()