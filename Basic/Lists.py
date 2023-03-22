if __name__ == '__main__':
    # takes first input as number of commands & init list
    N = int(input())
    ls = []
    # loops through range of commands, pos[0] tells us command
    for i in range(0, N):
        cmd = input().split()
        if cmd[0] == 'insert':
            ls.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(ls)
        elif cmd[0] == 'remove':
            ls.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            ls.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            ls.sort()
        elif cmd[0] == 'pop':
            ls.pop()
        elif cmd[0] == 'reverse':
            ls.reverse()