// ============================================================
// FUNCIÓN TemperaturaMedia
// Recibe la temperatura máxima y mínima de un día y devuelve
// la media de las dos
// ============================================================
Funcion media <- TemperaturaMedia(maxima, minima)
	Definir media Como Real
	media <- (maxima + minima) / 2
FinFuncion


// ============================================================
// PROGRAMA PRINCIPAL
// Guarda la mínima y la máxima de 5 días y muestra:
//  - la media de cada día
//  - los días con la temperatura más baja
//  - los días cuya máxima coincide con una temperatura dada
// ============================================================
Algoritmo temperaturas_5_dias
	// Dos vectores en paralelo: la posición i de cada uno
	// corresponde al mismo día
	Definir tMin, tMax Como Real
	Dimension tMin[5]
	Dimension tMax[5]
	Definir i Como Entero
	Definir menor, buscar Como Real
	Definir encontrado Como Logico
	
	// --- 1. Leer las temperaturas de los 5 días ---
	Para i <- 0 Hasta 4 Hacer
		Escribir "--- Día ", i + 1, " ---"
		Escribir "Temperatura máxima: "
		Leer tMax[i]
		// La mínima no puede ser mayor que la máxima
		Repetir
			Escribir "Temperatura mínima: "
			Leer tMin[i]
			Si tMin[i] > tMax[i] Entonces
				Escribir "La mínima no puede ser mayor que la máxima"
			FinSi
		Hasta Que tMin[i] <= tMax[i]
	FinPara
	
	// --- 2. Temperatura media de cada día ---
	Escribir ""
	Escribir "TEMPERATURA MEDIA DE CADA DÍA"
	Para i <- 0 Hasta 4 Hacer
		Escribir "  Día ", i + 1, ": ", TemperaturaMedia(tMax[i], tMin[i]), " ºC"
	FinPara
	
	// --- 3. Días con menos temperatura ---
	// Primero buscamos cuál es la mínima más baja de todas
	menor <- tMin[0]
	Para i <- 0 Hasta 4 Hacer
		Si tMin[i] < menor Entonces
			menor <- tMin[i]
		FinSi
	FinPara
	
	// Después mostramos TODOS los días que tienen esa mínima
	// (puede haber varios empatados)
	Escribir ""
	Escribir "DÍAS CON MENOS TEMPERATURA (", menor, " ºC)"
	Para i <- 0 Hasta 4 Hacer
		Si tMin[i] = menor Entonces
			Escribir "  Día ", i + 1
		FinSi
	FinPara
	
	// --- 4. Buscar días por temperatura máxima ---
	Escribir ""
	Escribir "Introduce una temperatura para buscar: "
	Leer buscar
	
	// Suponemos que no hay ninguno hasta que encontremos uno
	encontrado <- Falso
	Escribir "Días con temperatura máxima de ", buscar, " ºC:"
	Para i <- 0 Hasta 4 Hacer
		Si tMax[i] = buscar Entonces
			Escribir "  Día ", i + 1
			encontrado <- Verdadero
		FinSi
	FinPara
	
	// Si no se encontró ninguno, avisamos
	Si No encontrado Entonces
		Escribir "  Ningún día tuvo esa temperatura máxima"
	FinSi
FinAlgoritmo