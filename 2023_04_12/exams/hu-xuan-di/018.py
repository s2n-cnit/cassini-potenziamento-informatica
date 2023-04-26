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