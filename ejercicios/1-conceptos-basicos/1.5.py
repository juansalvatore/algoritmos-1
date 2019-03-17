# Ejercicio 1.5. 
# Implementar algoritmos que resuelvan los siguientes problemas:
# a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    return n1 / n2
    
def multiplicar(n1, n2):
    return n1 * n2

print('\nEjercicio: 1.5) a)', 'Sumar: ' + str(sumar(2, 2)))
print('\nEjercicio: 1.5) a)', 'Restar: ' + str(restar(2, 2)))
print('\nEjercicio: 1.5) a)', 'Dividir: ' + str(dividir(2, 2)))
print('\nEjercicio: 1.5) a)', 'Multiplicar: ' + str(multiplicar(2, 2)))


# b) Dado un número entero 𝑛, imprimir su tabla de multiplicar.
def tablas(n):
    for i in range(0, 11):
        print(n, 'x', i, '=', n * i)

print('\nEjercicio: 1.5) b) Tablas de multiplicar:')
tablas(2)