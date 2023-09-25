#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:15:07 2022

@author: sharikaloganathan
"""

import numpy as np

def greedyTSP(A):
    
    sum = 0
    counter = 0
    j = 0
    i = 0
    INT_MAX=99999
    mincost=INT_MAX
    visitedRouteList = {}
    path = []
    path.append(0)
    visitedRouteList[0] = 1
    route = [0] * len(A)
 
    while i < len(A) and j < len(A[i]):
        if counter >= len(A[i]) - 1:
            break
        if j != i and j not in path:
            if A[i][j] < mincost:
                mincost = A[i][j]
                route[counter] = j + 1
        j += 1
        if j == len(A[i]):
            sum += mincost
            mincost = INT_MAX
            path.append(route[counter] - 1)
            j = 0
            i = route[counter] - 1
            counter += 1
    i = route[counter - 1] - 1
    sum += A[i][0]
    path.append(0)
    print("Minimum Cost is :", end = " ")
    for i in range(len(path)-1):
        print(A[path[i]][path[i+1]], end = " ")
        if i < len(path)-2:
            print("+", end=" ")
    print(" = " +str(sum))
    print(path)
    return sum, path


# Driver Code
if __name__ == "__main__":
    
	#Testcase 1
    arr= np.array([
        [0, 60, 100, 50, 90],
        [60, 0, 70, 40, 30],
        [100, 70, 0, 65, 55],
        [50, 40, 65, 0, 110],
        [90, 30, 55, 110, 0]])
    
    greedyTSP(arr)
    

    #Testcase 2

    arr= np.array([
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]])    
    
    greedyTSP(arr)

	
