def perfect(n):
    perf = 0
    for i in range(1, n-1):
        if n % i == 0:
            perf = perf + i
    if perf == n:
        print('PERFETTO')
    else:
        print('non perfetto')
perfect(5)
perfect(6)
perfect(28)
perfect(100)
