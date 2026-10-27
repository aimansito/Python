Algoritmo random
	Definir num, numeroSecreto, intentos Como Entero
	numeroSecreto <- Aleatorio(0,100)
	intentos <- 10

	Mientras intentos > 0 Hacer
		Escribir "Introduce un número del 0 al 100"
		Leer num 
		Si num = numeroSecreto Entonces
			Escribir "Enhorabuena has acertado el numero!"
			Escribir "Lo has conseguido en ", 11 - intentos, " intentos."
			intentos <- 0
		SiNo
			intentos <- intentos -1
			Si intentos > 0 Entonces
				Si num < numeroSecreto  Entonces
					Escribir "El numero a adivinar es mayor."
				SiNo
					Escribir "El numero a adivinar es menor."
				FinSi
				Escribir "Te quedan ", intentos, " intentos."
			SiNo
				Escribir "Has agotado todos los intentos."
				Escribir "El numero era: ", numeroSecreto	
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
