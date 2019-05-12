# Ejercicio 11.4. Escribir una clase Caja para representar cuánto dinero hay en una caja de un
# negocio, desglosado por tipo de billete (por ejemplo, en el quiosco de la esquina hay 6 billetes
# de 500 pesos, 7 de 100 pesos y 4 monedas de 2 pesos). Las denominaciones permitidas son 1, 2,
# 5, 10, 20, 50, 100, 200, 500 y 1000 pesos. Debe comportarse según el siguiente ejemplo:

# >>> c = Caja({500: 6, 300: 7, 2: 4})
# ValueError: Denominación "300" no permitida
# >>> c = Caja({500: 6, 100: 7, 2: 4})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 2: 4} total: 3708 pesos'
# >>> c.agregar({250: 2})
# ValueError: Denominación "250" no permitida
# >>> c.agregar({50: 2, 2: 1})
# >>> str(c)
# 'Caja {500: 6, 100: 7, 50: 2, 2: 5} total: 3810 pesos'
# >>> c.quitar({50: 3, 100: 1})
# ValueError: No hay suficientes billetes de denominación "50"
# >>> c.quitar({50: 2, 100: 1})
# 200
# >>> str(c)
# 'Caja {500: 6, 100: 6, 2: 5} total: 3610 pesos'


class Caja:
    def __init__(self, caja, den_permitidas=[1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]):
        self.caja = self._validar_caja(caja)
        self.den_permitidas = den_permitidas

    def __str__(self):
        caja = ', '.join([f'{key}: {self.caja[key]}' for key in self.caja])
        total = 0
        for key in self.caja:
            total += self.caja[key] * key
        return 'Caja {' + caja + '} total: ' + str(total) + ' pesos'

    def _validar_caja(self, caja):
        for key in caja:
            if key not in self.den_permitidas:
                raise ValueError(f'Denominación "{key}" no permitida')
        return caja

    def agregar(self, billetes):
        self._validar_caja(billetes)
        for key in billetes:
            if key not in self.caja.keys():
                self.caja = {**self.caja, **billetes}
                return
            self.caja = {**self.caja, key: self.caja[key] + billetes[key]}

    def quitar(self, billetes):
        self._validar_caja(billetes)
        total = 0
        for key in billetes:
            caja_key = self.caja.get(key, 0)
            if caja_key - billetes[key] < 0:
                raise ValueError(
                    f'No hay suficientes billetes de denominación "{key}"')
            self.caja[key] -= billetes[key]
            total += billetes[key] * key
        return total
