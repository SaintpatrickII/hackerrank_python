from collections import defaultdict
n = int(input())
rooms = list(input().split())
# print(rooms)

no_of_guests = defaultdict()

for room in rooms:
    no_of_guests[room] = 1 + no_of_guests.get(room, 0)
    
# print(no_of_guests)
for k, v in no_of_guests.items():
    if v == 1:
        print(int(k))

# using default dict we can have dict with no values & insert them as they appear without keyerror