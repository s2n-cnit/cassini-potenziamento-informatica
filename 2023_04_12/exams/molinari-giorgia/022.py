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