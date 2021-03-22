"""First stage of the 'Text Generator' project.
We are taking text corpus as an input, and then
print statistics of it."""
from nltk import WhitespaceTokenizer

"""First we open file and tokenize it"""
with open(input(), 'r', encoding='utf-8') as file:
    corpus = WhitespaceTokenizer().tokenize(file.read())

"""Then we print all the statistics"""
print(f"Corpus statistics\nAll tokens: {len(corpus)}\nUnique tokens: {len(set(corpus))}")

"""At last we create the loop, where we output corpus element by index from user's input.
As well we check for possible Errors, and exit when use types 'exit'."""
while True:
    user_input = input()
    if user_input == 'exit':
        break
    try:
        print(corpus[int(user_input)])
    except IndexError:
        print("Index Error. Please input an integer that is in the range of the corpus.")
    except ValueError:
        print("Type Error. Please input an integer.")
