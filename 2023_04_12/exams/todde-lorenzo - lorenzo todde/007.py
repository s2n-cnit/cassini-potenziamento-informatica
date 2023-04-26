def main():
    Nlist = input("inserisci tutti gli elementi: ")
    obj =  input("inserisci l'oggetto da trovare: ")
    if obj in Nlist:
        print('Presente')
        return obj.index

main()

