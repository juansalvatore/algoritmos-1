import math
from helpers import ejercicio, round_decimal

# Ejercicio 1.2
# a) Calcular el perímetro de un rectángulo dada su base y su altura.
def perimetro_rectangulo(base, altura):
    lados = 2
    return base * lados + altura * lados

ejercicio('1.2) a) Perimetro Rectangulo:', perimetro_rectangulo(2, 4))

# b) Calcular el área de un rectángulo dada su base y su altura.
def area_rectangulo(base, altura):
    return base * altura

ejercicio('1.2) b) Area Rectangulo:', area_rectangulo(2, 5))

# c) Calcular el área de un rectángulo(alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas 𝑥1, 𝑥2, 𝑦1, 𝑦2.
def area_coordenadas(x1, x2, y1, y2):
    ladoX = x2 - x1
    ladoY = y2 - y1
    return area_rectangulo(ladoX, ladoY)

ejercicio('1.2) C) Area Coordenadas:', area_coordenadas(2, 5, 2, 4))

# d) Calcular el perímetro de un círculo dado su radio.
def perimetro_circulo(r):
    return round_decimal(math.pi * (r*2))

ejercicio('1.2) d) Perimetro Circulo:', perimetro_circulo(3))

# e) Calcular el área de un círculo dado su radio.
def area_circulo(r):
    return round_decimal(math.pi * (r**2))

ejercicio('1.2) e) Area Circulo:', area_circulo(3))

# f) Calcular el volumen de una esfera dado su radio.
def volumen_esfera(r):
    return round_decimal((4 * math.pi* r**3)/3)
    
ejercicio('1.2) f) Volumen Esfera:', volumen_esfera(3))


# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
def calcular_hipotenusa(cateto1, cateto2):
    return round_decimal(math.sqrt(cateto1 ** 2 + cateto2 ** 2))

ejercicio('1.2) g) Hipotenusa:', calcular_hipotenusa(2, 2))
