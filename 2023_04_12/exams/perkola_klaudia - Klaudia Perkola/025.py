def valuta_sport(sport_set):
    # Definizione di uno sport di squadra e uno sport individuale
    sport_di_squadra = {"calcio", "basket", "volley", "rugby", "hockey"}
    sport_individuale = {"atletica", "nuoto", "tennis", "golf", "pallavolo"}

    # Confronto tra lo sport inserito e gli sport definiti
    for sport in sport_set:
        if sport.lower() in sport_di_squadra:
            print("{} è uno sport di squadra.".format(sport))
        elif sport.lower() in sport_individuale:
            print("{} è uno sport individuale.".format(sport))
        else:
            print("{} non è uno sport definito.".format(sport))
