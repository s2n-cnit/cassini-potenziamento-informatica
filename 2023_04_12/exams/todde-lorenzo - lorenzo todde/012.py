def converter():
    meters = float(input('Inserisci i metri: '))
    statute_mile = meters/1609
    yards = meters*1.094
    feet = meters*3.281
    inches = meters*39.37
    print(str(statute_mile) + ' miglia terrestri')
    print(str(yards) + ' iarde')
    print(str(feet) + ' piedi')
    print(str(inches) + ' pollici')

converter()

