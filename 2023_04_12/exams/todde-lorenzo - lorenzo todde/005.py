def main():
    numbers = input("inserisci i numeri che vuoi sommare: ")
    numbers_list = numbers.split()
    sumtot = 0
    for i in numbers_list:
        sumtot = sumtot + float(i)
    print(sumtot)

main()

