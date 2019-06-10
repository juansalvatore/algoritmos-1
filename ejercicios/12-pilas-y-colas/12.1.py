# Ejercicio12.1. Escribir una clase TorreDeControl que modele el trabajo de una torre de control de un aeropuerto con una pista de aterrizaje.
# Los aviones que están esperando para aterrizar tienen prioridad sobre los que están esperando para despegar.
# La clase debe funcionar conforme al siguiente ejemplo:
# >>> torre = TorreDeControl()
# >>> torre.nuevo_arribo('AR156')
# >>> torre.nueva_partida('KLM1267')
# >>> torre.nuevo_arribo('AR32')
# >>> torre.ver_estado() Vuelos esperando para aterrizar: AR156, AR32 Vuelos esperando para despegar: KLM1267
# >>> torre.asignar_pista() El vuelo AR156 aterrizó con éxito. 18
# >>> torre.asignar_pista() El vuelo AR32 aterrizó con éxito.
# >>> torre.asignar_pista() El vuelo KLM1267 despegó con éxito.
# >>> torre.asignar_pista() No hay vuelos en espera.


class TorreDeControl:
    def __init__(self):
        self.arribos = []
        self.partidas = []

    def nuevo_arribo(self, avion):
        """ Prioridad por sobre nueva_partida """
        self.arribos.append(avion)

    def nueva_partida(self, avion):
        self.partidas.append(avion)

    def ver_estado(self):
        arribos = ', '.join([str(avion) for avion in self.arribos])
        partidas = ', '.join([str(avion) for avion in self.partidas])
        return f'Vuelos esperando para aterrizar: {arribos} Vuelos esperando para despegar: {partidas}'

    def asignar_pista(self):
        if len(self.arribos) != 0:
            return self.arribos.pop(0)
        elif len(self.partidas) != 0:
            return self.partidas.pop(0)
        raise IndexError('Lista vacía')


def main():
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    # print(torre.ver_estado())
    print(torre.asignar_pista())
    print(torre.asignar_pista())
    print(torre.asignar_pista())
    print(torre.asignar_pista())


main()
