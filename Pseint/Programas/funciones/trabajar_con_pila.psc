// ============================================================
// SUBPROCESO InicializarPila
// Rellena las 10 posiciones con "*", que significa
// "posición vacía". Los arreglos se pasan siempre por
// referencia, así que los cambios afectan a la pila original
// ============================================================
SubProceso InicializarPila(pila)
	Definir i Como Entero
	Para i <- 0 Hasta 9 Hacer
		pila[i] <- "*"
	FinPara
FinSubProceso


// ============================================================
// FUNCIÓN LongitudPila
// Recibe la pila y devuelve cuántos elementos tiene, es decir,
// cuántas posiciones no tienen "*"
// ============================================================
Funcion n <- LongitudPila(pila)
	Definir n, i Como Entero
	n <- 0
	Para i <- 0 Hasta 9 Hacer
		Si pila[i] <> "*" Entonces
			n <- n + 1
		FinSi
	FinPara
FinFuncion


// ============================================================
// FUNCIÓN EstaVaciaPila
// Devuelve Verdadero si la pila no tiene ningún elemento
// ============================================================
Funcion vacia <- EstaVaciaPila(pila)
	Definir vacia Como Logico
	vacia <- (LongitudPila(pila) = 0)
FinFuncion


// ============================================================
// FUNCIÓN EstaLlenaPila
// Devuelve Verdadero si la pila tiene sus 10 elementos
// ============================================================
Funcion llena <- EstaLlenaPila(pila)
	Definir llena Como Logico
	llena <- (LongitudPila(pila) = 10)
FinFuncion


// ============================================================
// SUBPROCESO AddPila
// Añade un elemento en la cima de la pila (la primera
// posición libre). Si está llena, muestra un error
// ============================================================
SubProceso AddPila(pila, elemento)
	Si EstaLlenaPila(pila) Entonces
		Escribir "Error: la pila está llena, no se puede añadir"
	SiNo
		// Si hay 3 elementos (posiciones 0, 1 y 2),
		// la primera libre es la 3, que coincide con la longitud
		pila[LongitudPila(pila)] <- elemento
		Escribir "Se ha añadido '", elemento, "' a la pila"
	FinSi
FinSubProceso


// ============================================================
// FUNCIÓN SacarDeLaPila
// Devuelve el último elemento añadido (la cima) y lo borra
// de la pila. Si está vacía, muestra un error y devuelve ""
// ============================================================
Funcion elemento <- SacarDeLaPila(pila)
	Definir elemento Como Cadena
	Definir cima Como Entero
	
	Si EstaVaciaPila(pila) Entonces
		Escribir "Error: la pila está vacía, no se puede sacar nada"
		elemento <- ""
	SiNo
		// El último elemento está en la posición longitud - 1
		cima <- LongitudPila(pila) - 1
		// Guardamos el elemento para devolverlo...
		elemento <- pila[cima]
		// ...y lo borramos poniendo "*" en su lugar
		pila[cima] <- "*"
	FinSi
FinFuncion


// ============================================================
// SUBPROCESO EscribirPila
// Muestra los elementos de la pila, desde la cima (el último
// añadido) hasta la base (el primero)
// ============================================================
SubProceso EscribirPila(pila)
	Definir i Como Entero
	
	Si EstaVaciaPila(pila) Entonces
		Escribir "La pila está vacía"
	SiNo
		Escribir "Contenido de la pila (de la cima a la base):"
		// Recorremos hacia atrás con "Con Paso -1"
		Para i <- LongitudPila(pila) - 1 Hasta 0 Con Paso -1 Hacer
			Escribir "  | ", pila[i], " |"
		FinPara
		Escribir "  +------+"
	FinSi
FinSubProceso


// ============================================================
// PROGRAMA PRINCIPAL
// Menú para trabajar con la pila hasta elegir salir
// ============================================================
Algoritmo trabajar_con_pila
	Definir pila Como Cadena
	Dimension pila[10]          // posiciones de la 0 a la 9
	Definir opcion Como Entero
	Definir elemento Como Cadena
	
	// Antes de usar la pila hay que inicializarla
	InicializarPila(pila)
	
	Repetir
		Escribir ""
		Escribir "========= PILA ========="
		Escribir "1. Añadir elemento a la pila"
		Escribir "2. Sacar elemento de la pila"
		Escribir "3. Longitud de la pila"
		Escribir "4. Mostrar pila"
		Escribir "5. Salir"
		Escribir "Elige una opción: "
		Leer opcion
		
		Segun opcion Hacer
			1:
				// El elemento no puede estar vacío ni ser "*",
				// porque "*" significa posición libre
				Repetir
					Escribir "Elemento a añadir: "
					Leer elemento
				Hasta Que elemento <> "" Y elemento <> "*"
				AddPila(pila, elemento)
			2:
				elemento <- SacarDeLaPila(pila)
				// Si devolvió "", la pila estaba vacía y ya
				// se mostró el error dentro de la función
				Si elemento <> "" Entonces
					Escribir "Se ha sacado '", elemento, "' de la pila"
				FinSi
			3:
				Escribir "La pila tiene ", LongitudPila(pila), " elementos"
			4:
				EscribirPila(pila)
			5:
				Escribir "¡Hasta luego!"
			De Otro Modo:
				Escribir "Opción no válida, elige del 1 al 5"
		FinSegun
		
	Hasta Que opcion = 5
FinAlgoritmo