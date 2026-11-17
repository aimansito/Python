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