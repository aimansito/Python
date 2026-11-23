# Constantes del juego

VACIO = 0
FICHA_0 = 1
FICHA_X = 2
TAMANIO = 3

def crear_tablero():
   # lista vacía para las filas
    tablero = []

    for fila in range(TAMANIO):
      #creo una fila nueva vacía
      nueva_fila = []

      for columna in range(TAMANIO):
        # añado una casilla vacía a la fila
        nueva_fila.append(VACIO)

        #añado la fila que ya tiene sus tres casillas 
      tablero.append(nueva_fila)
        
    return tablero

def simbolo_ficha(ficha):
  if ficha == FICHA_0:
    return "0" 
  elif ficha == FICHA_X:
    return "X"

  return " "


def mostrar_tablero(tablero):
  # Guardo cuantas filas tiene el tablero
  tamanio = len(tablero)

  #Dejamos una línea en blanco antes del tablero
  print()

  #Cabecera con los números de columna
  print("  1  2  3")

  #Recorro cada fila del tablero 
  for fila in range(tamanio):
    linea = f" {fila+1}"

    for columna in range(tamanio):
      if columna < tamanio -1:
        linea += "|"

    #Mostramos la fila completa
    print(linea)

    if fila < tamanio - 1:
      print(" ---+---+---")

  print() 


def colocar_ficha(tablero, ficha, x, y):
  # Si la ficha no es válida, o la fila o la columna se salen del tablero,
  # o la casilla está ocupada, no se puede colocar
  if (ficha != FICHA_0 and ficha != FICHA_X) or \
     x < 0 or x >= TAMANIO or \
     y < 0 or y >= TAMANIO or \
     tablero[x][y] != VACIO:
    # Algo no es válido: no colocamos nada
    return False

  # Todo correcto: colocamos la ficha
  tablero[x][y] = ficha
  # Avisamos de que se ha colocado bien
  return True

def tres_iguales(casilla1, casilla2, casilla3):
  #La primera no puede estar vacia y las tres tienen que ser iguales
  return casilla1 != VACIO and casilla1 == casilla2 and casilla2 == casilla3

#Devuelve True si en el tablero hay 3 fichas en linea
def hay_ganador(tablero):
  # Revisamos cada fila y columna en el mismo bucle 
  for i in range(TAMANIO):
    if tres_iguales(tablero[i][0], tablero[i][1], tablero[i][2]) or \
       tres_iguales(tablero[0][i], tablero[1][i], tablero[2][i]):
      return True

  # Si no, hay ganador solo si alguna de las dos diagonales tiene tres iguales
  return tres_iguales(tablero[0][0],tablero[1][1],tablero[2][2]) or tres_iguales(tablero[0][2],tablero[1][1],tablero[2][0])


def juego_terminado(tablero):
  for fila in tablero:
    for fila in tablero:
      #Si en esta fila queda alguna casilla vacía, el tablero no está lleno
      if VACIO in fila:
        return False
    return True 

def es_numero(texto):
  # un texto vacío no es un número 
  if len(texto) == 0:
    return False

  #Recorremos el texto caracter a caracter 
  for caracter in texto: 
    #Si no está entre '0' y '9' no es un dígito
    if caracter < "0" or caracter > "9":
      return False
    #Todos los caracteres eran digitos
    return True

def pedir_numero(mensaje, minimo, maximo):
  #Mostramos el mensaje y leemos lo que escribe el usuario, quitando espacios de los lados
  texto = input(mensaje).strip()

  #Repetimos mientras no sea un número o esté fuera del rango
  while not es_numero(texto) or int(texto) < minimo or int(texto) > maximo: 
    print(f"Valor no válido. Debe ser un número entre {minimo} y {maximo}. ")
    texto = input(mensaje).strip()
    
  return int(texto)

#Devuelve true si el texto no está vacío y todos sus caracteres son dígitos
def es_numero(texto):
  #Un texto vacío no es número
  if len(texto) == 0:
    return False

  #Recorremos el texto caracter a caracter
  for caracter in texto:
    if caracter < "0" or caracter > "9":
    #No es número 
     return False
  return True