from collections import defaultdict

n, m = map(int,input().split())

adict = defaultdict(list)
for i in range(1, n + 1):
    adict[input()].append(i)

for i in range(1, m + 1):
    key = input()
    if len(adict[key]) > 0:
        print(" ".join(str(s) for s in adict[key]))
    else:
        print(-1)