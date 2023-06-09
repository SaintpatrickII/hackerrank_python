import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(' ')
    cap_words = [w.capitalize() for w in words]
    return ' '.join(cap_words)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
