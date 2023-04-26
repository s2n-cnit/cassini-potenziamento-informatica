def sport(sport_preferito):
    sport_squadra = {"calcio", "basket", "volley", "hockey su ghiaccio",
                     "rugby", "football", "curling"}
    sport_individuale = {"tennis", "golf", "pugilato", "atletica", "surf",
                         "nuoto", "ciclismo", "judo"}

    if sport_preferito.lower() in sport_squadra:
        print("Il tuo sport preferito è uno sport di squadra.")
    elif sport_preferito.lower() in sport_individuale:
        print("Il tuo sport preferito è uno sport individuale.")
    else:
        print("Mi dispiace, non conosco questo sport.")


sport("tennis")
