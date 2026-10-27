// ============================================================
// EJERCICIO 10
// Lee una cadena e indica si es un palíndromo (se lee igual
// del derecho que del revés). Ignora espacios y mayúsculas,
// para que funcione con frases como "Anita lava la tina"
// ============================================================
Algoritmo palindromo
	Definir cadena, limpia, invertida, letra Como Cadena
	Definir i Como Entero
	
	Repetir
		Escribir "Introduce una palabra o frase: "
		Leer cadena
	Hasta Que Longitud(cadena) > 0
	
	// 1. Pasamos todo a minúsculas para que "A" y "a" sean iguales
	cadena <- Minusculas(cadena)
	
	// 2. Creamos una versión sin espacios
	limpia <- ""
	Para i <- 0 Hasta Longitud(cadena) - 1 Hacer
		letra <- SubCadena(cadena, i, i)
		Si letra <> " " Entonces
			limpia <- Concatenar(limpia, letra)
		FinSi
	FinPara
	
	// 3. Invertimos la versión limpia (mismo truco del ejercicio 6)
	invertida <- ""
	Para i <- 0 Hasta Longitud(limpia) - 1 Hacer
		letra <- SubCadena(limpia, i, i)
		invertida <- Concatenar(letra, invertida)
	FinPara
	
	// 4. Si al darle la vuelta queda igual, es palíndromo
	Si limpia = invertida Entonces
		Escribir "Es un palíndromo"
	SiNo
		Escribir "No es un palíndromo"
	FinSi
FinAlgoritmo