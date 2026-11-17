// Proyecto de ejemplo: JUEGO DEL 3 EN RAYA (versión en Java)
//
// Sigue el guion de proyecto.pdf:
//   - El tablero es una matriz de enteros 3x3 inicializada a 0 (casilla vacía).
//   - Las fichas de los jugadores (0) y (X) son valores enteros guardados en constantes.
//   - Se piden los nombres y, por turnos, la posición donde colocar la ficha.
//   - Se avisa si la casilla no existe o está ocupada.
//   - La partida acaba cuando hay 3 en línea o el tablero está lleno.
//   - Al terminar se pregunta si se quiere jugar otra partida.
//
// Funciones del guion (en Java se escriben en camelCase, en Python en snake_case):
//   mostrarTablero(tablero)              -> mostrar_tablero(tablero)
//   colocarFicha(tablero, ficha, x, y)   -> colocar_ficha(tablero, ficha, x, y)
//   hayGanador(tablero)                  -> hay_ganador(tablero)
//   juegoTerminado(tablero)              -> juego_terminado(tablero)
//
// Solo se usa lo visto en los temas: variables, constantes, entrada/salida,
// operadores, if/else, while, for, funciones y matrices (lista de listas).
//
// Compilar y ejecutar (desde esta carpeta):
//   javac -encoding UTF-8 TresEnRaya.java
//   java TresEnRaya

import java.util.Scanner;

public class TresEnRaya {

    // ---------------------------------------------------------------
    // CONSTANTES
    // En Java se declaran con "static final" y en MAYÚSCULAS.
    // En Python bastaría con escribirlas en mayúsculas: VACIO = 0
    // ---------------------------------------------------------------

    // Valor de una casilla vacía
    static final int VACIO = 0;
    // Valor que representa la ficha del jugador 1, el "0"
    static final int FICHA_O = 1;
    // Valor que representa la ficha del jugador 2, la "X"
    static final int FICHA_X = 2;
    // Número de filas y columnas del tablero
    static final int TAMANIO = 3;

    // Objeto para leer del teclado (en Python esto lo hace input())
    static Scanner teclado = new Scanner(System.in);


    // ---------------------------------------------------------------
    // FUNCIONES DEL TABLERO
    // ---------------------------------------------------------------

    // Crea el tablero 3x3 con todas las casillas a VACIO y lo devuelve
    static int[][] crearTablero() {
        // Creamos la matriz de 3 filas y 3 columnas
        int[][] tablero = new int[TAMANIO][TAMANIO];
        // Recorremos cada fila
        for (int fila = 0; fila < TAMANIO; fila++) {
            // Recorremos cada columna de esa fila
            for (int columna = 0; columna < TAMANIO; columna++) {
                // Dejamos la casilla vacía
                tablero[fila][columna] = VACIO;
            }
        }
        // Devolvemos el tablero ya inicializado
        return tablero;
    }


    // Devuelve el texto que se ve en pantalla para el valor de una casilla
    static String simboloFicha(int ficha) {
        // Si es la ficha del jugador 1
        if (ficha == FICHA_O) {
            // Se dibuja un 0
            return "0";
        // Si es la ficha del jugador 2
        } else if (ficha == FICHA_X) {
            // Se dibuja una X
            return "X";
        }
        // Cualquier otro valor (VACIO) se dibuja como un espacio
        return " ";
    }


    // Muestra el tablero en pantalla con 0 y X en lugar de números
    static void mostrarTablero(int[][] tablero) {
        // Cabecera con los números de columna (empezamos en 1 para el usuario)
        System.out.println();
        // Dejamos hueco para la columna de números de fila
        System.out.println("     1   2   3");
        // Recorremos las filas
        for (int fila = 0; fila < TAMANIO; fila++) {
            // Empezamos la línea con el número de fila (fila + 1 para el usuario)
            String linea = "  " + (fila + 1) + " ";
            // Recorremos las columnas de la fila
            for (int columna = 0; columna < TAMANIO; columna++) {
                // Añadimos el símbolo de la casilla rodeado de espacios
                linea = linea + " " + simboloFicha(tablero[fila][columna]) + " ";
                // Entre columnas ponemos una barra (menos después de la última)
                if (columna < TAMANIO - 1) {
                    // Separador vertical
                    linea = linea + "|";
                }
            }
            // Escribimos la fila completa
            System.out.println(linea);
            // Entre filas ponemos una línea horizontal (menos después de la última)
            if (fila < TAMANIO - 1) {
                // Separador horizontal
                System.out.println("    ---+---+---");
            }
        }
        // Línea en blanco al final para que se lea mejor
        System.out.println();
    }


