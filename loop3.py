t = "Banana"
d = {}
for c in t:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

print(d)