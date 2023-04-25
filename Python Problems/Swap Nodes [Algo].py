#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    tree = [1]
    for i in indexes:
        for j in i:
            tree.append(j)
            
    indexes = tree
    print(indexes)
    def swap(ci):
        if 2*ci+2 >= len(indexes):
            return
        indexes[2*ci+1], indexes[2*ci+2] = indexes[2*ci+2], indexes[2*ci+1]
        swapChildren(2*ci+1, 2*ci+2)
        
    def swapChildren(node1, node2):
        if 2*node2+2 >= len(indexes):
            return 
        x, y = indexes[2*node1+1], indexes[2*node1+2]
        indexes[2*node1+1], indexes[2*node1+2] = indexes[2*node2+1], indexes[2*node2+2]
        indexes[2*node2+1], indexes[2*node2+2] = x,y
        swapChildren(2*node1+1, 2*node1+2)
        swapChildren(2*node2+1, 2*node2+2)
        
    def inOrderTraversalOfArray(i, inorder):
        if i >= len(indexes):
            return
        if indexes[i] == -1:
            return
        inOrderTraversalOfArray(2*i+1, inorder)
        inorder.append(indexes[i])
        inOrderTraversalOfArray(2*i+2, inorder)
        
        
        
        
    ans = []
    for i in range(len(queries)):
        k = queries[i]
        x = 2
        while(k<=len(indexes)):
            for j in range(2**(k-1)-1, 2**k):
                swap(j)
            k = x*k
            x+=1
            print(indexes)
        inorder = []
        inOrderTraversalOfArray(0, inorder)
        ans.append(inorder.copy())
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
