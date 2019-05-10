
# 1. Escribir una función que reciba una cadena y devuelva una tupla con la palabra que tuvo mayor cantidad de apariciones,
# y la cantidad de apariciones que tuvo. Si hay dos o más palabras con máxima cantidad de apariciones, devolver cualquiera
# de ellas. La cadena contiene únicamente palabras y espacios. Ejemplo: "la cama la silla y la mesa." -> ("la", 3).


import csv


def palabra_con_mas_apariciones(str):
    dic = {}
    palabras = str.lower().split(' ')
    r = {'palabra': '', 'repeticiones': 0}
    for palabra in palabras:
        dic[palabra] = dic.get(palabra, 0) + 1
        if dic[palabra] >= r['repeticiones']:
            r['palabra'] = palabra
            r['repeticiones'] = dic[palabra]
    return (r['palabra'], r['repeticiones'])


# print(palabra_con_mas_apariciones("la cama la silla y la mesa."))

# 2. Se cuenta con un archivo en formato csv que guarda información de pasajes de avión, respetando la siguiente estructura:
# fecha, destino, precio. Escribir una función que dada la ruta del archivo, devuelva un diccionario cuyas claves sean
# cada uno de los destinos, y el valor asociado a cada clave una tupla(fecha, precio) con el pasaje más barato para
# el destino.


def info_aviones(archivo):
    vuelos = {}
    with open(archivo, 'r') as arch:
        reader = csv.reader(arch)
        next(reader)
        for destino, fecha, precio in reader:
            precio_anterior = vuelos.get(destino, '')
            if precio_anterior:
                if int(precio) < precio_anterior[1]:
                    vuelos[destino] = (fecha, int(precio))
            else:
                vuelos[destino] = (fecha, int(precio))

    return vuelos


# print(info_aviones('aviones.csv'))

# 3. Se quiere modelar un perchero para colgar ropa. Se pide crear las clases Perchero y Prenda tal que se se puedan
# ejecutar las siguientes líneas de código y se obtengan los resultados especificados. El constructor de Perchero recibe la
# cantidad de espacio total disponible, y el de Prenda recibe el nombre de la prenda y cuánto espacio ocupa:
# >>> p = Perchero(3)
# >>> p.colgar(Prenda('camisa', 1))
# >>> p.colgar(Prenda('pantalon', 1))
# >>> p.sacar('pantalon')
# Prenda('pantalon', 1)
# >>> p.sacar('remera')
# Exception: No se encontró la prenda
# >>> p.espacio_disponible()
# 2
# >>> p.colgar(Prenda('campera', 3))
# Exception: No hay espacio para colgar la prenda

class Perchero:
    def __init__(self, total_espacio_disponible):
        self.prendas = {}
        self.espacio_ocupado = 0
        self.total_espacio_disponible = total_espacio_disponible

    def colgar(self, prenda):
        try:
            if prenda.espacio + self.espacio_ocupado > self.total_espacio_disponible:
                raise Exception(
                    'Excepcion: No hay espacio para colgar la prenda')
        except Exception as err:
            return str(err)
        self.espacio_ocupado += prenda.espacio
        self.prendas[prenda.nombre.lower()] = prenda.espacio

    def sacar(self, nombre):
        try:
            if nombre in self.prendas:
                self.espacio_ocupado -= self.prendas[nombre]
                print(f"Prenda('{nombre}', {self.prendas[nombre]})")
                del self.prendas[nombre]
                return
            raise Exception('Excepcion: No se encontró la prenda')
        except Exception as err:
            return str(err)

    def espacio_disponible(self):
        return self.total_espacio_disponible - self.espacio_ocupado


class Prenda:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio

    def __str__(self):
        return f"Prenda('{self.nombre}', {self.espacio})"
