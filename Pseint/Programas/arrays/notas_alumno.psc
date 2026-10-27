// ============================================================
// Lee las 5 notas de un alumno (entre 0 y 10) y muestra
// todas las notas, la media, la nota más alta y la más baja
// ============================================================
Algoritmo notas_alumno
	Definir notas Como Real
	Dimension notas[5]          // posiciones 0, 1, 2, 3 y 4
	Definir i Como Entero
	Definir suma, media, maxima, minima Como Real
	
	// --- 1. Leer las 5 notas ---
	Para i <- 0 Hasta 4 Hacer
		// Repetimos hasta que la nota esté entre 0 y 10
		Repetir
			// i + 1 para que el usuario vea "Nota 1" y no "Nota 0"
			Escribir "Introduce la nota ", i + 1, " (0-10): "
			Leer notas[i]
			Si notas[i] < 0 O notas[i] > 10 Entonces
				Escribir "Nota no válida, debe estar entre 0 y 10"
			FinSi
		Hasta Que notas[i] >= 0 Y notas[i] <= 10
	FinPara
	
	// --- 2. Calcular suma, máxima y mínima ---
	suma <- 0
	// Partimos de la primera nota como máxima y mínima provisionales
	maxima <- notas[0]
	minima <- notas[0]
	
	Para i <- 0 Hasta 4 Hacer
		// Vamos acumulando todas las notas para la media
		suma <- suma + notas[i]
		// Si encontramos una nota mayor, pasa a ser la máxima
		Si notas[i] > maxima Entonces
			maxima <- notas[i]
		FinSi
		// Si encontramos una nota menor, pasa a ser la mínima
		Si notas[i] < minima Entonces
			minima <- notas[i]
		FinSi
	FinPara
	
	// La media es la suma entre el número de notas
	media <- suma / 5
	
	// --- 3. Mostrar resultados ---
	Escribir ""
	Escribir "Notas del alumno:"
	Para i <- 0 Hasta 4 Hacer
		Escribir "  Nota ", i + 1, ": ", notas[i]
	FinPara
	Escribir "Nota media: ", media
	Escribir "Nota más alta: ", maxima
	Escribir "Nota más baja: ", minima
FinAlgoritmo