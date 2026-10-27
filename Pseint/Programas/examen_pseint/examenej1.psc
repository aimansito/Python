Funcion cadenaCifrada <- cifrar(mensaje,n)
	Definir msj Como Cadena
	Definir i Como Entero
	Definir resultado Como Caracter
	msj <- Minusculas(mensaje) 
	resultado <- "" 
	Para  i <- 0 Hasta Longitud(mensaje) Hacer
		resultado <-  
	FinPara
FinFuncion
FinPara
Funcion cadenaDesCifrada <- descifrar(mensaje,n)


Algoritmo examenej1
	// Declarar 
	Definir frase Como Cadena
	Definir letra Como Caracter 
	Definir n Como Entero
	Escribir "Introduce una frase: "
	Leer frase 
	Repetir
		Escribir "Introduce el numero de caracteres que debe avanzar las letras: "
		Leer n 
	Hasta Que n >= 1 O n <> 25 
FinAlgoritmo
