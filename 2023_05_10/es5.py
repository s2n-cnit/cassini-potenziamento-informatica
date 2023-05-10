# Scrivi una funzione in Python che prende due stringhe, conta il numero di volte che ogni stringa contiene gli stessi tre caratteri allo stesso indice. Stampa l’output.

s1 = "Red    Paper"
s2 = "Yellow Paper"


def conta_sottostringhe(s1, s2):
    output = 0
    for i in range(len(s1) - 2):
        if s1[i : i + 3] == s2[i : i + 3]:
            output = output + 1
    return output
