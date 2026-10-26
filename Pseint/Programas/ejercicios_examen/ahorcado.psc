Funcion encontrada <- Contiene(texto, letra)
	Definir encontrada Como Logico
	Definir i Como Entero
	
	// Suponemos que no está hasta que la encontremos
	encontrada <- Falso
	
	// Solo recorremos el texto si no está vacío
	// (al principio de la partida, "usadas" está vacía)
	Si Longitud(texto) > 0 Entonces
		Para i <- 0 Hasta Longitud(texto) - 1 Hacer
			// Si la casilla i es la letra buscada, la hemos encontrado
			Si SubCadena(texto, i, i) = letra Entonces
				encontrada <- Verdadero
			FinSi
		FinPara
	FinSi
FinFuncion
Funcion resultado <- PalabraOculta(secreta,usadas)
	//Recibe la palabra secretea y las letras que ya se han dicho
	//Devuelve la palabra con las letras acertadas a la vista
	// y un asterisco en las que faltan. Ej "C*S"
	Definir resultado, letra Como Cadena
	Definir i Como Entero
	resultado <- ""
	//Recorremos la palabra secreta letra a letra
	Para i<-0 Hasta Longitud(secreta) - 1 Hacer
		letra <- Subcadena(secreta,i,i)
		//Si esa letra ya se ha dicho, se muestra; si no, asterisco
		Si Contiene(usadas, letra) Entonces
			resultado <- Concatenar(resultado,letra)
		SiNo
			resultado <- Concatenar(resultado,"*")
		FinSi
	FinPara
FinFuncion
SubProceso DibujarAhorcado(fallos)
	
	// Recibe el número de fallos y dibuja el ahorcado. Cada fallo
	// añade una parte del cuerpo. No devuelve nada, solo dibuja.
	Definir cabeza, cuerpo, piernas Como Cadena
	
	// Al principio no hay ninguna parte del cuerpo
	cabeza <- ""
	cuerpo <- ""
	piernas <- ""
	
	// Fallo 1: cabeza
	Si fallos >= 1 Entonces
		cabeza <- "O"
	FinSi
	// Fallo 2: tronco / Fallo 3: brazo izquierdo / Fallo 4: los dos brazos
	Si fallos = 2 Entonces
		cuerpo <- " |"
	FinSi
	Si fallos = 3 Entonces
		cuerpo <- "/|"
	FinSi
	Si fallos >= 4 Entonces
		cuerpo <- "/|\"
	FinSi
	// Fallo 5: pierna izquierda / Fallo 6: las dos piernas
	Si fallos = 5 Entonces
		piernas <- "/"
	FinSi
	Si fallos >= 6 Entonces
		piernas <- "/ \"
	FinSi
	
	// Dibujamos la horca con las partes que tocan
	Escribir "  +---+"
	Escribir "  |   |"
	Escribir "  |   ", cabeza
	Escribir "  |  ", cuerpo
	Escribir "  |  ", piernas
	Escribir "  |"
	Escribir "======"
FinSubProceso

Algoritmo ahorcado
	Definir secreta, letra, usadas, oculta Como Cadena
	Definir fallos, intentos Como Entero
	
	// --- 1. El jugador 1 introduce la palabra secreta ---
	Repetir
		Escribir "Jugador 1, introduce la palabra secreta: "
		Leer secreta
	Hasta Que Longitud(secreta) > 0
	// La pasamos a mayúsculas para que "a" y "A" cuenten igual
	secreta <- Mayusculas(secreta)
	// Borramos la pantalla para que el jugador 2 no la vea
	Borrar Pantalla
	
	// --- 2. Preparamos la partida ---
	usadas <- ""     // letras dichas hasta ahora
	fallos <- 0      // letras que no estaban en la palabra
	intentos <- 0    // total de letras introducidas
	// Al principio la palabra oculta es todo asteriscos
	oculta <- PalabraOculta(secreta, usadas)
	
	// --- 3. Bucle del juego ---
	// Se sigue jugando mientras no haya 6 fallos
	// y queden asteriscos (letras por adivinar)
	Mientras fallos < 6 Y Contiene(oculta, "*") Hacer
		Escribir ""
		Escribir "Palabra: ", oculta
		Escribir "Letras usadas: ", usadas
		Escribir "Fallos: ", fallos, " de 6"
		
		// Pedimos una letra válida: un solo carácter y no repetida
		Repetir
			Escribir "Jugador 2, introduce una letra: "
			Leer letra
			letra <- Mayusculas(letra)
			Si Longitud(letra) <> 1 Entonces
				Escribir "Debes introducir una sola letra"
			SiNo
				Si Contiene(usadas, letra) Entonces
					Escribir "Ya has dicho esa letra, prueba otra"
				FinSi
			FinSi
		Hasta Que Longitud(letra) = 1 Y No Contiene(usadas, letra)
		
		// Contamos el intento y guardamos la letra como usada
		intentos <- intentos + 1
		usadas <- Concatenar(usadas, letra)
		
		// Comprobamos si la letra está en la palabra secreta
		Si Contiene(secreta, letra) Entonces
			Escribir "¡Bien! La letra ", letra, " está en la palabra"
		SiNo
			Escribir "La letra ", letra, " no está en la palabra"
			fallos <- fallos + 1
		FinSi
		
		// Dibujamos el ahorcado y actualizamos la palabra oculta
		DibujarAhorcado(fallos)
		oculta <- PalabraOculta(secreta, usadas)
	FinMientras
	
	// --- 4. Fin de la partida ---
	Escribir ""
	Si Contiene(oculta, "*") Entonces
		// Quedan asteriscos: ha salido del bucle por los 6 fallos
		Escribir "¡Has perdido! La palabra era ", secreta
	SiNo
		// No quedan asteriscos: ha adivinado todas las letras
		Escribir "¡Has ganado! La palabra era ", secreta
		Escribir "Lo has conseguido en ", intentos, " intentos"
	FinSi
FinAlgoritmo
