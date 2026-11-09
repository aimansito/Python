# Ejercicio 15: quiniela de fútbol con 15 partidos

# Número de partidos de la quiniela
PARTIDOS = 15
# Tabla de equipos: cada fila es un partido con 2 columnas [local, visitante]
equipos = []
# Tabla de resultados: cada fila es un partido con 2 columnas [goles_local, goles_visitante]
resultados = []

# Recorremos los 15 partidos
for p in range(PARTIDOS):
    # Indicamos qué partido se está introduciendo
    print(f"\nPartido {p + 1}")
    # Pedimos el equipo local
    local = input("  Equipo local: ")
    # Pedimos el equipo visitante
    visitante = input("  Equipo visitante: ")
    # Pedimos los goles del local
    goles_local = int(input(f"  Goles de {local}: "))
    # Pedimos los goles del visitante
    goles_visitante = int(input(f"  Goles de {visitante}: "))
    # Guardamos la fila de equipos
    equipos.append([local, visitante])
    # Guardamos la fila de resultados
    resultados.append([goles_local, goles_visitante])

# Título de la quiniela
print("\n========== QUINIELA DE LA JORNADA ==========")
# Recorremos los partidos
for p in range(PARTIDOS):
    # Si gana el local, el signo es 1
    if resultados[p][0] > resultados[p][1]:
        # Signo 1
        signo = "1"
    # Si gana el visitante, el signo es 2
    elif resultados[p][0] < resultados[p][1]:
        # Signo 2
        signo = "2"
    # Si empatan, el signo es X
    else:
        # Signo X
        signo = "X"
    # Mostramos el partido, el resultado y el signo
    print(f"{p + 1:2}. {equipos[p][0]:>15} {resultados[p][0]} - "
          f"{resultados[p][1]} {equipos[p][1]:<15}  [{signo}]")

# Respuesta a la pregunta del enunciado:
# Para guardar TODAS las jornadas de la temporada habría que añadir una
# dimensión más a las tablas: equipos[jornada][partido][2] y
# resultados[jornada][partido][2]. Es decir, una lista de jornadas donde
# cada jornada contiene la tabla de 15 partidos que usamos aquí.
