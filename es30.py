
#da un numero binario a numero decimale
c = 0
somma = [] #per fare la somma finale

#chiedere cifre del numero binario
binario = int(input("quante cifre è composto il numero binario ?"))
print ("inserire la cifra del numero binario da destra a sinistra")
print("ricordo che le cifre dei numeri binari sono : 0 e 1")
for cifre in range(binario): 
    numero = int(input("quel'è la cifra ")) #cifre binari 1 e 0
    valore = (2** c)*numero 
    somma.append(valore) #aggiungere allora somma (per calcolo numero decimale)
    c +=1

#calcolo numero decimale
print("il numero decimale è", sum(somma))



    
























