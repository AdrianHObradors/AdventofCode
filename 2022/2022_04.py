with open("i_2022_04.txt") as file:
    sectors = file.read().splitlines()

def main():
    score = 0
    for s in sectors:
        a, b = s.split(',')
        a1, a2 = a.split('-')
        b1, b2 = b.split('-')
        a1, a2, b1, b2 = (int(a1), int(a2), int(b1), int(b2))
        if a1 == b1 or a2 == b2:
            score += 1
        elif a1 < b1:
            if a2 > b2:
                score += 1
        else:
            if a2 < b2:
                score += 1
    print(score)


if __name__ == '__main__':
    main()