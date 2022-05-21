alphabet = "abcdefghijklmnopqrstuvwxyz"
to_number = {v: k for k, v in enumerate(alphabet)}
to_letter = {k: v for k, v in enumerate(alphabet)}


def increase(password):
    if password[-1] == "z":
        return increase(password[:-1]) + "a"
    else:
        password = password[:-1] + to_letter[to_number[password[-1]] + 1]
        return password


def nextpass(password):
    condition1 = True
    condition2 = True
    condition3 = True
    while "i" in password or "o" in password or "l" in password:
        password = increase(password)
    while condition1 or condition2 or condition3:
        password = increase(password)
        condition1 = condition3 = True
        condition2 = False
        if "i" in password or "o" in password or "l" in password:
            condition2 = True
        for i in range(2, len(password)):
            if to_number[password[i]] - to_number[password[i-1]] == to_number[password[i-1]] - to_number[password[i-2]] == 1:
                condition1 = False
                continue
        repeats = 0
        banlet = ""
        for i in range(1, len(password)):
            if password[i] == password[i-1] and password[i] != banlet:
                repeats += 1
                banlet = password[i]
            if repeats >= 2:
                condition3 = False
                continue

    return password


print(nextpass("hepxxyzz"))


# hepxddef not correct
# hepxxxyz