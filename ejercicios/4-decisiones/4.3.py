# Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la
# matriz identidad correspondiente a esa dimensión.
def es_par(n):
    return n % 2 == 0

def matriz_identidad(n):
    area = n**2
    row = 1
    for col in range(1, area + 1):
        if(col % n == row or col == area):
            print(1, end=" ")
        else:
            print(0, end=" ")
        
        if (col % n == 0):
            print()
            row += 1
    

matriz_identidad(4)