def mutate_string(string, position, character):
    str_start = string[:position]
    str_end = string[position + 1:]
    new_str = str_start + str(character) + str_end
    return new_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)