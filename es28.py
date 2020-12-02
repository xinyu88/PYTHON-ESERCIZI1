print("ecco la lista dei studenti e i loro corrispondenti lanci effettuati")

#uso dizionario 

lista = {
    "marco" : 2.0,
    "camilla": 1.2,
    "fabio" : 2.5,
    "giulio" : 2.7 

}
print(lista)

#il vincitore dovrebbe essere giulio

if lista["marco"] > lista["camilla"] and lista["fabio"] and lista["giulio"] :
    print("il vincitore è marco con 2.0 come valore max ")

if lista["camilla"] > lista["marco"] and lista["fabio"] and lista["giulio"] :
    print("il vincitore è camilla con 1.2 come valore max")

if lista["fabio"] > lista["camilla"] and lista["marco"] and lista["giulio"] :
    print("il vincitore è fabio con 2.5 come valore max  ")

else : 
    print("il vincitore è giulio con 2.7 come valore max")