import math
import os
import random
import re
import sys


def if_else(num):
    if num % 2 != 0:
        print('Weird')
    elif num > 2 and num < 6:
        print('Not Weird')
    elif num >=6 and num < 21:
        print('Weird')
    else:
        print('Not Weird')
    
    
    
if __name__ == '__main__':
    n = int(input().strip())
    if_else(n)