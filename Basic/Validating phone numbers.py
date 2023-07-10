import re
n = int(input())

for _ in range(n):
    if re.match(r'[789]\d{9}$',input()): 
    # if string starts with [7,8,9] and has didgets occur 9 times after then return yes
        print('YES')
    else:
        print('NO')