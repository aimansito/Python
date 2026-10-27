Algoritmo examenej3
	Definir numuser, numsecret, intentos Como Entero 
	numsecret <- Aleatorio(0,100)
	intentos <- 7 
	Mientras intentos > 0 Hacer
		Escribir "Adivina el número: "
		Leer numuser
		Si num = numsecret Entonces
			Escribir "Enhorabuena has acertado el numero!"
			Escribir "Lo has conseguido en ", 8 - intentos, " intentos."
			intentos <- 0
			
		SiNo
			intentos <- intentos - 1
			Si intentos > 0 Entonces
				Si numuser < numsecret  Entonces
					Escribir "El numero a adivinar es mayor."
				SiNo
					Escribir "El numero a adivinar es menor."
				FinSi
				Escribir "Te quedan ", intentos, " intentos."
			SiNo
				Escribir "Has agotado todos los intentos."
				Escribir "El numero era: ", numsecret	
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
