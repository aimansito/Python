Algoritmo cuadradosycubos
	Definir vector_numeros Como Entero
	Dimension vector_numeros[10]
	Definir i Como Entero
	
	// 1.Rellenar el vector con números aleatorios del 1 al 10
	Para i <- 0 Hasta 11 Hacer
		vector_numeros[i] <- Aleatorio(1,10)
	FinPara
	
	//2. Mostrar cada numero con su cuadrado y su cubo
	Escribir "Número", "   ","Cuadrado", "    ", "Cubo"
	Para i <- 1 Hasta 10 Hacer
		Escribir vector_numeros[i], "         ", vector_numeros[i] ^ 2, "          ", vector_numeros[i] ^ 3
	FinPara
FinAlgoritmo
