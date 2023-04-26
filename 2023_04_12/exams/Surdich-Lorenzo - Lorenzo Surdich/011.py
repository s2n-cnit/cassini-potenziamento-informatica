def frequenza_caratteri(stringa):
    dizionario = {}
    for carattere in stringa:
        if carattere in dizionario:
            dizionario[carattere] += 1
        else:
            dizionario[carattere] = 1
    return dizionario