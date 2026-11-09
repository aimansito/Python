# Ejercicio 16: sueldo semanal de N trabajadores según horas trabajadas

# Pedimos el número de trabajadores
n = int(input("¿Cuántos trabajadores hay? "))
# Pedimos el precio por hora
precio_hora = float(input("¿Cuánto se paga por hora? "))
# Acumulador de lo que paga la empresa en total
total_empresa = 0
# Recorremos cada trabajador
for i in range(1, n + 1):
    # Pedimos las horas que ha trabajado en la semana
    horas = float(input(f"Horas semanales del trabajador {i}: "))
    # Calculamos su sueldo
    sueldo = horas * precio_hora
    # Mostramos su sueldo
    print(f"Sueldo del trabajador {i}: {sueldo:.2f} €")
    # Lo sumamos al total de la empresa
    total_empresa = total_empresa + sueldo
# Mostramos el total que paga la empresa
print(f"La empresa paga en total: {total_empresa:.2f} €")
