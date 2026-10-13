Algoritmo factorial
	Definir num, i, fact Como Entero
	Escribir  "Introduce un numero:"
	Leer num
	fact <- 1
	Para i <- 1 Hasta num Hacer
		fact <- fact * i
	FinPara
	Escribir "El factorial de ", num, " es: ", fact
FinAlgoritmo
