import json

with open("input.txt") as file:
    data = file.read()

data = json.loads(data)


def getsum(values):
    result = 0
    if isinstance(values, dict):
        # Remove first part for part 1
        if red(values):
            values = [0]
        else:
            values = values.values()  # Keep this still for part 1
    for i in values:
        if isinstance(i, int):
            result += i
        elif isinstance(i, str):
            continue
        else:
            result += getsum(i)
    return result


# Part 2
def red(values):
    values = values.values()
    for i in values:
        if isinstance(i, str):
            if i == "red":
                return True
    return False


print(getsum(data))
