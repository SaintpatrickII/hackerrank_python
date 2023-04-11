t = int(input())
for _ in range(t):
    n = int(input())
    l1 = set(map(int, input().split()))
    m = int(input())
    l2 = set(map(int, input().split()))
    print(l1.issubset(l2))