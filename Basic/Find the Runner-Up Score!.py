if __name__ == '__main__':
    n = int(input())
    # map is not subscriptable, we put into a set to remove duplicates, sort that set & transfer to a list which is subscriptable then take 2nd last element
    arr = list(sorted(set(map(int, input().split()))))
    print(arr[-2])