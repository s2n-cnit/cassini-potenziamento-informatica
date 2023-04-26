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