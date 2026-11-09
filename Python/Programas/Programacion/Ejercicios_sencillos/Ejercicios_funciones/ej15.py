# Ejercicio 15: cola (el primero en entrar es el primero en salir) con un vector de 10

# Tamaño máximo de la cola
TAMANO = 10
# Carácter que indica "posición vacía"
VACIO = "*"


# Crea y devuelve una cola con todas las posiciones vacías
def inicializar_cola():
    # Lista de 10 elementos con el carácter de vacío
    return [VACIO] * TAMANO


# Devuelve cuántos elementos tiene la cola
def longitud_cola(cola):
    # Contador de elementos
    contador = 0
    # Recorremos las posiciones
    for elemento in cola:
        # Si la posición no está vacía
        if elemento != VACIO:
            # Contamos un elemento
            contador = contador + 1
    # Devolvemos el total
    return contador


# Devuelve True si la cola no tiene elementos
def esta_vacia_cola(cola):
    # Está vacía si su longitud es 0
    return longitud_cola(cola) == 0


# Devuelve True si la cola está llena
def esta_llena_cola(cola):
    # Está llena si su longitud es igual al tamaño
    return longitud_cola(cola) == TAMANO


# Añade una cadena al final de la cola si no está llena
def add_cola(cadena, cola):
    # Si está llena
    if esta_llena_cola(cola):
        # Mostramos un error
        print("Error: la cola está llena")
    # Si hay hueco
    else:
        # La siguiente posición libre es justo la longitud actual
        cola[longitud_cola(cola)] = cadena


# ÚNICA FUNCIÓN DISTINTA A LA PILA: saca el PRIMER elemento añadido
def sacar_de_la_cola(cola):
    # Si está vacía
    if esta_vacia_cola(cola):
        # Mostramos un error
        print("Error: la cola está vacía")
        # Devolvemos None porque no hay nada que sacar
        return None
    # Guardamos el primer elemento (posición 0)
    elemento = cola[0]
    # Desplazamos todos los elementos una posición hacia la izquierda
    for i in range(TAMANO - 1):
        # Cada posición toma el valor de la siguiente
        cola[i] = cola[i + 1]
    # La última posición queda vacía
    cola[TAMANO - 1] = VACIO
    # Devolvemos el elemento sacado
    return elemento


# Muestra en pantalla los elementos de la cola (del primero al último)
def escribir_cola(cola):
    # Si está vacía
    if esta_vacia_cola(cola):
        # Lo indicamos
        print("La cola está vacía")
    # Si tiene elementos
    else:
        # Construimos la lista solo con los elementos ocupados
        elementos = cola[:longitud_cola(cola)]
        # Los mostramos separados por flechas (salida <- ... <- entrada)
        print("  Salida <- " + " <- ".join(elementos) + " <- Entrada")


# Creamos la cola
cola = inicializar_cola()
# Opción elegida
opcion = ""
# Repetimos hasta salir
while opcion != "5":
    # Menú
    print("\n1. Añadir elemento a la cola")
    # Opción 2
    print("2. Sacar elemento de la cola")
    # Opción 3
    print("3. Longitud de la cola")
    # Opción 4
    print("4. Mostrar cola")
    # Opción 5
    print("5. Salir")
    # Pedimos la opción
    opcion = input("Elige una opción: ")
    # Añadir
    if opcion == "1":
        # Pedimos el elemento y lo añadimos
        add_cola(input("Elemento a añadir: "), cola)
    # Sacar
    elif opcion == "2":
        # Sacamos el elemento
        elemento = sacar_de_la_cola(cola)
        # Si se ha sacado algo
        if elemento is not None:
            # Lo mostramos
            print("Elemento sacado:", elemento)
    # Longitud
    elif opcion == "3":
        # Mostramos la longitud
        print("Longitud de la cola:", longitud_cola(cola))
    # Mostrar
    elif opcion == "4":
        # Mostramos la cola
        escribir_cola(cola)
    # Salir
    elif opcion == "5":
        # Despedida
        print("¡Adiós!")
    # Opción no válida
    else:
        # Avisamos
        print("Opción no válida")
