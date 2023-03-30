from collections import OrderedDict
n = int(input())
# no of items


ord_dict = OrderedDict()
for _ in range(n):
    product = input().split()
    item = ' '.join(product[:-1])
    # item has spacing so product name is every element bar the last element
    price = int(product[-1])
    # price is the last element of every input line
    # add item if not exist otherwise add it
    if item not in ord_dict:
        ord_dict[item] = price
    else:
        ord_dict[item] += price

# print k,v pair
for i in ord_dict:
    print(i, ord_dict[i])