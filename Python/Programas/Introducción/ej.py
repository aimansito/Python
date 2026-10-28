 # Datos de prueba: 1 millon de registros (simulando transacciones bancarias) 
np.random.seed(42)
datos = np.random.randn(1_000_000)
lista_python = datos.tolist()


# Operacion 1: multiplicacion simple conversion de moneda

t0 = time.perf_counter()
_ = [x * 1.08 for x in lista_python]
t_py_mmult = time.perf_counter() - t0

t0 = time.perf_counter()
_ = datos *  1.08
t_np_mult = time.perf_counter() - t0