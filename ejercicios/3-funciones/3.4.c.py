# c) Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las
# coordenadas del producto vectorial, definido como:
# (𝑥1, 𝑦1, 𝑧1) × (𝑥2, 𝑦2, 𝑧2) =  (𝑦1𝑧2 − 𝑧1𝑦2, 𝑧1𝑥2 − 𝑥1𝑧2, 𝑥1𝑦2 − 𝑦1𝑥2)
# Ejemplo: producto_vec(1, 4, -2, 3, -1, 0) → (-2, -6, -13)

def producto_vec(𝑥1, 𝑦1, 𝑧1, 𝑥2, 𝑦2, 𝑧2):
    """recibe dos vectores en R3 y devuelve las coordenadas del producto vectorial"""
    return (𝑦1*𝑧2 - 𝑧1*𝑦2, 𝑧1*𝑥2 - 𝑥1*𝑧2, 𝑥1*𝑦2 - 𝑦1*𝑥2)

print(producto_vec(1, 4, -2, 3, -1, 0))