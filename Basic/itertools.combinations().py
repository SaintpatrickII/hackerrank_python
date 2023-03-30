from itertools import combinations

a = input().split()

# need to loop with i = 1 char and i = 2 chars
for i in range(1, int(a[1]) + 1):
    for j in combinations(sorted(a[0]), i):
        print(''.join(j))