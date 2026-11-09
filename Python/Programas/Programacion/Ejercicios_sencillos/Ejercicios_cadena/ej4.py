# Ejercicio 4: contar cuántas palabras tiene una frase

# Pedimos una frase por teclado
frase = input("Introduce una frase: ")

# split() separa la frase por los espacios y devuelve una lista de palabras
palabras = frase.split()
# len() nos dice cuántos elementos (palabras) tiene la lista
print("La frase tiene",len(palabras), "palabras")
