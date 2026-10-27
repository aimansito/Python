// ============================================================
// Rellena un vector de 10 enteros pidiendo números hasta que
// se llene o se introduzca un número negativo. Después muestra
// solo los elementos que se han introducido
// ============================================================
Algoritmo rellenar_vector
	Definir numeros Como Entero
	Dimension numeros[10]       // posiciones de la 0 a la 9
	Definir num, n, i Como Entero
	
	// "n" cuenta cuántos números se han guardado.
	// También indica en qué posición va el siguiente
	n <- 0
	
	// --- 1. Pedir números ---
	Repetir
		Escribir "Introduce un número (negativo para terminar): "
		Leer num
		
		// Solo se guarda si no es negativo
		Si num >= 0 Entonces
			numeros[n] <- num
			n <- n + 1
		FinSi
		
		// Paramos si el vector está lleno o si el número fue negativo
	Hasta Que n = 10 O num < 0
	
	// --- 2. Mostrar los elementos introducidos ---
	Si n = 0 Entonces
		Escribir "No se ha introducido ningún número"
	SiNo
		Escribir "Has introducido ", n, " números:"
		// Solo recorremos hasta n - 1, no hasta 9,
		// porque el resto de posiciones están vacías
		Para i <- 0 Hasta n - 1 Hacer
			Escribir "  Posición ", i, ": ", numeros[i]
		FinPara
	FinSi
FinAlgoritmo