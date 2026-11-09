# Ejercicio 10: juego del ahorcado

# Dibujos del ahorcado según el número de fallos (posición 0 = 0 fallos ... 6 = completo)
DIBUJOS = [
    "  +---+\n  |   |\n      |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n      |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n=========",
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n=========",
]
# Número máximo de fallos permitidos
MAX_FALLOS = 6

# El primer jugador escribe la palabra secreta (en minúsculas)
secreta = input("Jugador 1, escribe la palabra secreta: ").lower()
# Imprimimos muchas líneas en blanco para que el jugador 2 no la vea
print("\n" * 50)

# Lista con las letras que ya se han introducido
usadas = []
# Contador de fallos
fallos = 0
# Contador de intentos (letras introducidas)
intentos = 0
# Indica si se ha ganado
ganado = False

# Repetimos mientras no se haya ganado ni se hayan alcanzado los 6 fallos
while not ganado and fallos < MAX_FALLOS:
    # Construimos la palabra oculta: letra si ya se ha acertado, * si no
    oculta = ""
    # Recorremos cada letra de la palabra secreta
    for letra in secreta:
        # Si la letra ya se ha dicho
        if letra in usadas:
            # La mostramos
            oculta = oculta + letra
        # Si no
        else:
            # Mostramos un asterisco
            oculta = oculta + "*"
    # Mostramos el dibujo según los fallos
    print(DIBUJOS[fallos])
    # Mostramos la palabra oculta
    print("Palabra:", oculta)
    # Mostramos las letras introducidas anteriormente
    print("Letras usadas:", " ".join(usadas))

    # Pedimos una letra
    letra = input("Introduce una letra: ").lower()
    # Validamos que sea una única letra
    if len(letra) != 1 or not letra.isalpha():
        # Avisamos del error
        print("Debes introducir UNA letra")
        # Volvemos al principio del bucle
        continue
    # Si la letra ya se había dicho
    if letra in usadas:
        # Avisamos
        print("Esa letra ya la has dicho")
        # Volvemos al principio del bucle
        continue

    # Guardamos la letra como usada
    usadas.append(letra)
    # Contamos un intento
    intentos = intentos + 1
    # Si la letra está en la palabra
    if letra in secreta:
        # Indicamos el acierto
        print("¡Bien! La letra está en la palabra")
    # Si no está
    else:
        # Sumamos un fallo
        fallos = fallos + 1
        # Indicamos el fallo
        print(f"La letra no está. Fallos: {fallos}/{MAX_FALLOS}")

    # Suponemos que se ha ganado
    ganado = True
    # Recorremos las letras de la palabra secreta
    for l in secreta:
        # Si alguna letra no se ha dicho todavía
        if l not in usadas:
            # Aún no se ha ganado
            ganado = False

# Si se ha ganado
if ganado:
    # Mostramos la palabra y los intentos
    print(f"\n¡HAS GANADO! La palabra era '{secreta}'. Intentos: {intentos}")
# Si se ha perdido
else:
    # Mostramos el ahorcado completo
    print(DIBUJOS[MAX_FALLOS])
    # Mostramos la palabra secreta
    print(f"HAS PERDIDO. La palabra era '{secreta}'")
