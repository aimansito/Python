//Lee un nombre con apellidos y muestra sus iniciales en mayúsculas
Algoritmo iniciales
	Definir nombre, letra, anterior, inicles Como Cadena
	Definir i Como Entero 
	
	//Pedimos el nombre hasta que no esté vacío 
	Repetir 
		Escribir "Introduce tu nombre y apellidos: "
		Leer nombre 
	Hasta Que Longitud(nombre) > 0 
	
	inicles <- ""
	//"anterior" guarda el caracter de la vuelta anterior
	//Empieza como espacio para que la primera letra cuente
	// como inicial (es como si hubiera un espacio antes)
	
	anterior <- " "
	Para i <- 0 Hasta Longitud(nombre) - 1 Hacer
		letra <- SubCadena(nombre, i, i) 
		//Una letra es inicial si no es un espacio
		//y justo antes había un espacio
		Si letra <> " " Y anterior = " " Entonces
			inicles <- Concatenar(inicles, Mayusculas(letra))
		FinSi
		
		//Guardamos la letra actual para la siguiente vuelta 
		anterior <- letra 
	FinPara
	Escribir "Tus iniciales son: ", inicles
FinAlgoritmo
