def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


# Esempio di lista di dizionari rappresentante una scuola
scuola = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 7, 6]},
    {"nome": "Luca", "cognome": "Bianchi", "classe": "2B", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanna", "cognome": "Verdi", "classe": "4C", "voti": [10, 9, 8, 10]},
]

# Chiamata alla funzione per calcolare e stampare la media dei voti di tutti gli studenti
calcola_media_voti(scuola)