# Ejercicio 13: horas trabajadas en 6 días y sueldo

# Pedimos cuánto se paga por cada hora
precio_hora = float(input("¿Cuánto se paga por hora? "))
# Acumulador de horas totales
total_horas = 0
# Recorremos los 6 días de la semana laboral
for dia in range(1, 7):
    # Pedimos las horas trabajadas ese día
    horas = float(input(f"Horas trabajadas el día {dia}: "))
    # Las sumamos al total
    total_horas = total_horas + horas
# Calculamos el sueldo multiplicando horas por precio
sueldo = total_horas * precio_hora
# Mostramos el total de horas
print("Total de horas trabajadas:", total_horas)
# Mostramos el sueldo con dos decimales
print(f"Sueldo: {sueldo:.2f} €")
