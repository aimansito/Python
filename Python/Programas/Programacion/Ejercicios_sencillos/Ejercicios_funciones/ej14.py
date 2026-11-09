# Ejercicio 14: pila (el último en entrar es el primero en salir) con un vector de 10

# Tamaño máximo de la pila
TAMANO = 10
# Carácter que indica "posición vacía"
VACIO = "*"


# Crea y devuelve una pila con todas las posiciones vacías
def inicializar_pila():
    # Lista de 10 elementos con el carácter de vacío
    return [VACIO] * TAMANO


# Devuelve cuántos elementos tiene la pila
def longitud_pila(pila):
    # Contador de elementos
    contador = 0
    # Recorremos las posiciones
    for elemento in pila:
        # Si la posición no está vacía
        if elemento != VACIO:
            # Contamos un elemento
            contador = contador + 1
    # Devolvemos el total
    return contador


# Devuelve True si la pila no tiene elementos
def esta_vacia_pila(pila):
    # Está vacía si su longitud es 0
    return longitud_pila(pila) == 0


# Devuelve True si la pila está llena
def esta_llena_pila(pila):
    # Está llena si su longitud es igual al tamaño
    return longitud_pila(pila) == TAMANO


# Añade una cadena a la pila si no está llena
def add_pila(cadena, pila):
    # Si está llena
    if esta_llena_pila(pila):
        # Mostramos un error
        print("Error: la pila está llena")
    # Si hay hueco
    else:
        # La siguiente posición libre es justo la longitud actual
        pila[longitud_pila(pila)] = cadena


# Saca y devuelve el último elemento añadido
def sacar_de_la_pila(pila):
    # Si está vacía
    if esta_vacia_pila(pila):
        # Mostramos un error
        print("Error: la pila está vacía")
        # Devolvemos None porque no hay nada que sacar
        return None
    # La posición del último elemento es longitud - 1
    posicion = longitud_pila(pila) - 1
    # Guardamos el elemento
    elemento = pila[posicion]
    # Marcamos esa posición como vacía
    pila[posicion] = VACIO
    # Devolvemos el elemento sacado
    return elemento


# Muestra en pantalla los elementos de la pila (de arriba abajo)
def escribir_pila(pila):
    # Si está vacía
    if esta_vacia_pila(pila):
        # Lo indicamos
        print("La pila está vacía")
    # Si tiene elementos
    else:
        # Recorremos desde el último elemento hasta el primero
        for i in range(longitud_pila(pila) - 1, -1, -1):
            # Mostramos cada elemento
            print(f"  | {pila[i]} |")


# Creamos la pila
pila = inicializar_pila()
# Opción elegida
opcion = ""
# Repetimos hasta salir
while opcion != "5":
    # Menú
    print("\n1. Añadir elemento a la pila")
    # Opción 2
    print("2. Sacar elemento de la pila")
    # Opción 3
    print("3. Longitud de la pila")
    # Opción 4
    print("4. Mostrar pila")
    # Opción 5
    print("5. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")
    # Añadir
    if opcion == "1":
        # Pedimos el elemento y lo añadimos
        add_pila(input("Elemento a añadir: "), pila)
    # Sacar
    elif opcion == "2":
        # Sacamos el elemento
        elemento = sacar_de_la_pila(pila)
        # Si se ha sacado algo
        if elemento is not None:
            # Lo mostramos
            print("Elemento sacado:", elemento)
    # Longitud
    elif opcion == "3":
        # Mostramos la longitud
        print("Longitud de la pila:", longitud_pila(pila))
    # Mostrar
    elif opcion == "4":
        # Mostramos la pila
        escribir_pila(pila)
    # Salir
    elif opcion == "5":
        # Despedida
        print("¡Adiós!")
    # Opción no válida
    else:
        # Avisamos
        print("Opción no válida")
