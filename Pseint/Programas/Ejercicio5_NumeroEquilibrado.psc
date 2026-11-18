Algoritmo NumeroEquilibrado
	Definir num, numeroIntroducido, digito Como Entero
	Definir sumaPares, sumaImpares Como Entero
	
	sumaPares <- 0
	sumaImpares <- 0
	
	Repetir
		Escribir "Introduzca un número mayor o igual que 1: "
		Leer numeroIntroducido
	Hasta Que numeroIntroducido>=1
	
	num <- numeroIntroducido
	Repetir
		digito <- num % 10
		num <- trunc(num / 10)
		Si digito % 2 = 0 Entonces
			sumaPares <- sumaPares + digito
		SiNo
			sumaImpares <- sumaImpares + digito
		FinSi
	Hasta que num=0
	
	Si sumaPares = sumaImpares Entonces
		Escribir "El número ", numeroIntroducido, " es equilibrado"
	SiNo
		Escribir "El número ", numeroIntroducido, " NO es equilibrado"
	FinSi
FinAlgoritmo
