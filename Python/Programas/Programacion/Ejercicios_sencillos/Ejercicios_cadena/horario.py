#Escribe un programa que muestre tu horario de clase cad amodlo o asignatura debe mostrarse en un color diferente

# Códigos de color ANSI
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIAN = "\033[96m"
RESET = "\033[0m"  # Restablece el color original de la consola

# Asignamos un color fijo a cada módulo
colores = {
    "Programación": VERDE,
    "Bases de Datos": AZUL,
    "Sistemas": AMARILLO,
    "Lenguajes": MAGENTA,
    "Entornos": CIAN,
    "FOL": ROJO
}

# Horario estructurado por horas y días (Lunes a Viernes)
horario = [
    ("08:30 - 09:30", ["Programación", "Bases de Datos", "Sistemas", "Programación", "Lenguajes"]),
    ("09:30 - 10:30", ["Programación", "Bases de Datos", "Sistemas", "Programación", "Lenguajes"]),
    ("10:30 - 11:30", ["Sistemas", "Entornos", "Bases de Datos", "FOL", "Bases de Datos"]),
    ("12:00 - 13:00", ["Lenguajes", "Programación", "Entornos", "Bases de Datos", "Sistemas"]),
    ("13:00 - 14:00", ["FOL", "Programación", "FOL", "Entornos", "Sistemas"])
]

# Imprimimos la cabecera
dias = ["HORA", "LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES"]
print(f"{dias[0]:<15} {dias[1]:<16} {dias[2]:<16} {dias[3]:<16} {dias[4]:<16} {dias[5]:<16}")
print("-" * 98)

# Recorremos cada franja horaria
for hora, asignaturas in horario:
    fila = f"{hora:<15} "
    for asig in asignaturas:
        color = colores.get(asig, RESET)
        # Aplicamos el ancho fijo (16) a la palabra ANTES de envolverla en los códigos de color
        fila += f"{color}{asig:<16}{RESET} "
    print(fila)