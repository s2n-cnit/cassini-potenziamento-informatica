lista = ['Marco', 'Luigi', 'Paolo', 'Giuseppe', 'Maria']
el = input("Inserisci un nome da cercare: ")
trovato = False
for nome in lista:
    if nome == el:
        trovato = True
        break
if trovato:
    print(f"{el} è presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non è presente nella lista.")
