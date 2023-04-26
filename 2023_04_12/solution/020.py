def print_senza_andare_a_capo():
    input_utente = input("Inserisci una stringa: ")
    while input_utente != "":
        print(input_utente, end=" ")
        input_utente = input("Inserisci una stringa: ")


print_senza_andare_a_capo()
