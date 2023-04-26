def input_senza_andare_a_capo():
    inputs = []

    while True:
        user_input = input()
        if user_input == '':
            break  
        inputs.append(user_input)

    print(''.join(inputs), end='')

input_senza_andare_a_capo()