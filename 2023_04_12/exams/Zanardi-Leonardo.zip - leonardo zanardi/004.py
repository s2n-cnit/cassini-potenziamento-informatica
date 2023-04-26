def is_vocal():
    char = input('Lettera = ')
    vocals = ['a', 'e', 'i', 'o', 'u']
    if char in vocals:
        print('giusto')
    else:
        print('sbagliato')
        
is_vocal()