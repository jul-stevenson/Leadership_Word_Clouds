#!/usr/bin/env python
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read text
text = open(path.join(d, 'male.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display image
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
