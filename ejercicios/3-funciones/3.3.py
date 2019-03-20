# Ejercicio 3.3.
# Escribir una función que, dados cuatro números, devuelva el mayor producto de
# dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
# más grande que se puede obtener entre ellos (8 = −2 × −4).
def mayor_producto(*args):
    numbers = [*args]
    max1 = max(numbers)
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 * max2
    
print(mayor_producto(1, 2, 3, 4, 5))