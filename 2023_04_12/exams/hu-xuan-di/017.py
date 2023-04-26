def get_ascii_code(char):
    # Ottiene il codice ASCII del carattere
    ascii_code = ord(char)
    return ascii_code

# Esempio di utilizzo della funzione
input_char = input("Inserisci un carattere: ")
ascii_code = get_ascii_code(input_char)
print(f"Il codice ASCII associato a '{input_char}' è: {ascii_code}")