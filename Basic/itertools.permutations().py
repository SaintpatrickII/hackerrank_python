from itertools import permutations
string, perms = input().split()
perms = int(perms)
# get length of permutations


all_perms = sorted(list(permutations(string, perms)))
# sorted will order by first char of each perm

# for each perm tuplr, join characters with empty space
for p in all_perms:
    print(''.join(p))
