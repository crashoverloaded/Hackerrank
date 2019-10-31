#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    print(str.format('{0:.6f}',len([num for num in arr if num > 0])/len(arr)))
    print(str.format('{0:.6f}',len([num for num in arr if num < 0])/len(arr)))
    print(str.format('{0:.6f}',len([num for num in arr if num == 0])/len(arr)))
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

