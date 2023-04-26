def main():
    numbers = input("inserisci i numeri che vuoi moltiplicare: ")
    numbers_list = numbers.split()
    sumtot = 1
    for i in numbers_list:
        sumtot = sumtot * float(i)
    print(sumtot)

main()
