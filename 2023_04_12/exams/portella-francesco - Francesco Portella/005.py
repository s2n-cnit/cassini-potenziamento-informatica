def main():
    inputnum = input('inserire lista numeri:')
    lista = inputnum.split()
    sum = 0
    for i in range(len(lista)):
        sum = sum + float(lista[i])
    print(sum)

main()