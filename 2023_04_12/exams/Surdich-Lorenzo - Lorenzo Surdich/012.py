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