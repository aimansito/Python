Algoritmo cadena3
	Definir caden, caract Como Cadena
	Definir i , contador Como Entero
	Escribir "Introduce una cadena: "
	Leer caden
	
	Repetir 
		Escribir "Introduce un caracter:"
		Leer caract
	Hasta Que Longitud(caract) = 1
	contador <- 0
	caden <- Minusculas(caden)
	caract <- Minusculas(caract)
	Para i <- 0 Hasta Longitud(caden) - 1 Hacer
		Si SubCadena(caden,i,i) = caract Entonces
			contador <- contador + 1
		FinSi
	FinPara
	Escribir "La palabra ", caden, " incluye la letra ", caract, " ", contador, " veces"
FinAlgoritmo
