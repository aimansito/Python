Funcion letra <- CalcularLetra(numero)
	Definir letra, letras Como Cadena
	Definir resto Como Entero
	
	letras <- "TRWAGMYFPDXBNJZSQVHLCKE"
	resto <- numero MOD 23
	letra <- SubCadena(letras, resto, resto)
FinFuncion

Funcion valido <- ValidarDNI(dni)
	Definir valido Como Logico
	Definir parteNumero, letraDni, caracter Como Cadena
	Definir i Como Entero
	
	valido <- Verdadero
	
	// 1. Comprobar que los 8 primeros caracteres son números
	Para i <- 0 Hasta 7 Hacer
		caracter <- SubCadena(dni, i, i)
		Si caracter < "0" O caracter > "9" Entonces
			valido <- Falso
		FinSi
	FinPara
	
	// 2. Si son números, comparar la letra
	Si valido Entonces
		parteNumero <- SubCadena(dni, 0, 7)
		letraDni <- Mayusculas(SubCadena(dni, 8, 8))
		Si letraDni = CalcularLetra(ConvertirANumero(parteNumero)) Entonces
			valido <- Verdadero
		SiNo
			valido <- Falso
		FinSi
	FinSi
FinFuncion

Algoritmo validar_dni
	Definir dni Como Cadena
	
	Escribir "Introduce tu DNI (8 números y una letra): "
	Leer dni
	
	Si Longitud(dni) <> 9 Entonces
		Escribir "Error: el DNI debe tener 9 caracteres"
	SiNo
		Si ValidarDNI(dni) Entonces
			Escribir "El DNI es correcto"
		SiNo
			Escribir "El DNI no es correcto"
		FinSi
	FinSi
FinAlgoritmo