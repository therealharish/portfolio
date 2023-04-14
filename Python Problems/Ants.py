#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY V as parameter.
#

def solve(V):
    n = len(V)
    firstPart = n * (n - n//2) * 10**5
    
    i = 0
    count = 0
    while(i<len(V)-1):
        if V[i]+1 == V[i+1]:
            count += 1 
            i+=2
        else:
            i+=1
    ans = (firstPart + count) * 2
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V_count = int(input().strip())

    V = list(map(int, input().rstrip().split()))

    result = solve(V)

    fptr.write(str(result) + '\n')

    fptr.close()
