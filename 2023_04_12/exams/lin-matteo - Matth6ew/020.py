def get_user_inputs():
    inputs = []
    while True:
        user_input = input("Inserisci un input (INVIO per terminare): ")
        if user_input == "":
            break
        inputs.append(user_input)
    return inputs

user_inputs = get_user_inputs()

print("Gli input dell'utente sono:", end=" ")
for input_value in user_inputs:
    print(input_value, end=" ")