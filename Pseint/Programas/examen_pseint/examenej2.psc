Funcion primo <- esPrimo(num1,num2)
	Definir primo Como Logico
	primo <- Falso
	Si num1 MOD num2 = 0 Entonces
		primo <- Verdadero
	FinSi
FinFuncion

Algoritmo examenej2
	Definir num1, num2 Como Entero
	Repetir
		Escribir "Introduce el primer numero: "
		Leer num1
		Escribir "Introduce el segundo numero: "
		Leer num2
	Hasta Que num1 >= 2 Y num2 >=2 
	
	
	Si esPrimo(num1,num2) <- Verdadero Entonces
		Escribir "Los numeros ",num1,  " y ",num2 ," son primos gemelos"
	SiNo
		Escribir "Los numeros ",num1,  " y ",num2 ," no son primos gemelos"
	FinSi
FinAlgoritmo
