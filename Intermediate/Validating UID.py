# 2 uppercase chars
# 3 digits
#  only alphanumeric chars
# no chars should repeat
# 10 chars long

def valid_uid(string: str):
    s = set(string)
    if len(s) != 10:
        print('Invalid')
        return
    
    upper = 0
    digits = 0
    for c in s:
        if c.isdigit():
            digits += 1
        elif c.isupper():
            upper += 1
        else:
            continue
    if upper < 2:
        print('Invalid')
    elif digits < 3:
        print('Invalid')
    else:
        print('Valid')
    


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        # print(str(input()))
        valid_uid(str(input()))