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