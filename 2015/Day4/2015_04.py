import hashlib

# Input: "iwrupvqb"
code = "iwrupvqb"
zeros = 6
i = 1

while hashlib.md5((code + str(i)).encode()).hexdigest()[0:zeros] != "0"*zeros:
    i += 1

print(i)


