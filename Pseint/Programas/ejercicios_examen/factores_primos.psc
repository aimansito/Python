// ============================================================
// FUNCIÓN PedirNumero
// No recibe nada. Pide un número al usuario y lo devuelve,
// asegurándose de que sea mayor que 1 (el 0 y el 1 no tienen
// factores primos).
// ============================================================
Funcion n <- PedirNumero(mensaje)
	// "n" es la variable que devolverá la función
	Definir n Como Entero
	
	// Se repite la pregunta hasta que el número sea válido
	Repetir
		Escribir "Introduce un número mayor que 1: "
		Leer n
	Hasta Que n > 1
	
	// Al llegar a FinFuncion, se devuelve el valor de "n"
FinFuncion


// ============================================================
// SUBPROCESO MostrarFactores
// Recibe un número y escribe en pantalla su descomposición
// en factores primos. Es un subproceso (no una función)
// porque no devuelve nada: solo escribe.
// ============================================================
SubProceso MostrarFactores(numero)
	// n: copia del número que iremos dividiendo hasta llegar a 1
	// divisor: número con el que probamos a dividir
	Definir n, divisor Como Entero
	// primero: indica si todavía no hemos escrito ningún factor
	Definir primero Como Logico
	
	// Trabajamos sobre una copia para no perder el número original
	n <- numero
	// Empezamos probando con 2, que es el primer número primo
	divisor <- 2
	// Al principio aún no se ha escrito ningún factor
	primero <- Verdadero
	
	// Escribimos el inicio, por ejemplo "60 = "
	// "Sin Saltar" hace que lo siguiente siga en la misma línea
	Escribir Sin Saltar numero, " = "
	
	// Repetimos mientras quede algo por dividir
	// (cuando n llega a 1, ya hemos sacado todos los factores)
	Mientras n > 1 Hacer
		
		// Comprobamos si la división es exacta (resto 0)
		Si n MOD divisor = 0 Entonces
			
			// El divisor es un factor primo: hay que escribirlo
			Si primero Entonces
				// Si es el primer factor, se escribe solo, sin "x"
				Escribir Sin Saltar divisor
				// A partir de ahora ya no será el primero
				primero <- Falso
			SiNo
				// Si ya había factores antes, se escribe " x " delante
				Escribir Sin Saltar " x ", divisor
			FinSi
			
			// Dividimos n entre el factor encontrado.
			// No aumentamos el divisor, porque puede volver a
			// dividir (por ejemplo, el 2 aparece dos veces en 60)
			n <- n / divisor
			
		SiNo
			// La división no es exacta: este divisor ya no sirve,
			// así que probamos con el siguiente número.
			// Los que no son primos (4, 6, 8...) nunca dividirán,
			// porque sus factores ya se quitaron antes
			divisor <- divisor + 1
		FinSi
		
	FinMientras
	
	// Salto de línea final para terminar la salida
	Escribir ""
FinSubProceso


// ============================================================
// PROGRAMA PRINCIPAL
// Pide un número y muestra su descomposición en factores primos
// usando las funciones anteriores.
// ============================================================
Algoritmo factores_primos
	Definir numero Como Entero
	
	// Llamamos a la función y guardamos lo que devuelve.
	// Lleva flecha porque la función devuelve un valor
	numero <- PedirNumero("Introduce un número mayor que 1")
	
	// Llamamos al subproceso para que escriba los factores.
	// Va sin flecha porque el subproceso no devuelve nada
	MostrarFactores(numero)

FinAlgoritmo