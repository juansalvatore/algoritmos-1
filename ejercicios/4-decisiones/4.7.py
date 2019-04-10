# Ejercicio 4.7. ⋆ Escribir un programa que reciba como entrada un entero representando un
# año (por ejemplo 751, 1999, o 2158), y muestre por pantalla el mismo año escrito en números
# romanos
    # I-1
    # V-5
    # X-10
    # L-50
    # C-100
    # D-500
    # M-1000
def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)

print(int_to_roman(8))