indice = 0
counter = 0 #numero città con escursione termica maggiore
citta = ["Milano", "Roma", "Venezia"]
tmin = [] #temperatura minima
tmax = [] #temperatura massima
escursione = [] #escursione termica prefissata
differenza = [] #differenza escursioni termiche

for c in citta:
    print("a", citta[indice])
    e = int(input("Qual è il valore prefissato di escursione termica? "))
    escursione.append(e)
    indice += 1
print(escursione)

#ripetizione richiesta dei dati 
indice = 0
citta.clear()
tmin.clear()
tmax.clear()

for n in range(3):
    c = input("Qual è la città? ")
    citta.append(c)
    t1 = int(input("Qual è la sua temperatura minima? "))
    tmin.append(t1)
    t2 = int(input("Qual è la sua temperatura massima? "))
    tmax.append(t2)
    print()

#escursione termica
for c in citta:
    d = tmax[indice] - tmin[indice]
    differenza.append(d)
    indice += 1

print(differenza)
indice = 0
for c in citta:
    if differenza[indice] > escursione[indice]:
        counter += 1
    else:
        print("L'escursione termica della città", citta[indice],"è minore o nulla")
    indice += 1

print("Le città con escursione termica maggiore sono", counter)

























