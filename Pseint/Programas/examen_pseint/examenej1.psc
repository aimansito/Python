Funcion cadenaCifrada <- cifrar(mensaje,n)
	Definir cadenaCifrada Como Caracter
FinFuncion
Funcion cadenaDesCifrada <- descifrar(mensaje,n)
	Definir cadenaDesCifrada Como Caracter 
FinFuncion


Algoritmo examenej1
	Definir mensaje Como Caracter
	Definir n, op Como Entero
	Escribir "Bienvenido al programa cifrado por cesar"
	Escribir "Introduzca el mensaje a cifrar/descifrar"
	Leer mensaje
	Repetir
		Escribir "Introduzca el valor de la clave [1-25]"
		Leer n 
	Hasta Que n >= 1 Y n <= 25
	Repetir
		Escribir "Introduzca la opción deseada"
		Leer op 
		Segun op Hacer
			1: Escribir "El mensaje cfrado es: ", cifrar(mensaje, n)
			2: Escribir "El mensaje descifrado es: ", descifrar(mensaje,n)
		FinSegun
	Hasta Que op = 3 
FinAlgoritmo
