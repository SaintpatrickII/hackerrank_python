def count_substring(string, sub_string):
    '''
    - Initilise count for no of substrings in string
    - we know that for each character we loop through the length of remainder of the string must be >= length of sub string
    - len of substring must have -1 as python 0 index's
    - index the string from the current pointer to the length of the string (string index does not include last number)
    - if these match add one to the counter
    
    
    '''
    no_of_sub = 0
    for i in range(len(string) - (len(sub_string) - 1)):
        if string[i:i+(len(sub_string))] == sub_string:
            no_of_sub += 1
        else:
            continue
        
        
        
    return no_of_sub

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)