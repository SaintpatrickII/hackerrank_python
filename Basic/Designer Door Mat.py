n, m = map(int, input().split())

# TWO INPUT STRINGS
s1 = '.|.'
s2 = 'WELCOME'
# note for each susequent row s1 is s1 + 2s1 until middle WELCOME mat

# start
for i in range(n//2):
    print((s1*((i * 2)+1)).center(m, '-'))

    # middle
print(s2.center(m, '-'))

# bottom, goes reverse -1, and -1 from range as again python starts from 0 in loops
# if we say n = 7, n // 2 = 3 so would print in range 3 -> 0, whereas top only prints 0 -> 2
for i in range(n//2 - 1, -1, -1):
    print((s1*((i * 2)+1)).center(m, '-'))

