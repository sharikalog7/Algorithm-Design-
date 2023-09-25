import numpy as np
def NearestNeighbour(A, start):
    path = [start]
    cost = 0
    N = A.shape[0]
    mask = np.ones(N, dtype=bool)                         
    mask[start] = False
    for i in range(N-1):
        last = path[-1]
        next_ind = np.argmin(A[last][mask])
        next_loc = np.arange(N)[mask][next_ind]
        path.append(next_loc)
        mask[next_loc] = False
        cost += A[last, next_loc]
    cost+=A[path[-1],start]
    path.append(start)
    print("Minimum Cost is :", end = " ")
    for i in range(len(path)-1):
        print(A[path[i]][path[i+1]], end = " ")
        if i < len(path)-2:
            print("+", end=" ")
    print(" = "+str(cost))
    return cost, path


#Testcase 1
A = np.array([
    [0, 60, 100, 50, 90],
    [60, 0, 70, 40, 30],
    [100, 70, 0, 65, 55],
    [50, 40, 65, 0, 110],
    [90, 30, 55, 110, 0]])
print(NearestNeighbour(A,0))


#Testcase 2

A = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]])
print(NearestNeighbour(A,0))