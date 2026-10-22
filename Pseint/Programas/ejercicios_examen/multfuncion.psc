Funcion num <- GenerarNumero()
	Definir num Como Entero
	num <- Aleatorio(1,100)
FinFuncion
Funcion respuesta <- Preguntar(num1,num2,numPregunta)
	Definir respuesta Como Entero
	Escribir "Pregunta ", numPregunta, ": ¿Cuanto es ", num1, " x ", num2, " ? "
FinFuncion
Funcion acierto <- ComprobaRespuesta(num1,num2, respuesta)
	Definir acierto Como Logico
	Definir correcto Como Entero
	correcto <- num1 * num2
	Si respuesta = correcta Entonces
		Escribir "Correcta"
		acierto <- Verdadero
	SiNo
		Escribir "Incorrecto"
		acierto <- Falso
	FinSi
FinFuncion

Algoritmo multiplicacionesFunciones
	Definir i, num1, num2 , respuesta, aciertos Como Entero
	aciertos <- 0 
	Para i <- 1 Hasta 10 Hacer
		num1 <- GenerarNumero()
		num2 <- GenerarNumero()
		respuesta <- Preguntar(num1,num2,i)
		Si ComprobarRespuesta(num1,num2,respuesta) Entonces
			aciertos <- aciertos + 1
		FinSi
	FinPara
	
	Escribir "Has acertado ", aciertos, " de 10"
FinAlgoritmo
