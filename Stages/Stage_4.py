"""Forth stage of the 'Text Generator' project.
We are taking text corpus as an input, then create
bigrams from the tokenized corpus, sort them in 'freq_dict' dictionary with
heads as keys, and list of tails as values. After that we randomly choose
the first word of the sentence, and the second word will be predicted by
looking up the first word of the chain in the model and choosing the most
probable next word from the set of possible follow-ups. This step is repeated
10 times (10 words in 1 sentence). We also print 10 sentences.
"""
from nltk import WhitespaceTokenizer
from nltk.util import bigrams
from collections import Counter
import random

"""First we open file and tokenize it"""
with open(input(), 'r', encoding='utf-8') as file:
    corpus = WhitespaceTokenizer().tokenize(file.read())

"""Then we make a bigram and organize a dictionary in fallowing manner:
key is a head of bigram, and values are all the tails for it.
"""
my_bigrams = list(bigrams(corpus))
bigrams_dict = {}
for head, tail in my_bigrams:
    bigrams_dict.setdefault(head, []).append(tail)

"""Then we create new dictionary: key is a head, and values is a dictionary,
with tails as keys and their count as values
"""
freq_dict = {}
for head, tails in bigrams_dict.items():
    freq_dict[head] = Counter(tails)


def random_sentence():
    """This is a function, which when called will:
    1. Randomly choose the 'start_word' from our 'corpus'.
    2. Will use this word to find all possible tails and their weights.
    3. Choose one of these tails using random.choices() method.
    4. Append the list 'sentence' with obtained value.
    5. Increase counter count.
    6. Repeat 10 times."""
    sentence = []
    start_word = random.choice(corpus)
    counter = 0
    while counter < 10:
        start_word = random.choices(list(freq_dict[start_word].keys()), list(freq_dict[start_word].values()))[0]
        sentence.append(start_word)
        counter += 1
    return ' '.join(sentence)


"""We print 10 sentences, by calling 'random_sentence' function 10 times"""
lines = 0
while lines < 10:
    print(random_sentence())
    lines += 1
