# Ejercicio 7: subrutina Login con un máximo de 3 intentos


# Función que comprueba usuario y contraseña y actualiza el número de intentos.
# En Python los enteros no se pueden modificar "por referencia", así que
# devolvemos el número de intentos actualizado junto con el resultado.
def login(usuario, contrasena, intentos):
    # Si el usuario y la contraseña son los correctos
    if usuario == "usuario1" and contrasena == "asdasd":
        # Devolvemos True y los intentos sin cambiar
        return True, intentos
    # Si no son correctos, incrementamos los intentos
    intentos = intentos + 1
    # Devolvemos False y los intentos incrementados
    return False, intentos


# Número de intentos fallidos realizados
intentos = 0
# Indica si se ha conseguido entrar
correcto = False
# Repetimos mientras no se haya entrado y se hayan hecho menos de 3 intentos
while not correcto and intentos < 3:
    # Pedimos el nombre de usuario
    usuario = input("Usuario: ")
    # Pedimos la contraseña
    contrasena = input("Contraseña: ")
    # Llamamos a login y recogemos el resultado y los intentos actualizados
    correcto, intentos = login(usuario, contrasena, intentos)
    # Si no ha sido correcto
    if not correcto:
        # Avisamos y mostramos los intentos que quedan
        print(f"Datos incorrectos. Te quedan {3 - intentos} intentos")

# Si se consiguió entrar
if correcto:
    # Damos la bienvenida
    print("¡Login correcto! Bienvenido")
# Si se agotaron los intentos
else:
    # Avisamos de que se ha bloqueado el acceso
    print("Has agotado los 3 intentos. Acceso denegado")
