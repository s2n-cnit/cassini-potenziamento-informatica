def stampa_media_studenti(school):
    for studente in school:
        # Stampiamo nome e cognome dello studente
        print(f"{studente['nome']} {studente['cognome']}")

        # Calcoliamo la media dei voti dello studente
        voti = studente['voti']
        media = sum(voti) / len(voti)
        
        # Stampiamo la media dei voti
        print(f"Media voti: {media:.2f}\n")