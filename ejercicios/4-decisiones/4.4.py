# Ejercicio 4.4. 
# Escribir funciones que permitan encontrar:
# a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
# c), indicando si es un máximo o un mínimo.
# b) Las raíces (reales o complejas) de un polinomio de segundo grado.
# Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
# cero, ni calcular la raíz de un número negativo).
# c) La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
# Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.

def maximo_minimo(a, b, c):
    max = (-b + ((b**2 - 4*a*c) ** (1/2)))/ (2*a)
    min = (-b - ((b**2 - 4*a*c) ** (1/2)))/ (2*a)
    return 'Maximo: ' + str(max) + '\n' + 'Minimo: ' + str(min)

print(maximo_minimo(1, -3, 2))