// ============================================================
// Declara tres vectores de 5 enteros, pide los valores de
// vector1 y vector2, y calcula vector3 = vector1 + vector2
// sumando posición a posición
// ============================================================
Algoritmo suma_vectores
	Definir vector1, vector2, vector3 Como Entero
	Dimension vector1[5]
	Dimension vector2[5]
	Dimension vector3[5]
	Definir i Como Entero
	
	// --- 1. Pedir los valores de vector1 ---
	Escribir "Valores del vector 1:"
	Para i <- 0 Hasta 4 Hacer
		Escribir "  Posición ", i, ": "
		Leer vector1[i]
	FinPara
	
	// --- 2. Pedir los valores de vector2 ---
	Escribir "Valores del vector 2:"
	Para i <- 0 Hasta 4 Hacer
		Escribir "  Posición ", i, ": "
		Leer vector2[i]
	FinPara
	
	// --- 3. Calcular vector3 ---
	// Cada posición de vector3 es la suma de la MISMA
	// posición de vector1 y vector2
	Para i <- 0 Hasta 4 Hacer
		vector3[i] <- vector1[i] + vector2[i]
	FinPara
	
	// --- 4. Mostrar los tres vectores en columnas ---
	Escribir ""
	Escribir "Pos   V1   V2   V3"
	Para i <- 0 Hasta 4 Hacer
		Escribir i, "     ", vector1[i], "    ", vector2[i], "    ", vector3[i]
	FinPara
FinAlgoritmo