Algoritmo examenej6
	Definir notas_clase,notas_criterio Como Entero
	Dimension notas_clase[10] , notas_criterio[4][4] 
	Definir i,j Como Entero
	
	Para i <- 0 Hasta 11 Hacer
		notas_clase[i] <- Aleatorio(0,10)
	FinPara
	
	Para i <- 0 Hasta 9 Hacer
		Para j <- Hasta 3 Hacer
			Si notas_clase[i] > 0 O notas_clase[i] < 4
				
				notas_criterio[i][j] <- notas_clase[i]
				
			Sino Si notas_clase[i] = 5 O notas_clase[i] = 6
					
					notas_criterio[i][j] <- notas_clase[i]
					
			SiNo Si notas_clase[i] = 7 O notas_clase[i] =8 
						
					notas_criterio[i][j] <- notas_clase[i]
					
			SiNo Si notas_clase[i] = 9 O notas_clase[i] = 10
					
					notas_criterio[i][j] <- notas_clase[i]
					
			FinSi
		FinPara
	FinPara
	
	Para i <- 0 Hasta 3 Hacer
		Para j <- 0 Hasta 3 Hacer
			Escribir notas_criterio[i][j]
		FinPara
	FinPara
FinAlgoritmo
