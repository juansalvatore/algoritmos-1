# Ejercicio 6.5. Escribir una función que dada una cadena de caracteres, devuelva:
# a) La primera letra de cada palabra. Por ejemplo, si recibe 'Universal Serial Bus' debe
# devolver 'USB'.
# b) Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe
# 'república argentina' debe devolver 'República Argentina'.
# c) Las palabras que comiencen con la letra ‘A’. Por ejemplo, si recibe 'Antes de ayer'
# debe devolver 'Antes ayer'


def first_letters(str):
    result = []
    for word in str.split(' '):
        result.append(word[0])
    return ''.join(result)


# print(first_letters('Universal Serial Bus'))


def capitalize(str):
    result = []
    for word in str.split(' '):
        result.append(word[0].upper() + word[1: len(word)])
    return ' '.join(result)


# print(capitalize('republica argentina'))

def words_that_start(str):
    result = []
    for word in str.split(' '):
        if word[0].lower() == 'a':
            result.append(word)
    return ' '.join(result)


print(words_that_start('Antes de estaba andande ayer'))
