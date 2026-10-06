Algoritmo nota
	Definir nota1, nota2, nota3, media Como Real
	Definir rec Como Cadena 
	Escribir "Introduce la nota del primer examen"
	Leer nota1
	Escribir "Introduce la nota del segundo examen"
	Leer nota2
	media <- (nota1+nota2) / 2
	Si media >= 5 Entonces
		Escribir "Aprobado"
		Escribir "Media: ",media
	SiNo
		Escribir "Resultado de la recuperación(apto/no apto?"
		Leer rec
		Si rec = "apto" Entonces
			media <-5
		FinSi
		Escribir "Nota Final: ",media
	FinSi
FinAlgoritmo
