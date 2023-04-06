from collections import deque
n = int(input())

q = deque()
for i in range(n):
    cmd = input().split()
    if cmd[0] == 'append':
        q.append((cmd[1]))
    elif cmd[0] == 'pop':
        q.pop()
    elif cmd[0] == 'popleft':
        q.popleft()
    else:
        q.appendleft((cmd[1]))
print(' '.join(q))