import pandas as pd

peliculas = {
    "Titulo": ["Origen", "El Padrino", "Interstellar", "Parásitos", "Coco"],
    "Año": [2010, 1972, 2014, 2019, 2017],               # enteros  -> int64
    "Director": ["Christopher Nolan", "Francis Ford Coppola",
                 "Christopher Nolan", "Bong Joon-ho", "Lee Unkrich"],
    "Puntuacion": [8.8, 9.2, 8.7, 8.5, 8.4],              # decimales -> float64
    "Genero": ["Ciencia ficción", "Drama", "Ciencia ficción", "Thriller", "Animación"],
}

df_peliculas = pd.DataFrame(peliculas)


print(df_peliculas.head());
print(df_peliculas.info);
print(df_peliculas.describe());
print(df_peliculas.shape());