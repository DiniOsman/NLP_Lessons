from nltk.book import *

def lexical_diversity(text):
    return len(text) / len(set(text))
print(lexical_diversity(text3))

def  percentage(count, total):
    return 100 * count / total

sent1 = ["Call", "Me", "Ishmael", '.']
print(percentage(4, 5))
print(lexical_diversity(text3))
print(lexical_diversity(text5))
print(percentage(text4.count('a'), len(text4)))
print(lexical_diversity(sent1))