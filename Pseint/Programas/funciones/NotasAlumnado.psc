Algoritmo NotasAlumnado
	Definir notasAlumnos, cantidadNotas, numAlumnos, i Como Entero 
	Definir calificaciones Como Caracter
	numAlumnos <- 10 
	Dimensionar notasAlumnos[numAlumnos]
	Dimensionar cantidadNotas[4]
	Dimensionar calificaciones[4]
	calificaciones[0] <-"Suspenso"
	calificaciones[1] <- "Aprobado"
	calificaciones[2] <- "Notable"
	calificaciones[3] <- "Sobresaliente"
	Para i <- 0 Hasta 3
		cantidadNotas[i] <- 0 
	FinPara
	Para i <- 0 Hasta numAlumnos - 1 Hacer
		notasAlumnos[i] <- Aleatorio(0,10)
	FinPara
	Para i <- 0 Hasta numAlumnos - 1
		Escribir "Nota del Alumno/a ", i +1, ": ", notasAlumnos[i]
		Segun notasAlumnos[i] Hacer
			0,1,2,3,4: cantidadNotas[0] <- cantidadNotas[0]+1
			5,6: cantidadNotas[1] <- cantidadNotas[1]+1
			7,8: cantidadNotas[2] <- cantidadNotas[2]+1
			9,10: cantidadNotas[3] <- cantidadNotas[3]+1
		FinSegun
	FinPara
	Para i <- 0 Hasta 3 Hacer
		Escribir "Hay ", cantidadNotas[i], " ", calificaciones[i]
	FinPara
	
	
FinAlgoritmo
