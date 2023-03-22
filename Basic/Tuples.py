if __name__ == '__main__':
    # note only works in pypy3
    n = int(input())
    integer_list = map(int, input().split())
    # Tuples in Python - Hacker Rank Solution START
    t = tuple(integer_list)
    print(hash(t))