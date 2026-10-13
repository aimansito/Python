Algoritmo potencia
	Definir base, resultado Como Real
	Definir exponente, i Como Entero
	
	Escribir "Introduce la base:"
	Leer base
	
	Escribir "Introduce el exponente"
	Leer exponente
	
	resultado <- 1
	Para i <- 1 Hasta exponente Hacer
		resultado <- resultado * base
	FinPara
	
	Escribir "El resultado es: ", resultado
FinAlgoritmo
