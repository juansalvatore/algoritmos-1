import sys
import csv
import pprint
from datetime import datetime
from helpers import CadenaMarkov, Hashtags

class Tweets():
    def __init__(self, arch_tweets):
        self.arch_tweets = arch_tweets
        self.tweets = self._set_tweets()

    def generar(self, usuarios=[]):
        usuarios = self._set_usuarios(usuarios)
        self._print_generando_tweets(usuarios)
        tweet_generado = CadenaMarkov(self.tweets, usuarios).recorrer()
        print(f'{tweet_generado}\n"""\n')
        self._guardar_a_favoritos(tweet_generado)
    
    def trending(self, n=0):
        Hashtags(self.arch_tweets).get_trending(n)

    def favoritos(self, n):
        with open('favoritos.csv') as favoritos:
            for i, tweet in enumerate(favoritos):
                if i == n: return
                tweet = tweet.split('\t')[1].rstrip('\n')
                print(f'{i + 1} - {tweet}')

    def _print_generando_tweets(self, usuarios):
        usuarios_str = ''
        for i, usuario in enumerate(usuarios):
            usuarios_str += usuario
            if i == len(usuarios) - 1:
                break
            usuarios_str += ', '
        print(f'Generando tweet a partir de: {usuarios_str}...\n\n"""')

    def _guardar_a_favoritos(self, tweet_generado):
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
            Recibe una referencia al constructor y retorna un diccionario con una clave por cada usuario y 
            como valor un arreglo compuesto por una cadena de caracteres por cada tweet del respectivo usuario.
        """
        dic = {}
        with open(self.arch_tweets, encoding="utf8") as tweets:
            reader = csv.reader(tweets, delimiter='\t')
            for tweet in reader:
                dic[tweet[0]] = [*dic.get(tweet[0], [tweet[1]]), tweet[1]]
        return dic
    

def main():
    print(sys.argv)
    tweets = Tweets('tweets.csv')
    tweets.trending(4)
    # tweets.generar()
    # tweets.favoritos(5)

main()