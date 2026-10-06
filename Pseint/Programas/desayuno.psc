Algoritmo desayuno
	Definir comida, tipoTostada, bebida Como Caracter
	Definir precio Como Real
	precio <- 0
	Escribir "¿Que ha tomado? (tostada/churros/donuts)"
	Leer comida
	Si comida = "tostada" Entonces
		Escribir "Tostada básica o especial?"
		Leer tipoTostada
		
		Si tipoTostada = "basica" Entonces
			precio <- precio + 1.20
		SiNo
			precio <- precio + 1.60
		FinSi
		
	SiNo
		Si comida = "churros" Entonces
			precio <- precio + 1.50
		SiNo
			precio <- precio + 1.00
		FinSi
	FinSi
	
	Escribir "Qué va a beber?(zumo/café)"
	Leer bebida
	Si bebida = "zumo" Entonces
		precio <- precio + 1.80
	SiNo
		precio <- precio + 1.20
	FinSi
	
	Escribir  "El precio total del desayuno es: ",precio, " euros"
FinAlgoritmo
