# Ejercicio 15: pago que se duplica cada mes durante 20 meses

# Lo que se paga el primer mes
pago = 10
# Acumulador del total pagado
total = 0
# Recorremos los 20 meses
for mes in range(1, 21):
    # Mostramos el pago de ese mes
    print(f"Mes {mes}: {pago} €")
    # Lo sumamos al total
    total = total + pago
    # El mes siguiente se paga el doble
    pago = pago * 2
# Mostramos el total pagado tras los 20 meses
print(f"Total pagado: {total} €")
