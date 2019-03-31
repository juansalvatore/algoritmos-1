# d) Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
# 3 puntos en ℝ3 y devuelva el área del triángulo que conforman.
# Ayuda: Si 𝐴, 𝐵 y 𝐶 son 3 puntos en el espacio, la norma del producto vectorial 𝐴𝐵 × 𝐴𝐶 es
# igual al doble del área del triángulo 𝐴𝐵𝐶.
# Ejemplo: area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) → 19.4551
import math
def norma(x, y, z):
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)

def diferencia(x1, y1, z1, x2, y2, z2):
    return x1-x2, y1-y2, z1-z2

def producto_vec(𝑥1, 𝑦1, 𝑧1, 𝑥2, 𝑦2, 𝑧2):
    """Recibe dos vectores en R3 y devuelve las coordenadas del producto vectorial"""
    return (𝑦1*𝑧2 - 𝑧1*𝑦2, 𝑧1*𝑥2 - 𝑥1*𝑧2, 𝑥1*𝑦2 - 𝑦1*𝑥2)

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Recibe tres vectores en R3 y devuelve el area del triangulo que conforman"""
    ab = diferencia(x2, y2, z2, x1, y1, z1)
    ac = diferencia(x3, y3, z3, x1, y1, z1)
    return norma(*producto_vec(*ab,*ac)) / 2

print(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))