caden = input ("Introduce una cadena")
while True:
    caract = input("Introduce un caracter")
    if len(caract) == 1:
        break
contador = 0
caden = caden.lower()
caract = caract.lower()

for i in range(len(caden)):
    if caden[i] == caract: 
        contador += 1
print (f"La palabra {caden} incluye la letra {caract} {contador} veces")