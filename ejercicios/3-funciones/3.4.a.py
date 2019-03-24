# Ejercicio 3.4.Área de polígonos
# a) Escribir una función que reciba las coordenadas de un vector en ℝ3
# (x,y,z) y devuelva
# la norma del vector, dada por ‖(𝑥, 𝑦, 𝑧)‖ = √𝑥2 + 𝑦2 + 𝑧2.
# Ejemplo: norma(3, 2, -4) → 5.3851
import math
def norma(x, y, z):
    return math.sqrt(x ** 2 + y ** 2 + z ** 2)
    
print(norma(3, 2, -4))