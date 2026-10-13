Algoritmo vocales	
	Definir vocal, caract Como Caracter
	Escribir "Introduce una letra"
	Leer caract 
	Mientras caract <> " " Hacer
		Si caract = "a" o caract = "e" o caract = "i" o caract = "o" o caract = "u" Entonces
			Escribir "VOCAL"
		SiNo
			Escribir "NO VOCAL"
		FinSi
		Escribir "Introduce un caracter (espacio para terminar): "
        Leer caract
	FinMientras
FinAlgoritmo
