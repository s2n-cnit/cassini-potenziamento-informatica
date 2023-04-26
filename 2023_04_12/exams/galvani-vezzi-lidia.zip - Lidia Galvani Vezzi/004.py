def vocal():
    char = input('Letter: ').lower()
    vocals = ['a', 'e', 'i', 'o', 'u']
    if char in vocals:
        print('yes')
    else:
        print('no')
        
vocal()