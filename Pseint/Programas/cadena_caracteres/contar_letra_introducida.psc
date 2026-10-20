Algoritmo contar_letra_introducida
	Definir cade,caract Como Cadena
	Definir i, contador Como Entero
	
	Escribir "Introduce  una cadena: "
	Leer cade
	cade <- Minusculas(cade)
	Repetir 
		Escribir "Introduce un caracter: "
		Leer caract
		caract <-  Minusculas(caract)
	Hasta Que Longitud(caract)=1
	contador <- 0
	Para i <- 0 Hasta Longitud(cade)-1 Hacer
		Si Subcadena(cade,i,i) = caract Entonces
			contador <- contador + 1
		FinSi
	FinPara
	Escribir "El caracter aparece ",  contador, " veces."
FinAlgoritmo
