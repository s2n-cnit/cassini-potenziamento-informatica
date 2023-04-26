def frequency(a: str):
    out = {}
    for i in a:
        if i in out:
            out[i] += 1
        else:
            out[i] = 1
    return out

