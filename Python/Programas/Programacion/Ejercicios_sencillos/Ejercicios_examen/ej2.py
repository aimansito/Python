# Ejercicio 2: calcular la letra del DNI y validar un DNI completo

# Tabla oficial de letras: la posición es el resto de dividir el número entre 23
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"


# Recibe el número del DNI y devuelve la letra que le corresponde
def calcular_letra(numero):
    # La letra es la que está en la posición numero % 23
    return LETRAS[numero % 23]


# Recibe un DNI (8 números + letra) y devuelve True si es válido
def validar_dni(dni):
    # Comprobamos que tenga exactamente 9 caracteres
    if len(dni) != 9:
        # Si no, no es válido
        return False
    # Separamos los 8 primeros caracteres (el número)
    numero = dni[:8]
    # El último carácter es la letra (la pasamos a mayúscula)
    letra = dni[8].upper()
    # Los 8 primeros caracteres tienen que ser dígitos
    if not numero.isdigit():
        # Si no, no es válido
        return False
    # Es válido si la letra coincide con la calculada
    return letra == calcular_letra(int(numero))


# Pedimos el DNI y quitamos espacios sobrantes
dni = input("Introduce un DNI (8 números y letra): ").strip()
# Si no tiene 9 caracteres, lo indicamos específicamente
if len(dni) != 9:
    # Mensaje de error de longitud
    print("Error: el DNI debe tener 9 caracteres")
# Si tiene 9 caracteres y es válido
elif validar_dni(dni):
    # Indicamos que es correcto
    print("El DNI es correcto")
# Si tiene 9 caracteres pero no es válido
else:
    # Indicamos que es incorrecto
    print("El DNI NO es correcto")
