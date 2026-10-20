Funcion resultado <- ConvertirEspacio(texto)
	Definir resultado Como Cadena
	Definir i Como Entero
	resultado <- ""
	Para i <- 0 Hasta Longitud(texto)  Hacer
		resultado <- Concatenar(resultado, SubCadena(texto,i,i))
		resultado <- Concatenar(resultado," ")
	FinPara
FinFuncion
Algoritmo ConvertirEspaciado
	Definir frase Como Cadena
	Escribir "Introduce un texto: "
	Leer frase 
	Escribir ConvertirEspacio(frase)
FinAlgoritmo
