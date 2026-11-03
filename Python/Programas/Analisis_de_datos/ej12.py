import numpy as np

mat = np.arange(16).reshape(4, 4)
print("Matriz original:\n", mat)

# Dividir en 2 bloques horizontales
print("División vertical:\n", np.vsplit(mat, 2))

# Dividir en 2 bloques verticales
print("División horizontal:\n", np.hsplit(mat, 2))