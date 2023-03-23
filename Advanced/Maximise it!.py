from itertools import product
# itertools product allows us to loop through diffferent lists & combine all unique possibilities into one list of tuples
# i.e. 
# a = [5, 4]
# b = [3, 2]
# c = [a, b]
# list(product(*c)) = [(5, 3), (5, 2), (4, 3), (4, 2)]


# n is the amount of sublists, m is the number we will be taking modulus of later
n, m = map(int, input().split())
list_of_outputs = []

# range n will allow us to loop through every list of elements
# map into int, however first number for each input is the length of that input line, so we transfer into list & index this first element out
# finally append to list of outputs
for i in range(n):
    l = list(map(int, input().split()))[1:]
    list_of_outputs.append(l)
    
#  create map function, this uses lambda operator
# first arg(func) takes each list & squares the elements, then sums these & divides by required modulus
#  second arg(iter) is our list of product, or every combination of values
squared = map(lambda x : sum(i*i for i in x)%m, product(*list_of_outputs))
# final step is just to get the max number from this list
print(max(squared))