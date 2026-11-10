def mcd(a, b):
    #Si a es menor que b, los intercambiamos para dividir el mayor entre el menor 
    if a < b:
        a, b = b, a
    #Calculamos el resto de dividir eel mayor entre el menor
    resto = a % b
    #Mientras la división no sea exacta
    while resto != 0:
        #El divisor pasa a ser el dividendo
        a = b
        #El resto pasa a ser el divisor
        b = resto
        #Volvemos a calcular el resto
        resto = a % b

    # Cuando la división es exacta, el último divisor es el mcd
    return b 

#Pedimos el primer número
num1 = int(input("Introduce el primer número"))
#Pedimos el segundo número
num2 = int(input("Introduce el segundo número"))
#Si alguno es 0 negativo, el método no se aplica
if num1 <= 0 or num2 <= 0:
    print("Los numeros deben ser enteros positivos")
else: 
    print(f"El MCD de {num1} y {num2} es {(mcd(num1,num2))}")
