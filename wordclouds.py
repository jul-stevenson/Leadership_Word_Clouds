#!/usr/bin/env python
from os import path
from nltk import *
from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

label_numbers = [1, 2, 3, 4]
labels = ["Male NN", "Male JJ", "Female NN", "Female JJ"]
count = [0, 0, 0, 0]

# Generate lists of nouns and adjectives
for x in tagged_Male:
    if x[1] == 'NN' or x[1] == 'JJ':
        male_words += ' '
        male_words += x[0]
        if x[1] == 'NN':
            count[0] = count[0] + 1
        else:
            count[1] = count[1] + 1

for y in tagged_Female:
    if y[1] == 'NN' or x[1] == 'JJ':
        female_words += ' '
        female_words += y[1]
        if y[1] == 'NN':
            count[2] = count[2] + 1
        else:
            count[3] = count[3] + 1

plt.bar(label_numbers, count, align='center')
plt.xticks(label_numbers, labels)
plt.show()

man_mask = np.array(Image.open(path.join(d, "man.jpg")))

# Generate wordcloud images
maleWordCloud = WordCloud(max_words=30, mask=man_mask).generate(male_words)
femaleWordCloud = WordCloud(background_color="white", max_words=30).generate(femaleText)

# Display images
plt.imshow(maleWordCloud)
plt.axis("off")
plt.show()
plt.imshow(femaleWordCloud)
plt.axis("off")
plt.show()
