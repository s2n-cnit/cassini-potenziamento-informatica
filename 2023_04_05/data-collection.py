# Data Collection

# sourcery skip: merge-set-add, move-assign-in-block
lt = [1, 2, 3]
s = {1, 2, 3}
t = (1, 2, 3)

lt[0] = 2
# s[0] = 2
s.add(4)
s.add(4)
print(s)
# t[0] = 2

print(lt * 2)  # [2, 2, 3, 2, 2 3]
print([0] * 20)

lt.append(4)
print(lt)

lt.remove(2)
print(lt)

lt.extend([1, 2, 3])
print(lt)

lt.pop(2)
print(lt)

lt.reverse()
print(lt)

ln = lt[1:3]
print(ln)

for x in lt[:2]:
    print(x)

print(len(lt))

# Dato una lista l di dimensioni n (n pari)
# restituire una nuova lista (ln) con n/2 elementi
# in modo che ln[i] = (l[i] + l[i + n/2]) / 2


def compute(ls: list):
    n = len(ls)
    len_ln = n // 2  # Divisione intera, equivale a int(n / 2)
    ln = [0] * len_ln
    for i in range(len_ln):
        ln[i] = (ls[i] + ls[i + len_ln]) / 2
    return ln


print(lt[:4], compute(lt))

# Provare a creare la funzione reverse:
# Data una lista l restituire una nuova lista con l'ordine inverso.
# l.reverse()


def reverse(ls):
    ln = [0] * len(ls)
    for i in range(len(ls)):
        ln[i] = ls[len(ls) - 1 - i]
    return ln


print(lt, reverse(lt))
