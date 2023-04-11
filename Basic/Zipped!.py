n, m = map(int, input().split())

ls = []
for _ in range(m):
    ls.append(list(map(float, input().split())))
var = list(zip(*ls))


for student in var:
    print(sum(student)/m)