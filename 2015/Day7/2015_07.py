# Bitwise operations
# 16-bit signal (0 to 65535)
import re

with open("input.txt") as file:
    instructions = file.read().splitlines()

# instructions = ["NOT x -> h", "123 -> x", "456 -> y", "NOT y -> i", "x AND y -> d", "x OR y -> e", "x LSHIFT 2 -> f",
#                "y RSHIFT 2 -> g"]


# wires = {"b": 46065}  # This is for part 2

wires = {}
breaker = 0
while wires.get("a") is None:
    length = len(wires)
    for i in instructions:
        w = re.findall("[a-z]+", i)[-1]
        if wires.get(w) is not None:
            instructions.remove(i)
            continue
        a = re.findall("(.+) [A-Z]+", i)
        b = re.findall("[A-Z]+ (.+) ->", i)
        if not a and not b:
            c = re.findall(r"(.+) ->", i)[0]
            if c.isnumeric():
                c = int(c)
            else:
                c = wires.get(c)
            if c is not None:
                wires[w] = c
                continue
            else:
                continue
        if a:
            if a[0].isnumeric():
                a = int(a[0])
            else:
                a = wires.get(a[0])
        if b:
            if b[0].isnumeric():
                b = int(b[0])
            else:
                b = wires.get(b[0])
        if a is None or b is None:
            continue
        if "AND" in i:
            wires[w] = a & b
        elif "OR" in i:
            wires[w] = a | b
        elif "LSHIFT" in i:
            wires[w] = a << b
        elif "RSHIFT" in i:
            wires[w] = a >> b
        elif "NOT" in i:
            wires[w] = ~ b & 0xffff
    if len(wires) == length:
        breaker += 1
        if breaker >= 20:
            print("Loop might be stuck...")
            break


print(f'The value of the wire "a" is {wires["a"]}')
