

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/007.py
#
if __name__ == '__main__':
    elements = input("Inserisci una lista: ").split()
    element = input("Controlla se un elemento è nella lista: ")
    if element in elements:
        print("Elemento trovato all'indice", elements.index(element), "(Gli indici prtono da 0).")
    else:
        print("Elamento non trovato")


# -----------------------
# ./roggero_costantino/007.py
#
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

elemento = input("Inserisci un elemento da cercare nella lista: ")

try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./lin-matteo - Matth6ew/007.py
#
def main():
    input_lista = input('inserisci lista di oggetti separati da "spazio": ')
    list = input_lista.split()
    thing = input('inserisci un elemento da cercare: ')
    if thing in list:
        print("L'elemento è presente nella posizione " + str(list.index(thing)))
    else:
        print("L'elemento non è presente")

main()


# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/007.py
#
def in_list():
    x = float(input('Numero: '))
    numeri = list(map(float, input('Elenco: ').strip().split(',')))
    
    if x in numeri:
        print(f'{x} è dentro elenco all indice {numeri.index(x)}')
    else:
        print(f'{x} non è dentro l elenco')
        
in_list()

# -----------------------
# ./molinari-giorgia/007.py
#
# Definisci la lista di elementi
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

# Chiedi all'utente di inserire un elemento da cercare
elemento = input("Inserisci un elemento da cercare nella lista: ")

# Utilizza il metodo index() per cercare l'elemento nella lista
# Se l'elemento è presente, restituisce l'indice, altrimenti solleva un'eccezione ValueError
try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/007.py
#
# Definisci la lista di elementi
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

# Chiedi all'utente di inserire un elemento da cercare
elemento = input("Inserisci un elemento da cercare nella lista: ")

# Utilizza il metodo index() per cercare l'elemento nella lista
# Se l'elemento è presente, restituisce l'indice, altrimenti solleva un'eccezione ValueError
try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/007.py
#
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

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/007.py
#
def in_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
in_list()

# -----------------------
# ./alessandro-lugaro/007.py
#
lista_elementi = ['banana', 'book', 'computer', 'home']

elemento = input("Inserisci un elemento da cercare nella lista: ")

try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./botta-alessio - Alessio Botta/007.py
#
def in_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
in_list()

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/007.py
#
elemento = input("Inserisci l'elemento: ")
lista = input("Inserisci gli elementi della lista separati da uno spazio: ").split()

if elemento in lista:
    print("L'elemento", elemento, "è presente nella lista all'indice", lista.index(elemento))
else:
    print("L'elemento", elemento, "non è presente nella lista")

# -----------------------
# ./todde-lorenzo - lorenzo todde/007.py
#
def main():
    Nlist = input("inserisci tutti gli elementi: ")
    obj =  input("inserisci l'oggetto da trovare: ")
    if obj in Nlist:
        print('Presente')
        return obj.index

main()



# -----------------------
# ./dapino-berenice/007.py
#


# -----------------------
# ./portella-francesco - Francesco Portella/007.py
#
def main():
    input_lista = input('inserisci lista di oggetti separati da "spazio": ')
    list = input_lista.split()
    thing = input('inserisci un elemento da cercare: ')
    if thing in list:
        print("L'elemento è presente nella posizione " + str(list.index(thing)))
    else:
        print("L'elemento non è presente")

main()


# -----------------------
# ./moretti-christian/007.py
#
# Definisci la lista di elementi
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

# Chiedi all'utente di inserire un elemento da cercare
elemento = input("Inserisci un elemento da cercare nella lista: ")

# Utilizza il metodo index() per cercare l'elemento nella lista
# Se l'elemento è presente, restituisce l'indice, altrimenti solleva un'eccezione ValueError
try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/007.py
#
def el_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
el_list()

# -----------------------
# ./hu-xuan-di/007.py
#
# Definisci la lista di elementi
lista_elementi = ['apple', 'banana', 'cherry', 'date', 'fig']

# Chiedi all'utente di inserire un elemento da cercare
elemento = input("Inserisci un elemento da cercare nella lista: ")

# Utilizza il metodo index() per cercare l'elemento nella lista
# Se l'elemento è presente, restituisce l'indice, altrimenti solleva un'eccezione ValueError
try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/007.py
#
def in_list():
    x = float(input('Numero: '))
    numeri = list(map(float, input('Elenco: ').strip().split(',')))
    
    if x in numeri:
        print(f'{x} è dentro elenco all indice {numeri.index(x)}')
    else:
        print(f'{x} non è dentro l elenco')
        
in_list()

# -----------------------
# ./zono veran - Fabrizio Verani/007.py
#
def in_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
in_list()

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/007.py
#
def in_list():
    a = float(input('Number: '))
    nums = list(map(float, input('List: ').strip().split(',')))
    
    if a in nums:
        print(f'{a} is in the list at index {nums.index(a)}')
    else:
        print(f'{a} is not in the list')
        
in_list()

# -----------------------
# ./Matteo-Marazzi/007.py
#
lista_elementi = ['banana', 'book', 'computer', 'home']

elemento = input("Inserisci un elemento da cercare nella lista: ")

try:
    indice = lista_elementi.index(elemento)
    print("L'elemento", elemento, "è presente nella lista all'indice", indice)
except ValueError:
    print("L'elemento", elemento, "non è presente nella lista.")