from itertools import combinations_with_replacement
s = input().split()
word = sorted(s[0])
n = int(s[1])
combinations = list(combinations_with_replacement(word, n))
for i in combinations:
    print(''.join(i))