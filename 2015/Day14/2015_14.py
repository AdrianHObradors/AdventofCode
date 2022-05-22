with open("input.txt") as file:
    reindeer = file.read().splitlines()


# Comet flies at 14 km/s for 10 seconds, rests for 127 seconds
# Dancer flies at 16 km/s for 11 seconds, rests for 162 seconds

time = 2503  # From input

def position(t, speed, speedtime, rest):
    x = 0
    st = speedtime
    r = rest
    while t > 0:
        t -= 1
        if st > 0:
            x += speed
            st -= 1
        elif r > 0:
            r -= 1
            if r == 0:
                st = speedtime
                r = rest
    return(x)


# position(t, speed, speedtime, rest)
final_positions = []
for i in reindeer:
    i = i.split()
    x = position(time, int(i[3]), int(i[6]), int(i[13]))
    final_positions.append(x)


print(max(final_positions))

# 2176 is too low
# 2640 is too low