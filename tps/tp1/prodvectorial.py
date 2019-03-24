def producto_vectorial(x1, y1, z1, x2, y2, z2):
    """Recibe las coordenadas de dos vectores en R3 y devuelve el producto vectorial"""
    return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2

assert producto_vectorial(54, 12, 29, 1, 11, 12) == (-175, -619, 582)
assert producto_vectorial(71, 52, 24, 1, 11, 6) == (48, -402, 729)
assert producto_vectorial(70, 19, 37, -2, 11, 37) == (296, -2664, 808)
assert producto_vectorial(94, 67, 35, -11, 11, 31) == (1692, -3299, 1771)
assert producto_vectorial(99, 66, 33, -19, 11, 25) == (1287, -3102, 2343)
assert producto_vectorial(49, 35, 22, -17, 11, 24) == (598, -1550, 1134)
assert producto_vectorial(92, 53, 20, 10, 11, 3) == (-61, -76, 482)