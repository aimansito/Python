// ============================================================
// FUNCIÓN Calcular_mcd
// Recibe dos números y devuelve su máximo común divisor
// (método de Euclides). Trabaja con los valores absolutos
// para que funcione también con fracciones negativas
// ============================================================
Funcion mcd <- Calcular_mcd(a, b)
	Definir mcd, x, y, resto Como Entero
	
	// Abs quita el signo: Abs(-6) = 6
	x <- Abs(a)
	y <- Abs(b)
	
	// Euclides: dividimos y desplazamos los papeles
	// hasta que el resto sea 0
	Mientras y <> 0 Hacer
		resto <- x MOD y
		x <- y
		y <- resto
	FinMientras
	
	// El último divisor (que ha quedado en x) es el MCD
	mcd <- x
FinFuncion


// ============================================================
// SUBPROCESO Simplificar_fraccion
// Divide numerador y denominador entre su MCD.
// Modifica la fracción recibida, por eso usa Por Referencia
// Ej: 6/8 -> 3/4
// ============================================================
SubProceso Simplificar_fraccion(num Por Referencia, den Por Referencia)
	Definir divisor Como Entero
	
	divisor <- Calcular_mcd(num, den)
	num <- Trunc(num / divisor)
	den <- Trunc(den / divisor)
	
	// Si el signo negativo ha quedado abajo, lo pasamos arriba
	// para que 3/-4 se muestre como -3/4
	Si den < 0 Entonces
		num <- -num
		den <- -den
	FinSi
FinSubProceso


// ============================================================
// SUBPROCESO Leer_fraccion
// Lee por teclado una fracción y la simplifica.
// Devuelve numerador y denominador, por eso Por Referencia
// ============================================================
SubProceso Leer_fraccion(num Por Referencia, den Por Referencia)
	Escribir "  Numerador: "
	Leer num
	// El denominador no puede ser 0
	Repetir
		Escribir "  Denominador (distinto de 0): "
		Leer den
	Hasta Que den <> 0
	
	Simplificar_fraccion(num, den)
FinSubProceso


// ============================================================
// SUBPROCESO Escribir_fraccion
// Escribe la fracción en pantalla. Si el denominador es 1,
// solo escribe el numerador. Usa "Sin Saltar" para que se
// pueda escribir algo más en la misma línea
// ============================================================
SubProceso Escribir_fraccion(num, den)
	Si den = 1 Entonces
		Escribir Sin Saltar num
	SiNo
		Escribir Sin Saltar num, "/", den
	FinSi
FinSubProceso


// ============================================================
// OPERACIONES
// Las cuatro reciben dos fracciones (n1/d1 y n2/d2), calculan
// el resultado según su fórmula, lo simplifican y lo dejan
// en nr/dr (Por Referencia)
// ============================================================
SubProceso Sumar_fracciones(n1, d1, n2, d2, nr Por Referencia, dr Por Referencia)
	nr <- n1 * d2 + d1 * n2
	dr <- d1 * d2
	Simplificar_fraccion(nr, dr)
FinSubProceso

SubProceso Restar_fracciones(n1, d1, n2, d2, nr Por Referencia, dr Por Referencia)
	nr <- n1 * d2 - d1 * n2
	dr <- d1 * d2
	Simplificar_fraccion(nr, dr)
FinSubProceso

SubProceso Multiplicar_fracciones(n1, d1, n2, d2, nr Por Referencia, dr Por Referencia)
	nr <- n1 * n2
	dr <- d1 * d2
	Simplificar_fraccion(nr, dr)
FinSubProceso

SubProceso Dividir_fracciones(n1, d1, n2, d2, nr Por Referencia, dr Por Referencia)
	nr <- n1 * d2
	dr <- d1 * n2
	Simplificar_fraccion(nr, dr)
FinSubProceso


// ============================================================
// SUBPROCESO Mostrar_operacion
// Escribe una línea como "1/2 + 1/3 = 5/6". Así no hay que
// repetir estas líneas en cada opción del menú
// ============================================================
SubProceso Mostrar_operacion(n1, d1, simbolo, n2, d2, nr, dr)
	Escribir_fraccion(n1, d1)
	Escribir Sin Saltar " ", simbolo, " "
	Escribir_fraccion(n2, d2)
	Escribir Sin Saltar " = "
	Escribir_fraccion(nr, dr)
	// Salto de línea final
	Escribir ""
FinSubProceso


// ============================================================
// PROGRAMA PRINCIPAL
// Menú que se repite hasta elegir la opción 5
// ============================================================
Algoritmo fracciones
	Definir opcion, n1, d1, n2, d2, nr, dr Como Entero
	
	Repetir
		// --- Mostrar el menú ---
		Escribir ""
		Escribir "===== CALCULADORA DE FRACCIONES ====="
		Escribir "1. Sumar dos fracciones"
		Escribir "2. Restar dos fracciones"
		Escribir "3. Multiplicar dos fracciones"
		Escribir "4. Dividir dos fracciones"
		Escribir "5. Salir"
		Escribir "Elige una opción: "
		Leer opcion
		
		// --- Las opciones 1 a 4 necesitan leer dos fracciones ---
		Si opcion >= 1 Y opcion <= 4 Entonces
			Escribir "Primera fracción:"
			Leer_fraccion(n1, d1)
			Escribir "Segunda fracción:"
			Leer_fraccion(n2, d2)
		FinSi
		
		// --- Ejecutar la operación elegida ---
		Segun opcion Hacer
			1:
				Sumar_fracciones(n1, d1, n2, d2, nr, dr)
				Mostrar_operacion(n1, d1, "+", n2, d2, nr, dr)
			2:
				Restar_fracciones(n1, d1, n2, d2, nr, dr)
				Mostrar_operacion(n1, d1, "-", n2, d2, nr, dr)
			3:
				Multiplicar_fracciones(n1, d1, n2, d2, nr, dr)
				Mostrar_operacion(n1, d1, "x", n2, d2, nr, dr)
			4:
				// No se puede dividir entre una fracción que vale 0
				Si n2 = 0 Entonces
					Escribir "No se puede dividir entre 0"
				SiNo
					Dividir_fracciones(n1, d1, n2, d2, nr, dr)
					Mostrar_operacion(n1, d1, ":", n2, d2, nr, dr)
				FinSi
			5:
				Escribir "¡Hasta luego!"
			De Otro Modo:
				Escribir "Opción no válida, elige del 1 al 5"
		FinSegun
		
	Hasta Que opcion = 5
	
FinAlgoritmo