import numpy as np

with open("input.txt") as file:
    instructions = file.read().splitlines()

lights = np.zeros((1000, 1000), dtype=int) - 1

for instruction in instructions:
    (x_i, y_i, x_f, y_f) = [int(s) for s in instruction.replace(",", " ").split() if s.isdigit()]
    if "turn on" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] = 1
    elif "turn off" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] = -1
    elif "toggle" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] *= -1

print(lights[lights == 1].sum())


# Part 2
lights = np.zeros((1000, 1000), dtype=int)

for instruction in instructions:
    (x_i, y_i, x_f, y_f) = [int(s) for s in instruction.replace(",", " ").split() if s.isdigit()]
    if "turn on" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] += 1
    elif "turn off" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] -= 1
    elif "toggle" in instruction:
        lights[x_i:x_f+1, y_i:y_f+1] += 2
    lights[lights < 0] = 0

print(lights.sum())