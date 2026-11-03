n = int(input("¿Cuántos números primos quieres mostrar?"))

contador = 0
num = 2

while contador < n:
    primo = True
    for divisor in range(2, num):
        if num % divisor == 0:
            primo = False
        if primo: 
            print(num)
            contador += 1
        num += 1