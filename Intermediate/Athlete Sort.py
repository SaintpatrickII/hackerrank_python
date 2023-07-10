import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)
    arr = []
# fresh array

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
        # creates sublist of int values of each input line split

    
    k = int(input())
    # key for which index we want to be sorted
    arr2 = sorted(arr, key =lambda x : x[k])
    # create copy of list with key being the kth element
    # print(arr2)
    for i in arr2:
        print(' '.join(str(x) for x in i))
        # list comprehension to join all elements of each list with a whitespace