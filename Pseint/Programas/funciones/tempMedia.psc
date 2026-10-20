Funcion media <- calculo(max,min)
	Definir media Como Real
	media <- (max + min) / 2
FinFuncion
Algoritmo calcularTemperaturaMedia
	Definir numDias, i Como Entero
	Definir tMax, tMin Como Real
	
	Repetir
		Escribir "¿Cuántos días vas a introducir?"
		Leer numDias
	Hasta Que numDias > 0  
	
	Para i <- 1 Hasta numDias Hacer
		Escribir "Dia ", i 
		Escribir "Temperatura máxima: "
		Leer tMax
		Escribir "Temperatura mínima: "
		Leer tMin
		Escribir "La temperatura media del día ", i, " es ", calculo(tMax, tMin), " ºC"
	FinPara
FinAlgoritmo
