import numpy as np
import pandas as pd
import re

with open("input.txt") as file:
    input = file.read().splitlines()


values = {"children": [], "cats": [], "samoyeds": [], "pomeranians": [], "akitas": [], "vizslas": [], "goldfish": [],
          "trees": [], "cars": [], "perfumes": []}


for i in input:
    for k in values.keys():
        s = re.split("[:|,] ", i)
        if k in s:
            values[k].append(int(s[s.index(k) + 1]))
        else:
            values[k].append(np.nan)

values_df = pd.DataFrame(values)


tape = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
        "cars": 2, "perfumes": 1}
for k, v in tape.items():
    values_df = values_df.loc[np.logical_or(np.isnan(values_df.loc[:, k]), values_df.loc[:, k] == v), :]
    print(len(values_df))

print(values_df)

print(f"Aunt Sue {values_df.index.values[0] + 1} sent the present")

#################### Part 2
values_df = pd.DataFrame(values)

for k, v in tape.items():
    if k in ["cats", "trees"]:
        values_df = values_df.loc[np.logical_or(np.isnan(values_df.loc[:, k]), values_df.loc[:, k] > v), :]
    elif k in ["pomeranians", "goldfish"]:
        values_df = values_df.loc[np.logical_or(np.isnan(values_df.loc[:, k]), values_df.loc[:, k] < v), :]
    else:
        values_df = values_df.loc[np.logical_or(np.isnan(values_df.loc[:, k]), values_df.loc[:, k] == v), :]
    print(len(values_df))

print(values_df)

print(f"Aunt Sue {values_df.index.values[0] + 1} sent the present")