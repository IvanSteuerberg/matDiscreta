"""
Sea g(n, k) = número de maneras de colocar k leones en n jaulas, de manera que nunca
haya dos leones en la misma jaula o en jaulas contiguas.
Hallar g(11, 4)
"""
import math
import sys
import timeit
sys.setrecursionlimit(30000)  # aumentado el límite de recurrencia del sistema para poder probar valores altos


"""
g(n,k) =
0 si n<2k-1
1 si n=2k-1
n si k=1
g(n-2, k-1) + g(n-1, k)


"""


#   k leones en n jaulas por recurrencia
def g(n, k):
    if k == 1:
        return n
    if n < (2 * k - 1):
        return 0
    if n == (2 * k - 1):
        return 1
    else:
        return g(n - 2, k - 1) + g(n - 1, k)


#   k leones en n jaulas por combinatoria
def h(n, k):
    if k == 1:
        return n
    if n < (2 * k - 1):
        return 0
    if n == (2 * k - 1):
        return 1
    else:
        return int(math.factorial(n - k + 1) / (math.factorial(k) * math.factorial(n - k + 1 - k)))

#   Algunos testeos para n entre [1, 11] y k entre [1,4]
"""
for n in range(1, 12):
    for k in range(1, 5):
        texto = f"g({n},{k}) = {g(n, k)}    ->   h({n}, {k}) = {h(n, k)}"
        print(texto)
"""

"""
Escoger la función que se quiere utilizar para el cálculo.
Introducir el número de jaulas y leones.
Todo a través del terminal y tantas veces como se quiera.
"""
while True:
    f = input("Quieres usar la funcion por recurrencia(g) o por combinatoria(h)? (introduce g o h):\n")
    n = int(input("Introduce el número de jaulas (n):\n"))
    k = int(input("Introduce el número de leones (k):\n"))
    start = timeit.default_timer()
    print(f"g({n},{k}) = {g(n, k)}" if f == "g" else f"h({n}, {k}) = {h(n, k)}")
    stop = timeit.default_timer()
    print(f"Tiempo de ejecución: {int(stop - start)}s")
