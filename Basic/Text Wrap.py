import textwrap

def wrap(string, max_width):
    # using textwrap.fill means no outpul after string has been wrapped, if we use .wrap end up with None at end of output
    return textwrap.fill(string, 4)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)