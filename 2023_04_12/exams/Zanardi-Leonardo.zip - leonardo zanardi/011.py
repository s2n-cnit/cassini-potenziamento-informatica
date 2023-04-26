def frequency(y: str):
    out = {}
    for x in y:
        if x in out:
            out[x] += 1
        else:
            out[x] = 1
    return out
