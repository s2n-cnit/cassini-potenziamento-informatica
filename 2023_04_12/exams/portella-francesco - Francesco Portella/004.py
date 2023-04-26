def main():
    carattere = input('inserisci un solo carattere: ')
    if len(carattere) != 1:
        print('non hai inserito un solo carattere')
    else:
        if carattere in 'aeiouAEIOU':
            print('il carattere è una vocale')
        else:
            print('il carattere non è una vocale')

main()