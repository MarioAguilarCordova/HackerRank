#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    rows = len(arr)
    
    firstDiag = 0
    secondDiag = 0
    
    for i in range(rows):
        firstDiag += arr[i][i]
        
    count = 0
    for i in range(rows - 1, -1, -1):
        
        secondDiag += arr[count][i]
        count += 1
    
    print(firstDiag)
    print(secondDiag)
    absoDiff = abs(firstDiag - secondDiag)
    
    return absoDiff
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
