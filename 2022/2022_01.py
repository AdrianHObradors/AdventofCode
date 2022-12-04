with open("i_2022_01.txt") as file:
    calories = file.read().splitlines()

print(calories)

a = 0
b = 0
for i in calories:
    if i != '':
        b += int(i)
    else:
        if b > a:
            a = b
        b = 0
print(a)

#Part 2
a = [0,0,0]
b = 0
for i in calories:
    if i != '':
        b += int(i)
    else:
        if b > min(a):
            a[a.index(min(a))] = b
        b = 0
print(a)
print(sum(a))