Algoritmo primos2
	Definir n,contador,num,divisor Como Entero
	Definir primo Como Logico
	Escribir "¿Cuantos numeros primos quieres mostrar?"
	Leer n
	
	contador <- 0
	num <- 2
	
	Mientras contador < n Hacer
		primo <- Verdadero
		Para divisor <- 2 Hasta num - 1 Hacer
			Si num MOD divisor = 0 Entonces
				primo <- Falso
			FinSi
		FinPara
		Si primo Entonces
			Escribir num
			contador <- contador + 1
		FinSi
		
		num <- num + 1 
	FinMientras
FinAlgoritmo
