def main():
    numbers = input("inserisci i numeri che vuoi confrontare: ")
    numbers_list = numbers.split()
    max_number = 0
    for i in numbers_list:
        if int(i) >= max_number:
            max_number = int(i)
    print(max_number)

main()

