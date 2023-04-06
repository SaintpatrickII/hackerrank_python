# s = ''
input_str = list(input().strip())

# strip to get all elements of str into a list

# print(input_str)
caps = []
lowercase = []
numbers_odd = []
numbers_even = []
# check elements for their category
for i in input_str:
    if i.isupper():
        caps.append(i)
    #  any odd % 2 cannot give 0 as a remainder so is put with odd numbers
    elif i.isnumeric() and int(i) % 2 != 0:
        numbers_odd.append(i)
    elif i.isnumeric() and int(i) % 2 == 0:
        numbers_even.append(i)
    elif i.islower():
        lowercase.append(i)
        
caps.sort()
lowercase.sort()
numbers_odd.sort()
numbers_even.sort()
# print(caps, lowercase, numbers_odd)
one = ''.join(lowercase)
two = ''.join(caps)
three = ''.join(numbers_odd)
four = ''.join(numbers_even)
s = one + two + three + four
print(s)
