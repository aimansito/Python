Algoritmo inverso
	//Lee una cadena y genera otra con los caracteres en orden 
	// inverso 
	
	Definir cad, invertida, letra Como Cadena
	Definir i Como Entero
	
	Repetir
		Escribir "Introduce una cadena: "
		Leer cad
	Hasta Que Longitud(cad) > 0
	
	invertida <- "" 
	//Recorremos la cadena de principio a fin
	Para i <- 0 Hasta Longitud(cad) - 1 Hacer
		letra <- Subcadena(cad, i, i) 
		invertida <- Concatenar(letra, invertida)
	FinPara
	
	Escribir "Cadena invertida: ", invertida
FinAlgoritmo
