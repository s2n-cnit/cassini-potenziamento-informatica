def valuta_sport(sport_set):
    sport_di_squadra = {"calcio", "curling", "basket", "rugby"}
    sport_individuale = {"atletica", "arrampicata", "tennis", "ginnastica"}

    for sport in sport_set:
        if sport.lower() in sport_di_squadra:
            print("{} è uno sport di squadra.".format(sport))
        elif sport.lower() in sport_individuale:
            print("{} è uno sport individuale.".format(sport))
        else:
            print("{} non è uno sport definito.".format(sport))


sport_preferiti = {"calcio", "atletica", "tennis", "pallavolo"}
valuta_sport(sport_preferiti)