with open("i_2022_03.txt") as file:
    rucksack = file.read().splitlines()

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'



def main():
    value = 0
    for l in rucksack:
        size = int(len(l)/2)
        first = l[:size]
        second = l[size:]
        for i in first:
            if i in second:
                value += priority.index(i) + 1
                break
    print(value)

    # Part two
    b_value = 0
    for a in range(0, len(rucksack), 3):
        for item in rucksack[a]:
            if (item in rucksack[a+1]) & (item in rucksack[a+2]):
                b_value += priority.index(item) + 1
                break
    print(b_value)

if __name__ == '__main__':
    main()

