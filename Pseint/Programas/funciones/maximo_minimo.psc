// ============================================================
// SUBPROCESO calcularMaxMin
// Recibe un vector de números y cuántos hay. Deja el mayor en
// "maximo" y el menor en "minimo".
// Una función de PSeInt solo puede devolver UN valor, y aquí
// necesitamos dos, así que se usan parámetros Por Referencia:
// lo que se guarde en ellos cambia las variables del programa
// principal
// ============================================================
SubProceso calcularMaxMin(numeros, n, maximo Por Referencia, minimo Por Referencia)
	Definir i Como Entero
	
	// Partimos de que el primer número es el máximo y el mínimo
	maximo <- numeros[0]
	minimo <- numeros[0]
	
	// Recorremos todos los números introducidos
	Para i <- 0 Hasta n - 1 Hacer
		// Si encontramos uno mayor, pasa a ser el máximo
		Si numeros[i] > maximo Entonces
			maximo <- numeros[i]
		FinSi
		// Si encontramos uno menor, pasa a ser el mínimo
		Si numeros[i] < minimo Entonces
			minimo <- numeros[i]
		FinSi
	FinPara
FinSubProceso


// ============================================================
// PROGRAMA PRINCIPAL
// Pide números, los guarda en un vector y muestra el máximo
// y el mínimo usando calcularMaxMin
// ============================================================
Algoritmo maximo_minimo
	Definir numeros Como Real
	Dimension numeros[100]      // posiciones de la 0 a la 99
	Definir n, i Como Entero
	Definir mayor, menor Como Real
	
	// --- 1. Preguntar cuántos números hay (entre 1 y 100) ---
	Repetir
		Escribir "¿Cuántos números vas a introducir? (1-100)"
		Leer n
	Hasta Que n >= 1 Y n <= 100
	
	// --- 2. Leer los números en las posiciones 0 a n-1 ---
	Para i <- 0 Hasta n - 1 Hacer
		// i + 1 para que el usuario vea "Número 1" y no "Número 0"
		Escribir "Número ", i + 1, ": "
		Leer numeros[i]
	FinPara
	
	// --- 3. Calcular máximo y mínimo ---
	// Tras esta llamada, "mayor" y "menor" ya tienen los resultados
	calcularMaxMin(numeros, n, mayor, menor)
	
	// --- 4. Mostrar resultados ---
	Escribir "El máximo es ", mayor
	Escribir "El mínimo es ", menor
FinAlgoritmo