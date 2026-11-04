def escribir_centrado(texto):
    espacios = 40 - len(texto) // 2

    margen = ""
    while len(margen) < espacios: 
        margen = margen + " "

    subrayado = ""
    while len(subrayado) < len(texto):
        subrayado = subrayado + ""

    print(margen + texto)
    print(subrayado + texto)