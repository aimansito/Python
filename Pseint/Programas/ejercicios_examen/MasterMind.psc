//GenerarSecreto
//Rellena el arreglo "secreto" con 4 cifras al azar sin Repetir
//No devuelve nada: los arreglos se pasan por referencia asi que
//los cambios hechos aqui se ven en el programa principal
Funcion GenerarSecreto(secreto Por Referencia)
	Definir i, j Como Entero
	Definir repetido Como Logico
	
	Para i <- 1 Hasta 4 Hacer
		//Generamos una cifra y la repetimos mientras ya exista
		Repetir
			//La primera cifra va de 1 a 9 para que no empiece por 0
			Si i = 1 Entonces
				secreto[i] <- Azar(9)+1
			SiNo
				//El resto de cifras van de 0 a 9
				secreto[i] <- Azar(10)
			FinSi
			//Comprobamos si la cifra ya estaba en alguna posición anterior
			repetido <- Falso
			Para j <- 1 Hasta i - 1 Hacer
				Si secreto[j] = secreto[i] Entonces
					repetido <- Verdadero
				FinSi
			FinPara
		Hasta Que no repetido 
	FinPara
FinFuncion

//Recibe la propuesta como texto y devuelve verdadero si tiene
//exactamente 4 digitos sin repetir o falso en caso contrario
Funcion valida <- EsPropuestaValida(propuesta)
	Definir valida Como Logico
	Definir i,j Como Entero
	//Primera condición: exactamente 4 caracteres
	valida <- Longitud(propuesta) = 4
	//Solo revisamos los caracteres si la longitud es correcta
	Si valida Entonces
		Para i <- 1 Hasta 4 Hacer
			//Cada caracter tiene que ser un digito del "0" al "9"
			Si SubCadena(propuesta,i,i) < "0" O SubCadena(propuesta,i,i) > "9" Entonces
				valida <- Falso
			FinSi
			//Comparamos con los caracteres siguientes para detectar repetidos
			Para j <- i + 1 Hasta 4 Hacer
				Si Subcadena(propuesta,i,i) = Subcadena(propuesta,j,j) Entonces
					valida <- Falso
				FinSi
			FinPara
		FinPara
	FinSi
FinFuncion

//Pide al jugador un numero hasta que sea valido y lo devuelve
//Usa la funcion EsPropuestaVlida para comprobarlo
Funcion propuesta <- PedirPropuesta
	Definir propuesta Como Caracter
	
	Repetir
		Escribir "Introduce un número de 4 cifras sin repetir: "
		Leer propuesta 
		//Si no es válido, avisamos y se vuelve a PedirPropuesta
		Si No EsPropuestaValida(propuesta)Entonces
			Escribir "Propuesta no válida"
		FinSi
	Hasta Que  EsPropuestaValida(propuesta)
FinFuncion

//Devuelve cuantas cifras de la propuesta coinciden con el secreto en la misma posición

Funcion muertos <- ContarMuertos(secreto, propuesta)
	Definir muertos, i Como Entero
	muertos <- 0
	//Comparamos cada posicion de la propuesta con la misma del secreto
	Para i <- 1 Hasta 4 Hacer
		Si ConvertirANumero(SubCadena(propuesta, i ,i)) = secreto[i] Entonces
			muertos <- muertos + 1
		FinSi
	FinPara
FinFuncion

//Devuelve cuantas cifras de la propuesta están en el secreto pero en una posición distinta
Funcion heridos <- ContarHeridos(secreto,propuesta)
	Definir heridos, i, j Como Entero
	heridos <- 0 
	//Recorremos cada cifra de la propuesta(posicion i)
	Para i <- 1 Hasta 4 Hacer
		//La comparamos con cada cifra del secreto(posicion j)
		Para j <- 1 Hasta 4 Hacer
			//Cuenta solo si coincide la cifra pero NO la posicion
			Si i <> j Y ConvertirANumero(SubCadena(propuesta, i,i)) = secreto[j] Entonces
				heridos <- heridos + 1
			FinSi
		FinPara
	FinPara
FinFuncion


Algoritmo MasterMind
	// Arreglo con las 4 cifras del número secreto
	Dimension secreto[4]
	Definir secreto, muertos, heridos, intentos Como Entero
	Definir propuesta Como Caracter
	
	// El programa elige el número secreto
	GenerarSecreto(secreto)
	Escribir "He pensado un número de 4 cifras sin cifras repetidas. ¡Adivínalo!"
	
	intentos <- 0
	
	// Se repite hasta que el jugador acierte
	Repetir
		// Pedimos una propuesta válida y contamos el intento
		propuesta <- PedirPropuesta
		intentos <- intentos + 1
		
		// Calculamos las pistas
		muertos <- ContarMuertos(secreto, propuesta)
		heridos <- ContarHeridos(secreto, propuesta)
		
		Escribir muertos, " MUERTOS y ", heridos, " HERIDOS"
		
		// Con 4 muertos se han acertado todas las cifras en su sitio
	Hasta Que muertos = 4
	
	Escribir "¡Enhorabuena! Has adivinado el ", propuesta, " en ", intentos, " intentos."
FinAlgoritmo
