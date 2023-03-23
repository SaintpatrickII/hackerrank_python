N = input().split()
my_likes = input().split()
A = set(input().split())
B = set(input().split())
# n is useless here, my likes is the list of values we check against
#  A is likes & B is dislikes

happiness = 0
for i in my_likes:
    if i in A:
        happiness += 1
    if i in B:
        happiness -= 1

print(happiness)