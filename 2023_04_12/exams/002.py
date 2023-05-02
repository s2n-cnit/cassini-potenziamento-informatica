

-----------------------
./Baglietto-Luca - Luca Baglietto/002.py
if __name__ == '__main__':
    a = int(input("Inserisci il numero a: "))
    b = int(input("Inserisci il numero b: "))
    c = int(input("Inserisci il numero c: "))
    if a > b:
        mx = a
    else:
        mx = b
    if c > mx:
        mx = c
    print("Il massimo è", mx)


-----------------------
./roggero_costantino/002.py
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("Il numero più grande è:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Il numero più grande è:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Il numero più grande è:", numero3)


-----------------------
./lin-matteo - Matth6ew/002.py
def main():
    a = float(input('primo numero:'))
    b = float(input('secondo numero:'))
    c = float(input('terzo numero:'))
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >=c :
        print(b)
    else:
        print(c)

main()

-----------------------
./Zanardi-Leonardo.zip - leonardo zanardi/002.py
def max_3():
    x = float(input('first number: '))
    y = float(input('second number: '))
    z= float(input('third number: '))
    
    if x > y and x > z:
        print(x)
    elif y > x and y > z:
        print(y)
    else:
        print(z)
        
max_3()

-----------------------
./ExamFrittoli - Lorenzo Frittoli/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./Alessandro-Lugaro/002.py
n1 = float(input("Inserisci il primo numero: "))
n2 = float(input("Inserisci il secondo numero: "))
n3 = float(input("Inserisci il terzo numero: "))

if n1 > n2 and n1 > n3:
    print("Il numero più grande è:", n1)
elif n2 > n1 and n2 > n3:
    print("Il numero più grande è:", n2)
elif n3 > n1 and n3 > n2:
    print("Il numero più grande è:", n3)


-----------------------
./Esercizi informatica/002.py
# Chiedi all'utente di inserire tre numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# Confronta i tre numeri utilizzando le istruzioni if, elif ed else
if numero1 > numero2 and numero1 > numero3:
    print("Il numero più grande è:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Il numero più grande è:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Il numero più grande è:", numero3)
else:
    print("I numeri sono uguali!")

-----------------------
./botta-alessio - Alessio Botta/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./esercizi informatica minetti giulio - Giulio Minetti/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./Surdich-Lorenzo - Lorenzo Surdich/002.py
a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))
c = float(input("Inserisci il terzo numero: "))

if a > b and a > c:
  print("Il numero più grande è:", a)
elif b > a and b > c:
  print("Il numero più grande è:", b)
else:
  print("Il numero più grande è:", c)

-----------------------
./Esercizi informatica 3/002.py
# Chiedi all'utente di inserire tre numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# Confronta i tre numeri utilizzando le istruzioni if, elif ed else
if numero1 > numero2 and numero1 > numero3:
    print("Il numero più grande è:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Il numero più grande è:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Il numero più grande è:", numero3)
else:
    print("I numeri sono uguali!")

-----------------------
./todde-lorenzo - lorenzo todde/002.py
def main(): 
    a = input("Inserisci il primo numero: ")
    b = input("Inserisci il secondo numero: ")
    c = input("Inserisci il terzo numero: ")
    if a >= b:
        if a >= c:
            print(a)
        elif b >= c:
            print(b)
        else:
            print(c)
    elif b >= c:
        print(b)
    else: 
        print(c)
main()

-----------------------
./dapino-berenice/002.py
def main(): 
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    c = float(input("Inserisci il terzo numero: "))
    if a>b: 
        if a>c: 
            print("Numero maggiore:", a)
        else:
            print("Numero maggiore:", c)

    else:
        if b>c:
            print("Numero maggiore:", b)
        else: 
            print("Numero maggiore:", c)



main()

-----------------------
./Esercizi informatica 2/002.py
# Chiedi all'utente di inserire tre numeri
numero1 = float(input("Inserisci il primo numero: "))
numero2 = float(input("Inserisci il secondo numero: "))
numero3 = float(input("Inserisci il terzo numero: "))

# Confronta i tre numeri utilizzando le istruzioni if, elif ed else
if numero1 > numero2 and numero1 > numero3:
    print("Il numero più grande è:", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("Il numero più grande è:", numero2)
elif numero3 > numero1 and numero3 > numero2:
    print("Il numero più grande è:", numero3)
else:
    print("I numeri sono uguali!")

-----------------------
./portella-francesco - Francesco Portella/002.py
def main():
    a = float(input('primo numero:'))
    b = float(input('secondo numero:'))
    c = float(input('terzo numero:'))
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >=c :
        print(b)
    else:
        print(c)

main()

-----------------------
./zumiani-sara.zip - Sara Zumiani/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./Hunag-Marco.zip - Marco Huang/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./zono veran - Fabrizio Verani/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/002.py
def max_3():
    a = float(input('1st number: '))
    b = float(input('2nd number: '))
    c = float(input('3rd number: '))
    
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
        
max_3()

-----------------------
./Matteo-Marazzi/002.py
n1 = float(input("Inserisci il primo numero: "))
n2 = float(input("Inserisci il secondo numero: "))
n3 = float(input("Inserisci il terzo numero: "))

if n1 > n2 and n1 > n3:
    print("Il numero più grande è:", n1)
elif n2 > n1 and n2 > n3:
    print("Il numero più grande è:", n2)
elif n3 > n1 and n3 > n2:
    print("Il numero più grande è:", n3)
