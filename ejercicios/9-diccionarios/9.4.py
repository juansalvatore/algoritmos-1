# Ejercicio 9.4. Escribir una función que reciba un texto y para cada caracter presente en el texto
# devuelva la cadena más larga en la que se encuentra ese caracter.

def cadenas_mas_largas(texto):
    dic = {}
    texto = texto.split(' ')
    for palabra in texto:
        for letra in palabra:
            if dic.get(letra, ''):
                if len(palabra) >= len(dic[letra]):
                    dic[letra] = palabra
            else: 
                dic[letra] = palabra
    return dic

print(cadenas_mas_largas('a aa b bb c cc ccc'))