# 8) Escribir una funcion recursiva que reciba una cadena y devuelva True si es un palındromo
# (se lee igual hacia adelante que hacia atras) o False si no lo es.


def es_palindromo(cadena):
    if len(cadena) < 2:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])


print(es_palindromo("hola"))
print(es_palindromo("hooh"))
