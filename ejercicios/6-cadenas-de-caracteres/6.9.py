def pedir_entero(mensaje, min, max):
    """imprime un mensaje y luego espera que el usuario ingrese un numero entero 
        que se encuentre en el rango [min, max] con el minimo y el máximo incllusives.
        En caso de no cumplir el requisito aclara el rango y pide entrar un nuevo numero."""
    numero = input(mensaje)
    while not numero.isdigit() or int(numero) not in range(min, max + 1):
        print(f'Por favor ingresa un número entre {min} y {max}.')
        numero = input(mensaje)
    return numero
    
edad = pedir_entero('¿cuántos años tenés? [0-150]: ', 2, 150)
print(edad)
