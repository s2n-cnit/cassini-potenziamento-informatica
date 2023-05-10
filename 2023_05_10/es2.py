# Scrivi un programma Python per trovare quattro numeri interi pari positivi la cui somma è un dato numero intero pari. Esempio - input: n = 100 output: [94,2,2,2]

n = 100

for i in range(2, n, 2):
    for j in range(i + 1, n, 2):
        for k in range(j + 1, n, 2):
            for z in range(k + 1, n, 2):
                if i + j + k + z == n:
                    print(i, j, k, z)
                    exit(0)

print(2, 2, 2, n - 6)
print(2, 4, 6, n - 12)

# n / 4 = 25 -> 24 * 4 = 96 -> 2, 2

ref = n / 4
if ref % 2 != 0:
    ref = ref - 1
rem = n - ref * 4
n_agg = rem / 2
for i in range(n_agg):
    print(ref + 2)
for i in range(4 - n_agg):
    print(ref)
