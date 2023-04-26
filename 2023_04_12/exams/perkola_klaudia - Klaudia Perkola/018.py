def perfetto(n):
    somma_divisori = 0

    #itera sui numeri da 1 a n/2 (escluso n)
    for i in range(1, n//2 + 1):
        #se i è un divisore di n, si aggiunge alla somma
        if n % i == 0:
            somma_divisori += i

    #se la somma dei divisori è uguale a n, allora n è un numero perfetto
    if somma_divisori == n:
        return True
    else:
        return False

n = int(input("Inserisci un numero intero positivo: "))
if perfetto(n):
    print(f"Il numero {n} è un numero perfetto.")
else:
    print(f"Il numero {n} non è un numero perfetto.")