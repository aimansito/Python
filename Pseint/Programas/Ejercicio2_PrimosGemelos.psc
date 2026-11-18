

Funcion primo <- esPrimo(num)
	Definir contador, limite Como Entero
	Definir primo como Logico
	
	contador <- 2
	limite <- Trunc(raiz(num))
	primo <- verdadero
	Mientras contador<=limite Y primo Hacer
		Si num%contador = 0 Entonces
			primo <- falso
		FinSi
		contador <- contador+1
	FinMientras
FinFuncion

Algoritmo PrimosGemelos
	Definir num1, num2 Como Entero
	
	Repetir
		Escribir "Introduce el numero 1"
		Leer num1
	Hasta Que num1>=2
	Repetir
		Escribir "Introduce el numero 2"
		Leer num2
	Hasta Que num2>=2	
	
	Si esPrimo(num1) Y esPrimo(num2) Y abs(num1-num2)=2 Entonces
		Escribir "Los números ",num1, " y ", num2, " son PRIMOS GEMELOS"
	SiNo
		Escribir "No son primos gemelos"
	FinSi
	
FinAlgoritmo
