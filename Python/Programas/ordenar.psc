Algoritmo sin_titulo
	Definir num1,num2,num3 Como Real
	Definir aux Como Real
	Escribir "Introduce el primer num"
	Leer num1
	Escribir "Introduce el segundo num"
	Leer num2
	Escribir "Introduce el tercer num"
	Leer num3
	Si num1 > num2 Entonces
		aux <- num1
		num1 <- num2
		num2 <- aux
		Sino Si num1 > num3 Entonces
		aux <- num1
		num1 <- num3
		num3 <- aux
		FinSi
		Sino Si  num2 > num3 Entonces
		aux <- num2
		num2 <- num3
		num3 <- aux
		FinSi
	FinSi
	Escribir "Números ordenados de menor a mayor"
	Escribir  num1," ",num2," ",num3
FinAlgoritmo
