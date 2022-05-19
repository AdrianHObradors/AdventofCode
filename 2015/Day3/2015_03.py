import numpy as np

with open("input.txt") as file:
    directions = file.read()

values = {"^": [0, 1], "v": [0, -1], "<": [-1, 0], ">": [1, 0]}

# Part 1
position = np.array([0, 0])
presents = {"[0 0]": 1}
for d in directions:
    position += values[d]
    presents[str(position)] = presents.get(str(position), 0) + 1

print(f'The solution for part 1 is {len(presents)}')

# Part 2
position1 = np.array([0, 0])
position2 = np.array([0, 0])
presents = {"[0 0]": 1}
for i, d in enumerate(directions):
    if i % 2 == 0:
        position1 += values[d]
        presents[str(position1)] = presents.get(str(position1), 0) + 1
    else:
        position2 += values[d]
        presents[str(position2)] = presents.get(str(position2), 0) + 1

print(f'The solution for part 2 is {len(presents)}')
