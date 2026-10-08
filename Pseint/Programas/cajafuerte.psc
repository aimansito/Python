Algoritmo sin_titulo
	Definir clave, num, i Como Entero
	num <- 4325
	i <- 4
	Mientras i>0 Hacer
		Escribir 'Introduce la clave'
		Leer clave
		Si clave==num Entonces
			Escribir 'Has acertado'
			i <- 0
		SiNo
			Escribir 'Intentalo de nuevo'
			i <- i-1
		FinSi
	FinMientras
FinAlgoritmo
