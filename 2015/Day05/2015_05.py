with open("input.txt") as file:
    word_list = file.read().splitlines()



nices = 0
for word in word_list:
    if "ab" in word or "cd" in word or "pq" in word or "xy" in word:
        continue
    if word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") < 3:
        continue
    a = ""
    for w in word:
        if w == a:
            nices += 1
            break
        else:
            a = w

print(f'The answer for part 1 is {nices}')


# Part 2
nices = 0
for word in word_list:
    a = False
    b = False
    for i in range(len(word) - 1):
        if not a and word.count(word[i:i+2]) >= 2:
            a = True
        if not b and i < len(word) - 2 and word[i] == word[i + 2]:  # This is a bit weird and the order is important
            b = True
    if a and b:
        nices += 1

print(f'The part 2 answer is {nices}')


