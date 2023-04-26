def colours():
    cols = list(input('Input 10 colours: ').strip().split(','))
    pref = input('Input 1st letter: ')
    for c in cols:
        if c.startswith(pref):
            print(c)
            
colours()