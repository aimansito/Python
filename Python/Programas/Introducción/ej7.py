import math
nota1 = int(input("Introduce la nota del primer examen"))
mediaDeseada = int(input("Introduce la media deseada"))
nota2 = (mediaDeseada - nota1 * 0.4) / 0.6
print("Para tener la nota media de un ",mediaDeseada, " tienes que sacar un ",nota2," en el segundo examen")
