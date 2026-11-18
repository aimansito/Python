Algoritmo Temperatura
	Definir temperaturas como Real
	Definir i, diasSuperanMedia como Entero
	Definir suma, media como Real
	Definir dias Como Caracter
	Dimension dias[7]
	Dimension temperaturas[7]
	dias[0] <- "Lunes" 
	dias[1] <- "Martes"
	dias[2] <- "Miercoles"
	dias[3] <- "Jueves"
	dias[4] <- "Viernes"
	dias[5] <- "Sabado"
	dias[6] <- "Domingo"
	
	suma <- 0
	//Leer la temperatura de cada dia
	Para i <- 0 hasta 6 Hacer
		//Leer la temperatura validando el rango
		Repetir
			Escribir "Introduce la temperatura del día ", i+1
			Leer temperaturas[i]
		Hasta Que temperaturas[i]>=-50 Y temperaturas[i]<=60
		
		suma <- suma + temperaturas[i]
	FinPara
	
	diasSuperanMedia <- 0
	media <- suma/7
	Escribir "La temperatura media ha sido ",media, "ºC"
	Para i <- 0 hasta 6 Hacer
		Si temperaturas[i] > media Entonces
			Escribir "El día ", dias[i], " ha superado la media"
			diasSuperanMedia <- diasSuperanMedia+1
		FinSi
	FinPara
	Si diasSuperanMedia = 0 Entonces
		Escribir "Ningún día de la semana supera la media"
	FinSi
FinAlgoritmo
