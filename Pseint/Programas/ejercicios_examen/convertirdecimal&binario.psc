Funcion resultado <- ConvertirABinario(num)
	Definir resultado Como Caracter
	Definir n, resto Como Entero
	n <- num 
	Si n = 0 Entonces
		binario <- "0"
	SiNo
		binario <- ""
		Mientras n > 0 Hacer
			resto <- n MOD 2
			binario <- Concatenar(ConvertirATexto(resto),binario)
			n <- Trunc(n/2)
		FinMientras
	FinSi
FinFuncion
Funcion decimal <- ConvertirADecimal(binario)
	Definir decimal, i Como Entero
	decimal <- 0 
	Para i <- 1 Hasta Longitud(binario) Hacer
		decimal <- decimal * 2 + ConvertirANumero(SubCadena(binario,i,i))
	FinPara
FinFuncion

Algoritmo ConvertirBinario
	Definir op, num, i Como Entero
	Definir bin Como Caracter
	Definir valido Como Logico
	
	Repetir 
		Escribir ""
		Escribir "1. Convertir de decimal a binario"
		Escribir "2. Convertir de binario a decimal"
		Escribir "3. Salir"
		Escribir "Elige una opción"
		Leer op
		
		Segun op Hacer
			1: 
				Repetir 
					Escribir "Introduce un numero entero ( 0 a mayor ):"
					Leer num
				Hasta Que num >= 0
				Escribir num, " en binario es ", ConvertirABinario(num)
			2:
				Repetir
					Escribir "Introduce un número binario: "
					Leer bin 
					valido <- Longitud(bin) > 0
					Para i <- 1 Hasta Longitud(bin) Hacer
						Si Subcadena(bin,i,i) Y  
					FinPara
				Hasta Que 
			3:
			De Otro Modo:
				
		FinSegun
	Hasta Que 
FinAlgoritmo
