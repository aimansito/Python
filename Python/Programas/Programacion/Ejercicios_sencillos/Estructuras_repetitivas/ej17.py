# Ejercicio 17: sueldo semanal de N trabajadores según días y horas de cada día

# Pedimos el número de trabajadores
n = int(input("¿Cuántos trabajadores hay? "))
# Pedimos el precio por hora
precio_hora = float(input("¿Cuánto se paga por hora? "))
# Acumulador de lo que paga la empresa en total
total_empresa = 0
# Recorremos cada trabajador
for i in range(1, n + 1):
    # Pedimos cuántos días ha trabajado
    dias = int(input(f"¿Cuántos días trabajó el trabajador {i}? "))
    # Acumulador de horas de este trabajador
    horas_totales = 0
    # Recorremos cada día trabajado
    for d in range(1, dias + 1):
        # Pedimos las horas de ese día
        horas = float(input(f"  Horas del día {d}: "))
        # Las sumamos a sus horas totales
        horas_totales = horas_totales + horas
    # Calculamos su sueldo
    sueldo = horas_totales * precio_hora
    # Mostramos su sueldo
    print(f"Sueldo del trabajador {i}: {sueldo:.2f} €")
    # Lo sumamos al total de la empresa
    total_empresa = total_empresa + sueldo
# Mostramos el total que paga la empresa
print(f"La empresa paga en total: {total_empresa:.2f} €")
