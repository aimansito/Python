SubProceso  EscribirCentrado(texto)
	Definir espacios Como Entero
	Definir margen, subrayado Como Cadena
	
	// 1 calcular cuantos espacios hay que poner delante 
	espacios <- 40 - Trunc(Longitud(texto)/2)
	// 2 construir el margen de espacios
	margen <- ""
	Mientras Longitud(margen) < espacios Hacer
		margen <- Concatenar(margen, " ")
	FinMientras
	
	// 3 Construir el subrayado con tantos "=" como letras tenga el texto
	subrayado <- ""
	Mientras Longitud(subrayado) < Longitud(texto) Hacer
		subrayado <- Concatenar(subrayado, "=")
	FinMientras
	
	// 4 escribir el texto y el subrayado , los dos con el mismo margen
	Escribir margen, texto
	Escribir margen, subrayado
FinSubProceso
Algoritmo escrCentrado
	Definir mensaje Como Cadena
	Escribir "Introduce un mensaje: "
	Leer mensaje
	EscribirCentrado(mensaje)
FinAlgoritmo
