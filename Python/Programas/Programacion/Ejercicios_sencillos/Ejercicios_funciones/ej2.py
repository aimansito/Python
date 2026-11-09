# Ejercicio 2: función EsMultiplo y comprobar si un número es múltiplo del otro


# Función que devuelve True si num1 es múltiplo de num2
def es_multiplo(num1, num2):
    # Si num2 es 0 no se puede dividir, así que no lo consideramos múltiplo
    if num2 == 0:
        # Devolvemos False
        return False
    # Es múltiplo si el resto de la división es 0
    return num1 % num2 == 0


# Pedimos el primer número
a = int(input("Introduce el primer número: "))
# Pedimos el segundo número
b = int(input("Introduce el segundo número: "))

# Si a es múltiplo de b
if es_multiplo(a, b):
    # Lo indicamos
    print(f"{a} es múltiplo de {b}")
# Si no, comprobamos si b es múltiplo de a
elif es_multiplo(b, a):
    # Lo indicamos
    print(f"{b} es múltiplo de {a}")
# Si ninguno es múltiplo del otro
else:
    # Lo indicamos
    print("Ninguno es múltiplo del otro")
