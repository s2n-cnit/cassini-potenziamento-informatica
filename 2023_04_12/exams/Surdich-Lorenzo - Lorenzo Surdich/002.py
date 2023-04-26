a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))
c = float(input("Inserisci il terzo numero: "))

if a > b and a > c:
  print("Il numero più grande è:", a)
elif b > a and b > c:
  print("Il numero più grande è:", b)
else:
  print("Il numero più grande è:", c)