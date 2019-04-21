def pedir_entero(mensaje, min, max):
    """imprime un mensaje y luego espera que el usuario ingrese un numero entero
        que se encuentre en el rango [min, max] con el minimo y el máximo incllusives.
        En caso de no cumplir el requisito aclara el rango y pide entrar un nuevo numero."""
    while True:
        numero = input(mensaje)
        if numero.isdigit() or ((len(numero) > 1 and numero[0] == '-') and (numero[1:].isdigit())):
            if int(numero) >= min and int(numero) <= max:
                return int(numero)
        print(f'Por favor ingresa un número entre {min} y {max}.')


edad = pedir_entero('¿cuántos años tenés? [0-150]: ', -25, 150)
print(edad)
