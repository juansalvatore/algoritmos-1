# Input que devuelve un integer
def get_int(message):
    return int(input(message))

# Redondea numero a dos decimales
def round_decimal(number):
    return "{:.2f}".format(number)

# Convierte la temperatura de fahrenheit a Celsius
def fahrenheit_to_celsius(temp):
    return round_decimal(((temp - 32) * 5) / 9) + 'C'

def es_par(number):
    return number % 2 == 0