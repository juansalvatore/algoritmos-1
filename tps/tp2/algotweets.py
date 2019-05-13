import sys
from twitter import Tweets

def main():
    tweets = Tweets('tweets.csv')
    if len(sys.argv) == 1:
        return print('Debes pasar un segundo argumento [generar/trending/favoritos]')
    if sys.argv[1] == 'trending':
        try:
            tweets.trending(int(sys.argv[2]))
        except:
            tweets.trending()
    elif sys.argv[1] == 'generar':
        try:
            tweets.generar(sys.argv[2:])
            return
        except:
            return
    elif sys.argv[1] == 'favoritos':
        try:
            tweets.favoritos(int(sys.argv[2]))
        except Exception as err:
            tweets.favoritos()

main()