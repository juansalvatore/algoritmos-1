import sys
import csv
import pprint
import random

class Tweets():
    def __init__(self, arch_tweets):
        self.arch_tweets = arch_tweets
        self.tweets = self._set_tweets()
        self.sorted_trending_hashtags = self._create_sorted_trending_hashtags()

    # GENERAR
    # $ python3 algotweets.py generar <usuario1> <usuario2> ...
    def generar(self, usuarios=[]):
        usuarios = self._validar_usuarios(usuarios)
        cadena_markov = self._generar_cadena_markov(usuarios)
        # pprint.pprint(cadena_markov)
        next_word = 'Aquí'
        tweet_generado = ''
        while True:
            tweet_generado += next_word.rstrip('\n')
            if next_word == '\n':
                break
            tweet_generado += ' '
            opciones_palabras = cadena_markov[next_word]
            opciones = list(opciones_palabras.keys())
            next_word = random.choice(opciones)
        print(tweet_generado)

    def _generar_cadena_markov(self, usuarios):                
        dic = {}
        for usuario in usuarios:
            for tweets in self.tweets[usuario]:
                for tweet in tweets.split('\n'):
                    palabras = tweet.split(' ')
                    for i, palabra_a in enumerate(palabras):
                        if palabra_a == '':
                            continue
                        try:
                            if not palabras[i + 1]:
                                continue
                        except:
                            dic[palabra_a] = {'\n': 1}
                            continue
                        if dic.get(palabra_a, ''):
                            if dic[palabra_a].get(palabras[i + 1], ''):
                                dic[palabra_a][palabras[i + 1]] += 1
                            else:
                                dic[palabra_a] = {**dic[palabra_a], palabras[i + 1]: 1}
                        else:
                            dic[palabra_a] = {palabras[i + 1]: 1}
        return dic

    def _validar_usuarios(self, usuarios):
        if not usuarios:
            usuarios = self.tweets.keys()
        else:
            # validar que el usuario existe
            for usuario in usuarios: 
                if usuario not in self.tweets.keys():
                    return print(f'No se tiene información sobre el usuario: {usuario}')
        return usuarios

    def _set_tweets(self):
        dic = {}
        with open(self.arch_tweets, encoding="utf8") as tweets:
            reader = csv.reader(tweets, delimiter='\t')
            for tweet in reader:
                dic[tweet[0]] = [*dic.get(tweet[0], [tweet[1]]), tweet[1]]
        return dic

    # TRENDING
    # $ python3 algotweets.py trending <cantidad>
    def trending(self, n):
        if not self.sorted_trending_hashtags:
            print('No hay hashtags')
        for i, hashtag in enumerate(self.sorted_trending_hashtags):
            if i >= n:
                return
            print(hashtag['name'])
    
    def _create_sorted_trending_hashtags(self):
        trending_dic = {}
        with open(self.arch_tweets, encoding="utf8") as tweets:
            reader = csv.reader(tweets, delimiter='\t')
            for tweet in reader: 
                hashtags = self._get_hashtags(tweet[1])
                for hashtag in hashtags:
                    if hashtag:
                        trending_dic[hashtag] = trending_dic.get(hashtag, 0) + 1
        sortable = [{'name': key, 'repetitions': trending_dic[key]} for key in trending_dic.keys()]
        sortable.sort(key=lambda x: x['repetitions'], reverse=True)
        return sortable


    def _get_hashtags(self, tweet):
        return [word for word in tweet.split(' ') if word[0] == '#']
                

    # FAVORITOS
    # $ python3 algotweets.py favoritos <cantidad>

def main():
    tweets = Tweets('test.csv')
    # tweets.trending(10)
    tweets.generar()

main()