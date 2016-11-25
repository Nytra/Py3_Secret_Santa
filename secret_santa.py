# secret_santa.py
# created by Sam Scott
# 25/11/2016

import random

# ===== Read the names into memory
names = []
with open("names.txt", "r") as f:
    lines = f.readlines()
    for raw_string in lines:
        name = raw_string.strip()
        names.append(name)

# ===== Match people up
d = {}
for name in names:
    match = name
    while match == name:
        match = random.choice(names)
        if match in d.values():
            match = name
    d[name] = match

# ===== Display the results
for name in d.keys():
    print(name, "->", d[name])


