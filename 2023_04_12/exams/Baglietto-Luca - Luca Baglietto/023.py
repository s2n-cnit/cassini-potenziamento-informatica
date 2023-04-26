if __name__ == "__main__":
    title = input("Inserisci il titolo: ")
    print("Scrivi la canzone")
    with open(title+".txt", "w") as f:
        while True:
            t = input()
            if t == '':
                break
            f.write(t+'\n')
    print("Canzone salvata")