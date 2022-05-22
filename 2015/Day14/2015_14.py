with open("input.txt") as file:
    reindeer = file.read().splitlines()

time = 2503  # From input


def position(t, speed, speedtime, rest):
    x = 0
    st = speedtime
    r = rest
    timed_position = {}  # For part 2 only
    initial_t = t  # For part 2 only
    while t > 0:
        if st > 0:
            x += speed
            st -= 1
        elif r > 0:
            r -= 1
            if r == 0:
                st = speedtime
                r = rest
        timed_position[initial_t - t] = x  # Not needed for part 1
        t -= 1
    return timed_position  # Change to x for part 1


# Part 1
"""
# position(t, speed, speedtime, rest)
final_positions = []
for i in reindeer:
    i = i.split()
    x = position(time, int(i[3]), int(i[6]), int(i[13]))
    final_positions.append(x)


#print(max(final_positions))
"""

x_per_sec = {}
for i in reindeer:
    i = i.split()
    x_per_sec[i[0]] = position(time, int(i[3]), int(i[6]), int(i[13]))

scores = {r: 0 for r in x_per_sec.keys()}
for t in range(time):
    winners = []
    distance = 0
    for r in x_per_sec.keys():
        if x_per_sec[r][t] > distance:
            winners = [r]
            distance = x_per_sec[r][t]
        elif x_per_sec[r][t] == distance:
            winners.append(r)
    for w in winners:
        scores[w] += 1

print(max(scores.values()))
