def frequenze(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1
    return d
