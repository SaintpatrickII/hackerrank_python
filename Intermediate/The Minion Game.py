def minion_game(string):
    vowels = "AEIOU"
    Stuart = 0
    Kevin = 0
    for i in range(len(string)):
        if string[i] in vowels :
            Kevin += len(string[i:])
        else :
            Stuart += len(string[i:])
            
    if Stuart > Kevin :
        print(f"Stuart {Stuart}")
    elif Kevin > Stuart :
        print(f"Kevin {Kevin}")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)