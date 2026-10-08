Algoritmo media_numeros
	Definir num, contador, media, suma, div Como Real
	suma <- 0
	contador <- 1
	div <- 0
	Mientras contador>0 Hacer
		Escribir 'Introduce un número(negativo para terminar)'
		Leer num
		Si num<0 Entonces
			contador <- 0
			Escribir 'Has introducido un número negativo'
			Escribir 'La media es : ', media
		SiNo
			div = div + 1
			suma <- suma+num
			media <- suma/div
		FinSi
	FinMientras
FinAlgoritmo
