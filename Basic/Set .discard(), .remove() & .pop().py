n = int(input())
s = set(map(int, input().split()))
cmds = int(input())
for i in range(cmds):
    cmd = input().split()
    if cmd[0] == 'pop':
        s.pop()
    elif cmd[0] == 'remove':
        s.remove(int(cmd[1]))
    else:
        s.discard(int(cmd[1]))
print(sum(s))