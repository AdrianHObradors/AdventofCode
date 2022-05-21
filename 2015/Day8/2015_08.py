with open("input.txt") as file:
    strings = file.read().splitlines()


codelen = 0
lenlen = 0
for s in strings:
    codelen += len(s)
    lenlen += len(s.encode().decode('unicode-escape')) - 2
print(codelen - lenlen)

code2 = 0
for s in strings:
    code2 += len(s) + 2 + s.count('"') + s.count('\\')
print(code2 - codelen)