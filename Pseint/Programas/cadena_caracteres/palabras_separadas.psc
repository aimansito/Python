Algoritmo palabras_separadas
	Definir frase, letra, palabraActual Como Cadena
	Definir i, numPalabras Como Entero 
	Definir listaPalabras Como Cadena
	Dimension listaPalabras[100]
	
	Escribir  "Introduce una frase: "
	Leer frase
	numPalabras <- 0 
	palabraActual <- ""
	
	Para i <- 0 Hasta Longitud(frase)-1 Hacer 
		letra <- SubCadena(frase, i,i)
		Si letra = " " Entonces
			Si palabraActual <> "" Entonces
				listaPalabras[numPalabras] <- palabraActual
				numPalabras <- numPalabras + 1
				palabraActual <- ""
 			FinSi
		SiNo
			palabraActual <- Concatenar(palabraActual,letra)
		FinSi
	FinPara
	Si palabraActual <> "" Entonces
		listaPalabras[numPalabras] <- palabraActual
		numPalabras <- numPalabras + 1
	FinSi
	Escribir "La frase tiene ", numPalabras, " palabras"
	Si numPalabras > 0 Entonces
		Para i <- 0 Hasta numPalabras - 1 Hacer
			
			Escribir "Palabra ", i+1, ": ", listaPalabras[i]
		FinPara
	FinSi
FinAlgoritmo
