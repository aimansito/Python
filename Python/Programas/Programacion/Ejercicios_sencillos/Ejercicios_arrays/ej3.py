# Ejercicio 3: 5 notas de un alumno con la media, la más alta y la más baja

# Vector donde guardaremos las notas
notas = []
# Pedimos 5 notas
for i in range(5):
    # Leemos la nota como número decimal
    nota = float(input(f"Introduce la nota {i + 1} (0-10): "))
    # Mientras la nota no esté entre 0 y 10, la volvemos a pedir
    while nota < 0 or nota > 10:
        # Pedimos de nuevo la nota
        nota = float(input("Nota no válida. Introduce una nota entre 0 y 10: "))
    # Guardamos la nota en el vector
    notas.append(nota)

# Mostramos todas las notas
print("Notas:", notas)
# Calculamos la media: suma de las notas entre la cantidad de notas
media = sum(notas) / len(notas)
# Mostramos la media con 2 decimales
print(f"Nota media: {media:.2f}")
# max() devuelve el valor más alto del vector
print("Nota más alta:", max(notas))
# min() devuelve el valor más bajo del vector
print("Nota más baja:", min(notas))
