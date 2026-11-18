

Algoritmo AdivinarNumero
	Definir intentos, numSecreto, numUsuario, i Como Entero
	Definir acertado como Logico
	acertado <- falso
	intentos<- 7
	numSecreto <- Aleatorio(1,100)
	
	//Línea de depuración para conocer el número secreto en las pruebas
	//Escribir "numero secreto", numSecreto
	
	i<-0
	
	Repetir
		i <- i+1
		Repetir
			Escribir sin saltar "Intento ",i," de ",intentos,"."
			Escribir sin saltar "Introduce un numero (1-100): "
			Leer numUsuario
		Hasta Que numUsuario>=1 y numUsuario <=100
		Si numUsuario > numSecreto Entonces
			Escribir "El número secreto es MENOR"
		Sino 
			Si numUsuario < numSecreto Entonces
				Escribir "El número secreto es MAYOR"
			sino 
				acertado <- Verdadero
				Escribir "Has acertado en ", i, " intentos"
			FinSi
		FinSi
	Hasta Que acertado=Verdadero O i = intentos
	
	Si acertado = Falso Entonces
		Escribir "El número secreto es: ",numSecreto
	FinSi
	
FinAlgoritmo
