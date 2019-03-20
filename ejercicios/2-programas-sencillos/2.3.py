# Ejercicio 2.3. 
# Utilice el programa anterior para generar una tabla de conversión de temperaturas, 
# desde 0 °F hasta 120 °F, de 10 en 10.
from helpers import fahrenheit_to_celsius

def generar_tabla():
    for i in range(0, 13):
        fahrenheit = i * 10
        print(str(fahrenheit) + 'F', fahrenheit_to_celsius(fahrenheit))

generar_tabla()