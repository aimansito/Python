// ============================================================
// EJERCICIO 7
// Lee una cadena y dos caracteres, y sustituye cada aparición
// del primero por el segundo. Ej: "casa", a, o -> "coso"
// ============================================================
Algoritmo sustituir_caracter
	Definir cadena, buscar, poner, nueva, letra Como Cadena
	Definir i Como Entero
	
	Repetir
		Escribir "Introduce una cadena: "
		Leer cadena
	Hasta Que Longitud(cadena) > 0
	
	// Validamos que cada carácter tenga longitud 1
	Repetir
		Escribir "Carácter que quieres sustituir: "
		Leer buscar
	Hasta Que Longitud(buscar) = 1
	
	Repetir
		Escribir "Carácter por el que lo sustituyes: "
		Leer poner
	Hasta Que Longitud(poner) = 1
	
	nueva <- ""
	
	// Construimos la cadena nueva letra a letra
	Para i <- 0 Hasta Longitud(cadena) - 1 Hacer
		letra <- SubCadena(cadena, i, i)
		Si letra = buscar Entonces
			// Es el carácter a sustituir: ponemos el nuevo
			nueva <- Concatenar(nueva, poner)
		SiNo
			// Cualquier otro carácter se copia tal cual
			nueva <- Concatenar(nueva, letra)
		FinSi
	FinPara
	
	Escribir "Resultado: ", nueva
FinAlgoritmo