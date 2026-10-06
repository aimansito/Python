Algoritmo piedrapapeltijera
	Definir jug1,jug2 Como Caracter
	Escribir "Jugador 1 elige una opción"
	Leer jug1
	Escribir "Jugador 2 elige una opción"
	Leer jug2
	Si (jug1 <> "piedra" Y jug1 <> "papel" Y jug1 <> "tijera") O (jug2 <> "piedra" Y jug2 <> "papel" Y jug2 <> "tijera")
		Escribir "Opción incorrecta"
	SiNo
		Si jug1 = jug2 Entonces
			Escribir "Empate"
		SiNo
			Si (jug1 = "piedra" Y jug2 = "tijera") O (jug1="papel" y jug2 = "piedra") O (jug1="tijera" Y jug2="papel") Entonces
				Escribir "Gana el jugador 1"
			SiNo
				Escribir "Gana el jugador 2"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
