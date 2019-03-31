# e) Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ2
# (x1,y1,x2,y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.
# Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados
# están en ℝ3 con coordenada 𝑧 = 0.
# Ejemplo: area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) → 65

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    """Recibe 4 vectores en R2 y devuelve el area del cuadrilátero que conforman"""
    return (1/2) * (
        x1 * y2 
      + x2 * y3 
      + x3 * y4 
      + x4 * y1 
      - y1 * x2 
      - y2 * x3 
      - y3 * x4 
      - y4 * x1
    )

print(area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5))