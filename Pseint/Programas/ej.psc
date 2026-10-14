Algoritmo cadena2	
	Definir cadena, subcadena Como Cadena
	Escribir "Introduce una cadena: "
	Leer cadena
	Escribir "Introduce una subcadena: "
	Leer subcadena
	Si SubCadena(cadena, 0, Longitud(subcadena)-1) = subcadena Entonces 
		Escribir "La cadena comienza por la subcadena"
	SiNo
		Escribir "La cadena NO comienza por la subcadena"
	FinSi
FinAlgoritmo
