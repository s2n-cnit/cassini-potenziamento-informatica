num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Inserisci il secondo numero: "))

if num1 > num2:
    print(num1, "è il numero più grande")
elif num2 > num1:
    print(num2, "è il numero più grande")
else:
    print("I numeri sono uguali")