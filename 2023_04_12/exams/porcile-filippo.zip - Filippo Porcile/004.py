# Chiedi all'utente di inserire un carattere
carattere = input("Inserisci un carattere: ")

# Verifica se il carattere è una vocale
if carattere in "aeiouAEIOU":
    print("Il carattere inserito è una vocale.")
else:
    print("Il carattere inserito non è una vocale.")