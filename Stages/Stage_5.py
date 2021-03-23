"""Fifth stage of the 'Text Generator' project.
We are taking text corpus as an input, then create
bigrams from the tokenized corpus, sort them in 'freq_dict' dictionary with
heads as keys, and list of tails as values. After that we choose
the first word of the sentence: it should starts with capital letter, and
can't ends with a '?!.'. Second and the rest of the words will be predicted by
looking up the first word of the chain in the model and choosing the most
probable next word from the set of possible follow-ups. This step is repeated
till the new word ends with a '!?.', if length of sentence is long as 5 or more tokens.
We also print 10 sentences.
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
    1. Choose the 'start_word' from our 'corpus', so it's starts with capital letter, and not ends with punctuation.
    2. Will use this word to find all possible tails and their weights.
    3. Choose one of these tails using random.choices() method.
    4. Append the list 'sentence' with obtained value.
    5. Loop ends after first tail with '!?.' if 'len(sentence)' is >= 5.
    6. Repeat 10 times.
    """

    def first_word_function():
        """Loop through choosing first word, till it start with capital letter, and not ends with '!?.'"""
        first_word = random.choice(corpus)
        while first_word[-1] in '!.?' or first_word[0].islower() or not first_word[0].isalpha():
            first_word = random.choice(corpus)
        return first_word

    sentence = []
    start_word = first_word_function()
    sentence.append(start_word)
    while True:
        start_word = random.choices(list(freq_dict[start_word].keys()), list(freq_dict[start_word].values()))[0]
        sentence.append(start_word)
        if len(sentence) >= 5 and start_word[-1] in '!.?':
            break
    return ' '.join(sentence)


"""We print 10 sentences, by calling 'random_sentence' function 10 times"""
lines = 0
while lines < 10:
    print(random_sentence())
    lines += 1
