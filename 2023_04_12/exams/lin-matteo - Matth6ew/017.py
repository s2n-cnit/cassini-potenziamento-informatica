def get_ascii_code(char):
    ascii_code = ord(char)
    return ascii_code

input_char = input("Inserisci un carattere: ")
ascii_code = get_ascii_code(input_char)
print(f"Il codice ASCII associato a '{input_char}' è: {ascii_code}")