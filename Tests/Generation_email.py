import requests
import random


def Email():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    WORDS = response.content.splitlines()
    word1 = str(random.choice(WORDS))
    word2 = str(random.choice(WORDS))
    return word1 + word2 + "@gmail.com"
