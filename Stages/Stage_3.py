"""Third stage of the 'Text Generator' project.
We are taking text corpus as an input, then create
bigrams from the tokenized corpus, sort them in dictionary with
heads as keys, and list of tails as values, and than output results
based on key from user input
"""
from nltk import WhitespaceTokenizer
from nltk.util import bigrams
from collections import Counter

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

"""At last we create the loop, where we output element from our 'freq_dict',
by the key from user's input. As well we check for possible Errors, 
and exit when use types 'exit'.
"""
while True:
    user_input = input()
    if user_input == 'exit':
        break
    print(f"Head: {user_input}")
    try:
        for tail, count in freq_dict[user_input].most_common(7):
            print(f"Tail: {tail}\t\tCount: {count}")
    except KeyError:
        print("The requested word is not in the model. Please input another word.")
