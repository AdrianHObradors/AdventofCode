# I am not happy with this. Doesn't work well. I got the answer right but the values I got depended on who I sat first.
# I am not sure if it would work every time. I will revisit it later.

with open("input.txt") as file:
    happiness = file.read().splitlines()


persons = {p.split()[0]: None for p in happiness}


for i in happiness:
    i = i.split()
    if i[2] == "gain":
        gain = 2
    else:
        gain = 1
    if isinstance(persons[i[0]], dict):
        persons[i[0]][i[-1][:-1]] = (-1) ** gain * int(i[3])
    else:
        persons[i[0]] = {i[-1][:-1]: (-1) ** gain * int(i[3])}


# This code snippet is for part 2
persons["Me"] = {p: 0 for p in persons.keys()}
for p in persons.keys():
    persons[p]["Me"] = 0
# Remove until here for part 1


def gethapp(person1, person2):
    return persons[person1][person2] + persons[person2][person1]


happsum = {}
for i in persons.keys():
    happsum[i] = {}
    for j in persons.keys():
        if i != j:
            happsum[i][j] = gethapp(i, j)


"""
sat = []
happsum = 0
for a in persons.keys():
    sat.append(a)
    best_partner = ""
    value_best_partner = float(""-inf"")
    for b in persons.keys():
        if a != b and b not in sat:
            gethapp(a, b)"""


def find_best_partner(person, sat=[]):
    best_partner = ""
    value_best_partner = float("-inf")
    for a in persons.keys():
        if a not in sat:
            if gethapp(person, a) > value_best_partner:
                best_partner = a
                value_best_partner = gethapp(person, a)
    sat.append(best_partner)
    return best_partner, value_best_partner, sat



partner = "Me"
sat = ["Me"]
total_happ = 0
for i in range(15):
    partner, value, sat = find_best_partner(partner, sat)
    if partner:
        total_happ += value
    else:
        total_happ += gethapp(sat[0], sat[-2])
        print(total_happ, partner, value, sat)
        break
    print(partner, value, sat, total_happ)



#654 is too low
#692 is too low
# 709 is correct. (You get this one when sitting David first

# For part two 668 is correct. It somehow worked. 