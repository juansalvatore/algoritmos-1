# Input que devuelve un integer
def get_int(message):
    return int(input(message))

# Redondea numero a dos decimales
def roundDecimal(number):
    return "{:.2f}".format(number)

# Convierte la temperatura de fahrenheit a Celsius
def fahrenheitToCelsius(temp):
    return roundDecimal(((temp - 32) * 5) / 9) + 'C'

def esPar(number):
    return number % 2 == 0