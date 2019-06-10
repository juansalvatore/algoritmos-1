# Ejercicio 13.10. Escribir una funcion recursiva que dada una cadena determine si en la misma
# hay más letras A o letras E.


def cant_letras_a(c):
    cant_a = 0
    if not c:
        return 0
    elif c[0] == 'a':
        cant_a += 1
    return cant_a + cant_letras_e(c[1:])


def cant_letras_e(c):
    cant_e = 0
    if not c:
        return 0
    if c[0] == 'e':
        cant_e += 1
    return cant_e + cant_letras_a(c[1:])


def cant_letras(c):
    return cant_letras_a(c) < cant_letras_e(c)


print(cant_letras('aaaaabcdeeasdfee'))
