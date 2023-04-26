if __name__ == '__main__':
    letter = input("Inserisci una lettera: ")
    if len(letter) != 1:
        print("Input invalido")
    else:
        if letter in "aeiou":
            print("Vocale")
        else:
            print("Non una vocale")
