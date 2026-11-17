# Ejemplo 08: listas (lista1.pdf y lista2.pdf)

# ------------------------------------------------------------
# Crear listas y acceder por índice (el primero es el 0)
# ------------------------------------------------------------

# Lista con datos de distinto tipo
a = [90, "Python", 3.87]
# Primer elemento
print(a[0])
# Segundo elemento
print(a[1])
# Índice negativo: -1 es el último
print(a[-1])
# Lista vacía
vacia = []
# Lista creada con list() a partir de algo iterable (una cadena)
letras = list("hola")
# Mostramos
print(vacia, letras)

# Modificar un elemento
mi_lista = [10, "hola", "Pepe", 25]
# Antes
print("inicialmente", mi_lista[2])
# Cambiamos la posición 2
mi_lista[2] = "Juan"
# Después
print("ahora es", mi_lista[2])

# Eliminar un elemento por posición con del
del mi_lista[1]
# Mostramos
print(mi_lista)

# Acceder fuera de la lista da error IndexError: hay que comprobarlo antes
posicion = 10
# Comprobamos que la posición existe
if posicion >= 0 and posicion < len(mi_lista):
    # Existe
    print(mi_lista[posicion])
else:
    # No existe
    print("La posición", posicion, "no existe")

# ------------------------------------------------------------
# Sublistas (slices): lista[inicio:fin:paso]  (fin NO se incluye)
# ------------------------------------------------------------

# Lista de ejemplo
mi_lista = [10, 'hola', 'Juan', 25]
# Del 0 al 1
print(mi_lista[0:2])
# Desde el principio hasta el 1
print(mi_lista[:2])
# Desde el 2 hasta el final
print(mi_lista[2:])
# Copia completa
print(mi_lista[:])
# De dos en dos
print(mi_lista[::2])
# Al revés
print(mi_lista[::-1])

# Modificar varios elementos a la vez con un slice
a = [1, 2, 3, 4, 5, 6]
# Cambiamos las posiciones 1 y 2
a[1:3] = [7, 7]
# [1, 7, 7, 4, 5, 6]
print(a)
# Repartir valores de la lista en variables
x, y, z = a[3:]
# 4 5 6
print(x, y, z)

# ------------------------------------------------------------
# Listas anidadas
# ------------------------------------------------------------

# Lista dentro de lista
b = [1, 2, 3, ['p', 'q', [5, 6, 7]]]
# 'p'
print(b[3][0])
# 5
print(b[3][2][0])

# ------------------------------------------------------------
# Recorrer (iterar) listas
# ------------------------------------------------------------

# Lista de nombres
amigos = ['Juan', 'Dionisio', 'Pepe', 'Manolo']
# Solo los elementos
for amigo in amigos:
    # Saludamos a cada uno
    print(f'Hola {amigo}')
# Posición y elemento con enumerate
for posicion, amigo in enumerate(amigos):
    # Mostramos los dos
    print(posicion, amigo)
# Por índices con range y len (posiciones pares)
for i in range(0, len(amigos), 2):
    # Elemento de la posición i
    print(i, amigos[i])
# Dos listas a la vez con zip
notas = [5, 9, 7, 6]
# Cogemos un amigo y su nota en cada vuelta
for amigo, nota in zip(amigos, notas):
    # Mostramos los dos
    print(amigo, nota)

# ------------------------------------------------------------
# Operaciones: ordenar, máximo, mínimo, longitud
# ------------------------------------------------------------

# Lista de números
numeros = [7, 3, 9, 1]
# Ordena LA PROPIA lista (no devuelve nada)
numeros.sort()
# [1, 3, 7, 9]
print(numeros)
# Orden inverso
numeros.sort(reverse=True)
# [9, 7, 3, 1]
print(numeros)
# sorted() devuelve una lista nueva ordenada y no toca la original
print(sorted(numeros), numeros)
# Ordenar cadenas sin distinguir mayúsculas
palabras = ['hola', 'ola', 'Hola', 'hOLA']
# key=str.lower compara todo en minúsculas
palabras.sort(key=str.lower)
# Mostramos
print(palabras)
# Máximo, mínimo y longitud
print(max(numeros), min(numeros), len(numeros))

# ------------------------------------------------------------
# Búsquedas: in, index, count
# ------------------------------------------------------------

# Lista de nombres
mi_lista = ['Juan', 'Dionisio', 'Pepe', 'Manolo']
# in devuelve True o False (distingue mayúsculas)
print('Juan' in mi_lista, 'juan' in mi_lista)
# index: posición del elemento (si no está da ValueError: comprobar antes con in)
if 'Pepe' in mi_lista:
    # Mostramos la posición
    print("Pepe está en la posición", mi_lista.index('Pepe'))
# count: cuántas veces aparece
print(mi_lista.count('Juan'), mi_lista.count('juan'))

# ------------------------------------------------------------
# Edición: append, insert, remove, pop, clear, copy, reverse, extend
# ------------------------------------------------------------

# Lista de partida
lista = [1, 2, 3]
# Añadir al final
lista.append(4)
# Insertar en la posición 0
lista.insert(0, 0)
# Quitar el primer elemento con ese valor
lista.remove(2)
# [0, 1, 3, 4]
print(lista)
# pop() quita y devuelve el último
ultimo = lista.pop()
# pop(i) quita y devuelve el de la posición i
primero = lista.pop(0)
# Mostramos lo quitado y cómo queda
print(ultimo, primero, lista)
# Copia independiente (si no, las dos variables serían la misma lista)
copia = lista.copy()
# Cambiamos la copia
copia.append(99)
# La original no cambia
print(lista, copia)
# Invertir la propia lista
copia.reverse()
# Mostramos
print(copia)
# Añadir todos los elementos de otra lista
lista.extend([5, 6])
# Equivale a sumar listas
lista = lista + [7]
# Mostramos
print(lista)
# Vaciar la lista
lista.clear()
# []
print(lista)

# ------------------------------------------------------------
# Creación dinámica de listas
# ------------------------------------------------------------

# Valor de pi aproximado
pi = 3.14
# Radios de partida
radios = [2.0, 35, 7.1]
# Forma 1: lista vacía + bucle + append
circunferencias = []
# Recorremos los radios
for radio in radios:
    # Añadimos el cálculo
    circunferencias.append(radio * pi)
# Mostramos
print(circunferencias)
# Forma 2: comprensión de listas (lo mismo en una línea)
circunferencias = [pi * num for num in radios]
# Mostramos
print(circunferencias)

# ------------------------------------------------------------
# Algoritmia típica con listas (hecho a mano, sin max/sum)
# ------------------------------------------------------------

# Lista de temperaturas
temperaturas = [18, 22, 15, 25, 20]
# Suponemos que el primero es el mayor
mayor = temperaturas[0]
# Acumulador para la suma
total = 0
# Recorremos la lista
for t in temperaturas:
    # Si encontramos uno mayor, lo guardamos
    if t > mayor:
        # Nuevo mayor
        mayor = t
    # Acumulamos
    total += t
# Mostramos mayor y media
print("Mayor:", mayor, "Media:", total / len(temperaturas))
