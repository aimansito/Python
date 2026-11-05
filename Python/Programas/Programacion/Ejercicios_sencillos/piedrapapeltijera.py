def es_multiplo(a,b):
    if b == 0:
        resultado = (a == 0)
    else:
        resultado (a % b == 0)
    return resultado
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número"))

if es_multiplo(num1,num2):
    input(num1," es múltiplo de ",num2)

if es_multiplo(num2, num1):
    input(num2," es multiplo de ", num1)

if es_multiplo(num1, num2) and not es_multiplo(num2,num1):
    input("")