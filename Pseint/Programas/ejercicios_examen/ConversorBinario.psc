Funcion binario <- ConvertirABinario(num)
	Definir binario Como Caracter
	Definir n, resto Como Entero
	n <- num
	Si n = 0 Entonces
		binario <- "0"
	SiNo
		binario <- ""
		Mientras n > 0 Hacer
			resto <- n MOD 2
			binario <- Concatenar(ConvertirATexto(resto), binario)
			n <- Trunc(n / 2)
		FinMientras
	FinSi
FinFuncion

Funcion decimal <- ConvertirADecimal(binario)
	Definir decimal, i Como Entero
	decimal <- 0
	Para i <- 1 Hasta Longitud(binario) Hacer
		decimal <- decimal * 2 + ConvertirANumero(Subcadena(binario, i, i))
	FinPara
FinFuncion

Algoritmo ConversorBinario
	Definir opcion, num, i Como Entero
	Definir bin Como Caracter
	Definir valido Como Logico
	
	Repetir
		Escribir ""
		Escribir "1. Convertir de decimal a binario"
		Escribir "2. Convertir de binario a decimal"
		Escribir "3. Salir"
		Escribir "Elige una opción:"
		Leer opcion
		
		Segun opcion Hacer
			1:
				Repetir
					Escribir "Introduce un número entero (0 o mayor):"
					Leer num
				Hasta Que num >= 0
				Escribir num, " en binario es ", ConvertirABinario(num)
			2:
				Repetir
					Escribir "Introduce un número binario:"
					Leer bin
					valido <- Longitud(bin) > 0
					Para i <- 1 Hasta Longitud(bin) Hacer
						Si Subcadena(bin, i, i) <> "0" Y Subcadena(bin, i, i) <> "1" Entonces
							valido <- Falso
						FinSi
					FinPara
					Si No valido Entonces
						Escribir "Eso no es un número binario."
					FinSi
				Hasta Que valido
				Escribir bin, " en decimal es ", ConvertirADecimal(bin)
			3:
				Escribir "¡Hasta luego!"
			De Otro Modo:
				Escribir "Opción no válida."
		FinSegun
	Hasta Que opcion = 3
FinAlgoritmo