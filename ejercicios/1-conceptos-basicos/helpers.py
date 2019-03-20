# @HELPER: Log numero de ejercicio
def ejercicio(titulo, resultado):
    print('\nEjercicio:', titulo, resultado)

# Redondea numero a dos decimales
def round_decimal(number):
    return "{:.2f}".format(number)

# Input que devuelve un integer
def get_int(message):
    return int(input(message))