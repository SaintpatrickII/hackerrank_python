# from collections import Counter  import counter

n = int(input())
shoes = list(map(int, input().split()))
shoes = Counter(shoes)
# n is not needed, but shoes are the second input line, we store these in a list & convert
# to a counter dict


# we need number of customers to define loop length & a profit variable
no_of_cust = int(input())
profit = 0


for i in range(no_of_cust):
    # each next input line is size & price, so we map these to input
    size, price = map(int, input().split())
    # check that the size exists in counter dict & that there are still avalible pairs
    if size in shoes and shoes[size] > 0:
        profit += price
        shoes[size] -= 1
        # if shoe exists we add profit and -1 from shoe count
print(profit)