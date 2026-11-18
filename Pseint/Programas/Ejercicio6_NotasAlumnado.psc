

Algoritmo NotasAlumnado
	
	Definir notasAlumnos, numAlumnos, cantidadNotas, i como Entero
	Definir calificaciones Como Caracter
	
	numAlumnos <- 10
	Dimension notasAlumnos[numAlumnos]
	Dimension cantidadNotas[4]
	Dimension calificaciones[4]
	calificaciones[0] <- "Suspensos"
	calificaciones[1] <- "Aprobados"
	calificaciones[2] <- "Notables"
	calificaciones[3] <- "Sobresalientes"
	
	//Iniciliazar el array de cantidad de notas 
	Para i <- 0 Hasta 3 Hacer
		cantidadNotas[i] <- 0
	FinPara
	
	//Generar las notas aleatorias de 0 a 10
	Para i <- 0 hasta numAlumnos-1 Hacer
		notasAlumnos[i] <- Aleatorio(0, 10)
	FinPara
	
	//Contar las notas de cada calificación
	Para i <- 0 hasta numAlumnos-1 Hacer
		Escribir "Nota del alumno/a ", i+1, ": ",notasAlumnos[i]
		Segun notasAlumnos[i] Hacer
			0,1,2,3,4: cantidadNotas[0] <- cantidadNotas[0]+1
			5,6: cantidadNotas[1] <- cantidadNotas[1]+1
			7,8: cantidadNotas[2] <- cantidadNotas[2]+1
			9,10: cantidadNotas[3] <- cantidadNotas[3]+1
		FinSegun
	FinPara
	
	//Mostrar la cantidad de notas del alumnado
	Para i <- 0 hasta 3 Hacer
		Escribir "Hay ", cantidadNotas[i]," ",calificaciones[i]
	FinPara
	
	
FinAlgoritmo
