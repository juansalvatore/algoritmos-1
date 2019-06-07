import csv
import pprint
from datetime import datetime
from helpers import CadenaMarkov, Hashtags

class Tweets():
    '''
        La clase Tweet recibe una cadena de caracteres con el nombre del archivo
        contenedor de tweets. Retorna un objecto con los metodos publicos generar, trending y
        favoritos. 
    '''
    def __init__(self, arch_tweets):
        self.arch_tweets = arch_tweets
        self.tweets = self._set_tweets()

    def generar(self, usuarios=[]):
        """
            Recibe self y el arreglo usuarios como argumento opcional. Imprime un tweet creado 
            a partir de una cadena de markov, la cual es generada a partir del nombre de 
            archivo pasado a la clase Tweet. Permite al usuario guardar en 'favoritos.csv' el
            tweet generado. 
        """
        usuarios = self._set_usuarios(usuarios)
        self._print_generando_tweets(usuarios)
        tweet_generado = CadenaMarkov(self.tweets, usuarios).recorrer()
        print(f'{tweet_generado}\n"""\n')
        self._guardar_a_favoritos(tweet_generado)
    
    def trending(self, n = 0):
        """
            Recibe el nombre del archivo contenedor de tweets (str) y el parametro opcional n (int), que
            representa la cantidad de trending topics a imprimir. Imprime n cantidad de trending topics
            de mayor a menor cantidad de apariciones. En caso de que n sea mayor a la cantidad de Hashtags
            imprime todos los hashtags encontrados.
        """
        Hashtags(self.arch_tweets).get_trending(n)

    def favoritos(self, n = 0):
        """
            Recibe el parametro opcional n (int) e imprime n cantidad de tweets guardados en favoritos. 
            En caso de que n sea mayor a la cantidad de Hashtags imprime todos los hashtags encontrados.
        """
        try:
            with open('favoritos.csv') as favoritos:
                for i, tweet in enumerate(favoritos):
                    if n and i == n: return
                    tweet = tweet.split('\t')[1].rstrip('\n')
                    print(f'{i + 1} - {tweet}')
        except FileNotFoundError:
            return print('No se encontró el archivo "favoritos.csv"')

    def _print_generando_tweets(self, usuarios):
        """
            Recibe un arreglo de usuarios e imprime el mensaje:
            Generando tweet a partir de: usuario1, usuario2, ..., usuarioN...\\n\\n\"\"\"')
        """
        usuarios_str = ''
        for i, usuario in enumerate(usuarios):
            usuarios_str += usuario
            if i == len(usuarios) - 1:
                break
            usuarios_str += ', '
        print(f'Generando tweet a partir de: {usuarios_str}...\n\n"""')

    def _guardar_a_favoritos(self, tweet_generado):
        """
            Recibe un tweet (str) y pregunta al usuario si desea o no guardar el tweet.
            en caso de que el input sea 's' guarda al comienzo del archivo 'favoritos.csv' la fecha actual y 
            el tweet, separados por el caracter '\\t'. En caso de que sea 'n' el programa finaliza.
            Si el input no es 's' ni 'n' el programa continua pidiendo un input.
        """
        while True:
            input_usr = input('¿Desea agregar este tweet a favoritos? [s/n] ')
            if input_usr == 's':
                try: 
                    tweets_favoritos = []
                    with open('favoritos.csv', 'r') as favoritos:
                        for line in favoritos:
                            line = line.rstrip('\n')
                            tweets_favoritos.append(line)
                    with open('favoritos.csv', 'w') as favoritos:
                        favoritos.write(f'{datetime.now()}\t{tweet_generado}\n')  
                        for tweet in tweets_favoritos:
                            favoritos.write(f'{tweet}\n')  
                except Exception as err:
                    with open('favoritos.csv', 'w') as favoritos:
                        favoritos.write(f'{datetime.now()}\t{tweet_generado}\n')                    
                break
            if input_usr == 'n':
                break

    def _set_usuarios(self, usuarios):
        """
            Recibe un arreglo de usuarios (str), en caso de que este vacío retorna un arreglo con las claves
            del diccionario self.tweets, en caso contrario retorna el mismo arreglo recibido como argumento.
        """
        if not usuarios:
            usuarios = self.tweets.keys()
        else:
            # validar que el usuario existe
            for usuario in usuarios: 
                if usuario not in self.tweets.keys():
                    return print(f'No se tiene información sobre el usuario: {usuario}')
        return usuarios

    def _set_tweets(self):
        """ 
            Recibe una referencia al constructor (self) y retorna un diccionario con una clave por cada usuario y 
            como valor un arreglo compuesto por una cadena de caracteres por cada tweet del respectivo usuario.
        """
        dic = {}
        with open(self.arch_tweets, encoding="utf8") as tweets:
            reader = csv.reader(tweets, delimiter='\t')
            for tweet in reader:
                dic[tweet[0]] = [*dic.get(tweet[0], [tweet[1]]), tweet[1]]
        return dic
    