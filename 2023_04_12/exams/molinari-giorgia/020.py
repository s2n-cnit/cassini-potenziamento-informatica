def get_user_inputs():
    inputs = []
    while True:
        user_input = input("Inserisci un input (INVIO per terminare): ")
        if user_input == "":
            break
        inputs.append(user_input)
    return inputs

# Chiamata alla funzione per ottenere gli input dall'utente
user_inputs = get_user_inputs()

# Stampa gli input ottenuti senza andare a capo
print("Gli input dell'utente sono:", end=" ")
for input_value in user_inputs:
    print(input_value, end=" ")