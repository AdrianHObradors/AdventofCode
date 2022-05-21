import json
with open("input.txt") as file:
    data = file.read()

data = json.loads(data)


def getsum(values):
    result = 0
    if isinstance(values, dict):
        values = values.values()
    for i in values:
        if isinstance(i, int):
            result += i
        elif isinstance(i, str):
            continue

        else:
            result += getsum(i)
    return result


print(getsum(data))