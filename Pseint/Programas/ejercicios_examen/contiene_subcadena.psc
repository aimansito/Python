// ============================================================
// EJERCICIO 9
// Lee una cadena y una subcadena, y comprueba si la primera
// contiene a la segunda. Ej: "programacion" contiene "gram"
// ============================================================
Algoritmo contiene_subcadena
	Definir cadena, sub, trozo Como Cadena
	Definir i, largoCadena, largoSub Como Entero
	Definir encontrada Como Logico
	
	Repetir
		Escribir "Introduce la cadena: "
		Leer cadena
	Hasta Que Longitud(cadena) > 0
	
	Repetir
		Escribir "Introduce la subcadena a buscar: "
		Leer sub
	Hasta Que Longitud(sub) > 0
	
	largoCadena <- Longitud(cadena)
	largoSub <- Longitud(sub)
	encontrada <- Falso
	
	// Si la subcadena es más larga, es imposible que esté dentro
	Si largoSub <= largoCadena Entonces
		// Probamos cada posición donde podría empezar la subcadena
		Para i <- 0 Hasta largoCadena - largoSub Hacer
			// Recortamos un trozo del mismo tamaño que la subcadena
			trozo <- SubCadena(cadena, i, i + largoSub - 1)
			// Si el trozo coincide, la hemos encontrado
			Si trozo = sub Entonces
				encontrada <- Verdadero
			FinSi
		FinPara
	FinSi
	
	Si encontrada Entonces
		Escribir "La cadena contiene a '", sub, "'"
	SiNo
		Escribir "La cadena NO contiene a '", sub, "'"
	FinSi
FinAlgoritmo