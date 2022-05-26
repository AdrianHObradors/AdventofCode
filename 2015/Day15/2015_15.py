import numpy as np

# This solution is only for inputs where the number of ingredients is equal to 4, although it is easy enough to adapt.
# It grows with ~O(100^n), for n = number of ingredients though.


with open("input.txt") as file:
    data = file.read().splitlines()

ingredients = {i.split()[0][:-1]: {} for i in data}
for i in data:
    i = i.split()
    for j in range(4):
        ingredients[i[0][:-1]][i[2 * j + 1]] = int(i[2 * j + 2][:-1])
    ingredients[i[0][:-1]][i[-2]] = int(i[-1])

# quantity = {k: 0 for k in ingredients.keys()}

one = np.array(list(ingredients["Sprinkles"].values()))
two = np.array(list(ingredients["PeanutButter"].values()))
three = np.array(list(ingredients["Frosting"].values()))
four = np.array(list(ingredients["Sugar"].values()))
best = 0
(i, j, k, l) = (0, 0, 0, 0)

for i in range(1, 100):  # Should be 101, but I know it is going to be mixed.
    properties1 = i * one
    if i < 100:
        for j in range(1, 100):
            properties2 = properties1 + j * two
            if i + j < 100:
                for k in range(1, 100):
                    properties3 = properties2 + k * three
                    if i + j + k < 100:
                        l = 100 - i - j - k
                        properties4 = properties3 + l * four
                        properties4[properties4 < 0] = 0
                        if np.prod(properties4[:-1]) > best:
                            best = np.prod(properties4[:-1])
                            print(f'Current best is i = {i}, j = {j}, k = {k}, l = {l}, best = {best}')
                        continue
                    properties3[properties3 < 0] = 0
                    if i + j + k == 100 and np.prod(properties3[:-1]) > best:
                        best = np.prod(properties3[:-1])
                        print(f'Current best is i = {i}, j = {j}, k = {k}, l = {l}, best = {best}')
                    elif i + j + k > 100:
                        break
            properties2[properties2 < 0] = 0
            if i + j == 100 and np.prod(properties2[:-1]) > best:
                best = np.prod(properties2[:-1])
                print(f'Current best is i = {i}, j = {j}, k = {k}, l = {l}, best = {best}')
            elif i + j > 100:
                break
    properties1[properties1 < 0] = 0
    if i == 100 and np.prod(properties1[:-1]) > best:
        best = np.prod(properties1[:-1])
        print(f'Current best is i = {i}, j = {j}, k = {k}, l = {l}, best = {best}')


print(f'The best value obtained is {best}')
