def norma(x, y, z):
    """Recibe un vector en R3 y devuelve su norma"""
    return (x**2 + y**2 + z**2) ** 0.5

assert norma(2, 1, -2) == 3.0
assert norma(-2, 1, 2) == 3.0
assert norma(59, 82, 46) == 111.0
assert norma(57, 46, 78) == 107.0
assert norma(55, 66, 30) == 91.0
assert norma(-55, 66, -30) == 91.0
assert norma(54, 38, 99) == 119.0
assert norma(26, 2, 7) == 27.0
assert norma(0, 0, 0) == 0

x = 72
assert norma(70, 99, x) == 141.01418368376991