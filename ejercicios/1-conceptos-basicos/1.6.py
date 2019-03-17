# Ejercicio 1.6. 
# Escribir un programa que le pida una palabra al usuario, para luego imprimirla
# 1000 veces, en una única línea, con espacios intermedios.
# Ayuda: Investigar acerca del parámetro end de la función print.

def magicTrick():
    palabra = input('Por favor, escriba una palabra: ')
    for _ in range(100):
        print(palabra, end=' ')

magicTrick()