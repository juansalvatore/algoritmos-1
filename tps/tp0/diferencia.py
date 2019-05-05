def diferencia(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve su diferencia"""
    dif_x = x1 - x2
    dif_y = y1 - y2
    dif_z = z1 - z2
    return dif_x, dif_y, dif_z

assert diferencia(0, -9, -1, -9, 3, 8) == (9, -4, 42)
assert diferencia(5, 1, 2, -14, -2, -3) == (19, 4, 24)
assert diferencia(9, -8, 1, 20, 44, 8) == (-11, -43, 40)
assert diferencia(15, -10, -5, 28, 54, 25) == (-13, -59, 68)
assert diferencia(1, 1, 2, 2, 3, 3) == (0, 0, 0)