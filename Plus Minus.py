#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = 0.000000
    negative = 0.000000
    zeroes = 0.000000
    
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative += 1
        else:
            zeroes += 1
        
    positive = positive / len(arr)
    negative = negative / len(arr)
    zeroes = zeroes / len(arr)
        
    print(round(positive,6))
    print(round(negative,6))
    print(round(zeroes,6))
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
