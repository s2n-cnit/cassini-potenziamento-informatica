lista = [7, 66, 100, 457, 472]
risultato = 1
for numero in lista:
    if numero != 0:
        risultato *= numero
print("Il risultato della moltiplicazione tra tutti gli "
      f"elementi della lista è {risultato}")
