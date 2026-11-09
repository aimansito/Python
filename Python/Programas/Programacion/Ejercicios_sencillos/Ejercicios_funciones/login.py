#Funcion qe comprueba usuario y contraseña y actualiza el numero de intentos
#Devolvemos el numero de intentos actualizado junto cn el resultado

def login(usuario, contrasena, intentos):
    #Si las credenciales son correctos
    if usuario == "usuario1" and contrasena == "1245":
        return True, intentos
    intentos = intentos + 1
    return False, intentos

#numero de intentos fallidos realizados
intentos = 0
#indica si se ha conseguido entrar
correcto = False

while not correcto and intentos < 3:
    #pedimos las credenciales
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    correcto, intentos = login(usuario, contrasena, intentos)
    if not correcto: 
        print(f"Datos incorrectos Te queda {3 - intentos} intentos")
    
if correcto:
    print("Login permitido")
else:
    print("Acceso denegado, número de intentos alcanzado")