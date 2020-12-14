import numpy as np
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
def process_word(sozder):
    stemmer = PorterStemmer()
    sozder = re.sub(r'https?:\/\/.*[\r\n]*','',sozder)
    sozder = re.sub(r'#','',sozder)
    sozderler_clean=[]
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    sozder_tokens = tokenizer.tokenize(sozder)
    for word in sozder_tokens:
            if(word not in string.punctuation):  # remove punctuation
                stem_word1 = stemmer.stem(word)  # stemming word
                sozderler_clean.append(stem_word1)

    return sozderler_clean

def lookup(freqs, word, label):
   
    n = 0  # freqs.get((word, label), 0)

    pair = (word, label)
    if (pair in freqs):
        n = freqs[pair]

    return n
