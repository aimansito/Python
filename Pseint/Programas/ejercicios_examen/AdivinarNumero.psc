// Programa: el ordenador adivina un número pensado por el usuario
// Estrategia: búsqueda binaria (siempre propone el punto medio del intervalo)

Algoritmo AdivinarNumero
	
	// ---------- DECLARACIÓN DE VARIABLES ----------
	Definir inferior, superior Como Entero   // Límites del intervalo donde está el número
	Definir propuesta Como Entero            // Número que el ordenador propone en cada intento
	Definir intentos Como Entero             // Contador de intentos realizados
	Definir respuesta Como Caracter          // Respuesta del usuario: S, A o B
	Definir acertado Como Logico             // Indica si el ordenador ya ha acertado
	Definir trampa Como Logico               // Indica si las respuestas son contradictorias
	
	// ---------- LECTURA DE LOS LÍMITES ----------
	// Pedimos el límite inferior hasta que sea un entero positivo
	Repetir
		Escribir "Introduce el límite inferior (entero positivo):"
		Leer inferior
		// Si no es positivo, avisamos y se vuelve a pedir
		Si inferior <= 0 Entonces
			Escribir "El límite inferior debe ser mayor que 0."
		FinSi
	Hasta Que inferior > 0
	
	// Pedimos el límite superior hasta que sea mayor que el inferior
	Repetir
		Escribir "Introduce el límite superior:"
		Leer superior
		// Si no es mayor que el inferior, avisamos y se vuelve a pedir
		Si superior <= inferior Entonces
			Escribir "El límite superior debe ser mayor que ", inferior, "."
		FinSi
	Hasta Que superior > inferior
	
	// Instrucciones para el usuario
	Escribir "Piensa un número entre ", inferior, " y ", superior, "."
	Escribir "Responde: S (correcto), A (mi número es más alto), B (mi número es más bajo)."
	
	// ---------- INICIALIZACIÓN ----------
	intentos <- 0        // Todavía no se ha hecho ningún intento
	acertado <- Falso    // Todavía no se ha acertado
	trampa <- Falso      // Todavía no hay contradicciones
	
	// ---------- BUCLE PRINCIPAL ----------
	// Se repite hasta acertar o hasta detectar respuestas imposibles
	Repetir
		
		// El ordenador propone el número central del intervalo
		propuesta <- Trunc((inferior + superior) / 2)
		
		// Contamos este intento
		intentos <- intentos + 1
		
		// Mostramos la propuesta y pedimos una respuesta válida
		Repetir
			Escribir "¿Es el ", propuesta, "? (S/A/B)"
			Leer respuesta
			// Pasamos a mayúsculas para aceptar también s, a, b
			respuesta <- Mayusculas(respuesta)
			// Si no es una respuesta válida, avisamos
			Si respuesta <> "S" Y respuesta <> "A" Y respuesta <> "B" Entonces
				Escribir "Respuesta no válida. Escribe S, A o B."
			FinSi
		Hasta Que respuesta = "S" O respuesta = "A" O respuesta = "B"
		
		// Actuamos según la respuesta
		Segun respuesta Hacer
			"S":
				// El ordenador ha acertado
				acertado <- Verdadero
			"A":
				// La propuesta es más alta que el número buscado:
				// el número está por debajo, así que bajamos el límite superior
				superior <- propuesta - 1
			"B":
				// La propuesta es más baja que el número buscado:
				// el número está por encima, así que subimos el límite inferior
				inferior <- propuesta + 1
		FinSegun
		
		// Si los límites se cruzan, no queda ningún número posible:
		// el usuario se ha equivocado o ha hecho trampa
		Si No acertado Y inferior > superior Entonces
			trampa <- Verdadero
		FinSi
		
	Hasta Que acertado O trampa
	
	// ---------- RESULTADO ----------
	Si acertado Entonces
		// Mostramos el número acertado y los intentos usados
		Escribir "¡He acertado! Tu número es el ", propuesta, "."
		Escribir "Lo he adivinado en ", intentos, " intentos."
	SiNo
		// Las respuestas fueron contradictorias
		Escribir "Tus respuestas son contradictorias, ningún número las cumple. ¿Has hecho trampa?"
	FinSi
	
FinAlgoritmo