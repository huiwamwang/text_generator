"""Second stage of the 'Text Generator' project.
We are taking text corpus as an input, then create
bigrams from the tokenized corpus, and output results"""
from nltk import WhitespaceTokenizer
from nltk.util import bigrams

"""First we open file and tokenize it"""
with open(input(), 'r', encoding='utf-8') as file:
    corpus = WhitespaceTokenizer().tokenize(file.read())

"""Then we print all the statistics"""
my_bigrams = list(bigrams(corpus))
print(f"Number of bigrams: {len(my_bigrams)}")

"""At last we create the loop, where we output element of bigram list by index from user's input.
As well we check for possible Errors, and exit when use types 'exit'."""
while True:
    user_input = input()
    if user_input == 'exit':
        break
    try:
        print(f"Head: {my_bigrams[int(user_input)][0]}\tTail: {my_bigrams[int(user_input)][1]}")
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
    except ValueError:
        print("Typ Error. Please input an integer.")
