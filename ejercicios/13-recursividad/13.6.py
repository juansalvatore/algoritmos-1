# Ejercicio 13.6. Escribir una función recursiva que calcule recursivamente el n-ésimo número
# triangular (el número 1 + 2 + 3 + ⋯ + 𝑛).
def num_triangular(n):
    if n == 1:
        return 1
    return n + num_triangular(n-1)

print(num_triangular(6))

