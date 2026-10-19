Funcion resultado <- EsMultiplo(a, b)
	Definir resultado Como Logico
	Si b = 0 Entonces
		
		// no se puede dividir entre 0; solo 0 es multiplo de 0
		resultado <- (a=0)
	SiNo
		// a es multiplo de b si al dividir a ente b el resto es 0 
		resultado <- (a MOD b = 0)
	FinSi
FinFuncion

Algoritmo multiplos
	Definir num1, num2 Como Entero
	
	Escribir "Introduce el primer número: "
	Leer num1
	Escribir "Introduce el segundo número: "
	Leer num2
	
	Si EsMultiplo(num1,num2) Entonces
		Escribir num1, " es múltiplo de ", num2
	FinSi
	
	Si EsMultiplo(num1,num2) Entonces
		Escribir num2, " es multiplo de ", num1
	FinSi
	
	Si No EsMultiplo(num1, num2) Y No EsMultiplo(num2, num1) Entonces
		Escribir "Ninguno es múltiplo del otro"
	FinSi
FinAlgoritmo
