def elenca(studenti):
    if len(studenti) == 0:
        print("Nessuno studente")
        return
    sm = 0
    cnt = 0
    for s in studenti:
        print(s["nome"], s["cognome"], s["classe"])
        sm += sum(s["voti"])
        cnt += len(s["voti"])
    print("Media generale:", sm/cnt)
