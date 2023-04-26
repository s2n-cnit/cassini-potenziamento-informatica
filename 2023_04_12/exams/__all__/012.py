

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/012.py
#
def converti(metri):
    print(f"{metri/1609.344:.5} Miglia terrestri")
    print(f"{metri/0.9144:.5} Iarde")
    print(f"{metri/0.3048:.5} Piedi")
    print(f"{metri/0.0254:.5} Pollici")
converti(100)

# -----------------------
# ./roggero_costantino/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./lin-matteo - Matth6ew/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/012.py
#
def freedom_converter():
    meters = float(input('Lunghezza di input in una unità a scelta: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./molinari-giorgia/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/012.py
#
def americana(metri):
    conversions = dict()
    conversions["miglia"] = metri / 1609.344
    conversions["piedi"] = metri * 3.280840
    conversions["pollici"] = metri * 39.37008
    conversions["iarde"] = metri * 1.093613

    print(f"{metri} metri corrispondono a:")
    for key, value in conversions.items():
        print(f"{key}: {value}")

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./alessandro-lugaro/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)


# -----------------------
# ./botta-alessio - Alessio Botta/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/012.py
#
def freedom_converter():
    meters = input('Input length in non-idiotic unit: ')
    print('Miglia terrestri: ' + 1609.344 * meters)
    print('Iarde: ' + 0.9144 * meters)
    print('Piedi: ' + 0.3048 * meters)
    print('Pollici: ' + 0.0254 * meters)
    
freedom_converter()

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/012.py
#
def meters_to_imperial(meters):
    miles = meters / 1609.344
    yards = meters * 1.09361
    feet = meters * 3.28084
    inches = meters * 39.3701
    print(f"{meters} meters are:")
    print(f"{miles:.3f} miles")
    print(f"{yards:.1f} yards")
    print(f"{feet:.1f} feet")
    print(f"{inches:.1f} inches")

meters = float(input("Insert meters: "))
meters_to_imperial(meters)

# -----------------------
# ./todde-lorenzo - lorenzo todde/012.py
#
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



# -----------------------
# ./dapino-berenice/012.py
#
def main(): 
    metri = int(input("Metri: "))
    inch = 0.0254
    foot = 0.3048
    print("Polici: ", metri*inch)
    print("Piedi:", metri*foot)
    print("Iarde:", metri*3*foot)
    print("Miglia terrestri:", metri*3*foot*1760)

main()

# -----------------------
# ./portella-francesco - Francesco Portella/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./moretti-christian/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./hu-xuan-di/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/012.py
#
def freedom_converter():
    meters = float(input('Lunghezza di input in una unità a scelta: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./zono veran - Fabrizio Verani/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/012.py
#
def freedom_converter():
    meters = float(input('Input length in non-idiotic unit: '))
    print(f'Miglia terrestri: {1609.344 * meters}')
    print(f'Iarde: {0.9144 * meters}')
    print(f'Piedi: {0.3048 * meters}')
    print(f'Pollici: {0.0254 * meters}')
    
freedom_converter()

# -----------------------
# ./Matteo-Marazzi/012.py
#
def converti_unita_di_misura(metri):
    pollice = metri / 0.0254
    piede = metri / 0.3048
    iarda = metri / 0.9144
    miglia = metri / 1609.344

    print("Equivalente in pollici:", pollice)
    print("Equivalente in piedi:", piede)
    print("Equivalente in iarde:", iarda)
    print("Equivalente in miglia terrestri:", miglia)
