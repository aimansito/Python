Algoritmo Conjunto_Ejercicios
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 1:Cambio de Signo"
	Definir num Como Real
	Definir resultado Como Real
	Escribir Sin Saltar "Introduce el número"
	Leer num
	resultado = num * (-1)
	Escribir Sin Saltar "El signo del número es: ",num
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 2:La media entre dos números"
	Definir num1,num2,media Como Real
	Escribir Sin Saltar "Introduce el número 1:"
	Leer num1
	Escribir Sin Saltar "Introduce el número 2:"
	Leer num2
	media = (num1+num2)/2
	Escribir Sin Saltar "La media es:",media
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 3: Conversor Euros a pesetas"
	Definir num,resultado Como Real
	Escribir Sin Saltar "Introduce la cantidad de euros a convertir"
	Leer num
	resultado = num * 166.386
	Escribir Sin Saltar "La conversión de euros a pesetas en este número es:",resultado
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 4:Volumen de un cono"
	Definir r,h,resultado Como Real
	Escribir Sin Saltar "Introduce el radio"
	Leer r
	Escribir Sin Saltar "Introduce la base"
	Leer h
	resultado = 1/3 * 3.14 * r2 * h
	Escribir Sin Saltar "El resultado del volumen de un cono es:",resultado
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 5:Operaciones Aritméticas"
	Definir num1,num2,suma,resta,mult,div Como Real
	Escribir Sin Saltar "Escribe el numero 1"
	Leer num1
	Escribir Sin Saltar "Escribe el numero 2"
	Leer num2
	suma = num1+num2
	resta = abs(num1-num2)
	mult = num1*num2
	div = num1 / num2
	Escribir Sin Saltar "Los calculos son los siguientes: Suma:",suma, " Resta:",resta," Multiplicación:",mult," División:",div
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 6:Salario Semanal:"
	Definir horas,salario,resultado Como Real
	Escribir Sin Saltar "Introduce las horas trabajadas a la semana:"
	Leer horas
	Escribir Sin Saltar "Introduce el salario por hora:"
	Leer salario
	resultado = (horas * salario) * 4
	Escribir Sin Saltar "El salario es:", resultado
	Escribir Sin Saltar "============================="
	Escribir Sin Saltar "Ejercicio 7:Calcular nota:"
	Definir nota1,mediaDeseada,nota2 Como Real
	Escribir Sin Saltar "Introduce la nota del primer examen:"
	Leer nota1
	Escribir Sin Saltar "Introduce la media deseada:"
	Leer mediaDeseada
	nota2 = (mediaDeseada - nota1 * 0.4) / 0.6
	Escribir Sin Saltar "Para tener de nota media un ",mediaDeseada," debes sacar un ",nota2," en el segundo exámen"
FinAlgoritmo
