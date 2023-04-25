#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    adj = {i:[] for i in range(1,t_nodes+1)}
    for i in range(t_edges):
        adj[t_to[i]].append(t_from[i])
        
    print(adj)
    
    tree = [1 for i in range(1, t_nodes+1)]
    
    def dfs(source):
        if source in visited:
            return 0
        s = 0
        for nbr in adj[source]:
            s += 1 + dfs(nbr)
        return s
    
    for i in range(1, t_nodes+1):
        visited = set()
        tree[i-1] = dfs(i)
    
    count = 0
    for i in range(1, len(tree)):
        if tree[i] % 2 != 0:
            count += 1
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
