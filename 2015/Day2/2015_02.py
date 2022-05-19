import pandas as pd
import numpy as np

with open("input.txt") as file:
    data = file.read().splitlines()

# I don't like applying the function three times :/
df = pd.DataFrame({"raw": data})
df["2lw"] = df["raw"].apply(lambda x: int(x.split("x")[0]) * int(x.split("x")[1]))
df["2lh"] = df["raw"].apply(lambda x: int(x.split("x")[0]) * int(x.split("x")[2]))
df["2wh"] = df["raw"].apply(lambda x: int(x.split("x")[1]) * int(x.split("x")[2]))
df["small"] = df.min(axis=1, numeric_only=True)
df["result"] = 2*(df["2lw"] + df["2lh"] + df["2wh"]) + df["small"]
print(f'The answer for part 1 is {df["result"].sum()}')

# Part 2
df2 = pd.DataFrame()
df2["l"] = df["raw"].apply(lambda x: int(x.split("x")[0]))
df2["w"] = df["raw"].apply(lambda x: int(x.split("x")[1]))
df2["h"] = df["raw"].apply(lambda x: int(x.split("x")[2]))
df2["volume"] = df2["l"] * df2["w"] * df2["h"]
df2["size"] = df["raw"].apply(lambda x: [int(x.split("x")[0]), int(x.split("x")[1]), int(x.split("x")[2])])
df2["value"] = df2["size"].apply(lambda x: sum(2 * np.array(sorted(x)[0:2])))
df2["total"] = df2["volume"] + df2["value"]
print(f'The answer for part 2 is {df2["total"].sum()}')
