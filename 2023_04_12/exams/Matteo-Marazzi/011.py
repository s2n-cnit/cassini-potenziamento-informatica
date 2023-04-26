def frequenza_caratteri(stringa):
    dizionario_frequenza = {}
    for char in stringa:
        if char in dizionario_frequenza:
            dizionario_frequenza[char] += 1
        else:
            dizionario_frequenza[char] = 1
    return dizionario_frequenza

