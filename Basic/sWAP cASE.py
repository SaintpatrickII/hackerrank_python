def swap_case(s):
    # creates new str, checks if lower or upper, swaps these, if not just adds char to string normally
    output = ''
    for c in s:
        if c.islower() == True:
            output += c.upper()
        elif c.isupper() == True:
            output += c.lower()
        else:
            output += c
    return output

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# or can just do 
# def swap_case(s):
#     return s.swapcase()