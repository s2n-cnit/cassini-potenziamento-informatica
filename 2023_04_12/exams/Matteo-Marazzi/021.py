def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


scuola = [
    {"nome": "Matteo", "cognome": "Marazzi", "classe": "3G", "voti": [8, 7, 6]},
    {"nome": "Fabrizio", "cognome": "Verani", "classe": "1E", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanni", "cognome": "Rana", "classe": "2D", "voti": [10, 9, 8, 10]},
]

calcola_media_voti(scuola)