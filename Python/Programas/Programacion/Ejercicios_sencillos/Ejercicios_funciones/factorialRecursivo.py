#Funcion recursiva: se lama a sí misma con un número más pequeño
def factorial(n):
    #Caso base: el factrial de 0 y e 1 es 1 (aqui se para la recursión)
    if n <= 1:
        return 1
    #Caso recursivo: n! = n * (n-1)!
    return n * factorial(n-1)


#Pedimos un número entero
numero = int(input("Introduce un número entero"))
#El factorial no existe para numeros negativos
if numero < 0: 
    print("No existe el factorial de un número negativo")
else:
    print(f"{numero}! ={factorial(numero)}")