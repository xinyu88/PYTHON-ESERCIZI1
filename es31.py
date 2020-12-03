#rappresentazione in binario di un numero decimale 

decimale = []
n = int(input("inserisci il numero decimale da trasformare in binario"))
quoziente = 1
for cifre in range(n)
while True : 
    if n == 0 and quoziente == 0 : 
        break
    else : 
        resto = n % 2  #utilizzo % per il calcolo del resto = prima cifra del numero binario
        decimale.append(resto)

decimale.reverse()
print(decimale)


decimale = []
n= int(input("inserisci il numero decimale da trasformare in binario"))
quoziente = 1

while True : 
    if n ==0 and quoziente == 0  : 
        print()
        break
    else : 
        resto = n % 2
        decimale.append(resto)
        quoziente = n

decimale.reverse()
print(decimale)

num = int(input("Qual è il numero decimale da trasformare? "))
n = num
binario = [] #lista con tutti i resti delle divisioni
quoziente = 1
while True:
    if num == 0 or quoziente == 0:
        break
    elif quoziente <= num:
        quoziente = round(num / 2)
        resto = num%2
        binario.append(resto)
        num = quoziente
    else:
        num = round(quoziente / 2)
        resto = quoziente%2
        binario.append(resto)
        quoziente = num

binario.reverse()
print(binario)

















   



