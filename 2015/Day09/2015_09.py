import pandas as pd
import numpy as np
with open("input.txt") as file:
    data = file.read().splitlines()


distances = {d.split()[0]: None for d in data}
distances2 = {d.split()[2]: None for d in data}
distances.update(distances2)

for i in data:
    i = i.split()
    if isinstance(distances[i[0]], dict):
        distances[i[0]][i[2]] = int(i[-1])
    else:
        distances[i[0]] = {i[2]: int(i[-1])}
    if isinstance(distances[i[2]], dict):
        distances[i[2]][i[0]] = int(i[-1])
    else:
        distances[i[2]] = {i[0]: int(i[-1])}


dist = pd.DataFrame(distances)
min_travel = np.inf
for i in dist:
    dist = pd.DataFrame(distances)
    visited = [i]
    dist.loc[visited[0]] = np.inf
    travel_d = 0
    for j in range(len(dist) - 1):
        travel_d += dist[visited[-1]].min()
        visited.append(dist[visited[-1]].idxmin())
        dist.loc[visited[-1]] = np.inf
    min_travel = min(travel_d, min_travel)
    if min_travel == travel_d:
        min_route = visited

print(min_travel)
print(min_route)

# Part 2
dist = pd.DataFrame(distances)
max_travel = 0
for i in dist:
    dist = pd.DataFrame(distances)
    visited = [i]
    dist.loc[visited[0]] = 0
    travel_d = 0
    for j in range(len(dist) - 1):
        travel_d += dist[visited[-1]].max()
        visited.append(dist[visited[-1]].idxmax())
        dist.loc[visited[-1]] = 0
    max_travel = max(travel_d, max_travel)
    if max_travel == travel_d:
        max_route = visited

print(max_travel)
print(max_route)

# I am getting 764 but it is too low


"""def find_closest_place(person, visited=[]):
    closest = ""
    distance_closest = np.inf
    for place in distances.keys():
        if place not in visited:

            if gethapp(person, a) > distance_closest:
                best_partner = a
                distance_closest = gethapp(person, a)
    sat.append(closest)
    return best_partner, distance_closest, sat
"""



from itertools import permutations

places = set()
distances = dict()
for line in open('input.txt'):
    (source, _, dest, _, distance) = line.split()
    places.add(source)
    places.add(dest)
    distances.setdefault(source, dict())[dest] = int(distance)
    distances.setdefault(dest, dict())[source] = int(distance)

shortest = np.inf
longest = 0
for items in permutations(places):
    dist = sum(map(lambda x, y: distances[x][y], items[:-1], items[1:]))
    shortest = min(shortest, dist)
    longest = max(longest, dist)
    if dist == longest:
        print(items)

print("shortest: %d" % (shortest))
print("longest: %d" % (longest))