    // Coloca la ficha en la posición (x, y) del tablero.
    // x es la fila e y la columna, las dos de 0 a 2.
    // Devuelve true si se ha podido colocar y false si no.
    static boolean colocarFicha(int[][] tablero, int ficha, int x, int y) {
        // Validamos la ficha: solo puede ser la del jugador 1 o la del jugador 2
        if (ficha != FICHA_O && ficha != FICHA_X) {
            // Ficha no válida, no colocamos nada
            return false;
        }
        // Validamos que la fila existe en el tablero
        if (x < 0 || x >= TAMANIO) {
            // Fila fuera del tablero
            return false;
        }
        // Validamos que la columna existe en el tablero
        if (y < 0 || y >= TAMANIO) {
            // Columna fuera del tablero
            return false;
        }
        // Validamos que la casilla está libre
        if (tablero[x][y] != VACIO) {
            // Casilla ocupada
            return false;
        }
        // Todo correcto: colocamos la ficha
        tablero[x][y] = ficha;
        // Avisamos de que se ha colocado bien
        return true;
    }


    // Devuelve true si las tres casillas tienen la misma ficha y no están vacías
    static boolean tresIguales(int casilla1, int casilla2, int casilla3) {
        // La primera no puede estar vacía y las tres tienen que ser iguales
        return casilla1 != VACIO && casilla1 == casilla2 && casilla2 == casilla3;
    }


    // Devuelve true si en el tablero hay tres fichas en línea
    static boolean hayGanador(int[][] tablero) {
        // Revisamos cada fila y cada columna en el mismo bucle
        for (int i = 0; i < TAMANIO; i++) {
            // Fila i: casillas (i,0) (i,1) (i,2)
            if (tresIguales(tablero[i][0], tablero[i][1], tablero[i][2])) {
                // Hay tres en raya en una fila
                return true;
            }
            // Columna i: casillas (0,i) (1,i) (2,i)
            if (tresIguales(tablero[0][i], tablero[1][i], tablero[2][i])) {
                // Hay tres en raya en una columna
                return true;
            }
        }
        // Diagonal principal: (0,0) (1,1) (2,2)
        if (tresIguales(tablero[0][0], tablero[1][1], tablero[2][2])) {
            // Hay tres en raya en la diagonal principal
            return true;
        }
        // Diagonal secundaria: (0,2) (1,1) (2,0)
        if (tresIguales(tablero[0][2], tablero[1][1], tablero[2][0])) {
            // Hay tres en raya en la diagonal secundaria
            return true;
        }
        // No hay ninguna línea completa
        return false;
    }


    // Devuelve true si el tablero está completo y false si quedan casillas vacías
    static boolean juegoTerminado(int[][] tablero) {
        // Recorremos todas las filas
        for (int fila = 0; fila < TAMANIO; fila++) {
            // Recorremos todas las columnas
            for (int columna = 0; columna < TAMANIO; columna++) {
                // En cuanto encontramos una casilla vacía, el tablero no está lleno
                if (tablero[fila][columna] == VACIO) {
                    // Aún se puede jugar
                    return false;
                }
            }
        }
        // No quedan casillas vacías
        return true;
    }


    // ---------------------------------------------------------------
    // FUNCIONES PARA PEDIR Y VALIDAR DATOS POR TECLADO
    // ---------------------------------------------------------------

    // Devuelve true si el texto no está vacío y todos sus caracteres son dígitos
    // (equivale a texto.isdigit() en Python, pero hecho a mano)
    static boolean esNumero(String texto) {
        // Un texto vacío no es un número
        if (texto.length() == 0) {
            // No es número
            return false;
        }
        // Recorremos el texto carácter a carácter
        for (int i = 0; i < texto.length(); i++) {
            // Cogemos el carácter de la posición i
            char caracter = texto.charAt(i);
            // Si no está entre '0' y '9' no es un dígito
            if (caracter < '0' || caracter > '9') {
                // No es número
                return false;
            }
        }
        // Todos los caracteres eran dígitos
        return true;
    }


    // Pide un número entero entre minimo y maximo (ambos incluidos)
    // y lo vuelve a pedir hasta que sea correcto
    static int pedirNumero(String mensaje, int minimo, int maximo) {
        // Mostramos el mensaje y leemos la línea (en Python: input(mensaje))
        System.out.print(mensaje);
        // Leemos lo que escribe el usuario quitando espacios de los lados
        String texto = teclado.nextLine().trim();
        // Repetimos mientras no sea un número, sea demasiado largo para un int
        // (más de 9 cifras haría fallar a parseInt) o esté fuera del rango
        while (!esNumero(texto) || texto.length() > 9
                || Integer.parseInt(texto) < minimo || Integer.parseInt(texto) > maximo) {
            // Avisamos del error
            System.out.println("Valor no válido. Debe ser un número entre " + minimo + " y " + maximo + ".");
            // Volvemos a pedirlo
            System.out.print(mensaje);
            // Leemos de nuevo
            texto = teclado.nextLine().trim();
        }
        // Convertimos el texto a entero (en Python: int(texto)) y lo devolvemos
        return Integer.parseInt(texto);
    }


    // Pide un nombre que no esté vacío
    static String pedirNombre(String mensaje) {
        // Mostramos el mensaje
        System.out.print(mensaje);
        // Leemos el nombre quitando espacios de los lados
        String nombre = teclado.nextLine().trim();
        // Repetimos mientras esté vacío
        while (nombre.length() == 0) {
            // Avisamos del error
            System.out.println("El nombre no puede estar vacío.");
            // Volvemos a pedirlo
            System.out.print(mensaje);
            // Leemos de nuevo
            nombre = teclado.nextLine().trim();
        }
        // Devolvemos el nombre correcto
        return nombre;
    }


