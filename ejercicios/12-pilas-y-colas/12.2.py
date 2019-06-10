# Ejercicio 12.2. Escribir las clases Impresora y Oficina que permita modelar el funcionamiento
# de un conjunto de impresoras conectadas en red.
# Una impresora:
# • Tiene un nombre, y una capacidad máxima de tinta.
# • Permite encolar un documento para imprimir (recibiendo el nombre del documento).
# • Permite imprimir el documento que está al frente de la cola.
# – Si no hay documentos encolados, se muestra un mensaje informándolo.
# – Si no hay tinta suficiente, se muestra un mensaje informándolo.
# – En caso contrario, se muestra el nombre del documento, y se gasta 1 unidad de tinta.
# • Permite cargar el cartucho de tinta
# Una oficina:
# • Permite agregar una impresora
# • Permite obtener una impresora por nombre
# • Permite quitar una impresora por nombre
# • Permite obtener la impresora que tenga menos documentos encolados.
# Ejemplo:

# >>> o = Oficina()
# >>> o.agregar_impresora(Impresora('HP1234', 1))
# >>> o.agregar_impresora(Impresora('Epson666', 5))
# >>> o.impresora('HP1234').encolar('tp1.pdf')
# >>> o.impresora('Epson666').encolar('tp2.pdf')
# >>> o.impresora('HP1234').encolar('tp3.pdf')
# >>> o.obtener_impresora_libre().encolar('tp4.pdf') # se encola en Epson666
# >>> o.impresora('HP1234').imprimir()
# tp1.pdf impreso
# >>> o.impresora('HP1234').imprimir()
# No tengo tinta :(
# >>> o.impresora('HP1234').cargar_tinta()
# >>> o.impresora('HP1234').imprimir()
# tp3.pdf impreso


class _Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.prox = None


class _Cola:
    def __init__(self):
        self.prim = None
        self.ultimo = None
        self.len = 0

    def encolar(self, dato):
        nuevo = _Nodo(dato)
        if self.len != 0:
            self.ultimo.prox = nuevo
            self.ultimo = self.ultimo.prox
        else:
            self.prim = nuevo
            self.ultimo = self.prim
        self.len += 1

    def desencolar(self):
        if self.len == 0:
            raise ValueError('Cola vacia')
        dato = self.prim.dato
        self.prim = self.prim.prox
        self.len -= 1
        return dato

    def esta_vacia(self):
        return self.len == 0


class Impresora:
    def __init__(self, nombre, capacidad_max):
        self.nombre = nombre
        self.capacidad_max = capacidad_max
        self.cola = _Cola()
        self.cant_archivos = 0

    def encolar(self, archivo):
        self.cola.encolar(archivo)
        self.cant_archivos += 1

    def imprimir(self):
        if not self.cola.esta_vacia():
            if self.capacidad_max == 0:
                return 'No tengo tinta'
            self.capacidad_max -= 1
            self.cant_archivos -= 1
            return f'{self.cola.desencolar()} impreso'
        else:
            return 'No hay archivos para imprimir'

    def cargar_tinta(self):
        self.capacidad_max += 1


class Oficina:
    def __init__(self):
        self.impresoras = {}

    def agregar_impresora(self, impresora):
        self.impresoras[impresora.nombre] = impresora

    def impresora(self, nombre):
        if self.impresoras.get(nombre, 0):
            return self.impresoras[nombre]
        return 'No hay impresoras con ese nombre'

    def obtener_impresora_libre(self):
        minimo = -1
        impresora_libre = None
        for nombre in self.impresoras.keys():
            impresora = self.impresoras[nombre]
            if impresora.cant_archivos < minimo or minimo == -1:
                minimo = impresora.cant_archivos
                impresora_libre = impresora
        if impresora_libre is None:
            raise Exception('No hay impresoras')
        return impresora_libre

    def eliminar_impresora(self, nombre):
        return self.impresoras.pop(nombre, None)


def main():
    o = Oficina()
    o.agregar_impresora(Impresora('HP1234', 1))
    o.agregar_impresora(Impresora('Epson666', 5))
    o.impresora('HP1234').encolar('tp1.pdf')
    o.impresora('Epson666').encolar('tp2.pdf')
    o.impresora('HP1234').encolar('tp3.pdf')
    o.obtener_impresora_libre().encolar('tp4.pdf')  # se encola en Epson666
    print(o.impresora('HP1234').imprimir())
    print(o.impresora('HP1234').imprimir())
    o.impresora('HP1234').cargar_tinta()
    print(o.impresora('HP1234').imprimir())
    print(o.eliminar_impresora('HP1234'))


main()
