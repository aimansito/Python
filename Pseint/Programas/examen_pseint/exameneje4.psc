Algoritmo examenej4
	Definir dias_semana, temp, i, contador, media, suma Como Real
	Dimension dias_semana[7]
	contador <- 7
	suma <- 0
	media <- 0
	Repetir
		Escribir "Introduce un número: "
		Leer temp
		Para i <- 0 Hasta 6 Hacer
			Si temp > -50 Y temp < 60 Entonces
				dias_semana[i] <- temp
				contador <- contador - 1 
			FinSi
		FinPara 
	Hasta Que contador = 0
	
	Para i <- 0 Hasta 6 Hacer
		suma <- dias_semana[i] + suma
		media <- suma / 7
	FinPara
	
	Para i <- 0 Hasta 6 Hacer
		Si dias_semana[i] > media Entonces
			Segun i Hacer
				0: Escribir "Lunes tiene la temperatura: ",dias_semana[i]
					
				1: Escribir "Martes tiene la temperatura: ",dias_semana[i]
					
				2: Escribir "Miercoles tiene la temperatura: ",dias_semana[i]
					
				3: Escribir "Jueves tiene la temperatura: ",dias_semana[i]
					
				4: Escribir "Viernes tiene la temperatura: ",dias_semana[i]
					
				5: Escribir "Sabado tiene la temperatura: ",dias_semana[i]
					
				6: Escribir "Domingo tiene la temperatura: ",dias_semana[i]
					
			FinSegun
		FinSi
	FinPara
FinAlgoritmo
