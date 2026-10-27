// ============================================================
// FUNCIÓN EsBisiesto
// Recibe un año y devuelve Verdadero si es bisiesto.
// Un año es bisiesto si es divisible entre 4, salvo los que
// son divisibles entre 100, que solo lo son si también son
// divisibles entre 400
// ============================================================
Funcion bisiesto <- EsBisiesto(anio)
	Definir bisiesto Como Logico
	Si (anio MOD 4 = 0 Y anio MOD 100 <> 0) O anio MOD 400 = 0 Entonces
		bisiesto <- Verdadero
	SiNo
		bisiesto <- Falso
	FinSi
FinFuncion


// ============================================================
// FUNCIÓN DiasDelMes
// Recibe un mes y un año, y devuelve cuántos días tiene ese
// mes. Necesita el año por febrero, que depende de si es
// bisiesto. Si el mes no es válido, devuelve 0
// ============================================================
Funcion dias <- DiasDelMes(mes, anio)
	Definir dias Como Entero
	Segun mes Hacer
		1, 3, 5, 7, 8, 10, 12:
			dias <- 31
		4, 6, 9, 11:
			dias <- 30
		2:
			// Febrero: 29 días si el año es bisiesto, 28 si no
			Si EsBisiesto(anio) Entonces
				dias <- 29
			SiNo
				dias <- 28
			FinSi
		De Otro Modo:
			dias <- 0
	FinSegun
FinFuncion


// ============================================================
// SUBPROCESO LeerFecha
// Lee por teclado una fecha válida (día, mes y año).
// Devuelve tres valores, así que usa Por Referencia
// ============================================================
SubProceso LeerFecha(dia Por Referencia, mes Por Referencia, anio Por Referencia)
	Definir valida Como Logico
	
	Repetir
		Escribir "Día: "
		Leer dia
		Escribir "Mes: "
		Leer mes
		Escribir "Año: "
		Leer anio
		
		// La fecha es válida si el año es positivo, el mes está
		// entre 1 y 12, y el día entre 1 y los días de ese mes.
		// Si el mes no es válido, DiasDelMes devuelve 0 y la
		// condición del día también falla
		valida <- anio > 0 Y mes >= 1 Y mes <= 12 Y dia >= 1 Y dia <= DiasDelMes(mes, anio)
		
		Si No valida Entonces
			Escribir "Fecha no válida, inténtalo de nuevo"
		FinSi
	Hasta Que valida
FinSubProceso


// ============================================================
// FUNCIÓN Calcular_Dia_Juliano
// Recibe una fecha y devuelve qué número de día del año es.
// Suma los días de todos los meses anteriores y le añade el
// día del mes actual
// ============================================================
Funcion juliano <- Calcular_Dia_Juliano(dia, mes, anio)
	Definir juliano, m Como Entero
	
	juliano <- 0
	m <- 1
	// Sumamos los días de los meses completos anteriores.
	// Se usa Mientras porque en enero no hay meses anteriores
	// y el bucle no debe dar ninguna vuelta
	Mientras m < mes Hacer
		juliano <- juliano + DiasDelMes(m, anio)
		m <- m + 1
	FinMientras
	
	// Añadimos los días del mes actual
	juliano <- juliano + dia
FinFuncion


// ============================================================
// PROGRAMA PRINCIPAL
// ============================================================
Algoritmo dia_juliano
	Definir d, m, a Como Entero
	
	Escribir "Introduce una fecha:"
	// Tras la llamada, d, m y a tienen la fecha leída
	LeerFecha(d, m, a)
	
	Escribir "El ", d, "/", m, "/", a, " es el día ", Calcular_Dia_Juliano(d, m, a), " del año"
FinAlgoritmo