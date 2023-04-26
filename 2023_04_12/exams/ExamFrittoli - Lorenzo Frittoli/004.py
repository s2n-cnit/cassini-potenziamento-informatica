def is_vocal():
    char = input('Letter: ').lower()
    vocals = ['a', 'e', 'i', 'o', 'u']
    if char in vocals:
        print('y')
    else:
        print('n')
        
is_vocal()