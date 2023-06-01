# Data una lista di numeri decimali scrivere un programma che calcoli:
# - media
# - moda
# - mediana
# - varianza
# - deviazione standard
# - tabella delle frequenze di ciascun numero (in %).
# - grafico delle occorrenze di ciascun numero.

# Esempio:
#   lista = [1, 2, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7]
#
# Tabella:
# 1: 23,07%
# 2: 23.07%
# 3: 15.38%
# 4: 15.38%
# 5: 15.38%
# 6: 0.00%
# 7: 7.69%
#
# Grafico:
# 1 ***
# 2 ***
# 3 **
# 4 **
# 5 **
# 6
# 7 *

lista = [1, 2, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7]


def media(lista):
    return sum(lista) / len(lista)


# E(x)^2 - E(x^2)
# media(lista) ** 2 - media([x*x for x in lista])


def media_alt(lista):
    somma = 0.0
    n = 0
    for x in lista:
        somma += x  # somma = somma + x
        n += 1  # n = n + 1
    return somma / n


def moda(lista):
    massimo_num = min(lista)
    contatore_num = {}
    for x in lista:
        if x in contatore_num:
            contatore_num[x] += 1
        else:
            contatore_num[x] = 1
        if contatore_num[x] >= contatore_num[massimo_num]:
            massimo_num = x
    return massimo_num


lista = [1, 2, 3, 4, 5, 6]
lista = [1, 2, 3, 4, 5, 6, 7]


def mediana(lista):
    lung = len(lista)
    return media(lista[lung / 2 : 1]) if lung % 2 == 0 else lista[(lung - 1) / 2]


def varianza(lista):
    m = media(lista)
    return media((x - m) ** 2 for x in lista)


def tabella_frequenze(lista):
    contatore_num = {}
    minore = min(lista)
    maggiore = max(lista)
    for x in lista:
        contatore_num[x] = contatore_num[x] + 1 if x in contatore_num else 1
    for x in range(minore, maggiore):
        # for x in contatore_num.keys():
        if x in contatore_num:
            print(f"{x}:", "*" * contatore_num[x])
        else:
            print(f"{x}:")
