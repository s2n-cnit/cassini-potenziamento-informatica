def is_perfect_number(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) == n

num = int(input("Inserisci un numero: "))
if is_perfect_number(num):
    print(num, "è un numero perfetto")
else:
    print(num, "non è un numero perfetto")