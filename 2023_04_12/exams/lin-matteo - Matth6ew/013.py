def time():
    d = int(input('Days: '))
    h = int(input('Hours: '))
    m = int(input('Minutes: '))
    
    t = ((d*24 + h)*60 + m)*60
    print(f'Seconds elapsed: {t}')
    
time()