Algoritmo multiplicaciones
	Definir i, num1, num2, respuesta, correcta, aciertos Como Entero
	aciertos <- 0 
	
	Para i <- 1 Hasta 10 Hacer
		//1. Generar dos números al azar 
		num1 <- Aleatorio(1,10)
		num2 <- Aleatorio(1,10)
		correcta <- num1 * num2 
		//2. Preguntar
		Escribir "Pregunta ", i, ": ¿Cuánto es ", num1 ," x ", num2, "?"
		Leer respuesta
		
		//3. Comprobar la respuesta
		Si respuesta = correcta Entonces
			Escribir "¡Correcto!"
			aciertos <- aciertos + 1
		SiNo
			Escribir "Incorrecto. La respuesta correcta es ", correcta
		FinSi
	FinPara
	//4. Resultado Final
	Escribir "Has acertado", aciertos , " de 10"
FinAlgoritmo
