# Ejercicio 1.3
# Mostrar el resultado de ejecutar estos bloques de código en el intérprete de python:
# a) >>> for i in range(5):
# ... print(i * i)
def loop(r):
    for i in range(r):
        print(i, i*i)

print('\n1.3) a)')
loop(5)

# b) >>> for i in range(2, 6):
# ... print(i, 2 ** i)
def loopRange(start, end):
    for i in range(start, end + 1):
        print(i, 2 ** i)

print('\n1.3) b)')
loopRange(3, 10)