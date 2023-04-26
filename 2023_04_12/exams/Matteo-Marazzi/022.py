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