    // Pregunta si se quiere jugar otra partida.
    // Devuelve true si la respuesta es "s" y false si es "n".
    static boolean preguntarOtraPartida() {
        // Mostramos la pregunta
        System.out.print("¿Quieres jugar otra partida? (s/n): ");
        // Leemos la respuesta en minúsculas para aceptar "S" y "s"
        String respuesta = teclado.nextLine().trim().toLowerCase();
        // Repetimos mientras no sea ni "s" ni "n"
        while (!respuesta.equals("s") && !respuesta.equals("n")) {
            // Avisamos del error
            System.out.println("Responde 's' para sí o 'n' para no.");
            // Volvemos a preguntar
            System.out.print("¿Quieres jugar otra partida? (s/n): ");
            // Leemos de nuevo
            respuesta = teclado.nextLine().trim().toLowerCase();
        }
        // Devolvemos true solo si ha respondido "s"
        return respuesta.equals("s");
    }


    // ---------------------------------------------------------------
    // PARTIDA
    // ---------------------------------------------------------------

    // Juega una partida completa entre los dos jugadores
    static void jugarPartida(String nombreJugador1, String nombreJugador2) {
        // Creamos un tablero nuevo, todo vacío
        int[][] tablero = crearTablero();
        // Empieza el jugador 1 con la ficha 0
        int fichaActual = FICHA_O;
        // Nombre del jugador que tiene el turno
        String nombreActual = nombreJugador1;
        // Indica si la partida ya ha acabado
        boolean partidaAcabada = false;

        // Repetimos turnos hasta que la partida acabe
        while (!partidaAcabada) {
            // Enseñamos cómo está el tablero
            mostrarTablero(tablero);
            // Indicamos de quién es el turno y con qué ficha juega
            System.out.println("Turno de " + nombreActual + " (" + simboloFicha(fichaActual) + ")");

            // Indica si la ficha se ha podido colocar
            boolean colocada = false;
            // Pedimos posición hasta que se pueda colocar la ficha
            while (!colocada) {
                // Pedimos la fila (1 a 3 para el usuario)
                int fila = pedirNumero("Fila (1-3): ", 1, TAMANIO);
                // Pedimos la columna (1 a 3 para el usuario)
                int columna = pedirNumero("Columna (1-3): ", 1, TAMANIO);
                // Restamos 1 porque en la matriz las posiciones empiezan en 0
                colocada = colocarFicha(tablero, fichaActual, fila - 1, columna - 1);
                // Si no se ha podido colocar es que la casilla está ocupada
                if (!colocada) {
                    // Avisamos para que elija otra
                    System.out.println("Esa casilla ya está ocupada. Elige otra.");
                }
            }

            // Comprobamos si este movimiento ha hecho tres en raya
            if (hayGanador(tablero)) {
                // Enseñamos el tablero final
                mostrarTablero(tablero);
                // Anunciamos el ganador
                System.out.println("¡" + nombreActual + " ha ganado la partida!");
                // Se acaba la partida
                partidaAcabada = true;
            // Si nadie ha ganado, comprobamos si el tablero está lleno
            } else if (juegoTerminado(tablero)) {
                // Enseñamos el tablero final
                mostrarTablero(tablero);
                // Anunciamos el empate
                System.out.println("¡Tablas! El tablero está completo y nadie ha ganado.");
                // Se acaba la partida
                partidaAcabada = true;
            // Si la partida sigue, cambiamos de turno
            } else {
                // Si jugaba el 0, ahora le toca a la X
                if (fichaActual == FICHA_O) {
                    // Turno del jugador 2
                    fichaActual = FICHA_X;
                    // Con su nombre
                    nombreActual = nombreJugador2;
                // Si jugaba la X, ahora le toca al 0
                } else {
                    // Turno del jugador 1
                    fichaActual = FICHA_O;
                    // Con su nombre
                    nombreActual = nombreJugador1;
                }
            }
        }
    }


    // ---------------------------------------------------------------
    // PROGRAMA PRINCIPAL (en Python sería el código de main.py)
    // ---------------------------------------------------------------

    public static void main(String[] args) {
        // Título del juego
        System.out.println("===== TRES EN RAYA =====");
        // Pedimos el nombre del jugador 1 (juega con 0)
        String nombreJugador1 = pedirNombre("Nombre del jugador 1 (juega con 0): ");
        // Pedimos el nombre del jugador 2 (juega con X)
        String nombreJugador2 = pedirNombre("Nombre del jugador 2 (juega con X): ");

        // Indica si se quiere seguir jugando
        boolean seguirJugando = true;
        // Repetimos partidas mientras quieran seguir
        while (seguirJugando) {
            // Jugamos una partida completa
            jugarPartida(nombreJugador1, nombreJugador2);
            // Preguntamos si quieren jugar otra
            seguirJugando = preguntarOtraPartida();
        }
        // Despedida
        System.out.println("¡Gracias por jugar!");
    }
}
