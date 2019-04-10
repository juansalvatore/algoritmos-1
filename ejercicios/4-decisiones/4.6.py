# Ejercicio 4.6. 
# Suponiendo que el primer día del año fue lunes, escribir una función que reciba
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. 
# Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'.
def numero_a_dia(n):
    dias = ['', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado', 'domingo'] 
    return dias[n % 7]

print(numero_a_dia(1))