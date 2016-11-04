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

label_numbers = [1, 2, 3, 4, 5, 6]
labels = ["Male NN", "Male JJ", "Male VB", "Female NN", "Female JJ", "Female VB"]
count = [0, 0, 0, 0, 0, 0]
maleTotal = 0.0
femaleTotal = 0.0

# Generate lists of nouns and adjectives
for x in tagged_Male:
    maleTotal = maleTotal + 1
    sub = x[1][:2]
    if sub == 'NN' or sub == 'JJ' or sub == 'VB':
        male_words += ' '
        male_words += x[0]
        if sub == 'NN':
            count[0] = count[0] + 1
        elif sub == 'JJ':
            count[1] = count[1] + 1
        else:
            count[2] = count[2] + 2

for y in tagged_Female:
    femaleTotal = femaleTotal + 1
    sub = y[1][:2]
    if sub == 'NN' or sub == 'JJ' or sub == 'VB':
        female_words += ' '
        female_words += y[1]
        if sub == 'NN':
            count[3] = count[3] + 1
        elif sub == 'JJ':
            count[4] = count[4] + 1
        else:
            count[5] = count[5] + 1

# Calculate percentages of words are nouns or adjectives
count[0] = count[0]/maleTotal*100
count[1] = count[1]/maleTotal*100
count[2] = count[2]/femaleTotal*100
count[3] = count[3]/femaleTotal*100

# Show bar graph of noun and adj percentages
plt.bar(label_numbers, count, align='center')
plt.xticks(label_numbers, labels)
plt.ylim([0,100])
plt.show()

#man_mask = np.array(Image.open(path.join(d, "man.jpg")))

# Generate wordcloud images
#maleWordCloud = WordCloud(max_words=30, mask=man_mask).generate(male_words)
maleWordCloud = WordCloud(max_words = 100).generate(male_words)
femaleWordCloud = WordCloud(background_color="white", max_words = 100).generate(femaleText)

# Display images
plt.imshow(maleWordCloud)
plt.axis("off")
plt.show()
plt.imshow(femaleWordCloud)
plt.axis("off")
plt.show()
