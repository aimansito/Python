# Ejercicio 18: cronómetro con horas, minutos y segundos

# Importamos time para poder esperar un segundo
import time

# Empezamos en 0 horas
horas = 0
# Empezamos en 0 minutos
minutos = 0
# Empezamos en 0 segundos
segundos = 0
# Avisamos de cómo detenerlo
print("Cronómetro en marcha (pulsa Ctrl+C para parar)")
# Ejecutamos el cronómetro capturando Ctrl+C para terminar limpiamente
try:
    # Bucle infinito: el cronómetro no para hasta que el usuario lo detenga
    while True:
        # Mostramos el tiempo como HH:MM:SS (\r vuelve al principio de la línea)
        print(f"\r{horas:02d}:{minutos:02d}:{segundos:02d}", end="")
        # Esperamos un segundo
        time.sleep(1)
        # Sumamos un segundo
        segundos = segundos + 1
        # Si llegamos a 60 segundos
        if segundos == 60:
            # Reiniciamos los segundos
            segundos = 0
            # Y sumamos un minuto
            minutos = minutos + 1
        # Si llegamos a 60 minutos
        if minutos == 60:
            # Reiniciamos los minutos
            minutos = 0
            # Y sumamos una hora
            horas = horas + 1
# Si el usuario pulsa Ctrl+C
except KeyboardInterrupt:
    # Mostramos el tiempo final
    print(f"\nCronómetro detenido en {horas:02d}:{minutos:02d}:{segundos:02d}")
