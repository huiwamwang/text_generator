"""Second stage of the 'Text Generator' project.
We are taking text corpus as an input, then create
bigrams from the tokenized corpus, and output results"""
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
# print(f"Number of bigrams: {len(my_bigrams)}")
bigrams_dict = {}
for head, tail in my_bigrams:
    bigrams_dict.setdefault(head, []).append(tail)
for k, v in bigrams_dict.items():
    print(k, v)
freq_dict = {}
for k, v in bigrams_dict.items():
    freq_dict[k] = Counter(v)
for k, v in freq_dict.items():
    print(f"Head: {k}")
    for i, j in v.items():
        print(f"Tail: {i}\tCount: {j}")


"""At last we create the loop, where we output element of bigram list by index from user's input.
As well we check for possible Errors, and exit when use types 'exit'.
"""
while True:
    user_input = input()
    if user_input == 'exit':
        break
    print(f"Head: {user_input}")
    """try:"""
        # print(f"Head: {my_bigrams[int(user_input)][0]}\tTail: {my_bigrams[int(user_input)][1]}")
    print(freq_dict[user_input])
    for key, value in freq_dict[user_input].items():
        print(f"Tail: {key}\tCount: {value}")
    """except:
        print("Index Error. Please input an integer that is in the range of the corpus.")"""
"""    except ValueError:
        print("Typ Error. Please input an integer.")"""
