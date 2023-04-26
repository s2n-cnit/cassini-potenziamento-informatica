def main(): 
    days = int(input("Giorni:"))
    hours = int(input("Ore:"))
    minute = int(input("Minuti:"))

    sec = minute * 60 + hours * 60**2 + days* ((60**2)*24)

    print("Secondi:", sec)

main()