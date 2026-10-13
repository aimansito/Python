Algoritmo ej3-algor
	Definir num, media, suma, contador  Como Real
	contador <- 0
	suma <- 0
	Mientras num <> 0 Hacer
		suma = suma + num
		media = suma 
		Escribir "Introduce un numero(Un cero para terminar)"
		Leer num
	FinMientras
	Si contador > 0 Entonces
		media <- suma / contador 
		Escribir "La suma de los números introducidos es: ", suma" y de la media es: ", media
	SiNo
		Escribir "No se han introducido números"
	FinSi
FinAlgoritmo
