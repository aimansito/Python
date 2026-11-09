# Ejercicio 12: ahorro mensual y anual

# Lista con los nombres de los meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# Acumulador del dinero ahorrado
ahorro = 0
# Recorremos cada mes del año
for mes in meses:
    # Pedimos la cantidad depositada ese mes
    deposito = float(input(f"¿Cuánto depositas en {mes}? "))
    # La sumamos al ahorro acumulado
    ahorro = ahorro + deposito
    # Mostramos cuánto lleva ahorrado hasta ese mes
    print(f"Ahorro acumulado hasta {mes}: {ahorro:.2f} €")
# Mostramos el total ahorrado en el año
print(f"Total ahorrado en el año: {ahorro:.2f} €")
