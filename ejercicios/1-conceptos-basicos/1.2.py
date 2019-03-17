import math

# @HELPER: Log numero de ejercicio
def ejercicio(titulo, resultado):
    print('\nEjercicio:', titulo, resultado)

# @EJERCICIOS:

# Implementar algoritmos que permitan:
# a) Calcular el perímetro de un rectángulo dada su base y su altura.
def perimetroRectangulo(base, altura):
    return base * 2 + altura * 2

ejercicio('1.2) a) Perimetro Rectangulo:', perimetroRectangulo(2, 4))

# b) Calcular el área de un rectángulo dada su base y su altura.
def areaRectangulo(base, altura):
    return base * altura

ejercicio('1.2) b) Area Rectangulo:', areaRectangulo(2, 5))

# c) Calcular el área de un rectángulo(alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas 𝑥1, 𝑥2, 𝑦1, 𝑦2.
def areaCoordenadas(x1, x2, y1, y2):
    ladoX = x2 - x1
    ladoY = y2 - y1
    return areaRectangulo(ladoX, ladoY)

ejercicio('1.2) C) Area Coordenadas:', areaCoordenadas(2, 5, 2, 4))

# d) Calcular el perímetro de un círculo dado su radio.
def perimetroCirculo(r):
    return "{:.2f}".format(math.pi * (r*2))

ejercicio('1.2) d) Perimetro Circulo:', perimetroCirculo(3))

# e) Calcular el área de un círculo dado su radio.
def areaCirculo(r):
    return "{:.2f}".format(math.pi * (r**2))

ejercicio('1.2) e) Area Circulo:', areaCirculo(3))

# f) Calcular el volumen de una esfera dado su radio.
def volumenEsfera(r):
    return "{:.2f}".format((4 * math.pi* r**3)/3)
    
ejercicio('1.2) f) Volumen Esfera:', volumenEsfera(3))


# g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
