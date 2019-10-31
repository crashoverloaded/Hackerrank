#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr1,arr2=list(arr),list(arr)
    maxarr=[]
    minarr=[]
    for i in range(4):
        minarr.append(min(arr2))
        arr2.remove(min(arr2))
    for i in range(4):
        maxarr.append(max(arr1))
        arr1.remove(max(arr1))
    print(str(sum(minarr))+" "+str(sum(maxarr)))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

