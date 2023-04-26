def vocal():
    char = input('Letter: ')
    vocals = ['a', 'e', 'i', 'o', 'u']
    if char in vocals:
        print('yes')
    else:
        print('no')
        
vocal()