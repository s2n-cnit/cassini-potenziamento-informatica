def scuola(students: list):
    for s in students:
        print(f'Nome: {s['Nome']}')
        print(f'Cognome: {s['Cognome']}')
        print(f'Media: {sum(s['Voti'])/len(s['Voti'])}')

