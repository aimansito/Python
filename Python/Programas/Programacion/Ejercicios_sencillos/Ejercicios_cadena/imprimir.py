#Escribe un programa que muestre por pantalla 10 palabras en inglés junto a su correspondiente traducciónal castellano las palabras debe estar distribuidas y alineadas a la izquierda 


palabras = [("Computer","Ordenador")("Student","Alumno")("Cat","Gato")("Penguin","Pinguino")("Machine","Maquina")("Nature","Naturaleza")("Light","Luz")("Green","Verde")("Book","Libro")("Pyramid","Piramide")]


for ingles, castellano in palabras:
    print(f"{ingles:<15}{castellano:<15}")