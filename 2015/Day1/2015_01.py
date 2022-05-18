with open("input.txt") as file:
    data = file.read()

# Part 1
print(f'The solution for Part 1 is {data.count("(") - data.count(")")}')


# Part 2
def basement(sequence):
    floor = 0
    for i, s in enumerate(sequence):
        if s == "(":
            floor += 1
        else:
            floor -= 1
        if floor < 0:
            return i + 1


print(f'The solution for Part 2 is {basement(data)}')

# This is a recursive function but it doesn't work as it takes more than 1000 iterations
# def floor(i, step):
#    print(i)
#    if step == -1:
#        return i + 1
#    if data[i] == "(":
#        floor(i + 1, step + 1)
#    else:
#        floor(i + 1, step - 1)
