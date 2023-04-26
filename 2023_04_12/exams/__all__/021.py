

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/021.py
#
def elenca(studenti):
    if len(studenti) == 0:
        print("Nessuno studente")
        return
    sm = 0
    cnt = 0
    for s in studenti:
        print(s["nome"], s["cognome"], s["classe"])
        sm += sum(s["voti"])
        cnt += len(s["voti"])
    print("Media generale:", sm/cnt)


# -----------------------
# ./roggero_costantino/021.py
#
def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


scuola = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 7, 6]},
    {"nome": "Luca", "cognome": "Bianchi", "classe": "2B", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanna", "cognome": "Verdi", "classe": "4C", "voti": [10, 9, 8, 10]},
]

calcola_media_voti(scuola)

# -----------------------
# ./lin-matteo - Matth6ew/021.py
#
def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


scuola = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 7, 6]},
    {"nome": "Luca", "cognome": "Bianchi", "classe": "2B", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanna", "cognome": "Verdi", "classe": "4C", "voti": [10, 9, 8, 10]},
]

calcola_media_voti(scuola)

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/021.py
#
def scuoletta(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')

# -----------------------
# ./molinari-giorgia/021.py
#
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

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/021.py
#
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

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/021.py
#
def segreteria(studenti):
    for studente in studenti:
        media_voti = sum(studente["voti"]) / len(studente["voti"])
        studente["media"] = media_voti
    return studenti

studenti = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [6, 7, 8]},
    {"nome": "Luigi", "cognome": "Bianchi", "classe": "3A", "voti": [7, 8, 9]},
    {"nome": "Anna", "cognome": "Verdi", "classe": "3B", "voti": [8, 9, 10]},
]

media_studenti = segreteria(studenti)
print(f"{media_studenti}/n")

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/021.py
#
def scuoletta(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')

# -----------------------
# ./alessandro-lugaro/021.py
#
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

# -----------------------
# ./botta-alessio - Alessio Botta/021.py
#
def scuoletta(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')

# -----------------------
# ./esercizi informatica minetti giulio - Giulio Minetti/021.py
#
def scuoletta(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/021.py
#
def stampa_media_studenti(school):
    for studente in school:
        # Stampiamo nome e cognome dello studente
        print(f"{studente['nome']} {studente['cognome']}")

        # Calcoliamo la media dei voti dello studente
        voti = studente['voti']
        media = sum(voti) / len(voti)
        
        # Stampiamo la media dei voti
        print(f"Media voti: {media:.2f}\n")

# -----------------------
# ./portella-francesco - Francesco Portella/021.py
#
def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


scuola = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 7, 6]},
    {"nome": "Luca", "cognome": "Bianchi", "classe": "2B", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanna", "cognome": "Verdi", "classe": "4C", "voti": [10, 9, 8, 10]},
]

calcola_media_voti(scuola)

# -----------------------
# ./moretti-christian/021.py
#
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

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/021.py
#


# -----------------------
# ./hu-xuan-di/021.py
#
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

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/021.py
#


# -----------------------
# ./zono veran - Fabrizio Verani/021.py
#
def calcola_media_voti(studenti):
    for studente in studenti:
        nome = studente["nome"]
        cognome = studente["cognome"]
        classe = studente["classe"]
        voti = studente["voti"]
        media_voti = sum(voti) / len(voti) if voti else 0
        print("Nome: {}, Cognome: {}, Classe: {}, Voti: {}, Media voti: {:.2f}".format(nome, cognome, classe, voti, media_voti))


scuola = [
    {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 7, 6]},
    {"nome": "Luca", "cognome": "Bianchi", "classe": "2B", "voti": [9, 8, 7, 9]},
    {"nome": "Giovanna", "cognome": "Verdi", "classe": "4C", "voti": [10, 9, 8, 10]},
]

calcola_media_voti(scuola)

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/021.py
#
def scuola(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')



# -----------------------
# ./Matteo-Marazzi/021.py
#
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