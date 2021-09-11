from nltk.book import *
#sent1 = ["Call", "Me", "Ishmael", '.']
#print(len(sent1))

#fdist1 = FreqDist(text1)
#print(fdist1)
#vocabulary1 = list(fdist1.keys())
#print(vocabulary1[:50])
#print(fdist1.hapaxes())
#print(fdist1.plot(50, cumulative = True))
v = set(text1)
long_words = [w for w in v if len(w) > 15]
print(sorted(long_words))
 
