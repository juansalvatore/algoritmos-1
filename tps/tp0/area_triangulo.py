from vectores import diferencia, producto_vectorial, norma

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """Recibe las coordenadas de 3 vectores en R3 y devuelve el área del triángulo que conforman"""
    ab = diferencia(x1, y1, z1, x2, y2, z2)
    ac = diferencia(x1, y1, z1, x3, y3, z3)
    return norma(*producto_vectorial(*ab, *ac))/2
    
assert area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19.45507645834372
assert area_triangulo(0, 0, 1, 0, 1, 0, 1, 0, 0) == 0.8660254037844386
assert area_triangulo(0, 0, 0, 0, 0, 0, 0, 0, 0) == 0.0
assert area_triangulo(1, 1, 1, 1, 1, 1, 1, 1, 1) == 0.0
assert area_triangulo(-4, 12, -1, -22, 13, 4, -9, 3, 1) == 86.91806486571132
assert type(area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0)) == float