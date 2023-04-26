def time():
    d = int(input('giorni: '))
    h = int(input('ore: '))
    m = int(input('minuti: '))
    
    t = ((d*24 + h)*60 + m)*60
    print(f'secondi: {t}')
    
time()