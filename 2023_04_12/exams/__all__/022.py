

# -----------------------
# ./Baglietto-Luca - Luca Baglietto/022.py
#
import csv

def get_user():
    return {
        "username": input("username: "),
        "username": input("password: "),
        "email": input("email: "),
        "data_registr": input("data di degistrazione: ")
    }

def leggi():
    with open('names.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        res = []
        for row in reader:
            res.append(row)
    return res

def inizializza():
    with open('names.csv', 'w', newline='') as csvfile:
        fieldnames = ["username", "username", "email", "data_registr"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def aggiungi():
    with open('names.csv', 'a', newline='') as csvfile:
        fieldnames = ["username", "username", "email", "data_registr"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(get_user())

inizializza()
aggiungi()
print(leggi())

# -----------------------
# ./roggero_costantino/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

leggi_utenti()

# -----------------------
# ./lin-matteo - Matth6ew/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

leggi_utenti()

# -----------------------
# ./Zanardi-Leonardo.zip - leonardo zanardi/022.py
#
import csv

# Funzione per registrare un nuovo utente
def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


# Funzione per leggere e stampare a schermo i dati degli utenti registrati
def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


# Esempio di registrazione di un utente
registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

# Chiamata alla funzione per leggere e stampare a schermo i dati degli utenti registrati
leggi_utenti()

# -----------------------
# ./molinari-giorgia/022.py
#
import csv

# Funzione per registrare un nuovo utente
def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


# Funzione per leggere e stampare a schermo i dati degli utenti registrati
def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


# Esempio di registrazione di un utente
registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

# Chiamata alla funzione per leggere e stampare a schermo i dati degli utenti registrati
leggi_utenti()

# -----------------------
# ./porcile-filippo.zip - Filippo Porcile/022.py
#
import csv

# Funzione per registrare un nuovo utente
def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


# Funzione per leggere e stampare a schermo i dati degli utenti registrati
def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


# Esempio di registrazione di un utente
registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

# Chiamata alla funzione per leggere e stampare a schermo i dati degli utenti registrati

# -----------------------
# ./perkola_klaudia - Klaudia Perkola/022.py
#
import csv

def crea_file_csv(dizionario, nome_file):
    with open(nome_file, 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(['username', 'password', 'email', 'data_registrazione'])
        for utente in dizionario.values():
            writer.writerow([utente['username'], utente['password'], utente['email'], utente['data_registrazione']])

def leggi_file_csv(nome_file):
    with open(nome_file, 'r') as file_csv:
        reader = csv.reader(file_csv)
        for row in reader:
            print(row)

#dizionario degli utenti
utenti = {
    1: {'username': 'piero', 'password': 'p4ssw0rd', 'email': 'mario@gmail.com', 'data_registrazione': '2023-01-01'},
    2: {'username': 'lisa', 'password': 's3cr3t', 'email': 'luigi@yahoo.com', 'data_registrazione': '2023-01-02'},
    3: {'username': 'rita', 'password': 'p3ach', 'email': 'princess@castle.com', 'data_registrazione': '2023-01-03'}
}

#crea il file CSV
crea_file_csv(utenti, 'utenti.csv')

#legge il file CSV e stampa i dati a schermo
leggi_file_csv('utenti.csv')

# -----------------------
# ./ExamFrittoli - Lorenzo Frittoli/022.py
#
import csv

def writeusers()

# -----------------------
# ./alessandro-lugaro/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("Stefano_Lepri", "siuuum", "stefano.lepri@gmail.com", "2004-09-13")

leggi_utenti()

# -----------------------
# ./Surdich-Lorenzo - Lorenzo Surdich/022.py
#


# -----------------------
# ./portella-francesco - Francesco Portella/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

leggi_utenti()

# -----------------------
# ./moretti-christian/022.py
#
import csv

# Funzione per registrare un nuovo utente
def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


# Funzione per leggere e stampare a schermo i dati degli utenti registrati
def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


# Esempio di registrazione di un utente
registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

# Chiamata alla funzione per leggere e stampare a schermo i dati degli utenti registrati
leggi_utenti()

# -----------------------
# ./zumiani-sara.zip - Sara Zumiani/022.py
#


# -----------------------
# ./hu-xuan-di/022.py
#
import csv

# Funzione per registrare un nuovo utente
def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


# Funzione per leggere e stampare a schermo i dati degli utenti registrati
def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


# Esempio di registrazione di un utente
registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

# Chiamata alla funzione per leggere e stampare a schermo i dati degli utenti registrati
leggi_utenti()

# -----------------------
# ./Hunag-Marco.zip - Marco Huang/022.py
#


# -----------------------
# ./zono veran - Fabrizio Verani/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("mario_rossi", "mypassword", "mario.rossi@example.com", "2022-04-12")

leggi_utenti()

# -----------------------
# ./galvani-vezzi-lidia.zip - Lidia Galvani Vezzi/022.py
#


# -----------------------
# ./Matteo-Marazzi/022.py
#
import csv

def registrati(username, password, email, data_registrazione):
    utente = {"username": username, "password": password, "email": email, "data_registrazione": data_registrazione}
    with open('utenti.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=utente.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(utente)
    print("Utente registrato con successo!")


def leggi_utenti():
    with open('utenti.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("Username: {}, Password: {}, Email: {}, Data Registrazione: {}".format(row["username"], row["password"], row["email"], row["data_registrazione"]))


registrati("Stefano_Lepri", "siuuum", "stefano.lepri@gmail.com", "2004-09-13")

leggi_utenti()