#!/usr/bin/env python
from os import path
from nltk import *
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)

# Read texts
maleText = open(path.join(d, 'male.txt')).read()
femaleText = open(path.join(d, 'female.txt')).read()

maleTokens = word_tokenize(maleText)
femaleTokens = word_tokenize(femaleText)

tagged_Male = pos_tag(maleTokens)
tagged_Female = pos_tag(femaleTokens)

male_words = ''
female_words = ''

# Generate lists of nouns and adjectives
for x in tagged_Male:
    if x[1] == 'NN' or x[1] == 'JJ':
        male_words += ' '
        male_words += x[0]

for y in tagged_Female:
    if y[1] == 'NN' or x[1] == 'JJ':
        female_words += ' '
        female_words += y[1]


# Generate wordcloud images
maleWordCloud = WordCloud().generate(male_words)
femaleWordCloud = WordCloud().generate(femaleText)

# Display images
plt.imshow(maleWordCloud)
plt.axis("off")
plt.show()
plt.imshow(femaleWordCloud)
plt.axis("off")
plt.show()
