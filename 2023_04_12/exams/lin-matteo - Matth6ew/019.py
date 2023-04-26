def filter_colors_by_letter(colors, letter):
    filtered_colors = []
    
    for color in colors:
        if color.lower().startswith(letter.lower()):
            filtered_colors.append(color)
    
    return filtered_colors

color_list = []

for i in range(10):
    color = input(f"Inserisci il colore {i+1}: ")
    color_list.append(color)

letter = input("Inserisci una lettera per filtrare i colori: ")

filtered_colors = filter_colors_by_letter(color_list, letter)

print(f"I colori che iniziano con la lettera '{letter}' sono:")
for color in filtered_colors:
    print(color)