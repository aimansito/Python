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
// FUNCIÓN FechaValida
// Recibe un día, un mes y un año, y devuelve Verdadero si
// forman una fecha correcta y Falso si no
// ============================================================
Funcion valida <- FechaValida(dia, mes, anio)
	Definir valida Como Logico
	
	// Suponemos que es válida y vamos comprobando cada parte
	valida <- Verdadero
	
	// El año tiene que ser positivo
	Si anio <= 0 Entonces
		valida <- Falso
	FinSi
	
	// El mes tiene que estar entre 1 y 12
	Si mes < 1 O mes > 12 Entonces
		valida <- Falso
	SiNo
		// Solo si el mes es correcto tiene sentido mirar el día:
		// tiene que estar entre 1 y los días que tiene ese mes
		Si dia < 1 O dia > DiasDelMes(mes, anio) Entonces
			valida <- Falso
		FinSi
	FinSi
FinFuncion


// ============================================================
// SUBPROCESO LeerFecha
// Lee por teclado una fecha y no termina hasta que es válida.
// Devuelve tres valores, así que usa Por Referencia
// ============================================================
SubProceso LeerFecha(dia Por Referencia, mes Por Referencia, anio Por Referencia)
	Repetir
		Escribir "Día: "
		Leer dia
		Escribir "Mes: "
		Leer mes
		Escribir "Año: "
		Leer anio
		
		// Si la fecha no es válida, avisamos y se vuelve a pedir
		Si No FechaValida(dia, mes, anio) Entonces
			Escribir "Fecha no válida, inténtalo de nuevo"
		FinSi
	Hasta Que FechaValida(dia, mes, anio)
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
// Lee una fecha válida y muestra su día juliano
// ============================================================
Algoritmo dia_juliano
	Definir d, m, a Como Entero
	
	Escribir "Introduce una fecha:"
	// Tras la llamada, d, m y a tienen una fecha ya validada
	LeerFecha(d, m, a)
	
	Escribir "El ", d, "/", m, "/", a, " es el día ", Calcular_Dia_Juliano(d, m, a), " del año"
FinAlgoritmo