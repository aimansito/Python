Algoritmo saber_subcadena
	Definir cade, subcade Como Cadena
	Escribir "Introduce una cadena: "
	Leer cade
	Escribir "Introduce una subcadena: "
	Leer subcade
	
	Si Subcadena(cade,0,Longitud(subcade)-1) = subcade Entonces
		Escribir "La cadena comienza por la subcadena"
	SiNo
		Escribir "La cadena NO comienza por la subcadena"
	FinSi
FinAlgoritmo
