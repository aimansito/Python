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
  tamanio = len(tablero)

  print()
  print("     1   2   3")

  for fila in range(tamanio):
    # Empezamos la línea con el número de fila (fila + 1 para el usuario)
    linea = f"  {fila + 1} "

    for columna in range(tamanio):
      linea += f" {simbolo_ficha(tablero[fila][columna])} "

    if columna < TAMANIO - 1:
      linea = " | "