# Ejercicio 3: calcular el cambio con el menor número de monedas y billetes

# Valores de billetes y monedas de euro en CÉNTIMOS (de mayor a menor)
# Usamos céntimos (enteros) para evitar errores de redondeo con decimales
VALORES = [50000, 20000, 10000, 5000, 2000, 1000, 500,
           200, 100, 50, 20, 10, 5, 2, 1]

# Pedimos el total a pagar
total = float(input("Cantidad total a pagar (€): "))
# Pedimos lo que se ha entregado
entregado = float(input("Cantidad entregada (€): "))

# Si se ha entregado menos de lo que hay que pagar
if entregado < total:
    # Indicamos cuánto falta
    print(f"Falta dinero: {total - entregado:.2f} €")
# Si se ha entregado suficiente
else:
    # Calculamos el cambio en céntimos redondeando para quitar errores de decimales
    cambio = round((entregado - total) * 100)
    # Mostramos el cambio total
    print(f"Cambio: {cambio / 100:.2f} €")
    # Recorremos cada billete/moneda de mayor a menor
    for valor in VALORES:
        # Cuántas unidades de este valor caben en el cambio que queda
        cantidad = cambio // valor
        # Si cabe al menos una
        if cantidad > 0:
            # Decidimos si es billete (5 € o más) o moneda
            tipo = "billete(s)" if valor >= 500 else "moneda(s)"
            # Mostramos la cantidad y el valor en euros
            print(f"  {cantidad} {tipo} de {valor / 100:g} €")
            # Restamos lo ya entregado del cambio pendiente
            cambio = cambio % valor
