# b) Escribir una función que reciba las coordenadas de dos vectores en ℝ3
# (x1,y1,z1,x2,
# y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
# Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)
def diferencia(x1, y1, z1, x2, y2, z2):
    return x1-x2, y1-y2, z1-z2

print(diferencia(8, 7, -3, 5, 3, 2))