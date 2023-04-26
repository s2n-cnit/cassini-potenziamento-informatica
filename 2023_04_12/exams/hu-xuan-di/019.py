def filter_colors_by_letter(colors, letter):
    # Crea una nuova lista per i colori filtrati
    filtered_colors = []
    
    # Filtra i colori che iniziano con la lettera specificata
    for color in colors:
        if color.lower().startswith(letter.lower()):
            filtered_colors.append(color)
    
    return filtered_colors

# Crea una lista vuota per i colori
color_list = []

# Chiede all'utente di inserire 10 colori
for i in range(10):
    color = input(f"Inserisci il colore {i+1}: ")
    color_list.append(color)

# Chiede all'utente di inserire una lettera per filtrare i colori
letter = input("Inserisci una lettera per filtrare i colori: ")

# Chiama la funzione per filtrare i colori in base alla lettera inserita
filtered_colors = filter_colors_by_letter(color_list, letter)

# Stampa i colori filtrati
print(f"I colori che iniziano con la lettera '{letter}' sono:")
for color in filtered_colors:
    print(color)