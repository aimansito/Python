Algoritmo ConvertirARomano
	Dimension valores[13], simbolos[13]
	Definir valores, num, n, i Como Entero
	Definir simbolos, romano Como Caracter
	
	//Tabla de equivalencias (de mayor a menor)
	valores[0]<- 1000; simbolos[0]<- "M"
	valores[1]<- 900;  simbolos[1]<- "CM"
	valores[2]<- 500;  simbolos[2]<- "D"
	valores[3]<- 400;  simbolos[3]<- "CD"
	valores[4]<- 100;  simbolos[4]<- "C"
	valores[5]<- 90;   simbolos[5]<- "XC"
	valores[6]<- 50;   simbolos[6]<- "L"
	valores[7]<- 40;   simbolos[7]<- "XL"
	valores[8]<- 10;   simbolos[8]<- "X"
	valores[9]<- 9;   simbolos[9]<- "IX"
	valores[10]<- 5;   simbolos[10]<- "V"
	valores[11]<- 4;   simbolos[11]<- "IV"
	valores[12]<- 1;   simbolos[12]<- "I"
	Repetir
		Escribir "Pedir número mayor que 1 y menor o  igual que 1000"
		Leer num
		Si num <= 1 O num > 1000 Entonces
			Escribir "Número fuera de rango"
		FinSi
	Hasta Que num > 1 Y num <= 1000
	
	
	//Conversion
	n <- num
	romano <- ""
	Para i <- 1 Hasta 13 Hacer
		Mientras n >= valores[i] Hacer
			romano <- Concatenar(romano, simbolos[i])
			n <- n - valores[i]
		FinMientras
	FinPara
	Escribir num, " en números romano es ", romano
FinAlgoritmo
