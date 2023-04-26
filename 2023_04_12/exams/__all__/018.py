

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/018.py
#
def perfetto(n):
    sm = 0
    for d in range(1, n):
        if n % d == 0:
            sm += d
    return sm == n


# -----------------------
# ./roggero_costantino/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./lin-matteo - Matth6ew/018.py
#
def is_perfect_number(num):
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False

input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./molinari-giorgia/018.py
#
def is_perfect_number(num):
    # Inizializza la somma dei divisori a 0
    divisors_sum = 0
    
    # Calcola la somma dei divisori
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Verifica se la somma dei divisori è uguale al numero stesso
    if divisors_sum == num:
        return True
    else:
        return False

# Esempio di utilizzo della funzione
input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/018.py
#
def is_perfect_number(num):
    # Inizializza la somma dei divisori a 0
    divisors_sum = 0
    
    # Calcola la somma dei divisori
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Verifica se la somma dei divisori è uguale al numero stesso
    if divisors_sum == num:
        return True
    else:
        return False

# Esempio di utilizzo della funzione
input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/018.py
#
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

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./alessandro-lugaro/018.py
#
def is_perfect_number(num):
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False


input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./botta-alessio - Alessio Botta/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/018.py
#
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

# -----------------------
# ./todde-lorenzo - lorenzo todde/018.py
#
def perfect(n):
    perf = 0
    for i in range(1, n-1):
        if n % i == 0:
            perf = perf + i
    if perf == n:
        print('PERFETTO')
    else:
        print('non perfetto')
perfect(5)
perfect(6)
perfect(28)
perfect(100)


# -----------------------
# ./portella-francesco - Francesco Portella/018.py
#
def is_perfect_number(num):
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False

input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./moretti-christian/018.py
#
def is_perfect_number(num):
    # Inizializza la somma dei divisori a 0
    divisors_sum = 0
    
    # Calcola la somma dei divisori
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Verifica se la somma dei divisori è uguale al numero stesso
    if divisors_sum == num:
        return True
    else:
        return False

# Esempio di utilizzo della funzione
input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./hu-xuan-di/018.py
#
def is_perfect_number(num):
    # Inizializza la somma dei divisori a 0
    divisors_sum = 0
    
    # Calcola la somma dei divisori
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Verifica se la somma dei divisori è uguale al numero stesso
    if divisors_sum == num:
        return True
    else:
        return False

# Esempio di utilizzo della funzione
input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/018.py
#
def is_perfect_number(num):
    # Inizializza la somma dei divisori a 0
    divisors_sum = 0
    
    # Calcola la somma dei divisori
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    # Verifica se la somma dei divisori è uguale al numero stesso
    if divisors_sum == num:
        return True
    else:
        return False

# Esempio di utilizzo della funzione
input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./zono veran - Fabrizio Verani/018.py
#
def is_perfect_number(num):
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False


input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/018.py
#
def is_perfect(num: int):
    divs = 0
    for n in range(num-1):
        if num%(n+1) == 0:
            divs += (n+1)
            
    if divs == num:
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

# -----------------------
# ./Matteo-Marazzi/018.py
#
def is_perfect_number(num):
    divisors_sum = 0
    
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    
    if divisors_sum == num:
        return True
    else:
        return False


input_num = int(input("Inserisci un numero: "))
if is_perfect_number(input_num):
    print(f"Il numero {input_num} è un numero perfetto.")
else:
    print(f"Il numero {input_num} non è un numero perfetto.")