def minion_game(string):
    vowels = 'AEIOU'
    sarthak_score = 0
    hunny_score = 0

    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            sarthak_score += length - i
        else:
            hunny_score += length - i

    if sarthak_score > hunny_score:
        print("Sarthak", sarthak_score)
    elif hunny_score > sarthak_score:
        print("Hunny", hunny_score)
    else:
        print("Draw")

if __name__ == '__main__':
    print("Enter string:")
    s = input()
    minion_game(s)
