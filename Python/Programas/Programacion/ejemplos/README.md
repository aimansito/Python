# Ejemplos de los temas

Un fichero por cada apartado de los PDFs de `../Temas/`. Todos se pueden ejecutar
(`python 01_variables_y_tipos.py`) y están comentados línea a línea.

| Fichero | Qué enseña | PDF |
|---|---|---|
| `01_variables_y_tipos.py` | Comentarios, variables, snake_case, asignación múltiple, constantes, type hints, ámbito | tema1 (1-2) |
| `02_entrada_y_salida.py` | `input`, `print`, `int()`/`float()`, f-strings, validar un número con `isdigit()` | tema1 (3) |
| `03_operadores.py` | Aritméticos, `//`, `%`, `**`, `+=`..., comparación, `and`/`or`/`not`, `in` | tema1 (4) |
| `04_condicionales.py` | `if`/`elif`/`else`, condiciones compuestas, operador ternario | tema1 (5) |
| `05_bucles.py` | `while`, bandera, `for`, `range`, bucles anidados, `break`, `continue`, `else`, `pass` | tema1 (5) |
| `06_funciones_builtin_y_modulos.py` | `abs`, `chr`, `ord`, `divmod`, `len`, `max`, `min`..., `import math`, `random` | tema1 (6) |
| `07_funciones.py` | `def`, docstring, parámetros, valores por defecto, `return`, varios retornos, type hints, `global` | tema1 (7) + funciones |
| `08_listas.py` | Índices, slices, `del`, anidadas, recorrer con `enumerate`/`range`/`zip`, `sort`, `in`/`index`/`count`, `append`/`insert`/`remove`/`pop`..., comprensión | lista1 + lista2 |
| `09_matrices.py` | Lista de listas, crear un tablero 3x3, recorrer, filas, columnas y diagonales | lista2 |

## Herramientas permitidas (lo que se ha visto en clase)

- **Datos:** `int`, `float`, `str`, `bool`, listas y listas de listas (matrices). Constantes en MAYÚSCULAS.
- **Entrada/salida:** `input()`, `print()`, `int()`, `float()`, `str()`, f-strings.
- **Control:** `if`/`elif`/`else`, ternario, `while`, `for` + `range`, `break`, `continue`, `pass`.
- **Funciones:** `def`, parámetros (con y sin valor por defecto), `return`, docstring `'''...'''`.
- **Built-in:** `len`, `max`, `min`, `abs`, `chr`, `ord`, `divmod`, `enumerate`, `zip`, `sorted`, `type`...
- **Módulos:** solo los de la biblioteca estándar vistos (`math`, `random`).
- **Nombres:** `snake_case` para variables y funciones, descriptivos.
- **Buenas prácticas del guion:** validar la entrada del usuario y los parámetros de las funciones,
  y no repetir código (sacarlo a funciones).
