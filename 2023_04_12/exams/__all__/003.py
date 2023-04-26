

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/003.py
#
if __name__ == '__main__':
    numbers = input("Inserisci una lista di numeri: ").split()
    mx = float("-inf")
    for n in numbers:
        n = int(n)
        if n > mx:
            mx = n
    print("Il massimo è", mx)


# -----------------------
# ./roggero_costantino/003.py
#
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

lista_numeri = input_numeri.split()

for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

numero_piu_grande = lista_numeri[0]

for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./lin-matteo - Matth6ew/003.py
#
def main():
    inputnum = input('inserire lista numeri:')
    lista = inputnum.split()
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    maxnum= lista[0]
    for n in range(len(lista)):
        if maxnum <= lista[n]:
            maxnum = lista[n]
    print(maxnum)

main()

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/003.py
#
def max_list():
    numeri = list(map(int, input().strip().split(',')))
    
    x = numeri[0]
    for y in numeri:
        if y > x:
            x = y
            
    print(x)
    
max_list()

# -----------------------
# ./molinari-giorgia/003.py
#
# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/003.py
#
# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/003.py
#
# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/003.py
#
def max_list():
    nums = list(map(float, input('List: ').strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()

# -----------------------
# ./alessandro-lugaro/003.py
#

listanumeri = input("Inserisci una lista di numeri: ")

lista_numeri = listanumeri.split()


for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

numero_piu_grande = lista_numeri[0]

for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./botta-alessio - Alessio Botta/003.py
#
def max_list():
    nums = list(map(int, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/003.py
#
def max_list():
    nums = list(map(int, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/003.py
#
numeri = input("Inserisci una lista di numeri separati da uno spazio: ").split() # Chiediamo all'utente di inserire la lista di numeri
maggiore = int(numeri[0]) # Inizializziamo il valore maggiore come il primo numero della lista

for num in numeri: # Iteriamo su tutti i numeri della lista
    if int(num) > maggiore: # Confrontiamo se il numero attuale è maggiore di quello iniziale
        maggiore = int(num) # Se sì, il numero attuale diventa il nuovo maggiore

print("Il maggiore numero della lista è:", maggiore) # Stampiamo il risultato

# -----------------------
# ./todde-lorenzo - lorenzo todde/003.py
#
def main():
    numbers = input("inserisci i numeri che vuoi confrontare: ")
    numbers_list = numbers.split()
    max_number = 0
    for i in numbers_list:
        if int(i) >= max_number:
            max_number = int(i)
    print(max_number)

main()



# -----------------------
# ./dapino-berenice/003.py
#
def main(): 
    num = list(map(float, input().split(',')))

    m = num[0]
    for n in num: 
        if n>m: 
            m=n
        
    print(m)



main()


# -----------------------
# ./portella-francesco - Francesco Portella/003.py
#
def main():
    inputnum = input('inserire lista numeri:')
    lista = inputnum.split()
    for i in range(len(lista)):
        lista[i] = float(lista[i])
    maxnum= lista[0]
    for n in range(len(lista)):
        if maxnum <= lista[n]:
            maxnum = lista[n]
    print(maxnum)

main()

# -----------------------
# ./moretti-christian/003.py
#
# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/003.py
#
def max_list():
    nums = list(map(float, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()

# -----------------------
# ./hu-xuan-di/003.py
#
# Chiedi all'utente di inserire una lista di numeri separati da spazi
input_numeri = input("Inserisci una lista di numeri separati da spazi: ")

# Suddivide la stringa di input in una lista di stringhe di numeri
lista_numeri = input_numeri.split()

# Converte ciascuna stringa di numero in un numero float
for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

# Inizializza la variabile per il numero più grande con il primo numero della lista
numero_piu_grande = lista_numeri[0]

# Confronta i numeri nella lista per trovare il numero più grande
for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

# Stampa il numero più grande a schermo
print("Il numero più grande è:", numero_piu_grande)

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/003.py
#
def crea_istogramma(lista_numeri):
    for numero in lista_numeri:
        print('*' * numero)

# -----------------------
# ./zono veran - Fabrizio Verani/003.py
#
def max_list():
    nums = list(map(int, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_list()

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/003.py
#
def max_lista():
    nums = list(map(float, input().strip().split(',')))
    
    m = nums[0]
    for n in nums:
        if n > m:
            m = n
            
    print(m)
    
max_lista()

# -----------------------
# ./Matteo-Marazzi/003.py
#

listanumeri = input("Inserisci una lista di numeri: ")

lista_numeri = listanumeri.split()


for i in range(len(lista_numeri)):
    lista_numeri[i] = float(lista_numeri[i])

numero_piu_grande = lista_numeri[0]

for numero in lista_numeri:
    if numero > numero_piu_grande:
        numero_piu_grande = numero

print("Il numero più grande è:", numero_piu_grande)