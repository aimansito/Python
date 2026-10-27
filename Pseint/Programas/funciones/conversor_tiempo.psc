// ============================================================
// FUNCIÓN ConvertirASegundos
// Recibe un tiempo en horas, minutos y segundos, y devuelve
// el total en segundos. Ej: 1h 2m 5s -> 3725 segundos
// ============================================================
Funcion total <- ConvertirASegundos(horas, minutos, segundos)
	Definir total Como Entero
	// Una hora tiene 3600 segundos y un minuto tiene 60
	total <- horas * 3600 + minutos * 60 + segundos
FinFuncion


// ============================================================
// SUBPROCESO ConvertirAHMS
// Recibe un tiempo en segundos y lo descompone en horas,
// minutos y segundos. Como hay que devolver TRES valores,
// se usan parámetros Por Referencia
// Ej: 3725 segundos -> 1h 2m 5s
// ============================================================
SubProceso ConvertirAHMS(total, horas Por Referencia, minutos Por Referencia, segundos Por Referencia)
	Definir resto Como Entero
	
	// Cuántas horas completas caben (Trunc quita los decimales)
	horas <- Trunc(total / 3600)
	// Los segundos que sobran después de quitar las horas
	resto <- total MOD 3600
	// Cuántos minutos completos caben en lo que sobra
	minutos <- Trunc(resto / 60)
	// Lo que sobra después de quitar los minutos son los segundos
	segundos <- resto MOD 60
FinSubProceso


// ============================================================
// PROGRAMA PRINCIPAL
// Muestra un menú hasta que el usuario elija salir
// ============================================================
Algoritmo conversor_tiempo
	Definir opcion, h, m, s, total Como Entero
	
	Repetir
		// --- Mostrar el menú ---
		Escribir ""
		Escribir "===== CONVERSOR DE TIEMPO ====="
		Escribir "1. Convertir a segundos"
		Escribir "2. Convertir a horas, minutos y segundos"
		Escribir "3. Salir"
		Escribir "Elige una opción: "
		Leer opcion
		
		// --- Ejecutar la opción elegida ---
		Segun opcion Hacer
			1:
				// Leemos el tiempo validando cada parte
				Repetir
					Escribir "Horas: "
					Leer h
				Hasta Que h >= 0
				Repetir
					Escribir "Minutos (0-59): "
					Leer m
				Hasta Que m >= 0 Y m <= 59
				Repetir
					Escribir "Segundos (0-59): "
					Leer s
				Hasta Que s >= 0 Y s <= 59
				
				Escribir h, "h ", m, "m ", s, "s son ", ConvertirASegundos(h, m, s), " segundos"
				
			2:
				Repetir
					Escribir "Segundos totales: "
					Leer total
				Hasta Que total >= 0
				
				// Tras la llamada, h, m y s tienen el resultado
				ConvertirAHMS(total, h, m, s)
				Escribir total, " segundos son ", h, "h ", m, "m ", s, "s"
				
			3:
				Escribir "¡Hasta luego!"
				
			De Otro Modo:
				Escribir "Opción no válida, elige 1, 2 o 3"
		FinSegun
		
		// El menú se repite hasta que se elija salir
	Hasta Que opcion = 3
FinAlgoritmo