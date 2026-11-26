Algoritmo Capicua
	Definir num, original, digito, invertido Como Entero
	Repetir 
		Escribir "Número mayor o igual que 1: "
		Leer original 
	Hasta Que original >= 1 
	num <- original 
	invertido <- 0
	Repetir
		digito <- num % 10
		invertido <- invertido * 10 + digito
		num <- trunc(num/10)
	Hasta Que num = 0 
	
	Si invertido = original Entonces
		Escribir original, " es capicua"
	SiNo
		Escribir original, " NO es capicua" 
	FinSi
FinAlgoritmo
