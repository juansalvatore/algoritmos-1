import random
import csv

class CadenaMarkov:
    def __init__(self, dic = {}, usuarios = []):
        self.cadena = self._generar_cadena_markov(usuarios, dic)

    def get_hashtags_cadena(self):
        return self.cadena

    def recorrer(self, next_word = ''):
        """
            Recibe una palabra para comenzar a recorrer la cadena de markov y retorna una cadena de caracteres
            con el camino que se recorrió.
        """
        if not next_word:
            next_word = random.choice(list(self.cadena.keys()))
        if next_word not in self.cadena.keys():
            raise Exception('La palabra que se eligió para comenzar a recorrer la cadena de markov no se encontró en la cadena')
        camino_recorrido = ''
        while True:
            if len(camino_recorrido) + len(next_word.rstrip('\n')) > 280:
                break
            camino_recorrido += next_word.rstrip('\n')
            if next_word == '\n':
                break
            camino_recorrido += ' '
            opciones_palabras = self.cadena[next_word]
            nuevas_opciones = []
            for opcion in opciones_palabras.keys():
                for palabra in range(opciones_palabras[opcion]):
                    nuevas_opciones.append(opcion)
            next_word = random.choice(nuevas_opciones)
        return camino_recorrido

    def _generar_cadena_markov(self, usuarios, dic):
        """
            Recibe un diccionario con arreglos de cadenas de caracteres como valores y un arreglo de nombres de usuarios
            devuelve una cadena de markov realizada en base a este diccionario.
        """
        if not usuarios:
            usuarios = self.cadena_markov.keys()
        new_dic = {}
        for usuario in usuarios:
            for string in dic[usuario]:
                palabras = string.split(' ')
                for i, palabra_a in enumerate(palabras):
                    if palabra_a == '':
                        continue
                    try:
                        if not palabras[i + 1]:
                            continue
                    except:
                        new_dic[palabra_a] = {'\n': 1}
                        continue
                    if new_dic.get(palabra_a, ''):
                        if new_dic[palabra_a].get(palabras[i + 1], ''):
                            new_dic[palabra_a][palabras[i + 1]] += 1
                        else:
                            new_dic[palabra_a] = {**new_dic[palabra_a], palabras[i + 1]: 1}
                    else:
                        new_dic[palabra_a] = {palabras[i + 1]: 1}
        return new_dic

class Hashtags:
    def __init__(self, arch_tweets):
        self.trending = self._create_sorted_trending_hashtags(arch_tweets)

    def _create_sorted_trending_hashtags(self, arch_tweets):
        trending_dic = {}
        with open(arch_tweets, encoding="utf8") as tweets:
            reader = csv.reader(tweets, delimiter='\t')
            for tweet in reader: 
                hashtags = self.get_hashtags(tweet[1])
                for hashtag in hashtags:
                    if hashtag:
                        trending_dic[hashtag] = trending_dic.get(hashtag, 0) + 1
        sortable = [{'name': key, 'repetitions': trending_dic[key]} for key in trending_dic.keys()]
        sortable.sort(key=lambda x: x['repetitions'], reverse=True)
        return sortable

    def get_trending(self, n):
        self._validar_cantidad_trending(n)
        for i, hashtag in enumerate(self.trending):
            if i >= n:
                return
            print(hashtag['name'])
        return self.trending 

    def get_hashtags(self, tweet):
        return [word for word in tweet.split(' ') if word[0] == '#']

    def _validar_cantidad_trending(self, n):
        if not n:
            return print('Debes definir la cantidad de temas que se desean mostrar.')
        if n < 0:
            return print('Debes definir la cantidad de temas que se desean mostrar con un numero positivo.')
        if not self.trending:
            return print('No hay hashtags')