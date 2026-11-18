
Funcion cadenaCifrada <- cifrar(mensaje, n)
	Definir cadenaCifrada, car Como Caracter
	Definir i, posicion como Entero
	cadenaCifrada <- ""
	Para i<- 0 hasta Longitud(mensaje)-1 Hacer
		car <- Subcadena(mensaje, i, i)
		posicion <- buscarCaracterAlfabeto(car)
		Si posicion < 0 Entonces
			cadenaCifrada <- Concatenar(cadenaCifrada, car)
		SiNo
			cadenaCifrada <- Concatenar(cadenaCifrada, caracterAlfabeto(posicion+n))
		FinSi
	FinPara
FinFuncion


Funcion cadenaDescifrada <- descifrar(mensaje, n)
	Definir cadenaDescifrada Como Caracter
	cadenaDescifrada <- cifrar(mensaje, 26-n)
FinFuncion

Funcion car <- caracterAlfabeto(posicion)
	Definir alfabeto, car como Caracter
	alfabeto <- "abcdefghijklmnopqrstuvwxyz"
	car <- Subcadena(alfabeto, posicion % Longitud(alfabeto), posicion% Longitud(alfabeto))
FinFuncion

Funcion posicion <- buscarCaracterAlfabeto(car)
	Definir posicion, i como Entero
	Definir alfabeto, c como Caracter
	
	posicion <- -1
	
	Para i <- 0 hasta 25 Hacer
		c <- caracterAlfabeto(i)
		Si car = c Entonces
			posicion <- i
		FinSi
	FinPara
	
FinFuncion

Algoritmo Cesar
	Definir mensaje como Caracter
	Definir n, opcion como Entero
	
	//Línea de depuración para probar la función
	//Escribir "Posicion de z: ", buscarCaracterAlfabeto("z")
	
	Escribir "Bienvenido al programa Cifrado Cesar"
	Repetir
		Escribir "Introduzca el mensaje a cifrar/descifrar"
		Leer mensaje
		Repetir
			Escribir "Introduzca el valor de la clave [1-25]"
			Leer n
		Hasta Que n>=1 Y n<=25		
		Escribir "Introduzca la opción deseada (1-cifrar, 2-descifrar, 3-salir"
		Leer opcion
		Segun opcion Hacer
			1: Escribir "El mensaje cifrado es: ", cifrar(mensaje, n)
			2: Escribir "El mensaje descifrado es: ", descifrar(mensaje, n)
		FinSegun
	Hasta Que opcion=3

	
	
	
	
FinAlgoritmo
