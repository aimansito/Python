// ============================================================
// EJERCICIO 8
// Lee una cadena y cambia las mayúsculas a minúsculas y las
// minúsculas a mayúsculas. Ej: "Hola Mundo" -> "hOLA mUNDO"
// ============================================================
Algoritmo cambiar_mayusculas
	Definir cadena, nueva, letra Como Cadena
	Definir i Como Entero
	
	Repetir
		Escribir "Introduce una cadena: "
		Leer cadena
	Hasta Que Longitud(cadena) > 0
	
	nueva <- ""
	
	Para i <- 0 Hasta Longitud(cadena) - 1 Hacer
		letra <- SubCadena(cadena, i, i)
		
		// Si la letra cambia al pasarla a minúscula,
		// es que era mayúscula
		Si letra <> Minusculas(letra) Entonces
			nueva <- Concatenar(nueva, Minusculas(letra))
		SiNo
			// Si no era mayúscula, la pasamos a mayúscula.
			// Los espacios, números y signos no cambian
			nueva <- Concatenar(nueva, Mayusculas(letra))
		FinSi
	FinPara
	
	Escribir "Resultado: ", nueva
FinAlgoritmo