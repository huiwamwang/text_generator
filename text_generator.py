"""Last stage of the 'Text Generator' project.

***BLOCK 1***
We are taking text input with the name of the file with training word dataset,
open the file and tokenize it with 'WhitespaceTokenizer()' - basically
.split() function.

***BLOCK 2***
From the corpus, we create a list of trigrams.

***BLOCK 3***
We create a list of trigrams from the tokenized corpus, and sort them
in 'trigrams_dict' dictionary:
1. Keys: First two elements in the trigram, heads. Being saved as a tuple.
2. Values: All variations of the 3rd element, tail, fallowing the first two. Saved as a list.

***BLOCK 4***
We count the repetitions of tail element. For this, we create new dictionary - 'freq_dict',
and add heads (keys from 'trigrams_dict') as new keys, and as value, create embedded dictionary.
In it, we put tails as keys, and their count as values.

***BLOCK 5***
We create function 'random_sentence()' which choose the first head, then choose the tail,
and then iterate till count 5 word in the new sentence, and the first word with ends on '?!.'.

***BLOCK 6***
Loop through the function 10 times.
"""
from nltk import WhitespaceTokenizer
from nltk.util import trigrams
from collections import Counter
import random

"""***BLOCK 1***"""
with open(input(), 'r', encoding='utf-8') as file:
    corpus = WhitespaceTokenizer().tokenize(file.read())

"""***BLOCK 2***"""
my_trigrams = list(trigrams(corpus))

"""***BLOCK 3***"""
trigrams_dict = {}
for head_one, head_two, tail in my_trigrams:
    trigrams_dict.setdefault((head_one, head_two), []).append(tail)

"""***BLOCK 4***"""
freq_dict = {}
for head, tails in trigrams_dict.items():
    freq_dict[head] = Counter(tails)


"""***BLOCK 5***"""
def random_sentence():

    """This is a function, which when called will:
    1. Choose the 'start_word' by calling sub function 'first_word_function()'.
    2. Append it in the list 'sentence'.
    3. Choose the 'third_word' variable by calling random.choices() of all tails
    in the 'freq_dict' dictionary by the tuple of two previous words.
    4. Repeat step 3 till our 'sentence' list have 5 or more words, and last element
    is ending with '!?.'
    5. Repeat 10 times.
    """

    def first_word_function():
        """Loop through the keys of 'freq_dict', till the first of them will start
        with a capital letter, and not ends with '!?.'"""
        first_word = random.choice([list(i) for i in freq_dict.keys()])
        while first_word[0][-1] in '!.?' or first_word[0][0].islower() or not first_word[0][0].isalpha():
            first_word = random.choice([list(i) for i in freq_dict.keys()])
        return first_word

    sentence = []
    start_word = first_word_function()
    sentence.append(start_word)
    while True:
        start_word_tuple = tuple(start_word)
        third_word = random.choices(list(freq_dict[start_word_tuple].keys()),
                                    list(freq_dict[start_word_tuple].values()))
        sentence.append(third_word)
        start_word = [start_word[1], ''.join(third_word)]
        if len(sentence) >= 4 and third_word[0][-1] in '!.?':
            break
    return ' '.join([' '.join(i) for i in sentence])


"""***BLOCK 6***"""
lines = 0
while lines < 10:
    print(random_sentence())
    lines += 1
