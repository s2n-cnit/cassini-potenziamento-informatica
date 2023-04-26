def perfetto(n):
    sm = 0
    for d in range(1, n):
        if n % d == 0:
            sm += d
    return sm == n
