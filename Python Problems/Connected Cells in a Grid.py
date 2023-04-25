#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    row = len(matrix)
    col = len(matrix[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    
    def dfs(i, j, l, visited):
        if (i, j) in visited:
            return
        if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] == 0:
            return
        l.append([i, j])
        visited.add((i, j))
        for r,c in direction:
            dfs(i+r, j+c, l, visited)        
    
    ans = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                l = []
                dfs(i, j, l, set())
                ans = max(ans, len(l))
                
    return ans
        
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
